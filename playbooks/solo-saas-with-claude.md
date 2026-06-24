# Playbook: Ship a SaaS Solo with Claude Code + MCP

The loop one engineer uses to design, build, verify, and ship a real product with an AI agent — without producing [slop](../guides/kill-ai-slop-code.md).

## Stack

| Layer | Tool |
| --- | --- |
| Coding agent | [Claude Code](../README.md#ai-coding-agents) |
| Browser / test automation | [Playwright MCP](../README.md#mcp-servers) |
| Repo + CI actions | [GitHub MCP](../README.md#mcp-servers) |
| LLM features in-app | [OpenRouter](../README.md#llm-api-routers--aggregators) (one key, swap models) |
| Deploy | [Vercel](https://vercel.com) |
| Glue automations | [n8n](../README.md#automation--agent-frameworks) |

## The build loop

1. **Plan before code.** Have Claude Code restate the feature, list files it'll touch, and surface decisions for you. Approve the plan, not just the diff.
2. **Small vertical slices.** One user-visible capability at a time — auth, then one screen, then one API route. Ship each before the next.
3. **Verify with real tools.** Use [Playwright MCP](../README.md#mcp-servers) so the agent actually clicks through the feature and shows you it works — not "it should work."
4. **Review the diff.** Run a `/code-review` pass; cut invented APIs, duplicated helpers, and abstraction nothing uses.
5. **Ship via [GitHub MCP](../README.md#mcp-servers) + Vercel.** Open the PR, run CI, deploy preview, promote to prod.

## In-app AI without lock-in

Wire app features to [OpenRouter](../README.md#llm-api-routers--aggregators) so you can A/B models and route cheap vs. premium per call. Add [Vercel AI SDK](../README.md#automation--agent-frameworks) for streaming and tool-calling.

## Keep it from drifting

- One `CLAUDE.md` with your conventions; the agent reads it every session.
- A verify step is non-negotiable — see [Eliminate AI-slop code](../guides/kill-ai-slop-code.md).
- Automate the repetitive ops (onboarding emails, usage alerts) in [n8n](../README.md#automation--agent-frameworks) so you stay on product.

## The solo advantage

One person + an agent that plans, builds, and verifies can ship what used to take a small team — as long as you keep human judgment on scope and taste, and never merge code whose correctness you can't point at.
