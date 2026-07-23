# Open-Source AI Agents

Agents a solo builder can actually self-host or build on, verified live as of July 2026. No subscription, bring your own API key or a local model.

## Autonomous agents you run yourself

- [OpenClaw](https://github.com/openclaw/openclaw) by [openclaw](https://github.com/openclaw), a personal AI agent that runs as a single local process and takes commands from WhatsApp, Telegram, and Discord to run shell, manage files, and browse. self hosted, messaging ui, active.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://github.com/NousResearch), a server resident agent with persistent memory that auto generates its own skills and runs across Telegram, Slack, Signal, email, and CLI on Docker, SSH, or Modal. self hosted, persistent memory, active.
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) by [Significant Gravitas](https://github.com/Significant-Gravitas), the original goal driven autonomous agent, now a low code platform for building and running continuous agents from a visual block editor. self hosted, web ui, active.

## Coding agents you can self-host

- [opencode](https://github.com/anomalyco/opencode) by [Anomaly](https://github.com/anomalyco), a terminal first, model agnostic coding agent with a polished keyboard driven TUI that works with any provider or a local model. cli, terminal ui, active.
- [OpenHands](https://github.com/OpenHands/OpenHands) by [OpenHands](https://github.com/OpenHands), an autonomous dev agent that browses, edits, runs tests, and retries in a sandbox, and closes a large share of real GitHub issues headless in CI. self hosted, sandboxed, active.
- [Cline](https://github.com/cline/cline) by [Cline](https://github.com/cline), a model agnostic coding agent shipped as a VS Code extension, CLI, and SDK, with step by step human approval on every file edit and command. ide extension, cli, sdk, active.

## Frameworks to build your own agent

- [LangGraph](https://github.com/langchain-ai/langgraph) by [LangChain](https://github.com/langchain-ai), a graph based runtime for stateful multi step agents with checkpoints, human in the loop, and durable execution. python, js, active.
- [CrewAI](https://github.com/crewAIInc/crewAI) by [CrewAI](https://github.com/crewAIInc), a standalone framework for orchestrating role playing agents that split a task into collaborating crew members. python, multi agent, active.
- [smolagents](https://github.com/huggingface/smolagents) by [Hugging Face](https://github.com/huggingface), a barebones library where agents write their actions as executable Python code instead of JSON tool calls. python, code agents, active.

## FAQ

**What is the best open-source AI agent I can self-host right now?**
For a general personal assistant, OpenClaw and Nous Research's Hermes Agent both run entirely on your own machine, keep persistent memory, and take commands from chat apps like Telegram and Discord. For coding, opencode and OpenHands are the two most reached for self hosted options, one terminal first and one sandboxed and autonomous. All four are permissively licensed, so you bring your own API key or a local model and pay no subscription.

**What should I use for a self-hosted coding agent?**
opencode gives you a fast terminal UI that works with any model provider or a local model, Cline adds step by step approval on every edit inside VS Code or as a CLI, and OpenHands runs headless in a sandbox to close real GitHub issues in CI. Pick opencode or Cline for interactive daily work, OpenHands for unattended pipelines.

**Do OpenClaw and Nous Hermes actually exist, and where are the real repos?**
Yes, both are real and actively developed as of July 2026. OpenClaw lives at github.com/openclaw/openclaw and Hermes Agent lives at github.com/NousResearch/hermes-agent, both with commits landing regularly. Ignore the many blog posts quoting wildly different numbers, check the GitHub repos directly.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
