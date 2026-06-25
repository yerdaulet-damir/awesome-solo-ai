# Build Your Own RAG Chatbot Over Your Docs

> Turn any document, website, or knowledge base into a chatbot that actually knows your content — in a weekend.

## What you're building

A RAG chatbot (Retrieval-Augmented Generation) answers questions by first retrieving the most relevant chunks from your documents, then passing those chunks as context to a language model that generates a grounded answer. The end result is a chat interface where users ask questions in plain English and receive accurate, cited answers drawn from your actual content — not from the model's training data. This eliminates hallucination on your domain-specific knowledge and lets you update the chatbot by updating your docs.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| Web crawling + ingestion | Firecrawl MCP | Crawls any website or PDF and returns clean markdown — no scraper code needed | [mcp/firecrawl.md](../mcp/firecrawl.md) |
| Vector database | Supabase pgvector | Postgres extension for embeddings — same database you're already using, no new infra | [tools/supabase.md](../tools/supabase.md) |
| LLM routing | OpenRouter | Routes to Claude or GPT for generation; easy to switch models without changing code | [tools/openrouter.md](../tools/openrouter.md) |
| Frontend + API | Vercel AI SDK | Streaming chat UI in Next.js with three lines; hooks for loading states and citations | [tools/vercel.md](../tools/vercel.md) |

## Build it

**Step 1 — Crawl and ingest your docs with Firecrawl.** In Claude Code, invoke the Firecrawl MCP's `crawl` tool with your documentation URL or upload your PDF. Firecrawl returns structured markdown with metadata (title, source URL, page number). Save the output as a JSON array of documents — this is your raw corpus. For PDFs, use Firecrawl's document extraction endpoint which handles multi-column layouts and tables cleanly.

**Step 2 — Chunk the text.** Split each document into chunks of 300–500 tokens with 50-token overlap between adjacent chunks. Overlap prevents answers from being split across a chunk boundary. A simple recursive character splitter works — LangChain's `RecursiveCharacterTextSplitter` is one option, or write a 20-line TypeScript function that splits on sentence boundaries up to the token limit.

**Step 3 — Embed with OpenAI or Cohere.** Call the embeddings API on each chunk — OpenAI's `text-embedding-3-small` is $0.02 per million tokens (very cheap) and produces 1536-dimensional vectors. Cohere's `embed-english-v3.0` is slightly higher quality for retrieval tasks. Store the embedding alongside the chunk text and source URL in a `documents` table in Supabase. Run this once on ingest; re-run only when docs change.

**Step 4 — Store in pgvector.** Enable the pgvector extension in Supabase (`CREATE EXTENSION vector`). Add a `embedding vector(1536)` column to your documents table. Create an HNSW index (`CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops)`) for fast similarity search at scale. Supabase's free tier supports pgvector with no configuration beyond enabling the extension.

**Step 5 — Build the retrieval query.** At query time, embed the user's question using the same embedding model. Run a Supabase RPC function that returns the top-5 most similar chunks by cosine distance: `SELECT * FROM documents ORDER BY embedding <=> $1 LIMIT 5`. Pass these chunks as context into your LLM prompt. The system prompt should instruct the model to answer only from the provided context and cite the source URL.

**Step 6 — Wire to Claude via OpenRouter and deploy the chat UI.** Create a Next.js API route that takes the user's message, retrieves context from Supabase, calls OpenRouter's streaming chat completions endpoint with context prepended, and streams the response back. Use Vercel AI SDK's `useChat` hook on the frontend — it handles streaming, message history, and loading states out of the box. Deploy to Vercel; the API route becomes a serverless function automatically.

## What it costs

Firecrawl free tier: 500 pages per month of crawling. Supabase free tier: 500MB Postgres storage, enough for hundreds of thousands of embedded chunks. OpenAI embeddings: roughly $0.02 per million tokens — embedding 1,000 pages costs under $0.10 total. OpenRouter generation: $0.003 per 1k output tokens at Claude Sonnet pricing. Vercel free tier: 100GB bandwidth. Total cost to first 100 users: approximately $0, plus pennies in embedding costs on ingest.

## Real examples

Mintlify (docs hosting) ships a RAG chatbot on every customer's documentation site — the "Ask AI" button that appears on docs.anthropic.com and hundreds of other dev docs sites is essentially this architecture. It crawls the docs on each deploy and reindexes changed pages.

A solo founder built a chatbot over 10 years of customer support tickets for a SaaS company. The bot deflects 40% of new tickets by finding a previous answer. The build took one weekend; the retrieval accuracy improved significantly after switching from naive chunking to sentence-boundary chunking.

## FAQ

**What is RAG and why does it matter?**
RAG stands for Retrieval-Augmented Generation. It matters because language models are trained on public data up to a cutoff date and have no knowledge of your private documents, internal wikis, or proprietary content. RAG solves this by dynamically retrieving relevant text at query time and injecting it into the model's context window. The model generates an answer grounded in your actual documents rather than guessing from training data — which eliminates hallucinations on your specific domain.

**How do I ingest PDFs into a chatbot?**
Use Firecrawl's document extraction endpoint, which handles PDFs natively. Pass a PDF URL or upload a file — Firecrawl returns clean markdown preserving headings, tables, and lists. For PDFs with complex layouts (multi-column academic papers, scanned documents), Firecrawl's extraction quality is significantly better than raw PDF parsing libraries. Alternatively, use `pdf-parse` (npm) for simple PDFs and feed the extracted text directly into your chunking step.

**What's the best vector database for a solo builder?**
Supabase pgvector for builders who already use Postgres — zero new infrastructure, free tier is generous, and SQL queries give you hybrid search (combine semantic similarity with keyword filters like `WHERE category = 'billing'`). Pinecone for builders who want a managed vector service with a generous free tier and serverless pricing. Chroma for local development — runs in-process with no server. For a production app serving real users, pgvector on Supabase is the lowest-complexity choice.

**How do I avoid hallucinations in my chatbot?**
Three practices eliminate most hallucinations. First, instruct the model explicitly: "Answer only using the context provided. If the answer is not in the context, say 'I don't know.'" Second, return citations alongside answers — include the source URL in each retrieved chunk and ask the model to cite it. When users can verify answers, they catch the rare mistake and trust the tool more. Third, use a reranker (Cohere Rerank API) to score retrieved chunks before sending them to the model — this removes irrelevant chunks that confuse the model into making things up.

## Go deeper

- [mcp/firecrawl.md](../mcp/firecrawl.md) — Firecrawl MCP: crawl any site or PDF into markdown
- [tools/supabase.md](../tools/supabase.md) — pgvector setup, RPC functions, RLS for multi-tenant RAG
- [tools/openrouter.md](../tools/openrouter.md) — model routing for the generation layer
- [playbooks/rag-chatbot-over-docs.md](../playbooks/rag-chatbot-over-docs.md) — full RAG build walkthrough with code snippets
- [build/your-own-ai-saas.md](./your-own-ai-saas.md) — add billing and auth to turn the chatbot into a product

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
