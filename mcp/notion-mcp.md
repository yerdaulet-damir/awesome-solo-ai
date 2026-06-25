# Notion MCP

> Read and write your Notion workspace — query databases, update pages, draft docs — from inside Claude.

| | |
|---|---|
| **Made by** | Notion (official, makenotion/notion-mcp-server) |
| **Install** | `claude mcp add notion-mcp -- npx -y @notionhq/notion-mcp-server` |
| **Auth** | Notion integration token |
| **License** | MIT |

## What is the Notion MCP?

The Notion MCP lets an agent read pages, query and update databases, create new content, and manage block-level structure inside your Notion workspace. It requires Notion API version 2026-03-11. This turns Notion-as-second-brain into live context for agents: your research notes, task databases, and project docs become queryable without leaving Claude.

## Why solo builders use it

Solo builders who use Notion as their operating system — meeting notes, project tracking, research — can stop copying things between tools. Ask Claude to pull all open tasks from a Notion database, summarize the research notes from last week, or draft a product spec and write it directly into a Notion page. The context stays in one place.

The database query capability is particularly useful for task-management workflows. With a well-structured Notion database, you can ask Claude to surface everything blocked on external dependencies, calculate how many tasks shipped this sprint, or generate a weekly summary without ever opening the app. It is the kind of lightweight ops automation that used to require Zapier or a custom script.

For writing workflows, the ability to create and update pages turns Claude into a Notion-native writing assistant. Draft a doc in conversation, refine it, then push the final version directly to your workspace. No clipboard, no copy-paste friction. The integration token scoping means you can limit access to only the pages and databases your integration needs — good practice for any production workflow.

## Setup

Create an internal integration at [notion.so/my-integrations](https://www.notion.so/my-integrations). Share the relevant pages/databases with the integration.

```bash
export NOTION_API_TOKEN=ntn_...

claude mcp add notion-mcp -- npx -y @notionhq/notion-mcp-server
```

In config:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": { "NOTION_API_TOKEN": "ntn_..." }
    }
  }
}
```

## Example

```
Use the Notion MCP to query my "Product Roadmap" database.
Find all items with status "In Progress" and owner "me".
Draft a concise weekly update summarizing progress, then create a new Notion page in the "Updates" section with that draft.
```

## See also

- [Exa MCP](exa.md) — research externally, then write findings into Notion
- [Stripe MCP](stripe.md) — pull billing data and push summaries to Notion

## Source

[github.com/makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) · [developers.notion.com](https://developers.notion.com)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
