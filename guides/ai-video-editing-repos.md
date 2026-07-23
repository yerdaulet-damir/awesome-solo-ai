# AI Video Editing and Faceless Video Pipelines

If you want to edit or generate video from Claude Code or any AI agent, the ecosystem splits into three buckets: MCP servers that hand an agent a video editing toolbox, CLI and skill based pipelines that run the whole production, and programmatic frameworks that render video from code. Here are the ones worth your time.

- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) by [harry0703](https://github.com/harry0703), give it a topic or keyword and it writes the script, pulls stock footage, generates a voiceover, burns subtitles, and exports a finished HD short. faceless video, tts, api, one click.
- [OpenMontage](https://github.com/calesthio/OpenMontage) by [calesthio](https://github.com/calesthio), turns Claude Code or any coding agent into a full video studio with 12 pipelines, 100+ tools, and 700+ skill files, from research to scripting to final composition. agent skills, claude code, faceless video.
- [HyperFrames](https://github.com/heygen-com/hyperframes) by [HeyGen](https://github.com/heygen-com), write HTML, CSS, and seekable animations and render them to deterministic MP4, built to be driven by agents via a CLI or skills. cli, agent skills, html to video.
- [Remotion](https://github.com/remotion-dev/remotion) by [remotion-dev](https://github.com/remotion-dev), make videos programmatically with React, so an agent can generate components and render frames deterministically. cli, api, react.
- [Revideo](https://github.com/midrender/revideo) by [midrender](https://github.com/midrender), open source programmatic video framework in TypeScript, good when you want an agent to produce parametric, data driven clips. cli, api, typescript.
- [FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline) by [FireRedTeam](https://github.com/FireRedTeam), an intention driven editing agent with LLM planning and reusable Style Skills, and you can run its project level skills straight from Claude Code. agent skills, claude code, human in the loop.
- [Kinocut](https://github.com/KyaniteLabs/kinocut) by [KyaniteLabs](https://github.com/KyaniteLabs), a free, local MCP server plus a kino CLI and Python library that wraps FFmpeg with preflight guardrails and provenance receipts, no account or API key needed. mcp, cli, ffmpeg, local.
- [pireel](https://github.com/pireel/pireel) by [pireel](https://github.com/pireel), backend free, in browser talking head editor with storyboarding, kinetic captions, and WebCodecs export, drivable by any AI agent over MCP. mcp, browser, talking head.
- [capcut-ai-editor](https://github.com/mrbuslov/capcut-ai-editor) by [mrbuslov](https://github.com/mrbuslov), MCP server that automates talking head cleanup, cutting pauses, dropping duplicate takes, adding subtitles, then exports a CapCut project. mcp, capcut, talking head.
- [AI-Youtube-Shorts-Generator](https://github.com/SaarD00/AI-Youtube-Shorts-Generator) by [SaarD00](https://github.com/SaarD00), a faceless factory that takes a topic to a finished Short using Gemini for scripting, Edge-TTS for voice, and FFmpeg for editing. faceless video, gemini, ffmpeg.
- [agentic-video-editor](https://github.com/poseljacob/agentic-video-editor) by [poseljacob](https://github.com/poseljacob), an ave CLI where Director, Editor, and Reviewer agents take raw footage plus a brief to a polished ad using Gemini and FFmpeg. cli, multi agent, ffmpeg.

## FAQ

**How do I edit or make a video with Claude?**
Point Claude Code or Claude Desktop at a video editing MCP server such as Kinocut, pireel, or a FFmpeg based server, then just describe the edit in plain English like trim this clip from 1:30 to 2:45 and add captions. The MCP server translates your request into real FFmpeg or timeline commands and runs them locally, so Claude drives the tool the way a human editor would. For full production from a topic, skill based systems like OpenMontage and FireRed-OpenStoryline run inside Claude Code and handle scripting, assets, and the final cut.

**What is the best AI video editing repo or MCP server?**
For a free, local, no API key MCP server, Kinocut is the most current pick since it wraps FFmpeg with guardrails and a kino CLI and works with Claude Code, Cursor, and Cline. If you already live in CapCut, mrbuslov/capcut-ai-editor exposes cleanup and export as MCP tools, and pireel is a strong browser based option for talking head video. For programmatic, code first rendering, Remotion and Revideo let an agent generate the video from React or TypeScript.

**What is a good faceless video automation project on GitHub?**
MoneyPrinterTurbo is the most popular by a wide margin, near 99k stars, and turns one keyword into a subtitled short with voiceover in a single run. If you want a hackable Python pipeline instead of a web app, SaarD00's AI-Youtube-Shorts-Generator uses Gemini, Edge-TTS, and FFmpeg with a clean hook to twist script structure, and SamurAIGPT's AI-Faceless-Video-Generator adds an AI talking face on top. All three are open source and run with your own API keys.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
