# -*- coding: utf-8 -*-
"""compose-edition.py — the whole of *Rome, Solved.* in the hand of Clàudia Ferrer
(L'ÉDITION), from rome-book.json (extract-rome.py) and the Field Sheet PDF.

Her rules (atelier/references/directors/claudia-ferrer-edition.md), in La Tavola's palette:
  · a chapter OPENS on its photograph, in colour, to the trim; under it the section
    label, the title in Fraunces, the standfirst in Newsreader italic, and for a
    decision IN SHORT — the call — in the right column;
  · the body runs in two columns of Newsreader with a Fraunces drop cap on the lede;
    the ledger sits in a TINTED SIDEBAR inside the flow; figures run at the full
    measure with a bold-lead caption; plates close a chapter;
  · the forks are italic questions; the volatile note is a ruled footer line;
  · tools (contents, checklist, cards, failure tiers, the wallet card, decide-these-
    first, the Field Sheet) keep the same faces and the tint, set as the magazine's
    service pages: labels in DM Sans, rows ruled, nothing boxed.
The words are the book's. Figure labels are the book's, at their printed positions.

Usage: python3 compose-edition.py   (writes dossier3.html; then render-edition.py)
"""
import json, re, os, html as H
import pymupdf

BUILD = os.path.dirname(os.path.abspath(__file__)); os.chdir(BUILD)
CH = json.load(open('rome-book.json', encoding='utf-8'))
BY = {c['id']: c for c in CH}
# Owner's review 2026-10-25: photographs replaced in this edition (source files untouched).
#  d07 opened on a SIM-card photo inherited from the shipped book -> the card reader;
#  the wallet card took that card reader -> coffee and coins; Termini carried white bands baked into the file -> trimmed.
# d01's shipped ledger heads named three columns over two ('WALK TO CORE · CHARACTER · PRICE'
# above "base — character" and the walk time): label the two that exist.
for _c in CH:
    if _c['id'] == 'd01':
        for _b in _c.get('blocks', []):
            if _b.get('t') == 'ledger' and _b.get('heads') == ['WALK TO CORE', 'CHARACTER', 'PRICE']: _b['heads'] = ['BASE · CHARACTER', 'WALK TO CORE']
#  Also inherited from the shipped book: d09 (Ostia vs Pompeii) opened on Florence -> Ostia Antica;
#  'Where to stay' opened on a Bangkok hostel -> Rome rooftops.
PHOTO_SWAP = {'img/p29-0.jpeg': 'img/d07-card-reader.jpeg', 'img/p58-0.jpeg': 'img/wallet-coins.jpeg', 'img/p20-0.jpeg': 'img/termini-trim.jpeg',
              'img/p34-0.jpeg': 'img/d09-ostia.jpeg', 'img/p41-0.jpeg': 'img/stay-rooftops.jpeg'}
for _c in CH:
    for _b in _c.get('blocks', []):
        if _b.get('t') == 'photo' and _b.get('src') in PHOTO_SWAP: _b['src'] = PHOTO_SWAP[_b['src']]
FS_PDF = '/Users/sg54/travel-sites/_etsy/rome/files/rome-solved-FieldSheet.pdf'

def esc(s): return H.escape(s, quote=False)
def unspace(t):
    if re.fullmatch(r'(?:\S ?)+', t) and ' ' in t and all(len(w) <= 1 for w in t.split(' ')):
        return t.replace('  ', '\x00').replace(' ', '').replace('\x00', ' ')
    return t
WORDS = ['COSTS','YOU','THE','TRIP','OR','A','WHOLE','DAY','MONEY','GOOD','MEAL','MARKS','AS','TOURIST','COMFORT','BASE','YOU’LL','REGRET',
         'WHAT','TO','ASK','BEFORE','PAY','TWO','TRIPS','THAT','FOLLOW','CALLS','WHEN','PLAN','DOES','NOT','SURVIVE','GETTING','IN','FROM',
         'FIUMICINO','PASSES','&','TRANSIT','SIGHTS','SELL','OUT','GROUND','DECISIONS','CITY','BACK','MATTER','ANNEX','CONTENTS','CHAPTER','BOOK',',']
def nice(t):
    """Letterspaced caps as extracted ('T H E G R O U N D') → words, by greedy segmentation over the book's vocabulary."""
    flat = t.replace(' ', ''); out = []; i = 0
    while i < len(flat):
        for w in sorted(WORDS, key=len, reverse=True):
            if flat.startswith(w, i): out.append(w); i += len(w); break
        else: out.append(flat[i]); i += 1
    s = ' '.join(out).replace(' ,', ',').replace('YOU ’ LL', 'YOU’LL')
    return re.sub(r'\s+', ' ', s).strip()

CSS = r'''
@font-face{font-family:'Fraunces';src:url('models/fonts/Fraunces.ttf');font-weight:100 900;}
@font-face{font-family:'Fraunces';src:url('models/fonts/Fraunces-Italic.ttf');font-weight:100 900;font-style:italic;}
@font-face{font-family:'Newsreader';src:url('models/fonts/Newsreader.ttf');font-weight:200 800;}
@font-face{font-family:'Newsreader';src:url('models/fonts/Newsreader-Italic.ttf');font-weight:200 800;font-style:italic;}
@font-face{font-family:'DM';src:url('models/fonts/DMSans.ttf');font-weight:100 1000;}
@font-face{font-family:'Symbols';src:url('assets/fonts/NotoSansSymbols2-Regular.ttf');}
:root{ --paper:#EFE4CC; --ink:#2B241A; --grey:#6A5C42; --sect:#8A3324; --tint:#E4D6B8; --gold:#C9A94A; --red:#8A3324; --line:#D8C7A4;
  --mono:'DM'; --sans:'DM'; --body:'Newsreader'; --display:'Fraunces'; }
@page{ size:8.5in 11in; margin:92px 82px 72px 82px;
  @top-left{ content:"Rome, Solved."; font-family:'DM'; font-size:8px; font-weight:500; letter-spacing:.16em; text-transform:uppercase; color:var(--grey); }
  @top-right{ content:string(rh, last); font-family:'DM'; font-size:8px; font-weight:500; letter-spacing:.16em; text-transform:uppercase; color:var(--sect); }
  @bottom-left{ content:"Rome for Americans"; font-family:'Fraunces'; font-style:italic; font-size:9px; color:var(--grey); }
  @bottom-center{ content:none }
  @bottom-right{ content:counter(page); font-family:'DM'; font-weight:600; font-size:9px; color:var(--ink); } }
@page opener{ @top-left{content:none} @top-right{content:none} }
@page cover{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
@page annex{ margin:72px 82px 60px 82px; }
html,body{ background:var(--paper); -webkit-print-color-adjust:exact; print-color-adjust:exact; margin:0; }
.pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Newsreader'; font-size:11px; line-height:16px; color:var(--ink); font-variation-settings:'opsz' 12; }
.rh-src{ string-set:rh content(text); display:block; height:0; overflow:hidden; font-size:0; line-height:0; margin:0; }
i.mk{ font-style:normal; font-family:'Symbols'; font-size:.9em; color:var(--sect); font-weight:400; }
a{ color:inherit; text-decoration:none; }
section{ break-before:page; }
.pg{ break-before:page; } .pg.first{ break-before:auto; } .op{ page:opener; }
/* ── cover ── */
.pagedjs_cover_page .pagedjs_sheet{ background:linear-gradient(180deg, rgba(43,36,26,.15) 0%, rgba(43,36,26,0) 35%, rgba(43,36,26,.72) 100%), url('img/p03-0.jpeg') 50% 60% / cover no-repeat #2B241A; }
.cover{ page:cover; width:816px; height:980px; box-sizing:border-box; padding:52px 82px 0; display:flex; flex-direction:column; overflow:hidden; color:#fff; }
section#cover{ break-before:auto; }
.cover .mast{ display:flex; justify-content:space-between; font-family:'DM'; font-size:9px; font-weight:600; letter-spacing:.24em; text-transform:uppercase; }
.cover .blk{ margin-top:auto; padding-bottom:28px; }
.cover .t{ font-family:'Fraunces'; font-weight:600; font-size:110px; line-height:.9; letter-spacing:-.02em; font-variation-settings:'opsz' 144,'SOFT' 50; }
.cover .s{ font-family:'Newsreader'; font-style:italic; font-size:19px; line-height:25px; margin-top:22px; width:520px; font-variation-settings:'opsz' 18; }
.cover .d{ font-family:'Newsreader'; font-size:12px; line-height:17px; margin-top:18px; width:430px; opacity:.92; }
.cover .foot{ display:flex; justify-content:space-between; font-family:'DM'; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; opacity:.9; }
/* ── openers ── */
.hero{ margin:-92px -82px 0; width:816px; height:600px; overflow:hidden; position:relative; }
.hero img{ width:100%; height:100%; object-fit:cover; display:block; }
.hero .cap{ position:absolute; left:82px; right:82px; bottom:14px; color:#fff; font-family:'DM'; font-size:8.5px; font-weight:500; letter-spacing:.1em; text-transform:uppercase; text-shadow:0 1px 6px rgba(0,0,0,.7); }
.open{ display:grid; grid-template-columns:1fr 201.3px; column-gap:24px; padding-top:26px; align-items:start; }
.open.one{ grid-template-columns:1fr; }
.sect{ font-family:'DM'; font-weight:600; font-size:9px; letter-spacing:.22em; text-transform:uppercase; color:var(--sect); margin:0 0 10px; display:flex; align-items:center; gap:10px; }
.sect::after{ content:''; flex:1; height:1px; background:var(--sect); opacity:.5; }
h1{ font-family:'Fraunces'; font-weight:600; font-size:42px; line-height:.98; letter-spacing:-.015em; margin:0 0 12px; font-variation-settings:'opsz' 144,'SOFT' 50; }
h1.long{ font-size:34px; }
.sf{ font-family:'Newsreader'; font-style:italic; font-size:16px; line-height:22px; margin:0 0 16px; font-variation-settings:'opsz' 18; }
.call{ border-top:2px solid var(--sect); padding-top:8px; margin-top:4px; }
.call .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:7px; }
.call .big{ font-family:'Fraunces'; font-weight:500; font-size:14px; line-height:18px; margin:0 0 7px; font-variation-settings:'opsz' 36,'SOFT' 100; }
.call p{ margin:0; font-size:10.5px; line-height:15px; }
/* ── the body: two columns, Chromium balances each fragment ── */
.body2{ column-count:2; column-gap:24px; }
.body2 p, p.t{ margin:0 0 9px; text-align:justify; hyphens:auto; }
.body2 p.lede::first-letter, p.lede::first-letter{ font-family:'Fraunces'; font-weight:600; font-size:46px; line-height:36px; float:left; padding:3px 6px 0 0; color:var(--sect); font-variation-settings:'opsz' 144,'SOFT' 100; }
.body2 h3, h3{ font-family:'Fraunces'; font-weight:600; font-size:13px; line-height:16px; margin:12px 0 4px; break-after:avoid; font-variation-settings:'opsz' 36; }
.body2 h3 small, h3 small{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--sect); margin-left:8px; }
h2{ font-family:'DM'; font-weight:700; font-size:9.5px; letter-spacing:.22em; text-transform:uppercase; color:var(--sect); margin:18px 0 8px; padding-top:8px; border-top:2px solid var(--sect); break-after:avoid; column-span:all; }
.side{ background:var(--tint); padding:12px 14px 8px; margin:0 0 12px; break-inside:avoid; }
.side .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:8px; }
.side .heads{ display:flex; justify-content:space-between; font-family:'DM'; font-weight:700; font-size:7.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); padding-bottom:4px; }
.side .r{ padding:5px 0 6px; border-top:1px solid rgba(138,51,36,.25); }
.side .opt{ font-family:'Fraunces'; font-weight:600; font-size:11.5px; line-height:14px; font-variation-settings:'opsz' 36; }
.side .sub{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:1px; }
.side .v{ font-family:'DM'; font-weight:700; font-size:8.5px; line-height:12px; letter-spacing:.08em; text-transform:uppercase; margin-top:3px; color:var(--sect); }
figure{ margin:0; }
figure.band{ margin:0 0 14px; break-inside:avoid; } figure.band img{ display:block; width:100%; height:190px; object-fit:cover; }
figure.plate{ margin:14px 0 6px; break-inside:avoid; column-span:all; } figure.plate img{ display:block; width:100%; height:300px; object-fit:cover; }
figure.plate.tall img{ height:420px; }
figcaption{ font-family:'DM'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:6px; }
figcaption b{ color:var(--ink); font-weight:600; }
figure.fig{ margin:8px 0 16px; break-inside:avoid; } figure.fig svg{ display:block; width:100%; height:auto; }
figure.fig svg text{ font-family:'DM'; fill:#2B241A; paint-order:stroke; stroke:#F6EEDB; stroke-width:2.6px; stroke-linejoin:round; }
figure.fig svg text.mono{ font-weight:600; letter-spacing:.06em; }
figure.fig svg text.lab{ font-weight:500; }
.forks{ border-top:1px solid var(--line); padding-top:8px; margin-top:4px; break-inside:avoid; }
.forks .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin:6px 0 5px; }
.forks .q{ font-family:'Fraunces'; font-style:italic; font-weight:500; font-size:11.5px; line-height:14px; margin:0 0 6px; font-variation-settings:'opsz' 36; }
.forks .q b{ font-style:normal; font-family:'DM'; font-weight:600; font-size:9px; color:var(--ink); }
.note{ border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:8px 0; margin-top:8px; font-size:10px; line-height:14px; display:grid; grid-template-columns:96px 1fr; column-gap:14px; break-inside:avoid; }
.note .lab{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--red); }
.note p{ margin:0; text-align:left; } .note .x{ font-style:italic; color:var(--grey); display:block; margin-top:4px; }
/* ── service pages ── */
.toc{ column-count:2; column-gap:40px; margin-top:6px; }
.toc .s{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.22em; text-transform:uppercase; color:var(--sect); margin:14px 0 6px; break-after:avoid; }
.toc a{ display:grid; grid-template-columns:1fr 28px; column-gap:10px; align-items:baseline; padding:4px 0 5px; border-top:1px solid var(--line); break-inside:avoid; }
.toc a .t{ font-family:'Fraunces'; font-weight:500; font-size:11.5px; line-height:14px; font-variation-settings:'opsz' 36; }
.toc a .n{ font-family:'DM'; font-weight:600; font-size:10px; text-align:right; }
.toc a .n::after{ content:attr(data-page); }
.list .it{ display:grid; grid-template-columns:96px 1fr; column-gap:14px; padding:7px 0 8px; border-top:1px solid var(--line); break-inside:avoid; }
.list .it .k{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--sect); padding-top:2px; }
.list .it p{ margin:0; text-align:left; }
.cards{ column-count:2; column-gap:24px; }
.card{ break-inside:avoid; margin:0 0 10px; }
.card h3{ margin:0 0 3px; }
.tier{ margin-top:10px; } .tier h2{ column-span:none; }
.fail{ break-inside:avoid; padding:6px 0 7px; border-top:1px solid var(--line); }
.fail b{ font-family:'Fraunces'; font-weight:600; font-size:11.5px; line-height:14px; display:block; font-variation-settings:'opsz' 36; }
.fail p{ margin:2px 0 0; font-size:10px; line-height:13.5px; text-align:left; }
.wallet{ background:var(--tint); padding:18px 22px 14px; margin-top:6px; break-inside:avoid; }
.wallet .t{ font-family:'Fraunces'; font-weight:600; font-size:18px; margin:0 0 10px; font-variation-settings:'opsz' 72; }
.wallet .r{ display:grid; grid-template-columns:1fr 1fr; column-gap:16px; padding:5px 0 6px; border-top:1px solid rgba(138,51,36,.25); }
.wallet .r .k{ font-family:'Fraunces'; font-weight:500; font-size:11px; font-variation-settings:'opsz' 36; } .wallet .r .v{ font-family:'DM'; font-weight:600; font-size:9.5px; line-height:13px; color:var(--sect); }
.wont .it{ padding:8px 0 9px; border-top:1px solid var(--line); break-inside:avoid; }
.wont .it b{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:3px; }
.wont .it p{ margin:0; text-align:left; }
.tbl .r{ display:grid; grid-template-columns:220px 1fr 36px; column-gap:14px; padding:7px 0 8px; border-top:1px solid var(--line); break-inside:avoid; }
.tbl .r .q{ font-family:'Fraunces'; font-weight:600; font-size:11px; line-height:14px; font-variation-settings:'opsz' 36; }
.tbl .r .c{ font-size:10.5px; line-height:14px; } .tbl .r .n{ font-family:'DM'; font-weight:600; font-size:10px; text-align:right; } .tbl .r .n a::after{ content:attr(data-page); }
.tbl .heads{ display:grid; grid-template-columns:220px 1fr 36px; column-gap:14px; font-family:'DM'; font-weight:700; font-size:7.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); padding-bottom:4px; }
.asks{ column-count:2; column-gap:24px; margin-top:4px; }
.ask{ break-inside:avoid; margin:0 0 12px; border-top:2px solid var(--sect); padding-top:6px; }
.ask .who{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--sect); margin:0 0 4px; }
.ask p{ margin:0; font-family:'Fraunces'; font-style:italic; font-size:11px; line-height:14px; padding:3px 0; border-top:1px solid var(--line); font-variation-settings:'opsz' 36; }
.trip{ break-inside:avoid; margin:10px 0 0; }
.trip h3{ margin:0 0 2px; } .trip .as{ font-size:10px; line-height:13.5px; color:var(--grey); margin:0 0 6px; text-align:left; }
.trip .r{ display:grid; grid-template-columns:70px 1fr; column-gap:12px; padding:4px 0 5px; border-top:1px solid var(--line); }
.trip .r b{ font-family:'Fraunces'; font-weight:600; font-size:11px; font-variation-settings:'opsz' 36; } .trip .r span{ font-size:10.5px; line-height:14px; }
.trip .why{ font-size:10px; line-height:13.5px; margin:6px 0 0; border-top:2px solid var(--ink); padding-top:5px; text-align:left; }
.fb .r{ display:grid; grid-template-columns:170px 1fr; column-gap:14px; padding:6px 0 7px; border-top:1px solid var(--line); break-inside:avoid; }
.fb .r b{ font-family:'Fraunces'; font-weight:600; font-size:11px; line-height:14px; font-variation-settings:'opsz' 36; } .fb .r p{ margin:0; font-size:10.5px; line-height:14px; text-align:left; }
.fs{ page:annex; } .fs h1{ font-size:36px; margin-bottom:8px; } .fs .sf{ margin-bottom:8px; }
.fs .method{ font-size:9.5px; line-height:13px; color:var(--grey); margin:0 0 12px; }
.fs .cols{ column-count:2; column-gap:28px; }
.fs h2{ column-span:none; margin:8px 0 4px; } .fs .pg{ break-inside:auto; }
.fs .r{ display:grid; grid-template-columns:1fr 1fr; column-gap:10px; padding:4px 0 5px; border-top:1px solid var(--line); break-inside:avoid; }
.fs .r .k{ font-family:'Fraunces'; font-weight:500; font-size:10px; line-height:12.5px; font-variation-settings:'opsz' 36; } .fs .r .v{ font-family:'DM'; font-weight:600; font-size:8.5px; line-height:12px; color:var(--sect); }
.keep{ break-inside:avoid; }
.opener{ position:relative; } .ledger{ position:relative; } .verdict{ position:relative; }
'''

# ── figure text fixes: a label a line crossed, or a label past the edge — the book's words, moved whole ──
FIG_FIX = {3: [('Pantheon', 0, 10), ('TERMINI', -2, 0)], 1: [('Term', 0, 0)]}
def figure_html(b, fid):
    svg = open(b['svg_file'], encoding='utf-8').read()
    for label, dx, dy in FIG_FIX.get(fid, []):
        def mv(m):
            return f'<text x="{float(m.group(1))+dx:.1f}" y="{float(m.group(2))+dy:.1f}"' + m.group(3)
        svg = re.sub(r'<text x="([\d.\-]+)" y="([\d.\-]+)"([^>]*>' + re.escape(label) + r'[^<]*</text>)', mv, svg, count=1)
    svg = svg.replace('<svg ', f'<svg id="fig{fid}" ', 1)
    cap = b['cap']; m = re.match(r'(FIG\. \d+)\s*·\s*(.*)', cap, re.S)
    capx = f'<b>{m.group(1)}.</b> {esc(m.group(2))}' if m else esc(cap)
    return f'<figure class="fig" data-fig="{fid}">{svg}<figcaption>{capx}</figcaption></figure>'

def photo_html(b, cls='plate', tall=False, pos='50% 50%'):
    if not b or not b.get('src'): return ''
    cap = b.get('cap', ''); m = re.match(r'(PL\. \d+)\s*·\s*(.*)', cap, re.S)
    capx = f'<b>{m.group(1)}.</b> {esc(m.group(2))}' if m else (f'<b>{esc(cap.split(".")[0])}.</b> {esc(cap.split(".",1)[1].strip())}' if '.' in cap else esc(cap))
    return f'<figure class="{cls}{" tall" if tall else ""}"><img src="{b["src"]}" style="object-position:{pos}">{f"<figcaption>{capx}</figcaption>" if cap else ""}</figure>'

def ledger_html(d):
    if len(d['rows']) > 8:   # a long ledger would outgrow a column: two sidebars, the second continued
        h1 = dict(d, rows=d['rows'][:(len(d['rows']) + 1) // 2]); h2 = dict(d, rows=d['rows'][(len(d['rows']) + 1) // 2:], caption=d['caption'] + ' (continued)', heads=[])
        return ledger_html(h1) + ledger_html(h2)
    rows = ''
    for r in d['rows']:
        opt, sub = (r['opt'].split(' — ', 1) + [''])[:2] if ' — ' in r['opt'] else (r['opt'], '')
        vals = ' · '.join(r['vals'])
        rows += f'<div class="r"><div class="opt">{opt}</div>{f"<div class=sub>{sub}</div>" if sub else ""}<div class="v">{esc(vals)}</div></div>'
    heads = f'<div class="heads">{"".join(f"<span>{esc(h)}</span>" for h in d["heads"])}</div>' if d['heads'] else ''
    return f'<div class="side ledger"><span class="lab">{esc(d["caption"].title() if d["caption"].isupper() else d["caption"])}</span>{heads}{rows}</div>'

def forks_html(b):
    out = '<div class="forks">'; last = None
    for it in b['items']:
        if it['lab'] != last: out += f'<span class="lab">{esc(it["lab"])}</span>'; last = it['lab']
        cond, _, cons = it['text'].partition(' → ')
        out += f'<div class="q">{cond}{(" <b>→</b> " + cons) if cons else ""}</div>'
    return out + '</div>'

def note_html(note, xref):
    lab = '<i class="mk">◆</i> Volatile' if (note and '◆' in note['text']) else 'Note'
    return f'<div class="note"><span class="lab">{lab}</span><p>{note["text"] if note else ""}{f"<span class=x>{esc(xref["text"])}</span>" if xref else ""}</p></div>'

def group_lines(blocks):
    """Consecutive 'line' blocks of one face/size → one paragraph block (kept as 'lines' with runs)."""
    out = []
    for b in blocks:
        if b['t'] == 'line' and out and out[-1]['t'] == 'lines' and out[-1]['face'] == b['face'] and out[-1]['size'] == b['size'] and out[-1]['page'] == b['page']:
            out[-1]['items'].append(b)
        elif b['t'] == 'line':
            out.append({'t': 'lines', 'face': b['face'], 'size': b['size'], 'page': b['page'], 'y': b['y'], 'items': [b]})
        else: out.append(b)
    return out

def title_html(ch, long=False):
    return f'<h1{" class=long" if long or len(ch["title"]) > 44 else ""}>{esc(ch["title"])}</h1>'

def opener(ch, hero, in_short=None, cap=None, pos='50% 50%', sect=None):
    sect = sect or ch['kicker'] or 'Chapter'
    sf = next((b for b in ch['blocks'] if b['t'] == 'standfirst'), None)
    if in_short:
        lead, rest = in_short['lead'], in_short['rest']
        m = re.match(r'(.+?[.!?])(\s+\S.*)$', lead)
        if m: lead, rest = m.group(1), (m.group(2).strip() + ' ' + rest).strip()
    right = f'<div class="call verdict"><span class="lab">In short</span><div class="big">{esc(lead)}</div><p>{rest}</p></div>' if in_short else ''
    return f'''<div class="pg op first opener" id="{ch['id']}-p"><span class="rh-src">{esc(sect if sect != 'Chapter' else ch['title'])}</span>
  <div class="hero"><img src="{hero['src']}" style="object-position:{pos}"><div class="cap">{esc(cap if cap is not None else hero.get('cap', ''))}</div></div>
  <div class="open{'' if in_short else ' one'}"><div><div class="sect">{esc(sect)}</div>{title_html(ch)}{f'<div class="sf">{sf["text"]}</div>' if sf else ''}</div>{right}</div></div>'''

def body_flow(ch, blocks, lede=True, closers=True):
    """Paragraphs in two columns; figures and plates at the full measure between column blocks;
    the ledger, forks and note inside the flow."""
    out = []; buf = []; first = lede
    def flush():
        nonlocal buf
        if buf: out.append('<div class="body2">' + ''.join(buf) + '</div>'); buf = []
    plates_end = []
    for b in blocks:
        t = b['t']
        if t == 'p':
            buf.append(f'<p{" class=lede" if first else ""}>{b["text"]}</p>'); first = False
        elif t == 'figure': flush(); out.append(figure_html(b, b['fig']))
        elif t == 'photo':
            if b['kind'] == 'plate' or b['cap']: flush(); out.append(photo_html(b, 'plate'))
            elif closers: plates_end.append(b)
        elif t == 'ledger': buf.append(ledger_html(b))
        elif t == 'call': pass
        elif t == 'forks': buf.append(forks_html(b))
        elif t == 'note': buf.append(note_html(b, None))
        elif t == 'xref': buf.append(f'<div class="note" style="border-top:0;margin-top:-8px;padding-top:0"><span></span><p><span class="x" style="margin-top:0">{esc(b["text"])}</span></p></div>')
        elif t == 'lines':
            buf.append(lines_html(b))
    flush()
    for b in plates_end: out.append(photo_html(b, 'plate', tall=True))
    return ''.join(out)

def lines_html(b):
    f, s = b['face'], b['size']; items = b['items']
    text = ' '.join(it['text'] for it in items)
    if f == 'plex-md' and s == 8.2: return f'<h2>{esc(nice(items[0]["text"]).title())}</h2>'
    if (f == 'plex' and s in (6.8, 7.1, 7.5)) or (f == 'fell' and s == 14.2): return ''.join(f'<h3>{it["text"]}</h3>' for it in items)
    if f == 'goudy' and s == 9.4: return ''.join(f'<p class="who" style="font-family:DM;font-weight:700;font-size:8.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--sect);margin:8px 0 2px">{it["text"]}</p>' for it in items)
    return f'<p>{text}</p>'

# ═══ chapters ═══════════════════════════════════════════════════════════════════
OUT = []

# cover
cv = BY['cover']
OUT.append(f'''<section class="chap" id="cover"><div class="cover">
  <div class="mast"><span>Rome for Americans</span><span>A decision manual</span></div>
  <div class="blk"><div class="t">Rome,<br>Solved.</div><div class="s">Which of it is actually worth your time — and which is the photo everyone regrets.</div>
  <div class="d">The historic core is a kilometre and a half across its radius. You walk it. This book is that one fact, worked out.</div></div>
  <div class="foot"><span>La Tavola · First edition · 2026</span><span>romeforamericans.com</span></div></div></section>''')

# contents — sections and entries from the book's own TOC, page numbers resolved after pagination
toc = BY['what-s-inside']; order = [c['id'] for c in CH if c['id'] not in ('cover', 'what-s-inside', 'intro')] + ['fs']
entries = []; sect = None; k = 0
for b in toc['blocks']:
    if b['t'] == 'line' and b['face'] == 'plex' and b['size'] == 6.0: sect = nice(b['text']).title(); entries.append(('S', sect))
    elif b['t'] == 'line' and b['face'] == 'fell' and b['size'] == 9.8:
        cid = order[k] if k < len(order) else ''; k += 1; entries.append(('E', b['text'], cid))
    elif b['t'] == 'ledger': pass
toc_html = ''.join(f'<div class="s">{esc(e[1])}</div>' if e[0] == 'S' else f'<a href="#{e[2]}"><span class="t">{e[1]}</span><span class="n"{" data-page=sheet" if e[2] == "fs" else ""}></span></a>' for e in entries)
OUT.append(f'''<section class="chap" id="contents"><div class="pg first" id="contents-p"><span class="rh-src">Contents</span>
  <div class="sect" style="margin-top:40px">What’s inside</div><h1 style="font-size:54px">Contents</h1>
  <div class="toc">{toc_html}</div></div></section>''')

# intro — Rome, Solved.
ch = BY['intro']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo')
rest = [b for b in blocks if b is not hero and b['t'] != 'standfirst']
OUT.append(f'<section class="chap" id="intro">' + opener(ch, hero, cap='The compact core at golden hour — the kilometre and a half the whole book turns on.', sect='Rome, Solved.') + body_flow(ch, rest) + '</section>')

# essays and decisions
DECISIONS = [c for c in CH if c['id'].startswith('d0')]
ESSAYS = ['how-to-read-this-book', 'the-ground-a-city-you-can-wa', 'why-the-obvious-tool-doesn-t', 'day-zero-the-arrival', 'the-rhythm-of-the-week',
          'walking-the-quarters', 'the-set-pieces', 'the-plan-as-operations', 'eating-the-rule-that-outlive']
def essay(cid, pos='50% 50%'):
    ch = BY[cid]; blocks = group_lines(ch['blocks'])
    hero = next((b for b in blocks if b['t'] == 'photo'), None)
    rest = [b for b in blocks if b is not hero and b['t'] != 'standfirst']
    return f'<section class="chap" id="{cid}">' + opener(ch, hero, pos=pos) + body_flow(ch, rest) + '</section>'
def decision(ch):
    blocks = group_lines(ch['blocks'])
    hero = next((b for b in blocks if b['t'] == 'photo'), None)
    call = next((b for b in blocks if b['t'] == 'call'), None)
    note = next((b for b in blocks if b['t'] == 'note'), None); xref = next((b for b in blocks if b['t'] == 'xref'), None)
    rest = [b for b in blocks if b is not hero and b['t'] not in ('standfirst', 'call', 'note', 'xref')]
    html = opener(ch, hero, in_short=call, sect=ch['kicker'])
    html += body_flow(ch, rest, closers=False)
    # the note and the cross-reference close the argument, then the closing plate
    tail = note_html(note, xref)
    closers = [b for b in blocks if b['t'] == 'photo' and b is not hero and not b['cap']]
    # put the note inside the last column block
    html += '<div class="body2">' + tail + '</div>'
    for b in closers: html += photo_html(b, 'plate', tall=True)
    return f'<section class="chap decision" id="{ch["id"]}">' + html + '</section>'

for cid in ESSAYS[:3]: OUT.append(essay(cid))
for ch in DECISIONS: OUT.append(decision(ch))

# before you fly — the checklist
ch = BY['before-you-fly']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo'); items = []
cur_k = None
for b in blocks:
    if b['t'] == 'lines' and b['face'] == 'plex' and b['size'] == 6.8: cur_k = b['items'][0]['text']
    elif b['t'] == 'lines' and b['face'] == 'goudy' and b['size'] == 9.0 and cur_k is not None: items.append((cur_k, ' '.join(it['text'] for it in b['items']))); cur_k = None
intro_p = ''.join(f'<p class="t{" lede" if i == 0 else ""}">{b["text"]}</p>' for i, b in enumerate(b for b in blocks if b['t'] == 'p'))
ledger_cap = next((b['caption'] for b in blocks if b['t'] == 'ledger'), 'The pre-departure list · by deadline')
OUT.append(f'<section class="chap" id="before-you-fly">' + opener(ch, hero) + f'''<div class="body2">{intro_p}</div>
  <h2 style="column-span:none">{esc(ledger_cap.title())}</h2><div class="list">{''.join(f'<div class="it"><div class="k">{esc(k)}</div><p>{t}</p></div>' for k, t in items)}</div></section>''')

for cid in ESSAYS[3:5]: OUT.append(essay(cid))

# where to stay, assessed — five cards and two figures
ch = BY['where-to-stay-assessed']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo')
html = opener(ch, hero)
intro = [b for b in blocks if b['t'] == 'p' and b['page'] == 41 and b['y'] < 400]
html += '<div class="body2">' + ''.join(f'<p class="{"lede" if i == 0 else ""}">{b["text"]}</p>' for i, b in enumerate(intro)) + '</div>'
html += figure_html(next(b for b in blocks if b['t'] == 'figure' and b['fig'] == 10), 10)
cards = []; head = None
for b in blocks:
    if b['t'] == 'lines' and ((b['face'] == 'fell' and b['size'] == 14.2) or (b['face'] == 'plex' and b['size'] == 7.5)): head = b['items'][0]['text']
    elif b['t'] == 'p' and head: cards.append((head, b['text'])); head = None
html += '<div class="cards">' + ''.join(f'<div class="card"><h3>{esc(h.split(" · ")[0])}<small>{esc(h.split(" · ",1)[1]) if " · " in h else ""}</small></h3><p class="t">{t}</p></div>' for h, t in cards) + '</div>'
html += figure_html(next(b for b in blocks if b['t'] == 'figure' and b['fig'] == 11), 11)
closers = [b for b in blocks if b['t'] == 'photo' and b is not hero]
for b in closers: html += photo_html(b, 'plate', tall=True)
OUT.append(f'<section class="chap" id="where-to-stay-assessed">{html}</section>')

for cid in ESSAYS[5:8]: OUT.append(essay(cid))

# day trips, ranked — cards
ch = BY['day-trips-ranked-by-the-day-']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo'); html = opener(ch, hero)
ps = [b for b in blocks if b['t'] == 'p']
html += f'<div class="body2"><p class="lede">{ps[0]["text"]}</p></div>'
cards = []; head = None; tail_p = None
for b in blocks:
    if b['t'] == 'lines' and b['face'] == 'plex' and b['size'] == 7.1: head = b['items'][0]['text']
    elif b['t'] == 'p' and head: cards.append((head, b['text'])); head = None
    elif b['t'] == 'p' and cards and b is not ps[0]: tail_p = b
html += '<div class="cards">' + ''.join(f'<div class="card"><h3>{esc(h.split(" · ")[0])}<small>{esc(h.split(" · ",1)[1]) if " · " in h else ""}</small></h3><p class="t">{t}</p></div>' for h, t in cards) + '</div>'
if tail_p: html += f'<div class="body2"><p>{tail_p["text"]}</p></div>'
for b in [b for b in blocks if b['t'] == 'photo' and b is not hero]: html += photo_html(b, 'plate', tall=True)
OUT.append(f'<section class="chap" id="day-trips-ranked-by-the-day-">{html}</section>')

OUT.append(essay(ESSAYS[8]))

# failure modes — the tiers
ch = BY['failure-modes']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo'); html = opener(ch, hero)
html += '<div class="body2">' + ''.join(f'<p class="{"lede" if i == 0 else ""}">{b["text"]}</p>' for i, b in enumerate(b for b in blocks if b['t'] == 'p')) + '</div>'
html += figure_html(next(b for b in blocks if b['t'] == 'figure'), 14)
tiers = []; cur_t = None
for b in blocks:
    if b['t'] == 'lines' and b['face'] == 'plex-md': cur_t = [nice(b['items'][0]['text']).title(), []]; tiers.append(cur_t)
    elif b['t'] == 'lines' and b['size'] == 9.3 and cur_t is not None:
        for it in b['items']:
            runs = it.get('runs', [])
            if runs and runs[0][0] == 'fell' and len(runs[0][2].strip()) > 3:   # a new item: its head is the Fell run
                head = runs[0][2].strip(); body = ''.join(r[2] for r in runs[1:]).strip()
                cur_t[1].append([head, body])
            elif cur_t[1]: cur_t[1][-1][1] += ' ' + it['text']
            else: cur_t[1].append(['', it['text']])
tiers_html = ''
for name, items in tiers:
    tiers_html += f'<div class="tier"><h2>{esc(name)}</h2><div class="cards">' + ''.join(f'<div class="fail"><b>{esc(h)}</b><p>{t}</p></div>' for h, t in items) + '</div></div>'
html += tiers_html
for b in [b for b in blocks if b['t'] == 'photo' and b is not hero]: html += photo_html(b, 'plate')
OUT.append(f'<section class="chap" id="failure-modes">{html}</section>')

# the wallet card
ch = BY['the-wallet-card']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo'); html = opener(ch, hero)
# Pair by position (owner review 2026-10-25): a question wrapped onto two lines ("Must-book, weeks / ahead?")
# used to shift every answer below it by one row. A question runs until its '?'; each answer line joins the
# question whose first line is nearest above-or-level with it.
rows = []
for b in ch['blocks']:
    if b['t'] == 'line' and b['face'] == 'fell' and b['size'] == 9.0:
        if rows and not rows[-1][0].rstrip().endswith('?'): rows[-1][0] += ' ' + b['text']
        else: rows.append([b['text'], '', b['y']])
for b in ch['blocks']:
    if b['t'] == 'line' and b['face'] == 'plex' and b['size'] == 7.9 and rows:
        r = min((r for r in rows if r[2] <= b['y'] + 3), key=lambda r: b['y'] - r[2], default=rows[0])
        r[1] = (r[1] + ' ' + b['text']).strip()
rows = [(q, a) for q, a, _ in rows]
title = next((b['text'] for b in ch['blocks'] if b['t'] == 'line' and b['face'] == 'fell' and b['size'] == 14.2), 'Rome, on one card')
html += f'<div class="wallet"><div class="t">{esc(title)}</div>' + ''.join(f'<div class="r"><div class="k">{q}</div><div class="v">{esc(a)}</div></div>' for q, a in rows) + '</div>'
OUT.append(f'<section class="chap" id="the-wallet-card">{html}</section>')

# what this book won't tell you
ch = BY['what-this-book-won-t-tell-yo']; blocks = group_lines(ch['blocks'])
hero = next(b for b in blocks if b['t'] == 'photo'); html = opener(ch, hero)
html += '<div class="body2">' + ''.join(f'<p class="{"lede" if i == 0 else ""}">{b["text"]}</p>' for i, b in enumerate(b for b in blocks if b['t'] == 'p')) + '</div>'
items = []
for b in blocks:
    if b['t'] == 'lines' and b['face'] == 'goudy' and b['size'] == 9.5:
        for it in b['items']:
            m = re.match(r'((?:WE|THE)[^.]*\.)\s*(.*)', it['text'])
            if m: items.append([m.group(1), m.group(2)])
            elif items: items[-1][1] += ' ' + it['text']
html += '<div class="wont">' + ''.join(f'<div class="it"><b>{esc(h.title())}</b><p>{t}</p></div>' for h, t in items) + '</div>'
OUT.append(f'<section class="chap" id="what-this-book-won-t-tell-yo">{html}</section>')

# after the last tab — the closing essay: no hero at the top (its photographs are its plates)
ch = BY['after-the-last-tab']; blocks = group_lines(ch['blocks'])
photos = [b for b in blocks if b['t'] == 'photo']
OUT.append(f'<section class="chap" id="after-the-last-tab">' + opener(ch, photos[1] if len(photos) > 1 else photos[0], pos='50% 55%') +
           body_flow(ch, [b for b in blocks if b['t'] != 'photo'] + [p for p in photos if p is not (photos[1] if len(photos) > 1 else photos[0]) and not p['cap']]) + '</section>')

# decide these first — the table, the questions, the two trips, the fallbacks
ch = BY['decide-these-first']; blocks = ch['blocks']
hero = next(b for b in blocks if b['t'] == 'photo'); html = opener(ch, hero, sect='Before you book')
L = [b for b in blocks if b['t'] == 'line']
def rows_by_rules(lines, page, rules, cols):
    """Lines on a page bucketed by the horizontal rules between rows; each bucket → one row of columns by x."""
    buckets = []
    bounds = [0] + rules + [9999]
    for lo, hi in zip(bounds, bounds[1:]):
        ls = [l for l in lines if l['page'] == page and lo <= l['y'] < hi]
        if ls:
            row = []
            for x0, x1 in cols: row.append(' '.join(l['text'] for l in sorted([l for l in ls if x0 <= l['x'] < x1], key=lambda l: l['y'])))
            if any(row): buckets.append(row)
    return buckets
rules = ch['rules']
r62 = rows_by_rules([l for l in L if l['page'] == 62 and l['face'] in ('fell', 'goudy', 'plex') and l['size'] in (9.8, 9.0, 8.2)], 62, rules.get('62', rules.get(62, [])), [(60, 260), (260, 520), (520, 600)])
dec_ids = [c['id'] for c in DECISIONS]
tbl = '<div class="tbl"><div class="heads"><span>Decide</span><span>The call this book makes</span><span>Page</span></div>' + ''.join(
    f'<div class="r"><div class="q">{q}</div><div class="c">{c}</div><div class="n"><a href="#{dec_ids[i] if i < len(dec_ids) else ""}"></a></div></div>' for i, (q, c, n) in enumerate(r62) if q) + '</div>'
html += f'<div class="body2"><p class="lede">{next(b["text"] for b in blocks if b["t"] == "standfirst")}</p></div>'.replace('class="lede"', '') if False else ''
html += tbl
# the questions
asks = []; who = None; intro63 = next((b['text'] for b in blocks if b['t'] == 'p' and b['page'] == 63), '')
for l in L:
    if l['page'] == 63 and l['face'] == 'goudy' and l['size'] == 9.4: who = [l['text'], []]; asks.append(who)
    elif l['page'] == 63 and l['face'] == 'goudy' and l['size'] == 12.0 and who: who[1].append(l['text'])
html += f'<h2>What to ask, before you pay</h2><p class="t" style="margin-bottom:8px">{intro63}</p><div class="asks">' + ''.join(
    f'<div class="ask"><p class="who">{esc(w.title())}</p>' + ''.join(f'<p>{q}</p>' for q in qs) + '</div>' for w, qs in asks) + '</div>'
# the two trips
intro_trips = next((b['text'] for b in blocks if b['t'] == 'p' and b['page'] == 63 and 'nine calls' in b['text']), '')
trips = []; cur_tr = None
fb_y = next((l['y'] for l in L if l['page'] == 64 and l['face'] == 'plex-md' and l['size'] == 8.2), 9999)
for l in L:
    if l['face'] == 't3' and l['size'] == 10.0:
        if cur_tr and cur_tr['title'].endswith(','): cur_tr['title'] += ' ' + l['text']
        else: cur_tr = {'title': l['text'], 'as': '', 'rows': [], 'why': ''}; trips.append(cur_tr)
    elif cur_tr and l['face'] == 'goudy' and l['size'] == 10.3: cur_tr['as'] += (' ' if cur_tr['as'] else '') + l['text']
    elif cur_tr and l['face'] == 'goudy' and l['size'] == 10.8: cur_tr['why'] += (' ' if cur_tr['why'] else '') + l['text']
    elif cur_tr and l['face'] == 'fell' and l['size'] == 9.8 and l['page'] in (63, 64) and l['x'] < 100 and not (l['page'] == 64 and l['y'] >= fb_y): cur_tr['rows'].append([l['text'], '', l['y'], l['page']])
    elif cur_tr and l['face'] == 'goudy' and l['size'] == 9.0 and l['page'] in (63, 64) and l['x'] > 100 and not (l['page'] == 64 and l['y'] >= fb_y):
        # a WHAT HAPPENS line belongs to the nearest WHEN above it on the same page (rows may extract in either order)
        cur_tr.setdefault('what', []).append([l['y'], l['page'], l['text']])
for tr in trips:
    whats = tr.pop('what', [])
    # pair by order: each row's text is the what-lines between this row's y and the next row's y (same page), tolerant of a few px
    for i, r in enumerate(tr['rows']):
        nxt = tr['rows'][i + 1] if i + 1 < len(tr['rows']) else None
        for y, pg, t in whats:
            if pg == r[3] and y >= r[2] - 14 and (nxt is None or pg != nxt[3] or y < nxt[2] - 14): r[1] += (' ' if r[1] else '') + t
    tr['title'] = tr['title'].replace('fi rst', 'first').replace(' fi ', ' fi')
    tr['title'] = re.sub(r'\bfi\b', 'fi', tr['title'])
trips_html = ''.join(f'<div class="trip"><h3>{esc(tr["title"]).replace("Three days, fi", "Three days, fi")}</h3><p class="as">{tr["as"]}</p>' + ''.join(f'<div class="r"><b>{esc(w)}</b><span>{t}</span></div>' for w, t, *_ in tr['rows']) + f'<p class="why">{tr["why"]}</p></div>' for tr in trips)
html += f'<h2>Two trips that follow the calls</h2><p class="t" style="margin-bottom:4px">{intro_trips}</p><div class="cards" style="margin-top:6px">{trips_html}</div>'
# the fallbacks
r64 = rows_by_rules([l for l in L if l['page'] == 64 and l['face'] in ('fell', 'goudy') and l['size'] in (9.8, 9.0) and l['y'] > 0], 64, [y for y in rules.get('64', rules.get(64, []))], [(60, 165), (165, 600)])
fb_start = next((i for i, r in enumerate(r64) if r[0].startswith('Your Colosseum')), None)
fb = r64[fb_start:] if fb_start is not None else []
html += '<h2>When the plan does not survive the day</h2><div class="fb">' + ''.join(f'<div class="r"><b>{w}</b><p>{d}</p></div>' for w, d in fb if w) + '</div>'
OUT.append(f'<section class="chap" id="decide-these-first">{html}</section>')

# the Field Sheet — from its own PDF, in the same hand
fsd = pymupdf.open(FS_PDF); groups = []; cur_g = None; title = 'The Field Sheet'; sf = ''; method = []
col_lines = []
for p in fsd:
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            s = l['spans'][0]; t = ''.join(x['text'] for x in l['spans']).strip()
            if not t: continue
            col_lines.append((round(l['bbox'][0]), round(l['bbox'][1]), s['font'].split('+')[-1], round(s['size'], 1), t))
col_lines.sort(key=lambda l: (0 if l[0] < 300 else 1, l[1]))
for x, y, f, s, t in col_lines:
    if s == 25.5: title = t
    elif s == 12.0: sf = t
    elif s == 8.6: method.append(t)
    elif f.startswith('IBMPlexMono-Medi') and s == 7.9: cur_g = [nice(t).title(), []]; groups.append(cur_g)
    elif 'FELL' in f.upper() and s == 8.2 and cur_g is not None:
        if cur_g[1] and cur_g[1][-1][1] == '': cur_g[1][-1][0] += ' ' + t
        else: cur_g[1].append([t, ''])
    elif f.startswith('IBMPlexMono-Regu') and s == 7.1 and cur_g is not None and cur_g[1]: cur_g[1][-1][1] = (cur_g[1][-1][1] + ' ' + t).strip()
OUT.append(f'''<section class="chap fs" id="fs"><div class="pg first" id="fs-p"><span class="rh-src">The Field Sheet</span>
  <div class="sect">The annex</div><h1>{esc(title)}</h1><div class="sf">{esc(sf)}</div><p class="method">{esc(' '.join(method))}</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;column-gap:28px"><div>{''.join(f'<h2>{esc(g)}</h2>' + ''.join(f'<div class="r"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in rows) for g, rows in groups[:2])}</div><div>{''.join(f'<h2>{esc(g)}</h2>' + ''.join(f'<div class="r"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in rows) for g, rows in groups[2:])}</div></div></div></section>''')

html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Rome, Solved.</title>
<style>{CSS}</style></head><body>
{''.join(OUT)}
</body></html>'''
open('dossier3.html', 'w', encoding='utf-8').write(html)
print('composed dossier3.html in the Édition hand:', len(html), 'bytes;', html.count('class="pg op'), 'openers,', html.count('<figure class="fig"'), 'figures')
