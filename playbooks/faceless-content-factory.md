# Playbook: Faceless Short-Form Content Factory

Script → voice → avatar → captions → publish, mostly automated, run by one person. This is the pipeline behind faceless YouTube/TikTok/Reels channels.

## Stack

| Stage | Tool |
| --- | --- |
| Idea + script | [Claude Code](../README.md#ai-coding-agents) / any [LLM router](../README.md#llm-api-routers--aggregators) |
| Voiceover | [ElevenLabs](../README.md#voice-tts--cloning) (🧩 MCP) |
| Avatar / presenter | [HeyGen](../README.md#ai-avatars--talking-heads) (🧩 MCP) or [Argil](../README.md#ai-avatars--talking-heads) |
| B-roll | [Runway](../README.md#video-generation) / [Kling](../README.md#video-generation) / [Higgsfield](../README.md#video-generation) |
| Music / SFX | [Suno](../README.md#music--sound-effects) / [ElevenLabs SFX](../README.md#music--sound-effects) |
| Cut + caption + crop | `ffmpeg` via Claude Code |
| Translate to new markets | [Rask](../README.md#lipsync-dubbing--translation) / [HeyGen Translate](../README.md#lipsync-dubbing--translation) |
| Trigger + delivery | [n8n](../README.md#automation--agent-frameworks) / [Make](../README.md#automation--agent-frameworks) |

## The flow

1. **Batch scripts.** Ask your LLM for 10 hooks + 30s scripts on your niche. Keep the winners.
2. **Generate voice.** ElevenLabs MCP turns each script into a voiceover in your cloned voice.
3. **Render the talking head.** HeyGen MCP renders your avatar lip-synced to the voiceover. (Faceless variant: skip the avatar, use B-roll + captions only.)
4. **Assemble.** Claude Code runs `ffmpeg` to layer B-roll, crop 9:16, burn captions, add music.
5. **Localize (optional).** Rask re-dubs the finished video into 3–5 languages — same asset, 5× the reach.
6. **Publish.** n8n drops finished clips into a review folder / posts on schedule.

## One-prompt version

With the MCP servers connected, this whole chain can be a single Claude Code request:

> "From `topic.txt`: write a 30s hook, voice it with ElevenLabs, render my HeyGen avatar, crop to 9:16 with burned captions, add soft background music, and put the mp4 in `/out`."

## Throughput

A tuned version produces 10–20 finished shorts in an afternoon, solo. The bottleneck becomes *selection and posting*, not production — automate the boring parts, keep human taste on the hooks.

## Cost levers

Use [open/cheap model hosts](../README.md#llm-api-routers--aggregators) for scripting, reserve premium spend for the voice and avatar where quality is visible. Localization via [Rask](../README.md#lipsync-dubbing--translation) is the highest-ROI step most solos skip.
