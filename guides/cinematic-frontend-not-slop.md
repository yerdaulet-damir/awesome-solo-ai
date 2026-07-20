# How to Make Your AI-Generated Frontend Not Look Like Slop

> The patterns that expose AI slop, the stack that kills them, and the Claude skills that do it automatically.

## What AI slop UI actually looks like

You know it when you see it: Inter or Roboto at 16px, a split hero with text left and a floating card right, eight feature cards in a 3×3 grid, a teal gradient CTA button, rounded-everything at 12px, and a font pairing of "bold sans for headings, regular sans for body." Every section is the same height. Nothing moves. It loads fine and reads like every other AI-generated site.

The problem is not that the code is bad. The problem is that a language model trained on the web has learned the most statistically common UI patterns — and median web design is slop. Asking Claude to "build a landing page" without constraints produces the median.

The fix is constraints. The right stack, the right Claude skills, and a short list of patterns to explicitly ban.

## The anti-slop stack

**GSAP + Lenis + Framer Motion** — detailed setup in [tools/frontend-motion.md](../tools/frontend-motion.md).

The short version: Lenis for smooth scroll inertia, GSAP ScrollTrigger for scroll-pinned scenes and scrubbed timelines, Framer Motion for React component transitions. These three libraries are what the sites that win Awwwards actually run on. They are not hard to add — the Lenis + GSAP wiring is 6 lines.

**Space Grotesk or Syne or DM Serif** instead of Inter. Or better: a variable font with a wide optical range (Satoshi, Cabinet Grotesk, Familjen Grotesk). The font choice exposes AI output faster than any other single decision.

**One accent colour at 90% saturation** instead of teal/purple gradients. Pick one. Use it in one place. The rest is near-black, near-white, and a muted mid-tone.

## The pattern ban-list

Stop Claude from generating these by adding them to your CLAUDE.md or prompt:

```
DO NOT use:
- Inter or Roboto as the primary typeface
- Split-hero layout (text left, image/card right in a 50/50 grid)
- Feature card grids (3-up or 4-up icon + title + description cards)
- Teal or purple gradient CTA buttons
- border-radius > 8px on primary containers
- "Lorem ipsum" placeholder text
- Stock photo illustrations or undraw.co icons
- Eyebrow text above every heading ("WHY CHOOSE US", "FEATURES", "TESTIMONIALS")
- Section backgrounds that alternate white/light grey
```

## Scroll-driven animation: the one pattern that changes everything

A static page with good typography looks polished. A page where the hero headline assembles letter by letter as you load, where sections reveal with a 28px Y-translate and a power3.inOut ease, and where the 3D element in the background responds to scroll position — that reads as intentional.

The minimum viable version with GSAP:

```js
// Staggered reveal on scroll — works on any element with class .reveal
gsap.utils.toArray('.reveal').forEach(el => {
  gsap.from(el, {
    opacity: 0, y: 28, duration: 0.9, ease: 'power3.inOut',
    scrollTrigger: { trigger: el, start: 'top 88%' }
  })
})
```

Add this, wrap your sections in `.reveal`, and the page already reads differently. The ease matters: `power3.inOut` is the one easing that feels designed rather than default.

## Claude skills that enforce taste automatically

**[ui-ux-pro-max](../skills/ui-ux-pro-max.md)** — invoke before any frontend task and Claude gets 161 palettes, 57 font pairings, and 99 UX guidelines as active context. It makes the "which font and colour" decision before writing the first line of code.

**award-winning-motion** — the GSAP + ScrollTrigger + Lenis playbook as a skill. Handles scroll pinning, scrub timelines, cinematic preloaders, and image-sequence scroll-zoom. Invoke it when you want motion, not just code.

**scroll-world** — scroll-driven narrative sequencing skill. Each section escalates one story instead of listing features in isolation.

**[ponytail](../skills/ponytail.md)** — stops Claude from generating 400-line component files when 40 lines would work. Slop UI often comes with slop code.

## The one-prompt version

If you want a single prompt that enforces all of this, put this in your CLAUDE.md:

```
Frontend constraints (enforced on every UI task):
- Typeface: Space Grotesk for display, JetBrains Mono for code/labels, system-ui fallback
- Palette: near-black bg (#080b0a), one teal accent (#0d9488 / #19e3c2), muted text (#8b9692)
- Animation: GSAP + Lenis (lerp 0.09) + ScrollTrigger. Ease: power3.inOut only.
- Reveals: opacity 0 → 1, translateY 28px → 0, staggered. Use .js class guard for no-JS fallback.
- No split heroes, no feature card grids, no gradient CTAs, no Inter, no teal/purple gradients.
- Performance: transform/opacity only, will-change on animating elements, DPR cap at 2, reduced-motion respected.
```

## FAQ

**What makes a frontend look like it was AI-generated?**
The fastest tells: Inter at default weight, split hero, 3-column feature cards, gradient CTA button, and every section at the same height with the same padding. These are the most common patterns in training data, so they are the most statistically likely output without constraints.

**Is GSAP free?**
The core GSAP library and ScrollTrigger are free for most use cases including commercial projects. Some premium plugins (SplitText, MorphSVG) require a paid licence. Lenis and Framer Motion are both MIT.

**GSAP or Framer Motion?**
GSAP for scroll-driven, pinned, scrubbed, or timeline-sequenced animations. Framer Motion for React component transitions, gesture handling, and layout animations. They do not compete — use both. Wire Lenis to GSAP's ticker and Framer Motion handles components inside.

**How do I make Claude use these patterns by default?**
Add the constraint block above to your CLAUDE.md. Alternatively, install the ui-ux-pro-max and award-winning-motion Claude skills — they inject the relevant context automatically when Claude touches frontend code.

## Go deeper

- [Frontend Motion Stack](../tools/frontend-motion.md) — GSAP, Lenis, Framer Motion setup
- [ui-ux-pro-max skill](../skills/ui-ux-pro-max.md) — design-system generation before you write a line
- [Kill AI-slop code](kill-ai-slop-code.md) — same principle applied to the code layer
- [Build your own AI SaaS](../build/your-own-ai-saas.md) — full frontend + backend stack

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
