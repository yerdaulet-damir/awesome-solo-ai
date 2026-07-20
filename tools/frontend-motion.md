# Frontend Motion Stack

> GSAP + Lenis + Framer Motion — the three libraries that separate cinematic from slop.

| | |
|---|---|
| **GSAP** | [gsap.com](https://gsap.com) · free for most use, commercial license for some plugins |
| **Lenis** | [github.com/darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) · MIT |
| **Framer Motion** | [motion.dev](https://motion.dev) · MIT (was `framer-motion`, now `motion`) |

## What is the frontend motion stack?

GSAP (GreenSock Animation Platform) is the industry-standard JavaScript animation engine — timeline control, ScrollTrigger for scroll-driven scenes, and pinning. Lenis is a smooth-scroll wrapper that normalises scroll velocity across browsers and wires into GSAP's ticker. Framer Motion is the React animation library with a declarative API for component transitions, gestures, and layout animations.

## The three tools and when to use each

**GSAP + ScrollTrigger** is the power tool. Use it when you want scroll-pinned sequences, scrubbed timelines, staggered reveals, or anything that needs precise frame control. ScrollTrigger fires animations based on scroll position — pin a section, scrub a timeline, sync video to scroll. This is what award-winning sites run on.

**Lenis** fixes the one thing browsers get wrong: scroll inertia. Native scroll jumps; Lenis gives it momentum and lerp control. Wire it to GSAP's ticker and every ScrollTrigger animation gets smooth input automatically. Drop-in, ~1KB, no configuration needed beyond `lerp: 0.09`.

**Framer Motion (motion)** is for React. Declarative — `animate`, `initial`, `exit`, layout animations that just work, gesture handling (`whileHover`, `whileTap`), and `AnimatePresence` for route transitions. Use it for component-level animation; use GSAP when you need timeline control or ScrollTrigger across the whole page.

They stack: Lenis → GSAP ticker → ScrollTrigger on the page level, Framer Motion inside React components.

## Setup (GSAP + Lenis, HTML/vanilla)

```js
import Lenis from 'lenis'
import gsap from 'gsap'
import ScrollTrigger from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const lenis = new Lenis({ lerp: 0.09 })
lenis.on('scroll', ScrollTrigger.update)
gsap.ticker.add(t => lenis.raf(t * 1000))
gsap.ticker.lagSmoothing(0)
```

## Setup (Framer Motion, React/Next.js)

```bash
npm install motion
```

```jsx
import { motion, AnimatePresence } from 'motion/react'

// reveal on scroll
<motion.div
  initial={{ opacity: 0, y: 28 }}
  whileInView={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}
  viewport={{ once: true }}
>
```

## Claude skills for motion

- **[award-winning-motion](https://github.com/anthropics/skills)** — the GSAP + ScrollTrigger + Lenis playbook as a Claude skill; scroll-pinning, scrub, cinematic preloaders, image-sequence scroll-zoom
- **[ui-ux-pro-max](../skills/ui-ux-pro-max.md)** — 161 palettes and design system generation; use before motion to get the right tokens
- **[scroll-world](https://github.com/anthropics/skills)** — scroll-driven storytelling skill; narrative sequencing across sections

## Performance rules

- Cap `devicePixelRatio` at 2 (Three.js) or 1.5 on mobile
- Use `will-change: transform, opacity` only on animating elements — remove after animation
- `transform` and `opacity` only — never animate `top`, `left`, `width`, `height`
- Pause renders when tab is hidden: `document.addEventListener('visibilitychange', ...)`
- `prefers-reduced-motion`: `@media (prefers-reduced-motion: reduce)` kills all reveals, respects user setting

## Source

[gsap.com](https://gsap.com) · [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) · [motion.dev](https://motion.dev)

---

_Part of [Awesome Solo AI](../README.md) — curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
