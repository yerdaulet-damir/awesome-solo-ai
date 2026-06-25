# Self-Hosted Infra Stack

Five tools that together cover hosting, data, automation, observability, and search for a solo-run product — all self-hostable on a single $20/month VPS. This is the stack you graduate to when vendor bills start compounding or when you want data on your own infrastructure.

## The five pieces

### Coolify — hosting and deploy

[coollabsio/coolify](https://github.com/coollabsio/coolify) (~56k★, Apache 2.0) is the self-hosted alternative to Vercel, Heroku, and Railway. It runs on any VPS with a Docker-compatible host and handles: Git-based deploys (push to deploy), environment variable management, SSL certificates via Let's Encrypt, reverse proxy, and container orchestration. One Coolify instance on a $20 Hetzner server can host dozens of small apps.

**Setup:** one-command install on a fresh Ubuntu server. Connect your GitHub account, point it at a repo, Coolify detects the build system (Next.js, Docker, static) and sets up the pipeline. Custom domains take under two minutes.

**When to use instead of Vercel:** when you want full data residency, when you have multiple apps that would each hit Vercel's pro tier, or when your app has long-running processes that serverless functions can't support.

### NocoDB — database UI and no-code layer

[nocodb/nocodb](https://github.com/nocodb/nocodb) (~62k★, AGPL) connects to any existing Postgres (or MySQL, SQLite) database and gives you a spreadsheet-style UI over it — think Airtable, but it's a view layer over your real database, not a separate data store. Your Claude Code sessions write to the same Postgres that NocoDB reads. This is the killer feature: your AI agent and your no-code UI share one source of truth.

**Setup:** one Docker container, point it at your Supabase or self-hosted Postgres connection string. NocoDB introspects the schema and builds views for every table automatically. Share specific views with clients or team members without giving them database access.

**When to use:** anytime you need to let non-technical stakeholders view, edit, or export data from your app's database without building a custom admin panel.

### n8n — automation

[n8n-io/n8n](https://github.com/n8n-io/n8n) (~190k★, fair-code) is the automation engine that replaces Zapier and Make for everything non-trivial. The self-hosted version has no workflow limits, no operations caps, and no per-workflow fees. The node library covers 400+ integrations including Claude API, Supabase, Stripe, Resend, GitHub, Slack, and every major SaaS.

**Setup:** Docker Compose is the recommended path — n8n plus a Postgres container for persistence. Mount a volume for workflow data. The UI is accessible at port 5678. Put it behind your Coolify reverse proxy for a clean subdomain.

**The solo use case:** run automations that would cost $50–200/month on Zapier's paid tiers — onboarding sequences, webhook processors, content pipelines, usage alert emails — on the same VPS as your app, for free.

### Langfuse — LLM observability

[langfuse/langfuse](https://github.com/langfuse/langfuse) (~21k★, MIT) is what you use when your app makes LLM calls and you need to know: which prompts are slow, which are expensive, which are producing bad outputs, and what users are actually asking. It captures traces (input → output + latency + cost), lets you tag and score individual responses, and exports datasets for fine-tuning or evals.

**Setup:** Docker Compose with Postgres. Add three lines to your app code (the SDK is available for Node, Python, and any language via the REST API) and traces start flowing. Connect the Langfuse MCP to Claude Code to review traces directly in your agent sessions.

**When you need it:** as soon as your app has a production LLM call. Debugging a broken prompt without traces is guesswork. Debugging with Langfuse takes under a minute.

### Meilisearch — search

[meilisearch/meilisearch](https://github.com/meilisearch/meilisearch) (~56k★, MIT) is a fast, typo-tolerant search engine with an API that feels simpler than Elasticsearch and significantly simpler than Algolia to self-host. Sub-100ms search on millions of documents. Handles fuzzy matching, filters, facets, and geosearch out of the box. The index-everything approach means you can point it at any JSON data and get good search without schema design.

**Setup:** single binary or Docker container, no external dependencies. Add documents via REST API or the JavaScript/Python SDK. Claude Code can write the indexing logic in a few minutes once Meilisearch is running.

**When to use:** any app feature that needs search beyond simple `ILIKE` queries in Postgres. User-facing search boxes, admin record lookup, autocomplete — all more maintainable in Meilisearch than custom SQL.

## The full stack on one VPS

A Hetzner CX32 (4 vCPU, 8GB RAM, ~$12/month) runs all five tools comfortably for a solo product at early scale:

```
Coolify (hosting layer)
  ├── Your app (Next.js / whatever)
  ├── n8n (automations)
  ├── NocoDB (database UI)
  ├── Langfuse (LLM observability)
  └── Meilisearch (search)
Postgres (shared by app + NocoDB + n8n + Langfuse)
```

Coolify manages SSL, domains, and restarts for everything. One server, one bill, full ownership.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
