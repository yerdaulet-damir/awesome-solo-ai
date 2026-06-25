# Claude Skills for Solo Builders

> Trending Claude Code skills, each with its own deep page — what it is, when to use it, install steps, and a real example.

A **Claude skill** is a reusable `.claude/skills` folder (markdown + optional scripts) that teaches Claude Code a repeatable workflow you invoke by name. Below are the skills solo builders install most in 2026, grouped by job. Each links to a full page.

## Design & frontend
- [ui-ux-pro-max](ui-ux-pro-max.md) — design system from one prompt: 50+ styles, 161 palettes, 57 font pairings.
- [frontend-design](frontend-design.md) — Anthropic's official skill that kills generic AI-slop UI.

## SEO & growth
- [claude-seo](claude-seo.md) — full SEO + GEO suite: audit, schema, backlinks, AI-search optimization.

## Code quality & anti-slop
- [ponytail](ponytail.md) — makes the agent write ~54% less code by thinking like a lazy senior dev.
- [superpowers](superpowers.md) — plan-first, test-driven agentic workflow.
- [context7](context7.md) — injects up-to-date library docs so the agent stops hallucinating APIs.
- [karpathy-skills](karpathy.md) — four rules from Andrej Karpathy that stop Claude from coding on wrong assumptions (~144k stars, fastest-growing skill 2026).

## Cost & session length
- [caveman](caveman.md) — cuts Claude output tokens by ~65% and shrinks CLAUDE.md by ~46% without losing technical accuracy.
- [context-mode](context-mode.md) — filters shell noise from context and survives Claude resets; sessions that died at 30 min now run for hours.

## Build & verify
- [webapp-testing](webapp-testing.md) — official Anthropic skill: tests your local app in a real Playwright browser, catching JS errors invisible to static analysis.
- [mcp-builder](mcp-builder.md) — official Anthropic skill: guided workflow for shipping your own MCP server from any API or tool, no spec-reading required.

---

> ⚠️ **Security:** skills are markdown + shell. A 2026 Snyk study found ~13% of community skills had critical flaws, some exfiltrating credentials. Read the `SKILL.md` before installing anything outside Anthropic or an established maintainer.

_Part of [Awesome Solo AI](../README.md). Found a skill that belongs here? [Contribute](../CONTRIBUTING.md)._
