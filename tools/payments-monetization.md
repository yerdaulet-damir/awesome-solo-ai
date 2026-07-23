# Payments and Monetization for Solo Builders

The tools solo builders actually use to charge money for an AI product or SaaS, from raw processors to merchants of record that file your taxes to self hostable billing. Checked live in July 2026. This is not financial advice.

- [Stripe](https://stripe.com) by [Stripe](https://stripe.com), the default card processor at 2.9% plus $0.30, with Stripe Managed Payments now offering a merchant of record option at 5% plus $0.50. processor, mor option, active.
- [Lemon Squeezy](https://lemonsqueezy.com) by [Stripe](https://stripe.com), a flat 5% plus $0.50 merchant of record for indie digital products, now owned by Stripe and folding into Stripe Managed Payments. merchant of record, digital products, maintenance mode.
- [Polar](https://polar.sh) by [Polar Software](https://github.com/polarsource/polar), an open source merchant of record built on Stripe, 5% plus $0.50 free tier with paid plans that drop the rate as you grow. merchant of record, open source, developer first.
- [Paddle](https://paddle.com) by [Paddle.com Market Ltd](https://paddle.com), a mature 5% plus $0.50 merchant of record aimed at SaaS that has outgrown a raw processor. merchant of record, saas, established.
- [Creem](https://creem.io) by [Armitage Labs](https://creem.io), a merchant of record at 3.9% plus $0.40 with no monthly fee, pitched straight at indie hackers and AI startups. merchant of record, low fee, indie.
- [Gumroad](https://gumroad.com) by [Gumroad](https://gumroad.com), a flat 10% plus $0.50 merchant of record that is the fastest way to sell a digital download or template. merchant of record, digital downloads, simple.
- [Lago](https://getlago.com) by [Getlago](https://github.com/getlago/lago), open source usage based metering and billing you self host with no per transaction fee, good for token or seat metering. open source, usage billing, self hosted.
- [Kill Bill](https://killbill.io) by [The Billing Project](https://github.com/killbill/killbill), a 15 year old Apache licensed billing engine with a plugin for everything, for teams that need deep control. open source, enterprise, self hosted.
- [Keygen](https://keygen.sh) by [Keygen](https://github.com/keygen-sh/keygen-api), a license key and device activation API you can self host free to gate desktop or on prem software. open source, licensing, self hosted.
- [Stripe Agent Toolkit](https://github.com/stripe/agent-toolkit) by [Stripe](https://stripe.com), Python and TypeScript function calling wrappers that let LangChain, CrewAI, and the OpenAI Agents SDK charge cards. agent sdk, function calling, active.
- [Stripe MCP](https://mcp.stripe.com) by [Stripe](https://stripe.com), an OAuth remote MCP server exposing around 25 payment operations to any MCP client. mcp, payments, active.
- [Polar MCP](https://mcp.polar.sh/mcp/polar-mcp) by [Polar Software](https://polar.sh), a remote MCP server that gives an agent live access to your Polar orders and products. mcp, merchant of record, active.

## FAQ

**What is the best way to accept payments as a solo SaaS?**
If you sell to customers in multiple countries, a merchant of record like Polar, Paddle, Creem, or Lemon Squeezy is usually the least painful start, because they file the sales tax you would otherwise owe in dozens of jurisdictions. If you are US only or want the lowest headline rate, Stripe direct at 2.9% plus $0.30 is cheaper, but you own the tax paperwork. Many builders launch on a merchant of record and only move to raw Stripe once the fee gap gets large enough to fund an accountant.

**Stripe vs Lemon Squeezy vs Polar, which one?**
Stripe is a raw processor, so you keep more per sale but handle global tax yourself. Lemon Squeezy and Polar are both merchants of record at roughly 5% plus $0.50, so they cost more per sale but remit VAT and sales tax for you. Polar is open source and developer first with an MCP server and grandfathered lower rates for early orgs, while Lemon Squeezy is now a Stripe property in maintenance mode, so for a new project Polar or Stripe direct is the more future proof pick.

**What is a merchant of record and do I need one?**
A merchant of record is the legal seller of your product, which means the customer technically buys from them and they collect, file, and remit VAT, GST, and US sales tax on your behalf. You need one if you sell digital products or subscriptions internationally and do not want to register for tax in the EU, UK, and dozens of other places. If you only sell to US business customers or you already have accounting in place, a plain processor like Stripe is cheaper and the merchant of record premium of roughly 1.5 to 2 points is not worth it.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
