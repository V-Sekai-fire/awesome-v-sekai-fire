#!/usr/bin/env python3
"""Step 2 of the licence sweep: land the add-licence branches as PRs in waves.

Opens at most WAVE PRs at once through the ~/.local/bin/gh wrapper, which takes a pr-credit for
every `gh pr create` (25 credits org-wide, shared with other work). Merges each PR once its checks
pass; a PR with no checks merges after 3 minutes. A repo with a merge queue gets `gh pr merge`
without --delete-branch (gh refuses that flag there). The next wave opens only after the current
one drains. pr-credit or rate-limit errors are transient: it waits and retries.

State in .cache/licence-sweep/waves-state.json: name -> {"pr", "state": open|merged|failed, "note"}.
Resumable. Run exactly one copy: two copies race on the state file.
"""
import json, os, subprocess, time, sys

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
HERE = os.path.join(os.environ.get("AWESOME_DATA") or os.path.join(REPO, ".cache"), "licence-sweep")
STATE = os.path.join(HERE, "waves-state.json")
WAVE = 18
ORG = "V-Sekai-fire"
GH = os.path.expanduser("~/.local/bin/gh")  # wrapper: takes a pr-credit on `pr create`
SKIP = {"repository-riscv64-sysroot", "interactor-tool-walk-the-dog"}

todo = [n for n in json.load(open(os.path.join(HERE, "todo.json"))) if n not in SKIP]
state = json.load(open(STATE)) if os.path.exists(STATE) else {}
_tok = {"t": None, "at": 0}

def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)

def token():
    if time.time() - _tok["at"] > 1800:
        out = subprocess.run(["bao-mint-github", ORG], capture_output=True, text=True).stdout.split()
        if out and len(out[0]) > 100:
            _tok.update(t=out[0], at=time.time())
        elif not _tok["t"]:
            raise SystemExit("bao-mint-github failed")
    return _tok["t"]

def gh(*a):
    env = dict(os.environ, GH_TOKEN=token())
    return subprocess.run([GH, *a], capture_output=True, text=True, env=env)

def save():
    json.dump(state, open(STATE, "w"), indent=1)

def title_body(name):
    msg = subprocess.run(["git", "-C", os.path.join(HERE, "clones", name), "log", "-1", "--format=%s"],
                         capture_output=True, text=True).stdout.strip() or "Add a licence"
    body = ("Adds a LICENSE file so the repository states a free licence, and updates the README licence "
            "section to point at it. Vendored and third-party content keeps its own licence.\n\n"
            "Listed in https://github.com/V-Sekai-fire/awesome-v-sekai-fire.")
    return msg, body

def open_count():
    return sum(1 for v in state.values() if v["state"] == "open")

def create(name):
    t, b = title_body(name)
    r = gh("pr", "create", "-R", f"{ORG}/{name}", "--head", "add-licence", "--title", t, "--body", b)
    if r.returncode != 0:
        if "already exists" in r.stderr:
            r2 = gh("pr", "view", "add-licence", "-R", f"{ORG}/{name}", "--json", "number", "--jq", ".number")
            if r2.returncode == 0:
                state[name] = {"pr": int(r2.stdout), "state": "open"}; save(); return True
        if "no credit" in r.stderr or "pr-credit" in r.stderr or "rate limit" in r.stderr.lower():
            log("pr-credit unavailable or rate-limited; retry later")
            return False
        state[name] = {"pr": None, "state": "failed", "note": r.stderr.strip()[-300:]}; save()
        log("create failed", name, r.stderr.strip()[-200:]); return True
    num = int(r.stdout.strip().rsplit("/", 1)[-1])
    state[name] = {"pr": num, "state": "open"}; save()
    log("opened", name, num)
    return True

def check(name):
    v = state[name]
    r = gh("pr", "view", str(v["pr"]), "-R", f"{ORG}/{name}", "--json", "state,mergeable,statusCheckRollup")
    if r.returncode:
        return
    d = json.loads(r.stdout)
    if d["state"] == "MERGED":
        v["state"] = "merged"; save(); log("merged (already)", name); return
    if d["state"] == "CLOSED":
        v["state"] = "failed"; v["note"] = "closed"; save(); return
    checks = d.get("statusCheckRollup") or []
    concl = [(c.get("conclusion") or c.get("state") or "").upper() for c in checks]
    pending = [c for c in checks if (c.get("status") or "").upper() in ("QUEUED", "IN_PROGRESS", "PENDING", "WAITING")
               or (c.get("state") or "").upper() == "PENDING"]
    if pending:
        return
    bad = [c.get("name") or c.get("context") for c, k in zip(checks, concl) if k in ("FAILURE", "ERROR", "TIMED_OUT", "CANCELLED", "ACTION_REQUIRED")]
    if bad:
        if v.get("note") != "checks failed":
            v["note"] = "checks failed"; v["failed_checks"] = bad; save(); log("checks failed", name, bad)
        v.setdefault("seen_fail", time.time())
        return
    v.pop("seen_fail", None)
    if not checks:
        v.setdefault("nochecks_since", time.time())
        if time.time() - v["nochecks_since"] < 180:
            return
    if v.get("queued"):
        return
    for m in ("--squash", "--merge", "--rebase", "queue"):
        if m == "queue":  # merge queue: no --delete-branch, no method; the queue merges it
            r = gh("pr", "merge", str(v["pr"]), "-R", f"{ORG}/{name}")
            if r.returncode == 0:
                v["queued"] = True; v["note"] = "queued"; save(); log("queued", name); return
            err = r.stderr; break
        r = gh("pr", "merge", str(v["pr"]), "-R", f"{ORG}/{name}", m, "--delete-branch")
        if r.returncode == 0:
            v["state"] = "merged"; v["note"] = m; save(); log("merged", name, m); return
        err = r.stderr
    v["note"] = "merge failed: " + err.strip()[-200:]; save()
    log("merge failed", name, err.strip()[-200:])

def main():
    log(f"{len(todo)} repos; already: {sum(1 for v in state.values() if v['state']=='merged')} merged")
    stall = 0
    while True:
        for name in [n for n, v in state.items() if v["state"] == "open"]:
            check(name)
        pending_new = [n for n in todo if n not in state]
        open_ok = [n for n, v in state.items() if v["state"] == "open" and v.get("note") != "checks failed"]
        # A wave: only open new PRs once the previous wave has drained (failed ones stay open and still count).
        if pending_new and not open_ok:
            while pending_new and open_count() < WAVE:
                if not create(pending_new[0]):
                    break
                pending_new.pop(0)
                time.sleep(5)
        live = [n for n, v in state.items() if v["state"] == "open" and v.get("note") != "checks failed"]
        if not pending_new and not live:
            break
        if not live and open_count() >= WAVE:
            log("wave blocked by failed-check PRs; stopping"); break
        time.sleep(60)
    c = {}
    for v in state.values():
        c[v["state"] + ("/" + v["note"] if v["state"] != "merged" and v.get("note") else "")] = c.get(v["state"] + ("/" + v["note"] if v["state"] != "merged" and v.get("note") else ""), 0) + 1
    log("done", json.dumps(c))

main()
