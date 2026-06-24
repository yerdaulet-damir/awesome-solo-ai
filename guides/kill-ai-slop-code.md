# How to Eliminate AI-Slop Code and Write Production-Grade Code with AI

"AI slop" is code that looks plausible, compiles, and is quietly wrong, bloated, or unmaintainable. Here's the loop senior engineers use to get production code out of an AI agent instead.

## Why agents produce slop

- They optimize for *looking done*, not *being correct*.
- They over-engineer when the scope is vague.
- They invent APIs, duplicate existing helpers, and add dead abstraction.

The fix is process, not a magic prompt.

## The loop

**1. Tighten scope before code.** Make the agent restate the task and list the files it will touch. A wide prompt produces wide slop.

**2. Make it read first.** Force it to read the surrounding code and match existing patterns, naming, and helpers — don't let it write in a vacuum.

**3. Verify-driven, not vibes-driven.** Every change must be proven by running something — a test, the app, a probe. "It should work" is slop. Demand the observed output.

**4. Small diffs, review gates.** One concern per change. Review each diff for: invented APIs, duplicated logic, unhandled errors, and abstraction that isn't paying rent.

**5. Delete on sight.** If the agent added a wrapper, config flag, or "for flexibility" layer nothing uses — cut it. Production code is the minimum that works and reads cleanly.

## A reusable instruction block

Drop this into your `CLAUDE.md` or system prompt:

> Before coding: restate the task and list files you'll change. Read those files and match their style. Make the smallest change that works — no speculative abstraction, no new dependencies without asking. After coding: run it and show me the actual output. If a test or the app didn't run, say so plainly.

## Tools that help

- [Claude Code](../README.md#ai-coding-agents) with a verify step in the loop.
- [Playwright MCP](../README.md#mcp-servers) / [GitHub MCP](../README.md#mcp-servers) so the agent can actually run and check its work.
- A `/code-review` pass on the diff before merge.

## The one-line test

If you can't point at the command whose output proves the change works, it's slop. Find that command first.
