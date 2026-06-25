# Firecrawl MCP

> Turn any URL — JS-heavy app, PDF, Word doc — into clean Markdown your agent can read.

| | |
|---|---|
| **Made by** | Mendable AI |
| **Install** | `claude mcp add firecrawl-mcp -- npx -y firecrawl-mcp` |
| **Auth** | `FIRECRAWL_API_KEY` |
| **License** | MIT |

## What is the Firecrawl MCP?

The Firecrawl MCP lets an agent convert any URL — including JavaScript-rendered SPAs, PDFs, and Word documents — into clean, LLM-ready Markdown. It ships 12+ tools covering single-page fetch, full-site crawl, structured extraction with a schema, and a deep research mode that follows links automatically.

## Why solo builders use it

If Exa is for finding things, Firecrawl is for reading them. Once a search turns up a competitor's pricing page, a research paper, or a documentation site, Firecrawl is what actually gets the content into context in a form Claude can use. Raw HTML is noisy; Firecrawl strips nav, ads, and boilerplate so you get the signal.

The structured extraction tool deserves special attention for solo builders. Pass a Zod or JSON schema alongside a URL and Firecrawl returns typed data rather than prose — product prices, job listings, changelog entries — without writing a scraper. Combined with a cron job or a simple loop, it becomes a lightweight monitoring agent.

Full-site crawl mode lets an agent ingest entire documentation sites or competitor blogs in a single call, feeding a RAG pipeline or a competitive-intelligence workflow. Deep research mode adds autonomous link-following, which is useful when the answer is spread across multiple pages and you don't want to manage the traversal yourself.

## Setup

```bash
# Add to Claude Code
claude mcp add firecrawl-mcp -- npx -y firecrawl-mcp

export FIRECRAWL_API_KEY=your_key_here
```

Or in config:

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "your_key_here" }
    }
  }
}
```

## Example

```
Use the Firecrawl MCP to crawl https://docs.example.com and convert every page to Markdown.
Then extract a structured list of all API endpoints mentioned, with their HTTP method and description.
```

## See also

- [Exa MCP](exa.md) — for semantic search when you don't already have a URL
- [Playwright MCP](playwright.md) — when the page requires login or real user interaction

## Source

[github.com/mendableai/firecrawl-mcp-server](https://github.com/mendableai/firecrawl-mcp-server) · [firecrawl.dev/docs](https://docs.firecrawl.dev)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
