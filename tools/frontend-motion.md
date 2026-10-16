# Frontend Motion: GSAP, Motion, Lenis and Native CSS

Choose an animation tool by the interaction you need. Motion (formerly Framer Motion), GSAP and Lenis solve overlapping but different problems; installing all three is not a design requirement.

Updated 16 October 2026. See the [frontend design guide](../guides/cinematic-frontend-not-slop.md) for inspiration, components, 3D and agent skills.

## GSAP vs Motion vs CSS

| Tool | Use it for | Official starting point |
| --- | --- | --- |
| CSS transitions and keyframes | Hover, focus, simple state changes and short decorative effects | [MDN CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations) |
| CSS scroll-driven animations | Simple scroll/view progress without a JavaScript scroll listener | [Chrome guide](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) and [demos](https://scroll-driven-animations.style/) |
| Motion / Framer Motion | React gestures, layout changes and enter/exit transitions | [React docs](https://motion.dev/docs/react) |
| GSAP + ScrollTrigger | Sequenced timelines, pinning and scroll-scrubbed product stories | [ScrollTrigger docs](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) |
| Anime.js | DOM, SVG and JavaScript-value animation with timelines | [Current documentation](https://animejs.com/documentation/) |
| Lenis | Optional smooth scrolling and scroll-animation integration | [README and integration examples](https://github.com/darkroomengineering/lenis) |

Lenis changes input and scrolling behavior. Check nested scrollers, keyboard input, browser navigation and reduced motion before keeping it. Native scrolling is often enough.

## Motion in React or Next.js

Install the current package:

```bash
npm install motion
```

This client component shows Motion's gesture API on a working link. It stays visible before hydration and disables the transform effects for reduced motion:

```jsx
'use client';

import { motion, useReducedMotion } from 'motion/react';

export default function MotionDocsLink() {
  const reduceMotion = useReducedMotion();

  return (
    <motion.a
      href="https://motion.dev/docs/react"
      whileHover={reduceMotion ? undefined : { scale: 1.03 }}
      whileFocus={reduceMotion ? undefined : { scale: 1.03 }}
      whileTap={reduceMotion ? undefined : { scale: 0.98 }}
      transition={{ duration: reduceMotion ? 0 : 0.35 }}
    >
      Read Motion documentation
    </motion.a>
  );
}
```

CSS is enough if this is the only effect the page needs. When you add entry or scroll animations, keep important server-rendered content visible before animation code runs and test the actual loading path.

## GSAP setup and cleanup

Start with [GSAP installation](https://gsap.com/docs/v3/Installation/), then the [ScrollTrigger examples](https://gsap.com/docs/v3/Plugins/ScrollTrigger/). For React, use the official [@gsap/react integration](https://github.com/greensock/react) so animation lifecycle and cleanup follow the component. Use [gsap.matchMedia](https://gsap.com/docs/v3/GSAP/gsap.matchMedia()) for viewport and reduced-motion variants.

If you also choose Lenis, follow its current GSAP integration example rather than combining unrelated animation loops. Destroy scrolling and animation instances when the owning view is removed.

## Licensing and media costs

GSAP and its plugins are free under the current GSAP license, including commercial use; see [Webflow's announcement](https://webflow.com/updates/gsap-becomes-free) and [current product terms](https://webflow.com/legal/product-terms). It is not MIT, and the license contains restrictions for competing visual animation builders.

Motion, Lenis and Anime.js publish their licenses with their source. A runtime license does not grant rights to a purchased animation, font, photo or video used inside it.

## Check the finished interaction

- Keep navigation, headings and the main action accessible while media loads or a script fails.
- Provide a reduced-motion path; [MDN documents the preference](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).
- Prefer transform and opacity for routine transitions, and measure effects that change layout or perform expensive painting.
- Test a narrow screen and a low-powered device. A long pin or full-page video can work on a desktop and obstruct reading on a phone.
- Check the actual task: a technical performance score cannot tell whether the movement explains the product.

[Frontend design resources](../guides/cinematic-frontend-not-slop.md) · [Component libraries](landing-page-libraries.md) · [Tools index](README.md)
