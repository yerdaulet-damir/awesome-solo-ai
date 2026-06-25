# Playbook: YouTube Channel → Newsletter + Content Flywheel

One video becomes five distribution formats in under an hour. Whisper transcribes, Claude rewrites, n8n routes everything to where audiences already live.

## Stack

| Stage | Tool |
| --- | --- |
| Transcription | [Whisper](https://github.com/openai/whisper) (local) or AssemblyAI API |
| Rewrite + summarize | [Claude](../README.md#ai-coding-agents) via [OpenRouter](../README.md#llm-api-routers--aggregators) |
| Newsletter delivery | [Beehiiv](https://beehiiv.com) or [ConvertKit](https://convertkit.com) API |
| Twitter / X threads | Post via X API or [Typefully](https://typefully.com) |
| LinkedIn carousels | Generate slide copy → [Canva](https://canva.com) API or manual |
| Automation glue | [n8n](../README.md#automation--agent-frameworks) |

## The flow

1. **Transcribe.** Run `whisper video.mp4 --output_format txt` locally (free, runs on CPU). For speed, use AssemblyAI's async API — it transcribes a 20-minute video in about 90 seconds.
2. **Clean the transcript.** Claude's first pass: remove filler words, fix speaker-error tokens, split into logical sections with headings. Prompt: "Clean this transcript, remove filler, add H2 section headings, preserve all key claims and examples."
3. **Generate the newsletter.** Second prompt: "Turn this into a 400-word newsletter section: one key insight, three supporting points, a takeaway. Write in first person, keep the speaker's voice." Push to Beehiiv via API or draft it in ConvertKit.
4. **Write the Twitter thread.** Third prompt: "Turn the key insight from this transcript into a 7-tweet thread. Hook tweet first, each tweet one idea, last tweet a CTA to the full video." Format as numbered lines — your posting tool handles the rest.
5. **Script the LinkedIn carousel.** Fourth prompt: "Write 7 slide captions for a LinkedIn carousel about [topic]: slide 1 is the hook claim, slides 2–6 are supporting points, slide 7 is a CTA." Drop these into a Canva template.
6. **Extract short-video scripts.** Final prompt: "Find the 5 most quotable moments in this transcript — under 45 seconds each when spoken. Return them as standalone scripts with a hook line and a punchline."

## The n8n automation

Wire a Watch Folder trigger that fires when a new `.txt` transcript lands. n8n sends it to a Claude API node with each prompt in sequence, then routes outputs: newsletter draft → Beehiiv, thread → Typefully queue, carousel copy → a Notion page, short scripts → a content calendar row. The whole chain runs without your hands.

## One video, five formats

A 20-minute YouTube video consistently produces: one newsletter issue, one 7-tweet thread, one LinkedIn carousel (6–8 slides), five short-video scripts (for Reels/Shorts/TikTok), and one Reddit-friendly summary. That's a week of content from a single recording session. The ratio flips the usual creator math — production time stays constant while distribution multiplies.

## The quality lever

The biggest variable is transcript quality, not prompt quality. If Whisper mishears technical terms, your Claude outputs carry the errors downstream. Keep a personal dictionary of domain terms and add a pre-processing step that replaces known misspellings before the first Claude call.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
