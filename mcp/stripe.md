# Stripe MCP

> Inspect customers, subscriptions, payments, and disputes from inside Claude — without opening the dashboard.

| | |
|---|---|
| **Made by** | Stripe (official) |
| **Install** | `claude mcp add stripe -- npx -y @stripe/mcp --api-key $STRIPE_RESTRICTED_KEY` |
| **Auth** | Stripe restricted API key |
| **License** | MIT |

## What is the Stripe MCP?

The Stripe MCP lets an agent read and query your Stripe account — customers, subscriptions, payment intents, invoices, disputes, and refunds — directly from Claude. It uses restricted keys scoped to only the permissions you grant, so your secret key never touches the MCP layer. Think of it as a natural-language Stripe dashboard.

## Why solo builders use it

Churn investigation used to mean opening five Stripe tabs, filtering by date, exporting CSVs, and doing mental math. With the Stripe MCP, the same workflow becomes a single prompt: "show me all subscriptions that cancelled in the last 14 days, with the customer email and their last invoice amount." Claude assembles the picture in one turn.

The key discipline here is key scope. Create a restricted key in your Stripe dashboard that grants only read access to the resources you need — customers, subscriptions, charges — and nothing else. Never wire this MCP to your full secret key. A restricted key means that even if something goes wrong with a prompt, no money moves and no data gets written.

Beyond churn analysis, solo founders use this for revenue sanity checks during deploys ("has MRR moved since this morning?"), for customer support lookups, and for building internal dashboards where Claude drafts the narrative around the numbers. It turns your billing data into a conversational interface.

## Setup

Create a restricted key at [dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys) with only read permissions on the objects you need.

```bash
export STRIPE_RESTRICTED_KEY=rk_live_...

claude mcp add stripe -- npx -y @stripe/mcp --api-key $STRIPE_RESTRICTED_KEY
```

Or in config:

```json
{
  "mcpServers": {
    "stripe": {
      "command": "npx",
      "args": ["-y", "@stripe/mcp", "--api-key", "rk_live_..."]
    }
  }
}
```

## Example

```
Use the Stripe MCP to find all subscriptions that churned in the last 7 days.
For each one, show the customer email, plan name, amount, and the reason for cancellation if available.
Then summarize the total lost MRR.
```

## See also

- [Supabase MCP](supabase-mcp.md) — query your app database alongside billing data
- [Notion MCP](notion-mcp.md) — push churn summaries into a Notion dashboard

## Source

[github.com/stripe/agent-toolkit](https://github.com/stripe/agent-toolkit) · [docs.stripe.com/mcp](https://docs.stripe.com/mcp)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
