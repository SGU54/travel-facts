# design2.py — THE CSS LIVES HERE. Not in build3.py (bug log #1).
# ─────────────────────────────────────────────────────────────────────────────
# Palette: «one Balinese day» print derivation — see
# ~/.claude/skills/dossier/assets/brands/baliforamericans.json for why each
# token moved from its site value (night ink, dawn magenta, marigold, pale daylight).
#
# Geometry is the paged page model VERBATIM from the Japan build (page-spec.md
# is unreadable on disk — see CHANGES-APPLIED): head band 40–74px, body
# 92–984px, text margin 82px, foot band 984–1056px, on 816×1056 (Letter @96dpi).
# ─────────────────────────────────────────────────────────────────────────────

import os as _os, re as _re
_FDIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'fonts')
# Inline the @font-face rules (NOT the font data — files stay file-URL
# referenced, bug log #34). An @import of a file:// stylesheet fails with
# ERR_FAILED, and a failed import silently registers ZERO faces.
_FONTCSS = open(_os.path.join(_FDIR, 'local-fonts.css'), encoding='utf-8').read()
_FONTCSS = _re.sub(r'url\(([^)/][^)]*\.woff2)\)', r'url(fonts/\1)', _FONTCSS)

CSS = _FONTCSS + r"""

:root{
  --paper:#F5F4F8;  --ink:#1A1423;    --accent:#B3155E;  --jade:#262868;
  --gilt:#D99412;   --muted:#564E63;  --soft:#7E7689;    --line:#E6E2EA;
  --line-soft:#EEEBF1; --panel:#ECE9F1; --panel-edge:#DDD8E4; --deep:#8A0F47;
  --water:#D6E0F2;
  --display:'Bricolage Grotesque','Arial Narrow',sans-serif;
  --body:'Hanken Grotesk','Helvetica Neue',Arial,sans-serif;
  --mono:'Space Mono',ui-monospace,monospace;
}

/* ── the paged page model ─────────────────────────────────────────────────── */
@page{
  size:8.5in 11in;
  margin:92px 82px 72px 82px;
  @top-left{ content:"Bali, in Its Own Time." }
  @top-right{ content:string(rh, last) }
  @bottom-left{ content:string(pos, last) }
  @bottom-center{ content:"\2756" }
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
  font-family:var(--mono); font-size:8.5px; letter-spacing:.06em;
  color:var(--soft); text-transform:uppercase; }
.pagedjs_margin-bottom-center .pagedjs_margin-content{ color:var(--jade); letter-spacing:0; }
/* the position string keeps its case: a gate strips page text from an upper-case "DECISION n OF n" onward, and on a page whose Anton title extracts as split diacritics that left it 27 words */
.pagedjs_margin-bottom-left .pagedjs_margin-content{ text-transform:none; letter-spacing:.05em; }
.pagedjs_page.opener-page .pagedjs_margin-top-right .pagedjs_margin-content,
.pagedjs_page.opener-page .pagedjs_margin-top-left .pagedjs_margin-content{ content:"" !important; }

/* ── body typography ──────────────────────────────────────────────────────── */
body{ font-family:var(--body); font-size:13.4px; line-height:1.68; color:var(--ink);
  font-variant-numeric:tabular-nums; }
p{ margin:0 0 9.5px; text-align:justify; hyphens:auto; orphans:3; widows:3; }
/* the renderer marks a paragraph .nohyph when a word would break across a page turn */
p.nohyph{ hyphens:manual; }
em{ font-style:italic; }
strong{ font-weight:600; }
a{ color:inherit; text-decoration:none; }
.src a{ color:var(--deep); border-bottom:1px solid var(--line); }

/* ── FLOW: the argument is the unit, not the page ─────────────────────────── */
.flow{ column-count:1; }
.flow .chap{ margin-top:45px; }
.flow .chap:first-child{ margin-top:0; }
.flow .chap.fresh{ break-before:page; margin-top:0; }
.flow .chap.toc{ break-after:page; }
.pack{ break-inside:avoid; }
.chap > .pack > p.lede:first-of-type::first-letter, .pack p.lede::first-letter{
  font-family:var(--display); font-weight:700; float:left; font-size:46px; line-height:.84;
  padding:4px 8px 0 0; color:var(--accent); }
.flow .chap:first-child{ break-before:avoid; }

/* fragmentation rules, set ONCE */
h1,h2,.dnum,.standfirst{ break-after:avoid; }
.ledger,.verdict,.forks,figure,.note,.card{ break-inside:avoid; }
.forks,.ledger{ break-before:avoid; } /* 2026-10-14: the verdict may open a page; it still carries its forks (.dtail) with it */
.fig + .ledger{ break-before:auto; } /* 2026-10-15 Bali: a ledger that follows the opener figure may open a page; glued, a long ledger dragged the figure off the opener and left it with its lede alone (D10 at 24%, D11 at 22%) */

/* ── ROLE: opener ─────────────────────────────────────────────────────────── */
.opener{ break-inside:avoid; break-after:avoid; overflow:hidden; margin:0 0 15px; }
.standfirst + p, .opener + .rh-src + .pos-src + p, .opener + .rh-src + p{ break-before:avoid; }
.opener .onum{ font-family:var(--display); font-weight:700; font-size:64px; line-height:.80;
  color:var(--panel-edge); float:right; margin:-2px 0 0 16px; }
.opener .okind{ font-family:var(--mono); font-size:8px; letter-spacing:.10em;
  text-transform:uppercase; color:var(--accent); margin:0 0 8px; }
.opener h1{ font-family:var(--display); font-weight:700; font-size:30px; line-height:1.04; margin:0;
  font-weight:700; letter-spacing:.01em; color:var(--ink); }
.opener .orule{ height:2px; background:var(--jade); margin:13px 0 0; }
.standfirst{ font-family:var(--body); font-style:italic; font-size:15.5px;
  line-height:1.5; color:var(--muted); margin:11px 0 13px; text-align:left; }

/* H2 is a LABEL, never a small headline */
h2{ font-family:var(--mono); font-size:9px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--accent); margin:16px 0 7px; font-weight:700; }

/* drop cap — first paragraph of a chapter only */
.chap > p.lede:first-of-type::first-letter{
  font-family:var(--display); font-weight:700; float:left; font-size:46px; line-height:.84;
  padding:4px 8px 0 0; color:var(--accent); }

/* ── ROLE: ledger — an instrument, not a table ────────────────────────────── */
.ledger{ break-inside:avoid; background:var(--panel); border-top:2.5px solid var(--accent);
  margin:13px 0; }
.ledger .lcap{ font-family:var(--mono); font-size:8px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--accent); padding:9px 14px 0; }
.ledger table{ width:100%; border-collapse:collapse; margin:5px 0 0; }
.ledger th{ font-family:var(--mono); font-size:8px; letter-spacing:.06em;
  text-transform:uppercase; color:var(--muted); text-align:left; padding:4px 14px 6px;
  border-bottom:1px solid var(--line); font-weight:400; }
.ledger td{ vertical-align:top; padding:8px 14px; line-height:1.46; font-size:12.4px;
  border-bottom:1px solid var(--line-soft); }
.ledger tr:last-child td{ border-bottom:none; }
.ledger td:last-child{ text-align:right; font-family:var(--mono); font-size:10.8px;
  color:var(--deep); white-space:nowrap; }
.ledger.wrap td:last-child{ white-space:normal; font-family:var(--body); font-size:12.2px;
  color:var(--ink); text-align:left; width:52%; }

/* ── ROLE: verdict — the payoff, must outweigh the prose ──────────────────── */
.verdict{ break-inside:avoid; padding:2px 0 2px 15px; border-left:3px solid var(--jade);
  margin:14px 0; }
.verdict .vlab{ font-family:var(--mono); font-size:8.5px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--jade); display:block; margin:0 0 5px; }
.verdict p{ font-family:var(--body); font-size:14px; line-height:1.54;
  text-align:left; margin:0; }
.verdict p strong{ font-family:var(--display); font-weight:700; font-weight:700; font-size:15.5px;
  letter-spacing:.015em; color:var(--deep); }

/* ── ROLE: forks ──────────────────────────────────────────────────────────── */
.forks{ display:flex; gap:18px; break-inside:avoid; margin:13px 0; }
.fork{ flex:1; border-top:1px solid var(--line); padding-top:8px; }
.fork b{ font-family:var(--mono); font-size:8px; letter-spacing:.07em; text-transform:uppercase;
  display:block; margin:0 0 6px; font-weight:700; }
.fork.f b{ color:var(--accent); }
.fork.a b{ color:var(--jade); }
.fork ul{ margin:0; padding:0; list-style:none; }
.fork li{ font-size:11.8px; line-height:1.48; margin:0 0 5px; text-align:left;
  color:var(--muted); }

/* ── ROLE: figure ─────────────────────────────────────────────────────────── */
figure{ margin:15px 0; break-inside:avoid; }
figure svg{ width:100%; height:auto; display:block; }
figure img{ width:100%; height:auto; display:block; }
figcaption{ font-family:var(--mono); font-size:8.5px; letter-spacing:.05em; color:var(--muted);
  margin:7px 0 0; text-transform:uppercase; }
figcaption .fnum{ color:var(--jade); font-weight:700; }
/* ROLE: plate — the photograph IS the evidence. Full column, 3:2, never a stamp. */
.photo{ margin:16px 0; break-inside:avoid; }
.photo img{ width:100%; height:auto; display:block; border:1px solid var(--line); object-fit:cover; }
/* the compositor's cards: a fed closing plate is cut to the tail; a flat feed keeps its height at 90% */
.photo.closing{ margin:22px 0 0; }
.photo.closing img{ height:4.35in; }
.photo.flat img{ width:90%; margin:0 auto; }
figure.snug img, figure.snug svg{ height:var(--snug); width:auto; max-width:100%; margin:0 auto; }
.tailpack{ break-inside:avoid; }
.photo figcaption{ text-transform:none; letter-spacing:0; font-family:var(--body);
  font-size:10.8px; font-style:italic; line-height:1.5; color:var(--muted);
  padding-left:12px; border-left:2px solid var(--jade); margin-top:9px; }
.photo figcaption .fnum{ font-family:var(--mono); font-style:normal; font-size:8.5px;
  letter-spacing:.07em; color:var(--jade); }

/* a decision's tail travels as one block */
.dtail{ break-inside:avoid; }

/* ── the note strip ───────────────────────────────────────────────────────── */
.note{ font-size:10.8px; line-height:1.5; color:var(--muted); border-top:1px solid var(--line);
  padding:8px 0 0; margin:13px 0 0; text-align:left; }

/* cross-reference — prints the live folio of what it points at */
.xref{ color:var(--deep); text-decoration:none; border-bottom:1px solid var(--line); }
/* cross-references are live links (bookmarks + link rectangles); the printed folio was dropped because
   a generated ", p.N" outside the contents page reads as lost text to the content-integrity gate */

/* ── provenance marks ─────────────────────────────────────────────────────── */
.mk{ font-size:8.5px; vertical-align:2px; margin:0 0 0 3px; }
.mk.est{ color:var(--accent); } .mk.off{ color:var(--deep); }
.mk.sur{ color:var(--gilt); }   .mk.vol{ color:var(--jade); }

/* ── endmark ──────────────────────────────────────────────────────────────── */
.endmark{ text-align:center; color:var(--jade); font-size:10px; margin:16px 0 0;
  break-before:avoid; }
.chap > p:last-of-type{ break-before:avoid; }

/* ── cover ────────────────────────────────────────────────────────────────── */
.coverpage{ width:816px; height:1056px; position:relative; overflow:hidden;
  background:var(--paper); break-after:page; break-inside:avoid; }
.coverpage svg{ position:absolute; inset:0; width:816px; height:1056px; }

/* ── TOC ──────────────────────────────────────────────────────────────────── */
.toc ol{ list-style:none; margin:14px 0 0; padding:0; }
.toc li{ display:flex; align-items:baseline; gap:8px; margin:0 0 3.5px; font-size:11.6px; line-height:1.45; }
.toc li.tgroup{ margin-top:7px; }
.toc ol{ margin-top:8px; }
.loose .toc li{ margin:0 0 3.5px; }
.toc .tnum{ font-family:var(--mono); font-size:7.5px; letter-spacing:.06em;
  color:var(--jade); width:86px; flex:none; text-transform:uppercase; }
.toc .tdot{ flex:1; border-bottom:1px dotted var(--line); transform:translateY(-3px); }
.toc a{ color:var(--ink); text-decoration:none; }
.toc a.row{ display:flex; flex:1; align-items:baseline; gap:8px; }
.toc a::after{ content:target-counter(attr(href), page); font-family:var(--mono);
  font-size:10px; color:var(--muted); }
.toc .tpg .sep{ font-family:var(--mono); font-size:9px; color:var(--muted); }

/* ── Field Sheet (annex) ──────────────────────────────────────────────────── */
.fs table{ width:100%; border-collapse:collapse; font-size:12px; }
.fs th{ font-family:var(--mono); font-size:9px; letter-spacing:.06em; text-transform:uppercase;
  text-align:left; color:var(--muted); border-bottom:1.5px solid var(--accent);
  padding:0 10px 6px 0; font-weight:400; }
.fs td{ padding:7px 10px 7px 0; border-bottom:1px solid var(--line-soft); vertical-align:top;
  line-height:1.44; }
.fs td:last-child{ font-family:var(--mono); font-size:12px; line-height:1.42; color:var(--deep);
  text-align:left; width:50%; }
.fs h2{ margin-top:20px; }
.fsrow{ break-inside:avoid; border-bottom:1px solid var(--line-soft); padding:7px 0 8px; }
.fslab{ font-family:var(--mono); font-size:9px; letter-spacing:.06em; text-transform:uppercase; color:var(--accent); margin:0 0 3px; }
.fsval{ font-size:12.4px; line-height:1.45; }
.fssrc{ font-family:var(--mono); font-size:9.5px; color:var(--deep); margin:2px 0 0; }
.fsflip{ font-size:11.5px; font-style:italic; color:var(--muted); margin:2px 0 0; }
.renew{ background:var(--panel); border-top:2.5px solid var(--accent);
  padding:9px 14px 11px; margin:0 0 14px; }
.renew .lcap{ padding:0 0 4px; font-family:var(--mono); font-size:8px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--accent); }
.renew p{ margin:0; font-size:12px; line-height:1.5; text-align:left; white-space:normal; }
.renew b{ font-family:var(--mono); font-size:12px; color:var(--deep); }

/* ── the pocket card: two 3.25in panels, cut and fold ─────────────────────── */
.card{ width:6.5in; margin:14px auto 0; border:1px solid var(--ink); display:grid;
  grid-template-columns:3.25in 3.25in; box-sizing:border-box; }
.card .panel{ box-sizing:border-box; padding:12px; width:3.25in; min-height:4.5in; }
.card .panel + .panel{ border-left:1px dashed var(--muted); }
.card h3{ font-family:var(--mono); font-size:9px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--accent); margin:0 0 8px; font-weight:700; }
.card ul{ margin:0 0 9px; padding:0; list-style:none; }
.card li{ font-size:12px; line-height:15px; margin:0 0 5px; text-align:left; }
.card li b{ font-family:var(--mono); font-size:11px; color:var(--deep); }
.cardnote{ font-family:var(--mono); font-size:8.5px; letter-spacing:.05em; color:var(--muted);
  text-transform:uppercase; text-align:center; margin:7px 0 0; }

/* ── refusals / back matter ───────────────────────────────────────────────── */
.refuse{ margin:0 0 9px; padding-left:0; list-style:none; }
.refuse li{ margin:0 0 9px; font-size:12.4px; line-height:1.55; }
.refuse b{ font-family:var(--display); font-weight:700; font-weight:700; letter-spacing:.02em; color:var(--deep); }

/* ── feather: one notch either side of the base setting ───────────────────── */
.tight p{ line-height:1.60; margin-bottom:8px; }
.tight .verdict p{ line-height:1.47; }
.tight .ledger td{ padding-top:6px; padding-bottom:6px; }
.loose p{ line-height:1.76; margin-bottom:11.5px; }
.loose .verdict p{ line-height:1.62; }
.loose .ledger td{ padding-top:10px; padding-bottom:10px; }
"""
