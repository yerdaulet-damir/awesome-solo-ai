# Agent QA — application testing from your agent

> Run repeatable web and mobile user flows from natural-language test definitions.

## What is Agent QA?

**Agent QA is a TypeScript QA agent for testing web and mobile applications.** It exposes its test-authoring, execution, evidence, and triage operations through an official MCP server, and keeps persistent test memory so repeated flows can adapt to application changes.

## Why it matters for solo builders

A solo builder can keep application checks beside the product instead of maintaining a separate QA system. Agent QA can initialize example tests, validate YAML definitions, exercise browser or mobile flows, and return structured evidence to an MCP-aware coding agent.

## What you can do with it

- Describe a web or mobile user journey as a natural-language test.
- Re-run saved flows and use persistent memory to recover from UI changes.
- Inspect evidence and triage failures from an MCP client, CLI, or local dashboard.

## Example

> "Run the saved signup and checkout flows, then summarize any failed step with its evidence."

## Setup

Agent QA requires Node.js 24 or newer. Install it in the project, initialize a workspace, and start its stdio MCP server:

```bash
npm install -D agent-qa
npx agent-qa init --platform web
npx agent-qa mcp
```

Browser or mobile execution also needs the corresponding runtime and a configured model provider. The current release is source-available under FSL-1.1-ALv2 rather than OSI open source.

## Related

- [Playwright MCP](playwright.md) — direct browser automation without Agent QA's saved test workflow and memory layer.
- [GitHub MCP](github.md) — open an issue or pull request after a failed flow is diagnosed.

## Source

[github.com/vostride/agent-qa](https://github.com/vostride/agent-qa)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
