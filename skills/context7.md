# Context7 — up-to-date library docs for your agent

> Injects current, version-correct documentation so the agent stops hallucinating stale APIs.

## What is Context7?

**Context7 is an MCP-based tool that feeds Claude Code up-to-date documentation for the libraries you're using.** When the agent would otherwise rely on training data that's months old, Context7 pulls the current docs and code examples for the exact library version, so generated code matches the real API.

Built by **Upstash**, it's one of the most-installed context tools in the Claude Code ecosystem (hundreds of thousands of installs).

## Why it matters for solo builders

The most maddening AI-slop bug is confidently-wrong code against an API that changed. A solo builder eats that debugging time alone. Context7 removes a whole class of it by grounding the agent in real, current docs.

## When to use it

- Working with fast-moving libraries (frameworks, SDKs) where signatures drift.
- Any time the agent invents methods or uses deprecated calls.

## Install

Add Context7 as an MCP server in Claude Code (see the [repo](https://github.com/upstash/context7) for the config), then mention a library and the agent will fetch its live docs.

## Source

[github.com/upstash/context7](https://github.com/upstash/context7)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
