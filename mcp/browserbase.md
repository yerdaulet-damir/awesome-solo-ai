# Browserbase MCP

> Cloud browser automation — clicks, form fills, screenshots, full JS rendering — without a local Playwright setup.

| | |
|---|---|
| **Made by** | Browserbase |
| **Install** | `claude mcp add browserbase -- npx -y @browserbasehq/mcp` |
| **Auth** | `BROWSERBASE_API_KEY` + `BROWSERBASE_PROJECT_ID` |
| **License** | MIT |

## What is the Browserbase MCP?

The Browserbase MCP lets an agent drive a real, cloud-hosted browser — navigating pages, clicking elements, filling forms, taking screenshots, and handling full JavaScript rendering. Where Firecrawl reads static and JS-rendered content passively, Browserbase acts: it can log in, interact with authenticated pages, and complete multi-step web workflows an agent designs.

## Why solo builders use it

The defining use case is anything behind a login. Firecrawl and Exa can reach public web pages, but the moment a workflow requires authentication — checking an admin dashboard, interacting with a SaaS tool that has no API, scraping your own analytics — you need a real browser that can hold a session. Browserbase handles that without you running Playwright locally.

For automation workflows, the cloud-hosted model removes a whole category of ops work. No headless Chrome to maintain, no dependency on your local machine being on, no proxies to manage. Browserbase runs the browser in their infrastructure; your agent just sends instructions and receives results. Solo builders wire it to scheduled tasks that check things, fill forms, or capture screenshots on a cadence.

Screenshots are underrated here. An agent that can navigate to a URL, take a screenshot, and return it to Claude creates a feedback loop for visual debugging — confirming that a deploy looks right, catching UI regressions, or just letting you see what a customer-facing page looks like without opening a browser yourself.

## Setup

Get an API key and project ID at [browserbase.com](https://www.browserbase.com).

```bash
export BROWSERBASE_API_KEY=your_key
export BROWSERBASE_PROJECT_ID=your_project_id

claude mcp add browserbase -- npx -y @browserbasehq/mcp
```

In config:

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "npx",
      "args": ["-y", "@browserbasehq/mcp"],
      "env": {
        "BROWSERBASE_API_KEY": "your_key",
        "BROWSERBASE_PROJECT_ID": "your_project_id"
      }
    }
  }
}
```

## Example

```
Use the Browserbase MCP to navigate to my app's admin dashboard at https://app.example.com/admin.
Log in with the credentials in my .env file.
Take a screenshot of the users table and return it so I can confirm the new signup appears.
```

## See also

- [Firecrawl MCP](firecrawl.md) — for passive reading of public URLs without interaction
- [Playwright MCP](playwright.md) — local browser automation alternative
- [Exa MCP](exa.md) — for search when you don't need browser interaction

## Source

[github.com/browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) · [docs.browserbase.com](https://docs.browserbase.com)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
