# Awesome Solo AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

AI tools, Claude skills, MCP servers and workflows for solopreneurs, indie hackers and solo founders building a one-person business.

Start with the [starter stack](#-the-starter-stack) or the [free stack](free-solo-ai-stack.md). Looking for an agent integration? Go to [MCP servers](#mcp-servers) or [Claude skills and plugins](#claude-skills--plugins).

For website work, use the [frontend design resource guide](guides/cinematic-frontend-not-slop.md): inspiration, component libraries, GSAP, Motion, 3D and agent skills.

_Updated: October 2026._

Give Claude Code or Cursor the [`llms.txt`](llms.txt) index, for example:
> `Read https://raw.githubusercontent.com/yerdaulet-damir/awesome-solo-ai/main/llms.txt — which tool here generates a talking-head avatar video, and does it have an MCP server?`

If this list helped you choose a tool, star it to find it again.

---

## Contents

- [Why this list](#why-this-list)
- [Legend](#legend)
- [⭐ The Starter Stack](#-the-starter-stack) — if you only pick a few
- [🧰 Tool deep-pages](tools/) — per tool: site, API, CLI, MCP, example
- [LLM API Routers & Aggregators](#llm-api-routers--aggregators)
- [Video Generation](#video-generation)
- [AI Avatars & Talking Heads](#ai-avatars--talking-heads)
- [Lipsync, Dubbing & Translation](#lipsync-dubbing--translation)
- [Voice, TTS & Cloning](#voice-tts--cloning)
- [Music & Sound Effects](#music--sound-effects)
- [Image Generation & Editing](#image-generation--editing)
- [MCP Servers](#mcp-servers)
- [Claude Skills & Plugins](#claude-skills--plugins)
- [Agent Memory & Knowledge](#agent-memory--knowledge)
- [AI Coding Agents](#ai-coding-agents)
- [Automation & Agent Frameworks](#automation--agent-frameworks)
- [Frontend Motion & Design](#frontend-motion--design)
- [Backend, Deploy & Analytics](#backend-deploy--analytics)
- [Distribution & Marketing](#distribution--marketing)
- [💸 Free Solo AI Stack](free-solo-ai-stack.md) — only the free-tier & open-source tools
- [🔨 Build Your Own AI X](#-build-your-own-ai-x) — step-by-step guides to ship real AI products
- [Guides](#guides) — tutorials, Karpathy/Kaggle-style
- [Playbooks](#playbooks) — end-to-end solo workflows
- [🔓 Open-Source Alternatives](open-source/) — every closed tool has an OSS swap
- [📣 Distribution & Marketing](distribution/) — where and how to launch
- [FAQ](#faq)
- [Contributing](#contributing)
- [Maintained by](#maintained-by)

---

## Why this list

There are big awesome lists for [MCP servers](https://github.com/punkpeye/awesome-mcp-servers), for [Claude Code](https://github.com/hesreallyhim/awesome-claude-code), and for [generative AI](https://github.com/steven2358/awesome-generative-ai) — but nothing assembles the **AI stack a one-person company actually runs on**: the video/voice/image tools a solopreneur pays for, *plus* the MCP servers and Claude skills that let an agent drive them, *plus* the playbooks for shipping and growing solo. This is the home base for solopreneurs, indie hackers, and solo founders building with AI. Curated by judgment — tools that don't work get cut.

## Legend

- 🔌 **API** — has a public developer API
- 🧩 **MCP** — has an official Model Context Protocol server (agent-callable)
- 🆓 **Free** — has a usable free tier
- 🔓 **Open** — open weights / open source

---

## ⭐ The Starter Stack

New to building solo? **This is the first stack every solopreneur should know** — one solid pick per layer. Start here, expand later.

| Layer | Pick | Why |
| --- | --- | --- |
| Coding agent | [Claude Code](#ai-coding-agents) | the hub you feed everything else into |
| LLM access | [OpenRouter](tools/openrouter.md) | one key, every model, free tier |
| Voice | [ElevenLabs](tools/elevenlabs.md) | best TTS + cloning, has an MCP |
| Image | [Nano Banana](tools/nano-banana.md) / [Ideogram](tools/ideogram.md) | fast realistic images / real typography |
| Video + avatar | [HeyGen](tools/heygen.md) | scripted avatar video, has an MCP |
| Backend + vector DB | [Supabase](tools/supabase.md) | Postgres + auth + pgvector for RAG |
| Deploy | [Vercel](tools/vercel.md) | one push to production + AI SDK |
| Analytics | [PostHog](tools/posthog.md) | product + LLM analytics, generous free tier |

Each pick has a full page in [`tools/`](tools/) — website, API, CLI, MCP, and an example. On a budget? Every layer has a free path — see the [Free Solo AI Stack](free-solo-ai-stack.md).

## LLM API Routers & Aggregators

One API key, many models. The backbone of any solo AI app — swap providers without rewriting code.

- [OpenRouter](https://openrouter.ai) — 400+ models from 70+ providers behind one OpenAI-compatible endpoint; the default router. 🔌 🆓
- [Together AI](https://together.ai) — 200+ open-source models plus fine-tuning and image gen on fast GPU clusters. 🔌 🆓 🔓
- [Fireworks AI](https://fireworks.ai) — high-reliability inference with strong function-calling accuracy and custom deployments. 🔌 🆓
- [Groq](https://groq.com) — fastest raw inference (700+ tok/s) on custom LPU chips; curated model set. 🔌 🆓
- [DeepInfra](https://deepinfra.com) — cheapest-per-token frontier open-weight models on serverless infra. 🔌 🔓
- [Fal.ai](https://fal.ai) — the go-to fast inference host for image/video/audio models (Flux, Kling, etc.). 🔌
- [Replicate](https://replicate.com) — run and fine-tune thousands of open models via one API; great for media. 🔌
- [AI/ML API](https://aimlapi.com) — 400+ models across text, image, video, audio, and music in one key. 🔌 🆓
- [Groq](https://groq.com), [Hyperbolic](https://hyperbolic.xyz), [Novita](https://novita.ai), [Featherless](https://featherless.ai) — additional low-cost open-model hosts worth a look. 🔌
- [Eden AI](https://www.edenai.co) — GDPR-native EU aggregator across text, OCR, speech, translation. 🔌 🆓

> ⚠️ Avoid: **PlayHT** (shut down Dec 2025), **DALL·E 2/3** (deprecated, API ends May 2026), **Helicone** (acquired, maintenance mode).

## Video Generation

Text-to-video and image-to-video — the tools creators use for shorts, ads, and B-roll.

- [Runway](https://runwayml.com) — industry-standard text/image-to-video with fine motion control (Gen-4). 🔌
- [Kling AI](https://klingai.com) — high-fidelity, long-duration video gen; strong physics and consistency. 🔌
- [Higgsfield](https://higgsfield.ai) — cinematic camera-control and motion-preset video gen, built for social creators. 🔌
- [Google Veo](https://deepmind.google/models/veo/) — Google's flagship text-to-video with audio, via Gemini API. 🔌
- [OpenAI Sora](https://sora.com) — OpenAI's text-to-video model and app. 🔌
- [Luma Dream Machine](https://lumalabs.ai/dream-machine) — fast, fluid image-to-video and keyframes. 🔌
- [Magic Hour](https://magichour.ai) — create and edit video, images, and audio with AI. 🔌 🆓
- [Pika](https://pika.art) — creator-friendly video gen with effects and editing. 🔌
- [Hailuo / MiniMax](https://hailuoai.video) — high-quality cinematic video gen from text or image. 🔌
- [Hedra](https://www.hedra.com) — character-driven video and expressive talking characters. 🔌
- [Pixwit](https://pixwit.ai) — multi-model text-to-video and image-to-video with effect templates and image gen. 🆓

## AI Avatars & Talking Heads

Spokesperson and presenter video from a script — no camera, no studio.

- [HeyGen](https://heygen.com) — leading avatar/spokesperson video from text; clone yourself. 🔌 🧩 🆓
- [Synthesia](https://synthesia.io) — enterprise AI avatars in 140+ languages for training and explainer video. 🔌
- [Captions](https://captions.ai) — AI creator studio: avatars, editing, and dubbing for shorts. 🔌
- [Argil](https://argil.ai) — clone yourself into an AI influencer for faceless content at scale. 🔌
- [Tavus](https://tavus.io) — real-time conversational video avatars (digital twins) via API. 🔌
- [D-ID](https://d-id.com) — talking-head video and real-time interactive agents from a photo. 🔌

## Lipsync, Dubbing & Translation

- [Sync.so](https://sync.so) — best-in-class lipsync API to match any audio to any video. 🔌
- [HeyGen Translate](https://heygen.com/translate) — translate and re-lipsync video into 175+ languages. 🔌 🧩
- [Rask AI](https://rask.ai) — one-click video translation and dubbing for 130+ languages. 🔌
- [ElevenLabs Dubbing](https://elevenlabs.io/dubbing) — voice-preserving dubbing across 30+ languages. 🔌 🧩

## Voice, TTS & Cloning

- [ElevenLabs](https://elevenlabs.io) — market-leading TTS, voice cloning, and voice agents; 70+ languages. 🔌 🧩 🆓
- [Cartesia](https://cartesia.ai) — lowest-latency realtime TTS (~90ms) with 3-second voice cloning. 🔌 🧩
- [Fish Audio](https://fish.audio) — open-source TTS and voice cloning, ~80% cheaper than ElevenLabs. 🔌 🔓
- [Piper](https://github.com/OHF-Voice/piper1-gpl) — fast local neural TTS with CLI, Python, C/C++, and HTTP interfaces; runs offline. Voice-model licenses vary. 🆓 🔓
- [Hume](https://hume.ai) — emotion-aware voice (EVI) and expressive Octave TTS. 🔌
- [Rime](https://rime.ai) — developer/enterprise TTS with sub-200ms latency. 🔌
- [Resemble AI](https://resemble.ai) — enterprise voice cloning plus deepfake detection. 🔌 🧩
- [Hermes](https://buildwithhermes.com) — operating platform for running an AI voice-agent business solo: white-label phone agents with built-in CRM, campaigns, and client billing, from $149/mo.
- [OmniVoice Studio](https://github.com/debpalash/OmniVoice-Studio) — open-source, fully-local ElevenLabs alternative: voice cloning, dubbing, dictation, 646 languages, no API keys. 🆓 🔓

## Music & Sound Effects

- [Suno](https://suno.com) — leading text-to-song generator with vocals. 🔌 🆓
- [Udio](https://udio.com) — high-fidelity text-to-music (transitioning to a licensed platform). 🔌
- [ElevenLabs SFX](https://elevenlabs.io/sound-effects) — text-to-sound-effects up to 30s, loopable. 🔌 🧩
- [Stable Audio](https://stableaudio.com) — commercially-clean music and SFX from a licensed dataset. 🔌
- [Mubert](https://mubert.com) — real-time royalty-free generative music streams. 🔌

## Image Generation & Editing

- [Midjourney](https://midjourney.com) — best-in-class artistic/aesthetic image quality (v7). 🔌
- [Black Forest Labs FLUX](https://bfl.ai) — photorealism leader; FLUX.2 family with open-weight tiers. 🔌 🔓
- [Google Nano Banana](https://gemini.google) — Gemini image gen: fast, realistic, up to 4K, multi-reference editing. 🔌
- [OpenAI GPT Image](https://platform.openai.com) — general-purpose default image gen/edit (GPT Image 2). 🔌
- [Ideogram](https://ideogram.ai) — typography/text-in-image specialist. 🔌 🧩
- [Recraft](https://recraft.ai) — vector/SVG and brand-asset specialist. 🔌 🧩
- [Reve](https://reve.com) — strong prompt adherence, typography, and aesthetics. 🔌
- [Krea](https://krea.ai) — real-time canvas and a hub for Flux/Imagen/Ideogram/Nano Banana. 🔌
- [UpRes](https://upres.ai) — AI image & video upscaling (2x–8x) across 14 specialist models with REST API, CLI, and MCP server; free web tier gives 5 watermarked image upscales/month. 🔌 🧩 🆓

## MCP Servers

Model Context Protocol servers let your agent *do things*, not just chat. These are the ones a solo builder wires into Claude Code. **→ Full pages in [`mcp/`](mcp/).**

- [Agent QA](mcp/agent-qa.md) — run natural-language web/mobile tests with persistent test memory and self-healing flows. 🧩 🆓
- [ArtiGram](https://artigram.cafeboon.com): hosted remote MCP at `https://artigram.cafeboon.com/mcp` to publish AI-made HTML, React, SVG, Markdown or Mermaid as live shareable pages. Searching is public, publishing needs a free API key. 🧩 🆓
- [API.market MCP Gateway](https://api.market/api/mcp/gateway) — proprietary hosted gateway to discover and call APIs for generation, search, scraping, maps and data; OAuth or API key, with pricing and free tiers varying by API. 🧩
- [Aident Loadout](https://aident.ai) — remote MCP at `https://loadout.aident.ai/mcp` ([setup guide](https://docs.aident.ai/loadout/mcp)) that connects coding agents to 400+ Skills and connected apps through one setup; pay-as-you-go, some apps need your own OAuth or stored credentials, which stay in Vault with a full audit trail. 🧩
- [HeyGen MCP](mcp/heygen.md) — generate avatar videos, clone voices, and create speech from your agent. 🧩
- [ElevenLabs MCP](mcp/elevenlabs.md) — TTS, voice cloning, dubbing, and SFX as agent tools. 🧩 🔓
- [Cartesia MCP](mcp/cartesia.md) — low-latency realtime speech generation for agents. 🧩 🔓
- [Ideogram MCP](mcp/ideogram.md) — hosted image generation with real typography over MCP. 🧩
- [Karma.Domains](https://karma.domains/en/expired-domains-mcp/) — expired, auction and backorder domain search with backlink, authority and traffic metrics and Wayback history; hosted MCP server (OAuth or API key, Pro plan). 🔌 🧩
- [Playwright MCP](mcp/playwright.md) — drive a real browser for testing and scraping. 🧩 🔓
- [GitHub MCP](mcp/github.md) — issues, PRs, and repo actions from your agent. 🧩 🔓
- [Higgsfield](mcp/higgsfield.md) — cinematic video gen (API-first; how to drive it from an agent today). 🔌
- [Clawvisor](mcp/clawvisor.md) — API gateway that injects credentials at execution time; agent never sees your keys. Approve scopes once, get a full audit log. 🔓
- [Exa MCP](mcp/exa.md) — semantic web search returning structured JSON — the search MCP agents actually use in 2026. 🧩
- [Firecrawl MCP](mcp/firecrawl.md) — any URL → clean Markdown; crawl whole sites, extract structured data. 🧩
- [Stripe MCP](mcp/stripe.md) — inspect customers, subscriptions, and churn in plain language. 🧩
- [Supabase MCP](mcp/supabase-mcp.md) — query tables, run migrations, generate types, read logs from your agent. 🧩 🔓
- [Notion MCP](mcp/notion-mcp.md) — read/write Notion docs and databases as an agent tool. 🧩
- [Browserbase MCP](mcp/browserbase.md) — cloud browser for clicks, form fills, and screenshots when scraping isn't enough. 🧩
- [Sequential Thinking MCP](mcp/sequential-thinking.md) — externalises step-by-step reasoning; #1 by usage on Smithery. 🔓
- [Invompt](https://invompt.com) — drafts invoices and quotes from Claude, ChatGPT, or Cursor. You review each document before it is sent. Guest use needs no account. 🧩 🆓
- [looot](https://looot.ai) — one API key and prepaid balance for 2,500+ data endpoints (work emails, phones, company enrichment, Google SERP, web pages) over a remote MCP server; pay per call, no free tier. 🔌 🧩
- [Kleap](https://kleap.co/mcp) — hosted MCP (OAuth, 34 tools) and `npx kleap-cli` stdio server to create, edit, and publish websites. 🔌 🧩 🔓
- [CurlShot](https://curlshot.com) — screenshots a public URL as PNG, JPEG, WebP, PDF or scrolling video over one GET request or a remote MCP server; 100 free screenshots a month. 🔌 🧩 🆓

- [VideoGen MCP](https://videogen.io/videogen-mcp) — create videos, generate media, remix projects and export MP4s; requires VideoGen API access and paid generation credits. 🔌 🧩

- [Statsnet MCP](mcp/statsnet.md) — look up company registrations, executives, court records and finances through a remote MCP server; public company cards are free. 🧩 🆓

- [RestoSignals](https://restosignals.com) — finds US restaurants and bars 1-6 months before they open from public liquor-license, food-permit and business filings, scored with owner contact; remote MCP server and REST API, free API key. 🔌 🧩 🆓
- [ScraperSocial](https://scrapersocial.com/mcp/) — public social media data (profiles, posts, comments, search, video transcripts) from TikTok, Instagram, LinkedIn, YouTube, X, Reddit and 30+ platforms over one REST API or a remote MCP server; 100 free signup credits, then from $5/mo. 🔌 🧩

**More MCP servers:** [docs, search, data, email, and deploy servers worth wiring up in 2026](mcp/trending-2026.md).

**Registries to discover more:** [Official MCP Registry](https://github.com/modelcontextprotocol/registry) · [Smithery](https://smithery.ai) · [mcp.so](https://mcp.so) · [PulseMCP](https://www.pulsemcp.com) · [Glama](https://glama.ai/mcp/servers)

## Claude Skills & Plugins

A **Claude skill** is a reusable `.claude/skills` folder (markdown + scripts) that teaches Claude Code a repeatable workflow you can invoke by name. These are the trending ones solo builders install in 2026. **→ Full pages in [`skills/`](skills/).**

### Design & frontend
- [mblode/agent-skills](https://github.com/mblode/agent-skills) — Open-source collection of agent skills for UI audits, typography, documentation, PR review, and releases; installable with the skills CLI. 🔓
- [ui-ux-pro-max](skills/ui-ux-pro-max.md) — design-intelligence skill: 50+ styles, 161 palettes, 57 font pairings, picks a coherent design system from one prompt. 🔓
- [frontend-design](skills/frontend-design.md) — Anthropic's official skill that bans generic fonts and forces a deliberate aesthetic, killing AI-slop UI. 🔓
- [scroll-world](https://github.com/oso95/scroll-world) — agent skill that turns any brand into a scrollable 3D world: continuous scroll-driven camera fly-throughs, no cuts. 🔓

### SEO & growth
- [claude-seo](skills/claude-seo.md) — full SEO/GEO suite: technical audit, schema, E-E-A-T, backlinks, AI-search optimization, PDF reports. 🔓
- [NotFair](https://github.com/nowork-studio/NotFair) — Claude Code skills and plugin for SEO, GEO, Google Ads, and Meta Ads. 🔓

### Code quality & anti-slop
- [ponytail](skills/ponytail.md) — anti-over-engineering skill that makes the agent "think like the laziest senior dev"; ~54% less code on average. 🔓
- [redpen](https://github.com/yerdaulet-damir/redpen) — anti-slop *copywriting* skill: the old ad man with the red pen, every line must pass three questions (can I visualize it / falsify it / can nobody else say it) before it ships. Kills adjective-slop in headlines, landing pages, and taglines. 🔓
- [superpowers](skills/superpowers.md) — plan-first, TDD agentic framework (brainstorm → plan → subagent execution → review). 🔓
- [workkit](https://github.com/ITW-Creative-Works/workkit) - Claude Code plugin that runs GitHub Issues as a delivery pipeline: skills to triage, spec, build, review and ship each issue, checked by guard hooks and a scout, worker and verifier agent crew. 🆓
- [Context7](skills/context7.md) — injects up-to-date library docs so the agent stops hallucinating stale APIs. 🧩 🔓

### Official Anthropic skills
- [Anthropic Skills](https://github.com/anthropics/skills) — `pdf`, `docx`, `xlsx`, `pptx`, `mcp-builder`, `security-review`, and more. 🔓
- `/security-review` & `/commit` — built into Claude Code: scan a diff for vulns, write conventional commits.

> ⚠️ **Security note:** skills are just markdown + shell. A 2026 Snyk study found ~13% of tested community skills had critical flaws, some exfiltrating credentials. Read the `SKILL.md` before installing anything outside Anthropic or an established maintainer.

**More trending skills:** [browser control, reasoning, security, and research skills that gained traction in 2026](skills/trending-2026.md).

**Discover more:** [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) (canonical, curated) · [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) · [Claude Plugin Hub](https://www.claudepluginhub.com)

## Agent Memory & Knowledge

Give your agent a persistent brain beyond the codebase. **→ Full pages in [`memory/`](memory/).**

- [GBrain](memory/gbrain.md) — synthesis + graph + gap-analysis brain by Garry Tan (YC CEO); wire into Claude Code in one command. 🔓
- [Context7](skills/context7.md) — keeps the agent's library docs current. 🧩 🔓
- [Hyperconsciousness](https://github.com/louis030195/hyperconsciousness) - Developer-alpha encrypted, append-only knowledge store with a Rust CLI and scoped, expiring MCP access. 🧩 🔓
- [Mem0](https://github.com/mem0ai/mem0) — open-source memory layer for AI agents and apps. 🔓
- [Mnemoverse](https://mnemoverse.com) — hosted memory engine for AI agents, reached over MCP; tell it a recalled memory helped or misled, and it re-ranks what comes back next. 🔌 🧩 🆓
- [Screenpipe](https://screenpipe.com): Search locally captured screen text and audio transcripts for work recall and meeting notes via MCP or a local API; source-available under the Screenpipe Commercial License, with configured cloud services able to receive context. 🔌 🧩
- [ORANO Personal Context MCP](https://oranoai.com/mcp) — personal read-only remote MCP server (streamable HTTP, per-user Bearer key) that lets your agent search summaries and takeaways from videos, articles and PDFs you saved in ORANO. 🧩

## AI Coding Agents

- [Claude Code](https://claude.com/claude-code) — Anthropic's terminal/IDE coding agent; the hub of this stack. 🧩
- [NextReset](https://nextreset.ai/) — tracks source-linked Codex reset history and experimental forecasts, with a browser-local countdown timer. 🆓
- [Cursor](https://cursor.com) — the AI-native IDE. 🧩
- [Massvai](https://massvai.com) — builds exportable Next.js apps from prompts, with a live preview, Supabase, GitHub sync, and Vercel deployment. 🆓
- [Windsurf](https://windsurf.com) — agentic IDE with deep codebase awareness.
- [Cline](https://github.com/cline/cline) — open-source autonomous coding agent for VS Code. 🔓
- [Aider](https://aider.chat) — AI pair programming in your terminal. 🔓
- [Ivy Tendril](https://github.com/Ivy-Interactive/Ivy-Tendril) — desktop and web workspace for running coding agents in parallel Git worktrees with automated verification and review; FSL-1.1-ALv2 license.
- [YYLO](https://github.com/yylo-dev/yylo) — command-line orchestrator for coding agents with typed task, validation, merge, and release-readiness boundaries; each task runs in a dedicated branch/worktree behind a risk-based merge queue. 🔓 🆓
- [5dive](https://github.com/5dive-ai/5dive) — runs a team of AI agents on your own server. you hand them work from telegram. 🔓 🆓
- [OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) — records a coding-agent run beneath the harness, then replays it offline from the recorded bytes with no model called, or re-runs it from a chosen step on a different model. 🧩 🆓 🔓
- [Orbi](https://github.com/orbi-build/orbi) — self-hosted coding agent for GitHub repos: label an issue `ai-ready` and it writes the code, opens a PR, has an independent review session check it against the issue's acceptance criteria, merges, and tags a release. 🔓 🆓
- [Sillage](https://github.com/MarlBurroW/sillage) - self-hosted, mobile-first web UI that drives the native Claude Code and Codex CLIs on your own machine, with server-side sessions that outlive the client, full-text search across conversations, an IDE panel (files, editor, diffs, terminal), worktrees, and an installable PWA; single Docker container. 🧩 🆓 🔓
- [doany](https://doany.ai) — AI company builder: describe a business in plain words and it builds and hosts the website and product, takes Stripe payments, and helps with marketing and support. 🆓

## Automation & Agent Frameworks

- [Open-source AI agents you can self-host](agents/oss-agents.md), from personal assistants like OpenClaw and Hermes to coding agents like opencode, OpenHands, and Cline.
- [n8n](https://n8n.io) — open-source workflow automation with native AI nodes. 🔓
- [Make](https://make.com) — visual no-code automation for connecting AI tools.
- [Vercel AI SDK](https://sdk.vercel.ai) — TypeScript toolkit for building AI apps and agents. 🔓
- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful, controllable agent orchestration. 🔓
- [Mastra](https://mastra.ai) — TypeScript agent framework with workflows and memory. 🔓
- [CrewAI](https://crewai.com) — role-based multi-agent orchestration. 🔓
- [Frameworks for building fast](tools/frameworks-for-building.md) — web, full-stack, mobile, desktop, and AI SDK choices for solo products.
- [Agent Voice Response](https://github.com/agentvoiceresponse) — open-source platform to build and deploy AI voice agents (phone bots) wiring ASR + LLM + TTS. 🔓

## Frontend Motion & Design

Start with [How to Build Beautiful Websites Without AI Slop](guides/cinematic-frontend-not-slop.md): a curated directory organized by the page and interaction you need. Also available as a [readable web guide](https://yerdaulet-damir.github.io/awesome-solo-ai/frontend-design/).

- [Landing-page component libraries](tools/landing-page-libraries.md) — 21st.dev, React Bits, shadcn/ui, Tailark, Motion Primitives and other registries, compared by task.
- [Frontend motion](tools/frontend-motion.md) — GSAP vs Motion (Framer Motion), Lenis, Anime.js, native CSS, installation and reduced-motion considerations.
- [Design inspiration, fonts and icons](guides/cinematic-frontend-not-slop.md#web-design-inspiration-and-live-references) — Awwwards, Landing Love, Codrops, type references and icon families.
- [scroll-craft](https://github.com/nateherkai/scroll-craft) — agent workflow and supporting tools for scroll-driven websites, responsive composition and visual verification. 🔓
- [scroll-world](https://github.com/oso95/scroll-world) — builds a continuous scene/video journey scrubbed by scroll; generated media may require paid services. 🔓
- [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) and [ui-ux-pro-max](skills/ui-ux-pro-max.md) — agent instructions and design references; use them with a concrete brief and rendered-page review.

## Backend, Deploy & Analytics

The plumbing a solo builder needs to ship and run an AI product — picked for their AI-relevant angle, not as a generic dev-tools list.

- [Supabase](https://supabase.com) — Postgres + auth + storage with `pgvector` built in, so it doubles as the vector store for your RAG. 🔌 🔓
- [Prisma Postgres](https://www.prisma.io/postgres) - managed Postgres with zero cold starts and a no-card free plan; `npx create-db@latest` creates a database from the terminal, and the official MCP server lets agents manage it. 🔌 🧩 🆓
- [Vercel](https://vercel.com) — deploy in one push, plus the [AI SDK](https://sdk.vercel.ai) and [v0](https://v0.dev) for building AI UIs. 🔌
- [Prisma Compute](https://www.prisma.io/compute) - hosts TypeScript apps and AI agents (Node.js, Bun or Next.js) next to Prisma Postgres, with streamed responses and scale to zero when idle; free plan includes 1M requests/month. 🧩 🆓
- [PostHog](https://posthog.com) — product analytics, session replay, and LLM analytics to track AI feature cost and quality. 🔌 🔓
- [Self-hosted analytics for solo builders](guides/self-hosted-analytics.md), open-source web, product, and LLM observability you can own (Umami, Plausible, Langfuse, Helicone) plus analytics MCP servers.
- [Convex](https://convex.dev) — reactive backend with first-class AI agent and workflow support. 🔌
- [Clerk](https://clerk.com) — drop-in auth so you skip building login. 🔌
- [tgx](https://github.com/yerdaulet-damir/tgx) — TypeScript framework for building Telegram bots fast on grammY; state, Stars payments and menus built in, and designed to be built by AI agents (ships an MCP server). 🔓
- [Gemmein](https://gemmein.com/r/dir) — backend for web and mobile apps: sign-in, protected data, payments and AI tools, with security on by default. 🔌

## Distribution & Marketing

Building is half the job — this is how a solo builder gets users. **Where to launch, how to grow, and the tactics that work** — see the [launch playbook](playbooks/launch-and-get-first-users.md).

**Research what to build**
- [IdeaHunter](https://ideahunter.today) — turns public buyer pain and market signals into scoped app ideas with source evidence, MVP boundaries, and a validation step. 🆓
- [FalcoScan](https://falcoscan.com) — searchable AI product database with market activity, competition, and opportunity signals; includes an API and MCP server. 🔌 🧩

- [LaunchSpy](https://launchspy.io) — tracks Meta ads, funnels and software used by course creators, coaches and community owners; [API and MCP access](https://launchspy.io/mcp) require Pro or Business. 🔌 🧩

**Where to launch**
- [AI tool and MCP directories](distribution/ai-mcp-directories.md) — submission routes for products, servers and awesome lists, with paid listings and paused intake called out.
- [Product Hunt](https://producthunt.com) — the classic launch-day spike for tools and SaaS.
- [Hacker News](https://news.ycombinator.com) — "Show HN" for dev/technical products; high-signal traffic.
- [Reddit](https://reddit.com) — niche subs (r/SideProject, r/indiehackers) — and the #1 source AI engines cite.
- [Indie Hackers](https://indiehackers.com) — community of solo founders sharing what works.
- [Peerlist](https://peerlist.io) — launchpad and network for builders.
- [CodeTrendy](https://codetrendy.com) — directory for newly launched startups, SaaS and indie products; each submission passes an automated content check and staff may reject it, approved listings get their own page. Free listing needs an account and a CodeTrendy badge on your homepage; paid plans from $19 per listing, homepage featured placement from $39 one time or $30 per month. 🆓
- [startup-directories](https://github.com/saidbouig/startup-directories) — 214 startup and launch directories with what the free route gives, the measured link type and the date checked. 🆓 🔓

**Grow & post**
- [Marketing, SEO, and social from Claude Code](distribution/marketing-from-claude.md), the growth skills and MCP servers a solo builder runs straight from the terminal.
- [Social media automation, human in the loop](distribution/social-media-automation.md), self-hosted schedulers and cross-posting for X, LinkedIn, Reddit, and Threads (Postiz, Mixpost, praw, xMCP).
- [Typefully](https://typefully.com) — write, schedule, and grow on X/Threads.
- [Buffer](https://buffer.com) — schedule across every social channel.
- [LaunchGrill](https://launchgrill.com) — scores a landing page 0–100 against a published 18-test checklist, quoting the page for each finding. 🆓
- [SocialEcho](https://www.socialecho.net) — publish, monitor, analyze, and manage messages across eleven social platforms from one workspace. 🆓
- [Autoposting](https://autoposting.ai) — write in your own voice, clip long video, and schedule to X, LinkedIn, Instagram, Threads and YouTube.
- [BulkPublish social media content skills](https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills) — reusable, agent-agnostic skills for planning, adapting, reviewing, scheduling, and publishing social content through the [BulkPublish API](https://github.com/azeemkafridi/bulkpublish-api), with [MCP documentation](https://app.bulkpublish.com/docs). 🔌 🧩 🔓
- [claude-seo](skills/claude-seo.md) — SEO + GEO so search and AI engines surface you. 🔓
- [LLM Pulse](https://llmpulse.ai/) — tracks brand mentions, citations, sentiment, and competitor share of voice across AI search engines. 🔌 🧩
- [Robot Speed](https://www.robot-speed.com/mcp) — hosted SEO and AI-visibility MCP. OAuth endpoint has 39 tools; `/api/mcp/free` is no-auth and has 12. 🔌 🧩 🆓 🔓
- [LogNorm](https://lognorm.com) — hosted MCP server that gives Claude Code, Codex and Cursor a ranked backlog of SEO and AI-visibility fixes, content and research for your site; OAuth, no API keys. Free plan, paid from $99/mo. 🧩 🆓
- [Said by AI](https://www.saidbyai.com/) — asks GPT-4o mini 20 buyer-style questions about your category in three answer styles and reports how often your brand is named, which competitors are named instead, and what to change; one-time audit, free 5-question check. 🆓
- [NeverDrafts](https://www.neverdrafts.com) — checks brand mentions and citations across ChatGPT, Claude, Google AI Mode and Perplexity, then drafts content and publishes it to WordPress, Webflow or Framer; free audit, paid monitoring.
- [AltoRank](https://altorank.co) — SEO content software for keyword research, site readiness checks and drafts with sources for human review; [self-hosted](https://github.com/AltoRank/altorank) under AGPL-3.0 or hosted, with an official MCP server. 🧩 🔓
- [SEO and GEO tools](distribution/seo-geo-tools.md), skills and MCP servers to rank in Google and get cited by ChatGPT and Perplexity.
- [Drevon](https://www.drevon.dev) — Mac app that runs Claude Code or Codex agents in a browser with your existing logins (LinkedIn, Sales Navigator, Reddit) to research prospects and accounts, with MCP connectors for CRM, enrichment and outreach tools such as HubSpot, Clay and Smartlead; results saved as CSV, JSON or Markdown. 🆓

**Make the content**
- [Faceless content factory](playbooks/faceless-content-factory.md) — turn the [video](#video-generation), [voice](#voice-tts--cloning), and [avatar](#ai-avatars--talking-heads) tools above into a posting machine.
- [shortshort](https://www.shortshort.io) — turns long videos into vertical clips with face tracking and word-by-word captions; includes a limited free AI trial.
- [ScaleReach](https://www.scalereach.ai) - turns long videos into vertical 9:16 clips with AI captions and face-tracking crop, and schedules them to social accounts. 🔌 🧩
- [kdpbook.io](https://kdpbook.io) — describe a book in a chat and get the Amazon KDP files: print PDF, full-wrap cover, Kindle EPUB and listing sheet; includes 2,000 free credits at signup (free-plan exports are watermarked).
- [ImagineYourBook](https://www.imagineyourbook.com/) - plans and drafts full-length books, rewrites manuscripts in the author's voice, keeps series continuity with a story bible, and exports EPUB, Word, or Markdown.

---

## 🔨 Build Your Own AI X

Step-by-step guides to ship real AI products solo. Each guide names the exact stack, the steps, and what it costs — so you know what you're getting into before you start. See [`/build`](build/).

- [Build your own MCP server](build/your-own-mcp-server.md) — turn any API into a Claude Code tool, in an afternoon
- [Build your own AI voice app](build/your-own-ai-voice-app.md) — TTS, cloning, or a full voice assistant
- [Build your own AI SaaS](build/your-own-ai-saas.md) — the full revenue stack, $0 to first $100 MRR
- [Build your own AI avatar video pipeline](build/your-own-avatar-video.md) — script → voice → talking head, fully automated
- [Build your own RAG chatbot over your docs](build/your-own-rag-chatbot.md) — ingest any docs, deploy a chatbot in a weekend
- [Build your own AI Chrome extension](build/your-own-ai-chrome-extension.md) — the lowest-CAC AI product model
- [Build your own faceless content machine](build/your-own-faceless-content-machine.md) — one idea → video → published, no face required
- [Build your own AI agent](build/your-own-ai-agent.md) — a scheduled job that runs without you

---

## Guides

Hands-on, practical tutorials — Karpathy/Kaggle energy, not theory. See [`/guides`](guides).

- [How to edit videos with Claude Code (no manual editing)](guides/edit-video-with-claude.md)
- [AI video editing and faceless video repos (MCP servers, pipelines, frameworks)](guides/ai-video-editing-repos.md)
- [How to build automations without code](guides/automations-without-code.md)
- [How to eliminate AI-slop code and write production-grade code](guides/kill-ai-slop-code.md)
- [Beautiful websites without AI slop: frontend libraries, design references and agent skills](guides/cinematic-frontend-not-slop.md)

## Playbooks

End-to-end workflows a solo builder can copy. See [`/playbooks`](playbooks).

- [Faceless short-form content factory (script → voice → avatar → publish)](playbooks/faceless-content-factory.md)
- [Ship a SaaS solo with Claude Code + MCP](playbooks/solo-saas-with-claude.md)
- [Launch and get your first users (solo)](playbooks/launch-and-get-first-users.md)
- [Build a RAG chatbot over your docs in a weekend](playbooks/rag-chatbot-over-docs.md)
- [Turn a YouTube channel into a newsletter + content flywheel](playbooks/youtube-to-newsletter.md)
- [Ship an AI Chrome extension in 72 hours](playbooks/ai-chrome-extension.md)
- [Automate cold outreach personalization at scale](playbooks/cold-outreach-personalization.md)
- [Repurpose one idea into 10 content formats automatically](playbooks/content-repurposing-flywheel.md)
- [Vibe-code an MVP in a weekend](playbooks/vibe-code-mvp-weekend.md)
- [Automate a full SaaS billing + onboarding flow](playbooks/saas-billing-onboarding.md)
- [Build in public: tools and playbook for GitHub, X, and Reddit](playbooks/build-in-public.md)

---

## FAQ

**How do I edit videos with Claude / without code?**
Wire a video tool's MCP server (e.g. [HeyGen MCP](#mcp-servers) or [ElevenLabs MCP](#mcp-servers)) into Claude Code, then describe the edit in plain language. See [the guide](guides/edit-video-with-claude.md).

**Where is the HeyGen MCP / where is the Higgsfield MCP?**
[HeyGen ships an official MCP server](mcp/heygen.md). [Higgsfield is API-first](mcp/higgsfield.md) — drive it from an agent via its REST API or a thin MCP wrapper until an official server lands.

**How do solo builders make talking-head / avatar videos at scale?**
Clone yourself once in [HeyGen](#ai-avatars--talking-heads) or [Argil](#ai-avatars--talking-heads), then generate from scripts via API. Full pipeline in [the playbook](playbooks/faceless-content-factory.md).

**How do I write production code with AI and avoid AI slop?**
Use a verify-driven loop, tight scope, and review gates — see [Eliminate AI-slop code](guides/kill-ai-slop-code.md).

**How do I build no-code automations between AI tools?**
Use [n8n](#automation--agent-frameworks) or [Make](#automation--agent-frameworks); guide [here](guides/automations-without-code.md).

**What is the ui-ux-pro-max skill?**
[ui-ux-pro-max](skills/ui-ux-pro-max.md) is a Claude Code skill that gives the agent a design knowledge base — 50+ styles, 161 color palettes, and font pairings — so it produces a coherent, non-generic design system from a single prompt, no designer needed.

**What is the ponytail skill?**
[ponytail](skills/ponytail.md) is a Claude Code skill that makes the agent prefer native platform features over hand-built code — "think like the laziest senior dev" — cutting roughly half the code it writes and reducing token cost.

**What is the best Claude skill for SEO?**
[claude-seo](skills/claude-seo.md) is the most complete Claude Code SEO skill: technical audits, schema, E-E-A-T, backlinks, and GEO optimization for AI search, with PDF/Excel reports.

---

## Contributing

PRs and submissions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Rules: the tool must be **live**, the description **one neutral factual line**, and you must note 🔌/🧩/🆓/🔓 accurately. Dead or deprecated tools get cut.

## Maintained by

Built and curated by **[Yerdaulet Damir](https://yerdaulet.xyz)** — an AI engineer and AI-native developer who works at CTO / tech-lead level: senior, high-agency, full end-to-end ownership, with real product taste. Part builder, part indie researcher. Ships AI agents and AI SaaS (one platform does 20k+ video/image generations a month), wrote the low-code & vibe-coding course for Astana Hub — Central Asia's largest tech hub — and will take any problem, at any level, and grind it to done. Sits, builds, hustles ~18 hours a day.

[yerdaulet.xyz](https://yerdaulet.xyz) · [GitHub](https://github.com/yerdaulet-damir) · [X](https://x.com/aimyerdaulet) · [LinkedIn](https://linkedin.com/in/yerdaulet-damir) — open to building with ambitious teams (YC · SF · London).

> 💬 If this saved you time, a ⭐ helps others find it. Building something or hiring? [Reach out](https://yerdaulet.xyz).

<!-- Sponsors -->
## Sponsors

_This list's curated entries are never paid placements._ Want your tool featured in a clearly-marked sponsor slot? [Get in touch](mailto:yerdauletdev@gmail.com).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/80x15.png)](LICENSE) — released under [CC0](LICENSE). Public domain; remix freely.
