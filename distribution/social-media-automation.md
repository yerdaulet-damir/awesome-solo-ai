# Social Media Automation (Human in the Loop)

Open-source tools a solo builder can actually run to draft, schedule, and cross-post across X, LinkedIn, Reddit, and Threads, with a human approving before anything ships. Checked live in July 2026.

- [Postiz](https://github.com/gitroomhq/postiz-app) by [Nevo David](https://github.com/nevodavid), self hosted scheduler that queues and cross posts to 20+ networks including X, LinkedIn, Reddit, Bluesky, and Mastodon, with a public API and agent CLI. self hosted, scheduling, cross post, agpl.
- [Mixpost](https://github.com/inovector/mixpost) by [Inovector](https://github.com/inovector), Laravel package you host yourself to schedule and manage posts across 10+ platforms with no subscription. self hosted, scheduling, laravel, mit.
- [praw](https://github.com/praw-dev/praw) by [praw-dev](https://github.com/praw-dev), the Python Reddit API wrapper that handles OAuth2 and rate limits so a Reddit posting or digest bot stays inside the rules. reddit, python, api, bot.
- [awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) by [enescingoz](https://github.com/enescingoz), 280+ importable n8n workflows including cross post templates that fan one post out to X, LinkedIn, Instagram, and more. n8n, cross post, templates, workflow.
- [xMCP](https://github.com/xdevplatform/xMCP) by [X Developer Platform](https://github.com/xdevplatform), X's official MCP server that exposes the X API to any MCP client via FastMCP, billed per call. mcp, twitter, official, api.
- [linkedin-skills](https://github.com/sergebulaev/linkedin-skills) by [Serge Bulaev](https://github.com/sergebulaev), 11 Claude Code and Codex skills that draft LinkedIn posts and comments in your voice and wait for approval before anything is published. linkedin, claude skill, human in the loop, mit.
- [instagram-skills](https://github.com/sergebulaev/instagram-skills) by [Serge Bulaev](https://github.com/sergebulaev), sibling skill bundle that writes captions, carousels, and hooks for Instagram with the same approve before post gate. instagram, claude skill, drafting, mit.
- [threads-skills](https://github.com/sergebulaev/threads-skills) by [Serge Bulaev](https://github.com/sergebulaev), Claude Code and Codex skills for Threads posts, multi post threads, and replies that publish only after you sign off. threads, claude skill, drafting, mit.
- [mcp-twitter-server](https://github.com/crazyrabbitLTC/mcp-twitter-server) by [crazyrabbitLTC](https://github.com/crazyrabbitLTC), MCP server for the X API with workflow templates and live rate limit reporting for tweet drafting. mcp, twitter, workflows, mit.
- [x-autonomous-mcp](https://github.com/JohannesHoppe/x-autonomous-mcp) by [Johannes Hoppe](https://github.com/JohannesHoppe), MCP server that wraps the X API with daily budget limits and engagement dedup, documenting which X restrictions block cold replies. mcp, twitter, safety rails, new.

## FAQ

**What is the best open source Twitter automation or social media MCP server setup?**
For scheduling and cross posting, Postiz is the most active self hosted project and posts to X plus 20 other networks from your own server. For agent driven work, X now ships an official MCP server, xdevplatform/xMCP, which is the durable path since it uses the real API, though it bills per call and, since February 2026, blocks cold programmatic replies and quote tweets. Browser automation servers exist and avoid the API bill, but they violate X's terms and go stale fast, so keep a human approving each action rather than running them unattended.

**How do I build a Reddit bot playbook that does not get banned?**
Start from praw, the maintained Python Reddit API wrapper, which forces OAuth2 auth, a unique user agent, and the 100 request per minute ceiling that Reddit enforces. Reddit's 2026 Responsible Builder Policy treats bulk posting and scraping as a bannable offense, so scope your bot to one job like a daily digest or a reply drafter, and have it surface drafts for you to approve instead of auto posting into threads. The fastest way to a permanent ban is cold automated comments, so treat Reddit as assist only.

**What covers cross posting and LinkedIn content without a paid API?**
For fan out cross posting, Postiz and Mixpost both queue one piece of content to many networks from a server you control, and enescingoz/awesome-n8n-templates gives you importable n8n workflows that do the same wiring for free. LinkedIn has no public posting API for personal profiles, so the honest pattern is drafting: sergebulaev/linkedin-skills writes posts and comments in your voice inside Claude Code or Codex and holds them until you approve, then you paste or schedule the final text yourself. That approve before publish loop is the safe framing across every platform here.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
