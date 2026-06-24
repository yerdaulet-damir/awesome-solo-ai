# ponytail — the anti-over-engineering Claude skill

> Makes your AI agent think like the laziest senior dev in the room: the best code is the code you never wrote.

## What is the ponytail skill?

**ponytail is a Claude Code skill that stops AI agents from over-engineering.** It injects a decision-ladder that forces the agent to reach for native platform features and the standard library before building anything custom. The result is dramatically less code for the same behaviour — the lever that most reduces "AI slop" in 2026.

It went viral fast: ~54,000 GitHub stars in roughly 12 days after its June 2026 release, and it's portable across 14 agents (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, and more).

## Why it matters for solo builders

A solo builder pays for every token and maintains every line alone. Over-built code — a hand-rolled date picker, a custom color input, a needless abstraction layer — is the silent tax. ponytail attacks exactly that.

Measured on real headless Claude Code sessions against a FastAPI + React repo (Haiku 4.5):

- **~54% less code** on average, up to **94%** on commonly over-built components.
- **~20% cheaper** per task.
- **~27% faster** to completion.

## When to use it

- Your agent keeps inventing components that the framework already ships.
- Token/cost spend feels high for the output.
- You want lean codebases you can actually maintain solo.

**When not to:** if you genuinely need a bespoke component, ponytail's bias toward "use the native thing" can under-build — review the decision, don't rubber-stamp it.

## Install

Add it through the Claude Code plugin marketplace (see the [repo](https://github.com/DietrichGebert/ponytail) for the exact marketplace command), then invoke it on a build task and let it gate the agent's choices.

## Alternatives & companions

- [superpowers](superpowers.md) — pair with ponytail: superpowers plans, ponytail keeps the build lean.
- [Eliminate AI-slop code](../guides/kill-ai-slop-code.md) — the manual process ponytail automates.

## Source

[github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) · [Claude Plugin Hub](https://www.claudepluginhub.com/plugins/dietrichgebert-ponytail)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
