# Higgsfield — cinematic AI video (and how to drive it from an agent)

> Where is the Higgsfield MCP? Higgsfield is API-first today — here's how to call it from Claude Code right now.

## What is Higgsfield?

**Higgsfield is an AI video generation platform built for social creators, known for cinematic camera-control and motion presets.** You describe a shot — a dolly-in, an orbit, a specific motion style — and it generates short-form video tuned for TikTok, Reels, and Shorts.

## Does Higgsfield have an MCP server?

As of mid-2026 Higgsfield is **API-first and does not ship an official MCP server**. That doesn't block agent use — you can drive it from Claude Code in two ways:

1. **Direct API calls** — have the agent hit Higgsfield's REST API via a generic HTTP tool with your API key.
2. **A thin MCP wrapper** — wrap the API in a small custom MCP server (Anthropic's `mcp-builder` skill scaffolds one in minutes), so it appears as native agent tools.

If an official MCP server ships later, this page will point to it.

## Why it matters for solo builders

Higgsfield's camera-control output looks shot, not generated — the difference between scroll-past and watchable for a faceless channel. Wiring it behind an agent lets you batch-generate cinematic B-roll from a list of prompts.

## Example

> "For each line in `shots.txt`, generate a Higgsfield clip with an orbit camera move, and save them to `/broll`."

The agent loops the API call per prompt.

## Related

- [Video generation tools](../README.md#video-generation) — Runway, Kling, Veo, Sora alternatives.
- [Faceless Content Factory](../playbooks/faceless-content-factory.md).
- [mcp-builder skill](../skills/README.md) — scaffold the wrapper.

## Source

[higgsfield.ai](https://higgsfield.ai)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
