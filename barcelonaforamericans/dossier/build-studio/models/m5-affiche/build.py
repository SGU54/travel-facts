# -*- coding: utf-8 -*-
"""MODEL 5 — L'AFFICHE. The poster designer (Müller-Brockmann by way of Barcelona '92).
One page, one thing. The verdict is a poster: a field of colour and a number you can
read from across the room. Colour is structure — a red page, a paper page, a
photograph page — never decoration. Type is huge or small, nothing in between. One
narrow column of prose, ragged, with air around it. One photograph per chapter, full
bleed, cropped hard. Nothing boxed; the grid is the only furniture."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Archivo';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@font-face{font-family:'Archivo';src:url('%(F)sArchivo-Italic.ttf');font-weight:100 900;font-stretch:62%% 125%%;font-style:italic;}
@font-face{font-family:'Plex';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
@font-face{font-family:'Public';src:url('%(F)sArchivo.ttf');font-weight:100 900;font-stretch:62%% 125%%;}
:root{ --paper:#F4F2EC; --ink:#17201C; --red:#A23520; --gold:#E0A828; --blue:#0E6390; --grey:#6B7773; --line:#17201C; }
@page{ @top-left{ content:none } @top-right{ content:none } @bottom-center{ content:none }
       @bottom-left{ content:"Barcelona, Without the Traps."; font-family:'Archivo'; font-size:8.5px; font-weight:500; letter-spacing:.06em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Archivo'; font-weight:700; font-size:10px; color:var(--ink); } }
@page poster{ margin:0; @top-left{content:none} @top-right{content:none} @bottom-left{content:none} @bottom-center{content:none} @bottom-right{content:none} }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Archivo'; font-size:11px; line-height:17px; color:var(--ink); }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.poster{ page:poster; width:8.5in; height:11in; box-sizing:border-box; padding:64px 82px 60px; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.poster.red{ background:var(--red); color:var(--paper); } .poster.gold{ background:var(--gold); color:var(--ink); }
.poster .slug{ font-size:9px; font-weight:600; letter-spacing:.22em; text-transform:uppercase; display:flex; justify-content:space-between; }
.poster .giant{ font-weight:800; font-stretch:118%%; line-height:.8; letter-spacing:-.045em; margin:34px 0 0 -6px; }
.poster .under{ font-size:14px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; margin-top:18px; }
.poster .foot{ margin-top:auto; display:grid; grid-template-columns:1fr 300px; column-gap:40px; align-items:end; }
.poster .big{ font-size:30px; line-height:33px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.poster .foot p{ margin:0; font-size:12px; line-height:17px; font-weight:400; }
.poster.red .foot p{ color:#F8E9E3; }
.photo{ page:poster; width:8.5in; height:11in; box-sizing:border-box; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.photo img{ display:block; width:100%%; height:740px; object-fit:cover; }
.photo .tail{ padding:28px 82px 0; display:grid; grid-template-columns:340px 1fr; column-gap:48px; }
.photo .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-bottom:10px; }
.photo p{ margin:0; }
.photo .vol{ border-top:3px solid var(--red); padding-top:8px; }
.photo .vol .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.photo .vol p{ font-size:10px; line-height:14px; }
.photo .vol .x{ color:var(--grey); }
h1{ font-weight:800; font-stretch:88%%; font-size:58px; line-height:.92; letter-spacing:-.035em; margin:0 0 14px; }
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
.forks .it{ padding:10px 0 11px; border-bottom:1px solid var(--line); }
.forks .q{ font-size:16px; line-height:18px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; margin-bottom:4px; }
.forks p{ margin:0; font-size:10px; line-height:14px; }
.mapwrap svg{ display:block; width:100%%; height:auto; }
.mapwrap .cap{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
.ribbon{ display:grid; grid-template-columns:repeat(4,1fr); column-gap:24px; border-top:3px solid var(--line); margin-top:18px; }
.ribbon .it{ padding:10px 0 0; } .ribbon .it + .it{ border-left:1px solid var(--line); padding-left:14px; margin-left:-12px; }
.ribbon .opt{ font-size:15px; line-height:17px; font-weight:700; letter-spacing:-.02em; font-stretch:92%%; }
.ribbon .sub{ font-size:9px; line-height:12px; color:var(--grey); margin-top:4px; }
.ribbon .v{ font-size:8.5px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; margin-top:5px; }
.ribbon .it.pick .v{ color:var(--red); } .ribbon .it.pick .opt::before{ content:''; display:inline-block; width:10px; height:10px; background:var(--red); margin:0 7px 0 0; }
.note{ border-top:3px solid var(--red); padding-top:8px; margin-top:22px; }
.note .lab{ color:var(--red); font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; display:block; margin-bottom:5px; }
.note p{ margin:0; font-size:10px; line-height:14px; } .note .x{ color:var(--grey); }
figure.band{ margin:22px 0 0; } figure.band img{ display:block; width:100%%; height:262px; object-fit:cover; }
figure.band figcaption{ font-size:9px; line-height:13px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:8px; }
''' % {'F': FONTS}

def stack(d, picks):
    return '<div class="stack"><span class="lab">%s</span>' % esc(d['ledger_caption']) + ''.join(
        f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'

def ribbon(d, picks):
    return '<div class="ribbon">' + ''.join(
        f'<div class="it{" pick" if i in picks else ""}"><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'

def forks(d):
    return '<div class="forks">' + ''.join(f'<div class="it"><div class="q">{esc(f["strong"])}</div><p>{f["text"]}</p></div>' for f in d['forks']) + '</div>'

def note(d, cls='note'):
    lab = '<i class="mk">◆</i> Volatile · 2026' if d['volatile'] else 'Since 2019'
    return f'<div class="{cls}"><span class="lab">{lab}</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'

# ── d06 ────────────────────────────────────────────────────────────────────────
d = CH['d06']
d06 = f'''<div class="poster red"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span>{esc(d['title'])}</span></div>
  <div class="giant" style="font-size:330px">2+1</div>
  <div class="under">Two ticketed Gaudí sites. One house. The rest from the street.</div>
  <div class="foot"><div class="big">{esc(d['verdict_strong'])}</div><p>{d['verdict_rest']}</p></div>
</div>
<div class="pg">
  <h1>{esc(d['title'])}</h1>
  <div class="sf">{d['standfirst']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in d['paras'][:4])}</div>
    <div>{stack(d, {0, 1, 2})}{forks(d)}</div></div>
</div>
<div class="photo"><img src="{photo('A04.jpg')}" style="object-position:50% 40%">
  <div class="tail"><div><div class="cap">Sagrada Família, the nave — {esc(d['photos'][0]['cap'])}</div><p>{d['paras'][4]}</p></div>{note(d, 'vol')}</div>
</div>'''

# ── d01 ────────────────────────────────────────────────────────────────────────
d = CH['d01']
svg01 = map_svg({'#F2F7F5': '#F4F2EC', '#0E6390': '#17201C', '#0B4E70': '#17201C', '#E0A828': '#A23520', '#A23520': '#6B7773', '#5B6B66': '#6B7773'}, scale=1.5,
                fonts={'Plex, monospace': 'Archivo, sans-serif', 'Public, sans-serif': 'Archivo, sans-serif'})
svg01 = svg01.replace('fill="#A23520" opacity="0.6"', 'fill="#17201C" opacity="0.35"')   # the sea label
d01 = f'''<div class="poster gold"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span>{esc(d['title'])}</span></div>
  <div class="giant" style="font-size:150px;font-stretch:80%">EIXAMPLE</div>
  <div class="under">First trip, no special agenda — and it isn't close.</div>
  <div class="foot"><div class="big">Central, quiet at night, deepest hotel stock, and it puts Gaudí's front doors on your walking route.</div><p>{d['verdict_rest'].split('Choose El Born', 1)[1].join(['Choose El Born', ''])}</p></div>
</div>
<div class="pg">
  <div class="mapwrap">{svg01}<div class="cap">{esc(d['figure_cap'].split('·',1)[-1].strip())} — the default in red</div></div>
  {ribbon(d, {0})}
</div>
<div class="pg">
  <h1>{esc(d['title'])}</h1>
  <div class="sf">{d['standfirst']}</div>
  <div class="grid"><div class="prose">{''.join('<p>%s</p>' % p for p in d['paras'])}</div><div>{forks(d)}{note(d)}</div></div>
  <figure class="band"><img src="{photo('A01.jpg')}" style="object-position:50% 50%"><figcaption>The grid from above — {esc(d['photos'][0]['cap'].split('.',1)[1].strip())}</figcaption></figure>
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 5 — L\'Affiche</title><style>{CSS}</style></head><body>{d06}{d01}</body></html>'
write(html)
