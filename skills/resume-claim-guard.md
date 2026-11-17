# Resume Claim Guard: keep resume claims inside facts you can defend

## Source and supported agents

- Repository: https://github.com/korey2028-prog/resume-claim-guard
- Skill file: https://github.com/korey2028-prog/resume-claim-guard/blob/main/SKILL.md
- License: MIT
- Supported agents I document: Claude Code, Codex, WorkBuddy, and web LLMs via `PROMPT.md`.

## When to use it

Use it when you have a job description and want a tailored resume that will survive interview follow-ups. It asks what you actually did before it writes, caps verbs to the evidence, and previews likely interview questions.

Use a different approach if you only need an ATS keyword score or a one-click rewrite with no fact check.

## Install and access

Author's instructions: clone the repo into the agent's skills directory, for example `~/.claude/skills/resume-claim-guard` or `~/.codex/skills/resume-claim-guard`. Web-chat users can paste `PROMPT.md` and then the job description. The skill itself needs no separate API key and calls no external service, but your agent still sends what you paste (job description, resume, answers about your experience) to its own model provider, as with any prompt. Use a redacted or sample resume if that matters to you. Supporting files live in `references/`, `templates/`, `examples/`, and `platforms/`.

## Example I tried

Walkthrough: [`examples/jd-to-interview`](https://github.com/korey2028-prog/resume-claim-guard/tree/main/examples/jd-to-interview). It uses a fictional student and a fictional AI product-operations internship, not a real person's resume. Read in this order: `jd.md` (the job) → `resume-old.md` (an AI-inflated sample resume) → `conversation.md` (the intake questions) → `facts.md` (the confirmed fact list) → `resume-targeted.md` (the rewrite, with each line mapped to a fact ID).

One before/after claim from that example, translated from Chinese:

| | Claim |
|---|---|
| Before (`resume-old.md`) | "Developed and launched an AI event sign-up tool… served 120 users." |
| Confirmed fact `F-07`, `F-09` (`facts.md`) | A prototype generated with ChatGPT, never launched, tried only by the candidate and two roommates. 120 is the number of past sign-up records used as test imports, not users. |
| After (`resume-targeted.md`) | "Used ChatGPT to generate a sign-up form and stats page prototype; wrote the requirements and tested it by hand… Test-imported 120 past sign-up records; the prototype was only tried by me and two roommates." |

The audit in the same example also catches "led" where the candidate was one of six editors, and a "60% read-rate increase" the candidate could not source, which is dropped. I am the author, so these are the repository's own examples, not an independent test.

## Test notes and attribution

Last reviewed against repo `main` (commit `42406b9d9511705ec798922ac5d8e4b0c4f35505`, 2026-10-31). I am the author of the skill. AI-assisted drafting of this page was reviewed by me.
