# OpenRouter — one API key, every model

> Route 400+ models from 70+ providers through a single OpenAI-compatible endpoint.

## What is OpenRouter?

**OpenRouter is an LLM router that gives you access to hundreds of AI models — OpenAI, Anthropic, Google, Meta, DeepSeek, Mistral, and more — behind one API key and one OpenAI-compatible endpoint.** You swap models by changing a string, with automatic fallback and unified billing, so a solo app never gets locked to a single provider.

## Quick facts

- **Website:** [openrouter.ai](https://openrouter.ai)
- **API:** yes — OpenAI-compatible (`https://openrouter.ai/api/v1`)
- **CLI:** none official; works with any OpenAI-compatible CLI/SDK by setting the base URL
- **MCP:** no official server; call it from an agent via a generic OpenAI-style MCP wrapper
- **Free tier:** yes — free models + a free daily request quota

## What you build with it

- The "AI step" in any app or [automation](../README.md#automation--agent-frameworks) — one key covers every model.
- Cost control: route cheap models for bulk work, premium for the visible 10%.
- A/B different models without rewriting code.

## Example

Point any OpenAI SDK at OpenRouter:

```python
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=KEY)
client.chat.completions.create(model="anthropic/claude-...", messages=[...])
```

## Alternatives

[Together AI](https://together.ai) and [Groq](https://groq.com) for open models and speed; see [LLM API Routers](../README.md#llm-api-routers--aggregators).

## Source

[openrouter.ai](https://openrouter.ai) · [docs](https://openrouter.ai/docs)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
