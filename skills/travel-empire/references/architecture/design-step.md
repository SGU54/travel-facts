# Design step (Stage 5) — restyle the BUILT site into a distinct identity

**Design is the LAST stage, not the first.** It runs after the architecture, admin, content,
and publishing are all real and live. The structural engine (schema, admin, nav, queries) is
shared and invisible; the **visible design is built fresh for every site** — but it is applied
to the *actual rendered site*, not to mockups produced in a vacuum.

## Why design moved to the end (the bug it fixes)

Designing up front and handing the build a set of mockups did not work: the architecture build
shipped the template's default look and the approved mockups were ignored. Restyling the **real
built site** — its real components, real content, real responsive behavior — is the only way the
design that's approved is the design that ships. So: build on the neutral **minimalist template
look** through Stages 1–4, then restyle here against the running site.

## What "built first" means in practice

By the time this stage runs: the site is deployed, the admin works, categories and 60–80 real
articles are live on the minimalist template, the homepage/category/article pages all render real
data. You are now changing the LOOK only — tokens, type, component styling, motif — never the
structure, queries, or content. Verify each change against the live pages (homepage, a category,
a long article on mobile + desktop) so you're styling reality, not a guess.

## North star: a top-tier, memorable design — not a safe one

The goal of this stage is a site that looks like someone with taste *cared* — distinctive,
immersive, the kind of design that gets remembered and screenshotted. Competent-but-forgettable
is a failure here. Aim high: this is the one place in the pipeline where boldness is the job.

Clarity and boldness are NOT in tension — the reader must still get answers fast (legible body
type, obvious nav, strong hierarchy, fast load). But "clarity" is the floor, not the ceiling.
Do not let "keep it clear" talk you into bland. The best travel sites are both effortless to
read AND have a strong point of view. Deliver both; never trade the second away for the first.

## Design from a THESIS, not a palette (this is how the good ones happen)

The strongest sites in this empire came from a single committed **idea about the place** — a
feeling, a metaphor, a point of view — that everything then expresses. Not "Greek colors," but
a thesis. Example that worked (greeceforamericans, "Come Up For Air"): *Greece, for a nervous
first-timer, reads as a sequence of sea-crossings — you don't drive it, you surface from it; the
site is a descent and the relief of coming up for air.* From that one sentence flowed the whole
identity: a water-column palette (deep chrome → sea → aqua → salt reading surface) instead of the
postcard whitewash-blue cliché, a dark immersive chrome with a light reading surface, an animated
hero of rising bubbles and caustic light, a "waterline" break on the homepage, a mono "timetable"
type voice for ferry legs and prices.

The process that produces that:
1. **Find the thesis first.** Spend real thought on one sentence that captures a *feeling about
   this destination for this audience* — reject the obvious postcard read (whitewash-blue Greece,
   red-and-gold Spain) in favor of something truer and less expected. The thesis is the seed;
   everything else derives from it.
2. **Derive palette, type, motion, and layout FROM the thesis** — not from a swatch library. The
   palette should mean something (the water column, the desert at dusk, ink-on-paper restraint).
   Type should have a voice (a romantic display + a calm body + a utility/"timetable" mono is a
   strong, reusable shape). Motion and layout should embody the idea (a descent, a journey, a
   surfacing).
3. **Commit.** A half-applied bold idea reads as a mistake; a fully-committed one reads as
   intentional. Carry the thesis into the hero, the chrome, the section rhythm, the dividers,
   the empty states — everywhere.
4. Show the user the **direction with its thesis stated**, rendered on the real site, and refine.

## Dynamic / custom CSS is ENCOURAGED — don't stop at tokens

The token system is the floor for consistency, NOT a ceiling on ambition. Top-tier design here
routinely means hand-written, signature CSS beyond what tokens express:

- **Motion is the one bold thing.** A living, immersive hero is the single highest-leverage move.
  The Greece hero uses pure CSS/SVG: rising **bubbles** (`@keyframes` drift up with scale+opacity),
  drifting **caustic light** (animated radial gradients, `mix-blend-mode: screen`), a swaying
  god-ray **sun**, and a **waterline** transition between the airy index and the deep-water zone.
  All hand-authored in `globals.css` as opt-in `.cufa-*` classes. Build signature motion like this
  — it's what separates top-tier from template.
- **Custom gradients, blend modes, scoped component classes, SVG filters, clip-paths, layered
  backgrounds** — all fair game. Author them as named classes in `globals.css` (a stable
  interface; only the look is per-site), scoped so they don't leak onto reading pages.
- **You are NOT limited to the SITE_CONFIG token palette for these signature pieces.** Tokens keep
  the shared components coherent; the signature hero, dividers, and motifs can reach for whatever
  CSS the idea needs. (Earlier guidance said "tokens only, no per-page CSS" — that was too
  conservative and is explicitly relaxed for signature/motif work. Reading-surface and shared
  chrome still go through tokens for consistency and contrast; the *signature layer* is free.)

**The one guard on all this:** wrap every animation in the `prefers-reduced-motion` reset (the
template ships it), keep article-reading bodies calm and legible (motion belongs in chrome/hero,
not behind paragraphs), and don't let a heavy hero wreck mobile performance (CSS/SVG over images
or video; lazy where possible). Bold AND fast AND accessible — all three.

## MANDATORY: the screenshot self-critique loop (do this BEFORE showing the user)

The single biggest time-sink across builds was showing the user half-baked directions and
iterating through their feedback instead of Claude's own eyes. **Claude can render and SEE its
own output — use that every time, before the user ever looks.**

The loop, per direction:
1. Build the hero (+ a card row) on the real site or a faithful standalone preview.
2. Render it to PNG with headless Chromium (playwright/puppeteer) at desktop **and** phone width.
3. **Actually view the screenshot** and critique it honestly against this checklist:
   - Does it look like a templated AI default (centered hero, cream bg, serif headline, one
     terracotta accent)? If yes → reject, it's not distinctive enough.
   - Is the type doing real work (a confident display face, deliberate scale/tracking), or is it
     a safe Google-Font serif? 
   - Does the composition have a point of view, or is it a stock layout?
   - On the real photo (not a stand-in), does the hero hold up?
4. Rebuild from the critique. Repeat until it clears the bar.
5. ONLY THEN show the user — render-on-real-site, with the thesis stated.

Showing the user as a substitute for self-critique wastes their time and yours. The user is the
final taste check, not the first. Budget 3–5 internal render/critique cycles per direction before
the first reveal.

## Anti-patterns that have cost real iterations — avoid from the start

These are concrete failure modes from past builds. Each one was rejected by the user after wasted
rounds; treat them as hard "don't."

- **The AI-default look.** Cream/off-white background + a serif display (Fraunces, Cormorant,
  Playfair) + one terracotta/rust accent + centered hero = the generic "tasteful AI" template.
  It reads as un-designed. If the draft drifts here, stop and restart from the thesis. Prefer a
  **confident grotesk/sans display** (e.g. Archivo, a strong neo-grotesk) unless a serif is truly
  the thesis — and if serif, make it an intentional, unusual choice, not the default.
- **CSS-cartoon photo stand-ins shipped as the design.** Building flat CSS/SVG "scenes" (a
  cartoon mosque, a vector beach) as placeholder imagery and presenting that as the look. It reads
  cheap and fools no one. The design must be **photo-led**: real photography carries the warmth,
  and the design has to look premium *because of layout/type/restraint*, NOT because of a photo
  Claude can't see. Use CSS/SVG stand-ins ONLY as private scaffolding for Claude's own screenshot
  critique — never as a deliverable, and never let the design's quality depend on them.
- **Untranslated foreign-language hero text for an English audience.** A big "Hoş geldiniz" /
  "Καλώς orίσατε" hero on a site whose audience is American travelers is alienating, not
  evocative. Keep the primary headline in the reader's language; a small, translated accent word
  is the most that's safe.
- **Heavy metaphor/ornament when the brief is "crisp & trustworthy."** Rotating ethnic ornament,
  ornate borders, or a dense metaphor concept fights the goal. One ownable signature element
  (a line, a mark, a motion), used consistently, beats a pile of decorative motifs.
- **Fake / non-functional UI in the design.** Do not show buttons, search bars, pickers, or chips
  that don't do anything. Every interactive element must EITHER be wired to real behavior OR not
  appear. (See "Interactive elements must be real" below.)
- **Static numbers dressed as live data.** A hardcoded "$1 ≈ 32₺" rate or a fake "live" ticker
  reads as current and silently goes stale. Either compute it client-side (local time is genuinely
  live and free), or label it clearly as indicative, or omit it. Never imply freshness you can't
  back.

## Interactive elements must be real (no fake UI)

If the design includes an interactive affordance, it ships wired or not at all:
- **Search** → point it at the real `/search` route (`<form action="/search">`), not a dead input.
- **Quick-question chips** → real links into `/search?q=...` or the relevant article.
- **Itinerary picker** (the proven pattern) → a pure **client-side router**, NO AI/API: the user
  picks trip length × interests, and deterministic mapping sends them to REAL existing itinerary
  articles (+ a few "pair it with" guides). Verify every target slug exists before shipping so no
  link 404s. This adds real planning value at zero cost — make it the default "smart" feature
  rather than an AI call (the empire runs no paid APIs).

## Scrub leftover motifs from the previous site / template (do this when applying)

The token system reskins shared components automatically, but several components carry
**hardcoded, previous-site-specific styling** that tokens don't touch. Every build so far left at
least one of these behind. Audit and fix each when applying the design:

- **Section-head marker** (the little diamond/dot before headings): its COLOR is often hardcoded
  to the previous site's accent (e.g. a dark+gold "gilt" diamond from Greece). Re-derive it from
  THIS site's accent token.
- **Card style**: featured/article cards may carry the previous site's treatment (e.g. hard
  "brutalist" borders + offset box-shadow). Restyle to this site's card language.
- **Article hero shape**: a previous-site motif baked as a border-radius/clip (e.g. a 120px
  Roman-arch top from Greece). Replace with this site's hero treatment.
- **Hero text / eyebrow / dividers**: check none still encode the old site's words or shapes.
- **Logo mark**: ensure it carries this site's mark, variant-aware for light header vs dark footer.

Grep for the previous accent hex and for `rotate-45`, `box-shadow`, `border-radius:` in components
to find inherited styling. Rule: **every visible mark must derive from THIS site's tokens/thesis,
not be inherited.** Do a final pass listing each diamond/marker/card/hero and confirm its color and
shape come from this site.

## Drive the design from destination + audience

Beyond the thesis, ground the specifics:
- **Destination** — its light, materials, landscape, architecture (Morocco: clay, terracotta,
  zellige, warm sun; Japan: paper white, ink, indigo, restraint). Let the place suggest the
  palette — and push past the first cliché to a deeper read.
- **Audience** — what reads as trustworthy/native to them (a Russian-speaking audience, an
  American audience, a luxury vs budget traveler each expect a different register).
- **Differentiation** — it must NOT resemble the previous site. Different primary hue family,
  different type pairing, different motion idea, different layout rhythm. If it could be mistaken
  for the previous site, redo it.

Read the **`frontend-design`** skill for the styling constraints of this environment, and follow
it for component/CSS craft — but treat it as craft guidance, not a cap on ambition.

## Process: thesis → directions on the REAL site → commit

1. Land the **thesis** (one sentence; reject the obvious).
2. Derive 2-3 candidate **directions** from it (palette + type pairing + motion idea + mood),
   each with its thesis stated in a line.
3. Build them on the REAL site enough to judge — the **hero with its signature motion** + a card
   row is the honest test (a static mockup undersells a motion-led design, so prototype the motion).
   **Run the screenshot self-critique loop on each (render → view → critique → rebuild, desktop +
   phone) until it clears the bar BEFORE showing the user.** Use real or representative photography
   in the render, never CSS-cartoon stand-ins as the deliverable.
4. The user picks one (or blends).
5. Apply fully: chosen tokens into `SITE_CONFIG.brand` for the shared system, AND the signature
   `globals.css` classes for the hero/motifs/dividers. Commit the idea everywhere.
6. **Write `DESIGN-NOTES.md` at the repo root** capturing the thesis, the palette-with-meaning,
   the type voices, and the signature motion — *why* the design is what it is. This makes the
   design self-documenting so later edits build on the logic instead of guessing (it's what lets a
   future session polish or extend the look without dismantling it). Name the signature CSS classes
   stably (e.g. `.cufa-*`) and note them here as the component interface.

## Definition of done (Stage 5)

A committed, thesis-driven identity is live on the real site: shared system themed via
SITE_CONFIG tokens, a signature hero with hand-authored motion (reduced-motion-guarded), reading
surfaces calm and legible, mobile fast, no inherited resemblance to the previous site,
`DESIGN-NOTES.md` written, user approves. Then ship the standard feature set (5-features.md) and run the go-live checklist (4-publishing.md §9); terminal stage after launch is `stage: "live"`.

## Build the lead magnet here — VALIDATED, then packaged (design is after content)

The design step runs AFTER all batches are published, so the corpus is complete here.
The lead magnet (config + PDF) is built at this stage — but through TWO validation
gates, and the final repo is packaged only once BOTH are approved. Never hand over a
repo with an unvalidated PDF baked in.

**Gate 1 — site design.** Produce 2–3 design directions on the real site; user picks
the winner. (This is the normal design-step deliverable.)

**Gate 2 — the PDF.** After the site design is chosen, draft the config
(`<site>-leadmagnet.config.json`) using the APPROVED design's tokens in the `theme`
block, then present the PDF for validation in TWO separable parts:

- **Content picks** — the config (`schema_version: 2`) names each section's source
  `slug` + exact `heading` explicitly (2026-10-11: scoring was removed — see
  SKILL.md-CHANGES.md; a wrong automatic pick could silently cross sites). Run
  `leadmagnet-data.mjs CONFIG.json ... --suggest` first on an unfamiliar corpus to see
  candidate slugs/headings, then write the real selection into the config yourself and
  run it for real. This validates WHAT each section pulls. A wrong pick is a one-line
  config fix (change the named `slug`/`heading`) — independent of the look.
- **Design takes** — render 2–3 design variations of the SAME (correct) content, each as
  a REPRESENTATIVE SAMPLE (cover + one day page + the costs page — the three most
  design-distinct pages), so the user judges the look fast and side by side. Content is
  fixed (it's the best-scored answer); only the styling varies between takes.

The user approves the content picks AND picks a design take.

**Package (only after BOTH gates pass).** Render the FULL PDF in the chosen look,
commit `leadmagnet.json`, move the PDF to `apps/site/public/`, set
`SITE.leadMagnet.enabled:true` + `pdfUrl`. NOW hand over the complete repo — validated
design + validated PDF, both baked in.

So: **content live → design directions (gate 1) → config in approved theme → PDF picks +
design takes (gate 2) → package the whole repo.** Re-run the build any time content
changes later. (Emails capture to `common.subscribers` via `/api/subscribe`; the
`0009_subscribers.sql` migration + `SUPABASE_SERVICE_ROLE_KEY` env var are go-live
steps, not design.)

## Hard rules (craft guards — these protect quality, they do NOT cap ambition)

- **No inherited identity.** Never copy the previous site's palette/fonts/motion as a starting
  point. Every site starts from its own thesis + destination + audience.
- **Clarity is the floor, not the ceiling.** Reading must stay effortless — contrast, legible
  body type (~16px+), clear H2/H3 hierarchy, tap-friendly nav, calm reading surface. But this is
  the minimum bar to clear, not the goal; clear the bar AND be bold. Never cite "clarity" as a
  reason to ship bland.
- **Signature layer is free; shared/reading layer goes through tokens.** The hero, motifs,
  dividers, and motion can use hand-written `globals.css` (custom gradients, blend modes,
  keyframes, SVG, clip-paths) beyond the token palette — that's where top-tier lives. The SHARED
  components and the article reading surface still take color from the token system, so contrast
  and consistency hold across the site. Don't hardcode one-off colors into shared components; DO
  author rich scoped classes for the signature pieces.
- **All motion respects `prefers-reduced-motion`.** Wrap every animation in the reset (template
  ships it). Motion lives in chrome/hero, never behind article paragraphs.
- **Mobile-first AND performant.** Most travel traffic is mobile; judge at phone width first and
  keep a heavy hero cheap (CSS/SVG over images/video, lazy where possible). Bold must not mean slow.
- **Tailwind purges dynamic class strings.** A class built at runtime (`text-[color:${x}]`, or a
  class chosen by a variable) gets purged and renders colorless. For anything that changes by
  variant/state, use INLINE STYLE with CSS vars, not interpolated Tailwind classes. (Site #2: the
  footer logo + tagline vanished — dark ink on the dark footer — until switched to variant-aware
  inline style.)
- **Shared components must be variant-aware for color.** Logo, buttons, anything used in BOTH the
  light header and the dark footer needs its color from the variant (e.g.
  `isFooter ? var(--bone) : var(--ink)`), since the background differs.
- **Confirm token NAMES before using them** — read tailwind.config.ts. Don't assume; the accent
  might be `brass`/`brass-soft`, not `tomato`. A wrong token name silently fails.
- **Mock brand-trim changes BEFORE editing.** Recoloring signature trim to flag/accent colors:
  show a rendered mock and get explicit sign-off first. Saturated flag colors as repeated UI trim
  usually clash with a cool palette — offer harmonized or single-color options. (Site #2: built a
  Catalan red+gold ruban, user rejected it, full revert — a mock would have saved the round trip.)
- **Don't over-ask about tokens mid-flow.** When the user says "go big / don't hold back / don't
  worry about tokens," that's standing permission to author the signature CSS without pausing to
  confirm each color against the palette. Commit the vision; show the result.
- **Self-critique with screenshots before every reveal.** Render the hero at desktop + phone, view
  it, and reject AI-default/templated results yourself before the user sees them. The user is the
  final taste check, not the first pass.
- **Photo-led, never CSS-cartoon as deliverable.** The design must look premium from layout, type,
  and restraint — not depend on a stock photo Claude can't see. CSS/SVG scenes are private
  scaffolding for self-critique only.
- **No fake UI.** Every interactive element ships wired (search → `/search`, chips → real queries,
  itinerary picker → client-side routing to real articles) or is not shown.
- **No static data dressed as live.** Compute client-side, label as indicative, or omit. Never
  imply freshness (rates, "live" tickers) you can't back.
- **Scrub inherited motifs when applying.** Section-head marker color, card style, article-hero
  shape, logo mark — re-derive each from THIS site's tokens. Grep for the previous site's accent
  hex and for `rotate-45` / `box-shadow` / `border-radius:` in components to catch leftovers.
- **Verify fonts actually LOAD before trusting a screenshot.** A shot fired before
  `document.fonts.ready` renders the fallback face and lies to you — wait for fonts (and
  network-idle) before capturing. And only pick display faces that exist on Google Fonts: an
  unhosted choice silently falls back (e.g. Clash Grotesk is NOT on Google Fonts; Anton,
  Archivo Expanded, Bricolage Grotesque are).
- **Photo-led, but the brand MUST survive photo-less.** Identity cannot depend on a hero
  photograph — articles ship before their photos and some heroes have none. Author the signature
  background (`.motif-bg`) so a photo-less hero still reads as the brand; when a photo IS set it's
  a substrate under an authored wash, never the identity itself. (Thailand's homepage renders on
  the neon `.motif-bg` when no hero image is set, and looks intentional.)
- **Find the SPECIFIC read, reject the generic one.** "Calm/editorial/tropical" could be any
  country. Push to what's unmistakably THIS place before committing. (Thailand landed on vivid
  street life — Bangkok-taxi magenta + tuk-tuk orange + market colors — not the temple-at-sunset
  postcard, and not generic green-jungle.)
- **Tokens and signature classes are NAME contracts.** Restyle the values and the look; never
  rename `green`/`green-deep`/`brass`/`brass-soft`/`saffron`/`bone`/`ink`/`line` or `.motif-bg` /
  `.arch` / `.cosmati-inlay` / `.cosmati-divider`. Keep the shipped `prefers-reduced-motion` reset.

### Two live bugs to check after applying a theme (both cost real debugging on Thailand)
- **`.arch` colliding with the logo.** `.arch` carries `border-radius` + a border; if the header
  logo container reuses `.arch` (or inherits it), the logo renders trapped in a stray outlined
  rectangle. Check the logo after any `.arch` restyle.
- **A poster display font overflowing a fixed-width lockup.** Condensed/uppercase display faces
  (Anton) are much taller per glyph; the brand name set into a small fixed logo box wraps to
  multiple lines and clips ("Thailand" cut off at the top). Give the logo lockup room, or set the
  logo type explicitly instead of inheriting the display face at full size.
