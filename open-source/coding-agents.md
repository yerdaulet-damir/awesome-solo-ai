# Open-Source Coding Agents

Four serious options for running an AI coding agent without paying a closed-source vendor: opencode, Cline, Aider, and Continue. Each has a different mental model and a different sweet spot. Here's how they compare and when to reach for each.

## The four agents

### opencode (~176k★, MIT)

[sst/opencode](https://github.com/sst/opencode) is a terminal-native coding agent built by the team behind SST. It runs in your terminal, reads your codebase, and executes tasks end-to-end — file edits, shell commands, test runs, the full loop. The key design choice: it's a standalone CLI, not a VS Code extension, which means it works identically in any environment including SSH sessions and CI.

**Setup:** `npm install -g opencode`, then `opencode auth` to connect your API key (Anthropic, OpenAI, or any OpenAI-compatible endpoint). It reads a `OPENCODE.md` file at the repo root the same way Claude Code reads `CLAUDE.md`.

**Use when:** you want a Claude Code-like experience with your own API key, you work primarily in the terminal, or you want to run agents in headless/server environments.

### Cline (~63k★, Apache 2.0)

[cline/cline](https://github.com/cline/cline) is a VS Code extension that gives you a full agentic loop inside your editor. It reads files, edits code, runs terminal commands, and can use a browser via Playwright — all approved by you step-by-step or in auto-approve mode. The diff view for every edit is the standout UX feature: you see exactly what Cline is changing before it changes it.

**Setup:** Install from the VS Code Marketplace, configure your API key in settings (supports Claude via Anthropic or Bedrock, OpenAI, Gemini, local Ollama). Set a monthly cost limit in settings to avoid runaway token spend.

**Use when:** you're primarily in VS Code, you want tight visual control over every edit, or you want to wire a browser agent into the coding loop.

### Aider (~35k★, Apache 2.0)

[paul-gauthier/aider](https://github.com/paul-gauthier/aider) is the oldest and most battle-tested of these tools. It works by letting you `/add` files to a working set, then chat with the LLM to make changes — the agent edits those specific files and commits the changes to git automatically. It's opinionated about git: every change is a commit, which gives you a clean undo history.

**Setup:** `pip install aider-install && aider-install`, then `aider --model anthropic/claude-sonnet-4-5`. It supports the full Claude model lineup via the Anthropic API.

**Use when:** you want git-native editing (every agent action = one commit), you're working in Python/data science projects where pip tooling is natural, or you want a stable, predictable agent with no UI overhead.

### Continue (~25k★, Apache 2.0)

[continuedev/continue](https://github.com/continuedev/continue) is both a VS Code and JetBrains extension. Its strength is context management: you `/add` entire codebases to context, reference docs via `@url`, and attach files explicitly. It supports dozens of LLM providers through a unified `config.json`. The inline code completion (tab autocomplete) is a separate feature from the chat — both work simultaneously.

**Setup:** Install from VS Code Marketplace or JetBrains Plugin Repository. Edit `~/.continue/config.json` to add your model providers. Point it at Claude via Anthropic's API or a local Ollama endpoint.

**Use when:** you want JetBrains support, you want tight control over what context the agent sees, or you want AI code completion + chat as an integrated pair.

## Comparison at a glance

| | opencode | Cline | Aider | Continue |
| --- | --- | --- | --- | --- |
| Interface | Terminal CLI | VS Code | Terminal CLI | VS Code / JetBrains |
| Git integration | Manual | Manual | Auto-commit per change | Manual |
| Browser control | No | Yes (Playwright) | No | No |
| Diff preview | No | Yes | Yes (in terminal) | Yes |
| Best model | Claude / any | Claude / any | Claude / any | Claude / any |
| Headless / CI use | Yes | No | Yes | No |

## Using any of these with the Claude API

All four support the Anthropic API directly. The recommended model for heavy coding tasks is `claude-sonnet-4-5` — it has the best cost-to-capability ratio for long edit sessions. Use `claude-opus-4` for the hardest architectural tasks where you want maximum reasoning depth, and `claude-haiku-3-5` for autocomplete or quick inline edits where latency matters more than depth.

Set a context limit in each tool's config: Sonnet supports 200k tokens, but agent loops that fill the window run slowly and cost more. Start with a 50k limit and raise it when you need it.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
