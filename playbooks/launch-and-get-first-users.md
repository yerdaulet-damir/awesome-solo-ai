# Playbook: Launch and Get Your First Users (Solo)

You built the thing. Now the hard part — distribution. Here's the sequence a solo builder uses to go from zero to first real users without a marketing team.

## The order that works

1. **Build in public first.** Before launch day, post the journey on [X/Threads](https://typefully.com) and [Indie Hackers](https://indiehackers.com). People who watched you build are your launch-day upvotes.
2. **Seed the communities you'll launch in.** Be a real participant in [Reddit](https://reddit.com) niche subs and [Hacker News](https://news.ycombinator.com) for weeks *before* you ask for anything. Cold launches die.
3. **Pick one launch channel to go big on.** Don't spread thin:
   - Dev/technical product → **Show HN** on [Hacker News](https://news.ycombinator.com).
   - Visual/consumer tool → **[Product Hunt](https://producthunt.com)** with a prepared hunter and assets.
4. **Launch with a demo, not a description.** A 30-second video beats paragraphs. Make it with the [Faceless Content Factory](faceless-content-factory.md).
5. **Turn the spike into a loop.** A launch is one day; a content engine is forever. Repurpose into shorts and posts on a schedule.

## Why Reddit and YouTube matter most

Beyond users, these two channels are the **strongest signals AI engines use to cite you** — Perplexity pulls ~47% of citations from Reddit, and YouTube mentions correlate most strongly with AI visibility. A Reddit post and a YouTube walkthrough do double duty: real users *and* future AI citations.

## The solo content loop

```
build in public → launch big on one channel → repurpose into shorts/posts → repeat
```

Use [claude-seo](../skills/claude-seo.md) to make sure search and AI engines can find the landing page, and [PostHog](../README.md#backend-deploy--analytics) to see which channel actually converts so you double down on it.

## Worked example: list a launch on free directories

Here is a directory research and verification example from our own launch records, including the limits of what those records tell us.

**What we recorded.** In a 13 November 2026 snapshot, our research pool held 407 candidate records. A separate public link register held 159 entries with check dates from 20 October to 13 November 2026. Its written link labels split into 105 followed, 39 nofollow and 15 other or unclear. Some followed labels were explicitly uncertain. The register includes directories, profiles, articles, hosted pages and curated lists. These are historical record counts, not a conversion rate or visitor result.

**What needed checking.** The pool labelled 14 rows as requiring a badge and one as requiring a link back. Four rows were marked not free; another described badge or paid publication. Later status notes sometimes contradicted these labels, including public listings, so we could not treat every flag as a confirmed reason to skip a site. Recheck the actual offer before applying.

**What to copy.**

1. Prepare a short tagline, a description naming the intended user and problem, a square logo and a screenshot of the real product. Adapt them to each form.
2. Check the current free path, payment and phone requirements, and any required badge or link back before starting.
3. Keep submitted, pending review and verified public link as separate states.
4. Open the public page and record the date, HTTP status, robots directives, website destination and rel value. Keep pages marked noindex separate from indexable candidates. A nofollow link can still bring visitors; do not assume a ranking benefit.
5. Use campaign parameters your analytics supports. Test that a visit appears in the report you read, then check which parameters the published link keeps.

Those checks document the page and anchor observed at that time. They do not establish search indexing or visits.

**One place to start.** [RadarMakers](https://radarmakers.com) offers free product submissions for indie makers with manual review. Disclosure: I am part of the team that builds it.

## The one rule

Distribution is a habit, not an event. The solo builders who win aren't the best builders — they're the ones who showed up to post every week. Pick one channel, make it a routine, and let the [tools above](../README.md#distribution--marketing) remove the friction.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
