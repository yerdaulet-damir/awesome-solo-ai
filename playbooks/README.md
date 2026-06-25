# Playbooks

End-to-end workflows a solo builder can copy. Each playbook covers a full stack for one task — tool choices, the step-by-step flow, and the specific gotchas that cost time if you hit them cold.

## All playbooks

### Build

- [RAG chatbot over your docs](rag-chatbot-over-docs.md) — Firecrawl → Supabase pgvector → Claude → Vercel. Full pipeline in a weekend, including the chunk-size tradeoff that determines retrieval quality.
- [Ship a SaaS solo with Claude Code + MCP](solo-saas-with-claude.md) — The build loop one engineer uses to design, verify, and ship a real product with an AI agent.
- [Vibe-code an MVP in a weekend](vibe-code-mvp-weekend.md) — Friday idea → Saturday build → Sunday launch. The CLAUDE.md setup that keeps Claude on track for 12-hour sessions and the drift points to watch for.
- [AI Chrome extension in 72 hours](ai-chrome-extension.md) — DOM injection → Claude API → Stripe paywall. Extensions are the lowest-CAC product model right now. Covers the three most common Chrome Web Store rejection reasons.
- [SaaS billing + onboarding automation](saas-billing-onboarding.md) — Stripe MCP + Supabase MCP + Resend in one Claude Code session. The "Stripe from day one" playbook, including the one RLS policy that will bite you if you miss it.

### Grow

- [Launch and get your first users (solo)](launch-and-get-first-users.md) — Distribution sequence for a one-person launch: where to post, what to build before launch day, and how to turn a spike into a loop.
- [Cold outreach personalization at scale](cold-outreach-personalization.md) — 50 LinkedIn URLs → 50 personalized openers in 30 minutes via Firecrawl + Claude + Instantly. Includes deliverability basics.
- [Content repurposing flywheel](content-repurposing-flywheel.md) — One idea → ten formats automatically. Blog post → Twitter thread + LinkedIn carousel + newsletter + short-video scripts + Reddit comments + Product Hunt tagline via n8n + Claude.

### Content

- [Faceless short-form content factory](faceless-content-factory.md) — Script → voice → avatar → captions → publish. The pipeline behind faceless YouTube/TikTok/Reels channels.
- [YouTube channel → newsletter + content flywheel](youtube-to-newsletter.md) — Whisper transcription → Claude rewrite → Beehiiv/ConvertKit publish. One video into five distribution formats, automated with n8n.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
