# -*- coding: utf-8 -*-
"""design.py — ALL the CSS for Thailand, Covered.

Bug-log rule 1 from SKILL.md: the CSS lives in ONE module. Edits to the builder's
style block do nothing and half of Rome's cover bugs were exactly that.

Palette is measured, not chosen by eye — see dossier/brand.json for the ratios.
The jobs follow from the numbers:
    ink         #241A21  14.99:1 on paper   body
    ink_soft    #6B5F66   5.40:1             secondary, clears AA
    accent      #D81264   4.45:1             BELOW AA small — rules, fills, large type ONLY
    accent_deep #9C0C48   7.29:1             the accent for anything small
    rule        #DCCFC0   1.36:1             hairlines, never text

Carries the 2026-09-18 skill corrections:
  · essential text is 12px/17px minimum, in the BODY face (the old 7.5px caption
    contradicted this file's own "8 is the print floor", and 8px is 6 printed pt)
  · prose has its own measure (520px); the 652px column is for tables and figures
  · the ledger has three variants with fixed column contracts
  · the decision opener answers before it narrates
"""

PAPER       = "#F7F1E4"
PAPER_DEEP  = "#EFE5D2"
INK         = "#241A21"
INK_SOFT    = "#6B5F66"
RULE        = "#DCCFC0"
CHROME      = "#2B1E28"
ACCENT      = "#D81264"
ACCENT_DEEP = "#9C0C48"

DISPLAY = "'Anton', 'Archivo', sans-serif"
BODY    = "'Archivo', sans-serif"

CSS = f"""
/* ─── the sheet contract ────────────────────────────────────────────────── */
@page {{
  size: 8.5in 11in;
  margin: 92px 82px 72px 82px;
  background: {PAPER};

  @top-left  {{ content: string(booktitle);
                font: 400 10px/1.4 {BODY}; letter-spacing: .12em;
                text-transform: uppercase; color: {INK_SOFT};
                vertical-align: bottom; padding-bottom: 14px; }}
  @top-right {{ content: string(navtitle);
                font: 400 10px/1.4 {BODY}; letter-spacing: .12em;
                text-transform: uppercase; color: {INK_SOFT};
                text-align: right; vertical-align: bottom; padding-bottom: 14px; }}
  /* roles.md specifies POSITION in the foot band, not the brand. page-spec.md
     offered the brand alternative and all three shipped books took it; the
     2026-09-18 pass resolved it — position wins. */
  /* The foot band used to read FRONT MATTER / ESSAY / BACK MATTER on the left,
     which told the reader nothing the page did not already say. On a decision it
     still carries the position in the argument, which is worth knowing. On every
     other page it is empty, and the folio answers "how far through am I" instead
     of just "which sheet is this". */
  @bottom-left  {{ content: string(position);
                   font: 400 10px/1.4 {BODY}; letter-spacing: .12em;
                   text-transform: uppercase; color: {INK_SOFT};
                   vertical-align: top; padding-top: 22px; }}
  @bottom-right {{ content: counter(page) " / " counter(pages);
                   font: 400 12px/1.4 {BODY}; letter-spacing: .04em;
                   color: {INK_SOFT};
                   text-align: right; vertical-align: top; padding-top: 22px; }}
}}
@page cover {{ margin: 0; background: {CHROME};
               @top-left{{content:none}} @top-right{{content:none}}
               @bottom-left{{content:none}} @bottom-right{{content:none}} }}

html, body {{ margin: 0; padding: 0; background: {PAPER}; color: {INK}; }}
body {{ font-family: {BODY}; font-size: 13px; }}

/* The string-set carriers must not generate a box in the flow: as absolutely
   positioned spans they still opened a page of their own, which is why a blank
   sheet appeared either side of the cover. display:none keeps string-set working
   in Paged.js while taking them out of layout entirely. */
.booktitle, .navtitle, .position {{ display: none; }}
.booktitle {{ string-set: booktitle content(); }}
.navtitle  {{ string-set: navtitle  content(); }}
.position  {{ string-set: position  content(); }}

/* ─── reading modes (layout-architect.md, 2026-09-18) ───────────────────────
   One sheet, four inner arrangements. The outer edges never move; the measure
   and the hierarchy answer different tasks. */

/* ONE measure, and it is the instrument width. The prose used to be set to
   520px inside a 652px column: a dead band down the right of every page, text
   pinned left, two right edges on one sheet. A narrow measure earns its keep
   only when something lives in the band beside it, and nothing did.
   The type goes up to 16px so the longer line still reads. */
.prose {{ max-width: none; }}
.prose p {{ font-size: 16px; line-height: 24px; margin: 0 0 13px; }}
/* The opening paragraph is NOT a different size. It was 17px against a 15px
   body, which reads as the text shrinking rather than as emphasis. It leads by
   position and by weight; the size is the body size. */
.prose p.lede {{ font-size: 16px; line-height: 24px; font-weight: 500; }}

/* The compositor's card, and its limits. The renderer measures each section's
   tail page and re-sets the section one notch tighter (to pull a few orphan
   lines back) or one notch looser (to push enough lines down that the tail
   reads as a page rather than a fragment). Type SIZE never changes — only
   leading and paragraph spacing, by one and two pixels. Anything more is the
   inflated-air padding the depth audit fails a book for. */
.tight .prose p {{ line-height: 23px; margin-bottom: 11px; }}
.tight .opener p,
.tight .verdict p    {{ line-height: 23px; }}
.tight table.ledger td {{ padding-top: 7px; padding-bottom: 7px; }}
.loose .prose p   {{ line-height: 25px; margin-bottom: 15px; }}
.loose .opener p,
.loose .verdict p    {{ line-height: 25px; }}
.loose table.ledger td {{ padding-top: 11px; padding-bottom: 11px; }}

/* NO break-before here. section.dec already breaks, and a second break on the
   h1 split the eyebrow onto its own page with the title alone on the next. */
h1 {{ font-family: {DISPLAY}; font-weight: 400; font-size: 40px; line-height: 1.06;
      letter-spacing: .005em; margin: 0 0 6px; color: {INK}; }}
h1.q {{ max-width: 620px; }}
.eyebrow {{ font-size: 10px; letter-spacing: .16em; text-transform: uppercase;
            color: {ACCENT_DEEP}; margin: 0 0 14px; font-weight: 600; }}
.standfirst {{ font-size: 16px; line-height: 23px; color: {INK_SOFT};
               max-width: none; margin: 0 0 18px; font-style: italic; }}

/* the decision opener — answers before it narrates */
.opener {{ break-inside: avoid; border-left: 3px solid {ACCENT};
                  padding: 18px 22px; margin: 0 0 20px; max-width: none;
                  background: {PAPER_DEEP}; }}
.opener .k {{ font-size: 10px; letter-spacing: .16em; text-transform: uppercase;
                     color: {ACCENT_DEEP}; font-weight: 600; margin: 0 0 7px; }}
.opener p {{ font-size: 16px; line-height: 24px; margin: 0 0 10px; }}
.opener p:last-child {{ margin-bottom: 0; }}
.opener strong {{ font-weight: 600; }}

/* ─── the ledger: three variants, fixed column contracts ─────────────────── */
table.ledger {{ width: 100%; table-layout: fixed; border-collapse: collapse;
                margin: 4px 0 18px; break-inside: avoid; }}
table.ledger caption {{ caption-side: top; text-align: left;
                        font-size: 10px; letter-spacing: .14em; text-transform: uppercase;
                        color: {INK_SOFT}; padding: 0 0 8px; }}
table.ledger th {{ font-size: 11px; line-height: 15px; letter-spacing: .1em;
                   text-transform: uppercase; color: {ACCENT_DEEP}; font-weight: 600;
                   text-align: left; padding: 0 12px 7px 0;
                   border-bottom: 1.5px solid {ACCENT}; }}
table.ledger td {{ font-size: 12px; line-height: 17px; padding: 9px 12px 9px 0;
                   border-bottom: 1px solid {RULE}; vertical-align: top; }}
table.ledger td.num, table.ledger th.num {{ text-align: right; padding-right: 0;
                   font-variant-numeric: tabular-nums; }}
/* table-layout:fixed without widths gives equal thirds, which starves the two
   prose columns to feed a column of short labels. The option name is a label;
   the other two carry sentences. */
table.ledger col.label  {{ width: 25%; }}
table.ledger col.wide   {{ width: 38%; }}
table.ledger col.mid    {{ width: 17%; }}
table.ledger col.narrow {{ width: 13%; }}
table.ledger col.tiny   {{ width:  8%; }}
/* The decisive row is named in TEXT, never colour alone. The wording arrives
   from the builder rather than from a CSS `content` string, because it differs
   per table — an essay ledger has no choice to change. */
table.ledger tr.decisive td {{ background: {PAPER_DEEP}; }}
/* Its own line. As an inline nowrap span it overflowed the 25% label column and
   printed straight across the neighbouring cell. */
.dx {{ display: block; color: {ACCENT_DEEP}; font-size: 10px; letter-spacing: .08em;
       text-transform: uppercase; margin-top: 3px; }}

/* ─── the verdict, and the reversal that must be losable ─────────────────── */
/* A drawn rule states an edge; ragged prose does not. So the RULES span the full
   text column — the same right edge as the ledger above them — while the text
   inside keeps the reading measure. Two right edges on one page read as a
   mistake even when both are deliberate. */
.verdict {{ border-top: 2.5px solid {ACCENT}; padding: 14px 0 0; margin: 20px 0 16px;
         break-inside: avoid; }}
.verdict p {{ max-width: none; font-size: 16px; line-height: 24px; margin: 0; }}
.verdict .k {{ font-size: 10px; letter-spacing: .16em; text-transform: uppercase;
            color: {ACCENT_DEEP}; font-weight: 600; margin: 0 0 8px; }}

.forks {{ display: flex; gap: 34px; margin: 0 0 14px; break-inside: avoid; }}
.forks > div {{ flex: 1; }}
.forks .k {{ font-size: 10px; letter-spacing: .1em; text-transform: uppercase;
             color: {INK_SOFT}; font-weight: 600; margin: 0 0 8px;
             border-bottom: 1px solid {RULE}; padding-bottom: 6px; }}
.forks li {{ font-size: 13px; line-height: 18px; margin: 0 0 9px; list-style: none; }}
.forks ul {{ margin: 0; padding: 0; }}

/* ─── apparatus: 12px floor, BODY face, sentence case ────────────────────── */
figcaption, .caption {{ font-size: 12.5px; line-height: 18px; color: {INK_SOFT};
                        max-width: none; margin: 8px 0 0; }}
/* The closing note must not open a page on its own. `break-before: avoid` on the
   note alone just moved the problem two chapters along and added a sheet, so the
   note travels WITH the block it annotates instead: an essay's ledger and its
   note are one unbreakable group, and if they do not fit they cross together and
   the next page gets a real page's worth of content. */
.close {{ break-inside: avoid; }}
.figlabel {{ font-size: 11px; letter-spacing: .1em; text-transform: uppercase;
             color: {ACCENT_DEEP}; font-weight: 600; }}
.mk {{ font-size: 11px; color: {ACCENT_DEEP}; }}

figure {{ margin: 18px 0; break-inside: avoid; page-break-inside: avoid; }}
figure svg {{ width: 100%; height: auto; display: block; }}
/* the drawn figures ship as atomic images; the box is set by the viewBox ratio */
img.drawnimg {{ width: 100%; height: auto; display: block; }}
/* A drawn figure is an instrument, so it takes the instrument width — the same
   right edge as the ledger and the rules, never the prose measure. */
figure.drawn {{ margin: 22px 0 18px; }}


/* A plate is 3:2 at the full instrument width — 4.5in tall, 49% of the text
   block. e-image.md's arithmetic: a portrait would need 10.2in in a 6.8in
   column and can only ever render as a stamp floating in cream. */
figure.photo {{ margin: 20px 0 22px; break-inside: avoid; }}
figure.photo img {{ width: 100%; aspect-ratio: 3 / 2; object-fit: cover;
                    display: block; background: {PAPER_DEEP}; }}
figure.photo figcaption {{ margin-top: 9px; }}

/* Only sections AFTER the first break. The first one already starts a page —
   leaving the cover's named page is itself a break — and the two together left a
   blank sheet between the cover and chapter one. */
/* Between any two sections in the flow — the key page and Decision 01 included.
   The old form named `.dec + .dec` only, so a front-matter section would have
   run straight into chapter one with no break at all. */
.flow > section + section {{ break-before: page; }}
/* The end mark was ◆ — which is ALSO the volatile-value mark in the provenance
   key, three inches up the same page. A glyph may not mean two things in one
   book. The section ends with a rule, which means nothing else here. */
.endmark {{ border-top: 1.5px solid {RULE}; width: 84px; margin: 22px auto 0;
            height: 0; font-size: 0; }}

/* ─── the part divider ───────────────────────────────────────────────────── */
/* Not an empty rule to satisfy a checker: a divider is a different KIND of page,
   so it reads differently — deeper top air, display type a size up, and no
   running head of its own to compete with the part name. */
.partdiv {{ padding-top: 58px; }}
.partdiv h1 {{ font-size: 54px; margin-bottom: 12px; }}
.partdiv .standfirst {{ font-style: normal; max-width: none; }}
.pilist {{ margin: 26px 0 0; }}
.pi {{ display: flex; gap: 22px; padding: 11px 0;
       border-bottom: 1px solid {RULE}; break-inside: avoid; }}
.pi:first-child {{ border-top: 1.5px solid {ACCENT}; }}
.pik {{ flex: 0 0 132px; font-size: 11px; letter-spacing: .1em; font-weight: 600;
        text-transform: uppercase; color: {ACCENT_DEEP}; padding-top: 2px; }}
.piv {{ flex: 1; font-size: 14px; line-height: 20px; color: {INK}; }}

/* ─── the Field Sheet: two cut-out cards, 3.25 × 4.5in ───────────────────── */
.cards {{ display: flex; gap: 28px; margin: 20px 0 16px; break-inside: avoid; }}
.card {{ width: 312px; min-height: 432px; box-sizing: border-box;
         border: 1px dashed {INK_SOFT}; padding: 16px 16px 14px;
         background: {PAPER}; }}
.cardhead {{ font-family: {DISPLAY}; font-size: 20px; line-height: 1.1;
             color: {INK}; margin: 0 0 5px; }}
.cardsub {{ font-size: 12px; line-height: 16px; color: {INK_SOFT};
            margin: 0 0 11px; padding-bottom: 9px;
            border-bottom: 1.5px solid {ACCENT}; }}
.card ul {{ margin: 0; padding: 0; list-style: none; }}
.card li {{ font-size: 12px; line-height: 16px; margin: 0 0 9px; color: {INK}; }}
.card li:last-child {{ margin-bottom: 0; }}
.ck {{ display: block; font-size: 10px; letter-spacing: .08em; font-weight: 600;
       text-transform: uppercase; color: {ACCENT_DEEP}; }}
/* a line to write the assistance number on — the one number the book cannot
   supply and the one the corpus says decides the outcome */
.fill {{ display: inline-block; width: 100%; border-bottom: 1px solid {INK_SOFT};
         height: 15px; }}

/* ─── the key page ───────────────────────────────────────────────────────── */
.htgrid {{ margin: 22px 0 30px; }}
.ht {{ break-inside: avoid; margin: 0 0 20px; padding-left: 16px;
       border-left: 2px solid {RULE}; max-width: none; }}
.ht .k {{ font-size: 13px; letter-spacing: .02em; color: {INK};
          font-weight: 600; margin: 0 0 6px; }}
.ht p {{ font-size: 15px; line-height: 22px; margin: 0; color: {INK_SOFT}; }}
table.keytable td.keymark {{ text-align: left; font-size: 13px; color: {ACCENT_DEEP}; }}
table.keytable td {{ border-bottom: 1px solid {RULE}; }}

/* ─── cover ──────────────────────────────────────────────────────────────── */
/* The chrome must reach the trim. A div cannot: `height:100%` has no resolved
   parent height in Paged.js, so it fell back to min-height and left a paper
   strip along the right and bottom edges. Paint the SHEET instead. */
.pagedjs_page:has(.cover) {{ background: {CHROME}; }}
.pagedjs_page:has(.cover) .pagedjs_page_content,
.pagedjs_page:has(.cover) .pagedjs_area {{ background: {CHROME}; }}
.cover {{ page: cover; width: 100%; height: 100%; min-height: 1040px;
          background: {CHROME}; color: {PAPER}; position: relative; overflow: hidden; }}
.cover .wrap {{ position: absolute; left: 82px; right: 82px; top: 104px; }}
.cover .press {{ font-size: 11px; letter-spacing: .28em; text-transform: uppercase;
                 color: {ACCENT}; margin: 0 0 34px; }}
.cover h1 {{ font-family: {DISPLAY}; font-size: 98px; line-height: .94;
             letter-spacing: .01em; margin: 0; color: {PAPER}; break-before: auto; }}
/* cover.md: the cover PROMISES, the interior proves. One device, at most three
   labels, nothing below 24px at cover size. */
.cover .promise {{ font-size: 24px; line-height: 32px; color: {PAPER};
                   max-width: 600px; margin: 30px 0 0; opacity: .92; }}
.cover .foot {{ position: absolute; left: 82px; right: 82px; bottom: 58px;
                font-size: 12px; letter-spacing: .14em; text-transform: uppercase;
                color: {PAPER}; opacity: .55; }}

/* the device — seven places, four marks each, and a rule where the marks stop */
.device {{ position: absolute; left: 82px; right: 82px; bottom: 110px; }}
.cdrow {{ display: flex; align-items: center; gap: 26px; padding: 9px 0; }}
.cd-break {{ border-bottom: 2px solid {ACCENT}; padding-bottom: 15px; margin-bottom: 8px; }}
.cdname {{ flex: 0 0 auto; font-family: {DISPLAY}; font-weight: 400; font-size: 26px;
           line-height: 1; color: {PAPER}; letter-spacing: .01em; }}
/* the marks carry to the right margin, so the row spans the sheet the way
   the rule under it does */
.cddots {{ display: flex; gap: 42px; margin-left: auto; }}
.cd {{ width: 18px; height: 18px; border-radius: 50%; display: block; }}
.cd-full {{ background: {PAPER}; }}
.cd-none {{ background: transparent; box-shadow: inset 0 0 0 1.5px rgba(247,241,228,.34); }}
/* the mainland case: half the mark, because Krabi's airport and hospitals are
   real and are not on the island */
.cd-half {{ background: linear-gradient(90deg, {PAPER} 0 50%, transparent 50% 100%);
            box-shadow: inset 0 0 0 1.5px rgba(247,241,228,.55); }}
"""
