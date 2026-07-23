# Landing Page Libraries: Components, 3D, and Motion

The libraries below are what solo builders actually reach for in Cursor or Claude Code to ship a landing page that does not read as a template. All checked live in July 2026.

## Component and UI libraries

- [shadcn/ui](https://github.com/shadcn-ui/ui) by [shadcn](https://github.com/shadcn), copy the source into your repo and own it instead of installing a black box package, which is why every AI coding tool emits it by default. mit, react, tailwind.
- [HeroUI](https://github.com/heroui-inc/heroui) by [HeroUI Inc](https://github.com/heroui-inc), a full React Aria based component set with a v3 rewrite on Tailwind v4 that also ships React Native, so one design system covers web and app. mit, react, accessible.
- [Magic UI](https://github.com/magicuidesign/magicui) by [magicuidesign](https://github.com/magicuidesign), 50 plus animated marquees, beams, and text effects that drop into a shadcn project and read clean in both light and dark. mit, animated, marketing.
- [Aceternity UI](https://ui.aceternity.com) by Manu Arora, copy paste 200 plus effect heavy components like 3D cards and glowing beams for the dark Linear style SaaS look. animated, dark, effects. License varies per component, check before shipping.
- [Motion Primitives](https://github.com/ibelick/motion-primitives) by [Julien Thibeaut](https://github.com/ibelick), small focused motion pieces like scroll reveal and animated text that you paste in one at a time rather than adopting a whole kit. mit, motion, minimal.
- [Origin UI](https://github.com/origin-space/originui) by [Origin Space](https://github.com/origin-space), hundreds of Tailwind v4 blocks that follow shadcn conventions so they slot into an existing setup with no new mental model. mit, tailwind, blocks.
- [Cult UI](https://github.com/nolly-studio/cult-ui) by [Nolly Studio](https://github.com/nolly-studio), shadcn compatible components with built in micro interactions like animated navbars and testimonial carousels for marketing pages. mit, animated, shadcn.

## 3D on the web

- [Three.js](https://github.com/mrdoob/three.js) by [Ricardo Cabello](https://github.com/mrdoob), the WebGL library every other 3D web tool is built on, use it directly when you want a hand built hero scene. mit, webgl, 3d.
- [React Three Fiber](https://github.com/pmndrs/react-three-fiber) by [Poimandres](https://github.com/pmndrs), write Three.js as declarative React components and pull in the drei helper pack for cameras, loaders, and controls. mit, react, 3d.
- [react-spline](https://github.com/splinetool/react-spline) by [Spline](https://github.com/splinetool), design a 3D scene in the Spline editor, export a splinecode url, and drop it into a page with one component and no shader code. mit, no code, 3d.

## Templates and blocks

- [Tailark](https://github.com/tailark/blocks) by [Méschac Irung](https://github.com/meschacirung), free open source marketing blocks like hero, pricing, FAQ, and CTA built on shadcn, aimed at shipping a site not a dashboard. mit, marketing, blocks.

## Newer motion tools

- [Anime.js](https://github.com/juliangarnier/anime) by [Julian Garnier](https://github.com/juliangarnier), the v4 rewrite is now modular ES modules with a lighter footprint, a solid GSAP alternative when you do not need ScrollTrigger. mit, animation, lightweight.
- [NumberFlow](https://github.com/barvian/number-flow) by [Max Barvian](https://github.com/barvian), a dependency free component that animates changing numbers for pricing toggles and stat counters, works in React, Vue, Svelte, and vanilla. mit, react, micro.

## Claude skill for frontend

- [frontend-design](https://github.com/anthropics/skills) by [Anthropic](https://github.com/anthropics), an official Agent Skill that pushes Claude toward distinctive typography, color, and layout and explicitly away from purple gradient AI slop. skill, claude, design.

## FAQ

**What is the best React component library for landing pages right now?**
For a marketing page specifically, pair shadcn/ui as your base with Tailark for ready marketing blocks and Magic UI or Cult UI for the animated moments. All three copy source straight into your repo, so you keep full control and avoid a heavy runtime dependency. If you want an accessible batteries included kit instead of copy paste, HeroUI covers buttons, modals, and forms out of the box.

**What are good shadcn alternatives or additions in 2026?**
Most of these are additions rather than replacements, since they install through the shadcn CLI or paste into a shadcn project. Origin UI and Cult UI extend the primitive set, Magic UI and Aceternity add animated effects, and Tailark supplies full marketing sections. If you genuinely want a different base, HeroUI is the strongest standalone system, built on React Aria for accessibility rather than on shadcn's Radix plus Tailwind approach.

**What animation library should I use, and what are the Framer Motion alternatives?**
If you already run GSAP with ScrollTrigger and Lenis, keep that as your spine for scroll and pinning. Anime.js v4 is the lighter alternative when you only need timeline tweens without a scroll engine, and NumberFlow handles the specific case of animating changing numbers. For 3D moments reach for React Three Fiber, or export a Spline scene if you would rather design the 3D visually than write shaders.

---

_Part of [Awesome Solo AI](../README.md), curated by [Yerdaulet Damir](https://yerdaulet.xyz). The AI stack solo builders feed to Claude Code._
