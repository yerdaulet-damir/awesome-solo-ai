# Build Your Own AI SaaS

> Ship a revenue-generating AI product solo — the full stack in one weekend.

## What you're building

An AI SaaS is a web application that charges recurring fees to automate one workflow using a language model. The end result is a URL with a login page, a Stripe billing integration, and a core feature that does something useful with an LLM — writing, extraction, classification, generation, or analysis. This guide covers the fastest path from idea to first dollar: one workflow, four tools, deployed by Sunday night.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| LLM routing | OpenRouter | One API key for every major model; swap models without code changes; pay only for what you use | [tools/openrouter.md](../tools/openrouter.md) |
| Auth + database | Supabase | Postgres, auth, and storage in one free tier; Row Level Security means no custom auth logic | [tools/supabase.md](../tools/supabase.md) |
| Hosting + frontend | Vercel | Zero-config Next.js deploy; edge functions handle LLM calls without a separate backend | [tools/vercel.md](../tools/vercel.md) |
| Product analytics | PostHog | Free up to 1M events; shows which features users actually use before you build more | [tools/posthog.md](../tools/posthog.md) |
| Payments | Stripe MCP | Manage products, prices, and customer portal directly from Claude Code during setup | [mcp/stripe.md](../mcp/stripe.md) |

## Build it

**Step 1 — Pick one workflow to automate.** The graveyard of failed AI SaaS is full of "AI writing assistants" that do everything. Pick a workflow someone does repeatedly at work and charges time to: proposal writing, job description drafting, invoice parsing, competitive analysis, email personalization. The more specific the workflow, the easier the copy and the lower the churn.

**Step 2 — Set up auth and database (Supabase).** Create a Supabase project, enable email auth, and create a `users` table with a `plan` column. Use Supabase's Next.js auth helpers (`npm i @supabase/ssr`) to wrap your routes in a session check. This takes under an hour and gives you working login, signup, and session cookies with no additional code.

**Step 3 — Wire the LLM (OpenRouter).** Create a Vercel edge function at `app/api/generate/route.ts`. Call OpenRouter's chat completions endpoint — it is OpenAI-compatible, so pass `model: 'anthropic/claude-sonnet-4-5'` (or any other model) in the request body. OpenRouter handles rate limiting, fallbacks, and model routing automatically. Keep your system prompt in a constant at the top of the file so Claude Code can edit it as a first-class artifact.

**Step 4 — Add Stripe.** Use the Stripe MCP in Claude Code to create your product and price objects without touching the Stripe dashboard. Create a checkout session endpoint (`POST /api/checkout`) that redirects to Stripe, and a webhook handler (`POST /api/webhooks/stripe`) that updates the `plan` column in Supabase when payment succeeds. Add a customer portal link so users can self-manage billing. This is the step most builders skip — ship it in the first weekend, not later.

**Step 5 — Gate the core feature.** In your generation endpoint, check `user.plan` before calling OpenRouter. Free users get a capped number of runs per month (stored in a `usage` table); paid users get unlimited. Show a clear upgrade prompt when the free limit is hit. The simplest paywall converts better than a feature-gated one.

**Step 6 — Deploy and launch.** Push to Vercel, set environment variables (`OPENROUTER_API_KEY`, `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`), and verify the Stripe webhook URL in the Stripe dashboard. PostHog auto-captures page views; add one manual event on workflow completion (`posthog.capture('workflow_completed')`). Then post in three places: the subreddit for your target user, a relevant Discord, and your own Twitter/X.

## What it costs

Supabase free tier: 500MB database, 1GB file storage, 50,000 monthly active users. Vercel free tier: 100GB bandwidth, unlimited deployments. OpenRouter: pay per token, no minimum — Claude Sonnet is roughly $0.003 per 1,000 output tokens. PostHog free: 1 million events per month. Stripe: 2.9% + 30¢ per transaction, no monthly fee. Your cost from zero to first $100 MRR is approximately $0, plus Stripe's cut on revenue.

## Real examples

Marketingblocks, Jasper, and Copy.ai all started as single-workflow tools — one template, one LLM call, one price. The solo builders who took them from $0 to $10k MRR did it by being extremely specific about the one job their tool did, not by adding more features.

A solo developer built a "job description writer" AI SaaS targeting HR managers — one text input, one LLM call formatted as a structured JD, $29/mo per seat. It reached $8k MRR in four months with no marketing budget, only ProductHunt and LinkedIn posts.

## FAQ

**What AI SaaS ideas actually make money solo?**
Workflow automation beats content generation. Ideas that work: document parsing (extract structured data from PDFs), personalized outreach (generate custom emails from a CSV of leads), internal knowledge search (chat over your company's docs), and niche report generation (generate a SEO audit, a financial summary, a competitive analysis). The pattern is: repetitive professional task + clear output format + someone who bills hourly for doing it manually.

**How do I pick a model for my AI SaaS?**
Use OpenRouter and A/B test. Start with Claude Sonnet for quality-sensitive tasks (writing, analysis, extraction), GPT-4o-mini for high-volume low-cost tasks (classification, tagging), and Gemini Flash for tasks that need long context cheaply. OpenRouter lets you switch models by changing one string — so ship with the best model and optimize cost later once you have paying users.

**What's the fastest way to add payments to an AI app?**
Stripe Checkout is the fastest path: one redirect, Stripe handles the UI. Use the Stripe MCP in Claude Code to create your price object in seconds, then generate the checkout session server-side with two lines of Stripe SDK code. Avoid building a custom payment form — Stripe Checkout converts better than custom UIs and handles PCI compliance automatically.

**How do I avoid OpenAI rate limits?**
Route through OpenRouter. OpenRouter load-balances across multiple provider accounts and automatically retries on 429s. You can also set fallback models in your request — `"anthropic/claude-sonnet-4-5"` as primary with `"openai/gpt-4o"` as fallback. For high-volume apps, add request queuing in your edge function with a simple in-memory queue or Redis.

## Go deeper

- [tools/openrouter.md](../tools/openrouter.md) — model routing, fallbacks, cost tracking
- [tools/supabase.md](../tools/supabase.md) — auth, database, RLS policies for SaaS
- [mcp/stripe.md](../mcp/stripe.md) — Stripe MCP: manage billing from Claude Code
- [tools/posthog.md](../tools/posthog.md) — analytics that tell you what to build next
- [playbooks/solo-saas-with-claude.md](../playbooks/solo-saas-with-claude.md) — full walkthrough of the solo SaaS build
- [playbooks/saas-billing-onboarding.md](../playbooks/saas-billing-onboarding.md) — Stripe + Supabase billing integration detail

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
