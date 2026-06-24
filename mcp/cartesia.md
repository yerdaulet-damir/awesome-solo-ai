# Cartesia MCP — realtime low-latency speech

> The fastest text-to-speech for agents that need to talk back in real time.

## What is the Cartesia MCP server?

**The Cartesia MCP server exposes Cartesia's ultra-low-latency text-to-speech to an AI agent over the Model Context Protocol.** Its Sonic models generate speech with around 90ms time-to-first-byte and clone a voice from roughly three seconds of audio — built for realtime, conversational use. The server is open-source and maintained by Cartesia.

## Why it matters for solo builders

When you're building a voice agent, a phone bot, or any product where the user waits for a reply, latency is the experience. Cartesia is the pick when [ElevenLabs](elevenlabs.md) quality is less important than instant response.

## What you can do with it

- Realtime speech for conversational agents.
- Fast voice cloning for a custom narrator.

## Example

> "Stream this assistant reply as speech in my cloned voice with minimal delay."

## Setup

Get a Cartesia API key, then add the [cartesia-mcp](https://github.com/cartesia-ai/cartesia-mcp) server to your Claude Code MCP config.

## Related

- [ElevenLabs MCP](elevenlabs.md) — higher quality, slightly higher latency.
- [Voice, TTS & Cloning tools](../README.md#voice-tts--cloning).

## Source

[github.com/cartesia-ai/cartesia-mcp](https://github.com/cartesia-ai/cartesia-mcp) · [cartesia.ai](https://cartesia.ai)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
