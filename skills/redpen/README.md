# Redpen — anti-slop copywriting skill

> The old ad man with the red pen, inside your agent. Every line passes three tests or gets cut.

An original skill built for [Awesome Solo AI](../../README.md), in the shape of [ponytail](https://github.com/DietrichGebert/ponytail) (anti-slop for code) — but for words. It ports Harry Dry's copywriting method into a persistent agent persona: concrete over abstract, point don't talk, facts not adjectives.

**Install:** copy [`SKILL.md`](SKILL.md) into your `.claude/skills/redpen/` folder. Invoke with `/redpen` or just write copy while it's active.

## The three tests (the whole engine)

Every sentence runs all three, and a line that fails one gets cut *before* you move on:

1. **Can I visualize it?** — if you can't drop it on your foot, it's abstract.
2. **Can I falsify it?** — provably true/false makes ears prick up; adjectives don't.
3. **Can nobody else say it?** — never write an ad a competitor can sign.

## Proof, not adjectives

Redpen doesn't claim "better copy." It points. Same product, before and after the three tests:

| Slop (fails a test) | Redpen (passes all three) | Fix |
|---|---|---|
| "Don't just get a job — change an entire industry." | "Worn by supermodels in London and dads in Ohio." | can't visualize / anyone can say → concrete + ownable |
| "A powerful, seamless AI platform that empowers creators." | "1,000 songs in your pocket." | adjectives → one visual, falsifiable line |
| "The best all-in-one wellness supplement." | "You're going to need a smaller cabinet." | can't falsify → point at the outcome |
| "A dating app for meaningful long-term connections." | "The dating app designed to be deleted." | anyone can say → conflict + only-we-can-say |
| "Learn copywriting and grow your business fast!" | "You'll spend 22,000 hours writing. Spend 2 learning how." | vague claim → a fact that reframes cost as saving |

Every "after" line: you can picture it (test 1), it's true or false (test 2), and no competitor can sign it (test 3). It reads in one Mississippi, two Mississippi.

## Why it pairs with ponytail

[ponytail](../ponytail.md) kills slop in your **code**; redpen kills slop in your **words**. Same discipline — cut everything that isn't working, prove with the concrete, leave the one thing you can't improve. Run both and your product ships tight on both layers.

---

_Part of [Awesome Solo AI](../../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
