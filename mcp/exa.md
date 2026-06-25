# Exa MCP

> Semantic web search built for agents — structured results, no scraping, no throttling.

| | |
|---|---|
| **Made by** | Exa Labs |
| **Install** | `claude mcp add exa-mcp-server -- npx -y exa-mcp-server` |
| **Auth** | `EXA_API_KEY` |
| **License** | MIT |

## What is the Exa MCP?

The Exa MCP lets an agent run semantic web searches and get back structured JSON — title, URL, snippet, and optional full page text — without scraping or hitting rate limits. It is the most widely used search MCP in 2026, designed from the ground up for programmatic consumption rather than human-readable HTML.

## Why solo builders use it

The gap between "search the web" and "get usable data into context" has always been painful. Traditional search APIs return ten blue links; Exa returns structured objects an agent can reason over immediately. That means you wire it once and your agent can research competitors, surface citations, or populate a RAG pipeline without a separate scraping layer.

For competitive research workflows, Exa is the first tool to reach for. A single query can return full page text alongside metadata, so Claude can summarize, compare, or extract structured information in the same turn. No Playwright, no BeautifulSoup, no headless browser — just results.

Free tier is generous enough for prototyping. Paid plans are priced per-search with no monthly minimum, which suits the sporadic, bursty usage patterns of solo side-projects better than subscription-heavy alternatives.

## Setup

```bash
# Add to Claude Code
claude mcp add exa-mcp-server -- npx -y exa-mcp-server

# Set your key (add to shell profile or .env)
export EXA_API_KEY=your_key_here
```

Or in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": ["-y", "exa-mcp-server"],
      "env": { "EXA_API_KEY": "your_key_here" }
    }
  }
}
```

## Example

```
Search for the top five AI-native CRM tools launched in 2025.
For each one, return the product name, founding year, pricing model, and a one-sentence description.
Use the Exa MCP to gather this data from the web.
```

## See also

- [Firecrawl MCP](firecrawl.md) — when you need to read a specific URL rather than search
- [Playwright MCP](playwright.md) — when the target page requires real browser interaction

## Source

[github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) · [exa.ai/docs](https://docs.exa.ai)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
