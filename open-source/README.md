# Open-Source Alternatives

Every closed tool in the solo AI stack has an open-source alternative you can self-host. Sometimes the OSS version is genuinely better. Sometimes it saves you $300/month. Sometimes it just keeps your data on your own infrastructure. This section maps the full closed → open landscape so you can make the call with real information.

## The map

| Closed Tool | OSS Alternative | GitHub | License | Verdict |
| --- | --- | --- | --- | --- |
| ElevenLabs | Kokoro-TTS | [hexgrad/kokoro](https://github.com/hexgrad/kokoro) (~30k★) | Apache 2.0 | Strong. Runs locally, near-ElevenLabs quality on English. |
| ElevenLabs | Chatterbox | [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) (~15k★) | MIT | Good voice cloning from short samples. |
| Midjourney | FLUX.1 | [black-forest-labs/flux](https://github.com/black-forest-labs/flux) | Apache 2.0 | Closest OSS to MJ quality. Needs GPU or replicate.com. |
| Midjourney | ComfyUI | [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) (~75k★) | GPL-3.0 | Node-based workflow editor for all diffusion models. |
| Zapier / Make | n8n | [n8n-io/n8n](https://github.com/n8n-io/n8n) (~190k★) | fair-code | Best-in-class self-hosted automation. Most Zapier workflows port directly. |
| Zapier / Make | Activepieces | [activepieces/activepieces](https://github.com/activepieces/activepieces) (~12k★) | MIT | Cleaner UI than n8n, growing connector library. |
| Notion | AppFlowy | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) (~73k★) | AGPL | Best Notion OSS clone. Offline-first, Rust backend. |
| Notion | AFFiNE | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) (~60k★) | MIT | Canvas + docs hybrid. Different UX from Notion, worth evaluating. |
| Cursor / Copilot | opencode | [sst/opencode](https://github.com/sst/opencode) (~176k★) | MIT | Terminal-native coding agent. Bring your own API key. |
| Cursor / Copilot | Cline | [cline/cline](https://github.com/cline/cline) (~63k★) | Apache 2.0 | VS Code extension. Full agentic loop with tool use. |
| Perplexity | Perplexica | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) (~20k★) | MIT | Self-hosted AI search. SearXNG under the hood. |
| Perplexity | Khoj | [khoj-ai/khoj](https://github.com/khoj-ai/khoj) (~25k★) | AGPL | Personal AI assistant with web + doc search. |
| ChatGPT UI | Open WebUI | [open-webui/open-webui](https://github.com/open-webui/open-webui) (~124k★) | MIT | Best self-hosted multi-model chat UI. Ollama + OpenAI compatible. |
| ChatGPT UI | LibreChat | [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (~37k★) | MIT | Feature-rich, supports agents and code interpreter. |
| Vercel | Coolify | [coollabsio/coolify](https://github.com/coollabsio/coolify) (~56k★) | Apache 2.0 | Best self-hosted Heroku/Vercel alternative. See [self-hosted-infra.md](self-hosted-infra.md). |
| Vercel | Dokploy | [Dokploy/dokploy](https://github.com/Dokploy/dokploy) (~24k★) | Apache 2.0 | Lighter than Coolify, simpler mental model. |
| Airtable | NocoDB | [nocodb/nocodb](https://github.com/nocodb/nocodb) (~62k★) | AGPL | Spreadsheet UI over any Postgres/MySQL. Best Airtable OSS substitute. |
| Airtable | Baserow | [baserow/baserow](https://github.com/baserow/baserow) | MIT | Cleaner than NocoDB for non-technical users. |
| Retool | ToolJet | [ToolJet/ToolJet](https://github.com/ToolJet/ToolJet) (~35k★) | AGPL | Drag-and-drop internal tool builder. |
| Retool | Appsmith | [appsmithorg/appsmith](https://github.com/appsmithorg/appsmith) (~35k★) | Apache 2.0 | Strong JS customization, good for complex internal apps. |
| Calendly | Cal.com | [calcom/cal.com](https://github.com/calcom/cal.com) (~33k★) | AGPL | Full scheduling infrastructure. Self-host or use their cloud. |
| LangSmith | Langfuse | [langfuse/langfuse](https://github.com/langfuse/langfuse) (~21k★) | MIT | LLM observability, tracing, and evals. See [self-hosted-infra.md](self-hosted-infra.md). |
| Loom | Cap | [CapSoftware/Cap](https://github.com/CapSoftware/Cap) (~20k★) | MIT | Open-source screen recording. S3 for storage, your own infrastructure. |
| Auth0 / Clerk | Better Auth | [better-auth/better-auth](https://github.com/better-auth/better-auth) (~29k★) | MIT | TypeScript-first. Easiest drop-in for Next.js projects. |
| Auth0 / Clerk | Authentik | [goauthentik/authentik](https://github.com/goauthentik/authentik) (~22k★) | MIT | Enterprise-grade identity provider, SAML/OIDC/LDAP. |
| Algolia | Meilisearch | [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch) (~56k★) | MIT | Typo-tolerant, fast, simple API. See [self-hosted-infra.md](self-hosted-infra.md). |
| Algolia | Typesense | [typesense/typesense](https://github.com/typesense/typesense) (~25k★) | GPL-3.0 | Fast, simpler to configure than Elasticsearch. |
| Intercom | Chatwoot | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) (~33k★) | MIT | Omnichannel customer support. Solid Intercom replacement. |
| Linear | Plane | [makeplane/plane](https://github.com/makeplane/plane) (~53k★) | AGPL | Issue tracking + roadmaps. Most feature-complete Linear OSS alternative. |
| Figma | Penpot | [penpot/penpot](https://github.com/penpot/penpot) (~53k★) | MPL-2.0 | Browser-based design tool. SVG-native, strong component system. |
| Suno | AudioCraft / MusicGen | [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) (Meta, ~23k★) | MIT | Generates music from text prompts. Quality gap vs Suno is significant. |
| HeyGen | MuseTalk | [TMElyralab/MuseTalk](https://github.com/TMElyralab/MuseTalk) (~6k★) | MIT | Real-time lip sync for talking-head video. Functional but far behind HeyGen. |

## Two real gaps

**Suno** has no real open-source equal. AudioCraft / MusicGen generates music from text, but the production quality, musicality, and lyric handling are noticeably weaker. If AI music generation is central to your workflow, Suno or Udio are still the answer — there's no credible self-hosted substitute.

**HeyGen** (realistic AI avatars with lip sync) is a harder problem. MuseTalk does lip sync on existing video, and it works, but the output quality, expression range, and ease of use are far behind what HeyGen produces. The gap here is compute and proprietary training data. Watch this space — it's closing faster than music, but it's not close yet.

## Deeper dives

- [Open-source coding agents](coding-agents.md) — opencode vs Cline vs Aider vs Continue, when to use each
- [Self-hosted infra stack](self-hosted-infra.md) — Coolify + NocoDB + n8n + Langfuse + Meilisearch, the full setup

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
