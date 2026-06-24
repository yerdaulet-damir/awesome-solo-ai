# How to Edit Videos with Claude Code (No Manual Editing)

You can turn Claude Code into a video editor by giving it tools through [MCP](../README.md#mcp-servers) — then describing edits in plain English. No timeline, no mouse.

## The idea

Claude can't edit pixels by itself. You give it **tools** (MCP servers or a CLI like `ffmpeg`), and it orchestrates them. Two layers:

1. **Generation/voice/avatar** via MCP — [HeyGen MCP](../README.md#mcp-servers) for avatars, [ElevenLabs MCP](../README.md#mcp-servers) for voice and SFX.
2. **Cuts, crops, captions, concatenation** via `ffmpeg`, which Claude Code runs through the Bash tool.

## Quick start: caption + 9:16 crop for shorts

In a project folder with your `input.mp4`, just ask Claude Code:

> "Crop `input.mp4` to vertical 9:16, burn in subtitles from `captions.srt`, and export `short.mp4`."

It will run something like:

```bash
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih,subtitles=captions.srt" -c:a copy short.mp4
```

## Quick start: script → voiced avatar clip

1. Add the [HeyGen MCP](../README.md#mcp-servers) and [ElevenLabs MCP](../README.md#mcp-servers) servers to Claude Code.
2. Ask: *"Write a 30-second hook about X, generate the voiceover with ElevenLabs, render it as my HeyGen avatar, and download the mp4."*
3. Claude calls the tools in sequence and hands you the file.

## Why this beats a GUI for solo creators

- **Batch it.** "Do this for all 12 clips in `/raw`" — one prompt, twelve outputs.
- **Reproducible.** The prompt *is* the edit recipe; rerun it next week.
- **Composable.** Chain generation → edit → publish in one playbook (see [Faceless Content Factory](../playbooks/faceless-content-factory.md)).

## Tools referenced

[HeyGen](../README.md#ai-avatars--talking-heads) · [ElevenLabs](../README.md#voice-tts--cloning) · [Runway / Kling / Higgsfield](../README.md#video-generation) for B-roll · `ffmpeg` for cuts.
