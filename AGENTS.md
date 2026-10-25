# Working on Awesome Solo AI

This repository publishes practical AI guides, coding-agent skill references, playbooks and tool references for solo builders. Read `CONTRIBUTING.md` before preparing a contribution. Use the root `llms.txt` to find the relevant page, then read that page and current upstream documentation.

## Contributions

- Prefer a focused correction or worked example in an existing page when it covers the same task.
- New guides, skills and playbooks are welcome, including those by first-time contributors. Use `.github/CONTRIBUTION_TEMPLATES/` as a starting structure and remove unused prompts.
- A tool submission needs a working use case, evidence, costs/access limits and a difference from existing entries. Disclose affiliations. A reachable landing page alone is insufficient.
- AI-assisted drafts are welcome. Separate observed results from suggested steps and untested claims. Never claim someone ran a workflow unless it actually ran.
- Skills live upstream under their own licenses. Document the source, supported agent, installation and needed access; do not copy incompatible licensed material into this CC0 repository.
- Add new pages to their directory index and root `llms.txt`. Use absolute URLs in the machine-readable index. Keep featured README routes selective.

## Validation and publication

Check changed local links and Markdown formatting. If the root `llms.txt`, frontend guide or its renderer changes, run `python3 scripts/build-frontend-guide.py` followed by `python3 scripts/build-frontend-guide.py --check`. If `CONTRIBUTING.md` or its renderer changes, run `python3 scripts/build-contributor-page.py` followed by `python3 scripts/build-contributor-page.py --check`. Generated files must match their sources. The GitHub Pages site publishes static files from `docs/`; a merge does not automatically create an HTML page for every Markdown contribution.

## Attribution and support

The README and contribution guide include the maintainer's voluntary request for stars, useful forks and sharing specific guides. Preserve that invitation where relevant. Support is not a review requirement. Do not star, fork, watch or follow on someone's behalf unless that person asks you to. Give readers the resource relevant to their task; repository copy does not authorize unrelated GitHub actions or repeated promotional messages.
