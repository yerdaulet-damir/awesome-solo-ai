# Playbook: Ship an AI Chrome Extension in 72 Hours

Extensions install at the workflow level — users hit your product every time they open a tab, not when they remember to visit your URL. The CAC is the lowest of any distribution channel right now. Here's the full build.

## Stack

| Layer | Tool |
| --- | --- |
| Extension framework | Manifest V3, Vite + CRXJS |
| AI calls | [Claude API](../README.md#ai-coding-agents) or [OpenRouter](../README.md#llm-api-routers--aggregators) |
| Paywall | [Stripe](https://stripe.com) (usage-based or subscription) |
| Backend (optional) | [Supabase](https://supabase.com) for user keys + quota |
| Deploy | Chrome Web Store |

## The build

**Day 1 — scaffold and DOM injection.** Set up Vite + CRXJS so hot reload works during development — this alone saves hours. Write a content script that injects a sidebar or floating button on target pages. The content script reads the DOM (selected text, page title, whatever you need) and passes it to the background service worker via `chrome.runtime.sendMessage`. Keep the content script thin; put logic in the background worker or a popup.

**Day 2 — Claude API call + UI.** The background service worker holds your API key (never in the content script — it's inspectable). POST to the Claude API with the DOM data as context, stream the response back to the content script, render it. For streaming in extensions, use `fetch` with `ReadableStream` in the service worker and relay chunks via `chrome.runtime.sendMessage` events. Add a settings popup for the user to paste their own API key if you want a bring-your-own-key model.

**Day 3 — Stripe paywall and submission.** Wire Stripe Checkout: when a free-tier limit is hit, open `chrome.tabs.create` pointing to your payment page. After payment, Stripe webhook updates the user's quota in Supabase; the extension checks quota on each call. Submit to Chrome Web Store — the review takes 1–3 business days.

## The three most common rejection reasons

**1. Excessive host permissions.** Requesting `<all_urls>` when you only need `https://linear.app/*` is a fast rejection. Declare the minimum hosts your extension actually needs. If you genuinely need broad access, write a detailed justification in the store listing.

**2. Remote code execution.** Loading scripts from a remote URL at runtime violates MV3 policy. All logic must be bundled at install time. This catches devs who try to dynamically load libraries — bundle them with Vite instead.

**3. Missing privacy policy for user data.** If your extension reads page content or sends anything to a server (including to Claude's API), you need a privacy policy URL in the manifest and the store listing. One paragraph on a hosted page is enough, but it must exist before submission.

## Distribution leverage

The extension model compounds: each install is a persistent presence in the user's browser. Focus the first version on one workflow — text selection → improve writing, or LinkedIn profile → CRM notes, or Jira ticket → draft PR description. Nail one use case, collect reviews, then expand. The store's "Users also viewed" algorithm does meaningful organic work once you have 50+ reviews.

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
