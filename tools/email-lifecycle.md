# Email and Lifecycle Tools for Solo Builders

The email stack a one person AI product actually runs on, split by job. Transactional and lifecycle senders wire straight into your app, newsletter platforms grow an audience, and the self hosted options keep your list on your own infra. Checked live in July 2026.

## Transactional and lifecycle

- [Resend](https://resend.com) by [Resend](https://resend.com), an email API you drop into your app to send signup confirmations and password resets from a few lines of code. free tier: 3,000 emails a month. mcp, transactional, developer first.
- [Loops](https://loops.so) by [Astrodon](https://loops.so), product, marketing, and transactional email in one tool built for SaaS, so onboarding sequences and receipts live in the same place. free tier: 1,000 contacts. lifecycle, saas, mcp via partners.

## Newsletters

- [Kit](https://kit.com) by [Nathan Barry](https://kit.com), the creator first platform formerly called ConvertKit, with visual automations and a landing page builder for writers who sell. free tier: up to 10,000 subscribers. newsletter, creators, automations.
- [beehiiv](https://www.beehiiv.com) by [beehiiv](https://www.beehiiv.com), a newsletter platform with a built in website, referral program, and ad network for people treating the list as a business. free tier: unlimited sends. newsletter, growth, monetization.
- [Buttondown](https://buttondown.com) by [Justin Duke](https://www.jmduke.com), a deliberately small Markdown first newsletter tool from an independent bootstrapped shop. free tier: up to 100 subscribers. newsletter, minimal, indie.

## Self-hosted and open source

- [Listmonk](https://github.com/knadh/listmonk) by [Kailash Nadh](https://github.com/knadh), a single Go binary plus PostgreSQL that runs your whole mailing list on hardware you control. free tier: agplv3, self host. self hosted, open source, bring your own smtp.
- [Novu](https://github.com/novuhq/novu) by [Novu](https://github.com/novuhq), open source notification infrastructure that fans one event out to email, SMS, push, and an in app inbox. free tier: mit core, 10k events a month cloud. self hosted, open source, mcp.

## FAQ

**What is the best transactional email for an indie SaaS?**
Resend is the default pick for a solo builder because it reads like a normal developer API instead of a marketing suite, and the free 3,000 emails a month covers most early apps. If you want transactional receipts and lifecycle onboarding sequences in the same tool, Loops is the better fit since it treats product email and marketing email as one contact list. Both keep you off the enterprise sales call.

**What is the best newsletter platform for a solo builder?**
It depends on whether the list is the product or a channel. Buttondown suits someone who wants to write in Markdown, keep it tiny, and support an independent maker, with a free tier up to 100 subscribers. Kit gives you 10,000 free subscribers plus automations and landing pages if you plan to sell digital products, and beehiiv leans hardest into growth with a referral program and ad network baked in.

**What is a good open source alternative to Mailchimp?**
Listmonk is the closest self hosted replacement, a single Go binary backed by PostgreSQL that handles campaigns, segmentation, and transactional sends, licensed AGPLv3 so you can run it on your own server. You bring your own SMTP or SES for delivery, which is where the real cost lives, but your subscriber list never leaves your infrastructure. For notifications rather than newsletters, Novu covers email plus SMS, push, and in app inbox from one open source stack.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
