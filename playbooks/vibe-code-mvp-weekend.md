# Playbook: Vibe-Code an MVP in a Weekend

Friday night you have an idea. Sunday evening it's live with real users on it. This is the exact sequence that makes that happen without the build drifting into a side project graveyard.

## Stack

| Layer | Tool |
| --- | --- |
| Coding agent | [Claude Code](../README.md#ai-coding-agents) |
| Database + auth | [Supabase](https://supabase.com) (Supabase MCP connected) |
| Deploy | [Vercel](https://vercel.com) |
| Payments (if needed) | [Stripe MCP](../README.md#mcp-servers) |
| Launch platforms | Show HN, Product Hunt, relevant subreddits |

## Friday night: idea → CLAUDE.md

The most important file you write isn't code — it's `CLAUDE.md`. Before touching a component, spend 30 minutes writing:

- What the product does in one sentence
- The three screens that must exist for the MVP to be launchable
- The data model (3–5 tables max)
- What "done" looks like for the weekend
- What to skip (auth complexity, edge cases, mobile optimization)

A good CLAUDE.md is the diff between 12 hours of productive building and 12 hours of Claude inventing features you didn't ask for. Add a "do not build" list — it matters as much as the build list.

## Saturday: build the core

Start with the data model. Tell Claude Code: "Create Supabase migrations for [your schema]. Apply them via Supabase MCP. Show me the table structure before we build any UI." Confirming the schema before the first component prevents the most expensive refactor of the weekend.

Build in vertical slices: one complete user flow at a time, from database row to rendered UI. The order matters — get data flowing before you polish anything. A working ugly thing beats a beautiful broken thing.

Every two hours, run a verification pass: open the app in a real browser, click through the happy path, note what breaks. Don't wait until Sunday to discover the auth flow is broken.

## Sunday: ship, don't polish

Stop building at noon. The afternoon is for: writing a good README, setting up a real domain, writing the Show HN post, and preparing the Product Hunt listing if you're going there.

Show HN posts that work follow a formula: "Show HN: [what it does] ([URL])". Two paragraphs in the body — what problem it solves and what's interesting about the technical approach. Post between 9am–noon Pacific on a weekday if you want votes; Sunday evening is fine if you want honest feedback.

## Common drift points and how to recover

**Claude invents an abstraction you didn't ask for.** Catch it in the diff review. Say: "Revert the [X] abstraction, implement this the simple direct way." Keep the CLAUDE.md "do not build" list updated with anything you've already rejected once.

**The feature set expands.** Every time you think of a new feature during the build, write it in a `BACKLOG.md` file and keep building. The weekend scope is fixed.

**The build stalls on a hard problem.** Time-box it: 30 minutes on any single problem, then either ask Claude to try a different approach or skip the feature. An MVP that ships without feature X beats an MVP that never ships because X took the whole weekend.

## After you launch

Your first 24 hours of feedback is worth more than your next month of building. Read every comment, reply to everyone. The gap between what you built and what users want is the real spec for week two.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
