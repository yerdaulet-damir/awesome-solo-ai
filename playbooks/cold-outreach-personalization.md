# Playbook: Automate Cold Outreach Personalization at Scale

Fifty LinkedIn URLs in, fifty genuinely personalized openers out, ready to send in 30 minutes. The difference between a 2% reply rate and a 12% reply rate is one specific sentence that proves you read their profile.

## Stack

| Stage | Tool |
| --- | --- |
| Profile scraping | [Firecrawl MCP](../README.md#mcp-servers) |
| Personalization engine | [Claude](../README.md#ai-coding-agents) via [OpenRouter](../README.md#llm-api-routers--aggregators) |
| Sequence + sending | [Instantly](https://instantly.ai) or [Lemlist](https://lemlist.com) |
| Data storage | Google Sheets or [Supabase](https://supabase.com) |

## The workflow

1. **Build your prospect list.** Export 50 LinkedIn URLs from Sales Navigator, a manual search, or a niche directory. Drop them in a CSV with columns: `name`, `linkedin_url`, `company`, `role`.
2. **Scrape profile data.** Tell Claude Code: "For each LinkedIn URL in this CSV, use Firecrawl MCP to fetch the profile page and extract: current role, last three positions, education, recent activity/posts, and any shared interests." Firecrawl returns clean text from the rendered page — LinkedIn's SPA is no obstacle. Write the extracted data back to new columns.
3. **Generate openers.** Now the core prompt: "Write a 2-sentence cold email opener for [name]. They are a [role] at [company]. Here is their profile data: [extracted data]. The opener must reference one specific, non-generic detail from their background — a past company, a project they posted about, or an unusual career move. Do not use 'I came across your profile' or 'I noticed you work at.' Be direct."
4. **Batch it.** Process all 50 rows in one Claude Code session — it loops through the CSV, calls Claude for each row, and writes the openers back. The full batch takes under 5 minutes.
5. **Review before sending.** Scan the outputs in 10 minutes. Flag any opener that is generic ("You have an impressive background") or factually wrong. Fix or delete — bad personalization is worse than none.
6. **Load into the sequence tool.** Import the CSV to Instantly or Lemlist. Map the opener column to a `{{personalized_intro}}` variable in your template. The rest of the email (your pitch, CTA) stays constant.

## Deliverability basics

Warm your sending domain for at least two weeks before any volume. Use a subdomain (`mail.yourco.com`) separate from your main domain — if it gets flagged, your main domain stays clean. Limit sends to 30–50 per day per inbox when starting out. In Instantly, enable "email warmup" on every sending account; it auto-exchanges emails with other Instantly users to build sender reputation.

Plain-text emails outperform HTML in cold outreach. No logos, no tracking pixels on the first send. One link maximum. Subject lines under six words. These aren't style preferences — they're deliverability hygiene.

## What makes the opener work

The specific detail is doing all the work. "I saw you built the payments infra at [company X] before they were acquired" lands because it requires actual knowledge. "Impressive background" lands nowhere because it requires none. Claude is good at this task precisely because it can synthesize a career narrative from unstructured profile text and find the one angle worth mentioning. Your job is picking the right 50 people, not writing 50 openers.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
