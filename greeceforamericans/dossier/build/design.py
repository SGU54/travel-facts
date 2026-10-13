# -*- coding: utf-8 -*-
"""design.py — THE CSS. Single source of truth (bug #1: never put CSS in build.py).

Implements the paged page model verbatim from page-spec.md, tokenised to the
greeceforamericans print palette (brand.json). One baseline (22.5px), one spacing
scale, one type ramp — the overlay test in layout-architect.md must hold.
"""

# palette (from brand.json — Aegean whitewash, translated for ink on warm paper)
PAPER="#F4EFE6"; INK="#1E2A32"; ACCENT="#1C6E8C"; GILT="#C6A15B"
MUTED="#6E7B82"; SOFT="#94A0A6"; LINE="#DCD3C4"; LINE_SOFT="#E7DFD1"
ZONE="#E8E0D0"; STONE="#E0E6E4"; DEEP="#144E63"; WATER="#CFE0E4"; WIND="#B9CDD2"

FONTDIR = "fonts"

def css():
    return f"""
/* ============ FONTS (by file URL — never base64; bug #34) ============ */
@font-face{{font-family:'Cormorant';src:url('{FONTDIR}/CormorantGaramond-SemiBold.ttf') format('truetype');font-weight:600;font-style:normal;font-display:block}}
@font-face{{font-family:'Cormorant';src:url('{FONTDIR}/CormorantGaramond-Medium.ttf') format('truetype');font-weight:500;font-style:normal;font-display:block}}
@font-face{{font-family:'Cormorant';src:url('{FONTDIR}/CormorantGaramond-Regular.ttf') format('truetype');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'Cormorant';src:url('{FONTDIR}/CormorantGaramond-MediumItalic.ttf') format('truetype');font-weight:500;font-style:italic;font-display:block}}
@font-face{{font-family:'Spectral';src:url('{FONTDIR}/Spectral-Regular.ttf') format('truetype');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'Spectral';src:url('{FONTDIR}/Spectral-Medium.ttf') format('truetype');font-weight:500;font-style:normal;font-display:block}}
@font-face{{font-family:'Spectral';src:url('{FONTDIR}/Spectral-SemiBold.ttf') format('truetype');font-weight:600;font-style:normal;font-display:block}}
@font-face{{font-family:'Spectral';src:url('{FONTDIR}/Spectral-Light.ttf') format('truetype');font-weight:300;font-style:normal;font-display:block}}
@font-face{{font-family:'Spectral';src:url('{FONTDIR}/Spectral-Italic.ttf') format('truetype');font-weight:400;font-style:italic;font-display:block}}
@font-face{{font-family:'PlexMono';src:url('{FONTDIR}/IBMPlexMono-Regular.ttf') format('truetype');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'PlexMono';src:url('{FONTDIR}/IBMPlexMono-Medium.ttf') format('truetype');font-weight:500;font-style:normal;font-display:block}}
@font-face{{font-family:'PlexMono';src:url('{FONTDIR}/IBMPlexMono-SemiBold.ttf') format('truetype');font-weight:600;font-style:normal;font-display:block}}

:root{{
  --paper:{PAPER}; --ink:{INK}; --accent:{ACCENT}; --gilt:{GILT};
  --muted:{MUTED}; --soft:{SOFT}; --line:{LINE}; --line-soft:{LINE_SOFT};
  --zone:{ZONE}; --stone:{STONE}; --deep:{DEEP}; --water:{WATER}; --wind:{WIND};
  --display:'Cormorant'; --body:'Spectral'; --mono:'PlexMono';
}}

/* ============ THE PAGED PAGE MODEL (page-spec.md verbatim) ============ */
@page{{
  size:8.5in 11in;
  margin:92px 82px 72px 82px;
  @top-left{{ content:"Greece, in Order." }}
  @top-right{{ content:string(rh, last) }}
  @bottom-left{{ content:"Greece for Americans" }}
  @bottom-center{{ content:"\\2693" }}   /* anchor */
  @bottom-right{{ content:counter(page) }}
}}
@page cover{{ margin:0;
  @top-left{{content:none}} @top-right{{content:none}}
  @bottom-left{{content:none}} @bottom-center{{content:none}} @bottom-right{{content:none}} }}
@page annex{{ margin:92px 82px 76px 82px; }}
.coverpage{{ page:cover; }} .fs{{ page:annex; }}

html,body{{ background:var(--paper); -webkit-print-color-adjust:exact; print-color-adjust:exact;
  margin:0; padding:0; color:var(--ink); }}
.pagedjs_sheet{{ background:var(--paper); }}
.pagedjs_pagebox{{ background:var(--paper); }}

/* ONE selector sets the running-head string (bug #35) */
.rh-src{{ string-set: rh content(text);
  display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; padding:0; }}

/* furniture typography */
.pagedjs_margin-top-left .pagedjs_margin-content,
.pagedjs_margin-top-right .pagedjs_margin-content{{
  font-family:var(--mono); font-size:9px; letter-spacing:.16em; color:var(--muted);
  text-transform:uppercase; }}
.pagedjs_margin-top-right .pagedjs_margin-content{{ color:var(--accent); }}
.pagedjs_margin-bottom-left .pagedjs_margin-content,
.pagedjs_margin-bottom-right .pagedjs_margin-content{{
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; color:var(--muted); }}
.pagedjs_margin-bottom-center .pagedjs_margin-content{{
  font-family:var(--mono); font-size:10px; color:var(--gilt); }}

/* ============ THE FLOW ============ */
.flow{{ font-family:var(--body); font-size:13.4px; line-height:22.5px; color:var(--ink);
  font-weight:400; text-rendering:optimizeLegibility; }}
.flow .chap{{ break-before:page; }}
.flow .chap:first-child{{ break-before:avoid; }}
.flow .dec + .dec{{ margin-top:22.5px; }}

/* headings never strand at a page foot */
.flow h1, .flow .dnum, .flow .standfirst, .flow h2{{ break-after:avoid; }}
.flow h2 + p, .flow .standfirst + p{{ break-before:avoid; }}

/* never split across the fold */
.flow table, .flow figure, .flow .forlist, .flow .note, .flow .verdict,
.flow .ledger, .flow .aside{{ break-inside:avoid; }}
.flow .verdict + .forlist{{ break-before:avoid; }}
.flow p{{ orphans:3; widows:3; margin:0 0 11px 0; text-align:justify;
  hyphens:auto; -webkit-hyphens:auto; }}
.flow p:last-child{{ margin-bottom:0; }}

/* ============ THE OPENER STACK (fixed composition) ============ */
.eyebrow{{ font-family:var(--mono); font-size:8px; letter-spacing:.26em; text-transform:uppercase;
  color:var(--accent); margin:0 0 22.5px 0; font-weight:500; }}
h1.t{{ font-family:var(--display); font-weight:600; font-size:41px; line-height:44px;
  color:var(--ink); margin:0 0 17px 0; letter-spacing:-.005em; }}
.standfirst{{ font-family:var(--display); font-weight:500; font-style:italic; font-size:17.5px;
  line-height:25px; color:var(--deep); margin:0 0 17px 0; padding-bottom:17px;
  border-bottom:1px solid var(--line); }}
/* drop cap — first paragraph of a chapter only */
.chap > .body-first::first-letter, p.dropcap::first-letter{{
  font-family:var(--display); font-weight:600; float:left; font-size:64px; line-height:46px;
  padding:2px 9px 0 0; color:var(--accent); }}

/* ============ HEADINGS INSIDE A CHAPTER ============ */
h2.s{{ font-family:var(--mono); font-weight:600; font-size:11px; letter-spacing:.15em;
  text-transform:uppercase; color:var(--deep); margin:34px 0 11px 0; }}
h3.s{{ font-family:var(--display); font-weight:600; font-size:19px; line-height:24px;
  color:var(--ink); margin:22.5px 0 6px 0; }}

/* ============ STANDALONE (sub-)section within a flowed chapter ============ */
.dec .lead{{ margin-top:0; }}

/* ============ PROVENANCE MARKS (seasoning; writing-code.md) ============ */
.mk{{ font-family:var(--mono); font-size:8.5px; letter-spacing:.06em; white-space:nowrap;
  font-weight:500; }}
.mk.est{{ color:var(--accent); }}   /* STRUCTURAL / geography */
.mk.stb{{ color:var(--deep); }}     /* STABLE / ordering holds */
.mk.off{{ color:var(--gilt); }}     /* OFFICIAL */
.mk.sur{{ color:var(--muted); }}    /* SURVEYED */
.mk.vol{{ color:var(--soft); }}     /* VOLATILE (rare in book body) */

/* ============ THE VERDICT (the boxed call) ============ */
.verdict{{ background:var(--zone); border-left:2.5px solid var(--accent);
  padding:17px 20px 17px 20px; margin:22.5px 0 0 0; }}
.verdict .vlead{{ font-family:var(--display); font-weight:600; font-size:17px; line-height:22.5px;
  color:var(--deep); margin:0 0 6px 0; }}
.verdict p{{ font-family:var(--body); font-size:12.5px; line-height:19px; margin:0;
  text-align:left; color:var(--ink); }}
.verdict .vq{{ font-family:var(--mono); font-size:8px; letter-spacing:.22em; text-transform:uppercase;
  color:var(--accent); display:block; margin:0 0 8px 0; }}

/* ============ THE LEDGER (data table) ============ */
.ledger{{ margin:17px 0 0 0; width:100%; border-collapse:collapse; }}
.led-h{{ font-family:var(--mono); font-size:8px; letter-spacing:.18em; text-transform:uppercase;
  color:var(--soft); padding-bottom:8px; border-bottom:1px solid var(--line); text-align:left;
  font-weight:500; }}
.led-h.r{{ text-align:right; }}
.ledger td{{ padding:7px 10px 7px 0; border-bottom:1px solid var(--line-soft); line-height:1.42;
  font-size:12px; vertical-align:top; }}
.ledger td.r{{ text-align:right; font-family:var(--mono); font-size:11px; color:var(--deep);
  white-space:nowrap; }}
.ledger td.k{{ font-family:var(--body); font-weight:600; color:var(--ink); width:31%; }}
.ledger tr:last-child td{{ border-bottom:none; }}

/* ============ ASIDE / NOTE / PULL ============ */
.aside{{ background:var(--stone); padding:14px 17px; margin:22.5px 0 0 0; font-size:11.3px;
  line-height:18.5px; color:var(--ink); }}
.aside .at{{ font-family:var(--mono); font-size:8px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--deep); display:block; margin-bottom:7px; font-weight:600; }}
.note{{ font-size:11px; line-height:18.3px; color:var(--muted); margin:17px 0 0 0;
  padding-left:14px; border-left:2px solid var(--line); }}
.pull{{ font-family:var(--display); font-weight:500; font-style:italic; font-size:20px;
  line-height:26px; color:var(--accent); margin:22.5px 0; padding:0; text-align:left; }}

/* ============ FORLIST (failure modes, checklists) ============ */
.forlist{{ margin:11px 0 0 0; padding:0; list-style:none; }}
.forlist li{{ position:relative; padding:0 0 11px 20px; font-size:12.6px; line-height:19px; }}
.forlist li::before{{ content:"\\2013"; position:absolute; left:0; color:var(--accent);
  font-family:var(--mono); }}
.forlist li b{{ font-family:var(--body); font-weight:600; color:var(--deep); }}
.forlist.num{{ counter-reset:fm; }}
.forlist.num li{{ padding-left:26px; }}
.forlist.num li::before{{ counter-increment:fm; content:counter(fm,decimal-leading-zero);
  font-family:var(--mono); font-size:9px; color:var(--soft); top:2px; }}

/* ============ FIGURES ============ */
.map, .photo{{ margin:11px 0 22.5px 0; break-inside:avoid; }}
.map svg{{ width:100%; display:block; border:1px solid var(--line-soft); background:var(--paper); }}
.photo img{{ width:100%; display:block; border:1px solid var(--line-soft); }}
.photo.wide img{{ height:3.3in; object-fit:cover; }}
.photo.band img{{ height:2.35in; object-fit:cover; }}
.photo.closing img{{ height:4.35in; object-fit:cover; }}
.map figcaption, .photo figcaption{{ font-family:var(--body); font-size:7.5px; line-height:1.6;
  color:var(--muted); margin-top:8px; padding-top:6px; border-top:1px solid var(--line-soft); }}
.fign{{ font-family:var(--mono); color:var(--accent); letter-spacing:.16em; font-size:7.5px; }}
/* a fed CLOSING map: the chapter's final page reads as a designed figure plate,
   not a stranded fragment. Generous vertical rhythm fills the tail. */
.map.closing{{ margin:45px 0 0 0; padding:34px 0 0 0; border-top:1px solid var(--line); break-inside:avoid; }}
.map.closing svg{{ border:1px solid var(--line); min-height:3.4in; }}
.map.closing figcaption{{ font-size:8.5px; margin-top:15px; padding-top:11px; line-height:1.7; }}

/* ============ ENDMARK (closes a section — spends the whitespace) ============ */
.endmark{{ text-align:center; margin:22.5px 0 0 0; color:var(--gilt); font-size:13px;
  font-family:var(--mono); }}
.endmark::before{{ content:"\\2693"; }}   /* the anchor — the book's device */
.chap.loose .flow-inner{{ }}

/* feathering notches (±1 from baseline; applied per chapter by the renderer) */
.chap.tight{{ }}
.chap.tight p{{ line-height:22px; margin-bottom:10px; }}
.chap.tight .photo.wide img{{ height:3.05in; }}
.chap.loose p{{ line-height:24px; }}

/* ============ COVER (full bleed, unfurnished) ============ */
.coverpage{{ position:relative; width:8.5in; height:11in; margin:0; padding:0; overflow:hidden;
  background:var(--paper); }}
.coverpage svg{{ position:absolute; top:0; left:0; width:8.5in; height:11in; display:block; }}

/* ============ FRONT MATTER (contract, how-to-read, contents) ============ */
.fm h1.t{{ font-size:37px; }}
.toc{{ margin:13px 0 0 0; width:100%; border-collapse:collapse; }}
.toc td{{ padding:3.5px 0; font-size:11.5px; line-height:1.3; border-bottom:1px solid var(--line-soft);
  vertical-align:baseline; }}
.toc td.n{{ font-family:var(--mono); font-size:8.5px; color:var(--accent); width:26px; }}
.toc td.pg{{ text-align:right; font-family:var(--mono); font-size:9.5px; color:var(--muted);
  width:34px; }}
.toc td.pg::before{{ content:target-counter(attr(href url), page); }}
.toc .part td{{ font-family:var(--mono); font-size:7.5px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--soft); padding-top:9px; padding-bottom:2px; border-bottom:none; }}
.toc a{{ color:var(--ink); text-decoration:none; }}

/* marks legend row */
.marklist{{ list-style:none; margin:11px 0 0 0; padding:0; }}
.marklist li{{ font-size:12px; line-height:22.5px; padding-left:0; }}
.marklist .mk{{ display:inline-block; min-width:150px; }}

/* small caps helper */
.sc{{ font-variant:small-caps; letter-spacing:.03em; }}
.lead{{ font-size:13.4px; }}
"""
