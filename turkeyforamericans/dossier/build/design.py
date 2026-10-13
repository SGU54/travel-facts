"""THE CSS LIVES HERE — never in build.py (bug log #1).

Geometry is page-spec.md verbatim. Scale and ramp are layout-architect.md §2.
Every vertical value below is on the scale: 6 / 11 / 17 / 22.5 / 34 / 45 / 68.
"""
import json, pathlib

B = json.loads((pathlib.Path(__file__).parent / "assets/brands/turkeyforamericans.json").read_text())
P = B["palette"]

TITLE = B["title"]
SITE = "Turkey for Americans"


def css() -> str:
    return f"""
/* ---------- fonts: FILE URL, never base64 (bug #34) ---------- */
@font-face{{font-family:'Anton';src:url('fonts/anton-latin-400-normal.woff2')format('woff2');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'Gelasio';src:url('fonts/gelasio-latin-400-normal.woff2')format('woff2');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'Gelasio';src:url('fonts/gelasio-latin-400-italic.woff2')format('woff2');font-weight:400;font-style:italic;font-display:block}}
@font-face{{font-family:'Gelasio';src:url('fonts/gelasio-latin-600-normal.woff2')format('woff2');font-weight:600;font-style:normal;font-display:block}}
@font-face{{font-family:'Gelasio';src:url('fonts/gelasio-latin-700-normal.woff2')format('woff2');font-weight:700;font-style:normal;font-display:block}}
@font-face{{font-family:'Space Mono';src:url('fonts/space-mono-latin-400-normal.woff2')format('woff2');font-weight:400;font-style:normal;font-display:block}}
@font-face{{font-family:'Space Mono';src:url('fonts/space-mono-latin-700-normal.woff2')format('woff2');font-weight:700;font-style:normal;font-display:block}}

:root{{
  --paper:{P['paper']}; --ink:{P['ink']}; --read:{P['read']}; --accent:{P['accent']};
  --flag:{P['flag']}; --gilt:{P['gilt']}; --muted:{P['muted']}; --soft:{P['soft']};
  --line:{P['line']}; --line-soft:{P['line_soft']}; --zone:{P['zone']};
  --stone:{P['stone']}; --deep:{P['deep']}; --water:{P['water']};
  --display:'Anton',sans-serif; --body:'Gelasio',Georgia,serif; --mono:'Space Mono',monospace;
  --lead:22.5px;               /* THE baseline. one leading in the whole book. */
}}

/* ---------- the paged page model (page-spec.md, verbatim) ---------- */
@page{{
  size:8.5in 11in;
  margin:92px 82px 72px 82px;
  @top-left{{ content:"{TITLE}" }}
  @top-right{{ content:string(rh, last) }}
  @bottom-left{{ content:"{SITE}" }}
  @bottom-center{{ content:"\\25c6" }}
  @bottom-right{{ content:counter(page) }}
}}
@page cover{{ margin:0;
  @top-left{{content:none}} @top-right{{content:none}}
  @bottom-left{{content:none}} @bottom-center{{content:none}} @bottom-right{{content:none}} }}
@page annex{{ margin:92px 82px 76px 82px; }}
.coverpage{{ page:cover; }}  .fs{{ page:annex; }}

html,body{{ background:var(--paper); -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
.pagedjs_sheet{{ background:var(--paper); }}

/* ONE selector sets the running-head string (bug #35) */
.rh-src{{ string-set: rh content(text);
  display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }}

.pagedjs_margin-top-left .pagedjs_margin-content,
.pagedjs_margin-top-right .pagedjs_margin-content,
.pagedjs_margin-bottom-left .pagedjs_margin-content,
.pagedjs_margin-bottom-center .pagedjs_margin-content,
.pagedjs_margin-bottom-right .pagedjs_margin-content{{
  font-family:var(--mono); font-size:9px; letter-spacing:.14em; color:var(--muted);
  text-transform:uppercase; }}

/* ---------- body ---------- */
body{{ font-family:var(--body); font-size:13.4px; line-height:var(--lead);
  color:var(--read); margin:0; hyphens:auto; }}
p{{ margin:0 0 11px; text-align:justify; orphans:3; widows:3; }}

/* ---------- the opener stack: ONE unkillable container ----------
   paged.js ignores break-after:avoid between siblings across a page break,
   so the eyebrow→H1→standfirst→rule→first-para stack is a single
   break-inside:avoid box instead of five siblings hoping to stay together. */
.opener{{ break-inside:avoid; margin:0 0 22.5px; }}
.eyebrow{{ font-family:var(--mono); font-size:8px; letter-spacing:.26em;
  text-transform:uppercase; color:var(--accent); margin:0 0 19px; }}
h1{{ font-family:var(--display); font-weight:400; font-size:39px; line-height:44px;
  letter-spacing:-.012em; color:var(--ink); margin:0 0 17px; text-transform:none; }}
.standfirst{{ font-family:var(--body); font-style:italic; font-size:17px;
  line-height:26px; color:var(--muted); margin:0 0 17px; }}
.oprule{{ border:0; border-top:1px solid var(--line); margin:0 0 22.5px; }}

/* drop cap: first paragraph of a chapter only */
.dropcap::first-letter{{ font-family:var(--display); font-weight:400; float:left;
  font-size:58px; line-height:45px; padding:2px 6px 0 0; color:var(--accent); }}

/* ---------- H2 is a mono LABEL, visibly subordinate (page-spec) ---------- */
.sub{{ break-inside:avoid; }}          /* H2 + its first paragraph, one box */
h2{{ font-family:var(--mono); font-weight:700; font-size:11px; letter-spacing:.18em;
  text-transform:uppercase; color:var(--accent); margin:34px 0 11px; }}
.sub h2{{ margin-top:0; }}
.subwrap{{ margin-top:34px; }}

/* ---------- marks: apparatus, mono, never in the flow of the sentence ---------- */
.mark{{ font-family:var(--mono); font-size:9px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--muted); white-space:nowrap; }}

/* ---------- ledger ---------- */
table{{ width:100%; border-collapse:collapse; break-inside:avoid;
  margin:17px 0 22.5px; font-size:12px; line-height:19px; }}
thead th{{ font-family:var(--mono); font-size:8px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--muted); text-align:left;
  border-bottom:1px solid var(--ink); padding:0 8px 6px; }}
tbody td{{ padding:6px 8px; border-bottom:1px solid var(--line); vertical-align:top; }}
tbody tr td:first-child{{ color:var(--ink); }}
.ledger-cap{{ font-family:var(--mono); font-size:8px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--accent); margin:22.5px 0 0; }}

/* ---------- the verdict apparatus — never splits ---------- */
.verdict{{ break-inside:avoid; margin:22.5px 0; padding:17px 0 0;
  border-top:2px solid var(--ink); }}
.verdict .call{{ font-family:var(--body); font-weight:600; font-size:15px;
  line-height:24px; color:var(--ink); margin:0 0 11px; text-align:left; }}
.fork{{ break-inside:avoid; margin:11px 0 0; font-size:12.5px; line-height:20px; }}
.fork b{{ font-family:var(--mono); font-size:9px; letter-spacing:.12em;
  text-transform:uppercase; color:var(--accent); font-weight:700; }}
.aside{{ font-style:italic; color:var(--muted); font-size:12px; line-height:20px;
  margin:22.5px 0 0; text-align:left; }}

/* ---------- figures & plates ---------- */
figure{{ margin:22.5px 0; break-inside:avoid; }}   /* NOT flex (bug #15) */
figure img, figure svg{{ display:block; width:100%; height:auto; }}
figcaption{{ font-family:var(--mono); font-size:8px; letter-spacing:.04em;
  line-height:13px; color:var(--muted); margin:10px 0 0; padding-top:6px;
  border-top:1px solid var(--line); }}
figcaption b{{ color:var(--accent); font-weight:700; letter-spacing:.12em;
  text-transform:uppercase; }}
.photo img{{ width:100%; }}
.photo.closing img{{ height:4.35in; object-fit:cover; }}

/* ---------- lists: the kit card & the marks legend ---------- */
.kit{{ break-inside:avoid; text-align:left; margin:0 0 11px; padding-left:28px;
  text-indent:-28px; }}
.kitnum{{ font-family:var(--mono); font-weight:700; font-size:9px; color:var(--accent);
  letter-spacing:.08em; display:inline-block; width:28px; text-indent:0; }}
.legend{{ break-inside:avoid; text-align:left; margin:0 0 11px; padding-left:110px;
  text-indent:-110px; }}
.legend .mark{{ display:inline-block; width:102px; text-indent:0; color:var(--accent); }}

/* ---------- flow & chapter breaks ---------- */
.flow .chap{{ break-before:page; }}
.flow .chap:first-child{{ break-before:auto; }}
.endmark{{ font-family:var(--mono); font-size:11px; color:var(--accent);
  margin:22.5px 0 0; }}

/* ---------- front matter / TOC ---------- */
.fm{{ break-before:page; }}
.toc{{ list-style:none; padding:0; margin:22.5px 0 0; }}
.toc li{{ display:flex; align-items:baseline; gap:8px; margin:0 0 11px;
  font-size:12.5px; }}
.toc .t{{ font-family:var(--body); color:var(--ink); }}
.toc .d{{ flex:1; border-bottom:1px dotted var(--line); transform:translateY(-3px); }}
.toc .n{{ font-family:var(--mono); font-size:10px; color:var(--muted); }}
.toc a{{ text-decoration:none; color:inherit; }}
.toc a::after{{ content:target-counter(attr(href), page); }}

/* ---------- the cover ---------- */
.coverpage{{ position:relative; width:8.5in; height:11in; overflow:hidden;
  background:var(--paper); break-after:page; }}
.coverpage svg{{ position:absolute; top:0; left:0; width:8.5in; height:11in; }}

/* ---------- the annex (Field Sheet) ---------- */
.fs{{ break-before:page; }}
.fs h1{{ font-size:34px; line-height:38px; }}
.fs .dated{{ font-family:var(--mono); font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--accent); margin:0 0 22.5px; }}
"""
