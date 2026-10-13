# design2.py — THE CSS LIVES HERE. Not in build3.py (bug log #1).
# ─────────────────────────────────────────────────────────────────────────────
# Palette: «Washi Crest» print derivation — see
# ~/.claude/skills/dossier/assets/brands/japanforamericans.json for why each
# token moved from its site value.
#
# Geometry is page-spec.md VERBATIM: head band 40–74px, body 92–984px,
# text margin 82px, foot band 984–1056px, on 816×1056 (US Letter @96dpi).
# ─────────────────────────────────────────────────────────────────────────────

import os as _os, re as _re
_FDIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'fonts')
# Inline the @font-face rules (NOT the font data — files stay file-URL
# referenced, bug log #34). An @import of a file:// stylesheet fails with
# ERR_FAILED on this volume, and a failed import silently registers ZERO
# faces, so the book renders in fallback type.
_FONTCSS = open(_os.path.join(_FDIR, 'local-fonts.css'), encoding='utf-8').read()
_FONTCSS = _re.sub(r'url\(([^)/][^)]*\.woff2)\)', r'url(fonts/\1)', _FONTCSS)

CSS = _FONTCSS + r"""

:root{
  --paper:#F5EFE1;  --ink:#242A33;    --accent:#1B3670;  --gilt:#B89547;
  --muted:#5C6068;  --soft:#8A8E97;   --line:#E1D7C2;    --line-soft:#EBE3D3;
  --panel:#EAE2D0;  --panel-edge:#E4DAC6; --deep:#16305F; --sakura:#C87F94;
  --water:#CBD6E0;
  --display:'Zen Old Mincho','Hiragino Mincho ProN',serif;
  --body:'Spectral','Hiragino Mincho ProN',Georgia,serif;
  --mono:'IBM Plex Mono','Hiragino Sans',monospace;
}

/* ── the paged page model (page-spec.md) ──────────────────────────────────── */
@page{
  size:8.5in 11in;
  margin:92px 82px 72px 82px;
  @top-left{ content:"Japan, Worked Out." }
  @top-right{ content:string(rh, last) }
  @bottom-left{ content:string(pos, last) }
  @bottom-center{ content:"\25c6" }
  @bottom-right{ content:counter(page) }
}
@page cover{ margin:0;
  @top-left{content:none} @top-right{content:none}
  @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
@page annex{ margin:92px 82px 76px 82px; }
.coverpage{ page:cover; }  .fs{ page:annex; }

html,body{ background:var(--paper); -webkit-print-color-adjust:exact;
  print-color-adjust:exact; margin:0; }
.pagedjs_sheet{ background:var(--paper); }

/* ONE selector per named string — two shadow each other (bug log #35) */
.rh-src{ string-set: rh content(text);
  display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }
.pos-src{ string-set: pos content(text);
  display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }

.pagedjs_margin-top-left .pagedjs_margin-content,
.pagedjs_margin-top-right .pagedjs_margin-content,
.pagedjs_margin-bottom-left .pagedjs_margin-content,
.pagedjs_margin-bottom-right .pagedjs_margin-content,
.pagedjs_margin-bottom-center .pagedjs_margin-content{
  font-family:var(--mono); font-size:8.5px; letter-spacing:.14em;
  color:var(--soft); text-transform:uppercase; }
.pagedjs_margin-bottom-center .pagedjs_margin-content{ color:var(--gilt); letter-spacing:0; }
/* openers suppress their running head — handler sets this class */
.pagedjs_page.opener-page .pagedjs_margin-top-right .pagedjs_margin-content,
.pagedjs_page.opener-page .pagedjs_margin-top-left .pagedjs_margin-content{ content:"" !important; }

/* ── body typography ──────────────────────────────────────────────────────── */
body{ font-family:var(--body); font-size:13.4px; line-height:1.68; color:var(--ink);
  font-variant-numeric:tabular-nums; }
p{ margin:0 0 9.5px; text-align:justify; hyphens:auto; orphans:3; widows:3; }
em{ font-style:italic; }
strong{ font-weight:600; }

/* ── FLOW: the argument is the unit, not the page (layout.md) ─────────────── */
.flow{ column-count:1; }
.flow .chap{ break-before:page; }
.flow .chap:first-child{ break-before:avoid; }

/* fragmentation rules, set ONCE (layout.md step 2) */
h1,h2,.dnum,.standfirst{ break-after:avoid; }
.ledger,.verdict,.forks,figure,.plate,.note{ break-inside:avoid; }
.verdict,.forks,.ledger{ break-before:avoid; }

/* ── ROLE: opener — a chapter begins, an event not a heading ──────────────── */
.opener{ break-inside:avoid; break-after:avoid; overflow:hidden; margin:0 0 15px; }
.opener .onum{ font-family:var(--display); font-size:58px; line-height:.78;
  color:var(--panel-edge); float:right; margin:-4px 0 0 16px; font-weight:600; }
.opener .okind{ font-family:var(--mono); font-size:8px; letter-spacing:.30em;
  text-transform:uppercase; color:var(--gilt); margin:0 0 8px; }
.opener h1{ font-family:var(--display); font-size:31px; line-height:1.06; margin:0;
  font-weight:600; }
.opener .orule{ height:2px; background:var(--gilt); margin:13px 0 0; }
.standfirst{ font-family:var(--display); font-style:italic; font-size:16px;
  line-height:1.5; color:var(--muted); margin:11px 0 13px; text-align:left; }

/* H2 is a LABEL, never a small headline (page-spec.md type hierarchy) */
h2{ font-family:var(--mono); font-size:9px; letter-spacing:.22em; text-transform:uppercase;
  color:var(--accent); margin:16px 0 7px; font-weight:600; }

/* drop cap — first paragraph of a chapter only */
.chap > p.lede:first-of-type::first-letter{
  font-family:var(--display); float:left; font-size:44px; line-height:.86;
  padding:3px 7px 0 0; color:var(--accent); font-weight:600; }

/* ── ROLE: ledger — an instrument, not a table ────────────────────────────── */
.ledger{ break-inside:avoid; background:var(--panel); border-top:2.5px solid var(--accent);
  margin:13px 0; }
.ledger .lcap{ font-family:var(--mono); font-size:8px; letter-spacing:.22em;
  text-transform:uppercase; color:var(--accent); padding:9px 14px 0; }
.ledger table{ width:100%; border-collapse:collapse; margin:5px 0 0; }
.ledger th{ font-family:var(--mono); font-size:8px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted); text-align:left; padding:4px 14px 6px;
  border-bottom:1px solid var(--line); font-weight:500; }
.ledger td{ vertical-align:top; padding:8px 14px; line-height:1.46; font-size:12.4px;
  border-bottom:1px solid var(--line-soft); }
.ledger tr:last-child td{ border-bottom:none; }
.ledger td:last-child{ text-align:right; font-family:var(--mono); font-size:11.4px;
  color:var(--deep); white-space:nowrap; }

/* ── ROLE: verdict — the payoff, must outweigh the prose ──────────────────── */
.verdict{ break-inside:avoid; padding:2px 0 2px 15px; border-left:3px solid var(--gilt);
  margin:14px 0; }
.verdict .vlab{ font-family:var(--mono); font-size:8.5px; letter-spacing:.24em;
  text-transform:uppercase; color:var(--gilt); display:block; margin:0 0 5px; }
.verdict p{ font-family:var(--display); font-size:13.6px; line-height:1.54;
  text-align:left; margin:0; }
.verdict p strong{ font-weight:600; color:var(--deep); }

/* ── ROLE: forks — labelled by MEANING, not for/against ───────────────────── */
.forks{ display:flex; gap:18px; break-inside:avoid; margin:13px 0; }
.fork{ flex:1; border-top:1px solid var(--line); padding-top:8px; }
.fork b{ font-family:var(--mono); font-size:8px; letter-spacing:.18em; text-transform:uppercase;
  display:block; margin:0 0 6px; font-weight:600; }
.fork.f b{ color:var(--accent); }
.fork.a b{ color:var(--gilt); }
.fork ul{ margin:0; padding:0; list-style:none; }
.fork li{ font-size:11.8px; line-height:1.48; margin:0 0 5px; text-align:left;
  color:var(--muted); }

/* ── ROLE: figure — the evidence anchor ───────────────────────────────────── */
figure{ margin:15px 0; break-inside:avoid; }
figure svg{ width:100%; height:auto; display:block; }
figure img{ width:100%; height:auto; display:block; }
figcaption{ font-family:var(--mono); font-size:8.5px; letter-spacing:.1em; color:var(--muted);
  margin:7px 0 0; text-transform:uppercase; }
figcaption .fnum{ color:var(--gilt); font-weight:600; }
/* ROLE: plate — the photograph IS the evidence. Full column, 3:2, never a stamp. */
.plate{ margin:16px 0; break-inside:avoid; }
.plate img{ width:100%; height:auto; display:block; border:1px solid var(--line); }
.plate figcaption{ text-transform:none; letter-spacing:0; font-family:var(--body);
  font-size:10.8px; font-style:italic; line-height:1.5; color:var(--muted);
  padding-left:12px; border-left:2px solid var(--gilt); margin-top:9px; }
.plate figcaption .fnum{ font-family:var(--mono); font-style:normal; font-size:8.5px;
  letter-spacing:.18em; color:var(--gilt); }

/* a decision's tail travels as one block — never a lone note on a sheet */
.dtail{ break-inside:avoid; break-before:avoid; }

/* ── the note strip (provenance / Field Sheet pointer) ────────────────────── */
.note{ font-size:10.8px; line-height:1.5; color:var(--muted); border-top:1px solid var(--line);
  padding:8px 0 0; margin:13px 0 0; text-align:left; }

/* cross-reference — prints the live folio of what it points at */
.xref{ color:var(--deep); text-decoration:none; border-bottom:1px solid var(--line); }
.xref::after{ content:", p." target-counter(attr(href), page);
  font-family:var(--mono); font-size:9px; color:var(--muted); }

/* ── provenance marks — seasoning, never mid-sentence (writing-code.md) ───── */
.mk{ font-size:8.5px; vertical-align:2px; margin:0 0 0 3px; }
.mk.est{ color:var(--accent); } .mk.off{ color:var(--deep); }
.mk.sur{ color:var(--gilt); }   .mk.vol{ color:var(--sakura); }

/* ── endmark so a partial tail reads closed, not empty ────────────────────── */
.endmark{ text-align:center; color:var(--gilt); font-size:10px; margin:16px 0 0;
  break-before:avoid; }

/* The renderer's feathering only measures section.dec, so PROSE chapters get no
   tail management at all — the Eating chapter stranded its closing paragraph on a
   sheet of its own. Keep a chapter's last paragraph with the text above it. */
.chap > p:last-of-type{ break-before:avoid; }

/* ── cover ────────────────────────────────────────────────────────────────── */
.coverpage{ width:816px; height:1056px; position:relative; overflow:hidden;
  background:var(--paper); break-after:page; break-inside:avoid; }
.coverpage svg{ position:absolute; inset:0; width:816px; height:1056px; }

/* ── TOC ──────────────────────────────────────────────────────────────────── */
.toc h1{ font-family:var(--display); font-size:28px; margin:0 0 4px; font-weight:600; }
.toc ol{ list-style:none; margin:18px 0 0; padding:0; }
.toc li{ display:flex; align-items:baseline; gap:8px; margin:0 0 6.5px; font-size:12.4px; }
.toc li.tgroup{ margin-top:11px; }
.toc ol{ list-style:none; margin:14px 0 0; padding:0; }
.toc .tnum{ font-family:var(--mono); font-size:7.5px; letter-spacing:.12em;
  color:var(--gilt); width:86px; flex:none; text-transform:uppercase; }
.toc .tdot{ flex:1; border-bottom:1px dotted var(--line); transform:translateY(-3px); }
.toc a{ color:var(--ink); text-decoration:none; }
.toc .tpg a{ text-decoration:none; }
.toc .tpg a::after{ content:target-counter(attr(href), page); font-family:var(--mono);
  font-size:10px; color:var(--muted); }

/* ── Field Sheet (annex) — dense reference grid ───────────────────────────── */
.fs table{ width:100%; border-collapse:collapse; font-size:11.4px; }
.fs th{ font-family:var(--mono); font-size:8px; letter-spacing:.14em; text-transform:uppercase;
  text-align:left; color:var(--muted); border-bottom:1.5px solid var(--accent);
  padding:0 10px 6px 0; font-weight:500; }
.fs td{ padding:7px 10px 7px 0; border-bottom:1px solid var(--line-soft); vertical-align:top;
  line-height:1.44; }
.fs td:last-child{ font-family:var(--mono); font-size:10.8px; color:var(--deep);
  text-align:right; white-space:nowrap; }

/* the Field Sheet's own renewal notice — a block, never a ledger row, so it
   cannot inherit the value column's nowrap and run off the sheet */
.renew{ background:var(--panel); border-top:2.5px solid var(--accent);
  padding:9px 14px 11px; margin:0 0 14px; }
.renew .lcap{ padding:0 0 4px; }
.renew p{ margin:0; font-size:11.8px; line-height:1.5; text-align:left;
  white-space:normal; }
.renew b{ font-family:var(--mono); font-size:11px; color:var(--deep); }

/* ── refusals / back matter ───────────────────────────────────────────────── */
.refuse li{ margin:0 0 9px; font-size:12.4px; line-height:1.55; }
.refuse b{ font-family:var(--display); color:var(--deep); }

/* ── feather: the one notch either side of the base setting ───────────────────
   render-paged.py's feather pass marks a chapter .tight (pull a small spill back
   onto the preceding page) or .loose (open the setting so a thin tail page
   receives enough lines to read as a page rather than a stub).

   These rules did not exist. The pass computed its verdicts, applied the class,
   and printed "loosening [...]" on every single build — against a stylesheet
   that defined nothing for either class, so it had never moved a line in this
   book's history. Base is 13.4px/1.68 with 9.5px between paragraphs; one notch
   is about +/- 1 line in 12. Keep both modest: the page-shape and consistency
   gates measure exactly what these change.                                    */
.tight p{ line-height:1.60; margin-bottom:8px; }
.tight .verdict p{ line-height:1.47; }
.tight .ledger td{ padding-top:6px; padding-bottom:6px; }

.loose p{ line-height:1.76; margin-bottom:11.5px; }
.loose .verdict p{ line-height:1.62; }
.loose .ledger td{ padding-top:10px; padding-bottom:10px; }
"""
