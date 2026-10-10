#!/usr/bin/env python3
"""Fetch the public V-Sekai-fire repository data that build.py reads.

Writes into DATA (default: .cache/ beside this repo, git-ignored):
  repos.json        public repos: name, description, language, fork, archived, licence
  forks.json        public forks with their parent
  readme-desc.json  README lead text for repos without a description

Needs a GitHub token in GH_TOKEN (for example `bao-mint-github V-Sekai-fire`).
Private repositories are never fetched, so nothing private can reach the list.
"""
import base64, concurrent.futures as cf, json, os, subprocess, sys

ORG = "V-Sekai-fire"
DATA = os.environ.get("AWESOME_DATA") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".cache")
os.makedirs(DATA, exist_ok=True)

def gh(*a):
    r = subprocess.run(["gh", *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr)
    return r.stdout

FIELDS = "name,description,isArchived,isFork,visibility,primaryLanguage,stargazerCount,pushedAt,url,licenseInfo"
repos = json.loads(gh("repo", "list", ORG, "--limit", "5000", "--visibility", "public", "--json", FIELDS))
forks = json.loads(gh("repo", "list", ORG, "--limit", "5000", "--visibility", "public", "--fork", "--json", "name,parent,description"))

def readme_lead(name):
    r = subprocess.run(["gh", "api", f"repos/{ORG}/{name}/readme", "--jq", ".content"], capture_output=True, text=True)
    if r.returncode:
        return name, None
    lines = base64.b64decode(r.stdout).decode("utf8", "replace").splitlines()
    out = []
    for l in (x.strip() for x in lines):
        if not l or l.startswith(("#", "!", "[!", "<", "```", "|", "---", "===", "[![")):
            continue
        out.append(l)
        if len(" ".join(out)) > 160:
            break
    return name, " ".join(out)[:200]

need = [r["name"] for r in repos if not r["description"] or r["description"].startswith(("Migrated from mirror", "Fork of "))]
with cf.ThreadPoolExecutor(12) as ex:
    desc = dict(ex.map(readme_lead, need))

for fn, obj in (("repos.json", repos), ("forks.json", forks), ("readme-desc.json", desc)):
    json.dump(obj, open(os.path.join(DATA, fn), "w"), indent=1)
print(f"{len(repos)} public repos, {len(forks)} forks, {len(desc)} README leads -> {os.path.abspath(DATA)}")
