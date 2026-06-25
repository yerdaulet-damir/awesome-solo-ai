# caveman — 65% fewer output tokens, same technical accuracy

> Token budget running out before the task is done? Caveman compresses Claude's output without compressing its thinking.

**Install:** `claude skill add JuliusBrussee/caveman`  
**Stars:** ~12k  
**License:** MIT

## What is the caveman skill?

**caveman is a Claude Code skill that strips Claude's natural-language output down to compressed, technically precise prose — cutting output tokens by ~65% while preserving every meaningful piece of information.** It also ships a `/caveman-compress` companion command that shrinks your `CLAUDE.md` context file by roughly 46%, so you get more implementation per dollar and longer effective sessions before the context window fills.

## Why solo builders use it

Claude's default output style is verbose. It explains its reasoning in full paragraphs, restates the problem before solving it, and hedges. All of that is readable in a chat interface; in a long agentic session it is an expensive habit. Every token of explanation is a token not spent on code, and on a long implementation streak the difference compounds — sessions that should last two hours start hitting limits at thirty minutes.

caveman reorients Claude's output toward the person who already understands the codebase and just wants the answer. The agent still thinks through the problem; it just stops narrating that process back to you. The benchmark result — 65% fewer tokens, no accuracy loss — holds up in practice because most of what gets trimmed is ceremony, not information.

The `/caveman-compress` command is worth running once on any `CLAUDE.md` that's grown over time. A file that started as 200 lines of useful context often carries 80 lines of preamble, caveats, and formatting that Claude reads every turn. Compressing it once buys back meaningful context budget for every subsequent session.

## Example

```
/caveman
/task refactor the billing module to support multi-currency
```

With caveman active, Claude skips the three-paragraph preamble and writes code.

## Pairs well with

- [context-mode](context-mode.md) — caveman cuts output tokens; context-mode cuts input noise; together they extend session length substantially

## Source

[github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
