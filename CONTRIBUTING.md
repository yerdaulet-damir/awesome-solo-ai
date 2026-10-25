# Contributing to Awesome Solo AI

Help someone complete a task with AI tools or coding agents. Publish a guide, skill reference or playbook, improve an existing page, or recommend a resource you have used. Recommendations are reviewed for reader value; submitting one does not guarantee a listing.

## Start with something small

First-time contributors and new projects are welcome. There is no minimum star count, follower count or project age. A small example you have run is enough to start.

| Contribution | Where it goes | What to include |
| --- | --- | --- |
| Correction or worked example | An existing guide, skill reference or playbook | The problem, what you tried and how you checked the fix |
| Guide | `guides/` | One task, setup, steps, expected result and limitations. [Template](.github/CONTRIBUTION_TEMPLATES/guide.md) |
| Skill reference | `skills/` | Source/license, supported agents, install/use steps and a tested example. [Template](.github/CONTRIBUTION_TEMPLATES/skill.md) |
| Playbook | `playbooks/` | A complete workflow, prompts/config, costs, checks and failure cases. [Template](.github/CONTRIBUTION_TEMPLATES/playbook.md) |
| Tool, MCP server or agent recommendation | The relevant catalog section and `llms.txt` | A task you used it for, evidence it works, limitations and its difference from an existing option |

Browse the [guides](guides/README.md), [skills](skills/README.md) and [playbooks](playbooks/README.md) first. Extending an existing page is welcome. You do not need to write a whole tutorial to correct one instruction.

## What a reader should get

- A specific task and enough detail to repeat the useful part: inputs, setup, commands or prompts, and an expected result.
- An honest account of what you tested, when you tested it and what you could not verify. Describe failures as failures.
- Links to primary documentation, source code and licenses. State important pricing, free-tier and access limits beside the relevant step.
- For skills and agents, name the supported agent and the files, scripts, permissions and external services involved. Keep credentials out of examples.

Use the structure that fits the contribution. A correction needs a concise explanation and a check; a workflow needs enough steps to reproduce it. AI-assisted writing and code are welcome. The submitter is responsible for checking the result and reviewing the final diff.

## Recommending your own product

Disclose your relationship to the product. Show a working example and explain a concrete difference from resources already listed. A landing page and a neutral sentence alone do not establish usefulness.

A walkthrough using your product is welcome if it teaches a reusable task, identifies prerequisites and costs, and explains where other options fit. Maintainers may keep the example in a guide without adding a separate catalog entry. A thin tutorial whose only purpose is another product link will be declined.

You do not need to make an unrelated contribution to qualify. One useful correction, example or workflow can be the entire PR. Small and new tools are eligible when their usefulness can be checked.

## Keep discovery in sync

1. Add new pages to the relevant directory index: `guides/README.md`, `skills/README.md` or `playbooks/README.md`.
2. Add the page to the matching section of the root `llms.txt`, using an absolute URL and a factual description. For a tool listing, update both the root README and `llms.txt`.
3. Keep the root README's task routes selective. A page can be published in its directory and agent index without a homepage feature.
4. If you change the root `llms.txt` or frontend guide, run `python3 scripts/build-frontend-guide.py`, then `python3 scripts/build-frontend-guide.py --check`. Commit generated files with their sources. See [publishing instructions](scripts/README.md).
5. If you change this contribution guide, run `python3 scripts/build-contributor-page.py` and `python3 scripts/build-contributor-page.py --check` to update the website's copy.

Tool flags mean: API = public developer API; MCP = official MCP server; Free = usable recurring free tier; Open = open-source implementation or open weights. Distinguish a one-time trial from a free tier, paid MCP access from a free web app, and an open SDK from a closed service.

## Submit and review

Open a focused PR such as `Fix guide: <step>`, `Add skill: <task>` or `Add playbook: <workflow>`, and complete the template. For a larger idea, [propose it first](https://github.com/yerdaulet-damir/awesome-solo-ai/issues/new?template=share-a-contribution.yml). Issues are proposals, not automatic listings.

Maintainers check whether the contribution works, fits the library, adds something distinct and respects sources. They may request changes, suggest an existing page to improve, or decline a redundant submission. Reviews focus on the work, not the popularity of its author. A merge publishes the contribution in this repository and preserves its GitHub authorship history.

The repository uses [CC0](LICENSE). Submit only material you can publish under those terms. Link to third-party code or skills under their own licenses; do not copy them here unless their terms permit it and required notices are preserved.

## Support and sharing

If this library helped you, a star is much appreciated. Fork it to adapt a workflow or contribute, and link to the specific guide when sharing what you built. Stars, forks, follows and promotion are optional and do not affect review decisions.

If you publish a walkthrough that uses this library, a source link helps readers find the setup and corrections. You can use this short credit:

```markdown
Resources and workflow notes: [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai).
```

## We decline

- Duplicate directories, generic wrappers or promotional listings without a distinct use case and a working example.
- Invented test results, unchecked generated instructions, copied material without permission, or unsupported claims about adoption or earnings.
- Broken resources and hidden access requirements, costs or affiliations.
- Paid placement in the curated catalog. Sponsorship must be labeled separately.
