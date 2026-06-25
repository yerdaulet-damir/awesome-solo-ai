# Playbook: Content Repurposing Flywheel — One Idea, Ten Formats

Write once, distribute everywhere. One blog post or idea note becomes a Twitter thread, LinkedIn carousel, newsletter section, five short-video scripts, three Reddit comments, and a Product Hunt tagline — automatically.

## Stack

| Stage | Tool |
| --- | --- |
| Transformation engine | [Claude](../README.md#ai-coding-agents) via [OpenRouter](../README.md#llm-api-routers--aggregators) |
| Automation orchestration | [n8n](../README.md#automation--agent-frameworks) |
| Long-form source | Notion, Ghost, or any CMS with an API |
| Video scripts delivery | Notion or Google Docs |
| Social scheduling | [Typefully](https://typefully.com) (Twitter) / [Buffer](https://buffer.com) (LinkedIn) |

## The format matrix

Every piece of content has a native format for each platform. Fighting it wastes reach.

| Format | Platform | What works |
| --- | --- | --- |
| Twitter thread | X / Twitter | Strong hook tweet, 6–8 points, last tweet = CTA or hot take |
| LinkedIn carousel | LinkedIn | 7–8 slides, bold claim on slide 1, data/story on 2–6, ask on 7 |
| Newsletter section | Email | 300–500 words, one insight, concrete example, one link |
| Short video scripts | Reels / Shorts / TikTok | 30–60s, hook in first 3s, payoff at the end |
| Reddit comment | Reddit | Helpful, no pitch, link buried or absent, shows domain knowledge |
| Product Hunt tagline | Product Hunt | 10 words, benefit-first, no jargon |

## The n8n workflow

The automation starts when a new post publishes to your CMS (Ghost webhook or Notion database trigger). n8n fetches the full post text and fires six Claude API calls in parallel — one per format. Each call uses a dedicated prompt tuned to that platform's native style. The outputs land in a Notion database with columns for each format, tagged with the source post.

A review step sits between generation and publishing: n8n sends a Telegram or Slack message with a preview of all six formats and two buttons — Approve or Edit. Approve triggers the publishing sequence: thread goes to Typefully queue, carousel copy goes to a Buffer draft, newsletter section gets appended to this week's draft in Beehiiv.

## The six core prompts

Each prompt receives the same source article and produces one format:

- **Thread:** "Turn this into a 7-tweet thread. Hook tweet must make a counterintuitive claim. Each tweet = one idea. Last tweet = provocative question."
- **Carousel:** "Write 7 LinkedIn slide captions. Slide 1: bold stat or claim. Slides 2–6: one supporting point each, max 25 words. Slide 7: what should the reader do next?"
- **Newsletter:** "Distill this into a 400-word newsletter section. One insight, one real example, one takeaway. First-person voice."
- **Video scripts:** "Extract 5 standalone 45-second video scripts from this article. Each needs a hook line and a payoff line."
- **Reddit comments:** "Write 3 Reddit comments that add value to discussions about this topic. Helpful, not promotional, cite specific points."
- **Product Hunt tagline:** "Write 5 Product Hunt tagline options for the main idea in this post. Under 10 words each, benefit-first."

## The compounding effect

The flywheel's value isn't the output volume — it's the feedback loop. Reddit comments show which angles get upvoted. Twitter threads show which hooks get retweeted. Newsletter clicks show which insights people actually care about. After three months, you know exactly which ideas resonate before you write the long-form version. The repurposing engine doubles as your fastest audience research tool.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
