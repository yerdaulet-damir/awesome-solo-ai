# karpathy-skills — verify before you code

> Four rules from Andrej Karpathy that kill Claude's most expensive failure mode: charging ahead on the wrong assumption.

**Install:** `claude skill add multica-ai/andrej-karpathy-skills`  
**Stars:** ~144k  
**License:** MIT

## What is the karpathy-skills skill?

**karpathy-skills is a Claude Code skill that encodes four rules distilled from Andrej Karpathy's coding philosophy: verify assumptions before coding, reach for the minimal solution first, make surgical changes only, and validate every step against the original goal.** It intercepts the most common failure mode in agentic AI — confident, fast, and wrong — before the diff lands.

It became the fastest-growing Claude skill of 2026, reaching ~144,000 stars faster than any other skill in the ecosystem.

## Why solo builders use it

Agentic Claude is optimistic by default. Given an ambiguous prompt it picks an interpretation and runs. The problem is that the interpretation is often wrong, and by the time you notice, you're staring at a large diff that solves the wrong problem. karpathy-skills forces a verification step before any code is written, turning that optimism into a pause-and-confirm.

The "minimal solutions first" rule pairs naturally with solo constraints. When you're the only maintainer, every line you ship is a line you have to understand, debug, and eventually delete. Karpathy's framing — treat code as a liability, not an asset — maps directly onto what it costs a solo builder to carry dead weight across a codebase.

Surgical changes only means the skill blocks the agent from refactoring things you didn't ask it to refactor. That single guardrail prevents the classic Claude session where you asked it to fix a bug and it rewrote three modules.

## Example

```
/karpathy before touching anything, state your assumptions about the current auth flow and wait for me to confirm
```

## Pairs well with

- [ponytail](ponytail.md) — karpathy verifies assumptions and scopes changes; ponytail keeps the resulting code minimal
- [superpowers](superpowers.md) — superpowers handles the plan/test loop; karpathy enforces the goal-validation gate throughout

## Source

[github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
