# Supabase MCP

> Connect Claude directly to your Supabase project — query data, manage tables, generate types, fetch logs.

| | |
|---|---|
| **Made by** | Supabase (official, supabase-community) |
| **Install** | `claude mcp add supabase -- npx -y @supabase/mcp-server-supabase --project-ref $SUPABASE_PROJECT_REF` |
| **Auth** | Supabase service key (`SUPABASE_SERVICE_ROLE_KEY`) |
| **License** | MIT |

## What is the Supabase MCP?

The Supabase MCP lets an agent manage tables, query rows, fetch project config, generate TypeScript types, and retrieve service logs from a Supabase project, all without leaving Claude. It supports a read-only mode flag for safe exploration, making it the most natural database MCP for any Next.js and Supabase solo SaaS.

## Why solo builders use it

The gap between "I need to check something in the database" and actually checking it is usually five clicks and a copy-pasted SQL query. The Supabase MCP closes that gap entirely. Schema questions, data investigations, type generation — they all become prompts instead of context switches.

For active development, the TypeScript type generation tool alone saves meaningful time. Ask Claude to introspect your current schema and generate up-to-date types, then write them into your `types/supabase.ts` file in one step. No manual `supabase gen types` invocation, no copy-paste, no outdated types silently causing bugs.

In production, read-only mode lets you hand this MCP to an ops workflow without worrying about accidental writes. You can query recent user signups, investigate a specific row, or pull logs from a failed edge function — all from Claude, all safely. Pair it with the Stripe MCP and you have a full-stack investigation tool: cross-reference who signed up with what they paid.

## Setup

```bash
export SUPABASE_PROJECT_REF=your_project_ref
export SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

claude mcp add supabase -- npx -y @supabase/mcp-server-supabase \
  --project-ref $SUPABASE_PROJECT_REF
```

For read-only access, add `--read-only`:

```bash
claude mcp add supabase -- npx -y @supabase/mcp-server-supabase \
  --project-ref $SUPABASE_PROJECT_REF --read-only
```

## Example

```
Use the Supabase MCP to query the users table and show me everyone who signed up in the last 48 hours.
Then generate up-to-date TypeScript types for the entire schema and write them to src/types/supabase.ts.
```

## See also

- [Stripe MCP](stripe.md) — cross-reference billing data with your app database
- [GitHub MCP](github.md) — trigger deploys after schema migrations

## Source

[github.com/supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) · [supabase.com/docs/guides/ai/mcp](https://supabase.com/docs/guides/ai/mcp)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
