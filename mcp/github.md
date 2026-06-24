# GitHub MCP — repo actions from your agent

> Open issues and PRs, review code, and run repo actions from Claude Code.

## What is the GitHub MCP server?

**The GitHub MCP server lets an AI agent operate your GitHub repositories over the Model Context Protocol** — create and comment on issues, open and review pull requests, read code, and trigger actions. It's GitHub's official server.

## Why it matters for solo builders

A solo builder is also their own PM and reviewer. GitHub MCP folds those chores into the agent: it can file the issue it just discovered, open the PR for the fix, and tie work to your CI — keeping you in flow instead of tab-switching.

## What you can do with it

- Open a PR for a change the agent just made.
- Triage and label issues.
- Read repo context to ground its work.

## Example

> "Open a PR for this fix, link it to issue #42, and request the CI checks."

## Setup

Add the [github-mcp-server](https://github.com/github/github-mcp-server) to your Claude Code MCP config with a GitHub token scoped to your repos.

## Related

- [Ship a SaaS solo with Claude Code](../playbooks/solo-saas-with-claude.md).
- [Playwright MCP](playwright.md) — verify before you open the PR.

## Source

[github.com/github/github-mcp-server](https://github.com/github/github-mcp-server)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
