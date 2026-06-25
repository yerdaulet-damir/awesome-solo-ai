# MCP Servers for Solo Builders

> Model Context Protocol servers let your agent *do things* — generate video, speak, browse, ship code — not just chat. Each has its own page below.

A **MCP server** exposes a tool (an API, a browser, a filesystem) to an AI agent over the Model Context Protocol, so Claude Code can call it directly. Below are the servers a solo builder wires in, grouped by job.

## Media generation
- [HeyGen MCP](heygen.md) — generate avatar videos, clone voices, create speech from your agent.
- [ElevenLabs MCP](elevenlabs.md) — text-to-speech, voice cloning, dubbing, and sound effects.
- [Cartesia MCP](cartesia.md) — ultra-low-latency realtime speech.
- [Ideogram MCP](ideogram.md) — image generation with strong typography, over MCP.
- [Higgsfield](higgsfield.md) — cinematic video gen (API-first; how to drive it from an agent today).

## Dev & automation
- [Playwright MCP](playwright.md) — drive a real browser for testing and scraping.
- [GitHub MCP](github.md) — issues, PRs, and repo actions from your agent.
- [Browserbase MCP](browserbase.md) — cloud browser automation: clicks, form fills, screenshots, JS-gated pages.
- [Supabase MCP](supabase-mcp.md) — query data, manage tables, generate TypeScript types, fetch logs from your Supabase project.
- [Sequential Thinking MCP](sequential-thinking.md) — structured step-by-step reasoning before acting; #1 by usage on Smithery.

## Search & reading
- [Exa MCP](exa.md) — semantic web search returning structured JSON; #1 most-used search MCP in 2026.
- [Firecrawl MCP](firecrawl.md) — convert any URL (JS pages, PDFs, Word docs) to clean Markdown; 12+ tools including full-site crawl.

## Productivity & billing
- [Stripe MCP](stripe.md) — inspect customers, subscriptions, payments, and disputes from inside Claude.
- [Notion MCP](notion-mcp.md) — read/write Notion docs, query databases, update pages; official Notion server.

## Where to discover more
- [Official MCP Registry](https://github.com/modelcontextprotocol/registry) — Anthropic's canonical index.
- [Smithery](https://smithery.ai) · [mcp.so](https://mcp.so) · [PulseMCP](https://www.pulsemcp.com) · [Glama](https://glama.ai/mcp/servers)

---

_Part of [Awesome Solo AI](../README.md). Know an MCP server that belongs here? [Contribute](../CONTRIBUTING.md)._
