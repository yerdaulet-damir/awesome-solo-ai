# Build Your Own AI Voice App

> Clone a voice, add TTS to your product, or build a full voice assistant — for free to start.

## What you're building

An AI voice app is any product that converts text to natural-sounding speech, optionally using a cloned or designed voice. The end result can be as simple as a "read aloud" button on a web page or as complex as a real-time voice assistant that responds to microphone input. This guide covers the full range — TTS integration, voice cloning, and wiring audio to a frontend — using ElevenLabs for generation and Cartesia's MCP for in-context voice control from Claude Code.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| Voice generation + cloning | ElevenLabs | Best quality TTS in 2026, voice cloning in under 60 seconds, generous free tier | [tools/elevenlabs.md](../tools/elevenlabs.md) |
| In-agent voice control | Cartesia MCP | Call TTS endpoints directly from Claude Code during development — no API client needed | [mcp/cartesia.md](../mcp/cartesia.md) |
| Database + auth | Supabase | Stores user voice preferences, usage records, and API keys server-side | [tools/supabase.md](../tools/supabase.md) |
| Deployment | Vercel | Edge functions handle TTS proxying; zero cold starts on the audio endpoint | [tools/vercel.md](../tools/vercel.md) |

## Build it

**Step 1 — Define the voice use case.** Narrow to one before you write code: a text-to-speech button, a podcast generator, a voice assistant, or a custom voice for your product. Each has different latency requirements and different cost profiles. A "read aloud" feature on a blog tolerates two seconds of generation delay; a real-time voice assistant does not.

**Step 2 — Get an ElevenLabs API key.** Sign up at elevenlabs.io, grab your key from the profile dashboard, and store it as an environment variable (`ELEVENLABS_API_KEY`). Verify it works by calling `/v1/text-to-speech/{voice_id}` with curl — you should get a playable MP3 back in under a second for short text.

**Step 3 — Integrate the TTS endpoint.** In a Next.js API route (or Vercel Edge Function), POST the user's text to ElevenLabs and stream the audio response back to the client. Use ElevenLabs' streaming endpoint (`/v1/text-to-speech/{voice_id}/stream`) rather than the download endpoint so audio starts playing before the full file is generated. Set `Content-Type: audio/mpeg` and pipe the response body directly.

**Step 4 — Add voice cloning (optional).** Upload a one-minute clean audio sample to ElevenLabs' Voice Lab via the API (`POST /v1/voices/add`). ElevenLabs returns a `voice_id` within seconds. Swap that ID into your TTS calls. For a product, store each user's `voice_id` in Supabase tied to their user row so they get their own voice on every request.

**Step 5 — Wire audio to your app UI.** On the frontend, fetch the TTS endpoint and play the result with the Web Audio API or a simple `<audio>` element with `src` set to an object URL. For streaming playback, use `MediaSource` with chunked fetch. ElevenLabs' JS SDK wraps all of this — install with `npm i elevenlabs` and call `stream()` with three lines.

**Step 6 — Deploy.** Push to Vercel. Set `ELEVENLABS_API_KEY` in the Vercel environment variables dashboard. Your TTS endpoint is now a global edge function — sub-200ms to first byte from most regions. Add Supabase RLS policies so users can only read their own voice IDs.

## What it costs

ElevenLabs' free tier covers 10,000 characters per month — enough to prototype and demo. The Starter plan ($5/mo) adds 30,000 characters; Creator ($22/mo) adds 100,000 characters and one-click voice cloning. Cartesia MCP is free to run locally. Supabase and Vercel are both free up to meaningful traffic. Your first 100 users paying nothing costs you nothing beyond ElevenLabs Starter.

## Real examples

Beehiiv newsletters added a "listen to this issue" feature powered by ElevenLabs — each issue generates a full audio version automatically on publish. The solo builder who shipped it wrote roughly 40 lines of webhook handler code; ElevenLabs does the rest.

A solo developer built a language-learning app where learners practice pronunciation against a cloned voice of a native speaker. The voice was cloned from a 90-second recording, costs $22/mo to run for unlimited learners, and the app charges $9/mo per user.

## FAQ

**What's the difference between TTS and voice cloning?**
Text-to-speech converts text into speech using a pre-built voice model — ElevenLabs ships dozens of high-quality premade voices you can use immediately. Voice cloning trains a small fine-tuned model on an audio sample of a specific person's voice, so the output sounds like that person. TTS is instant and free to start; voice cloning requires a sample and is limited to certain plans.

**Can I clone my own voice for free?**
ElevenLabs' free tier supports "Instant Voice Cloning" — a lower-quality clone from a short sample. Professional Voice Cloning (higher fidelity, more consistent) requires the Creator plan at $22/mo. For most product use cases, Instant Cloning is indistinguishable to end users.

**Which voice API has the best quality in 2026?**
ElevenLabs leads on naturalness and emotional range, especially in English. Cartesia is competitive on latency (sub-100ms streaming) and is better for real-time applications. OpenAI TTS is fast and cheap but noticeably more robotic on long-form content. For a product where voice quality is a differentiator, ElevenLabs is the default choice.

**How do I add TTS to a Next.js app?**
Create a file at `app/api/tts/route.ts`. Inside, receive the text from the request body, call ElevenLabs' streaming endpoint with your API key, and return the audio stream with `Content-Type: audio/mpeg`. On the client, call `fetch('/api/tts', { method: 'POST', body: JSON.stringify({ text }) })` and play the result with the Web Audio API. The ElevenLabs JS SDK (`npm i elevenlabs`) wraps this in a `stream()` helper that handles chunking automatically.

## Go deeper

- [tools/elevenlabs.md](../tools/elevenlabs.md) — ElevenLabs deep page: models, voices, pricing tiers
- [mcp/cartesia.md](../mcp/cartesia.md) — Cartesia MCP: real-time TTS in Claude Code
- [tools/supabase.md](../tools/supabase.md) — storing user voice IDs and usage records
- [tools/vercel.md](../tools/vercel.md) — deploying the TTS proxy as an edge function
- [playbooks/faceless-content-factory.md](../playbooks/faceless-content-factory.md) — using voice generation in a content pipeline

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
