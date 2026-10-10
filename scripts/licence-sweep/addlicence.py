#!/usr/bin/env python3
"""Step 1 of the licence sweep: add a LICENSE to each unlicensed V-Sekai-fire original.

Reads .cache/repos.json (scripts/fetch.py). Targets: public, non-archived, non-fork repos whose
licenseInfo is empty. For each it makes a sparse, shallow clone (LICENSE and README.md only),
writes the licence chosen in SPDX (default MIT), rewrites the README "## Licence" section to
point at it (keeping sentences about vendored or third-party content), and commits.

Usage: GH_TOKEN=... python3 addlicence.py [--push] [names...]
  --push   push each commit to an `add-licence` branch. The org ruleset forbids direct pushes
           to main (PR + prek/test checks required), so step 2 (waves.py) opens and merges PRs.
Writes .cache/licence-sweep/todo.json: the repos with a pushed add-licence branch.
"""
import json, os, re, subprocess, sys, datetime

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
CACHE = os.environ.get("AWESOME_DATA") or os.path.join(REPO, ".cache")
HERE = os.path.join(CACHE, "licence-sweep")
WORK = os.path.join(HERE, "clones")
os.makedirs(WORK, exist_ok=True)
TOKEN = os.environ["GH_TOKEN"]
PUSH = "--push" in sys.argv
ONLY = [a for a in sys.argv[1:] if not a.startswith("--")]
HOLDER = "K. S. Ernest (iFire) Lee and contributors"
YEAR = datetime.date.today().year

SKIP = {
    "repository-riscv64-sysroot": "redistributed glibc/libgcc/libstdc++ binaries under LGPL/GPL; no single licence fits",
    "interactor-tool-walk-the-dog": "upstream research code (PeizhuoLi/walk-the-dog), which has no licence to inherit",
    # Decided by hand after reading each README "## Licence" section and the JSON records of the fbx fixtures.
}
SPDX = {
    **{n: "CC0-1.0" for n in ["datasource-dataset-unslop-good", "interactor-test-fbx-kenney", "interactor-test-fbx-quaternius",
                              "interactor-test-fbx-arm-pulser", "interactor-test-fbx-opengameart", "interactor-test-fbx-polyhaven",
                              "interactor-test-fbx-rug", "interactor-test-fbx-thebasemesh"]},
    **{n: "CC-BY-4.0" for n in ["interactor-test-fbx-sketchfab-01", "interactor-test-fbx-sketchfab-03",
                                "interactor-test-fbx-sketchfab-04", "interactor-test-fbx-github"]},
    **{n: "CC-BY-SA-4.0" for n in ["interactor-test-fbx", "interactor-test-fbx-mocap-market"]},
    **{n: "Apache-2.0" for n in ["datasource-dataset-architext-v1", "interactor-fire-architext-v2", "interactor-authority",
                                 "interactor-elixir-enet", "entities-khr-interactivity-samples", "interactor-crowd"]},
}
NAMES = {"MIT": "MIT", "Apache-2.0": "Apache-2.0", "CC0-1.0": "CC0 1.0", "CC-BY-4.0": "CC BY 4.0", "CC-BY-SA-4.0": "CC BY-SA 4.0"}

def sh(*a, cwd=None, check=True):
    return subprocess.run(a, cwd=cwd, check=check, capture_output=True, text=True)

def licence_text(spdx):
    cache = os.path.join(HERE, f"lic-{spdx}.txt")
    if not os.path.exists(cache):
        if spdx in ("MIT", "Apache-2.0", "CC0-1.0"):
            body = json.loads(sh("gh", "api", f"licenses/{spdx.lower()}").stdout)["body"]
        else:
            url = {"CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/legalcode.txt",
                   "CC-BY-SA-4.0": "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt"}[spdx]
            body = sh("curl", "-fsSL", url).stdout
        open(cache, "w").write(body)
    t = open(cache).read()
    if spdx == "MIT":
        t = t.replace("[year]", str(YEAR)).replace("[fullname]", HOLDER)
    return t.rstrip() + "\n"

DROP = re.compile(r"no (repository[- ]wide |top-level )?licen|not stated|states? no|does not state|has no|no `?LICENSE|carries no|adds none|"
                  r"no other licen|^Not stated|^There is no|no licence file|SPDX header|package metadata|belong here|"
                  r"^(MIT|Apache|CC0|MIT OR)\b|mix\.exs", re.I)
KEEP = re.compile(r"vendor|third|upstream|addon|weight|checkpoint|model|\bart\b|asset|submodule|bundled|sample|avatar|"
                  r"reference doc|record|binar|tree|author|credit|clip", re.I)

def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z`\[])", text) if s]

def new_section(spdx, body):
    kept = [s for s in sentences(body) if KEEP.search(s) and not DROP.search(s)]
    head = f"{NAMES[spdx]}. See [LICENSE](LICENSE)."
    return head + (" " + " ".join(kept) if kept else "")

def fix_readme(path, spdx):
    if not os.path.exists(path):
        return None
    src = open(path).read()
    m = re.search(r"(^##\s+Licen[cs]e\s*\n)(.*?)(?=^##\s|\Z)", src, re.S | re.M)
    if not m:
        return None
    sec = new_section(spdx, m.group(2))
    head = m.group(1).rstrip() + "\n\n"
    out = src[:m.start(1)] + head + sec + "\n" + ("\n" if m.end(2) < len(src) else "") + src[m.end(2):]
    open(path, "w").write(out)
    return sec

def main():
    repos = json.load(open(os.path.join(CACHE, "repos.json")))
    targets = sorted(r["name"] for r in repos if not r["isFork"] and not r["isArchived"] and not r.get("licenseInfo"))
    results = []
    for n in targets:
        if ONLY and n not in ONLY:
            continue
        if n in SKIP:
            results.append((n, "skipped", SKIP[n])); continue
        spdx = SPDX.get(n, "MIT")
        d = os.path.join(WORK, n)
        if not os.path.isdir(d):
            r = sh("git", "-c", "credential.helper=", "-c", f"credential.helper=!f(){{ echo username=x-access-token; echo password={TOKEN}; }}; f",
                   "clone", "-q", "--depth", "1", "--filter=blob:none", "--no-checkout", f"https://github.com/V-Sekai-fire/{n}.git", d, check=False)
            if r.returncode:
                results.append((n, "clone-failed", r.stderr.strip()[-200:])); continue
            sh("git", "sparse-checkout", "set", "--no-cone", "/LICENSE", "/README.md", cwd=d)
            sh("git", "checkout", "-q", cwd=d)
        if os.path.exists(os.path.join(d, "LICENSE")):
            results.append((n, "has-LICENSE", "")); continue
        open(os.path.join(d, "LICENSE"), "w").write(licence_text(spdx))
        sec = fix_readme(os.path.join(d, "README.md"), spdx)
        sh("git", "add", "-A", cwd=d)
        msg = f"Add the {NAMES[spdx]} licence"
        sh("git", "commit", "-q", "-m", msg, cwd=d)
        status = "committed"
        if PUSH:
            r = sh("git", "-c", "credential.helper=", "-c", f"credential.helper=!f(){{ echo username=x-access-token; echo password={TOKEN}; }}; f",
                   "push", "-q", "-f", "origin", "HEAD:refs/heads/add-licence", cwd=d, check=False)
            status = "pushed" if r.returncode == 0 else "push-failed: " + r.stderr.strip()[-200:]
        results.append((n, status, f"{spdx} | {sec}"))
        print(n, status, spdx, "|", sec, flush=True)
    json.dump(results, open(os.path.join(HERE, "addlicence-results.json"), "w"), indent=1)
    json.dump([r[0] for r in results if r[1] == "pushed"], open(os.path.join(HERE, "todo.json"), "w"), indent=1)
    for r in results:
        if r[1] not in ("pushed", "committed"):
            print(*r)

main()
