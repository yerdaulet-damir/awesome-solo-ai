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

## Before Friday: choosing the idea from revenue cases (worked example)

Revenue posts can be a good source of ideas if you read them for what they actually prove. Here are two LinkedIn tools built with Claude Code, taken from [Shipped & Paid](https://shippedandpaid.com), a directory of AI-built apps with revenue claims that I run.

**Kleo, an AI writer for LinkedIn posts.** On Dec 15, 2025, cofounder Cameron Trew [posted on X](https://x.com/camtrew/status/2000550729447043420) "We built a $62k MRR SaaS in 90 days" with a Polar card showing $61,910 MRR for Nov 2 – Dec 1, 2025. Stack: Claude Code, Vercel, Inngest, Neon. Distribution: a waitlist built from the 60k users of Kleo 1.0, a free Chrome extension, plus the cofounders' large LinkedIn audiences. 500 discounted beta spots sold out in 4 days. Proof: a screenshot.

**ZenMode, a desktop app for LinkedIn outreach.** On Oct 18, 2026, solo founder Jonathan Lis [posted](https://x.com/ZenModeJon/status/2111850827799224679) that he made about $9.6k in six months, building with Claude and Claude Code. His [TrustMRR page](https://trustmrr.com/startup/zenmode), synced from Stripe, showed $9,536 all-time and $1,635 MRR from 40 subscriptions when I checked it on Oct 25, 2026. Distribution: cold outreach using his own tool, build-in-public posts and "alternative to" SEO pages. Proof: verified.

How I weigh the labels:

- **Verified** (a third-party profile connected to Stripe or RevenueCat): the connected payment provider reported those figures on that date. That doesn't verify all revenue, costs, or the founder's wider claims.
- **Screenshot**: plausible, but it's an image the founder chose to share, often at a peak. Look for a second source before relying on it.
- **Self-reported** (a number in a post or interview): a lead, not evidence. Look for a dated source behind it before planning around it.

**The decision.** Kleo has the bigger number, but it came from distribution most solo builders don't have. ZenMode suggests a smaller hypothesis worth testing: one person without a coding background, about 40 paying subscriptions, a problem from his own sales job, and a channel he controls. That's evidence the problem exists, not a recipe. With no audience, scope the weekend around a draft-and-manual-review workflow: import a target list, have the model draft a personalised first message and one follow-up, and let the user review, edit and send each one by hand. No automated connection requests. Add a Stripe checkout and a line in the "done" section of `CLAUDE.md` that says *validated when 3 strangers pay within 14 days*. If you already have an audience, look at Kleo's launch (waitlist, then a limited paid beta) rather than its feature list.

**What the figures don't tell you.**

- Survivorship: you only see the posts that worked.
- Costs and churn: neither number shows model or API costs, refunds, or how long customers stay.
- Timing: MRR is a snapshot. Kleo's is a 30-day window from late 2025.
- Audience: follower counts you see today aren't pre-launch numbers, and they explain more than the stack does.
- Platform risk: both products depend on LinkedIn. Kleo 1.0 was [shut down after a LinkedIn cease-and-desist](https://x.com/jakezward/status/1975183615257411704), and ZenMode's founder says automating LinkedIn is against its terms.

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
