# superpowers — plan-first, test-driven agent workflow

> Stops Claude from charging into code before it understands the task.

## What is the superpowers skill?

**superpowers is a Claude Code skill that imposes a disciplined, plan-first development workflow on the agent.** Instead of jumping straight to code, it runs the agent through brainstorm → isolated worktree → written plan → subagent execution → RED-GREEN-REFACTOR (test-driven) → review. It is one of the most-recommended Claude Code skills of 2026.

Built by **obra** (Jesse Vincent), it's distributed through its own plugin marketplace.

## Why it matters for solo builders

A solo builder has no teammate to catch a half-understood task before it becomes a tangled diff. superpowers forces the planning and testing a senior team would demand, so features arrive correct and reviewable rather than as a pile of plausible code.

## When to use it

- Non-trivial features where getting the approach right matters more than speed.
- Anytime the agent tends to over-reach or skip tests.

Pair with [ponytail](ponytail.md) — superpowers decides *what* to build and tests it; ponytail keeps the build *minimal*.

## Install

```
/plugin marketplace add obra/superpowers-marketplace
```

Then start a feature and let it run the plan → test → review loop.

## Source

[github.com/obra/superpowers](https://github.com/obra/superpowers)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
