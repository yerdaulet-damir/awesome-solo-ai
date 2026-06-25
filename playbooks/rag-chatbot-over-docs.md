# Playbook: RAG Chatbot Over Your Docs in a Weekend

Crawl your docs, embed them, store vectors in Postgres, and ship a chatbot that answers questions accurately — in two days, solo.

## Stack

| Stage | Tool |
| --- | --- |
| Crawl + ingest | [Firecrawl MCP](../README.md#mcp-servers) |
| Vector storage | [Supabase](https://supabase.com) pgvector |
| Embedding model | `text-embedding-3-small` (OpenAI) or Claude via [OpenRouter](../README.md#llm-api-routers--aggregators) |
| Query brain | [Claude](../README.md#ai-coding-agents) (claude-sonnet-4-5 or better) |
| Deploy | [Vercel](https://vercel.com) |

## The pipeline

1. **Crawl.** Point Firecrawl MCP at your docs URL. It returns clean markdown — no boilerplate, no nav junk. Tell Claude Code: "Crawl `docs.example.com`, write each page to `/corpus` as a markdown file."
2. **Chunk.** Split each page into ~400-token chunks with 50-token overlap. This is the most important tuning knob (more on this below). Claude Code writes the chunker in under five minutes.
3. **Embed.** Call the embedding API for each chunk. Store `(chunk_text, embedding vector, source_url, chunk_index)` in a Supabase table with a pgvector column.
4. **Retrieve.** At query time, embed the user question, run a cosine similarity search (`<=>` operator in Supabase) to pull the top-k chunks.
5. **Respond.** Feed the retrieved chunks as context into Claude. Prompt: "Answer using only the provided context. If the answer isn't there, say so." The "say so" clause is what separates a useful chatbot from a hallucination machine.
6. **Deploy.** Wrap the query-retrieve-respond chain in a Next.js API route, ship to Vercel. The Supabase connection string goes in environment variables.

## The one gotcha: chunk size vs. context tradeoffs

Short chunks (200 tokens) give precise retrieval — the right sentence surfaces — but miss context that spans paragraphs. Long chunks (1000+ tokens) preserve context but waste your context window with irrelevant text and make similarity search noisier. The sweet spot for most docs is **400–600 tokens with 10–15% overlap**. If your docs have a lot of code blocks, chunk by logical section (header → next header) rather than token count — code examples should stay whole.

A second trap: naive top-k retrieval grabs the most similar chunks by vector, but if your docs have repeated boilerplate ("see also", "note:") those surface constantly. Pre-filter by excluding chunks under 100 tokens before embedding.

## Cost shape

Embedding a 500-page docs site runs under $2 at `text-embedding-3-small` rates. Supabase free tier handles the vectors. The real cost is per-query Claude calls — control it with response caching for repeated questions.

## What to build next

Add a feedback loop: a thumbs-down on any answer logs the question + chunks to a Supabase table. Review it weekly. Those failures tell you exactly which docs are missing, ambiguous, or outdated — a RAG chatbot is the best docs quality signal you'll ever have.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
