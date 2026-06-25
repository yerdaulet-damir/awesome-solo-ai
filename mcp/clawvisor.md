# Clawvisor MCP

> An API gateway that lets your agent act on external services — without ever seeing your credentials.

| | |
|---|---|
| **Made by** | clawvisor (open-source) |
| **Repo** | [github.com/clawvisor/clawvisor](https://github.com/clawvisor/clawvisor) |
| **Stars** | ~242 · 53 releases · actively maintained |
| **Auth** | Purpose-based approval — you approve scopes, gateway injects credentials |
| **License** | Open-source |

## What is Clawvisor?

Clawvisor is an open-source API gateway that sits between a Claude Code agent and external services like Gmail, GitHub, Slack, or Notion. Agents declare what they intend to do; you approve the scope once; Clawvisor injects credentials only at execution time — the agent never touches your API keys. Every action is audited.

## Why solo builders use it

When you give an agent an API key, you're giving it blanket access. That works fine for low-stakes tools, but it becomes a real problem when the agent can send emails, open GitHub PRs, post Slack messages, or push to production. One wrong prompt — or a prompt injection in external content — and the agent does something you didn't intend.

Clawvisor solves this without requiring you to build an approval flow yourself. You define the purpose ("summarize emails from the last 24 hours") and the scope (read-only, Gmail, last 24h). Clawvisor enforces those constraints at the gateway level, independent of what's in the prompt. The agent can't exceed the declared scope even if it tries.

For solo builders running autonomous agents on a schedule — content research, outreach drafts, repo triage — this is the layer that makes "run unsupervised" feel less risky. You approve the scope once, get an audit log of every action, and know the agent can't go sideways.

## Setup

```bash
git clone https://github.com/clawvisor/clawvisor
# follow setup instructions in the repo README
# configure the services you want to proxy (Gmail, GitHub, Slack, Notion...)
# wire it as an MCP server in Claude Code
```

## Example

```
Use Clawvisor to read the last 20 emails in my inbox tagged "support",
summarize each one in one sentence, and draft a reply for any that
have been waiting more than 48 hours. Do not send anything — drafts only.
```

Clawvisor enforces "drafts only" at the gateway — even if the agent generates a send command, the scope blocks it.

## See also

- [GitHub MCP](github.md) — safe repo management via official MCP
- [Notion MCP](notion-mcp.md) — read/write Notion within a declared scope
- [Build your own AI agent](../build/your-own-ai-agent.md) — the full autonomous agent stack

## Source

[github.com/clawvisor/clawvisor](https://github.com/clawvisor/clawvisor)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
