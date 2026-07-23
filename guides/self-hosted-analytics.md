# Analytics for Solo Builders (Self-Hosted and Open-Source)

Analytics you can run yourself, own the data, and point an agent at. Web, product, and LLM observability, all open source or self hostable, all verified live in July 2026.

## Web and product analytics

- [Umami](https://github.com/umami-software/umami) by [Umami Software](https://github.com/umami-software), single page, cookieless web analytics that runs in one Postgres container. open source, self hosted, web analytics, api.
- [Plausible](https://github.com/plausible/analytics) by [Plausible](https://github.com/plausible), a script under 1KB that reports pageviews, visitors, and referrers with no cookies. open source, self hosted, web analytics, api.
- [Rybbit](https://github.com/rybbit-io/rybbit) by [Rybbit](https://github.com/rybbit-io), a newer GA alternative that adds session replay, funnels, and web vitals in one dashboard. open source, self hosted, product analytics, session replay.
- [GoatCounter](https://github.com/arp242/goatcounter) by [Martin Tournoij](https://github.com/arp242), a tiny Go binary for privacy friendly pageview counting with no personal data stored. open source, self hosted, web analytics, lightweight.
- [Matomo](https://github.com/matomo-org/matomo) by [Matomo](https://github.com/matomo-org), the full Google Analytics replacement with goals, heatmaps, and a complete reporting API. open source, self hosted, web analytics, api.
- [Medama](https://github.com/medama-io/medama) by [Medama](https://github.com/medama-io), a single binary privacy first analytics server for people who want the smallest possible footprint. open source, self hosted, web analytics, lightweight.

## LLM and AI observability

- [Langfuse](https://github.com/langfuse/langfuse) by [Langfuse](https://github.com/langfuse), traces every LLM call, run, and eval, with prompt management and datasets, self hosted in about five minutes. open source, self hosted, llm observability, evals, mcp.
- [Helicone](https://github.com/Helicone/helicone) by [Helicone](https://github.com/Helicone), a one line proxy that logs cost, latency, and quality across 100+ models and ships its own MCP server. open source, self hosted, llm observability, proxy, mcp.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) by [Traceloop](https://github.com/traceloop), OpenTelemetry native instrumentation so your LLM traces land in whatever backend you already run. open source, opentelemetry, llm observability.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix) by [Arize AI](https://github.com/Arize-ai), local first tracing and evaluation for RAG and agent apps, runs in a notebook or a container. open source, self hosted, llm observability, evals.
- [Highlight](https://github.com/highlight/highlight) by [Highlight](https://github.com/highlight), open source session replay plus error monitoring you can self host. open source, self hosted, session replay, monitoring.

## Analytics MCP servers

- [PostHog MCP](https://github.com/PostHog/mcp) by [PostHog](https://github.com/PostHog), the official server that lets an agent query insights, funnels, and feature flags from your PostHog project. mcp, product analytics, official.
- [Grafana MCP](https://github.com/grafana/mcp-grafana) by [Grafana](https://github.com/grafana), lets an agent pull dashboards, query Prometheus and Loki, and read incidents straight from Grafana. mcp, observability, official.
- [Sentry MCP](https://github.com/getsentry/sentry-mcp) by [Sentry](https://github.com/getsentry), gives an agent access to issues, traces, and error context from your Sentry org. mcp, error monitoring, official.

## FAQ

**What are the best open source, self-hosted web analytics tools?**
Umami and Plausible are the two most reached for picks, both cookieless and both replacing Google Analytics with a sub 1KB script and a clean single page dashboard. If you want more than pageviews, Rybbit adds session replay and funnels, while Matomo covers the heavier enterprise end with a full reporting API. All four run in Docker and keep the event data on your own server.

**How do I add LLM observability to an indie AI product?**
Start with Langfuse or Helicone, since both self host in minutes and need almost no code. Helicone works as a one line proxy that logs every request, so you get cost and latency tracking without touching your app logic, while Langfuse uses SDK decorators and gives you traces, evals, and prompt versioning. If you already run OpenTelemetry, OpenLLMetry sends the same LLM traces into your existing backend instead of a new dashboard.

**What is an analytics MCP server and why would I want one?**
An analytics MCP server exposes your metrics to an AI agent over the Model Context Protocol, so Claude or Cursor can query the numbers directly instead of you clicking through a dashboard. PostHog, Grafana, and Sentry all ship official ones, and Langfuse and Helicone bundle MCP servers for their LLM traces. In practice you ask a question in plain language, the agent runs the query, and you debug an error or read a funnel without leaving your editor.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
