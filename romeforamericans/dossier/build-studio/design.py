"""design.py — THE CSS. Lives here, not in the assembler (bug log #1).
La Tavola palette (inherited from romeforamericans.json), page-spec geometry (page-spec.md),
flow fragmentation rules (d-draw.md/layout.md). Fonts embedded as base64 by the assembler.
Token substitution via .replace('@k@', v) — NOT %-format (CSS + base64 contain literal %).
"""

PALETTE = dict(
    paper="#F6EEDB", ink="#2B241A", accent="#8A3324", gilt="#C9A84C",
    muted="#7A6B4E", soft="#9C8C6B", line="#DED0AF", line_soft="#E7DCC0",
    zone="#E9DEC2", stone="#E3D6B4", deep="#6E241D", water="#CFD8CE",
)

def css(font_face_block):
    c = PALETTE
    s = font_face_block + r"""
:root{
  --paper:@paper@; --ink:@ink@; --accent:@accent@; --gilt:@gilt@;
  --muted:@muted@; --soft:@soft@; --line:@line@; --line-soft:@line_soft@;
  --zone:@zone@; --stone:@stone@; --deep:@deep@; --water:@water@;
  --display:'IM Fell English'; --body:'Sorts Mill Goudy'; --mono:'IBM Plex Mono';
}
*{ box-sizing:border-box; }
@page{ size:8.5in 11in; margin:1.02in 0 1.0in 0; }
html,body{ margin:0; padding:0; background:var(--paper); color:var(--ink);
  -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ font-family:var(--body); }

/* furniture is drawn by the renderer's header/footer template (paper-filled) */


/* ---------- FIXED PAGE (page-spec.md: body inset 92/82/72/82) ---------- */
.page{
  width:8.5in; position:relative; overflow:hidden;
  background:var(--paper); padding:0 82px 0 82px;
  page-break-after:always; break-after:page;
  page-break-before:always; break-before:page;
}
.page:last-child{ page-break-after:auto; break-after:auto; }
.page .runhead, .page .folio{ display:none; }
.page .runhead-unused{
  position:absolute; top:40px; left:82px; right:82px; height:34px;
  display:flex; justify-content:space-between; align-items:flex-end;
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; color:var(--muted);
  text-transform:uppercase; border-bottom:.5px solid var(--line);
  padding-bottom:5px;
}
.page .folio{
  position:absolute; bottom:30px; left:82px; right:82px;
  display:flex; justify-content:space-between; align-items:center;
  font-family:var(--mono); font-size:9px; color:var(--muted); letter-spacing:.06em;
}
.page .folio .dot{ color:var(--gilt); }

/* ---------- TYPE HIERARCHY ---------- */
.eyebrow{ font-family:var(--mono); font-size:8px; letter-spacing:.26em;
  text-transform:uppercase; color:var(--accent); margin:0 0 19px 0; }
h1{ font-family:var(--display); font-weight:normal; font-size:39px; line-height:1.06;
  margin:0 0 16px 0; letter-spacing:.005em; }
h1.big{ font-size:44px; }
.standfirst{ font-family:var(--display); font-style:italic; font-size:17px; line-height:1.4;
  color:var(--ink); margin:0 0 18px 0; padding-bottom:16px;
  border-bottom:.5px solid var(--line); }
h2{ font-family:var(--mono); font-weight:500; font-size:11px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--accent); margin:26px 0 10px 0; }
h3{ font-family:var(--display); font-weight:normal; font-size:19px; margin:20px 0 8px 0; }

p{ font-size:13.4px; line-height:1.68; margin:0 0 11px 0; text-align:justify;
  hyphens:auto; -webkit-hyphens:auto; }
.prose > p:first-of-type::first-letter, p.dropcap::first-letter{
  font-family:var(--display); font-size:52px; line-height:0.82; float:left;
  padding:6px 8px 0 0; color:var(--accent); }
.lede{ font-size:14px; }
em{ font-style:italic; }
strong{ font-weight:normal; font-family:var(--display); font-style:normal; }
a{ color:var(--accent); text-decoration:none; }

/* ---------- PROVENANCE MARKS ---------- */
.mk{ font-family:var(--mono); font-size:8.5px; letter-spacing:.06em; white-space:nowrap;
  vertical-align:.06em; }
.mk.est{ color:var(--accent); }
.mk.off{ color:var(--deep); }
.mk.sur{ color:var(--muted); }
.mk.vol{ color:var(--gilt); }
.markkey{ font-family:var(--mono); font-size:9px; }

/* ---------- LEDGER TABLE ---------- */
table.ledger{ width:100%; border-collapse:collapse; margin:14px 0; font-size:12px; }
table.ledger caption{ font-family:var(--mono); font-size:8.5px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--muted); text-align:left; margin-bottom:8px; }
table.ledger th{ font-family:var(--mono); font-size:8.5px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--accent); text-align:left; font-weight:500;
  border-bottom:1px solid var(--accent); padding:5px 10px 5px 0; }
table.ledger th.num, table.ledger td.num{ text-align:right; padding-right:0; }
table.ledger td{ padding:6px 10px 6px 0; border-bottom:.5px solid var(--line);
  vertical-align:top; line-height:1.42; }
table.ledger td.num{ font-family:var(--mono); font-size:11px; white-space:nowrap; }
table.ledger tr:last-child td{ border-bottom:none; }
table.ledger .opt{ font-family:var(--display); font-size:13px; }

/* ---------- VERDICT ---------- */
.verdict{ background:var(--zone); border-left:3px solid var(--accent);
  padding:13px 16px; margin:15px 0; font-size:12.8px; line-height:1.56; }
.verdict .lab{ font-family:var(--mono); font-size:8px; letter-spacing:.2em;
  text-transform:uppercase; color:var(--accent); display:block; margin-bottom:5px; }
.verdict strong{ font-family:var(--display); }

/* ---------- FOR/AGAINST ---------- */
.forlist{ display:flex; gap:18px; margin:12px 0; }
.forlist > div{ flex:1; }
.forlist h4{ font-family:var(--mono); font-size:8px; letter-spacing:.16em;
  text-transform:uppercase; margin:0 0 6px 0; }
.forlist .y h4{ color:var(--accent); }
.forlist .n h4{ color:var(--muted); }
.forlist ul{ margin:0; padding:0; list-style:none; }
.forlist li{ font-size:11.6px; line-height:1.44; margin-bottom:5px; padding-left:13px;
  position:relative; text-align:left; }
.forlist li::before{ content:"—"; position:absolute; left:0; color:var(--soft); }

.note{ font-size:11.4px; line-height:1.5; color:var(--muted); margin:12px 0;
  padding:9px 13px; background:var(--line-soft); border-radius:2px; }
.note .mk{ color:var(--gilt); }

.xref{ font-family:var(--mono); font-size:10px; color:var(--muted); }

/* ---------- FIGURES ---------- */
figure{ margin:16px 0; }
figure.map, figure.photo{ margin:18px 0; }
.map svg{ width:100%; height:auto; display:block; }
.map figcaption, .photo figcaption{ font-family:var(--mono); font-size:8px; line-height:1.5;
  color:var(--muted); margin-top:9px; padding-top:7px; border-top:.5px solid var(--line);
  letter-spacing:.02em; }
.map figcaption .fign, .photo figcaption .fign{ color:var(--accent); letter-spacing:.1em; }
.photo img{ width:100%; height:2.55in; object-fit:cover; display:block; border-radius:1px; }
.flow figure.photo{ break-inside:avoid; }

/* ---------- FLOW (layout.md / d-draw.md) ---------- */
.flow{ padding:0 0.95in; }
.flow .runhead{ position:fixed; }  /* furniture via header/footer template on flowed pages */
.flow .dec + .dec{ margin-top:34px; padding-top:2px; }
.flow p{ line-height:1.72; margin-bottom:12px; }
.flow h1, .flow .dnum, .flow .standfirst, .flow h2, .flow h3{ break-after:avoid; }
.flow p:first-of-type{ break-before:avoid; }
.flow table, .flow figure, .flow .forlist, .flow .note, .flow .verdict{ break-inside:avoid; }
.flow .verdict + .forlist{ break-before:avoid; }
.flow p{ orphans:3; widows:3; }
.dnum{ font-family:var(--mono); font-size:8px; letter-spacing:.24em; text-transform:uppercase;
  color:var(--accent); margin:0 0 8px 0; }

/* ---------- CONTENTS ---------- */
.toc{ font-size:12px; }
.toc .row{ display:flex; align-items:baseline; margin:0 0 5px 0; }
.toc .t{ font-family:var(--display); font-size:13px; }
.toc .lead{ flex:1; border-bottom:.5px dotted var(--soft); margin:0 8px 4px 8px; }
.toc .pg{ font-family:var(--mono); font-size:9.5px; color:var(--muted); }
.toc .part{ font-family:var(--mono); font-size:8px; letter-spacing:.2em;
  text-transform:uppercase; color:var(--accent); margin:13px 0 7px 0; }
.toc .part:first-child{ margin-top:0; }

/* wallet card */
.wallet{ border:1.5px solid var(--accent); border-radius:6px; padding:16px 18px; margin:16px 0;
  background:var(--paper); }
.wallet h3{ margin-top:0; color:var(--accent); }
.wallet .row{ display:flex; justify-content:space-between; font-size:12px; padding:5px 0;
  border-bottom:.5px solid var(--line); gap:14px; }
.wallet .row:last-child{ border-bottom:none; }
.wallet .q{ font-family:var(--display); }
.wallet .a{ font-family:var(--mono); font-size:10.5px; text-align:right; color:var(--deep); }

/* field sheet */
.fs h1{ font-size:34px; margin-bottom:12px; margin-top:8px; padding-top:2px; }
.fs .standfirst{ font-size:16px; margin-bottom:15px; padding-bottom:13px; }
.fs h2{ color:var(--deep); margin:16px 0 8px 0; font-size:10.5px; }
.fs table{ width:100%; border-collapse:collapse; font-size:11px; margin:7px 0 4px 0; }
.fs th{ font-family:var(--mono); font-size:8px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--muted); text-align:left; border-bottom:1px solid var(--line); padding:5px 8px 5px 0; }
.fs td{ padding:6px 8px 6px 0; border-bottom:.5px solid var(--line-soft); vertical-align:top; line-height:1.45; }
.fs td.k{ font-family:var(--display); }
.fs td.v{ font-family:var(--mono); font-size:9.5px; color:var(--deep); }
.fs .note{ margin:0 0 16px 0; padding:11px 15px; font-size:11.5px; line-height:1.55; }
.fs-grid{ column-count:2; column-gap:30px; }
.fs-sec{ break-inside:avoid; -webkit-column-break-inside:avoid; margin-bottom:16px; display:inline-block; width:100%; }
.fs-sec h2{ margin-top:0; }

/* refusals / back matter */
.refuse{ margin:14px 0; }
.refuse .item{ margin:0 0 13px 0; }
.refuse .no{ font-family:var(--mono); font-size:9px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--accent); }
.refuse .then{ font-size:12.6px; line-height:1.56; }
"""
    for k, v in PALETTE.items():
        s = s.replace("@" + k + "@", v)
    return s
