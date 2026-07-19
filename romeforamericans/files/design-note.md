# Design note — the page model and the layout-architect layer

## Part 1 · The rendering defect, and the architecture that replaced it

**Diagnosis.** The bug was structural, not a tuning miss: margins and furniture were a
property of the *chapter* (a runhead div as each chapter's first child, top padding on
the flow), while pagination is a property of the *page*. Chromium confirmed every escape
route closed: header/footer templates clip their backgrounds (white bands on cream),
bare `@page` margins are unpainted, `position:fixed` prints once. Anything that decorates
the flow will only ever decorate the first page of each fragment.

**The fix — real pages before printing.** Your suspicion was right: the flow is now
sliced into actual fixed-size page divs by a pagination engine (Paged.js, vendored in
the skill) before Chromium prints. Each sheet is a DOM element, so:

- the **paper paints edge-to-edge by construction** — there is no margin band outside
  the painted box for Chromium to leave white;
- the **92/82/72/82 column is a real `@page` margin inside the painted sheet**, on every
  page identically;
- **runhead + folio are `@page` margin boxes** — ordinary DOM, on every page, with the
  running head fed by a `string-set` from each chapter (so continuations carry the
  current chapter, "DECISION 04 · ANCIENT ROME"), suppressed on opener pages by a
  renderer handler (the opener announces itself);
- the **cover and the annex are named pages** (`page: cover` full-bleed unfurnished;
  `page: annex` same bands, its own clearance) — exceptions the CSS can name;
- the **TOC's page numbers are now real**: rows link to section ids and
  `target-counter` resolves the printed folio at layout time. The hardcoded (wrong)
  numbers are gone.

Two paginator constraints surfaced and are now doctrine: **no base64 megabytes** (data-
URI fonts stall the CSS parse; data-URI photos silently truncated the book at p37 of 48
— fonts and images go by file URL, pre-decoded before pagination), and **one selector
per named string** (two `string-set` sources shadow each other → stale runheads).

**Proof.** `proof-pages.pdf` opens with the *old* continuation page (text 2–3px from the
trim, no furniture), then the new render: cover, TOC, essay opener, decision opener +
its continuation (full furniture, correct margins), a plain continuation, a closing-
plate page, the Field Sheet. The new gate `audit-furniture.py` checks every page for
paint-to-trim, folio, runhead, and column compliance — it passes the new build clean and
fails the old PDF on nearly every page. All eight `audit-book.py` gates are green
(median fill 69%, consistency span 58, zero stubs), and DOM page count is asserted equal
to PDF page count on every render.

## Part 2 · The layout-architect layer

The new authority is **`references/layout-architect.md`** — read before Stage C and
Stage F, and explicitly authoritative over page-spec/layout/design-system where they
conflict. It doesn't add a sixth rules file; it states the point of view the rules
serve, and the other files were reconciled underneath it:

**The governing idea:** every sheet is the same instrument playing different bars —
one grid, one baseline, one furniture system, one spacing scale, with deliberate variety
*on top of* that constancy (full-bleed cover, closing-image pages, dense ledgers, airy
tails). The test is the overlay: any two body pages must coincide in margins, furniture,
and baseline.

**The grid it imposes.** One vertical unit — 22.5px (body 13.4/22.5). The old build ran
the flow at 1.72 leading against a documented 1.68: two books interleaved; reconciling
them recovered ~a line per page. All vertical space now comes from one scale
(6 · 11 · 17 · 22.5 · 34 · 45 · 68) with one asymmetry that makes pages parse: ≥ one
line between blocks, ≤ ¾-line within them. One type ramp (~×1.27), three faces with
fixed jobs: display carries statements, body carries argument, mono carries apparatus.

**Composition judgment, made mechanical where it can be.** Figures now sit *inside* the
prose after the paragraph that introduces them (chapters too, not just decisions — the
end-of-chapter figure was what marooned FIG.1 on its own page and stranded ten lines).
Every section closes with an endmark, converting a legitimate partial tail from absence
into air. And chapter tails are finished by a **feathering pass** in the renderer — the
compositor's three cards, measured every build, never hand-listed: TIGHT pulls a small
spill back (one notch tighter, with escalation if it fails — a 2-line orphan is worse
than the 6-line one); FEED moves the chapter's photograph to its end as a tall 4.35in
closing plate that fills the tail as a designed image page; LOOSE opens a plate-less
chapter a notch so a thin tail receives enough lines to read set. Bounds are the point:
±1 notch, per chapter, from the documented baseline — a book whose whole colour moved
to fix one tail has been padded, and the fill gates catch that.

**The instrument was recalibrated with the architecture** (the skill's own precedent,
bug #19): the stub gate's 40%-of-sheet line was derived from the double-margin flow;
under real pages the same fraction holds far more column, so a complete, endmark-closed
verdict apparatus at 38% is a set tail. The line now sits at a third of the sheet.

**Generality.** Nothing here is Rome's: the page model, the string-fed runhead, the
named pages, the baseline/scale/ramp, the feathering pass, and both gates are
destination-agnostic (paper colour and furniture strings come from each project's brand
tokens; `render-paged.py` ships in `scripts/`, the polyfill in `assets/`). Rome was only
the proof.

## What changed, file by file

**Skill** (`dossier-skill-v2.zip`): NEW `references/layout-architect.md`,
`scripts/render-paged.py`, `scripts/audit-furniture.py`, `assets/paged.polyfill.js`;
REWRITTEN engine sections of `references/page-spec.md` (paged model + the graveyard) and
`references/f-render.md`; UPDATED `references/layout.md` (obsolete furniture caveat
removed, feathering), `assets/design-system.md` (baseline/scale), `SKILL.md` (stages,
quick-ref, bug log #33–37), `scripts/audit-book.py` (stub recalibration, documented).

**Build** (`rome-build-repaginated.tar.gz`): `design.py` (page model, one baseline,
feather/loose cards, endmark, closing plates), `build3.py` (ids, `.rh-src`, TOC links,
interleaved figures, endmarks, file-URL fonts/photos), `render_paged.py` (the driver);
the three dead-end render scripts removed.
