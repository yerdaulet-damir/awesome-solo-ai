# Playwright MCP — give your agent a real browser

> Let Claude Code click, type, and verify in a live browser — for testing, scraping, and proving a change works.

## What is the Playwright MCP server?

**The Playwright MCP server lets an AI agent drive a real browser** — navigate pages, click, fill forms, read the DOM, and screenshot — over the Model Context Protocol. It's Microsoft's official server built on the Playwright automation framework.

## Why it matters for solo builders

This is the difference between an agent that *says* a feature works and one that *shows* it. Wire in Playwright MCP and Claude Code can actually walk through your UI, confirm the button does the thing, and catch breakage before you ship — the verification step that kills [AI-slop code](../guides/kill-ai-slop-code.md).

## What you can do with it

- End-to-end test a feature by describing the user flow.
- Scrape data from pages that need interaction.
- Reproduce a bug the way a user hits it.

## Example

> "Open the signup page, register a test user, and confirm the dashboard loads — screenshot each step."

## Setup

Add the [playwright-mcp](https://github.com/microsoft/playwright-mcp) server to your Claude Code MCP config; it installs the browser on first run.

## Related

- [Ship a SaaS solo with Claude Code](../playbooks/solo-saas-with-claude.md).
- [GitHub MCP](github.md) — open the PR once it's verified.

## Source

[github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
