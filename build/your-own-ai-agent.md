# Build Your Own AI Agent

> An agent that runs a repeatable job on a schedule — research, outreach, content, or ops — without you.

## What you're building

An AI agent is a program that uses a language model to complete a multi-step task autonomously, calling tools as needed until the job is done. Unlike a chatbot (which waits for input), an agent is triggered by a schedule or event, executes a defined workflow — searching the web, reading documents, writing outputs, updating a database — and stops when the task is complete. The end result is a job that used to take you 30-60 minutes each time running reliably without your involvement.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| Agent runtime | Claude Code | Orchestrates multi-step tasks, calls MCP tools, follows CLAUDE.md context files | — |
| Step-by-step reasoning | Sequential Thinking MCP | Forces Claude to think through a task in explicit steps before acting — reduces loops and mistakes | [mcp/sequential-thinking.md](../mcp/sequential-thinking.md) |
| Web search + research | Exa MCP | Semantic search over the live web; returns clean structured results Claude can reason over | [mcp/exa.md](../mcp/exa.md) |
| Output storage | Supabase | Stores agent outputs (reports, leads, summaries) with timestamps and run metadata | [tools/supabase.md](../tools/supabase.md) |
| Scheduler | n8n or GitHub Actions | Triggers the agent on a cron schedule; passes the current date and context as input |  — |

## Build it

**Step 1 — Define the job.** A good agent job is repeatable, has clear inputs and outputs, and takes a human 20-60 minutes to do manually. Examples: "Every Monday, find the 10 most-discussed AI tools on Hacker News and summarize what practitioners are saying about them." "Every day at 8am, check our competitors' pricing pages and flag any changes." Write this as a one-paragraph brief — this becomes your agent's core prompt.

**Step 2 — Pick the MCP tools the agent needs.** Map each step in the job to an MCP tool. Web research → Exa MCP. Web scraping → Firecrawl MCP. Database reads/writes → Supabase MCP. Email sending → any SMTP MCP. Notion updates → Notion MCP. Install only the MCPs your agent actually needs — fewer tools means fewer opportunities for Claude to pick the wrong one. Add them to `.claude/settings.json` under `mcpServers`.

**Step 3 — Write the CLAUDE.md context file.** This file is what makes your agent consistent across runs. It should define the agent's role ("You are a competitive intelligence agent for a B2B SaaS"), the job brief (the paragraph from step 1), the output format (a structured markdown report, a JSON array for Supabase, a Notion page), and constraints ("Do not include speculation. Only report what you found from sources."). A good CLAUDE.md turns a generic Claude into a specialized agent that knows its job.

**Step 4 — Test interactively with Claude Code.** Before automating, run the agent manually in a Claude Code session. Type the trigger prompt and watch it execute. Check that it calls the right tools, handles empty results gracefully (what happens when Exa returns no results?), and produces output in the expected format. Iterate on the CLAUDE.md and tool selection until three consecutive manual runs produce consistent, useful output.

**Step 5 — Wrap in a scheduler.** For GitHub Actions: create `.github/workflows/agent.yml` with a `schedule: cron` trigger. The job step calls `claude --print "$(cat agent-prompt.txt)"` (Claude Code CLI) and pipes the output to a file or to a `curl` POST to your Supabase table. For n8n: use a Cron trigger node followed by an Execute Command node that runs the same Claude Code CLI command. GitHub Actions is free for public repos and 2,000 minutes/month for private repos — enough for daily agent runs.

**Step 6 — Add output storage.** Every agent run should write its output to Supabase with a `created_at` timestamp and a `run_id`. This gives you a history of what the agent found over time, lets you diff outputs between runs to detect changes, and gives you a place to query the agent's knowledge programmatically. Use Supabase's REST API (a simple `fetch` POST) or the Supabase MCP if you want Claude to write the output directly during the run.

## What it costs

Claude Code CLI usage is billed by API token. A typical agent run that does web research and writes a report consumes 10,000-50,000 tokens — roughly $0.05-$0.25 per run at Sonnet pricing. For a daily agent, that is $1.50-$7.50/mo in LLM costs. Exa MCP: free tier covers 1,000 searches per month. Supabase: free tier. GitHub Actions: free. n8n self-hosted: free. Total for a daily research agent: $2-10/mo.

## Real examples

A solo investor built a "VC radar" agent that runs every Monday morning — it searches Exa for funding announcements in a specific sector, scrapes the company pages with Firecrawl, formats a structured briefing, and posts it to a private Notion page. The agent replaces 90 minutes of manual research per week with a $3/mo LLM bill.

A solo content creator built an agent that monitors Reddit threads in their niche, identifies recurring questions, and drafts an answer post for each one. The agent runs daily, outputs a queue of draft posts to Supabase, and the creator reviews and approves them in five minutes instead of spending an hour finding and answering questions manually.

## FAQ

**What is an AI agent vs a chatbot?**
A chatbot responds to user messages in a turn-by-turn conversation and waits for input between turns. An AI agent is triggered autonomously (by a schedule or event), executes a multi-step plan using tools, and runs to completion without waiting for human input. The same LLM can power both — the difference is the surrounding architecture: conversation loop vs. autonomous execution loop. Agents are better for recurring jobs with defined outputs; chatbots are better for interactive, open-ended interactions.

**How do I build an AI agent with Claude Code?**
Write a CLAUDE.md file defining the agent's job, install the MCP tools it needs in `.claude/settings.json`, and run Claude Code with the `--print` flag to execute non-interactively: `claude --print "Run the competitor monitoring job for today."` Claude reads the CLAUDE.md context, calls the MCP tools in sequence, and prints the output. Wrap this in a GitHub Actions cron job or n8n workflow to automate execution. The entire setup takes under two hours.

**What MCP servers do AI agents need?**
It depends on the job. Research agents need Exa (web search) and Firecrawl (web scraping). Knowledge management agents need Notion MCP or Supabase MCP. Outreach agents need an email or LinkedIn MCP. Coding agents need GitHub MCP. The Sequential Thinking MCP is useful for any agent doing multi-step reasoning — it forces Claude to plan before acting and dramatically reduces mid-run errors. Start with the minimum set of tools for the job; add more only when a step fails that a new tool would fix.

**How do I make an AI agent run on a schedule?**
GitHub Actions is the zero-infrastructure option: create a workflow YAML file with `on: schedule: - cron: '0 9 * * 1'` (runs every Monday at 9am UTC). The job step runs Claude Code CLI with your prompt. For more complex orchestration (retry logic, conditionals, multi-step pipelines), use n8n — create a Cron trigger node and chain your agent call as a downstream node. For high-frequency agents (every hour), GitHub Actions free tier may not be enough — self-host n8n on a $6/mo VPS instead.

## Go deeper

- [mcp/sequential-thinking.md](../mcp/sequential-thinking.md) — structured reasoning for agents that plan before acting
- [mcp/exa.md](../mcp/exa.md) — web search for research agents
- [tools/supabase.md](../tools/supabase.md) — storing agent outputs and run history
- [mcp/firecrawl.md](../mcp/firecrawl.md) — web scraping for agents that need page content
- [playbooks/vibe-code-mvp-weekend.md](../playbooks/vibe-code-mvp-weekend.md) — building fast with Claude Code as the driver

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
