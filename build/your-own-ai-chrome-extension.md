# Build Your Own AI Chrome Extension

> The lowest-CAC AI product model: ship a browser extension with an AI brain in 72 hours.

## What you're building

An AI Chrome extension adds a language model capability directly into the user's browser — a sidebar, a right-click action, a popup, or an overlay that works on any page. The end result is a product users install once and get value from repeatedly across every website they visit, with no separate app to open. Chrome extensions have near-zero customer acquisition cost because the Chrome Web Store is a discovery channel, and the install flow takes 10 seconds.

## The stack

| Layer | Tool | Why this one | Deep page |
|---|---|---|---|
| AI backend | Claude API (via Anthropic) | Best reasoning quality for text tasks; system prompt control; affordable at typical extension usage volumes | — |
| Extension framework | Manifest V3 + Vite + CRXJS | CRXJS handles the MV3 hot-reload nightmare; Vite gives you React/TypeScript/Tailwind with zero config | — |
| Payments | Stripe MCP | Create products, prices, and customer portal from Claude Code; webhook to unlock premium features | [mcp/stripe.md](../mcp/stripe.md) |

## Build it

**Step 1 — Define the one action your extension does.** The Chrome Web Store rewards extensions that do one thing well. Write it as a user story: "As a user on any webpage, I can highlight text and have the extension [summarize / explain / translate / rewrite / critique] it." One action means one prompt template, one content script behavior, and a clear store listing description. Extensions that do five things get no reviews; extensions that do one thing get stars.

**Step 2 — Scaffold MV3 with Vite and CRXJS.** Run `npm create crxjs@latest` and select React + TypeScript. CRXJS generates a working MV3 extension with manifest.json, a popup, a background service worker, and a content script — all wired together with hot reload. You have a working extension that loads in Chrome within five minutes. Add Tailwind for styling: `npm i -D tailwindcss` and follow the Vite Tailwind guide.

**Step 3 — Inject the content script.** The content script runs on every page and listens for user actions — a text selection, a button click, a keyboard shortcut. Use the Selection API (`window.getSelection().toString()`) to capture highlighted text. Post a message to the background service worker with `chrome.runtime.sendMessage({ type: 'PROCESS_TEXT', text: selectedText })`. The content script handles DOM; the service worker handles API calls.

**Step 4 — Call the Claude API from the background service worker.** In the service worker, receive the message and POST to `https://api.anthropic.com/v1/messages` with your system prompt and the selected text as the user message. Store your API key in `chrome.storage.sync` rather than hardcoding it — let users enter their own key in the options page, or proxy through your own backend if you want to keep the key server-side. Stream the response back to the content script via `chrome.tabs.sendMessage`.

**Step 5 — Add a popup UI.** The popup (the small window that opens when users click the extension icon) is a React component. Display the AI response here, or show it as an inline tooltip on the page. Keep the popup under 400px wide — Chrome clips wider popups on smaller screens. Use Tailwind's `prose` class for rendered markdown output.

**Step 6 — Wire Stripe for a paywall.** Use the Stripe MCP in Claude Code to create a product ("Pro Plan", $7/mo) and a price object. Build a minimal options page with a "Upgrade" button that redirects to a Stripe Checkout session hosted on your domain (a single Vercel function). On successful payment, Stripe's webhook sets a flag in your database; your extension checks this flag when the user opens it. Gate the AI feature behind the flag — free users get 10 uses per day, paid users get unlimited.

**Step 7 — Submit to the Chrome Web Store.** Create a developer account ($5 one-time fee). Package your extension with `npm run build` — CRXJS outputs a zip file ready for upload. Write a clear store listing: one sentence describing the action, three screenshots showing the before/after, and a privacy policy URL (required — use a one-page site or Notion page). Approval takes 1-3 business days on first submission.

## What it costs

Chrome Web Store developer account: $5 one-time. Claude API: roughly $0.01 per typical extension use (one text selection → one response). At 1,000 daily active users with 3 uses each, that is $30/day — covered by 5 paying subscribers at $7/mo each. Vercel (for the Stripe webhook): free tier. Total to first 10 paying users: $5 + your Claude API dev testing costs.

## Real examples

Compose AI (acquired by Grammarly) started as a Chrome extension that autocompleted text in any input box. It reached 100,000 users before raising a dollar of funding. The core product was a content script, an LLM call, and a ghost-text overlay — under 300 lines of code.

A solo developer built "SummarizeThis" — highlight any article, press Ctrl+Shift+S, get a three-sentence summary in a tooltip. It reached 40,000 installs organically through the Chrome Web Store search, with no paid marketing. Monthly revenue from the $5/mo pro plan: $3,200.

## FAQ

**How do I build a Chrome extension with AI?**
Scaffold with CRXJS (`npm create crxjs@latest`), add a content script that captures user input (selected text, form field content, page HTML), send it to a background service worker, POST to the Claude API or your backend proxy from the service worker, and return the response to display in a popup or inline overlay. The full skeleton is under 100 lines across three files.

**What Manifest version should I use in 2026?**
Manifest V3 is mandatory — Google removed MV2 extension support from the Chrome Web Store in 2024. MV3 replaces background pages with service workers (ephemeral, no persistent state) and restricts certain APIs. The main practical difference: you cannot use `XMLHttpRequest` in service workers (use `fetch`), and service workers terminate after ~30 seconds of inactivity (save state to `chrome.storage` before that).

**How do I monetize a Chrome extension?**
The three models that work: freemium with a usage cap (free users get N uses/day, paid users get unlimited), one-time payment for a Pro version, and subscription with a Stripe customer portal. Freemium converts best for utility extensions where users discover value before paying. Keep prices low ($3-9/mo) — extension users are price-sensitive compared to SaaS users.

**What are the most common Chrome Web Store rejection reasons?**
Missing or vague privacy policy (required for any extension that handles user data or makes network requests). Permission justification — if you request `<all_urls>` host permission, the review team wants a clear explanation in your listing. Single-purpose violation — extensions that do unrelated things get rejected. Deceptive store listing screenshots — your screenshots must show the actual extension UI, not mockups. All four are fixable in under an hour.

## Go deeper

- [mcp/stripe.md](../mcp/stripe.md) — Stripe MCP for building the paywall from Claude Code
- [playbooks/ai-chrome-extension.md](../playbooks/ai-chrome-extension.md) — full Chrome extension build playbook with code
- [build/your-own-ai-saas.md](./your-own-ai-saas.md) — if you want a full web app backend behind the extension
- [tools/vercel.md](../tools/vercel.md) — deploy the Stripe webhook handler and API proxy
- [skills/mcp-builder.md](../skills/mcp-builder.md) — if you want to turn your extension's backend into a reusable MCP

---
_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
