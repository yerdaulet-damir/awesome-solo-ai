# Build in Public: Tools and Playbook

Real tools and steps for shipping open source and AI products in the open, drawn from builders who have actually done it. Checked live in July 2026.

## Tools

- [star-history](https://github.com/star-history/star-history) by [star-history](https://github.com/star-history), plots a repo's star growth over time so you can correlate spikes with launches. github, stars, analytics.
- [Shields.io](https://github.com/badges/shields) by [badges](https://github.com/badges), generates the SVG status and stars badges that make a README scannable in the first second. readme, badges.
- [OSSInsight](https://github.com/pingcap/ossinsight) by [PingCAP](https://github.com/pingcap), analyzes billions of GitHub events to show how your repo compares to others and where stargazers come from. github, analytics.
- [readme.so](https://github.com/octokatherine/readme.so) by [Katherine Peterson](https://github.com/octokatherine), a drag and drop editor that assembles a structured README from prebuilt sections. readme.
- [All Contributors](https://allcontributors.org) by [all-contributors](https://github.com/all-contributors), a bot and spec that adds a contributors table crediting every kind of contribution, not just code. community, contributors.
- [git-cliff](https://github.com/orhun/git-cliff) by [Orhun Parmaksiz](https://github.com/orhun), generates a changelog straight from your conventional commit history with a configurable template. changelog, releases.
- [changesets](https://github.com/changesets/changesets) by [Thinkmill](https://github.com/changesets), lets contributors declare intended version bumps, then automates versioning and changelog generation, strong for monorepos. changelog, releases.
- [semantic-release](https://github.com/semantic-release/semantic-release) by [semantic-release](https://github.com/semantic-release), fully automates version numbers and package publishing based on commit messages. releases, automation.
- [release-please](https://github.com/googleapis/release-please) by [Google](https://github.com/googleapis), opens a release pull request from your conventional commits so each merge cuts a versioned GitHub release. releases, automation.
- [F5Bot](https://f5bot.com) by [F5Bot](https://f5bot.com), free keyword alerts that email you within minutes when your terms appear on Reddit, Hacker News, or Lobsters. reddit, monitoring, free.
- [Subreddit Signals](https://www.subredditsignals.com) by [Subreddit Signals](https://www.subredditsignals.com), finds relevant subreddits and classifies buyer intent so you can reply where people already have the problem. reddit, research.

## Playbook

### GitHub
1. Write the README to convert on the first screen, one sentence saying what it does and for whom, then a GIF or terminal demo, then a copy paste install that works on the first try.
2. Add topics and a Shields.io badge row so the repo surfaces in GitHub search and reads as maintained.
3. Get your first 50 stars from people you actually know, teammates and friends, before any public launch.
4. Automate releases with release-please or semantic-release and keep a user facing changelog, then announce each release with a short clip of what changed.
5. Watch Insights, Traffic for referring sites and pair it with star-history, then spend next month on the channel that produced the most stars per hour.

### X
1. Post your build in public, real commits, deploys, and revenue numbers, turning development work you already did into content.
2. Reply fast and often to established builders in your niche, ideally within the first minutes of their post, this is the reply first tactic that compounds reach.
3. Ship consistently, a weekly update with a fresh demo beats one viral post a year.
4. Lead threads with a concrete result or screenshot, not a hook promise, and keep the first post self contained.

### Reddit
1. Pick three to five subreddits where your user already hangs out and read them for a week before posting anything.
2. Spend weeks replying helpfully first, then make one launch post in the single best subreddit, cross posting the same thing to five subreddits gets you banned from five.
3. Frame the post as a technical, honest description, no hype, and answer every comment with what you changed.
4. Run F5Bot on your product and problem keywords so you can join threads where people are asking, within minutes.

## FAQ

**How do I grow a GitHub repo and get stars?**
Build something that solves a real problem, then make the README convert on the first screen with a one line description and an immediate demo. Seed your first stars from people you know, launch in the specific communities where your users are, and keep shipping releases with a visible changelog. Stars are a discoverability and credibility signal, not a usage metric, so track referring sites in Insights and reinvest in whatever channel actually sent stargazers.

**What is a build in public playbook that still works in July 2026?**
Building is no longer the bottleneck, distribution is, so run two channels at a time well instead of all of them badly. The channels that convert for developers are build in public on X, a single niche subreddit you have earned trust in, and turning your own commits, releases, and revenue into posts. Sequence it, gain traction in one, then layer in the next, and plan for real traction to take many months, not weeks.

**What is the right Reddit launch strategy for a developer product?**
Reddit converts higher per hour than X or LinkedIn for many indie products, but only if you have context in the community first. Find three to five relevant subreddits, lurk and reply for a week or more, then make one honest launch post in the best fit subreddit and reply to every comment. A hundred clicks from people with the exact problem beat a thousand from an audience with no context, and mass cross posting is the fastest way to get banned.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
