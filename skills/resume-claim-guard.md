# Resume Claim Guard: keep resume claims inside facts you can defend

## Source and supported agents

- Repository: https://github.com/korey2028-prog/resume-claim-guard
- Skill file: https://github.com/korey2028-prog/resume-claim-guard/blob/main/SKILL.md
- License: MIT
- Supported agents I document: Claude Code, Codex, WorkBuddy, and web LLMs via `PROMPT.md`. I have not claimed Cursor or Copilot.

## When to use it

Use it when you have a job description and want a tailored resume that will survive interview follow-ups. It asks what you actually did before it writes, caps verbs to the evidence, and previews likely interview questions.

Use a different approach if you only need an ATS keyword score or a one-click rewrite with no fact check.

## Install and access

Author's instructions: clone the repo into the agent's skills directory, for example `~/.claude/skills/resume-claim-guard` or `~/.codex/skills/resume-claim-guard`. Web-chat users can paste `PROMPT.md` and then the job description. No paid API key and no external service are required. Supporting files live in `references/`, `templates/`, `examples/`, and `platforms/`.

## Example I tried

I am the author. The worked example in the repo (`examples/`) walks a job description through intake questions, a confirmed fact list, a tailored draft, and a claim audit. I did not invent pass/fail metrics for this PR. Please treat the repository examples as the reproducible walkthrough.

## Test notes and attribution

Last reviewed against repo `main` (commit `42406b9d9511705ec798922ac5d8e4b0c4f35505`, 2026-10-31). I am the author of the skill. AI-assisted drafting of this page was reviewed by me.
