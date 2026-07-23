# SEO and GEO Tools for Solo Builders

Tools that help you rank in Google and get pulled into answers from ChatGPT, Perplexity, and Google AI Overviews. All checked live in July 2026.

- [SE Ranking seo-skills](https://github.com/seranking/seo-skills) by [SE Ranking](https://github.com/seranking), seven Claude skills that pull live SE Ranking data to produce content briefs, backlink gap reports, keyword clusters, and AI search share of voice. claude skill, mcp, keyword research.
- [GEO Optimizer](https://github.com/Auriti-Labs/geo-optimizer-skill) by [Auriti Labs](https://github.com/Auriti-Labs), audits how visible your pages are to ChatGPT, Perplexity, Gemini, and AI Overviews, scores citability, and generates your llms.txt. cli, python, mcp, geo.
- [DataForSEO MCP](https://github.com/dataforseo/mcp-server-typescript) by [DataForSEO](https://github.com/dataforseo), the official MCP server that hands your agent live SERP positions, keyword volumes, backlinks, and on page data. mcp, serp, backlinks.
- [AutoGEO](https://github.com/cxcscmu/AutoGEO) by [CMU](https://github.com/cxcscmu), a research framework that learns what generative engines prefer and rewrites a page to get quoted more often without changing its meaning. python, cli, research.
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) by [ai-search-guru](https://github.com/ai-search-guru), self hosted tracker that logs how ChatGPT, Perplexity, Gemini, and Copilot answer your prompts over time and whether they mention you or a competitor. api, web app, brand tracking.
- [llms-txt-generator](https://github.com/aircodelabs/llms-txt-generator) by [aircodelabs](https://github.com/aircodelabs), a CLI and MCP tool that reads your project and writes llms.txt and llms-full.txt so models can find the pages that matter. cli, mcp, llms txt.
- [Richie.js](https://github.com/cresteem/Richie.js) by [Cresteem](https://github.com/cresteem), maps existing page content to JSON-LD and outputs schema for articles, products, FAQs, and breadcrumbs in Node or the browser. schema, json ld, cli.

## FAQ

**What is a good SEO skill for Claude?**
SE Ranking's seo-skills is a set of Claude Agent Skills wired to their MCP server, so you ask for a content brief or a backlink gap report and Claude runs the whole workflow against live data. If you want a broader open source option that leans into AI search, GEO Optimizer ships as an MCP server too and covers citability scoring alongside classic technical SEO.

**How do I get cited by AI search engines like ChatGPT and Perplexity?**
Start with a GEO tool that measures citability rather than a guess. GEO Optimizer scores a page across dozens of methods and tells you which passages ChatGPT and Perplexity are likely to quote, and AutoGEO goes further by rewriting content to match what the engines pull from. Track whether it worked with GetCito, which logs how the models answer your target prompts week over week.

**What is the fastest way to generate an llms.txt file and schema markup?**
For llms.txt, point aircodelabs' generator or GEO Optimizer at your site and it crawls your pages and writes llms.txt and llms-full.txt, the plain text index that models read to understand your structure. For schema markup, Richie.js maps your existing page content to JSON-LD for articles, products, and FAQs, which is the same structured data that feeds Google rich results and AI citations. Validate the output in Google's Rich Results Test before you ship it.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
