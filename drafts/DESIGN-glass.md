# Student dashboard · "Liquid Glass, crisp lines" — design spec

Status: **design template** (`drafts/home-glass/`), not on student sites. Source: `tools/home_glass.py` (theme) + `tools/build_student_home.py --theme=glass`.
Research done 27.11.2026. Rules of the course still apply: light themes only, pastel accent per level, no level/brand on student pages, signature "Valentyna Hordiienko · Middle Learning Architect", buttons ≥ 44 px on phones.

---

## 1. What the research says

### What a student dashboard must do (learning-analytics research)
- **One clear next step.** Dashboards help when feedback is *actionable*; many show data but no "what now" (Afzaal et al. 2023; MIT Meta-LAD). → hero starts with **Your next step** = the first assignment not sent yet, one dark **Start** button.
- **Support self-regulation: plan → monitor → reflect** (EDUCAUSE MyLA; Meta-LAD). → *Plan*: next lesson + this week strip + My plan. *Monitor*: Assignments, skills, vocabulary. *Reflect*: teacher's note, speaking comment, grammar by topic.
- **Process and skills, not "you are good/bad".** Feedback about the process supports deeper learning; feedback about the self is least effective (Jivet et al., LAK 2021). → skill cards say "from 3 review tasks", "learning now", never rank the student.
- **No social comparison** (Meta-LAD design dimensions). → no leaderboards, no class averages.
- **Show learning, not just activity.** Streak-only apps make people "better at the app" (Duolingo case studies; Duolingo Score 2025). → we show skills and speaking pace; a streak may be added later only with forgiveness (freeze/repair, as Speak 2025).
- **Key info on the home screen without digging** (Fluently relaunch, Babbel progress tab). → next step, next lesson, lessons left, assignments are above the fold.

### What "Liquid Glass" is (Apple, WWDC25) and how to use it on the web
- Glass is a **functional layer for navigation and controls that floats above content** and never competes with it; content sits on standard (more opaque) material (WWDC25 219 "Meet Liquid Glass"; HIG Materials).
- **Concentric shapes**: nested radii share a centre — inner radius = outer radius − padding; controls are **capsules** (WWDC25 356).
- Edges catch light: **brightest at the top**; tint only enough to stay legible.
- On the web CSS can only approximate it: `backdrop-filter` blur/saturate + translucent fill + 1px gradient edge; real refraction needs an SVG displacement filter or WebGL and is Chromium-only (LogRocket, ekino, Aave "Building Glass for the Web") → **we don't use refraction** (cost, Safari, readability).
- Readability is the main risk of glass (NN/g "Glassmorphism"): text over busy, multi-coloured backgrounds; more blur needed over busy backgrounds; Apple lets users reduce transparency. Trend articles 2026: glass for **navigation, not the data layer**; bento grids only when block sizes carry meaning.

---

## 2. Principles

1. **Two materials.**
   - **Glass** (`--glass` = white 46 %, blur 30 px, saturate 180 %, gradient 1 px edge): sidebar, hero picture frame, floating badges, teacher bar, banners.
   - **Frost** (`--frost` = white 86 %, blur 24 px, 1 px hairline): every card with text or numbers.
2. **Crisp lines.** 1 px hairlines `rgba(17,19,42,.08)` (dividers `.05`), top inner highlight `inset 0 1px 0 #fff`, tight shadows (`0 1px 1px` + one soft drop). No glow, no blurred blobs under text.
3. **Quiet background.** Two very light radial tints (lavender + level tint) on `#f4f4f9`. Nothing moves behind text.
4. **Concentric radii, 8 px grid.** Sidebar 28 → items 16 (padding 12); hero 32; frame 32 → picture 16; cards 24; inner blocks 16/12; controls 999 (capsule). Spacing 8 / 16 / 24 / 32.
5. **One accent + ink.** Ink `#11132a` for text and the primary button; lilac `#6d5ce8` for labels, bars, rubric dots, chart; the level colour only as a background tint and on the avatar. Status colours (green/amber/red) only for status.
6. **Hierarchy by type, not by colour:** eyebrow 11 px uppercase lilac → H1 44 px −1.6 tracking → lesson 22 px lilac → body 15 px. Numbers use tabular figures.
7. **One primary action per view** (dark capsule with ↗). Everything else is a light capsule.

## 3. Tokens

| Token | Value |
|---|---|
| `--ink / --ink2 / --mut` | `#11132a` / `#454a66` / `#6c7190` |
| `--lil / --lil2` | `#6d5ce8` / `#efecff` |
| `--hair / --hair2` | `rgba(17,19,42,.08)` / `.05` |
| `--frost / --glass` | `rgba(255,255,255,.86)` / `.46` |
| `--edge` | `linear-gradient(180deg, white .98 → white .35 at 38% → ink .10)` (brightest at the top) |
| radii | 32 hero · 28 sidebar · 24 card · 16 inner · 12 small · 999 capsule |
| shadows | `--sh`: `0 1px 1px rgba(17,19,42,.04), 0 6px 20px -6px rgba(17,19,42,.08)`; `--sh2` (floating glass): `… 0 18px 40px -16px rgba(60,50,150,.22)` |

## 4. Page structure (top → bottom)

1. **Hero** (frost): greeting eyebrow · name · current lesson · **Your next step** (first unsent assignment, *Start*) · lesson pages as capsules · **This week** strip (Mon–Sun, lesson days outlined, today in lilac) + next lesson time · teacher's note. Right: business-English illustration in a glass frame with a specular sheen; floating badges *lessons left* and *speaking pace* (sparkline).
2. **Stats** (3): Assignments to do · Lessons left (private students only) · Lessons done. (Next lesson lives in the hero.)
3. **Assignments**: only homework Vale approved (`student_assignments`); title, due/given, overdue red, Sent/To do, Open/Review.
4. **My plan** (THIS WEEK): next 4 lessons, goal with days left, stages.
5. **My progress** (YOUR GROWTH): 4 skill cards (review-only, smoothed, "learning now", "needs review" after 28 days) · Speaking (WPM line, rubric dots, teacher comment) · My vocabulary (know / learning / not started → trainer) · Grammar by topic.
6. **My course** (ALL UNITS): units accordion.
7. Teacher mode (unchanged logic; dark glass bar).

## 5. Accessibility (must stay true)
- Text only on frost (≥ 86 % white) → body text contrast ≥ 4.5:1; never put text directly on glass over a busy picture.
- `prefers-reduced-transparency` → all glass/frost become solid white; `prefers-contrast: more` → hairlines darker.
- Focus ring 2 px lilac; capsules ≥ 44 px; keyboard: units are buttons with `aria-expanded`; skip link; `aria-current` in the menu.
- Test at 375 px with network off (`page.route(/^https?:/, r => r.abort())`).

## 6. Not done yet / ideas
- Streak with forgiveness (freeze/repair) — only if Vale wants it; must count real practice, not clicks.
- "Words due today" from the trainer (spaced repetition) as a second next step.
- Dark mode is **not** planned (course rule: light themes only).

## Sources
- Apple: [HIG Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [WWDC25 219 Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/), [WWDC25 356 Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356/), [Apple newsroom, June 2025](https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/)
- Glass on the web: [LogRocket](https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/), [ekino — Liquid glass in CSS and SVG](https://medium.com/ekino-france/liquid-glass-in-css-and-svg-839985fcb88d), [Aave — Building Glass for the Web](https://aave.com/design/building-glass-for-the-web), [DEV — 6 ways](https://dev.to/devyatov/liquid-glass-on-the-web-6-ways-to-build-it-with-css-and-svg-3m07)
- Readability: [NN/g — Glassmorphism](https://www.nngroup.com/articles/glassmorphism/), [Axess Lab — Glassmorphism meets accessibility](https://axesslab.com/?p=5111)
- Dashboards & trends: [DEV — SaaS dashboard trends 2026](https://dev.to/thekitbase/saas-dashboard-design-trends-in-2026-with-examples-121m), [Muzli — dashboard examples 2026](https://www.muz.li/blog/best-dashboard-design-examples-inspirations-for-2026)
- Learning dashboards: [EDUCAUSE — Show students their data (MyLA)](https://er.educause.edu/articles/2021/7/show-students-their-data-using-dashboards-to-support-self-regulated-learning), [MIT Meta-LAD](https://omniedulab.mit.edu/meta-lad/), [Jivet et al., TU Delft](https://repository.tudelft.nl/file/File_02bfdf48-a844-41ca-9159-e500e7b4db6c), [Afzaal et al. 2023](https://doi.org/10.1007/s10758-023-09650-0)
- Language apps: [Duolingo product highlights](https://blog.duolingo.com/product-highlights/), [Speak winter 2025](https://www.speak.com/blog/winter-2025), [Fluently home redesign](https://torbenziegler.github.io/Fluently/blog/why-fluently-home-is-now-built-for-momentum), [Babbel new interface](https://support.babbel.com/hc/en-gb/articles/25075048448274--New-app-interface)
