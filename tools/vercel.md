# Vercel — deploy in one push, plus AI building blocks

> Ship a frontend to production in one push, and build AI UIs with the AI SDK and v0.

## What is Vercel?

**Vercel is a deployment platform for web apps that ships your frontend to production from a single git push, and it makes the AI SDK and v0 — tools for building and generating AI-powered interfaces.** For a solo builder it removes DevOps and provides first-class primitives for streaming LLM responses and tool-calling.

## Quick facts

- **Website:** [vercel.com](https://vercel.com)
- **API:** yes — REST API + the [AI SDK](https://sdk.vercel.ai) (TypeScript)
- **CLI:** yes — `vercel` CLI to deploy and manage
- **MCP:** community MCP servers for deploys/log access exist
- **Free tier:** yes — Hobby tier for personal projects
- **Extras:** [v0](https://v0.dev) generates UI from prompts

## What you build with it

- Deploy a Next.js/any app to production instantly.
- Stream LLM output and tool calls with the AI SDK.
- Prototype UI fast with v0, then ship it.

## Example

```bash
vercel        # preview deploy
vercel --prod # promote to production
```

## Alternatives

[Convex](https://convex.dev) for backend+deploy together; Netlify/Cloudflare for hosting. See [Backend tools](../README.md#backend-deploy--analytics).

## Source

[vercel.com](https://vercel.com) · [AI SDK](https://sdk.vercel.ai) · [v0](https://v0.dev)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
