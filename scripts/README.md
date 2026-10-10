# Scripts

The README list is generated. Edit the rules here, not the list by hand.

## Rebuild the list

```sh
read -r token expires_at < <(bao-mint-github V-Sekai-fire)
GH_TOKEN=$token python3 scripts/fetch.py   # public repos only, into .cache/ (git-ignored)
python3 scripts/build.py --check           # section membership; fails on a repo no rule places
python3 scripts/build.py                   # writes README.md
```

`build.py` holds the decisions:

- `SECTIONS`: subject groups and the name rules that fill them. First match wins. A new repository that matches no rule stops the build, so every new repository gets a deliberate place.
- `OVERRIDES`: hand-written descriptions. Use one when the GitHub description is missing, is README boilerplate, or makes a speed, size or "SOTA" claim with no benchmark.
- Descriptions otherwise come from the GitHub description, or the first sentence of the README when there is none.
- Forks go in the collapsed "Forks we maintain" list with their parent.
- Private repositories are never fetched.

## Licence sweep

`scripts/licence-sweep/` added a licence to every unlicensed repository. [docs/licence-sweep.md](../docs/licence-sweep.md) records the decisions; [docs/licence-sweep-record.md](../docs/licence-sweep-record.md) lists every repository and its PR.

```sh
GH_TOKEN=$token python3 scripts/licence-sweep/addlicence.py --push   # commit LICENSE + README section to add-licence branches
python3 scripts/licence-sweep/waves.py                               # PRs in waves of 18, merge on green
python3 scripts/licence-sweep/record.py                              # write docs/licence-sweep-record.md
```
