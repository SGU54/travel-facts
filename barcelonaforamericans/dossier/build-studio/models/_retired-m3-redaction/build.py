# -*- coding: utf-8 -*-
"""MODEL 3 — LA RÉDACTION. The broadsheet art director.
The page is a front page: hierarchy is the whole art, columns are narrow because
the eye reads forty characters fast, the headline is the chapter, the deck is the
standfirst, THE CALL is boxed beside the photograph like a news summary, and
nothing floats — everything sits on a rule. Photographs run once, large, in ink."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Playfair';src:url('%(F)sPlayfairDisplay.ttf');font-weight:400 900;}
@font-face{font-family:'Playfair';src:url('%(F)sPlayfairDisplay-Italic.ttf');font-weight:400 900;font-style:italic;}
@font-face{font-family:'Serif4';src:url('%(F)sSourceSerif4.ttf');font-weight:200 900;}
@font-face{font-family:'Serif4';src:url('%(F)sSourceSerif4-Italic.ttf');font-weight:200 900;font-style:italic;}
@font-face{font-family:'Franklin';src:url('%(F)sLibreFranklin.ttf');font-weight:100 900;}
/* the map's own font names, mapped into this dialect */
@font-face{font-family:'Plex';src:url('%(F)sLibreFranklin.ttf');font-weight:100 900;}
@font-face{font-family:'Public';src:url('%(F)sLibreFranklin.ttf');font-weight:100 900;}
:root{ --paper:#FBFAF6; --ink:#141A18; --rule:#141A18; --hair:#B9C0BC; --grey:#5B6B66;
  --spot:#A23520; --gold:#E0A828; --tint:#EEEBE2; }
@page{ @top-left{ content:"Barcelona, Without the Traps."; font-family:'Franklin'; font-weight:600; font-size:8px; letter-spacing:.18em; text-transform:uppercase; color:var(--ink); }
       @top-right{ content:string(rh, last); font-family:'Franklin'; font-weight:600; font-size:8px; letter-spacing:.18em; text-transform:uppercase; color:var(--ink); }
       @bottom-left{ content:"Barcelona for Americans"; font-family:'Playfair'; font-style:italic; font-size:9px; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Playfair'; font-weight:700; font-size:11px; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Serif4'; font-size:10.5px; line-height:14px; color:var(--ink); font-variation-settings:'opsz' 10; }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.slug{ display:flex; justify-content:space-between; align-items:baseline; border-top:1px solid var(--rule); border-bottom:3px solid var(--rule);
  padding:5px 0 4px; font-family:'Franklin'; font-weight:700; font-size:9px; letter-spacing:.2em; text-transform:uppercase; }
.slug .r{ font-weight:400; color:var(--grey); letter-spacing:.14em; }
h1{ font-family:'Playfair'; font-weight:900; font-size:64px; line-height:.94; letter-spacing:-.022em; margin:16px 0 10px; color:var(--ink); }
.deck{ font-family:'Serif4'; font-style:italic; font-size:16.5px; line-height:21px; width:540px; color:var(--ink); margin:0 0 14px; font-variation-settings:'opsz' 18; }
.row{ display:grid; grid-template-columns:426.7px 201.3px; column-gap:24px; align-items:start; margin:0 0 14px; }
figure{ margin:0; }
figure.ink img{ display:block; width:100%; object-fit:cover; filter:grayscale(1) sepia(.14) contrast(1.08); }
figure.ink figcaption{ font-family:'Franklin'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:5px; }
figure.ink figcaption b{ color:var(--ink); font-weight:700; text-transform:uppercase; letter-spacing:.08em; }
figure.map svg{ display:block; width:100%; height:auto; border:1px solid var(--hair); }
figure.map figcaption{ font-family:'Franklin'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:5px; }
.call{ border-top:3px solid var(--rule); padding-top:6px; }
.lab{ font-family:'Franklin'; font-weight:700; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; display:block; margin:0 0 6px; }
.call .big{ font-family:'Playfair'; font-weight:700; font-size:16.5px; line-height:19px; letter-spacing:-.005em; margin:0 0 7px; }
.call p{ margin:0; text-align:left; hyphens:auto; }
.body3{ column-count:3; column-gap:24px; column-rule:1px solid var(--hair); border-top:1px solid var(--hair); padding-top:10px; }
.body3 p{ margin:0 0 7px; text-align:justify; hyphens:auto; orphans:2; widows:2; }
.body3 p.lede::first-letter{ font-family:'Playfair'; font-weight:900; font-size:40px; line-height:30px; float:left; padding:4px 5px 0 0; }
.glance{ border-top:3px solid var(--rule); }
.glance .row2{ display:grid; grid-template-columns:1fr 128px; column-gap:12px; padding:7px 0 6px; border-bottom:1px solid var(--hair); }
.glance .opt{ font-family:'Playfair'; font-weight:700; font-size:12px; line-height:14px; }
.glance .sub{ font-size:9.5px; line-height:12px; color:var(--grey); margin-top:2px; }
.glance .v{ font-family:'Franklin'; font-weight:700; font-size:9px; line-height:12px; letter-spacing:.06em; text-transform:uppercase; text-align:right; padding-top:1px; }
.glance .row2.pick .v{ color:var(--spot); }
.glance .cap{ font-family:'Franklin'; font-size:8.5px; color:var(--grey); margin-top:6px; }
.forks{ border-top:3px solid var(--rule); }
.fork{ padding:7px 0 8px; border-bottom:1px solid var(--hair); }
.fork .q{ font-family:'Playfair'; font-weight:700; font-size:12px; line-height:14px; margin:0 0 3px; }
.fork p{ margin:0; text-align:left; hyphens:auto; }
.strip{ background:var(--tint); border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); padding:8px 12px; margin:14px 0; display:grid; grid-template-columns:112px 1fr; column-gap:16px; }
.strip .lab{ margin:0; color:var(--spot); }
.strip p{ margin:0; text-align:left; } .strip .x{ font-style:italic; color:var(--grey); }
.plate img{ height:%(PH)spx; }
'''.replace('%(F)s', FONTS).replace('%(PH)s', '420')

def ledger(d, picks):
    rows = ''.join('<div class="row2%s"><div><div class="opt">%s</div><div class="sub">%s</div></div><div class="v">%s</div></div>'
                   % (' pick' if i in picks else '', r['opt'], esc(r['sub']), esc(r['call'])) for i, r in enumerate(d['ledger']))
    return '<div class="glance"><span class="lab" style="padding-top:6px">At a glance</span>%s<div class="cap">%s</div></div>' % (rows, esc(d['ledger_caption']))

def forks(d):
    return '<div class="forks"><span class="lab" style="padding-top:6px">If you are not the default reader</span>' + ''.join(
        '<div class="fork"><div class="q">%s</div><p>%s</p></div>' % (esc(f['strong']), f['text']) for f in d['forks']) + '</div>'

def strip(d):
    lab = ('<i class="mk">◆</i> Volatile · 2026' if d['volatile'] else 'What changed')
    return '<div class="strip"><span class="lab">%s</span><p>%s <span class="x">%s</span></p></div>' % (lab, d['note'], esc(d['note_xref']))

def chapter(sid, hero_html, picks, page2_photo, body_paras_p1):
    d = CH[sid]
    paras = ''.join('<p%s>%s</p>' % (' class="lede"' if i == 0 else '', p) for i, p in enumerate(d['paras']))
    p1 = f'''<div class="pg"><span class="rh-src">{esc(d['kicker'])}</span>
  <div class="slug"><span>{esc(d['kicker'])}</span><span class="r">First trip · 3–5 days</span></div>
  <h1>{esc(d['title'])}</h1>
  <div class="deck">{d['standfirst']}</div>
  <div class="row">{hero_html}
    <div class="call"><span class="lab">The call</span><div class="big">{esc(d['verdict_strong'])}</div><p>{d['verdict_rest']}</p></div></div>
  <div class="body3">{paras}</div>
</div>'''
    ph = page2_photo
    p2 = f'''<div class="pg">
  <div class="row">{ledger(d, picks)}{forks(d)}</div>
  {strip(d)}
  <figure class="ink plate"><img src="{photo(ph['src'])}"><figcaption><b>Plate</b> &nbsp;{esc(ph['cap'])}</figcaption></figure>
</div>'''
    return p1 + p2

d06 = CH['d06']
hero06 = '<figure class="ink"><img src="%s" style="height:300px"><figcaption><b>Sagrada Família</b> &nbsp;%s</figcaption></figure>' % (photo('A04.jpg'), esc(d06['photos'][0]['cap']))
d01 = CH['d01']
svg01 = map_svg({'#F2F7F5': '#F3F1EA', '#0E6390': '#141A18', '#0B4E70': '#141A18', '#E0A828': '#E0A828', '#A23520': '#A23520', '#5B6B66': '#5B6B66'}, scale=1.55,
                fonts={'Plex, monospace': 'Franklin, sans-serif', 'Public, sans-serif': 'Franklin, sans-serif'})
hero01 = '<figure class="map">%s<figcaption><b style="color:#141A18;text-transform:uppercase;letter-spacing:.08em;font-weight:700">Map</b> &nbsp;%s</figcaption></figure>' % (svg01, esc(d01['figure_cap']))

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 3 — La Rédaction</title><style>{CSS}</style></head><body>
{chapter('d06', hero06, {0, 1, 2}, {'src': 'p-d06.jpg', 'cap': d06['photos'][1]['cap']}, 5)}
{chapter('d01', hero01, {0}, {'src': 'A03.jpg', 'cap': d01['photos'][0]['cap']}, 3)}
</body></html>'''
write(html)
