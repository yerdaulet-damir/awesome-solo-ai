# Awesome Solo AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The home base for **solopreneurs, indie hackers, and solo founders** — every AI tool, Claude skill, MCP server, playbook, and growth tactic to **build *and* grow** a one-person company, curated and kept fresh, that you feed to Claude Code.

> _"The best companies of the next decade will be built by one person with the right tools and the discipline to ship."_

**A solo AI stack is the set of tools, Claude skills, MCP servers, and playbooks a one-person business uses to build, ship, and grow a product — making video, voice, images, code, automations, and distribution without hiring a team.** This list curates that stack: every entry is verified, dead links are pruned, and the whole thing is published as [`llms.txt`](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/llms.txt) so your AI agent can read it and call any tool here.

_Last updated: June 2026 · Curated by a working solo builder, not auto-generated._

💸 **On a budget?** See the [Free Solo AI Stack](free-solo-ai-stack.md) — only tools with real free tiers or open-source licenses, enough to launch for $0.

🤖 **Feed this to your agent.** Point Claude Code, Cursor, or any MCP-aware tool at the raw list and ask it to find the right tool for the job:
> `Read https://raw.githubusercontent.com/yerdaulet-damir/awesome-solo-ai/main/llms.txt — which tool here generates a talking-head avatar video, and does it have an MCP server?`

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
- [Pika](https://pika.art) — creator-friendly video gen with effects and editing. 🔌
- [Hailuo / MiniMax](https://hailuoai.video) — high-quality cinematic video gen from text or image. 🔌
- [Hedra](https://www.hedra.com) — character-driven video and expressive talking characters. 🔌

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

## MCP Servers

Model Context Protocol servers let your agent *do things*, not just chat. These are the ones a solo builder wires into Claude Code. **→ Full pages in [`mcp/`](mcp/).**

- [HeyGen MCP](mcp/heygen.md) — generate avatar videos, clone voices, and create speech from your agent. 🧩
- [ElevenLabs MCP](mcp/elevenlabs.md) — TTS, voice cloning, dubbing, and SFX as agent tools. 🧩 🔓
- [Cartesia MCP](mcp/cartesia.md) — low-latency realtime speech generation for agents. 🧩 🔓
- [Ideogram MCP](mcp/ideogram.md) — hosted image generation with real typography over MCP. 🧩
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

**Registries to discover more:** [Official MCP Registry](https://github.com/modelcontextprotocol/registry) · [Smithery](https://smithery.ai) · [mcp.so](https://mcp.so) · [PulseMCP](https://www.pulsemcp.com) · [Glama](https://glama.ai/mcp/servers)

## Claude Skills & Plugins

A **Claude skill** is a reusable `.claude/skills` folder (markdown + scripts) that teaches Claude Code a repeatable workflow you can invoke by name. These are the trending ones solo builders install in 2026. **→ Full pages in [`skills/`](skills/).**

### Design & frontend
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
- [Mem0](https://github.com/mem0ai/mem0) — open-source memory layer for AI agents and apps. 🔓

## AI Coding Agents

- [Claude Code](https://claude.com/claude-code) — Anthropic's terminal/IDE coding agent; the hub of this stack. 🧩
- [Cursor](https://cursor.com) — the AI-native IDE. 🧩
- [Windsurf](https://windsurf.com) — agentic IDE with deep codebase awareness.
- [Cline](https://github.com/cline/cline) — open-source autonomous coding agent for VS Code. 🔓
- [Aider](https://aider.chat) — AI pair programming in your terminal. 🔓

## Automation & Agent Frameworks

- [n8n](https://n8n.io) — open-source workflow automation with native AI nodes. 🔓
- [Make](https://make.com) — visual no-code automation for connecting AI tools.
- [Vercel AI SDK](https://sdk.vercel.ai) — TypeScript toolkit for building AI apps and agents. 🔓
- [LangGraph](https://github.com/langchain-ai/langgraph) — stateful, controllable agent orchestration. 🔓
- [Mastra](https://mastra.ai) — TypeScript agent framework with workflows and memory. 🔓
- [CrewAI](https://crewai.com) — role-based multi-agent orchestration. 🔓
- [Agent Voice Response](https://github.com/agentvoiceresponse) — open-source platform to build and deploy AI voice agents (phone bots) wiring ASR + LLM + TTS. 🔓

## Frontend Motion & Design

The libraries that separate cinematic from slop. **→ Full stack page: [tools/frontend-motion.md](tools/frontend-motion.md) · Guide: [How to make your frontend not look like AI slop](guides/cinematic-frontend-not-slop.md)**

- [GSAP + ScrollTrigger](tools/frontend-motion.md) — industry-standard animation engine; scroll-pinned scenes, scrubbed timelines, staggered reveals. Free for most use. 🔌 🆓
- [Lenis](tools/frontend-motion.md) — smooth-scroll inertia wrapper; 6 lines to wire into GSAP. MIT. 🆓 🔓
- [Framer Motion / Motion](tools/frontend-motion.md) — declarative React animation: `whileInView`, `AnimatePresence`, layout animations. MIT. 🆓 🔓
- [ui-ux-pro-max skill](skills/ui-ux-pro-max.md) — 161 palettes + 57 font pairings as Claude context; pick the design system before writing a line of code. 🔓
- [award-winning-motion skill](https://github.com/anthropics/skills) — GSAP + ScrollTrigger + Lenis playbook as a Claude skill: cinematic preloaders, scroll-zoom, scrub. 🔓
- [scroll-world skill](https://github.com/anthropics/skills) — scroll-driven narrative sequencing; each section escalates one story. 🔓

## Backend, Deploy & Analytics

The plumbing a solo builder needs to ship and run an AI product — picked for their AI-relevant angle, not as a generic dev-tools list.

- [Supabase](https://supabase.com) — Postgres + auth + storage with `pgvector` built in, so it doubles as the vector store for your RAG. 🔌 🔓
- [Vercel](https://vercel.com) — deploy in one push, plus the [AI SDK](https://sdk.vercel.ai) and [v0](https://v0.dev) for building AI UIs. 🔌
- [PostHog](https://posthog.com) — product analytics, session replay, and LLM analytics to track AI feature cost and quality. 🔌 🔓
- [Convex](https://convex.dev) — reactive backend with first-class AI agent and workflow support. 🔌
- [Clerk](https://clerk.com) — drop-in auth so you skip building login. 🔌
- [tgx](https://github.com/yerdaulet-damir/tgx) — TypeScript framework for building Telegram bots fast on grammY; state, Stars payments and menus built in, and designed to be built by AI agents (ships an MCP server). 🔓

## Distribution & Marketing

Building is half the job — this is how a solo builder gets users. **Where to launch, how to grow, and the tactics that work** — see the [launch playbook](playbooks/launch-and-get-first-users.md).

**Where to launch**
- [Product Hunt](https://producthunt.com) — the classic launch-day spike for tools and SaaS.
- [Hacker News](https://news.ycombinator.com) — "Show HN" for dev/technical products; high-signal traffic.
- [Reddit](https://reddit.com) — niche subs (r/SideProject, r/indiehackers) — and the #1 source AI engines cite.
- [Indie Hackers](https://indiehackers.com) — community of solo founders sharing what works.
- [Peerlist](https://peerlist.io) — launchpad and network for builders.

**Grow & post**
- [Marketing, SEO, and social from Claude Code](distribution/marketing-from-claude.md), the growth skills and MCP servers a solo builder runs straight from the terminal.
- [Typefully](https://typefully.com) — write, schedule, and grow on X/Threads.
- [Buffer](https://buffer.com) — schedule across every social channel.
- [claude-seo](skills/claude-seo.md) — SEO + GEO so search and AI engines surface you. 🔓

**Make the content**
- [Faceless content factory](playbooks/faceless-content-factory.md) — turn the [video](#video-generation), [voice](#voice-tts--cloning), and [avatar](#ai-avatars--talking-heads) tools above into a posting machine.

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
- [How to make your AI-generated frontend not look like slop (GSAP + Lenis + Framer Motion)](guides/cinematic-frontend-not-slop.md)

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
