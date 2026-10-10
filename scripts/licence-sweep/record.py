#!/usr/bin/env python3
"""Write docs/licence-sweep-record.md from the sweep's state files (one row per repository)."""
import json, os

REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
HERE = os.path.join(os.environ.get("AWESOME_DATA") or os.path.join(REPO, ".cache"), "licence-sweep")
results = json.load(open(os.path.join(HERE, "addlicence-results.json")))
waves = json.load(open(os.path.join(HERE, "waves-state.json")))
ORG = "https://github.com/V-Sekai-fire"

rows = []
for name, status, info in sorted(results, key=lambda r: r[0].lower()):
    spdx = info.split(" | ")[0] if " | " in info else ""
    w = waves.get(name)
    if status == "skipped":
        how = f"not licensed: {info}"
    elif w and w.get("pr"):
        how = f"[PR #{w['pr']}]({ORG}/{name}/pull/{w['pr']}) {w['state']}"
    elif status == "pushed-main":
        how = "pushed to main"
    else:
        how = status
    rows.append(f"- [{name}]({ORG}/{name}) - {spdx or '-'} - {how}")

out = ["# Licence sweep record", "",
       "One line per repository: licence added, and how it landed. See [licence-sweep.md](licence-sweep.md) for the decisions.", ""]
out += rows
open(os.path.join(REPO, "docs", "licence-sweep-record.md"), "w").write("\n".join(out) + "\n")
print(len(rows), "rows")
