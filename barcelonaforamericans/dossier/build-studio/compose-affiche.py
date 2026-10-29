# -*- coding: utf-8 -*-
"""compose-affiche.py — the whole of *Barcelona, Without the Traps.* in the hand of
Marta Serra (L'AFFICHE), from dossier3.raw.html.

Her rules (atelier/references/directors/marta-serra-affiche.md):
  · a decision opens on a POSTER: a field of red or gold, the call as a number or a
    word (build/briefs.md, "The posters"), the verdict at the foot;
  · an essay opens on a PAPER poster: its thesis sentence (the standfirst, verbatim)
    at 64px, one phrase in red, no number; a tool opens on a poster that IS the tool;
  · then a text page — Archivo 800 condensed title, one 340px ragged column, the
    ledger as a stack at the right, the forks under it; no boxes, rules only;
  · then the photograph page: one frame, full bleed to 740px, the chapter's last
    paragraph and the volatile note under it;
  · map chapters give the map a page of its own with the ledger as a ribbon;
  · one family (Archivo), red #A23520 and gold #E0A828 as fields, paper, ink, grey.
The words are the book's. The only lines she writes are the poster glosses, which
restate the ledger's picks (briefs.md), and the labels.

Usage: python3 compose-affiche.py   (after build-html.py; writes dossier3.html)
"""
import json, re, os, html as H
from bs4 import BeautifulSoup, NavigableString
import marta2   # Marta Serra, Season II: the decision posters draw their verdict (owner, 2026-10-25)

BUILD = os.path.dirname(os.path.abspath(__file__)); os.chdir(BUILD)
RAW = 'dossier3.raw.html' if os.path.exists('dossier3.raw.html') else 'dossier3.html'
doc = open(RAW, encoding='utf-8').read()
import writer; doc = writer.write(doc)   # the writer's answers to Ruth's filings (studio 2026-10-25)
briefs = json.load(open('briefs.json', encoding='utf-8'))

# ── the posters (briefs.md, "The posters") ─────────────────────────────────────
POSTERS = {}
for m in re.finditer(r'^\| (d\d\d) \| ([^|]+?) \| ([^|]+?) \|$', open('briefs.md', encoding='utf-8').read(), re.M):
    POSTERS[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
FIELD = {'d01': 'gold', 'd02': 'red', 'd03': 'gold', 'd05': 'red', 'd06': 'red', 'd07': 'gold', 'd08': 'red'}
GIANT = {'d01': 'font-size:150px;font-stretch:80%', 'd02': 'font-size:230px;font-stretch:88%', 'd03': 'font-size:330px',
         'd05': 'font-size:330px', 'd06': 'font-size:330px', 'd07': 'font-size:118px;font-stretch:76%', 'd08': 'font-size:210px;font-stretch:92%'}
PICKS = {'d01': {0}, 'd02': {0, 1}, 'd03': {0, 1, 2, 3}, 'd05': {0, 1, 2, 3}, 'd06': {0, 1, 2}, 'd07': {0}, 'd08': {0, 1, 2, 3}}
# the red phrase on an essay's paper poster — a phrase of the standfirst, verbatim
RED = {'contract': 'how to think about Barcelona', 'howto': 'five marks', 'ground': 'four small times',
       'fly': 'in deadline order', 'dayzero': 'the first six', 'timing': 'only one of those three',
       'setpieces': 'the order of operations', 'horizons': 'Only two things genuinely bind', 'risk': 'in the wrong direction',
       'back': 'leaves to you and to the day', 'then': 'they disappear from the trip', 'fail': 'grouped by what they cost you',
       'beforeyoubook': 'in the order they bind', 'plan': 'keep the order between them'}
# the sentence at the poster's foot: the chapter's briefed pull (verbatim)
def pull_of(sid):
    b = briefs['chapters'].get(sid, {})
    if b.get('hero', {}).get('type') == 'pull': return b['hero']['text']
    if b.get('pull'): return b['pull']['text']
    r = b.get('reserve') or []
    return r[0]['text'] if r else ''
def reserve_of(sid, skip=''):
    b = briefs['chapters'].get(sid, {})
    return [r['text'] for r in (b.get('reserve') or []) if r['text'] != skip]
def readwith_of(sid):
    b = briefs['chapters'].get(sid, {})
    return [m['html'] for m in (b.get('margin') or []) if m.get('k') == 'Read with']

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = r'''
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w300-wd100.ttf');font-weight:300;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w400-wd100-Italic.ttf');font-weight:400;font-stretch:100%;font-style:italic;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w400-wd100.ttf');font-weight:400;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w500-wd100.ttf');font-weight:500;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w600-wd100.ttf');font-weight:600;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w700-wd100.ttf');font-weight:700;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w700-wd92-Italic.ttf');font-weight:700;font-stretch:92%;font-style:italic;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w700-wd92.ttf');font-weight:700;font-stretch:92%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd100.ttf');font-weight:800;font-stretch:100%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd118.ttf');font-weight:800;font-stretch:118%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd76.ttf');font-weight:800;font-stretch:76%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd80.ttf');font-weight:800;font-stretch:80%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd88.ttf');font-weight:800;font-stretch:88%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd92.ttf');font-weight:800;font-stretch:92%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd62.ttf');font-weight:800;font-stretch:62%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd66.ttf');font-weight:800;font-stretch:66%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd84.ttf');font-weight:800;font-stretch:84%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd96.ttf');font-weight:800;font-stretch:96%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w800-wd110.ttf');font-weight:800;font-stretch:110%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w900-wd88.ttf');font-weight:900;font-stretch:88%;font-style:normal;}
@font-face{font-family:'Archivo';src:url('models/fonts/archivo-static/Archivo-w900-wd92.ttf');font-weight:900;font-stretch:92%;font-style:normal;}
/* static instances cut from the variable font at the exact coordinates the book uses (2026-10-24): Chromium embeds a named TrueType instead of Type3 */
@font-face{font-family:'Symbols';src:url('assets/fonts/NotoSansSymbols2-Regular.ttf');}
@font-face{font-family:'Plex';src:url('models/fonts/archivo-static/Archivo-w400-wd100.ttf');font-weight:400;}
@font-face{font-family:'Public';src:url('models/fonts/archivo-static/Archivo-w400-wd100.ttf');font-weight:400;}
@font-face{font-family:'Anton';src:url('models/fonts/archivo-static/Archivo-w400-wd100.ttf');font-weight:400;}
:root{ --paper:#F4F2EC; --ink:#17201C; --red:#A23520; --gold:#E0A828; --blue:#0E6390; --grey:#6B7773; --line:#17201C; --hair:#D9D6CE; --mono:'Archivo'; --sans:'Archivo'; --body:'Archivo'; --display:'Archivo'; }
@page{ size:8.5in 11in; margin:92px 82px 72px 82px;
  @top-left{ content:none } @top-right{ content:none } @bottom-center{ content:none }
  @bottom-left{ content:"Barcelona, Without the Traps."; font-family:'Archivo'; font-size:8.5px; font-weight:500; letter-spacing:.06em; color:var(--grey); }
  @bottom-right{ content:counter(page); font-family:'Archivo'; font-weight:700; font-size:10px; color:var(--ink); } }
@page poster{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
@page annex{ margin:72px 82px 60px 82px; }
html,body{ background:var(--paper); -webkit-print-color-adjust:exact; print-color-adjust:exact; margin:0; }
.pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Archivo'; font-size:11px; line-height:17px; color:var(--ink); }
.rh-src{ string-set:rh content(text); display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }
section{ break-before:page; } section.cont{ break-before:auto; }
.pg{ break-before:page; } .pg.first{ break-before:auto; }
i.mk{ font-style:normal; font-family:'Symbols'; font-size:.9em; color:var(--red); font-weight:400; font-stretch:100%; }   /* no synthetic bold: a synthesised glyph embeds as Type3 */
.fsnote{ font-family:'Archivo'; font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); }
a{ color:inherit; text-decoration:none; }
/* ── posters ── */
.poster{ page:poster; width:8.5in; height:11in; box-sizing:border-box; padding:64px 82px 60px; position:relative; overflow:hidden; display:flex; flex-direction:column; break-before:page; }
.poster.red{ background:var(--red); color:var(--paper); } .poster.gold{ background:var(--gold); color:var(--ink); } .poster.paper{ background:var(--paper); color:var(--ink); }
.poster .slug{ font-size:9px; font-weight:600; letter-spacing:.22em; text-transform:uppercase; display:flex; justify-content:space-between; }
.poster .slug .lab{ color:var(--red); } .poster.red .slug .lab{ color:var(--paper); }
.poster .giant{ font-weight:800; font-stretch:118%; line-height:.8; letter-spacing:-.045em; margin:34px 0 0 -6px; }
.poster .under{ font-size:14px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; margin-top:18px; }
.poster .foot{ margin-top:auto; display:grid; grid-template-columns:1fr 300px; column-gap:40px; align-items:end; }
.poster .foot.rule{ border-top:3px solid var(--ink); padding-top:12px; }
.poster .big{ font-size:30px; line-height:33px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; }
.poster .foot p{ margin:0; font-size:12px; line-height:17px; font-weight:400; }
.poster.red .foot p{ color:#F8E9E3; }
.thesis{ font-weight:800; font-stretch:88%; font-size:60px; line-height:58px; letter-spacing:-.035em; margin-top:110px; }
.thesis.long{ font-size:50px; line-height:49px; margin-top:90px; }
.thesis em{ font-style:normal; color:var(--red); }
/* ── cover ── */
.cover .title{ font-weight:800; font-stretch:88%; font-size:112px; line-height:.86; letter-spacing:-.045em; margin:60px 0 0 -4px; }
.cover .title b{ color:var(--gold); font-weight:800; }
.cover .sub{ font-size:17px; line-height:23px; font-weight:400; width:470px; margin-top:34px; }
.cover .meta{ margin-top:auto; font-size:11px; line-height:17px; border-top:3px solid var(--paper); padding-top:12px; display:grid; grid-template-columns:1fr 1fr; column-gap:40px; }
.cover .meta b{ font-weight:700; }
.cover .stamp{ display:inline-block; border:2px solid var(--paper); padding:5px 10px; font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; margin-top:40px; }
.cover .bar{ display:flex; justify-content:space-between; font-size:9px; font-weight:600; letter-spacing:.2em; text-transform:uppercase; margin-top:20px; }
/* ── photograph page ── */
.photo{ page:poster; width:8.5in; height:11in; box-sizing:border-box; position:relative; overflow:hidden; display:flex; flex-direction:column; break-before:page; }
.photo img{ display:block; width:100%; height:740px; object-fit:cover; }
.photo .tail{ padding:28px 82px 0; display:grid; grid-template-columns:340px 1fr; column-gap:48px; }
.photo .tail.one{ grid-template-columns:1fr; }
.photo .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-bottom:10px; }
.photo p{ margin:0 0 9px; } .photo .tail.two p{ font-size:10.5px; line-height:15px; }
.vol{ border-top:3px solid var(--red); padding-top:8px; }
.vol .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.vol p{ font-size:10px; line-height:14px; } .vol .x{ color:var(--grey); }
/* ── text pages ── */
h1{ font-weight:800; font-stretch:88%; font-size:58px; line-height:.92; letter-spacing:-.035em; margin:0 0 14px; }
.sf{ font-weight:300; font-size:15.5px; line-height:21px; width:430px; margin:0 0 26px; }
.grid{ display:grid; grid-template-columns:340px 264px; column-gap:48px; align-items:start; }
.prose p, p.t{ margin:0 0 11px; text-align:left; hyphens:auto; width:340px; }
.prose p:first-child::first-line, p.t.lede::first-line{ font-weight:600; }
.aside{ float:right; clear:right; width:264px; margin:0 0 20px 48px; }
.join{ border-top:3px solid var(--gold); margin-top:16px; padding-top:8px; break-inside:avoid; } .pg > .join{ width:400px; }   /* on a map page the join keeps the reading measure */
.join .lab{ display:block; font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--red); margin-bottom:5px; } .join p{ font-size:11px; line-height:15px; margin:0; }
.xr{ border-top:3px solid var(--red); break-inside:avoid; margin-bottom:18px; }
.xr .lab{ font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; padding:12px 0 4px; color:var(--red); }
.xr .it{ display:grid; grid-template-columns:34px 1fr; padding:9px 0 10px; border-bottom:1px solid var(--line); color:inherit; text-decoration:none; }
.xr .n{ font-size:17px; line-height:19px; font-weight:800; color:var(--red); font-stretch:92%; }
.xr .t{ font-size:13px; line-height:16px; font-weight:700; letter-spacing:-.01em; font-stretch:92%; }
h2{ font-size:19px; line-height:21px; font-weight:800; font-stretch:92%; letter-spacing:-.02em; margin:14px 0 10px; padding-top:10px; border-top:3px solid var(--ink); width:340px; break-after:avoid; }
h3{ font-size:14px; line-height:17px; font-weight:700; letter-spacing:-.01em; font-stretch:92%; margin:12px 0 5px; width:340px; break-after:avoid; }
.stack{ border-top:3px solid var(--line); break-inside:avoid; }
.stack .it{ padding:10px 0 11px; border-bottom:1px solid var(--line); }
.stack .opt{ font-size:19px; line-height:21px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; }
.stack .it.pick .opt::before{ content:''; display:inline-block; width:11px; height:11px; background:var(--red); margin:0 8px 1px 0; }
.stack .sub{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:3px; }
.stack .v{ font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; margin-top:5px; }
.stack .it.pick .v{ color:var(--red); }
.stack .lab{ font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; padding:6px 0 2px; }
.stack.sm .opt{ font-size:14px; line-height:16px; } .stack.sm .it{ padding:7px 0 8px; }
.forks{ margin-top:22px; border-top:3px solid var(--line); break-inside:avoid; }
.forks .it{ padding:10px 0 11px; border-bottom:1px solid var(--line); }
.forks .q{ font-size:16px; line-height:18px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; margin-bottom:4px; }
.forks p{ margin:0; font-size:10px; line-height:14px; }
.sideq{ border-top:3px solid var(--red); padding-top:10px; margin-bottom:22px; break-inside:avoid; }
.sideq .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:6px; }
.sideq .big19{ font-size:19px; line-height:22px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; }
.sideq p{ margin:6px 0 0; font-size:10px; line-height:14px; color:var(--grey); }
.keyline{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:16px; border-top:1px solid var(--hair); padding-top:8px; }
.note{ border-top:3px solid var(--red); padding-top:8px; margin-top:22px; width:340px; }
.note .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.note p{ margin:0; font-size:10px; line-height:14px; } .note .x{ color:var(--grey); }
.mapwrap{ break-inside:avoid; } .mapwrap svg{ display:block; width:100%; height:auto; }
.mapwrap .cap, figure.fig figcaption, figure.band figcaption{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
.ribbon{ display:grid; grid-template-columns:repeat(4,1fr); column-gap:24px; border-top:3px solid var(--line); margin-top:18px; }
.ribbon.n5{ grid-template-columns:repeat(5,1fr); column-gap:16px; }
.ribbon .it{ padding:10px 0 0; } .ribbon .it + .it{ border-left:1px solid var(--line); padding-left:14px; margin-left:-12px; }
.ribbon .opt{ font-size:15px; line-height:17px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; }
.ribbon.n5 .opt{ font-size:13px; line-height:15px; }
.ribbon .sub{ font-size:9px; line-height:12px; color:var(--grey); margin-top:4px; }
.ribbon .v{ font-size:8.5px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; margin-top:5px; }
.ribbon .it.pick .v{ color:var(--red); } .ribbon .it.pick .opt::before{ content:''; display:inline-block; width:10px; height:10px; background:var(--red); margin:0 7px 0 0; }
figure{ margin:0; }
figure.band{ margin:22px 0 0; break-inside:avoid; } figure.band img{ display:block; width:100%; height:262px; object-fit:cover; }
figure.fig{ margin:14px 0 22px; break-inside:avoid; } figure.fig svg{ display:block; width:100%; height:auto; }
figure.fig.half{ width:340px; }
/* lists (the checklist, the questions) */
.li{ width:340px; margin:0 0 10px; padding-left:0; }
.cols2{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; clear:both; } .cols2 h2, .cols2 .li{ width:auto; } .cols2 h2{ margin-top:0; grid-column:1 / -1; }   /* desk 2026-10-25, Marta → Brunner p14: the heading spans both lists */
.li .dl{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; display:block; margin-bottom:2px; }
.li p{ margin:0; }
/* failure modes */
.fails{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; }
.fail{ break-inside:avoid; padding:6px 0 7px; border-bottom:1px solid var(--line); }
.fail .head{ display:block; font-size:13px; line-height:15px; font-weight:700; letter-spacing:-.01em; font-stretch:92%; margin-bottom:3px; }
.fail p{ margin:0; font-size:10px; line-height:14px; } .fail em{ font-style:normal; color:var(--red); font-weight:700; font-size:9px; letter-spacing:.08em; }
h2.th{ width:auto; margin-top:14px; } h2.th b{ color:var(--red); font-weight:800; }
.tiers{ margin-top:50px; }
.tier{ border-top:3px solid var(--ink); padding:18px 0 26px; display:grid; grid-template-columns:200px 1fr; column-gap:30px; align-items:start; }
.tier .n{ font-weight:800; font-stretch:118%; font-size:150px; line-height:.8; letter-spacing:-.05em; color:var(--red); }
.tier .h{ font-size:30px; line-height:32px; font-weight:800; letter-spacing:-.025em; font-stretch:88%; margin-top:14px; }
.tier .k{ font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
/* before you book */
.seven{ margin-top:36px; }
.seven .it{ display:grid; grid-template-columns:70px 1fr 40px; column-gap:16px; border-top:3px solid var(--ink); padding:12px 0 14px; align-items:start; }
.seven .n{ font-weight:800; font-stretch:118%; font-size:48px; line-height:.8; letter-spacing:-.04em; color:var(--red); }
.seven .q{ font-size:11px; line-height:14px; font-weight:400; color:var(--grey); }
.seven .c{ font-size:16px; line-height:18px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; margin-top:2px; }
.seven .pn{ font-size:14px; font-weight:800; text-align:right; } .seven .pn a::after{ content:attr(data-page); }
.asks{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; row-gap:6px; margin-top:4px; }
.ask{ border-top:3px solid var(--red); padding-top:8px; margin-bottom:14px; break-inside:avoid; }
.ask .who{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; margin:0 0 6px; }
.ask ul{ margin:0; padding:0; list-style:none; } .ask li{ font-size:11px; line-height:15px; padding:4px 0; border-bottom:1px solid var(--hair); }
.trips{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; }
.trip{ break-inside:avoid; } .trip .tname{ font-size:19px; line-height:21px; font-weight:800; font-stretch:92%; letter-spacing:-.02em; margin:0 0 4px; }
.trip .tassume{ font-size:9.5px; line-height:13px; color:var(--grey); margin:0 0 8px; }
.trip .day{ display:grid; grid-template-columns:44px 1fr; column-gap:10px; border-top:1px solid var(--line); padding:6px 0; }
.trip .day b{ font-weight:800; font-size:18px; line-height:18px; font-stretch:92%; letter-spacing:-.02em; } .trip .day span{ font-size:10px; line-height:14px; }
.trip .twhy{ font-size:10px; line-height:14px; margin:8px 0 0; border-top:3px solid var(--ink); padding-top:6px; }
.fb .it{ display:grid; grid-template-columns:220px 1fr; column-gap:24px; border-top:1px solid var(--line); padding:9px 0 10px; break-inside:avoid; }
.fb .it .w{ font-size:13px; line-height:15px; font-weight:700; font-stretch:92%; letter-spacing:-.01em; } .fb .it .d{ font-size:10.5px; line-height:14px; }
/* contents */
.toc a{ display:grid; grid-template-columns:52px 1fr 40px; column-gap:16px; align-items:baseline; border-top:1px solid var(--line); padding:5px 0 6px; }
.toc a.dec{ border-top-color:var(--red); }
.toc .num{ font-weight:800; font-stretch:118%; font-size:18px; line-height:18px; letter-spacing:-.03em; } .toc a.dec .num{ color:var(--red); }
.toc .t{ font-size:12px; line-height:15px; font-weight:500; } .toc .dots{ display:none; }
.toc a::after{ content:attr(data-page); font-weight:800; font-size:14px; text-align:right; }
.toc a.fs::after{ content:"sheet"; font-size:9px; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:var(--grey); }
/* the plan */
.days{ display:grid; grid-template-columns:repeat(5,1fr); column-gap:10px; margin-top:40px; height:660px; }
.days .d{ padding:14px 12px 16px; display:flex; flex-direction:column; border-top:3px solid var(--ink); }
.days .d.fix{ background:var(--red); color:var(--paper); border-top-color:var(--red); }
.days .n{ font-weight:800; font-stretch:118%; font-size:150px; line-height:.8; letter-spacing:-.05em; margin-left:-4px; }
.days .t{ margin-top:auto; font-size:15px; line-height:17px; font-weight:700; letter-spacing:-.01em; font-stretch:92%; }
.days .k{ font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; margin-top:8px; }
.days .d:not(.fix) .k{ color:var(--grey); }
.dayrow{ display:grid; grid-template-columns:120px 1fr; column-gap:24px; border-top:3px solid var(--ink); padding:16px 0 26px; break-inside:avoid; }
.dayrow.fix{ border-top-color:var(--red); }
.dayrow .n{ font-weight:800; font-stretch:118%; font-size:104px; line-height:.82; letter-spacing:-.05em; }
.dayrow.fix .n{ color:var(--red); }
.dayrow .k{ font-size:9px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--grey); }
.dayrow.fix .k{ color:var(--red); }
.dayrow .h{ font-size:19px; line-height:22px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; margin:3px 0 5px; }
.dayrow p{ margin:0; width:auto; max-width:340px; }   /* desk 2026-10-25, Marta: the day sheet keeps her reading measure, the 340px column */
/* the wallet card */
.rules2{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; border-top:3px solid var(--red); padding-top:12px; margin-bottom:26px; }
.rules2 .big{ font-size:30px; line-height:32px; font-weight:800; letter-spacing:-.025em; font-stretch:88%; }
.rules2 .big b{ color:var(--red); }
.rules2 p{ margin:6px 0 0; font-size:10px; line-height:14px; color:var(--grey); width:auto; }
.wgrid{ display:grid; grid-template-columns:1fr 1fr; column-gap:40px; row-gap:18px; }
.wgrid .stack .it.wl{ display:grid; grid-template-columns:118px 1fr; column-gap:10px; align-items:baseline; padding:6px 0 6px; }
.wgrid .stack .it.wl .opt{ font-size:12px; line-height:15px; } .wgrid .stack .it.wl .v{ margin-top:0; font-size:8.5px; line-height:12px; }
.cards{ display:flex; gap:28px; margin-top:30px; align-items:flex-start; break-inside:avoid; }
.card{ width:324px; height:204px; box-sizing:border-box; outline:1.5px dashed var(--grey); outline-offset:8px; padding:16px 18px; display:flex; flex-direction:column; }
.card.front{ background:var(--red); color:var(--paper); }
.card.front .g{ font-weight:800; font-stretch:118%; font-size:66px; line-height:.82; letter-spacing:-.045em; margin-top:12px; }
.card.front .s{ font-size:12px; line-height:15px; font-weight:700; margin-top:auto; }
.card .tag{ font-size:8.5px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:flex; justify-content:space-between; }
.card.back{ background:#fff; }
.card.back .ln{ display:grid; grid-template-columns:92px 1fr; column-gap:8px; font-size:9.5px; line-height:12.5px; border-top:1px solid var(--hair); padding:3px 0; }
.card.back .ln b{ font-weight:700; } .card.back .ln:first-of-type{ border-top:2px solid var(--ink); margin-top:6px; }
.cut{ font-size:9px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:20px; }
/* the marks key */
.marks .it{ display:grid; grid-template-columns:30px 1fr; column-gap:10px; padding:8px 0 9px; border-bottom:1px solid var(--line); }
.marks .it i.mk{ font-size:20px; line-height:22px; }
.marks .it b{ font-size:12px; font-weight:700; } .marks .it span{ font-size:10px; line-height:14px; display:block; }
/* the field sheet (annex) */
.fs{ page:annex; }
.fs h1{ font-size:44px; margin-bottom:8px; } .fs .sf{ margin-bottom:10px; font-size:13px; line-height:18px; width:520px; }
.fs .fsdate{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; }
.fstable{ width:100%; border-collapse:collapse; font-size:10.5px; margin:4px 0 10px; border-top:3px solid var(--ink); break-inside:avoid; }
.fstable th{ text-align:left; font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); padding:8px 0 6px; border-bottom:1px solid var(--line); }
.fstable td{ padding:4px 10px 4px 0; border-bottom:1px solid var(--hair); vertical-align:top; }
.fstable td.n{ text-align:right; white-space:nowrap; font-weight:700; }
.fs p.note{ width:auto; border:0; font-size:10px; line-height:14px; color:var(--grey); margin:-8px 0 14px; padding:0; }
.fs h2{ width:auto; margin-top:6px; font-size:16px; }
'''

# ── Elias Brunner, the text pages (references/maquettiste/elias-brunner.md) ─────────
# His standing fixes, applied to every build so the faults cannot come back:
#   glyph — real quotes and apostrophes in the text (never in code or styles);
#   runt  — the last two words of a paragraph glued when the last word is short;
#   ladder — hyphenation limited (no break leaving fewer than 3 letters, words under 7 kept whole).
import sys as _sys; _sys.path.insert(0, os.path.expanduser('~/.claude/skills/atelier/scripts'))
from brunner_set import BRUNNER_CSS, brunner_set   # Elias Brunner's standing fixes, shared by every book

# ── helpers ────────────────────────────────────────────────────────────────────
def esc(s): return H.escape(s, quote=False)
def marks(h):
    h = re.sub(r"<span class=['\"]mk \w+['\"]>\s*(&#\d+;|[●◇▲◆◈])\s*(VOLATILE|SURVEYED|ESTABLISHED|OFFICIAL)?\s*</span>", lambda m: '<i class="mk">%s</i>' % H.unescape(m.group(1)), h)
    return h
def inner(el): return marks(el.decode_contents().strip()) if el else ''
def txt(el): return re.sub(r'\s+', ' ', el.get_text(' ', strip=True)) if el else ''
def red(sf, phrase):
    return sf.replace(phrase, '<em>%s</em>' % phrase, 1) if phrase and phrase in sf else sf
def img_src(f): return f.img['src'] if f and f.img else None
def cap_of(f): return re.sub(r'^PL\. \w+\s*', '', txt(f.figcaption)) if f and f.figcaption else ''

SVG_FONTS = {'Plex, monospace': 'Archivo, sans-serif', 'Public, sans-serif': 'Archivo, sans-serif', 'Anton, sans-serif': 'Archivo, sans-serif'}
def recolour(svg, colours, scale=1.25):
    for k, v in colours.items(): svg = svg.replace(k, v)
    for k, v in SVG_FONTS.items(): svg = svg.replace('font-family="%s"' % k, 'font-family="%s"' % v)
    svg = re.sub(r'font-size="([\d.]+)"', lambda m: 'font-size="%.1f"' % (float(m.group(1)) * scale), svg)
    svg = svg.replace('font-family="Archivo, sans-serif" letter-spacing', 'font-family="Archivo, sans-serif" font-weight="600" letter-spacing')
    return svg
MAPCOL = {'#F2F7F5': '#F4F2EC', '#0E6390': '#17201C', '#0B4E70': '#17201C', '#E0A828': '#A23520', '#A23520': '#6B7773', '#5B6B66': '#6B7773', '#D3DED9': '#D9D6CE', '#8FA8A2': '#C9CCC4'}
FIGCOL = {'#F2F7F5': '#F4F2EC', '#0B4E70': '#17201C', '#0E6390': '#17201C', '#E0A828': '#A23520', '#A23520': '#A23520', '#5B6B66': '#6B7773', '#D3DED9': '#D9D6CE', '#8FA8A2': '#C9CCC4', '#1B2622': '#17201C'}
TIMECOL = {'#F2F7F5': '#F4F2EC', '#8FA8A2': '#C9CCC4', '#0E6390': '#6B7773', '#E0A828': '#E0A828', '#A23520': '#A23520', '#1B2622': '#17201C', '#5B6B66': '#6B7773', '#D3DED9': '#D9D6CE'}

def sect(sid): return soup.find('section', id=sid)
soup = BeautifulSoup(doc, 'lxml')
DECNUM, XRTEXT = {}, {}   # read before any chapter is composed (composing decomposes kickers): "Decision 04" → d05
for _x in soup.find_all('section'):
    _k = _x.find(class_='kicker'); _m = re.search(r'Decision\s+(0\d)', _k.get_text(' ') if _k else '')
    if _m and re.match(r'd0\d$', _x.get('id', '')): DECNUM[_m.group(1)] = (_x['id'], _x.h1.get_text(' ', strip=True))
    XRTEXT[_x.get('id')] = _x.get_text(' ')

def photos(sec):
    band = next((f for f in sec.find_all('figure') if f.img and 'band' in (f.get('class') or [])), None)
    wide = next((f for f in sec.find_all('figure') if f.img and 'wide' in (f.get('class') or [])), None)
    svg = next((f for f in sec.find_all('figure') if f.svg), None)
    return band, wide, svg

def flow_items(sec):
    """The chapter's body in order, as (kind, element) — what a text page carries."""
    out = []
    for el in sec.children:
        if isinstance(el, NavigableString): continue
        name = el.name; cls = el.get('class') or []
        if name in ('span', 'h1') or 'kicker' in cls or 'standfirst' in cls: continue
        if name == 'figure': out.append(('svg' if el.svg else 'photo', el)); continue
        if name == 'p': out.append(('p', el)); continue
        if name in ('h2', 'h3'): out.append((name, el)); continue
        if name in ('ul', 'ol'): out.append(('ul', el)); continue
        if name == 'div': out.append((cls[0] if cls else 'div', el)); continue
        if name == 'table': out.append(('table', el)); continue
        if name == 'nav': out.append(('nav', el)); continue
    return out

def poster_essay(sid, sec, lab, thesis_phrase, foot_big, foot_p):
    sf = inner(sec.find(class_='standfirst'))
    long = len(txt(sec.find(class_='standfirst'))) > 150
    return f'''<div class="poster paper" id="{sid}-p"><span class="rh-src">{esc(txt(sec.h1))}</span>
  <div class="slug"><span class="lab">{esc(lab)}</span><span>{esc(txt(sec.h1))}</span></div>
  <div class="thesis{' long' if long else ''}">{red(sf, thesis_phrase)}</div>
  <div class="foot rule"><div class="big">{_pull(foot_big)}</div>{f'<p>{foot_p}</p>' if foot_p else ''}</div>
</div>'''

def _pull(t):   # a pull is a sentence: capital first, and its period
    t = t.strip(); t = t[:1].upper() + t[1:]
    return t if re.search(r'[.?!”’]$', t) else t + '.'
def xr_calls(sid):
    """studio 2026-10-25 (Brunner side → Marta): the decisions this chapter sends the reader to — the margin works"""
    ds = sorted(set(re.findall(r'Decision\s+(0\d)', XRTEXT.get(sid, ''), re.I)))
    ds = [d for d in ds if d in DECNUM and DECNUM[d][0] != sid]
    if not ds: return ''
    return ('<div class="xr"><span class="lab">The calls this chapter decides</span>'
            + ''.join(f'<a href="#{DECNUM[d][0]}-p" class="it"><span class="n">{d}</span><span class="t">{esc(DECNUM[d][1])}</span></a>' for d in ds) + '</div>')
LATER = {}   # sid → the margin items that wait for the next h2 (Marta: the margin runs with the text, not above it)
def aside_of(sid, pulls=True, extra=''):
    parts = []
    for h in readwith_of(sid):
        parts.append(f'<div class="sideq"><span class="lab">Read with</span><div class="big19">{h.split("<br>")[0]}</div><p>{h.split("<br>")[1] if "<br>" in h else ""}</p></div>')
    later = []
    if pulls:
        res = reserve_of(sid, skip=pull_of(sid))[:3]
        if res: parts.append(f'<div class="sideq"><span class="lab">From this chapter</span><div class="big19">{esc(_pull(res[0]))}</div></div>')
        later += [f'<div class="sideq"><span class="lab">From this chapter</span><div class="big19">{esc(_pull(t))}</div></div>' for t in res[1:]]
    xr = xr_calls(sid)
    if xr: later.append(xr)
    parts.append(extra)
    LATER[sid] = later
    return '<div class="aside">%s</div>' % ''.join(parts) if any(parts) else ''

def list_cols(ul):
    """desk 2026-10-25 (Brunner p14 → Marta): a checklist in two columns that read down, balanced
    by length — not a grid that aligns rows and leaves holes beside the long items."""
    items = []
    for li in ul.find_all('li', recursive=False):
        h = marks(li.decode_contents().strip())
        m = re.match(r'\s*<span class="deadline">([^<]*)</span>\s*(?:&nbsp;)?\s*(.*)$', h, re.S)
        items.append(f'<div class="li"><span class="dl">{m.group(1)}</span><p>{m.group(2).strip()}</p></div>' if m else f'<div class="li"><p>{h}</p></div>')
    w = [len(re.sub(r'<[^>]+>', '', x)) + 120 for x in items]
    best = min(range(1, len(items) + 1), key=lambda k: abs(sum(w[:k]) - sum(w[k:]))) if len(items) > 1 else 1
    return f'<div class="cols2"><div>{"".join(items[:best])}</div><div>{"".join(items[best:])}</div></div>'

def list_block(ul):
    out = []
    for li in ul.find_all('li', recursive=False):
        h = marks(li.decode_contents().strip())
        m = re.match(r'\s*<span class="deadline">([^<]*)</span>\s*(?:&nbsp;)?\s*(.*)$', h, re.S)
        if m: out.append(f'<div class="li"><span class="dl">{m.group(1)}</span><p>{m.group(2).strip()}</p></div>')
        else: out.append(f'<div class="li"><p>{h}</p></div>')
    return ''.join(out)

def text_pages(sid, sec, items, aside_html='', fig_cols=None, skip_last=True, lede=True, tail2=False, band_before_h2=None, band_html='', lists2=False):
    """One flowing text page (Paged.js breaks it as needed): h1 + standfirst, the aside
    floated right, then the body in order. The last paragraph is kept for the
    photograph page when skip_last."""
    ps = [i for i, (k, _) in enumerate(items) if k == 'p']
    tail_idx = set(ps[-2:] if tail2 else ps[-1:]) if (skip_last and ps) else set()
    body = []; first = True; nh2 = 0; nul = 0
    for i, (k, el) in enumerate(items):
        if i in tail_idx: continue
        if k == 'p':
            body.append(f'<p class="t{" lede" if first and lede else ""}">{inner(el)}</p>'); first = False
        elif k in ('h2', 'h3'):
            if k == 'h2':
                nh2 += 1
                if band_before_h2 == nh2: body.append(band_html)
            body.append(f'<{k}>{inner(el)}</{k}>')
            if k == 'h2' and LATER.get(sid) and not lists2: body.append(f'<div class="aside">{LATER[sid].pop(0)}</div>')
        elif k == 'ul':
            nul += 1; body.append(list_cols(el) if lists2 else list_block(el))
        elif k == 'svg' and fig_cols is not None:
            cap = txt(el.figcaption)
            body.append(f'<figure class="fig">{recolour(str(el.svg), fig_cols)}<figcaption>{esc(cap)}</figcaption></figure>')
    figs_at = [j for j, x in enumerate(body) if x.startswith('<figure')]
    if LATER.get(sid) and not lists2 and figs_at:   # a figure clears the float: what waits goes beside the prose after it (Rome's lesson, p70)
        body.insert(figs_at[0] + 1, f'<div class="aside">{"".join(LATER[sid])}</div>')
    elif LATER.get(sid) and not lists2 and aside_html.endswith('</div>'):   # no h2 left for them: they join the margin at the top (a float split mid-prose leaves holes)
        aside_html = aside_html[:-6] + ''.join(LATER[sid]) + '</div>'
    LATER[sid] = []   # a two-column checklist runs full width: nothing waits beside it
    sf = sec.find(class_='standfirst')
    tails = [items[i][1] for i in sorted(tail_idx)]
    return f'''<div class="pg first"><h1>{esc(txt(sec.h1))}</h1>{f'<div class="sf">{inner(sf)}</div>' if sf is not None else ''}{aside_html}{''.join(body)}</div>''', tails

def photo_page(src, cap, tail_p_html, vol_html='', pos='50% 50%', duo=None):
    two = bool(vol_html); twop = tail_p_html.count('<p') > 1
    if duo:   # Season II: the decision's closing frame in two inks, its verdict overprinted in gold
        w, size, wd = marta2.WORD[duo]
        return f'''<div class="photo duo"><div class="dw"><img src="{src}" style="object-position:{pos}"><div class="tone"></div><div class="lift"></div><div class="word" style="font-size:{size}px;font-stretch:{wd}%">{esc(w)}</div></div>
  <div class="tail{'' if two else ' one'}{' two' if twop else ''}"><div><div class="cap">{esc(cap)}</div>{tail_p_html}</div>{vol_html}</div>
</div>'''
    return f'''<div class="photo"><img src="{src}" style="object-position:{pos}">
  <div class="tail{'' if two else ' one'}{' two' if twop else ''}"><div><div class="cap">{esc(cap)}</div>{tail_p_html}</div>{vol_html}</div>
</div>'''

def note_block(sec, cls='note'):
    n = sec.find(class_='note')
    if n is None: return ''
    xref = n.find(class_='xref'); x = txt(xref) if xref else ''
    if xref: xref.decompose()
    vol = n.find('span', class_='vol'); isvol = vol is not None
    if vol: vol.decompose()
    sur = n.find('span', class_='sur'); issur = sur is not None and txt(sur).startswith('▲ SURVEYED')
    if issur: sur.decompose()
    body = re.sub(r'^\s*—\s*', '', re.sub(r'\s+', ' ', inner(n))).strip()
    lab = '<i class="mk">◆</i> Volatile · 2026' if isvol else ('<i class="mk">▲</i> Surveyed' if issur else 'Also')
    return f'<div class="{cls}"><span class="lab">{lab}</span><p>{body} <span class="x">{esc(x)}</span></p></div>'

# ── the cover ──────────────────────────────────────────────────────────────────
cv = soup.find(class_='coverpage')
cover = marta2.cover()   # Season II, the whole specimen (owner, 2026-10-25)

OUT = [cover]

# ── essays and tools, in book order ────────────────────────────────────────────
def essay(sid, lab, foot_big=None, foot_p=None, fig_cols=None, photo_src=None, photo_cap=None, pos='50% 50%', band_end=False, pulls=True, aside_extra='', tail2=False, band_before_h2=None, lists2=False):
    sec = sect(sid); band, wide, svg = photos(sec); items = flow_items(sec)
    big = foot_big or esc(pull_of(sid))
    fp = foot_p if foot_p is not None else esc(cap_of(band) if band else '')
    printed_caps = {esc(c) for c in [cap_of(band) if band else '', photo_cap or cap_of(wide if wide else band) if (wide or band) else ''] if c}
    if fp in printed_caps: fp = ''   # studio 2026-10-25 (fidelity TWICE ×4): a caption prints once, under its photograph
    out = [f'<section class="chap" id="{sid}">', poster_essay(sid, sec, lab, RED.get(sid), big, fp)]
    aside = aside_of(sid, pulls=pulls, extra=aside_extra)
    src = photo_src or img_src(wide) or img_src(band)
    band_html = f'<figure class="band" style="clear:both"><img src="{img_src(band)}"><figcaption>{esc(cap_of(band))}</figcaption></figure>' if band else ''
    page, tails = text_pages(sid, sec, items, aside, fig_cols=fig_cols, skip_last=not band_end, tail2=tail2, band_before_h2=band_before_h2, band_html=band_html, lists2=lists2)
    if band_end:
        page = page[:-6] + f'<figure class="band"><img src="{src}" style="object-position:{pos}"><figcaption>{esc(photo_cap or cap_of(band))}</figcaption></figure></div>'
        out.append(page)
    else:
        out.append(page)
        out.append(photo_page(src, photo_cap or cap_of(wide if wide else band), ''.join(f'<p>{inner(t)}</p>' for t in tails), pos=pos))
    out.append('</section>')
    return ''.join(out)

# THE CONTRACT
OUT.append(essay('contract', 'Before anything else'))

# HOW TO READ THIS — the marks key is the instrument, at the right
sec = sect('howto'); mk = sec.find(class_='markskey')
keyrows = ''.join(f'<div class="it"><i class="mk">{txt(r.find(class_="g"))}</i><div><b>{txt(r.find("strong"))}</b><span>{esc(txt(r.find_all("span")[-1]).replace(txt(r.find("strong")), "", 1).strip())}</span></div></div>' for r in mk.find_all(class_='row'))
keystack = f'<div class="stack marks"><span class="lab">Five marks</span>{keyrows}</div>'
mk.decompose()
OUT.append(essay('howto', 'The apparatus', pulls=False, aside_extra=keystack))

# CONTENTS — a paper page, the numbers big, decisions in red
sec = sect('contents'); nav = sec.find('nav')
rows = []
for a in nav.find_all('a'):
    href = a['href']; num = txt(a.find(class_='num')); t = txt(a.find(class_='t'))
    cls = 'dec' if href[1:].startswith('d0') else ('fs' if href == '#fs' else '')
    rows.append(f'<a href="{href if href == "#fs" else href + "-p"}" class="{cls}"><span class="num">{esc(num)}</span><span class="t">{esc(t)}</span></a>')
OUT.append(f'''<section class="chap" id="contents"><div class="pg first"><span class="rh-src">Contents</span><h1>Contents</h1>
  <div class="sf">Seven decisions, scored, between the ground they stand on and the days they produce. Red numbers are the calls.</div>
  <nav class="toc">{''.join(rows)}</nav></div></section>''')

# THE GROUND — Marta's own composition from the sample (m5b), on the raw paragraphs
sec = sect('ground'); G = [inner(p) for p in sec.find_all('p', recursive=False)]
band, wide, svg = photos(sec)
FOUR = [('The tourist tax', "isn't in your room rate", 'at check-out, when you are leaving'),
        ('The airport ticket', "isn't the one your metro card holds", 'at a gate, when you are rushed'),
        ('The dollars prompt', 'offered with a helpful smile', 'at a terminal, when someone is waiting'),
        ('The tourist rate', 'the bright-blue ATM; the tourist-priced table', 'at a table, when you are hungry')]
four = '<div class="stack"><span class="lab">Four small charges, four moods</span>' + ''.join(
    f'<div class="it"><div class="opt">{a}</div><div class="sub">{esc(b)}</div><div class="v" style="color:var(--red)">{esc(c)}</div></div>' for a, b, c in FOUR) + '</div>'
fig1 = '''<svg viewBox="0 0 652 250" xmlns="http://www.w3.org/2000/svg" font-family="Archivo, sans-serif">
<circle cx="190" cy="128" r="128" fill="none" stroke="#17201C" stroke-width="3"/>
<text x="190" y="128" text-anchor="middle" font-size="44" font-weight="800" letter-spacing="-1.5" fill="#17201C">ZONE 1</text>
<text x="190" y="152" text-anchor="middle" font-size="12" fill="#6B7773">metro · bus · tram · funicular · local rail</text>
<text x="190" y="168" text-anchor="middle" font-size="12" fill="#6B7773">one ticket covers essentially everything</text>
<line x1="320" y1="132" x2="530" y2="132" stroke="#A23520" stroke-width="3" stroke-dasharray="9 7"/>
<line x1="402" y1="114" x2="426" y2="150" stroke="#A23520" stroke-width="5"/><line x1="426" y1="114" x2="402" y2="150" stroke="#A23520" stroke-width="5"/>
<text x="414" y="98" text-anchor="middle" font-size="11" font-weight="700" letter-spacing="2" fill="#A23520">T-CASUAL STOPS HERE</text>
<text x="414" y="178" text-anchor="middle" font-size="11" fill="#6B7773">Hola Barcelona · T-usual: through</text>
<circle cx="580" cy="132" r="46" fill="#A23520"/><text x="580" y="141" text-anchor="middle" font-size="26" font-weight="800" fill="#F4F2EC">BCN</text>
<text x="580" y="202" text-anchor="middle" font-size="12" font-weight="700" fill="#17201C">Airport metro</text></svg>'''
h2g = txt(sec.find('h2'))
OUT.append(f'''<section class="chap" id="ground">{poster_essay('ground', sec, 'The organising fact', RED['ground'], esc(pull_of('ground')), 'Everything downstream of this fact is defence: where you sleep, how you sequence the days, what you order at lunch. The calls in this book are the moves that keep the extraction machine from running on you by default.')}
<div class="pg first"><span class="rh-src">The Ground</span><h1>The Ground</h1>
  <div class="aside">{four}<div class="sideq"><span class="lab">Read with Decision 03</span><div class="big19">The Money-Trap Web</div><p>The four extractions, in one place, each with its move (the sums are on the Field Sheet).</p></div></div>
  <p class="t lede">{G[0]}</p><p class="t">{G[1]}</p><p class="t">{G[2]}</p><p class="t">{G[3]}</p></div>
<div class="pg"><div class="aside"><div class="sideq"><span class="lab">If you read one page</span><div class="big19">Decision 03. It is the one we would hand a friend for free.</div></div></div>
  <p class="t">{G[4]}</p>
  <h2 style="width:auto;clear:both">{esc(h2g)}</h2><figure class="fig">{fig1}<figcaption>Fig. 1 — One integrated system, one gap — and the gap is at the airport</figcaption></figure>
  <div class="aside"><div class="sideq"><span class="lab">The rule</span><div class="big19">Check whether the ticket you already hold covers Zone 1 including the airport. If you are on a T-casual, it does not.</div><div class="keyline"><i class="mk">●</i> Established — structural, true for years</div></div></div>
  <p class="t">{G[5]}</p><p class="t">{G[6]}</p></div>
{photo_page(img_src(wide), cap_of(wide), f'<p>{G[7]}</p>')}</section>''')

# BEFORE YOU FLY · DAY ZERO · TIMING · THE SET PIECES
OUT.append(essay('fly', 'The checklist', lists2=True, tail2=True))
OUT.append(essay('dayzero', 'The arrival', pos='50% 40%'))
OUT.append(essay('timing', 'The shape of the year', fig_cols=TIMECOL, tail2=True))
OUT.append(essay('setpieces', 'Order of operations', band_before_h2=2, tail2=True))   # studio: the killed plate freed the column; the tail moves to the Park Güell page

# ── the seven decisions ────────────────────────────────────────────────────────
JOINS = json.load(open('_studio/writer/joins.json', encoding='utf-8'))
def decision(sid):
    sec = sect(sid); band, wide, svg = photos(sec)
    d = {}
    d['kicker'] = txt(sec.find(class_='kicker')); d['title'] = txt(sec.h1); d['sf'] = inner(sec.find(class_='standfirst'))
    t = sec.find('table', class_='ledger'); rows = []
    for tr in t.tbody.find_all('tr'):
        td = tr.find_all('td'); opt = td[0].find(class_='opt'); sub = td[0].find(class_='sub')
        for m in td[0].find_all(class_='mk'): m.decompose()
        rows.append((opt.decode_contents().strip(), re.sub(r'^\s*—\s*', '', txt(sub)) if sub else '', re.sub(r'\s*[●◇▲◆◈]\s*$', '', txt(td[1]))))
    v = sec.find(class_='verdict').p; strong = txt(v.strong); v.strong.decompose(); rest = inner(v)
    forks = []
    for col in sec.find(class_='fa').find_all(class_='col'):
        st = col.p.strong; q = txt(st); st.decompose(); forks.append((q, inner(col.p)))
    paras = [inner(p) for p in sec.find_all('p', recursive=False)]
    word, gloss = POSTERS[sid]; field = FIELD[sid]; picks = PICKS[sid]
    poster = f'''<div class="poster {field}" id="{sid}-p"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span>{esc(d['title'])}</span></div>
  <div class="giant" style="{GIANT[sid]}">{esc(word)}</div>
  <div class="under">{esc(gloss)}</div>
  <div class="foot"><div class="big">{esc(strong)}</div><p>{rest}</p></div>
</div>'''
    if marta2.has(sid): poster = marta2.poster(sid, d['kicker'])
    stack = '<div class="stack%s"><span class="lab">%s</span>' % (' sm' if len(rows) > 4 else '', esc(txt(t.caption))) + ''.join(
        f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{o}</div><div class="sub">{esc(s)}</div><div class="v">{esc(c)}</div></div>' for i, (o, s, c) in enumerate(rows)) + '</div>'
    fk = '<div class="forks">' + ''.join(f'<div class="it"><div class="q">{esc(q)}</div><p>{p}</p></div>' for q, p in forks) + '</div>'
    note = note_block(sec, 'vol')
    # studio 2026-10-26 (owner + Ruth M9): the join the free guides never make, beside the forks
    jn = next((j for j in JOINS if j['section_id'] == sid), None)
    JN = f'<div class="join"><span class="lab">What the free guides never connect</span><p>{esc(jn["text"])}</p></div>' if jn else ''
    out = [f'<section class="chap decision" id="{sid}">', poster]
    if svg is not None and sid in ('d01', 'd07'):   # a map chapter: the map page with the ribbon, then text + band
        cols = MAPCOL.copy()
        ribbon = f'<div class="ribbon{" n5" if len(rows) > 4 else ""}">' + ''.join(
            f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{o}</div><div class="sub">{esc(s)}</div><div class="v">{esc(c)}</div></div>' for i, (o, s, c) in enumerate(rows)) + '</div>'
        cap = txt(svg.figcaption).split('·', 1)[-1].strip()
        cap = re.sub(r'\bin gold\b', 'in red', cap)   # the map is recoloured: gold is printed red (desk 2026-10-25: the caption said both)
        out.append(f'<div class="pg"><div class="mapwrap">{re.sub(r"\b(IN|in) (GOLD|gold)\b", lambda m: m.group(1) + (" RED" if m.group(2).isupper() else " red"), recolour(str(svg.svg), cols, 1.5))}<div class="cap">{esc(cap)}</div></div>{ribbon}{JN}</div>')
        src = img_src(wide) or img_src(band)
        if sid in ('d01', 'd07'):
            bh = 262 if sid == 'd01' else 186
            out.append(f'''<div class="pg"><h1>{esc(d['title'])}</h1><div class="sf">{d['sf']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in paras)}</div><div>{fk}{note.replace('class="vol"', 'class="note"')}</div></div>
  <figure class="band"><img src="{src}" style="height:{bh}px;object-position:50% 40%"><figcaption>{esc(cap_of(wide or band))}</figcaption></figure></div>''')
        else:
            out.append(f'''<div class="pg"><h1>{esc(d['title'])}</h1><div class="sf">{d['sf']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in paras[:-1])}</div><div>{fk}</div></div></div>''')
            out.append(photo_page(src, cap_of(wide or band), f'<p>{paras[-1]}</p>', note, pos='50% 50%'))
    else:
        src = img_src(band) or img_src(wide)
        fig = ''
        if sid == 'd03':
            f = next(f for f in sec.find_all('figure') if f.svg)
        out.append(f'''<div class="pg"><h1>{esc(d['title'])}</h1><div class="sf">{d['sf']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in paras[:-1])}</div><div>{stack}{fk}</div></div></div>''')
        out.append(photo_page(src, cap_of(band or wide), f'<p>{paras[-1]}</p>', note + JN, pos='50% 45%', duo=sid if sid in marta2.WORD else None))
    out.append('</section>')
    return ''.join(out)

for sid in ('d01', 'd02', 'd03', 'd05', 'd06', 'd07', 'd08'):
    OUT.append(decision(sid))

# THE HORIZONS · RISK
OUT.append(essay('horizons', 'What to book, and when', fig_cols=FIGCOL, tail2=True))
OUT.append(essay('risk', 'Risk, calibrated', band_before_h2=3))

# THE PLAN — the poster is the tool (five days as five columns), then the day sheet
sec = sect('plan'); P = [inner(p) for p in sec.find_all('p', recursive=False)]
band, wide, svg = photos(sec)
DAYS = [(1, True, 'Sagrada, then the old city', 'Booked · fixed'), (2, True, 'Park Güell, then downhill', 'Booked · fixed'),
        (3, False, 'Market, hill, sea', 'Floats · absorbs overflow'), (4, True, 'The day trip, a full clear day', 'Booked · fixed'),
        (5, False, 'No agenda: the city itself', 'Floats')]
h3s = [txt(h) for h in sec.find_all('h3')]
cols = ''.join(f'<div class="d{" fix" if f else ""}"><div class="n">{n}</div><div class="t">{esc(t)}</div><div class="k">{esc(k)}</div></div>' for n, f, t, k in DAYS)
rows = ''.join(f'<div class="dayrow{" fix" if f else ""}"><div class="n">{n}</div><div><div class="k">{esc(k)}</div><div class="h">{esc(h3s[n-1].split(" — ", 1)[1][:1].upper() + h3s[n-1].split(" — ", 1)[1][1:])}</div><p>{P[n + 1]}</p></div></div>' for n, f, t, k in DAYS)
RULES = ['Keep the morning anchor on day one, whatever it is.', 'Keep the day trip whole and mid-week.', 'Keep at least one day with nothing in it.']
rules = '<div class="stack"><span class="lab">Three rules that survive any substitution</span>' + ''.join(f'<div class="it pick"><div class="opt">{esc(r)}</div></div>' for r in RULES) + '</div>'
h2p = txt(sec.find('h2'))
OUT.append(f'''<section class="chap" id="plan"><div class="poster paper" id="plan-p"><span class="rh-src">The Plan</span>
  <div class="slug"><span class="lab">The days as operations</span><span>The Plan</span></div>
  <div class="days">{cols}</div>
  <div class="foot"><div class="big">Three anchors, two free days — the shape, not the list.</div><p>It assumes five days, an Eixample base and the two bookings made. Substitute freely inside a day; keep the order between them.</p></div>
</div>
<div class="pg first"><h1>The Plan</h1><div class="sf">{inner(sec.find(class_='standfirst'))}</div>
  <div class="grid"><div class="prose"><p>{P[0]}</p><p>{P[1]}</p></div><div>{rules}</div></div>
  <figure class="band" style="margin-top:14px"><img src="{img_src(band)}"><figcaption>{esc(cap_of(band))}</figcaption></figure></div>
<div class="pg">{rows}</div>
{photo_page(img_src(wide), cap_of(wide), f'<h2 style="margin-top:0;padding-top:0;border:0;width:auto">{esc(h2p)}</h2><p>{P[7]}</p><p>{P[8]}</p>')}</section>''')

# FAILURE MODES — the poster is the three tiers; the page is the list in two columns
sec = sect('fail'); band, wide, svg = photos(sec)
tiers = [('Costs you money', 'recoverable · annoying · compounding'), ('Costs you a day', 'unrecoverable · one of five'), ('Costs the trip’s shape', 'unrecoverable · colours everything')]
groups = []; cur = None
for k, el in flow_items(sec):
    if k == 'h2': cur = [txt(el), []]; groups.append(cur)
    elif k == 'fail' and cur: cur[1].append(el)
counts = [len(g[1]) for g in groups]
tiers_html = ''.join(f'<div class="tier"><div class="n">{c}</div><div><div class="h">{esc(t)}</div><div class="k">{esc(k)}</div></div></div>' for (t, k), c in zip(tiers, counts))
intro = inner(sec.find('p', recursive=False))
fails = ''.join(f'<h2 class="th"><b>{c}</b> &nbsp;{esc(t)}</h2><div class="fails">' + ''.join(
    f'<div class="fail"><span class="head">{inner(f.find(class_="head"))}</span><p>{inner(f.p)}</p></div>' for f in items) + '</div>' for (t, items), c in zip(groups, counts))
OUT.append(f'''<section class="chap" id="fail"><div class="poster paper" id="fail-p"><span class="rh-src">Failure Modes</span>
  <div class="slug"><span class="lab">Organised by consequence</span><span>Failure Modes</span></div>
  <div class="tiers">{tiers_html}</div>
  <div class="foot rule"><div class="big">{esc(txt(sec.find(class_='standfirst')))}</div><p>A website of separate articles cannot sort mistakes this way. That is the point of a book.</p></div>
</div>
<div class="pg first"><h1>Failure Modes</h1><p class="t lede" style="width:430px">{intro}</p>{fails}</div>
{photo_page(img_src(wide), cap_of(wide), f'<p>{esc(cap_of(band))}</p>')}</section>''')

# THE WALLET CARD — the card itself, cut line and all
sec = sect('wallet'); w = sec.find(class_='wallet'); groups = []; cur = None
for el in w.children:
    if isinstance(el, NavigableString): continue
    if el.name == 'h3': cur = [txt(el), []]; groups.append(cur)
    elif el.name == 'div' and cur is not None: cur[1].append((txt(el.find(class_='k')), txt(el.find(class_='v'))))
wg = ''.join('<div class="stack"><span class="lab">%s</span>%s</div>' % (esc(h), ''.join(f'<div class="it wl"><div class="opt">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in ls)) for h, ls in groups)
BACK = [('Card / ATM', 'charge in EUROS, always'), ('Cash', 'a bank machine, not the blue one'), ('Airport metro', 'T-casual no · Hola / T-usual OK'),
        ('Lunch', 'menú del día, weekdays 1–4pm'), ('Dinner', 'from ~8:30pm'), ('Rice', 'cooked to order, 20+ min'), ('Apartment', 'HUTB number, or skip it')]
OUT.append(f'''<section class="chap" id="wallet"><div class="pg first" id="wallet-p"><span class="rh-src">The Wallet Card</span><h1>The Wallet Card</h1>
  <div class="sf">{inner(sec.find(class_='standfirst'))}</div>
  <div class="rules2"><div><div class="big">Say <b>euros</b> at every terminal.</div></div><div><div class="big">A <b>T-casual</b> will not open the airport gate.</div><p>A Hola Barcelona or a T-usual will.</p></div></div>
  <div class="wgrid" data-air="Marta: the two lists end where their facts end; the short column's air is mine">{wg}</div>
  <div class="cards"><div class="card front"><div class="tag"><span>Barcelona</span><span>Without the Traps</span></div><div class="g">EUROS.</div><div class="s">At every terminal. And a T-casual will not open the airport gate.</div></div>
    <div class="card back"><div class="tag" style="color:var(--red)"><span>The street card</span><span>2026</span></div>{''.join(f'<div class="ln"><b>{esc(k)}</b><span>{esc(v)}</span></div>' for k, v in BACK)}</div></div>
  <div class="cut">Cut along the dashed line, fold in two, keep it behind your card.</div></div></section>''')

# WHAT THIS WON'T TELL YOU · BARCELONA, THEN
OUT.append(essay('back', 'The honest edges', band_end=True))
sec = sect('then'); band, wide, svg = photos(sec); T = [inner(p) for p in sec.find_all('p', recursive=False)]
OUT.append(f'''<section class="chap" id="then">{poster_essay('then', sec, 'A last word', RED['then'], esc(txt(sec.find_all('p', recursive=False)[-1])), esc(cap_of(band)))}
{photo_page(img_src(band), cap_of(band), f'<p>{T[0]}</p><p>{T[1]}</p>', pos='50% 50%')}</section>''')

# BEFORE YOU BOOK — the poster is the seven calls; then the questions, the shapes, the fallbacks
sec = sect('beforeyoubook'); band, wide, svg = photos(sec)
t = sec.find('table', class_='ledger'); seven = []
for i, tr in enumerate(t.tbody.find_all('tr')):
    td = tr.find_all('td'); a = td[2].find('a')
    seven.append(f'<div class="it"><div class="n">0{i+1}</div><div><div class="q">{esc(txt(td[0]))}</div><div class="c">{esc(txt(td[1]))}</div></div><div class="pn"><a href="{a["href"]}-p"></a></div></div>')
t.decompose()
items = flow_items(sec); body = []; asks = []; trips = []
def flush():
    global asks, trips
    if asks: body.append('<div class="asks">' + ''.join(asks) + '</div>'); asks = []
    if trips:
        h = body.pop(); hh = body.pop()   # the paragraph and the heading before the shapes
        body.append('<div style="break-inside:avoid">' + hh + h + '<div class="trips">' + ''.join(trips) + '</div></div>'); trips = []
for k, el in items:
    if k == 'h2': flush(); body.append(f'<h2 style="width:auto;clear:both">{inner(el)}</h2>')
    elif k == 'p': body.append(f'<p class="t" style="width:430px">{inner(el)}</p>')
    elif k == 'askbox': asks.append(f'<div class="ask"><p class="who">{inner(el.find(class_="who"))}</p><ul>{"".join("<li>%s</li>" % inner(li) for li in el.find_all("li"))}</ul></div>')
    elif k == 'trip':
        days = ''.join(f'<div class="day"><b>{esc(txt(tr.find(class_="opt")))}</b><span>{inner(tr.find(class_="sub"))}</span></div>' for tr in el.find_all('tr')[1:])
        trips.append(f'<div class="trip"><p class="tname">{inner(el.find(class_="tname"))}</p><p class="tassume">{inner(el.find(class_="tassume"))}</p>{days}<p class="twhy">{inner(el.find(class_="twhy"))}</p></div>')
    elif k == 'fbwrap':
        flush(); body.append(f'<h2 style="width:auto;clear:both">{inner(el.find("h2"))}</h2><div class="fb">' + ''.join(
            f'<div class="it"><div class="w">{inner(tr.find(class_="opt"))}</div><div class="d">{inner(tr.find(class_="sub"))}</div></div>' for tr in el.find_all('tr')[1:]) + '</div>')
flush()
shapes = next(x for x in body if x.startswith('<div style="break-inside:avoid">')); body.remove(shapes)
shapes += f'<figure class="band"><img src="{img_src(band)}" style="object-position:50% 50%"><figcaption>{esc(cap_of(band))}</figcaption></figure>'
html_b = ''.join(body) + shapes
# Photographs (Hannah, 2026-10-28): every printed frame credited, on the book's last page.
_CR = os.path.join('_studio', 'marta', 'credits.json')
if os.path.exists(_CR):
    _c = json.load(open(_CR, encoding='utf-8'))
    html_b += ('<div class="credits" style="clear:both;margin-top:14px;font-size:8.5px;line-height:11.5px;color:#5a5048"><b>Photographs.</b> '
               + ' · '.join(f'{esc(e["what"])}: {esc(e["author"])} ({esc(e["platform"])})' for e in _c)
               + '. Unsplash and Pexels photographs under their own licences, read 28 October 2026.</div>')
OUT.append(f'''<section class="chap" id="beforeyoubook"><div class="poster paper" id="beforeyoubook-p"><span class="rh-src">Before you book</span>
  <div class="slug"><span class="lab">Before you book</span><span>Decide these first</span></div>
  <div class="seven">{''.join(seven)}</div>
  <div class="foot" style="margin-top:28px"><div class="big" style="font-size:19px;line-height:22px">{esc(txt(sec.find(class_='standfirst')))}</div></div>
</div>
<div class="pg first"><h1>Decide these first</h1>{html_b}</div></section>''')

# THE FIELD SHEET — the annex, in the same hand
sec = sect('fs')
fsb = []
for k, el in flow_items(sec):
    if k == 'p' and 'first' in (el.get('class') or []): fsb.append(f'<p class="t" style="width:560px;font-size:10.5px;line-height:15px">{inner(el)}</p>')
    elif k == 'p': fsb.append(f'<p class="note">{inner(el)}</p>')
    elif k == 'h2': fsb.append(f'<h2>{inner(el)}</h2>')
    elif k == 'table': fsb.append(marks(str(el)).replace('&#9670;', '<i class="mk">◆</i>').replace('&#9650;', '<i class="mk">▲</i>').replace('◆', '<i class="mk">◆</i>').replace('▲', '<i class="mk">▲</i>').replace('<i class="mk"><i class="mk">', '<i class="mk">').replace('</i></i>', '</i>'))
OUT.append(f'''<section class="chap fs" id="fs"><div class="pg first"><span class="rh-src">The Field Sheet</span><h1>The Field Sheet</h1>
  <div class="sf">{inner(sec.find(class_='standfirst'))}</div>{''.join(fsb)}</div></section>''')

html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Barcelona, Without the Traps.</title>
<style>{CSS}</style></head><body>
{''.join(OUT)}
</body></html>'''
html = html.replace('<style>' + CSS + '</style>', '<style>' + CSS + marta2.CSS + marta2.DUO_CSS + BRUNNER_CSS + '</style>', 1)
html = brunner_set(html)
import marta_pics; html = marta_pics.apply(html)   # Marta's picture edit, from her ledger
from studio import studio
html = studio(html)   # the studio of three: Marta's rulings on Brunner's proof + US house style
html = html.replace("<span class='mk vol'>&#9670; VOLATILE</span> — ", '').replace('<p class="note">◆ VOLATILE', '<p class="note"><i class="mk">◆</i> VOLATILE')
open('dossier3.html', 'w', encoding='utf-8').write(html)
print('composed dossier3.html in the Affiche hand:', len(html), 'bytes;', html.count('class="poster'), 'posters,', html.count('class="photo"'), 'photo pages')
