# -*- coding: utf-8 -*-
"""ROME · Mercè Oller — LA MOSAÏQUE, in La Tavola's palette: wax-red call tile, gilt picks, sepia pulls, ink notice."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Outfit';src:url('%(F)sOutfit.ttf');font-weight:100 900;}
@font-face{font-family:'Manrope';src:url('%(F)sManrope.ttf');font-weight:200 800;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'Plex';src:url('%(H)sIBMPlexMono-Regular.ttf');}
@font-face{font-family:'Public';src:url('%(F)sOutfit.ttf');font-weight:100 900;}
:root{ --paper:#E9DDC4; --tile:#F6EEDB; --ink:#2B241A; --grey:#6A5C42; --red:#8A3324; --gold:#C9A94A; --sepia:#6A5C42; --stone:#D8C7A4; --g:8px; }
@page{ @top-left{ content:"Rome, Solved."; font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--grey); }
       @bottom-left{ content:"Rome for Americans"; font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.06em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Outfit'; font-weight:700; font-size:11px; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Manrope'; font-size:10.5px; line-height:15px; color:var(--ink); }
i.mk{ color:var(--red); font-weight:400; }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.row{ display:grid; grid-template-columns:repeat(6, 1fr); column-gap:var(--g); margin-bottom:var(--g); }
.t{ background:var(--tile); padding:16px 18px; box-sizing:border-box; overflow:hidden; position:relative; }
.t.c2{ grid-column:span 2; } .t.c3{ grid-column:span 3; } .t.c4{ grid-column:span 4; } .t.c6{ grid-column:span 6; }
.t.red{ background:var(--red); color:#F6EEDB; } .t.gold{ background:var(--gold); color:var(--ink); } .t.sepia{ background:var(--sepia); color:#F6EEDB; }
.t.ink{ background:var(--ink); color:#F6EEDB; } .t.stone{ background:var(--stone); } .t.img{ padding:0; }
.t.img img{ display:block; width:100%%; height:100%%; object-fit:cover; position:absolute; inset:0; }
.t .k{ font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; display:block; margin-bottom:8px; opacity:.85; }
h1{ font-family:'Outfit'; font-weight:700; font-size:34px; line-height:.95; letter-spacing:-.025em; margin:0 0 10px; }
.sf{ font-size:12px; line-height:17px; font-weight:500; margin:0; }
.t .giant{ font-family:'Outfit'; font-weight:800; font-size:64px; line-height:.85; letter-spacing:-.04em; margin:0 0 10px; }
.t .big{ font-family:'Outfit'; font-weight:600; font-size:14px; line-height:17px; margin:0 0 6px; }
.t p{ margin:0 0 8px; text-align:left; hyphens:auto; } .t p:last-child{ margin-bottom:0; }
.stack{ display:grid; grid-auto-rows:1fr; row-gap:var(--g); grid-column:span 3; }
.stack .t{ padding:8px 14px; display:flex; flex-direction:column; justify-content:center; }
.stack .opt{ font-family:'Outfit'; font-weight:600; font-size:13px; line-height:15px; }
.stack .sub{ font-size:9px; line-height:12px; opacity:.8; margin-top:2px; }
.stack .v{ font-family:'Mono'; font-size:8px; letter-spacing:.06em; text-transform:uppercase; margin-top:3px; }
.t.pull{ display:flex; align-items:flex-end; }
.t.pull .q{ font-family:'Outfit'; font-weight:600; font-size:22px; line-height:24px; letter-spacing:-.02em; }
.t .fk{ font-family:'Outfit'; font-weight:500; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--red); display:block; margin-bottom:4px; }
.t .fq{ font-family:'Outfit'; font-weight:600; font-size:13px; line-height:15px; margin:0 0 4px; }
.t .cap{ position:absolute; left:0; right:0; bottom:0; padding:8px 12px; background:rgba(43,36,26,.82); color:#F6EEDB; font-family:'Outfit'; font-size:8.5px; letter-spacing:.06em; text-transform:uppercase; }
.t .x{ opacity:.7; } .t.ink .k{ color:var(--gold); opacity:1; }
.mapt svg{ display:block; width:100%%; height:auto; }
''' % {'F': FONTS, 'H': HOUSE}

def row(h, *tiles): return f'<div class="row" style="height:{h}px">' + ''.join(tiles) + '</div>'
def tile(cls, inner, style=''): return f'<div class="t {cls}"{" style=%r" % style if style else ""}>{inner}</div>'
def img(cls, src, cap, pos='50% 50%'): return f'<div class="t img {cls}"><img src="{photo(src)}" style="object-position:{pos}"><div class="cap">{cap}</div></div>'
def stack(d, picks, tail=''):
    return '<div class="stack">' + ''.join(
        f'<div class="t {"gold" if i in picks else "stone"}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}{tail}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
def note(d): return tile('c2 ink', f'<span class="k"><i class="mk">◆</i> Volatile · 2026</span><p style="font-size:10px;line-height:14px">{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p>')
def fork_tiles(d, span='c3'):
    out = []
    for lab in ('Follow this if', 'Overrule it if'):
        items = [f for f in d['forks'] if f['lab'] == lab]
        out.append(tile(span, f'<span class="fk">{esc(lab)}</span>' + ''.join(f'<div class="fq">{esc(f["strong"])}</div><p>{esc(f["text"])}</p>' for f in items)))
    return ''.join(out)

d = CH['d01']; P = d['paras']
svg01 = map_svg({'#F2F7F5': '#F6EEDB', '#0B4E70': '#2B241A', '#0E6390': '#6A5C42', '#A23520': '#8A3324', '#1B2622': '#2B241A', '#5B6B66': '#6A5C42'}, scale=1.45,
                fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'Outfit, sans-serif'})
d01 = f'''<div class="pg"><span class="rh-src">{esc(d['kicker'])}</span>
{row(232, tile('c4', f'<span class="k">{esc(d["kicker"])}</span><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div>'),
         tile('c2 red', f'<span class="k">The call</span><div class="giant">13′</div><div class="big">{esc(d["verdict_strong"])}</div>'))}
{row(420, tile('c3 mapt', svg01 + '<div style="font-family:Outfit;font-size:8.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--grey);margin-top:6px">The walkable core · Termini’s 35′ walk to scale</div>', 'padding:10px'), stack(d, {0, 1}, ' to the core'))}
{row(208, tile('c3', f'<p>{P[0]}</p>'), img('c3', 'd01-band.jpg', 'The Colosseum and St Peter’s — the two outer edges of a trip that is walked.', '50% 50%'))}
</div>
<div class="pg">
{row(244, tile('c3', f'<p>{P[1]}</p>'), tile('c3', f'<p>{P[2]}</p>'))}
{row(180, fork_tiles(d))}
{row(296, img('c2', 'd01-lane.jpg', 'A lane inside the core — the walk home at midnight.', '50% 40%'),
         tile('c2 sepia pull', '<div class="q">You did not save money. You spent it in the currency the trip is actually short of.</div>'), note(d))}
{row(140, tile('c6', f'<p>{P[3]}</p><p style="margin-top:8px"><b>{esc(d["verdict_strong"])}</b> {d["verdict_rest"]}</p>'))}
</div>'''

d = CH['d05']; P = d['paras']
d05 = f'''<div class="pg"><span class="rh-src">{esc(d['kicker'])}</span>
{row(232, tile('c4', f'<span class="k">{esc(d["kicker"])}</span><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div>'),
         tile('c2 red', f'<span class="k">The call</span><div class="giant" style="font-size:40px">Two lines</div><div class="big">{esc(d["verdict_strong"])}</div>'))}
{row(286, img('c3', 'd05-gallery.jpg', 'The Borghese Gallery — a booked slot already, no line to skip.', '50% 45%'), stack(d, {0, 1, 2}))}
{row(344, tile('c3', f'<p>{P[0]}</p><p>{P[1]}</p>'), tile('c3', f'<p>{P[2]}</p>'))}
</div>
<div class="pg">
{row(230, tile('c3 sepia pull', '<div class="q">A pre-booked timed ticket skips the ticket line. That’s the whole of what it does.</div>'),
         tile('c3', f'<p>{P[3]}</p>'))}
{row(180, fork_tiles(d))}
{row(280, img('c4', 'stpeters.jpg', 'St Peter’s — free entry; the wait is security, which nothing you can buy bypasses.', '50% 30%'), note(d))}
{row(170, tile('c6', f'<p>{P[4]}</p>'))}
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Rome — La Mosaïque</title><style>{CSS}</style></head><body>{d01}{d05}</body></html>'
write(html)
