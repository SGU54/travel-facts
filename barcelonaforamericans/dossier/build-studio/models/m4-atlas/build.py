# -*- coding: utf-8 -*-
"""MODEL 4 — L'ATLAS. The information designer (Isotype, the pilot book, the chart).
A page is a chart: everything has a position and a scale; one colour means "signal";
the type is quiet (Inter) and the apparatus is set in mono; paragraphs are numbered
so they can be cited; photographs are evidence plates — square, numbered, in a strip,
never atmosphere; the hero is the FIGURE, and where the chapter has none the AD draws
one from the ledger."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

CSS = PAGE + MARKS + '''
@font-face{font-family:'Grotesk';src:url('%(F)sSpaceGrotesk.ttf');font-weight:300 700;}
@font-face{font-family:'Inter';src:url('%(F)sInter-Light.ttf');font-weight:300;}
@font-face{font-family:'Inter';src:url('%(F)sInter-Regular.ttf');font-weight:400;}
@font-face{font-family:'Inter';src:url('%(F)sInter-SemiBold.ttf');font-weight:600;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Medium.ttf');font-weight:500;}
@font-face{font-family:'Plex';src:url('%(H)sIBMPlexMono-Regular.ttf');}
@font-face{font-family:'Public';src:url('%(F)sInter-SemiBold.ttf');}
:root{ --paper:#F5F6F3; --ink:#1B2622; --grey:#6B7773; --line:#C9D1CD; --panel:#E8EDEA; --signal:#A23520; --gold:#E0A828; }
@page{ @top-left{ content:"BARCELONA, WITHOUT THE TRAPS."; font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); text-transform:uppercase; }
       @bottom-left{ content:"BARCELONA FOR AMERICANS"; font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); }
       @bottom-right{ content:"P. " counter(page); font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Inter'; font-size:10.5px; line-height:15px; color:var(--ink); }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.hd{ display:grid; grid-template-columns:88.7px 1fr 201.3px; column-gap:24px; align-items:end; border-bottom:1px solid var(--ink); padding-bottom:10px; }
.hd .num{ font-family:'Grotesk'; font-weight:700; font-size:72px; line-height:.8; color:var(--signal); letter-spacing:-.03em; }
.hd h1{ font-family:'Grotesk'; font-weight:500; font-size:27px; line-height:30px; letter-spacing:-.01em; margin:0; }
.hd .sub{ font-family:'Mono'; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); margin-top:4px; }
.hd .key{ font-family:'Mono'; font-size:8px; line-height:12px; letter-spacing:.06em; color:var(--grey); text-transform:uppercase; }
.hd .key b{ color:var(--signal); font-weight:500; }
.abs{ font-weight:300; font-size:14.5px; line-height:20px; width:540px; margin:16px 0 14px; }
.abs b{ font-weight:600; }
figure{ margin:0; }
figure.inst{ margin:4px 0 16px; } figure.inst svg{ display:block; width:100%; height:auto; }
figure.inst figcaption, figure.mapf figcaption{ font-family:'Mono'; font-size:8.5px; line-height:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:6px; }
figure.mapf svg{ display:block; width:100%; height:auto; }
.cols{ display:grid; grid-template-columns:1fr 1fr; column-gap:24px; border-top:1px solid var(--line); padding-top:12px; }
.cols .c{ padding-left:28px; }
p.n{ position:relative; margin:0 0 8px; text-align:left; hyphens:auto; }
p.n .pn{ position:absolute; left:-28px; top:1px; font-family:'Mono'; font-size:8.5px; color:var(--signal); letter-spacing:.04em; }
.call{ border-left:4px solid var(--signal); padding:2px 0 2px 14px; margin:14px 0 0; }
.call .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--signal); display:block; margin-bottom:5px; }
.call .big{ font-family:'Grotesk'; font-weight:500; font-size:17px; line-height:21px; letter-spacing:-.01em; margin:0 0 6px; }
.call p{ margin:0; }
.tbl{ border-top:1px solid var(--ink); margin-top:10px; }
.tbl .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--grey); display:block; padding:6px 0 4px; }
.tbl .r{ display:grid; grid-template-columns:150px 1fr; column-gap:16px; padding:5px 0; border-top:1px solid var(--line); }
.tbl .r .k{ font-family:'Grotesk'; font-weight:500; font-size:11.5px; line-height:14px; } .tbl .r p{ margin:0; }
.notice{ margin-top:10px; border:1px solid var(--ink); padding:8px 12px 8px 12px; display:grid; grid-template-columns:120px 1fr; column-gap:14px; position:relative; }
.notice::before{ content:''; position:absolute; left:0; top:0; bottom:0; width:6px; background:repeating-linear-gradient(135deg,var(--signal) 0 3px,transparent 3px 7px); }
.notice .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--signal); padding-left:8px; }
.notice p{ margin:0; } .notice .x{ color:var(--grey); }
.plates{ display:grid; grid-template-columns:repeat(3,1fr); column-gap:24px; margin-top:14px; border-top:1px solid var(--line); padding-top:12px; }
.plates.sm img{ aspect-ratio:2/1; }
.plates img{ display:block; width:100%; aspect-ratio:1/1; object-fit:cover; }
.plates figcaption{ font-family:'Mono'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:6px; }
.plates figcaption b{ color:var(--ink); font-weight:500; }
.legend{ border-top:1px solid var(--ink); }
.legend .r{ display:grid; grid-template-columns:18px 1fr; column-gap:8px; padding:6px 0; border-bottom:1px solid var(--line); }
.legend .dot{ width:11px; height:11px; border-radius:50%; border:1.5px solid var(--ink); margin-top:2px; }
.legend .dot.gold{ background:var(--gold); } .legend .dot.sea{ background:#0E6390; border-color:#0E6390; }
.legend .k{ font-family:'Grotesk'; font-weight:500; font-size:11.5px; line-height:14px; }
.legend .s{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:1px; }
.legend .v{ font-family:'Mono'; font-size:8.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--signal); margin-top:2px; }
'''.replace('%(F)s', FONTS).replace('%(H)s', HOUSE)

def hd(d, num, key):
    kicker = d['kicker'].split('·')[-1].strip()
    return f'''<span class="rh-src">Sheet {num} · {esc(kicker)}</span><div class="hd"><div class="num">{num}</div>
  <div><h1>{esc(d['title'])}</h1><div class="sub">Decision {num} · {esc(kicker)} · first trip</div></div><div class="key">{key}</div></div>'''

def paras(d, idx):
    return ''.join('<p class="n"><span class="pn">§%d</span>%s</p>' % (i + 1, d['paras'][i]) for i in idx)

def call(d):
    return f'<div class="call"><span class="lab">The call</span><div class="big">{esc(d["verdict_strong"])}</div><p>{d["verdict_rest"]}</p></div>'

def forks(d):
    return '<div class="tbl"><span class="lab">If the reader is not the default</span>' + ''.join(
        f'<div class="r"><div class="k">{esc(f["strong"])}</div><p>{f["text"]}</p></div>' for f in d['forks']) + '</div>'

def notice(d, sid):
    lab = '<i class="mk">◆</i> Notice · 2026' if d['volatile'] else 'Notice'
    return f'<div class="notice"><span class="lab">{lab}</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'

def plates(items, num):
    return '<div class="plates">' + ''.join(
        f'<figure><img src="{photo(s)}" style="object-position:{pos}"><figcaption><b>PL. {num}.{i+1}</b> &nbsp;{esc(c)}</figcaption></figure>'
        for i, (s, c, pos) in enumerate(items)) + '</div>'

# ── d06: the instrument the AD draws from the ledger ──────────────────────────
def dose_figure(d):
    rows = d['ledger']
    attrs = [(1, 1, 1), (1, 1, 0), (1, 1, 1), (0, 0, 0)]    # ticket · timed · interior, from the ledger's own text
    W, top, pitch = 652, 48, 42
    cols = [(262, 'TICKET'), (330, 'TIMED'), (398, 'INTERIOR'), (482, 'THE CALL')]
    s = [f'<svg viewBox="0 0 {W} {top + pitch*4 - 4}" xmlns="http://www.w3.org/2000/svg" font-family="Inter">']
    s.append(f'<text x="0" y="12" font-family="Mono" font-size="8.5" letter-spacing="1.2" fill="#6B7773">FIG. 05-A · {esc(d["ledger_caption"]).upper()}</text>')
    s.append(f'<line x1="0" y1="{top-14}" x2="{W}" y2="{top-14}" stroke="#1B2622" stroke-width="1"/>')
    for x, lab in cols:
        s.append(f'<text x="{x + (7 if lab != "THE CALL" else 0)}" y="{top-20}" font-family="Mono" font-size="8" letter-spacing="1" fill="#6B7773" text-anchor="{"middle" if lab != "THE CALL" else "start"}">{lab}</text>')
    for i, r in enumerate(rows):
        y = top + i * pitch
        chosen = i < 3
        s.append(f'<text x="0" y="{y+12}" font-size="11.5" font-weight="600" fill="#1B2622">{esc(r["opt"].replace("<em>","").replace("</em>",""))}</text>')
        sub = esc(r['sub']); sub = sub if len(sub) < 60 else sub[:57] + '…'
        s.append(f'<text x="0" y="{y+25}" font-size="8.5" fill="#6B7773">{sub}</text>')
        for (x, _), on in zip(cols[:3], attrs[i]):
            fill = ('#A23520' if chosen else '#6B7773') if on else 'none'
            s.append(f'<rect x="{x}" y="{y+4}" width="14" height="14" fill="{fill}" stroke="{"#A23520" if chosen else "#6B7773"}" stroke-width="1"/>')
        s.append(f'<text x="482" y="{y+14}" font-family="Mono" font-size="9" fill="{"#A23520" if chosen else "#6B7773"}">{esc(r["call"])}</text>')
        s.append(f'<line x1="0" y1="{y+pitch-6}" x2="{W}" y2="{y+pitch-6}" stroke="#C9D1CD" stroke-width=".6"/>')
    # the dose bracket: rows 1–3 are the first-trip dose
    y0, y1 = top + 2, top + 3 * pitch - 8
    s.append(f'<line x1="246" y1="{y0}" x2="246" y2="{y1}" stroke="#A23520" stroke-width="2"/>')
    s.append('</svg>')
    return '<figure class="inst">%s<figcaption><i class="mk">■</i> applies &nbsp; <i class="mk">□</i> does not &nbsp;· signal red = earns a ticket on a first trip &nbsp;· the bracket is the dose: 2 + 1, the fourth interior is wallpaper</figcaption></figure>' % ''.join(s)

d06 = CH['d06']
key06 = 'Reading: §-numbered prose<br><i class="mk">■</i> attribute applies<br><b>signal red</b> = the call<br>PL. = evidence plate'
p1 = f'''<div class="pg">{hd(d06, '05', key06)}
  <div class="abs">{d06['standfirst']}</div>
  {dose_figure(d06)}
  <div class="cols"><div class="c">{paras(d06, [0, 1])}</div><div class="c">{paras(d06, [2, 3])}</div></div>
</div>'''
p2 = f'''<div class="pg">
  <div class="cols" style="border-top:0;padding-top:0"><div class="c">{paras(d06, [4])}{forks(d06)}</div><div>{call(d06)}</div></div>
  {notice(d06, 'd06')}
  {plates([('A04.jpg', 'Sagrada Família — the nave. The interior is the argument, and the argument is light.', '50% 50%'),
           ('p-d06.jpg', 'Park Güell — the monumental zone, timed and slotted.', '50% 60%'),
           ('p-setpieces.jpg', 'The rest: façades, enjoyable from the street without the ticket queue.', '50% 50%')], '05')}
</div>'''

d01 = CH['d01']
key01 = 'Reading: §-numbered prose<br><i class="mk">●</i> default base<br><i class="mk">◆</i> anchor sight<br>PL. = evidence plate'
svg01 = map_svg({'#F2F7F5': '#E8EDEA', '#0E6390': '#0E6390', '#0B4E70': '#1B2622', '#A23520': '#A23520', '#5B6B66': '#6B7773'}, scale=1.45,
                fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'Inter, sans-serif'})
def legend(d):
    kinds = ['gold', 'sea', 'sea', 'sea']
    return '<div class="legend">' + ''.join(
        f'<div class="r"><div class="dot {kinds[i]}"></div><div><div class="k">{r["opt"]}</div><div class="s">{esc(r["sub"])}</div><div class="v">{esc(r["call"])}</div></div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
p3 = f'''<div class="pg">{hd(d01, '01', key01)}
  <div class="abs">{d01['standfirst']}</div>
  <figure class="mapf">{svg01}<figcaption>FIG. 01-A · {esc(d01['figure_cap'].split('·',1)[-1].strip())}</figcaption></figure>
</div>'''
p4 = f'''<div class="pg">
  <div class="cols" style="border-top:0;padding-top:0;grid-template-columns:314px 314px"><div class="c">{paras(d01, [0, 1, 2])}</div><div><span class="lab" style="font-family:'Mono';font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);display:block;margin-bottom:4px">Key to fig. 01-A · {esc(d01['ledger_caption'])}</span>{legend(d01)}</div></div>
  {plates([('A01.jpg', 'The Eixample grid from above: the largest cluster of sights on foot.', '50% 50%'),
           ('h-contract.jpg', 'The medieval density south-east of the grid: El Born and the Gothic Quarter.', '50% 50%'),
           ('p-plan.jpg', 'The beach bases: superb if you will use the sea, a commute if you will not.', '50% 50%')], '01').replace('class="plates"','class="plates sm"')}
  <div class="cols" style="border-top:0;padding-top:0;margin-top:8px;grid-template-columns:314px 314px"><div>{forks(d01)}</div><div>{call(d01)}</div></div>
  {notice(d01, 'd01')}
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 4 — L\'Atlas</title><style>{CSS}</style></head><body>{p1}{p2}{p3}{p4}</body></html>'
write(html)
