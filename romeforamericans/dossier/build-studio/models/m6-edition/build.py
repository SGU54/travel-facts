# -*- coding: utf-8 -*-
"""ROME · Clàudia Ferrer — L'ÉDITION, in La Tavola's palette. The photograph opens; the words arrive under it."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Fraunces';src:url('%(F)sFraunces.ttf');font-weight:100 900;}
@font-face{font-family:'Fraunces';src:url('%(F)sFraunces-Italic.ttf');font-weight:100 900;font-style:italic;}
@font-face{font-family:'Newsreader';src:url('%(F)sNewsreader.ttf');font-weight:200 800;}
@font-face{font-family:'Newsreader';src:url('%(F)sNewsreader-Italic.ttf');font-weight:200 800;font-style:italic;}
@font-face{font-family:'DM';src:url('%(F)sDMSans.ttf');font-weight:100 1000;}
@font-face{font-family:'Plex';src:url('%(F)sDMSans.ttf');font-weight:100 1000;}
@font-face{font-family:'Public';src:url('%(F)sDMSans.ttf');font-weight:100 1000;}
:root{ --paper:#EFE4CC; --ink:#2B241A; --grey:#6A5C42; --sect:#8A3324; --tint:#E4D6B8; --gold:#C9A94A; --red:#8A3324; --line:#D8C7A4; }
@page{ @top-left{ content:"Rome, Solved."; font-family:'DM'; font-size:8px; font-weight:500; letter-spacing:.16em; text-transform:uppercase; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'DM'; font-size:8px; font-weight:500; letter-spacing:.16em; text-transform:uppercase; color:var(--sect); }
       @bottom-left{ content:"Rome for Americans"; font-family:'Fraunces'; font-style:italic; font-size:9px; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'DM'; font-weight:600; font-size:9px; color:var(--ink); } }
@page opener{ @top-left{content:none} @top-right{content:none} }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Newsreader'; font-size:11px; line-height:16px; color:var(--ink); font-variation-settings:'opsz' 12; }
i.mk{ color:var(--sect); font-weight:400; }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; } .pg.op{ page:opener; }
.hero{ margin:-92px -82px 0; width:816px; height:600px; overflow:hidden; position:relative; }
.hero img{ width:100%%; height:100%%; object-fit:cover; display:block; }
.hero .cap{ position:absolute; left:82px; bottom:14px; color:#fff; font-family:'DM'; font-size:8.5px; font-weight:500; letter-spacing:.1em; text-transform:uppercase; text-shadow:0 1px 6px rgba(0,0,0,.6); }
.open{ display:grid; grid-template-columns:1fr 201.3px; column-gap:24px; padding-top:26px; align-items:start; }
.sect{ font-family:'DM'; font-weight:600; font-size:9px; letter-spacing:.22em; text-transform:uppercase; color:var(--sect); margin:0 0 10px; display:flex; align-items:center; gap:10px; }
.sect::after{ content:''; flex:1; height:1px; background:var(--sect); opacity:.5; }
h1{ font-family:'Fraunces'; font-weight:600; font-size:44px; line-height:.98; letter-spacing:-.015em; margin:0 0 12px; font-variation-settings:'opsz' 144,'SOFT' 50; }
.sf{ font-family:'Newsreader'; font-style:italic; font-size:16px; line-height:22px; margin:0; font-variation-settings:'opsz' 18; }
.call{ border-top:2px solid var(--sect); padding-top:8px; margin-top:4px; }
.call .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:7px; }
.call .big{ font-family:'Fraunces'; font-weight:500; font-size:14.5px; line-height:18px; margin:0 0 7px; font-variation-settings:'opsz' 36,'SOFT' 100; }
.call p{ margin:0; font-size:10.5px; line-height:15px; }
.cols{ display:grid; grid-template-columns:314px 314px; column-gap:24px; align-items:start; }
.cols p{ margin:0 0 9px; text-align:justify; hyphens:auto; }
.cols p.lede::first-letter{ font-family:'Fraunces'; font-weight:600; font-size:46px; line-height:36px; float:left; padding:3px 6px 0 0; color:var(--sect); font-variation-settings:'opsz' 144,'SOFT' 100; }
.side{ background:var(--tint); padding:12px 14px 8px; margin:0 0 12px; }
.side .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:8px; }
.side .r{ padding:5px 0 6px; border-top:1px solid rgba(138,51,36,.25); }
.side .opt{ font-family:'Fraunces'; font-weight:600; font-size:12px; line-height:15px; font-variation-settings:'opsz' 36; }
.side .sub{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:1px; }
.side .v{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase; margin-top:3px; color:var(--ink); }
.side .r.pick .v{ color:var(--sect); }
figure.band{ margin:0 0 16px; } figure.band img{ display:block; width:100%%; height:168px; object-fit:cover; }
figcaption{ font-family:'DM'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:6px; } figcaption b{ color:var(--ink); font-weight:600; }
figure.mapf{ margin:0 0 14px; } figure.mapf svg{ display:block; width:100%%; height:auto; }
.forks{ border-top:1px solid var(--line); padding-top:8px; margin-top:4px; }
.forks .lab{ font-family:'DM'; font-weight:600; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--sect); display:block; margin-bottom:6px; }
.forks .q{ font-family:'Fraunces'; font-style:italic; font-weight:500; font-size:12px; line-height:14px; margin:0 0 2px; font-variation-settings:'opsz' 36; }
.forks p{ margin:0 0 7px; font-size:10px; line-height:13px; text-align:left; }
.note{ border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding:8px 0; margin-top:6px; font-size:10px; line-height:14px; display:grid; grid-template-columns:96px 1fr; column-gap:14px; }
.note .lab{ font-family:'DM'; font-weight:700; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--red); }
.note p{ margin:0; } .note .x{ font-style:italic; color:var(--grey); }
''' % {'F': FONTS}

def side(d, picks, tail=''):
    return '<div class="side"><span class="lab">%s</span>' % esc(d['ledger_caption']) + ''.join(
        f'<div class="r{" pick" if i in picks else ""}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}{tail}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
def forks(d):
    out = '<div class="forks">'; last = None
    for f in d['forks']:
        if f['lab'] != last: out += f'<span class="lab">{esc(f["lab"])}</span>'; last = f['lab']
        out += f'<div class="q">{esc(f["strong"])}</div><p>{esc(f["text"])}</p>'
    return out + '</div>'
def note(d): return f'<div class="note"><span class="lab"><i class="mk">◆</i> Volatile 2026</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'
def opener(d, src, cap, pos='50% 50%'):
    return f'''<div class="pg op"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="hero"><img src="{photo(src)}" style="object-position:{pos}"><div class="cap">{cap}</div></div>
  <div class="open"><div><div class="sect">{esc(d['kicker'])}</div><h1>{esc(d['title'])}</h1><div class="sf">{d['standfirst']}</div></div>
    <div class="call"><span class="lab">In short</span><div class="big">{esc(d['verdict_strong'])}</div><p>{d['verdict_rest']}</p></div></div></div>'''

d = CH['d01']; P = d['paras']
svg01 = map_svg({'#F2F7F5': '#E9DDC4', '#0E6390': '#6A5C42', '#0B4E70': '#2B241A', '#A23520': '#8A3324', '#1B2622': '#2B241A', '#5B6B66': '#6A5C42'}, scale=1.4,
                fonts={'Plex, monospace': 'DM, sans-serif', 'Public, sans-serif': 'DM, sans-serif'})
d01 = opener(d, 'forum.jpg', 'The Forum from above — one connected pedestrian district you cross on foot in well under an hour.', '50% 55%') + f'''
<div class="pg">
  <div class="cols" style="grid-template-columns:426.7px 201.3px"><figure class="mapf">{svg01}<figcaption><b>The walkable core.</b> {esc(d['figure_cap'].split('·',1)[-1].strip())}</figcaption></figure>{side(d, {0, 1}, ' to the core')}</div>
  <div class="cols"><div><p class="lede">{P[0]}</p><p>{P[1]}</p></div><div><p>{P[2]}</p></div></div>
</div>
<div class="pg">
  <figure class="band"><img src="{photo('d01-lane.jpg')}" style="height:250px;object-position:50% 35%"><figcaption><b>Inside the core.</b> {esc(d['photos'][1]['cap'])}</figcaption></figure>
  <div class="cols"><div><p>{P[3]}</p></div><div>{forks(d)}{note(d)}</div></div>
</div>'''

d = CH['d05']; P = d['paras']
d05 = opener(d, 'd05-gallery.jpg', 'The Borghese Gallery — everyone inside already holds a booked slot; there is no line for a “skip” product to skip.', '50% 45%') + f'''
<div class="pg">
  <figure class="band"><img src="{photo('stpeters.jpg')}" style="object-position:50% 30%"><figcaption><b>St Peter’s.</b> Free entry; the wait is security, and no admission product bypasses it.</figcaption></figure>
  <div class="cols"><div><p class="lede">{P[0]}</p><p>{P[1]}</p></div>
    <div>{side(d, {0, 1, 2})}<p>{P[2]}</p></div></div>
</div>
<div class="pg">
  <div class="cols"><div><p>{P[3]}</p><p>{P[4]}</p></div><div>{forks(d)}{note(d)}</div></div>
  <figure class="band" style="margin-top:14px"><img src="{photo('borghese.jpg')}" style="height:210px"><figcaption><b>The Borghese.</b> {esc(d['photos'][1]['cap'])}</figcaption></figure>
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Rome — L\'Édition</title><style>{CSS}</style></head><body>{d01}{d05}</body></html>'
write(html)
