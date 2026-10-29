# -*- coding: utf-8 -*-
"""MODEL 8 — LA MOSAÏQUE · Mercè Oller, the modular designer.
The page is assembled from tiles on the six-column grid with an 8px grout, the way a
trencadís wall is assembled from fragments: each tile holds ONE unit of information
(the verdict, one option, one photograph, one paragraph pair, one pull, the note) and
takes the colour of its job — red for the call, gold for the chosen options, blue for
a pull sentence, ink for the volatile note, paper for prose and the map. Nothing
floats; nothing is boxed; the grout is the only rule."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Outfit';src:url('%(F)sOutfit.ttf');font-weight:100 900;}
@font-face{font-family:'Manrope';src:url('%(F)sManrope.ttf');font-weight:200 800;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'Plex';src:url('%(H)sIBMPlexMono-Regular.ttf');}
@font-face{font-family:'Public';src:url('%(F)sOutfit.ttf');font-weight:100 900;}
:root{ --paper:#F3F1EB; --ink:#1B2622; --grey:#6B7773; --red:#A23520; --gold:#E0A828; --blue:#0E6390; --stone:#DDE1DC; --g:8px; }
@page{ @top-left{ content:"Barcelona, Without the Traps."; font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); }
       @bottom-left{ content:"Barcelona for Americans"; font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.06em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Outfit'; font-weight:700; font-size:11px; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Manrope'; font-size:10.5px; line-height:15px; color:var(--ink); }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.row{ display:grid; grid-template-columns:repeat(6, 1fr); column-gap:var(--g); margin-bottom:var(--g); }
.t{ background:#fff; padding:16px 18px; box-sizing:border-box; overflow:hidden; position:relative; }
.t.c2{ grid-column:span 2; } .t.c3{ grid-column:span 3; } .t.c4{ grid-column:span 4; } .t.c6{ grid-column:span 6; }
.t.red{ background:var(--red); color:#fff; } .t.gold{ background:var(--gold); color:var(--ink); } .t.blue{ background:var(--blue); color:#fff; }
.t.ink{ background:var(--ink); color:#F3F1EB; } .t.stone{ background:var(--stone); } .t.img{ padding:0; }
.t.img img{ display:block; width:100%; height:100%; object-fit:cover; position:absolute; inset:0; }
.t .k{ font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; display:block; margin-bottom:8px; opacity:.85; }
h1{ font-family:'Outfit'; font-weight:700; font-size:40px; line-height:.95; letter-spacing:-.025em; margin:0 0 10px; }
.sf{ font-size:12px; line-height:17px; font-weight:500; margin:0; }
.t .giant{ font-family:'Outfit'; font-weight:800; font-size:64px; line-height:.85; letter-spacing:-.04em; margin:0 0 10px; }
.t .big{ font-family:'Outfit'; font-weight:600; font-size:14px; line-height:17px; margin:0 0 6px; }
.t p{ margin:0 0 8px; text-align:left; hyphens:auto; } .t p:last-child{ margin-bottom:0; }
.t.red p, .t.ink p, .t.blue p{ opacity:.95; }
.stack{ display:grid; grid-template-rows:repeat(4, 1fr); row-gap:var(--g); grid-column:span 3; }
.stack .t{ padding:10px 14px; display:flex; flex-direction:column; justify-content:center; }
.stack .opt{ font-family:'Outfit'; font-weight:600; font-size:13px; line-height:15px; }
.stack .sub{ font-size:9px; line-height:12px; opacity:.8; margin-top:2px; }
.stack .v{ font-family:'Mono'; font-size:8px; letter-spacing:.06em; text-transform:uppercase; margin-top:4px; }
.t.pull{ display:flex; align-items:flex-end; }
.t.pull .q{ font-family:'Outfit'; font-weight:600; font-size:24px; line-height:26px; letter-spacing:-.02em; }
.t .fq{ font-family:'Outfit'; font-weight:600; font-size:15px; line-height:18px; margin:0 0 6px; }
.t .cap{ position:absolute; left:0; right:0; bottom:0; padding:8px 12px; background:rgba(27,38,34,.82); color:#fff; font-family:'Outfit'; font-size:8.5px; letter-spacing:.06em; text-transform:uppercase; }
.t .x{ opacity:.7; } .t.ink .k{ color:var(--gold); opacity:1; }
.mapt svg{ display:block; width:100%; height:auto; }
'''.replace('%(F)s', FONTS).replace('%(H)s', HOUSE)

def row(h, *tiles):
    return f'<div class="row" style="height:{h}px">' + ''.join(tiles) + '</div>'

def tile(cls, inner, style=''):
    return f'<div class="t {cls}"{" style=%r" % style if style else ""}>{inner}</div>'

def img(cls, src, cap, pos='50% 50%'):
    return f'<div class="t img {cls}"><img src="{photo(src)}" style="object-position:{pos}"><div class="cap">{cap}</div></div>'

def stack(d, picks, pickcls='gold'):
    return '<div class="stack">' + ''.join(
        f'<div class="t {pickcls if i in picks else "stone"}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'

def note(d):
    lab = '<i class="mk">◆</i> Volatile · 2026' if d['volatile'] else 'Since 2019'
    return tile('c2 ink', f'<span class="k">{lab}</span><p style="font-size:10px;line-height:14px">{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p>')

def forks(d, span='c3'):
    return ''.join(tile(span, f'<span class="k">{esc(f["lab"])}</span><div class="fq">{esc(f["strong"])}</div><p>{f["text"]}</p>') for f in d['forks'])

d = CH['d06']; P = d['paras']
d06 = f'''<div class="pg"><span class="rh-src">{esc(d['kicker'])}</span>
{row(232, tile('c4', f'<span class="k">{esc(d["kicker"])}</span><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div>'),
         tile('c2 red', f'<span class="k">The call</span><div class="giant">2+1</div><div class="big">{esc(d["verdict_strong"])}</div>'))}
{row(286, img('c3', 'A04.jpg', 'Sagrada Família — the nave. The interior is the argument.', '50% 42%'), stack(d, {0, 1, 2}))}
{row(344, tile('c3', f'<p>{P[0]}</p><p>{P[1]}</p>'), tile('c3', f'<p>{P[2]}</p><p>{P[3]}</p>'))}
</div>
<div class="pg">
{row(250, tile('c3 blue pull', '<div class="q">Two is a schedule. Four is a timetable, and a timetable is the thing that makes people describe a holiday as exhausting.</div>'),
         tile('c3', f'<p>{P[4]}</p><p style="margin-top:10px">{d["verdict_rest"]}</p>'))}
{row(170, forks(d))}
{row(360, img('c4', 'p-d06.jpg', 'Park Güell — the monumental zone. Timed and slotted; the terrace and the view.', '50% 60%'), note(d))}
</div>'''

d = CH['d01']; P = d['paras']
svg01 = map_svg({'#F2F7F5': '#FFFFFF', '#0B4E70': '#1B2622', '#5B6B66': '#6B7773', '#A23520': '#A23520'}, scale=1.5,
                fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'Outfit, sans-serif'})
d01 = f'''<div class="pg"><span class="rh-src">{esc(d['kicker'])}</span>
{row(232, tile('c4', f'<span class="k">{esc(d["kicker"])}</span><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div>'),
         tile('c2 gold', f'<span class="k">The call</span><div class="giant" style="font-size:38px">Eixample</div><div class="big">{esc(d["verdict_strong"])}</div>'))}
{row(420, tile('c3 mapt', svg01, 'padding:10px'), stack(d, {0}, 'blue').replace('class="t blue"', 'class="t blue" style="color:#fff"'))}
{row(208, tile('c3', f'<p>{P[0]}</p>'), img('c3', 'A01.jpg', 'The grid from above — geometric before it is anything else.', '50% 50%'))}
</div>
<div class="pg">
{row(240, tile('c3', f'<p>{P[1]}</p>'), tile('c3', f'<p>{P[2]}</p><p style="margin-top:10px">{d["verdict_rest"]}</p>'))}
{row(190, forks(d))}
{row(330, img('c2', 'h-contract.jpg', 'El Born — the medieval city, the trade for quiet.', '50% 50%'),
         tile('c2 blue pull', '<div class="q">There are no bad areas on this list.</div>'), note(d))}
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 8 — La Mosaïque</title><style>{CSS}</style></head><body>{d06}{d01}</body></html>'
write(html)
