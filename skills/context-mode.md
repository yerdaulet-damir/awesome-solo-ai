# context-mode — keep your session alive through shell noise and resets

> The sessions that used to die at 30 minutes now run for hours.

**Install:** `claude skill add mksglu/context-mode`  
**Stars:** ~8k  
**License:** MIT

## What is the context-mode skill?

**context-mode is a Claude Code skill that filters low-signal shell output from the active context window and rebuilds the full session state after a Claude reset, so long implementation sessions don't collapse halfway through a task.** It addresses two separate failure modes that solo builders hit constantly: context pollution from verbose terminal output, and the cold-start problem when Claude's memory clears mid-session.

## Why solo builders use it

A typical long session generates a lot of noise before it generates a working feature: npm install logs, test runner output, repeated git status calls, shell errors, incremental compile output. None of that is useful context for writing the next file. All of it counts against the window. context-mode intercepts that noise at the source and keeps the context window reserved for the information that actually shapes decisions — the plan, the current file, the task state.

The reset recovery is the other half. When Claude's context fills and resets, the default behavior is to start over. You re-explain the project, re-state the goal, re-orient the agent. That can cost twenty minutes of a session. context-mode serializes the relevant session state before a reset and restores it on the other side, so the agent picks up where it left off rather than greeting you like a stranger.

Together the two mechanisms mean a focused solo build session — the kind where you're heads-down implementing a feature over three or four hours — actually survives intact rather than fragmenting every time the context fills.

## Example

```
/context-mode on
/task implement the CSV export feature end-to-end
```

Shell noise from the build pipeline is filtered; if Claude resets mid-task, state is restored automatically on the next turn.

## Pairs well with

- [caveman](caveman.md) — context-mode filters input noise; caveman cuts output tokens; run both for maximum session length
- [superpowers](superpowers.md) — superpowers writes the plan upfront; context-mode ensures it survives long enough to execute it

## Source

[github.com/mksglu/context-mode](https://github.com/mksglu/context-mode)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
