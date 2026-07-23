# Marketing, SEO, and Social from Claude Code

The fastest way to run growth work as a solo builder is to give your terminal the same skills a marketing team would use, then wire in a couple of MCP servers for live data. These are the repos actually getting stars and commits right now, sorted from most battle tested to newer bets.

- [marketingskills](https://github.com/coreyhaines31/marketingskills) by [Corey Haines](https://github.com/coreyhaines31), the repo that kicked off the marketing skills as packages trend, with CRO, copywriting, SEO, and analytics skills you install with one CLI command. Claude Code skills, growth engineering, ~41k stars, updated daily.
- [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) by [Eric Siu](https://github.com/ericosiu), complete runnable workflows, not prompts, covering growth experiments, sales pipeline scoring, outbound, and content ops. Claude Code skills, scripts, SEO, ~3.1k stars.
- [openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills) by [OpenClaudia](https://github.com/OpenClaudia), 34 modular marketing skills that turn Claude Code into a full marketing department across SEO, content, email, ads, and analytics. Claude Code, Cursor, and any markdown instruction agent.
- [linkedin-skills](https://github.com/sergebulaev/linkedin-skills) by [Serge Bulaev](https://github.com/sergebulaev), writes human sounding LinkedIn posts, drafts comments, analyzes your feed, and builds a publishing cadence, all from the terminal with a draft and confirm step before anything ships. Claude Code and Codex skills, social media, ~420 stars.
- [seo-skills](https://github.com/seranking/seo-skills) by [SE Ranking](https://github.com/seranking), production SEO skills for content briefs, audits, backlink gaps, keyword clusters, schema, and GEO, documenting every API call so you can swap the data provider. Claude Agent Skills plus a remote MCP server.
- [kai-cmo-harness](https://github.com/cgallic/kai-cmo-harness) by [cgallic](https://github.com/cgallic), an AI CMO harness that starts from your repo, your product docs, pricing, and claims, rather than a blank chat box, spanning SEO, content, email, ads, and AI search visibility. Claude Code skills, newer project, ~25 stars.

For live data, plug in an MCP server so the skills above can reach real numbers instead of guessing:

- [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) by [Firecrawl](https://github.com/firecrawl), scrape, search, and crawl the open web into Claude for competitor teardowns and content research, with scrape and search working on the free tier without a key. MCP, ~7k stars.
- [mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript) by [DataForSEO](https://github.com/dataforseo), the official DataForSEO server exposing SERP positions, keyword volumes, backlinks, and on page data over MCP. Runs via npx, ~230 stars.

Prefer a menu over a single pick? Two curated lists stay current: [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) by [Composio](https://github.com/ComposioHQ) with a dedicated business and marketing section, and [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) by [VoltAgent](https://github.com/VoltAgent) collecting 1000+ skills across Claude Code, Codex, Cursor, and Gemini CLI.

## FAQ

**What are the best repos for marketing with Claude?**
For a solo builder, start with [Corey Haines' marketingskills](https://github.com/coreyhaines31/marketingskills) for broad CRO, copy, and SEO coverage, then add [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) if you want full workflows for outbound and pipeline. Both install straight into Claude Code and are updated most weeks, so you get skills that match the current model behavior rather than stale prompts.

**Is there an SEO skill for Claude, and how does it get real data?**
Yes. [seranking/seo-skills](https://github.com/seranking/seo-skills) ships audit, keyword cluster, schema, and GEO skills, and it pairs with a remote MCP server so the skill can pull live rankings instead of estimating. If you already have a DataForSEO account, the official [DataForSEO MCP server](https://github.com/dataforseo/mcp-server-typescript) gives the same skills access to SERP, keyword, and backlink numbers.

**How do I automate social media content with Claude Code and MCP?**
For LinkedIn specifically, [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) drafts posts and comments and plans a cadence from your terminal, always showing a draft before anything goes out. Pair a writing skill with a scraping MCP like [Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server) to research what is working in your niche first, and keep a human in the loop on publishing, since most platforms restrict fully hands off automation.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
