# claude-seo — full SEO + GEO suite for Claude Code

> Run a complete technical SEO and AI-search audit from your terminal, with client-ready reports.

## What is the claude-seo skill?

**claude-seo is a Claude Code skill that performs end-to-end SEO and GEO analysis** — technical audits, schema markup, E-E-A-T content review, backlinks, local SEO, and optimization for AI search engines (ChatGPT, Perplexity, Google AI Overviews). It bundles 25 sub-skills and 18 sub-agents and can export PDF/Excel reports.

The most prominent build is [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (~9,700 GitHub stars, released February 2026).

## What it covers

- **Technical SEO** — crawlability, indexability, Core Web Vitals, security headers.
- **GEO / AI search** — citability scoring, llms.txt, AI-crawler access, brand mentions.
- **Schema** — detect, validate, and generate JSON-LD.
- **Content** — E-E-A-T, readability, thin-content detection.
- **Off-page** — backlinks, anchor text, competitor gap.
- **Local & maps**, **e-commerce**, **international (hreflang)**, **semantic clustering**.

Tiered Google API credentials progressively unlock PageSpeed/CrUX → Search Console → GA4 → Keyword Planner data.

## Why it matters for solo builders

A solo founder can't afford an SEO agency. claude-seo runs the audit an agency would, on your own sites, and hands you a prioritized fix list and a report you could send a client — making SEO a productized service you could resell.

## When to use it

- Auditing your product sites for search + AI visibility.
- Generating schema and llms.txt for a launch.
- Offering SEO/GEO as a paid service to others.

## Install

```
/plugin marketplace add AgriciDaniel/claude-seo
```

Then invoke `/seo` or a sub-skill like `/seo-geo` on a URL.

## Note

"claude-seo" is a crowded namespace — other distinct projects exist (e.g. content-humanizing or Next.js-specific variants). The AgriciDaniel suite is the broadest.

## Source

[github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
