# How to Build Beautiful Websites Without AI Slop

A curated guide to frontend libraries, animation tools, design inspiration and agent skills for distinctive landing pages, portfolios and product websites. Includes Motion (Framer Motion), GSAP, 21st.dev, React Bits, scroll-craft and scroll-world, with a reason to choose each.

Updated 16 October 2026. Links point to official sites, documentation or author repositories. Paid editors, generated assets and component licenses are separate costs; check the linked terms for your use.

## Start with the page you need

An AI-generated website looks generic when its layout, images and claims could belong to any product. A font, gradient or component library is not the cause by itself. Start with the product's actual screenshots, photography, explanation and next action, then choose tools that support them.

| What you are building | A useful starting point | What deserves the design work |
| --- | --- | --- |
| Editorial site, portfolio or documentation | [Astro](https://docs.astro.build/) and CSS; add small interactive islands where needed | Typography, image selection, reading order and navigation |
| Marketing site attached to a React product | [Next.js](https://nextjs.org/docs), a headless UI foundation and [Motion](https://motion.dev/docs/react) for component transitions | Real product states, responsive layouts and shared interactions |
| Scroll-driven product story | [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/); optionally [Lenis](https://github.com/darkroomengineering/lenis) | A useful sequence, mobile composition and an accessible static version |
| Interactive 3D product demonstration | [Three.js](https://threejs.org/docs/) or [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/getting-started/introduction) | Lighting, camera, model size and a lightweight fallback |
| Designer-managed marketing site | [Framer](https://www.framer.com/) or [Webflow](https://webflow.com/) | A layout and CMS workflow the site owner can maintain |
| One immersive video-scroll experience | [scroll-craft](https://github.com/nateherkai/scroll-craft) or [scroll-world](https://github.com/oso95/scroll-world) | Original scenes, continuous transitions and media loading on phones |

Choose one route for the page. Adding every library below usually creates more integration work than visual quality.

## Browse this guide

- [Web design inspiration and live references](#web-design-inspiration-and-live-references)
- [Frameworks and visual website builders](#frameworks-and-visual-website-builders)
- [Component libraries and registries](#component-libraries-and-registries)
- [Motion and scroll animation](#motion-and-scroll-animation)
- [3D and interactive illustration](#3d-and-interactive-illustration)
- [Typography and icons](#typography-and-icons)
- [Frontend skills for Claude Code and Codex](#frontend-skills-for-claude-code-and-codex)
- [A practical workflow for a distinctive landing page](#a-practical-workflow-for-a-distinctive-landing-page)
- [Questions about AI slop and frontend libraries](#questions-about-ai-slop-and-frontend-libraries)

## Web design inspiration and live references

Use galleries to study a particular decision: navigation, type scale, product photography, transitions or mobile layout. Open the live site as well as the screenshot. A screenshot cannot show whether a menu works or whether a scroll sequence becomes tedious.

| Resource | Use it for |
| --- | --- |
| [Awwwards](https://www.awwwards.com/) | Awarded sites and collections organized by industry and technology; compare how different studios handle the same kind of business. |
| [Godly](https://godly.website/) | Website references with an emphasis on visual treatment and interaction; useful when assembling a short direction board. |
| [Landing Love](https://www.landing.love/) | Landing-page recordings; useful for seeing motion and section order rather than judging only a still hero. |
| [Land-book](https://land-book.com/) | Website and page references across industries; useful for comparing several approaches to a brief. |
| [Lapa Ninja](https://www.lapa.ninja/) | Landing-page examples grouped by category; useful for pricing, product and service page research. |
| [One Page Love](https://onepagelove.com/) | One-page sites and templates; useful when the whole visitor journey needs to fit one page. |
| [Codrops](https://tympanus.net/codrops/) | Creative coding tutorials, demos and implementation breakdowns for animation, typography and WebGL. Read each demo's dependencies before adopting it. |
| [Typewolf](https://www.typewolf.com/) | Typography in real websites, font combinations and type references; useful for selecting a type direction before choosing components. |

Save references with a note such as “the product image explains the offer before the headline” or “this menu stays usable on a small screen.” Copying a whole site's visual identity is not a design brief.

## Frameworks and visual website builders

These determine rendering and editing workflows. They do not supply a visual identity.

| Resource | Choose it when | Consider before choosing |
| --- | --- | --- |
| [Astro](https://docs.astro.build/) · [source](https://github.com/withastro/astro) | Most of the site is content and only some regions need JavaScript. | Plan which components need hydration; a mostly interactive application may suit another framework. |
| [Next.js](https://nextjs.org/docs) · [source](https://github.com/vercel/next.js) | A React marketing site needs to share code or server features with the product. | Choose static rendering, server rendering and client components deliberately; a brochure page does not need every app feature. |
| [SvelteKit](https://svelte.dev/docs/kit/introduction) | You want Svelte components, routing and a choice of rendering/deployment approaches. | Check the adapter and hosting environment you will use. |
| [Nuxt](https://nuxt.com/) | Your team or product already uses Vue and needs a site framework. | Decide how each route is rendered and where interactive code is necessary. |
| [Framer](https://www.framer.com/) | Designers need visual control over a marketing site and its publishing workflow. | Hosted publishing, CMS, marketplace assets and plan limits have their own terms. Framer the site builder is distinct from Motion the animation library. |
| [Webflow](https://webflow.com/) | A site owner needs visual layout tools, CMS content and hosted publishing. | Check the current plan, CMS requirements and any export or hosting constraints before committing the project. |

For app, mobile and backend choices, see [frameworks for building](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/frameworks-for-building.md).

## Component libraries and registries

Start with accessible behavior for menus, dialogs and forms. Then use a registry or block library for a particular section. A component that looks good in its demo still needs your content, error states and responsive checks.

| Resource | What you get | Where it fits |
| --- | --- | --- |
| [Radix Primitives](https://www.radix-ui.com/primitives/docs) · [source](https://github.com/radix-ui/primitives) | Unstyled React primitives for interactive UI. | Custom-styled dialogs, menus and controls where behavior matters more than a preset appearance. |
| [Base UI](https://base-ui.com/react/overview/about) · [source](https://github.com/mui/base-ui) | Unstyled React components with composable APIs. | An alternative foundation when you want to own styling and composition. |
| [shadcn/ui](https://ui.shadcn.com/docs) · [source](https://github.com/shadcn-ui/ui) | Component source you bring into your project, plus a registry format. | Owning and adapting your UI code. Inspect third-party registry code separately from the core project. |
| [21st.dev](https://21st.dev/) · [agent integration](https://21st.dev/mcp) | A component catalog and an MCP workflow for coding agents. | Finding a specific React/shadcn component with a preview. Catalog access, installs and AI generation have different limits; check current pricing and the selected component's license. |
| [React Bits](https://www.reactbits.dev/) · [source](https://github.com/DavidHDev/react-bits) | Animated text, backgrounds and interactive visual components. | One effect that serves the page. Its MIT + Commons Clause terms differ from plain MIT. |
| [Magic UI](https://magicui.design/docs) · [source](https://github.com/magicuidesign/magicui) | Animated React/Tailwind components and visual patterns. | An intentional accent or interaction; several unchanged demos together can make the page feel borrowed. |
| [Aceternity UI](https://ui.aceternity.com/) | React effects, components and marketing blocks. | A section or interaction that matches the direction. Free components and paid blocks/templates have different access and terms. |
| [Motion Primitives](https://motion-primitives.com/) · [source](https://github.com/ibelick/motion-primitives) | Small animated components built with Motion. | Focused text, disclosure and transition patterns whose timing you can tune. |
| [Tailark](https://tailark.com/docs) | Marketing blocks and pages with registry installation. | A starting structure for marketing content; inspect the selected kit because OSS and paid content are distinct. |
| [HyperUI](https://hyperui.dev/) · [source](https://github.com/markmead/hyperui) | Copyable Tailwind markup for marketing, commerce and application UI. | Simple sections you can reshape without adopting a component runtime. |
| [Origin UI](https://originui.com/) · [source](https://github.com/shadcn/originui) | React/Tailwind components following shadcn conventions. | Form and application patterns; a useful addition when the landing page includes an interactive product surface. |
| [Park UI](https://park-ui.com/docs/introduction) · [source](https://github.com/chakra-ui/park-ui) | Styled component source built on Ark UI and Panda CSS. | A coherent starting system when you prefer its styling approach. |
| [Tailwind Plus](https://tailwindcss.com/plus) | Commercial UI blocks and templates from the Tailwind team. | Conventional sections that save implementation time; review the commercial license before using or redistributing them. |

See [landing-page component libraries](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/landing-page-libraries.md) for a shorter comparison by task.

## Motion and scroll animation

Choose the smallest tool that expresses the interaction. A static page can be distinctive. Animation earns its cost when it explains a transition, responds to input or helps someone follow a sequence.

| Resource | Use it for | Main tradeoff |
| --- | --- | --- |
| [CSS scroll-driven animations](https://developer.chrome.com/docs/css-ui/scroll-driven-animations) · [examples](https://scroll-driven-animations.style/) | Reading progress, simple view/scroll timelines and progressive enhancement. | Check target-browser support and keep the non-animated page usable. |
| [Motion, formerly Framer Motion](https://motion.dev/docs/react) · [source](https://github.com/motiondivision/motion) | React layout changes, enter/exit transitions, gestures and scroll-linked components. | Use the React API where component state drives movement; simple CSS transitions need no library. |
| [GSAP and ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · [examples](https://gsap.com/demos/) | Timelines, pinned product stories and several elements synchronized to scroll. | Own animation cleanup and responsive behavior. GSAP and its plugins are free under the current license, which is not an unrestricted MIT license. See [Webflow's announcement](https://webflow.com/updates/gsap-becomes-free). |
| [Lenis](https://github.com/darkroomengineering/lenis) | Optional smooth scrolling and integration with scroll animation. | Changes scrolling behavior; test keyboard input, nested scrollers, reduced motion and low-powered devices. Native scrolling is a valid default. |
| [Anime.js](https://animejs.com/documentation/) · [source](https://github.com/juliangarnier/anime) | Timelines and animation of DOM, SVG and JavaScript values. | Check examples against the installed major version and implement reduced-motion behavior for your effects. |
| [Rive](https://rive.app/docs/runtimes/web) | Interactive vector illustrations with state machines and app-controlled inputs. | The runtime, editor plan and animation asset have separate licensing and performance considerations. |
| [Lottie Web](https://github.com/airbnb/lottie-web) · [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | Playing supplied motion assets and exported vector animations. | Test the actual asset in the chosen player; export support and composition complexity affect fidelity and startup cost. |

For a direct GSAP vs Motion comparison and a complete React example, use the [frontend motion guide](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/frontend-motion.md).

## 3D and interactive illustration

Use real 3D when the visitor needs to inspect or manipulate an object. For a pre-rendered camera journey, video scrubbing can be a different implementation choice; it does not make the scene interactive 3D.

| Resource | Use it for | Plan for |
| --- | --- | --- |
| [Three.js](https://threejs.org/docs/) · [examples](https://threejs.org/examples/) | Custom 3D scenes, model viewers and rendering experiments. | Model compression, texture sizes, lighting and a device-appropriate rendering budget. |
| [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/getting-started/introduction) · [source](https://github.com/pmndrs/react-three-fiber) | Three.js scenes expressed as React components. | Three.js knowledge and a version compatible with your React application. |
| [Drei](https://drei.docs.pmnd.rs/) · [source](https://github.com/pmndrs/drei) | Cameras, controls, loaders and other helpers for React Three Fiber. | The dependencies and rendering behavior of the helpers you select. |
| [Spline](https://spline.design/) · [web export docs](https://docs.spline.design/exporting-your-scene/web/exporting-as-code) | Visually authored interactive scenes embedded in a website. | Editor/export terms, scene weight and whether a static image is enough on mobile. |

For an immersive scene chain generated by an agent, see scroll-world below. Keep the headline, navigation and primary action in HTML so they remain available while media loads.

## Typography and icons

A display font is only one decision. Check the actual headline at phone width, the body text's reading size, language coverage and the font license. Use one icon family for ordinary controls so stroke weights and proportions stay consistent.

| Resource | What to use it for |
| --- | --- |
| [Google Fonts](https://fonts.google.com/) · [Fonts Knowledge](https://fonts.google.com/knowledge) | Font discovery and practical reading about type, spacing and choosing a family. |
| [Fontshare](https://www.fontshare.com/) | Type families and pairing references; check the license supplied with the selected font. |
| [Typewolf](https://www.typewolf.com/) | Seeing typography in real layouts before committing to a font pairing. |
| [Lucide](https://lucide.dev/) | A consistent outline icon family and framework packages for controls. |
| [Phosphor](https://phosphoricons.com/) | An icon family with several weights when the visual system needs more weight choices. |
| [Iconify](https://iconify.design/) | Searching and integrating multiple icon collections; individual sets have their own licenses. |
| [Simple Icons](https://simpleicons.org/) | Brand marks for integrations and a tool stack. A brand icon's availability does not replace its trademark guidelines. |

## Frontend skills for Claude Code and Codex

Skills are instructions and supporting files an agent reads. They are different from component packages and animation runtimes. Read a skill's requirements and inspect its scripts before giving it access to a project.

| Skill | Author repository | What it adds |
| --- | --- | --- |
| frontend-design | [Anthropic's skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | A workflow for choosing a visual direction and implementing an interface with attention to typography, layout and detail. |
| scroll-craft | [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) | A workflow and supporting tools for scroll-driven websites, references, responsive composition and visual verification. Uses supplied assets or optional generated media; media generation can cost extra. |
| scroll-world | [oso95/scroll-world](https://github.com/oso95/scroll-world) | A continuous camera journey assembled from scene images and video clips, then scrubbed by scroll. Requires media tooling and may require paid generation services. |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design references and guidance for interface styles, typography, palettes and implementation choices. Use the references to make a choice rather than generating a new palette for every section. |

Follow each repository's installation instructions for your agent. In scroll-craft, keep the skill's references, scripts and engine together. In scroll-world, plan asset generation and mobile media before starting a long scene chain. Neither skill guarantees a usable result without reviewing the rendered page.

## A practical workflow for a distinctive landing page

1. Write the offer in plain words. Decide what a visitor needs to understand and which action the page should make possible. Gather actual product screens, photos or examples that support the claim.
2. Pick a few references for different decisions. Record what you are borrowing from each: type hierarchy, image treatment, information order or an interaction. Use licensed assets you can publish.
3. Choose a framework and a UI foundation. Bring in one component or animation at a time. Give an agent exact reference URLs and ask it to explain why each dependency is needed.
4. Build a static first screen with the real headline, image and action. Check phone width before expanding the page. A font ban or a compulsory black-and-green palette is not a substitute for this check.
5. Add movement where it helps explain something. Keep body content visible when scripts fail, provide reduced-motion behavior and make the mobile version work without hover.
6. Test the rendered site. Use keyboard navigation, narrow viewports, slow-network loading and real links/forms. Review one full-page screenshot as well as the actual interaction.

Useful primary references: [web.dev Learn Accessibility](https://web.dev/learn/accessibility), [MDN reduced-motion media query](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion), [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) and [Playwright](https://playwright.dev/docs/intro). Lighthouse is a technical check; a score does not judge composition or whether the offer is understandable.

### A brief you can give a coding agent

```text
Build a website for this product and audience: [supply the facts].
The visitor's next action is: [name the action].
Use these real assets: [attach or link the files].
Study these reference URLs: [link them and name the useful detail in each].

Read this guide and choose only the resources this page needs:
https://yerdaulet-damir.github.io/awesome-solo-ai/frontend-design/

Before implementation, propose the information order, type direction,
mobile composition and any interaction that explains the product.
Use real copy. Identify missing assets or claims rather than inventing them.
Implement the page, then inspect it at mobile and desktop widths.
Check keyboard use, reduced motion, loading behavior, links and forms.
```

This is a brief to fill in, not a ready-made identity for every product. For application structure, continue with [build your own AI SaaS](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/build/your-own-ai-saas.md); for maintainable code, see [AI coding quality](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/guides/kill-ai-slop-code.md).

## Questions about AI slop and frontend libraries

### Which libraries help make an AI-generated website less generic?

Use galleries to choose a direction, a UI foundation such as Radix, Base UI or shadcn/ui for behavior, and a focused resource such as 21st.dev, React Bits or Motion Primitives for a particular interaction. The distinguishing work is adapting the layout, imagery, copy and motion to the actual product. A registry cannot make that choice for you.

### Should I use GSAP or Framer Motion?

Motion, formerly Framer Motion, is convenient for React component state, gestures, layout and enter/exit animation. GSAP is useful for coordinated timelines and scroll sequences. They overlap; use the one that matches the interaction and your project. A page does not need both by default.

### Is GSAP free, including ScrollTrigger and SplitText?

Webflow's [GSAP announcement](https://webflow.com/updates/gsap-becomes-free) makes GSAP and its plugins free, including commercial use. The current [product terms](https://webflow.com/legal/product-terms) still govern use; do not describe it as MIT or repeat the old blanket claim that SplitText requires a Club GSAP subscription.

### Is a scroll-world site the same as a Three.js website?

No. The scroll-world workflow assembles a rendered video chain and scrubs playback as the visitor scrolls. Three.js renders a scene in the browser and can respond to camera or object input. Choose between them based on whether you need a directed story or interactive inspection, then test the loading and device costs.

### Do these resources make a site discoverable by Google or LLMs?

They help implementation, not guaranteed discovery. Put the useful text and links in crawlable HTML, use descriptive titles and headings, expose the page through navigation and a sitemap, and keep the content available without animation. A machine-readable index can help agents navigate, but it does not guarantee indexing, ranking or citation.

## Related guides

- [Frontend motion: GSAP, Motion, Lenis and native CSS](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/frontend-motion.md)
- [Landing-page component libraries and registries](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/landing-page-libraries.md)
- [Frameworks for building a product](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/tools/frameworks-for-building.md)
- [Frontend-design skill](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/skills/frontend-design.md)
- [AI coding quality](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/guides/kill-ai-slop-code.md)
- [All guides](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/guides/README.md) · [Awesome Solo AI](https://github.com/yerdaulet-damir/awesome-solo-ai/blob/main/README.md)
