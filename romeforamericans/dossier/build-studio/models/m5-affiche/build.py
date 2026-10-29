# -*- coding: utf-8 -*-
"""ROME · Marta Serra — L'AFFICHE, in La Tavola's palette (wax red, plate gilt, foxed paper, iron-gall ink).
Decision 01 (the base, a map decision) and Decision 05 (the Vatican, a photograph decision)."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Archivo';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@font-face{font-family:'Archivo';src:url('%(F)sArchivo-Italic.ttf');font-weight:100 900;font-stretch:62%% 125%%;font-style:italic;}
@font-face{font-family:'Plex';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@font-face{font-family:'Public';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
:root{ --paper:#EFE4CC; --ink:#2B241A; --red:#8A3324; --gold:#C9A94A; --sepia:#6A5C42; --grey:#6A5C42; --line:#2B241A; }
@page{ @top-left{ content:none } @top-right{ content:none } @bottom-center{ content:none }
       @bottom-left{ content:"Rome, Solved."; font-family:'Archivo'; font-size:8.5px; font-weight:500; letter-spacing:.06em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Archivo'; font-weight:700; font-size:10px; color:var(--ink); } }
@page poster{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Archivo'; font-size:11px; line-height:17px; color:var(--ink); }
i.mk{ font-weight:400; font-stretch:100%%; color:var(--red); }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.poster{ page:poster; width:8.5in; height:11in; box-sizing:border-box; padding:64px 82px 60px; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.poster.red{ background:var(--red); color:var(--paper); } .poster.gold{ background:var(--gold); color:var(--ink); }
.poster .slug{ font-size:9px; font-weight:600; letter-spacing:.22em; text-transform:uppercase; display:flex; justify-content:space-between; }
.poster .giant{ font-weight:800; font-stretch:118%%; line-height:.8; letter-spacing:-.045em; margin:34px 0 0 -6px; }
.poster .under{ font-size:14px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; margin-top:18px; }
.poster .foot{ margin-top:auto; display:grid; grid-template-columns:1fr 300px; column-gap:40px; align-items:end; }
.poster .big{ font-size:30px; line-height:33px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.poster .foot p{ margin:0; font-size:12px; line-height:17px; font-weight:400; }
.poster.red .foot p{ color:#F3E3D6; }
.photo{ page:poster; width:8.5in; height:11in; box-sizing:border-box; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.photo img{ display:block; width:100%%; height:740px; object-fit:cover; }
.photo .tail{ padding:28px 82px 0; display:grid; grid-template-columns:340px 1fr; column-gap:48px; }
.photo .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-bottom:10px; }
.photo p{ margin:0; }
.photo .vol{ border-top:3px solid var(--red); padding-top:8px; }
.photo .vol .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.photo .vol p{ font-size:10px; line-height:14px; } .photo .vol .x{ color:var(--grey); }
h1{ font-weight:800; font-stretch:88%%; font-size:54px; line-height:.92; letter-spacing:-.035em; margin:0 0 14px; }
.sf{ font-weight:300; font-size:15.5px; line-height:21px; width:430px; margin:0 0 26px; }
.grid{ display:grid; grid-template-columns:340px 264px; column-gap:48px; align-items:start; }
.prose p{ margin:0 0 11px; text-align:left; hyphens:auto; }
.prose p:first-child::first-line{ font-weight:600; }
.stack{ border-top:3px solid var(--line); }
.stack .it{ padding:10px 0 11px; border-bottom:1px solid var(--line); }
.stack .opt{ font-size:19px; line-height:21px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.stack .it.pick .opt::before{ content:''; display:inline-block; width:11px; height:11px; background:var(--red); margin:0 8px 1px 0; }
.stack .sub{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:3px; }
.stack .v{ font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; margin-top:5px; }
.stack .it.pick .v{ color:var(--red); }
.stack .lab{ font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; padding:6px 0 2px; }
.forks{ margin-top:22px; border-top:3px solid var(--line); }
.forks .it{ padding:9px 0 10px; border-bottom:1px solid var(--line); }
.forks .k{ color:var(--red); font-size:8.5px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:3px; }
.forks .q{ font-size:14px; line-height:16px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; margin-bottom:3px; }
.forks p{ margin:0; font-size:10px; line-height:14px; }
.mapwrap svg{ display:block; width:100%%; height:auto; }
.mapwrap .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
.ribbon{ display:grid; grid-template-columns:repeat(5,1fr); column-gap:16px; border-top:3px solid var(--line); margin-top:18px; }
.ribbon .it{ padding:10px 0 0; } .ribbon .it + .it{ border-left:1px solid var(--line); padding-left:12px; margin-left:-10px; }
.ribbon .opt{ font-size:14px; line-height:16px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.ribbon .sub{ font-size:9px; line-height:12px; color:var(--grey); margin-top:4px; }
.ribbon .v{ font-size:11px; font-weight:800; letter-spacing:.06em; margin-top:5px; }
.ribbon .it.pick .v{ color:var(--red); } .ribbon .it.pick .opt::before{ content:''; display:inline-block; width:10px; height:10px; background:var(--red); margin:0 7px 0 0; }
.note{ border-top:3px solid var(--red); padding-top:8px; margin-top:22px; }
.note .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.note p{ margin:0; font-size:10px; line-height:14px; } .note .x{ color:var(--grey); }
figure.band{ margin:22px 0 0; } figure.band img{ display:block; width:100%%; height:250px; object-fit:cover; }
figure.band figcaption{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
''' % {'F': FONTS}

def stack(d, picks):
    return '<div class="stack"><span class="lab">%s</span>' % esc(d['ledger_caption']) + ''.join(
        f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
def ribbon(d, picks):
    return '<div class="ribbon">' + ''.join(
        f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])} walk</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
def forks(d):
    return '<div class="forks">' + ''.join(f'<div class="it"><span class="k">{esc(f["lab"])}</span><div class="q">{esc(f["strong"])}</div><p>{esc(f["text"])}</p></div>' for f in d['forks']) + '</div>'
def note(d, cls='note'):
    return f'<div class="{cls}"><span class="lab"><i class="mk">◆</i> Volatile · 2026</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'

d = CH['d01']
svg01 = map_svg({'#F2F7F5': '#EFE4CC', '#0E6390': '#2B241A', '#0B4E70': '#2B241A', '#A23520': '#8A3324', '#1B2622': '#2B241A'}, scale=1.35,
                fonts={'Plex, monospace': 'Archivo, sans-serif', 'Public, sans-serif': 'Archivo, sans-serif'})
d01 = f'''<div class="poster gold"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span>Where to sleep</span></div>
  <div class="giant" style="font-size:330px">13′</div>
  <div class="under">Minutes on foot to the centre, from the core. From Termini: thirty-five.</div>
  <div class="foot"><div class="big">{esc(d['verdict_strong'])}</div><p>{d['verdict_rest']}</p></div>
</div>
<div class="pg">
  <div class="mapwrap">{svg01}<div class="cap">The walkable core, the classic sights inside it, Termini’s 35-minute walk drawn to scale — the picks in red</div></div>
  {ribbon(d, {0, 1})}
  <div class="grid" style="margin-top:22px"><div class="prose"><p>{d['paras'][0]}</p></div></div>
</div>
<div class="pg">
  <h1>{esc(d['title'])}</h1>
  <div class="sf">{d['standfirst']}</div>
  <div class="grid"><div class="prose"><p>{d['paras'][1]}</p><p>{d['paras'][2]}</p></div><div>{forks(d)}{note(d)}</div></div>
</div>
<div class="photo"><img src="{photo('d01-lane.jpg')}" style="object-position:50% 35%">
  <div class="tail"><div><div class="cap">{esc(d['photos'][1]['cap'])}</div><p>{d['paras'][3]}</p></div></div>
</div>'''

d = CH['d05']
d05 = f'''<div class="poster red"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span>Skip the line</span></div>
  <div class="giant" style="font-size:170px;font-stretch:92%">TWO<br>LINES.</div>
  <div class="under">The ticket line and the security line. The expensive ticket touches one.</div>
  <div class="foot"><div class="big">{esc(d['verdict_strong'])}</div><p>{d['verdict_rest']}</p></div>
</div>
<div class="pg">
  <h1>{esc(d['title'])}</h1>
  <div class="sf">{d['standfirst']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in d['paras'][:3])}</div>
    <div>{stack(d, {0, 1, 2})}</div></div>
</div>
<div class="pg">
  <div class="grid"><div class="prose"><p>{d['paras'][3]}</p></div><div>{forks(d)}</div></div>
  <figure class="band"><img src="{photo('stpeters.jpg')}" style="object-position:50% 30%"><figcaption>St Peter’s — free entry; the wait is security, which nothing you can buy bypasses.</figcaption></figure>
</div>
<div class="photo"><img src="{photo('d05-gallery.jpg')}" style="object-position:50% 45%">
  <div class="tail"><div><div class="cap">The Borghese Gallery — {esc(d['photos'][0]['cap'])}</div><p>{d['paras'][4]}</p></div>{note(d, 'vol')}</div>
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Rome — L\'Affiche</title><style>{CSS}</style></head><body>{d01}{d05}</body></html>'
write(html)
