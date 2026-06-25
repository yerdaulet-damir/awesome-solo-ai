# Playbook: Automate SaaS Billing + Onboarding from Day One

Stripe from the first commit. Supabase for user state. Resend for transactional email. Claude Code writes the schema migrations, the webhook handlers, and the onboarding sequence — in one session.

## Stack

| Layer | Tool |
| --- | --- |
| Payments | [Stripe MCP](../README.md#mcp-servers) |
| Database + auth | [Supabase](https://supabase.com) (Supabase MCP) |
| Transactional email | [Resend](https://resend.com) |
| Coding agent | [Claude Code](../README.md#ai-coding-agents) |

## What to set up on day one

**In Stripe:** create one Product with two Prices (monthly and annual). Enable the customer portal. Set up a webhook endpoint pointing to your Vercel deploy URL — you need these events: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`, `invoice.payment_failed`. Don't add more events until you need them.

**In Supabase:** two tables beyond your app data — `customers` and `subscriptions`. The `customers` table maps Supabase auth user IDs to Stripe customer IDs. The `subscriptions` table stores the current plan, status, and period end date. This is the source of truth your app checks for feature gating.

## What to skip early

Skip metered billing, usage-based pricing, and multiple tiers until you have 20 paying customers. Proration math is complex and your first users don't need it. One flat monthly price and one flat annual price is enough to learn whether people will pay.

Skip invoice customization, tax configuration, and dunning sequences for the first month. Stripe's defaults handle these adequately. Configure them properly once you have revenue worth protecting.

## The one RLS policy that will bite you

In Supabase, when you enable Row Level Security on the `subscriptions` table and write the policy as `auth.uid() = user_id`, it works for reads — but your webhook handler runs server-side with the service role key, and service role bypasses RLS entirely. The trap: you write a policy, test it in the Supabase dashboard as an authenticated user, it looks right, and then you forget that your webhook upserts with service role. Six months later you add a second policy or switch to a different auth pattern and the writes silently break.

The fix: write a dedicated `upsert_subscription` Postgres function with `SECURITY DEFINER`, call it from your webhook handler. The function owns the mutation; RLS policies govern reads. Keep mutation logic in one place.

## The Claude Code session

Tell Claude Code: "Using Stripe MCP and Supabase MCP: (1) create the customers and subscriptions tables with migrations, (2) write a Next.js API route that handles these four Stripe webhook events and keeps the subscriptions table in sync, (3) write a `checkSubscription(userId)` helper that reads from Supabase and returns the current plan, (4) write three Resend email templates — welcome, payment failed, and trial ending in 3 days."

Review the webhook handler carefully. Verify that it checks the Stripe signature before processing any event (`stripe.webhooks.constructEvent`). This is not optional — an unverified webhook endpoint is a security hole.

## The onboarding sequence

The welcome email fires from the `checkout.session.completed` webhook handler, immediately after the subscription row is written. Use Resend's React email templates — they render consistently and Claude Code can write them. The "payment failed" email fires from `invoice.payment_failed` with a direct link to the Stripe customer portal. The "trial ending" email is a scheduled job (a Supabase cron or a Vercel cron) that queries for subscriptions expiring in 3 days and sends via Resend.

Three emails, one session, Stripe from day one. Everything you add later builds on a foundation that already works.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
