# webapp-testing — let Claude test your UI in a real browser

> Static analysis misses JavaScript errors. A real browser doesn't.

**Install:** `claude skill add anthropic/webapp-testing`  
**Stars:** official Anthropic skill  
**License:** MIT

## What is the webapp-testing skill?

**webapp-testing is an official Anthropic Claude Code skill that opens your locally running app in a real Playwright browser, exercises the UI, catches JavaScript errors and broken interactions, and iterates until the experience is correct — all without you leaving the editor.** It closes the gap between "the code looks right" and "the UI works right," which are two very different things in any frontend project.

## Why solo builders use it

A solo builder has no QA team. The verification loop for a UI change is typically: make the change, switch to a browser, click around, spot the issue, switch back. webapp-testing collapses that loop. Claude writes the code, opens the browser, tests the interaction, reads the console errors, fixes what's wrong, and tests again. You see the result, not the process.

The skill shines for the class of bugs that are invisible to static analysis: a button that renders correctly but fires the wrong event handler, a form that submits but silently swallows the response, a modal that opens but traps focus so the keyboard stops working. These bugs only show up when something actually runs in a browser, and webapp-testing puts a real browser inside the Claude Code session.

The practical loop is: ship a feature, run `/webapp-testing`, let Claude exercise the core flows, read the findings, fix them in the same session. For a solo builder shipping to production without a staging review, that loop is the difference between a clean release and an embarrassing hotfix.

## Example

```
/webapp-testing test the checkout flow end-to-end: add item to cart, proceed to payment, verify the order confirmation renders
```

Claude opens the browser, clicks through the flow, reports any JavaScript errors or broken states, and optionally fixes them.

## Pairs well with

- [mcp-builder](mcp-builder.md) — build the tools in one session with mcp-builder, verify they work in the browser with webapp-testing

## Source

[github.com/anthropics/claude-code-skills](https://github.com/anthropics/claude-code-skills)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
