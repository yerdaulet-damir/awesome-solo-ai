# How to Build Automations Without Code

Connect your AI tools into a working pipeline — triggered, scheduled, and hands-off — without writing a backend.

## Pick your engine

- [n8n](../README.md#automation--agent-frameworks) — open-source, self-hostable, native AI nodes. Best if you want to own it and avoid per-task fees.
- [Make](../README.md#automation--agent-frameworks) — visual, huge app catalog, fastest to start.
- [Vercel AI SDK](../README.md#automation--agent-frameworks) — when you outgrow no-code and want a tiny TypeScript service.

## The shape of every automation

```
Trigger  →  AI step  →  Action  →  (optional) Notify
```

**Example — auto-clip a podcast and post shorts:**

1. **Trigger:** new file in a Drive/Dropbox folder.
2. **AI step:** transcribe + an LLM picks the 3 most viral 30s moments.
3. **Action:** `ffmpeg`/a video tool cuts them, [ElevenLabs](../README.md#voice-tts--cloning) adds a hook voiceover.
4. **Notify:** drop the clips + captions in your Telegram/Slack for one-tap publish.

## Where AI plugs in

Any HTTP-capable node can call the [LLM routers](../README.md#llm-api-routers--aggregators) and media APIs in this list. One [OpenRouter](../README.md#llm-api-routers--aggregators) key covers the "AI step" for most flows.

## When to graduate to an agent

No-code is great for linear flows. The moment you need branching judgment ("decide *which* tool, then maybe loop"), move the logic into [Claude Code](../README.md#ai-coding-agents) or a [LangGraph](../README.md#automation--agent-frameworks)/[Mastra](../README.md#automation--agent-frameworks) agent and keep n8n/Make as the trigger + delivery layer.

## Start tiny

Build the dumbest version end-to-end first (one trigger, one AI call, one action). Ship it, then add steps. A working 3-node flow beats a perfect 12-node one that never launches.
