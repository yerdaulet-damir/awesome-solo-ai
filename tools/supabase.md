# Supabase — Postgres backend with vector search built in

> Database, auth, storage, and `pgvector` in one — the backend *and* the RAG store for a solo AI app.

## What is Supabase?

**Supabase is an open-source backend platform built on Postgres, providing a database, authentication, file storage, and realtime — with `pgvector` included, so it doubles as the vector store for retrieval-augmented generation.** For a solo AI builder it's one service that covers both the app backend and the embeddings layer.

## Quick facts

- **Website:** [supabase.com](https://supabase.com)
- **API:** yes — auto-generated REST + client SDKs
- **CLI:** yes — `supabase` CLI for local dev, migrations, deploy
- **MCP:** community MCP servers exist for querying/managing projects
- **Free tier:** yes — generous free project tier
- **Open source:** yes

## What you build with it

- The backend for any AI SaaS — users, data, files.
- A RAG pipeline: store embeddings in `pgvector`, query by similarity.
- Realtime features without running your own server.

## Example

```bash
supabase init && supabase start   # local stack
# store + query embeddings via pgvector for RAG
```

## Alternatives

[Convex](https://convex.dev) for reactive/agent-native backends; dedicated vector DBs (Pinecone, Qdrant) if you outgrow `pgvector`. See [Backend tools](../README.md#backend-deploy--analytics).

## Source

[supabase.com](https://supabase.com) · [docs](https://supabase.com/docs)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
