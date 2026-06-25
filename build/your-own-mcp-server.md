# Build Your Own MCP Server

> Turn any API into a Claude Code tool — in under 100 lines, in an afternoon.

## What you're building

An MCP (Model Context Protocol) server is a small process that exposes tools Claude can call during a conversation. You connect it once in Claude Code's config, and from that point on Claude can invoke your custom tools — hitting any API, reading any database, running any script — exactly as if those capabilities were built in. The end result is a named tool set that lives in Claude's context permanently.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| Scaffolding | mcp-builder skill | Generates boilerplate, types, and handler stubs from a plain-English spec — no MCP SDK spelunking | [skills/mcp-builder.md](../skills/mcp-builder.md) |
| Runtime | MCP SDK (TypeScript or Python) | Official spec implementation, maintained by Anthropic | [mcp/README.md](../mcp/README.md) |
| Host | Claude Code | The client that connects to your server and routes tool calls | — |
| Registry | Smithery | One-command publish, public discovery, install metrics | — |

## Build it

**Step 1 — Spec your tools.** Write down every action you want Claude to be able to take. Be concrete: not "manage tasks" but "create_task(title, due_date) → task_id" and "list_tasks(status) → array". One sentence per tool is enough. This spec is what you paste into mcp-builder.

**Step 2 — Scaffold with mcp-builder.** Open Claude Code and invoke the mcp-builder skill with your spec. It outputs a complete project directory with package.json, a typed handler file per tool, input/output schemas in JSON Schema format, and a working index.ts that registers everything. You have runnable code before you write a single business-logic line.

**Step 3 — Implement handlers.** Fill in each handler function with the actual API call, DB query, or file operation. The scaffolded handlers already have the right signature and error shape — your job is the three to ten lines in the middle that do the real work. Keep side effects isolated to handlers; the framework handles serialization.

**Step 4 — Test with Claude Code.** Add your server to `.claude/settings.json` under `mcpServers` pointing to `node dist/index.js`. Restart Claude Code, open a conversation, and type a natural-language request that should trigger your tool. Watch the tool call appear in the sidebar. Iterate on the tool descriptions until Claude routes to the right handler reliably — description quality matters more than implementation at this stage.

**Step 5 — Publish to Smithery.** Run `npx @smithery/cli publish`. Smithery reads your package.json, generates an install card with a one-line copy-paste command, and lists your server publicly. Anyone can install it with `npx @smithery/cli install your-server-name` and it appears in their Claude Code immediately.

## What it costs

Building and running an MCP server has no infrastructure cost — the server process runs locally on the user's machine (or on a server they already pay for). You pay only for Claude API tokens consumed during tool calls. A typical tool invocation costs $0.001–$0.003 in tokens at Sonnet pricing. If your MCP wraps a paid external API (weather, search, finance data), that API's own pricing applies. There is no Smithery listing fee.

## Real examples

The Exa MCP server wraps Exa's web search API into a single `search` tool. Before it existed, adding web search to a Claude workflow required manual copy-paste. After: `Claude, research the top five competitors for X` triggers a live search and Claude synthesizes the results inline. The server is under 80 lines of TypeScript.

The Firecrawl MCP does the same for web scraping — a single `crawl` tool that returns clean markdown. Solo builders use it to feed competitor pages, documentation sites, and Reddit threads directly into Claude without leaving the terminal.

## FAQ

**What is an MCP server?**
An MCP server is a local process that Claude Code connects to over stdio (or HTTP). It exposes a list of named tools with typed inputs and outputs. When Claude decides a tool call is appropriate during a conversation, it sends a JSON request to your server and receives a JSON response — exactly like a function call, but across a process boundary. The MCP spec standardizes the wire format so any client (Claude Code, Cursor, Continue) can use any server.

**Do I need to know the MCP spec to build one?**
No. The mcp-builder skill reads your plain-English tool descriptions and generates all the spec-compliant boilerplate. You only touch the handler bodies where you write your actual API calls. Reading the spec once is useful for understanding input schema validation and error codes, but it is not a prerequisite for shipping.

**How do I publish my MCP server?**
Install the Smithery CLI (`npm i -g @smithery/cli`), authenticate with `smithery login`, and run `smithery publish` from your project root. Smithery reads your package.json name, description, and tool list, creates a public listing page, and generates a one-line install command. You can also keep a server private and distribute it as a git repo — anyone can add it to their Claude Code config manually.

**What APIs work well as MCPs?**
Any API with a clear set of discrete operations maps naturally to MCP tools. REST APIs with CRUD endpoints are ideal — each endpoint becomes one tool. APIs that return large blobs of unstructured text (raw HTML, binary data) work less well without a preprocessing step. The best candidates are APIs you already call manually during Claude sessions: search engines, task managers, CRMs, internal databases, and data enrichment services.

## Go deeper

- [skills/mcp-builder.md](../skills/mcp-builder.md) — the skill that scaffolds your server from a spec
- [mcp/README.md](../mcp/README.md) — full catalogue of MCPs you can install or study
- [mcp/exa.md](../mcp/exa.md) — a real MCP server to read as a reference implementation
- [mcp/firecrawl.md](../mcp/firecrawl.md) — another real example: web crawling as a tool
- [playbooks/vibe-code-mvp-weekend.md](../playbooks/vibe-code-mvp-weekend.md) — weekend build context

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
