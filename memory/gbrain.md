# GBrain — the memory layer your coding agent is missing

> Search gives you raw pages. GBrain gives you the answer. Wire it into Claude Code in one command and your agent stops being amnesiac about everything that isn't code.

## What is GBrain?

**GBrain is an agent "brain" — a retrieval and knowledge layer that does synthesis, graph traversal, and gap analysis in one box, so an AI agent can answer from a structured memory instead of raw search results.** You can run a full autonomous agent on top of it, or just plug it into Claude Code or Codex as a supercharged retrieval layer with one command.

It's built and used by **Garry Tan, President & CEO of Y Combinator**, as the production brain behind his own agent deployments — ingesting meetings, emails, and the web into a graph of pages, people, and companies that his agents query autonomously.

## Why it matters for solo builders

A coding agent forgets everything outside the current repo — your past decisions, your contacts, your research, last week's meeting. GBrain gives a solo builder a persistent, queryable memory across all of it, so the agent acts on context you'd otherwise have to re-paste every session. For a one-person operation, that institutional memory is the thing a team would normally hold.

## What it does

- **Synthesis** — returns an answer, not a list of links.
- **Graph traversal** — connects people, companies, and documents.
- **Gap analysis** — surfaces what's missing from what it knows.
- **Agent-native** — run autonomously or wire into Claude Code / Codex as retrieval.

## When to use it

- You want your agent to remember context beyond the codebase (notes, CRM, research, meetings).
- You're building a personal autonomous agent and need a knowledge backbone.

**When not to:** for purely up-to-date *library docs*, a lighter tool like [Context7](../skills/context7.md) is enough.

## Setup

Connect GBrain to Claude Code as a retrieval layer (one-command install — see the repo). Then point your agent at it and it queries the brain for context automatically.

## Related

- [Context7](../skills/context7.md) — narrower: live library docs only.
- [MCP servers](../mcp/README.md) — how agents call external tools.

## Source

[github.com/garrytan/gbrain](https://github.com/garrytan/gbrain)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
