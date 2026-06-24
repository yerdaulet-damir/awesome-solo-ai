# HeyGen MCP — avatar video from your agent

> Where is the HeyGen MCP? Here. Generate avatar videos, clone voices, and create speech directly from Claude Code.

## What is the HeyGen MCP server?

**The HeyGen MCP server lets an AI agent create avatar and spokesperson videos through HeyGen's API over the Model Context Protocol.** Once connected to Claude Code (or any MCP client), the agent can generate a talking-head video from a script, clone a voice, produce speech, and manage avatars — no manual clicking in the HeyGen UI.

[HeyGen](https://heygen.com) is the leading AI avatar platform; the MCP server is its official agent interface.

## What you can do with it

- Generate a video of your AI avatar from text.
- Create speech and clone a voice for narration.
- Drive the whole "script → voiced avatar clip" step inside a larger automation.

## Why it matters for solo builders

It turns faceless and talking-head content into a scripted, repeatable pipeline. A solo creator clones themselves once, then generates dozens of videos from scripts — see the [Faceless Content Factory playbook](../playbooks/faceless-content-factory.md).

## Example

With the HeyGen MCP connected, ask Claude Code:

> "Write a 30-second hook about X, generate the voiceover, render it as my HeyGen avatar, and download the mp4."

The agent calls HeyGen's tools in sequence and returns the file.

## Setup

You need a HeyGen account and API key. Add the HeyGen MCP server to your Claude Code MCP config with that key (see HeyGen's developer docs), then confirm the tools appear.

## Related

- [ElevenLabs MCP](elevenlabs.md) — pair for higher-quality voice.
- [Edit videos with Claude Code](../guides/edit-video-with-claude.md).

## Source

[heygen.com](https://heygen.com) · [HeyGen developer docs](https://docs.heygen.com)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
