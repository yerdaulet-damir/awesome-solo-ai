# Build Your Own AI Avatar Video Pipeline

> Go from script to talking-head video without showing your face — fully automated.

## What you're building

An AI avatar video pipeline takes a text script and outputs a finished talking-head video where a photorealistic digital avatar delivers the content in a chosen voice. The end result is a repeatable, automated workflow: write or generate a script, send it through HeyGen's avatar renderer, and receive an MP4 — no camera, no studio, no face on screen. Claude Code authors the script; ElevenLabs optionally generates the voice; HeyGen's MCP handles the render call.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| Avatar video rendering | HeyGen MCP | Render talking-head videos from a script via API, directly from Claude Code | [mcp/heygen.md](../mcp/heygen.md) |
| Voice generation | ElevenLabs | Clone a voice or choose from premade library; feeds audio into HeyGen as a custom voice | [tools/elevenlabs.md](../tools/elevenlabs.md) |
| Script authoring | Claude Code | Writes scripts in a structured format HeyGen expects — scene by scene, with speaker notes | — |

## Build it

**Step 1 — Write the script with Claude.** Give Claude a topic, a target length (e.g., "90-second explainer"), and a tone. Ask it to output the script in HeyGen's SSML-compatible format: clean sentences, natural pauses marked with `<break time="0.5s"/>`, and no stage directions. Claude can also adapt an existing blog post, tweet thread, or outline into video-ready copy. Save the script as a markdown or text file.

**Step 2 — Clone or pick a voice in ElevenLabs.** If you want a custom voice, upload a 60-second audio sample to ElevenLabs Voice Lab — you get back a `voice_id`. If you are using HeyGen's built-in voices, skip this step. For the cloned-voice path, generate the audio file via ElevenLabs' API (`POST /v1/text-to-speech/{voice_id}`) using your script text as input. Download the MP3.

**Step 3 — Send to HeyGen MCP.** In Claude Code, invoke the HeyGen MCP's video creation tool. Pass the avatar ID (choose from HeyGen's public avatar library or a custom one you uploaded), the script text, and optionally the ElevenLabs audio file URL. The MCP returns a `video_id` immediately — HeyGen renders asynchronously.

**Step 4 — Poll for completion and retrieve.** HeyGen renders most videos within two to five minutes. Use the HeyGen MCP's `get_video` tool to check status by `video_id`. When status is `completed`, the tool returns a download URL. Download the MP4 or grab the hosted URL directly.

**Step 5 — Auto-publish (optional).** Wire the download URL to your publishing destination. For YouTube, use the YouTube Data API to upload the MP4 with title and description. For TikTok, use TikTok's Content Posting API. For LinkedIn, use their Video Share API. Each of these can be triggered from a Claude Code agent or an n8n webhook — the video URL from step 4 is the only input you need.

## What it costs

HeyGen Creator plan ($29/mo) includes 15 video credits per month — each credit covers roughly one minute of video. Additional credits are $0.15 per minute. ElevenLabs free tier covers 10,000 characters per month (enough for dozens of 90-second scripts); Creator plan ($22/mo) for higher volume. If you use HeyGen's built-in voices, ElevenLabs is optional and costs nothing. Total for a modest output of 10-15 videos per month: $29/mo.

## Real examples

Faceless YouTube channels in the finance and tech education niches routinely use HeyGen avatars to publish daily videos with subscriber counts in the hundreds of thousands. The creator never appears on screen — the avatar delivers the script, the voice is cloned from a few recorded sentences, and the entire production pipeline runs without a studio.

A solo SaaS founder uses this pipeline to produce product demo videos for every major feature update. Claude writes the script from the changelog, HeyGen renders the avatar, and the video is published to their docs site automatically. Total human time per video: under five minutes.

## FAQ

**Can I create AI avatar videos without showing my face?**
Yes. HeyGen provides a library of licensed photorealistic avatars you can use without any personal footage. You can also create a "Photo Avatar" from a single still photo of yourself — HeyGen animates it into a talking head. Neither option requires you to appear on camera. The only requirement for a fully custom avatar is a two-minute consent video for identity verification.

**What is the HeyGen MCP?**
The HeyGen MCP is an MCP server that wraps HeyGen's video generation API as Claude tools. Instead of writing API client code, you call `create_video_from_avatar` directly from a Claude Code conversation or agent script. It handles authentication, serialization, and status polling — see the [mcp/heygen.md](../mcp/heygen.md) page for full tool reference.

**How do I automate video creation with Claude Code?**
Write a CLAUDE.md file that defines the job: given a topic, produce a video. Claude reads the topic, writes the script, calls the ElevenLabs MCP to generate audio, calls the HeyGen MCP to render the video, and returns the final URL. Run this as a Claude Code agent on a schedule (cron via GitHub Actions, or n8n trigger) with a new topic each time. The entire pipeline is a single agent invocation.

**HeyGen vs Synthesia for solo creators?**
HeyGen's MCP availability makes it the better choice for automated pipelines — you can drive it programmatically from Claude Code without writing a custom API client. Synthesia has a cleaner avatar library but no MCP and a higher starting price ($22/mo vs HeyGen's $29/mo for similar output). For one-off manual video creation, both are comparable; for automated pipelines, HeyGen wins by having the integration already built.

## Go deeper

- [mcp/heygen.md](../mcp/heygen.md) — HeyGen MCP: full tool reference and setup
- [tools/elevenlabs.md](../tools/elevenlabs.md) — voice cloning and TTS for the audio layer
- [playbooks/faceless-content-factory.md](../playbooks/faceless-content-factory.md) — full faceless content production playbook
- [build/your-own-faceless-content-machine.md](./your-own-faceless-content-machine.md) — automate the full pipeline end to end
- [build/your-own-ai-voice-app.md](./your-own-ai-voice-app.md) — deeper dive into the voice generation layer

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
