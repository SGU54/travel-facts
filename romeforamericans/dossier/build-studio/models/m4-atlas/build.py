# -*- coding: utf-8 -*-
"""ROME · Ingrid Vos — L'ATLAS, in La Tavola's palette. Decision 01 (map) + Decision 05 (the two lines, drawn)."""
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
:root{ --paper:#EFE4CC; --ink:#2B241A; --grey:#6A5C42; --line:#D8C7A4; --panel:#E4D6B8; --signal:#8A3324; --gold:#C9A94A; }
@page{ @top-left{ content:"ROME, SOLVED."; font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); text-transform:uppercase; }
       @bottom-left{ content:"ROME FOR AMERICANS"; font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--grey); }
       @bottom-right{ content:"P. " counter(page); font-family:'Mono'; font-size:8px; letter-spacing:.16em; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'Inter'; font-size:10.5px; line-height:15px; color:var(--ink); }
i.mk{ color:var(--signal); font-weight:400; }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.hd{ display:grid; grid-template-columns:88.7px 1fr 201.3px; column-gap:24px; align-items:end; border-bottom:1px solid var(--ink); padding-bottom:10px; }
.hd .num{ font-family:'Grotesk'; font-weight:700; font-size:72px; line-height:.8; color:var(--signal); letter-spacing:-.03em; }
.hd h1{ font-family:'Grotesk'; font-weight:500; font-size:24px; line-height:27px; letter-spacing:-.01em; margin:0; }
.hd .sub{ font-family:'Mono'; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--grey); margin-top:4px; }
.hd .key{ font-family:'Mono'; font-size:8px; line-height:12px; letter-spacing:.06em; color:var(--grey); text-transform:uppercase; }
.hd .key b{ color:var(--signal); font-weight:500; }
.abs{ font-weight:300; font-size:14.5px; line-height:20px; width:540px; margin:16px 0 14px; }
figure{ margin:0; }
figure.inst{ margin:4px 0 16px; } figure.inst svg, figure.mapf svg{ display:block; width:100%%; height:auto; }
figure.inst figcaption, figure.mapf figcaption{ font-family:'Mono'; font-size:8.5px; line-height:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--grey); margin-top:6px; }
.cols{ display:grid; grid-template-columns:1fr 1fr; column-gap:24px; border-top:1px solid var(--line); padding-top:12px; }
.cols .c{ padding-left:28px; }
p.n{ position:relative; margin:0 0 8px; text-align:left; hyphens:auto; }
p.n .pn{ position:absolute; left:-28px; top:1px; font-family:'Mono'; font-size:8.5px; color:var(--signal); letter-spacing:.04em; }
.call{ border-left:4px solid var(--signal); padding:2px 0 2px 14px; margin:0; }
.call .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--signal); display:block; margin-bottom:5px; }
.call .big{ font-family:'Grotesk'; font-weight:500; font-size:16px; line-height:20px; letter-spacing:-.01em; margin:0 0 6px; }
.call p{ margin:0; }
.tbl{ border-top:1px solid var(--ink); margin-top:10px; }
.tbl .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--grey); display:block; padding:6px 0 4px; }
.tbl .r{ display:grid; grid-template-columns:150px 1fr; column-gap:16px; padding:5px 0; border-top:1px solid var(--line); }
.tbl .r .k{ font-family:'Grotesk'; font-weight:500; font-size:10.5px; line-height:13px; } .tbl .r p{ margin:0; }
.tbl .r .k b{ display:block; font-family:'Mono'; font-size:7.5px; letter-spacing:.1em; color:var(--signal); font-weight:500; text-transform:uppercase; margin-bottom:2px; }
.notice{ margin-top:10px; border:1px solid var(--ink); padding:8px 12px; display:grid; grid-template-columns:120px 1fr; column-gap:14px; position:relative; }
.notice::before{ content:''; position:absolute; left:0; top:0; bottom:0; width:6px; background:repeating-linear-gradient(135deg,var(--signal) 0 3px,transparent 3px 7px); }
.notice .lab{ font-family:'Mono'; font-size:8.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--signal); padding-left:8px; }
.notice p{ margin:0; } .notice .x{ color:var(--grey); }
.plates{ display:grid; grid-template-columns:repeat(3,1fr); column-gap:24px; margin-top:14px; border-top:1px solid var(--line); padding-top:12px; }
.plates img{ display:block; width:100%%; aspect-ratio:1/1; object-fit:cover; } .plates.sm img{ aspect-ratio:2/1; }
.plates figcaption{ font-family:'Mono'; font-size:8.5px; line-height:12px; color:var(--grey); margin-top:6px; }
.plates figcaption b{ color:var(--ink); font-weight:500; }
.legend{ border-top:1px solid var(--ink); }
.legend .r{ display:grid; grid-template-columns:18px 1fr; column-gap:8px; padding:6px 0; border-bottom:1px solid var(--line); }
.legend .dot{ width:11px; height:11px; border-radius:50%%; border:1.5px solid var(--ink); margin-top:2px; }
.legend .dot.pick{ background:var(--signal); border-color:var(--signal); }
.legend .k{ font-family:'Grotesk'; font-weight:500; font-size:11.5px; line-height:14px; }
.legend .s{ font-size:9.5px; line-height:13px; color:var(--grey); margin-top:1px; }
.legend .v{ font-family:'Mono'; font-size:8.5px; letter-spacing:.06em; text-transform:uppercase; color:var(--signal); margin-top:2px; }
''' % {'F': FONTS, 'H': HOUSE}

def hd(d, num, key):
    kicker = d['kicker'].split('·')[-1].strip()
    return f'''<span class="rh-src">Sheet {num} · {esc(kicker)}</span><div class="hd"><div class="num">{num}</div>
  <div><h1>{esc(d['title'])}</h1><div class="sub">Decision {num} · {esc(kicker)} · first trip</div></div><div class="key">{key}</div></div>'''
def paras(d, idx): return ''.join('<p class="n"><span class="pn">§%d</span>%s</p>' % (i + 1, d['paras'][i]) for i in idx)
def call(d): return f'<div class="call"><span class="lab">The call</span><div class="big">{esc(d["verdict_strong"])}</div><p>{d["verdict_rest"]}</p></div>'
def forks(d):
    return '<div class="tbl"><span class="lab">Follow it · overrule it</span>' + ''.join(
        f'<div class="r"><div class="k"><b>{esc(f["lab"])}</b>{esc(f["strong"])}</div><p>{esc(f["text"])}</p></div>' for f in d['forks']) + '</div>'
def notice(d): return f'<div class="notice"><span class="lab"><i class="mk">◆</i> Notice · 2026</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'
def plates(items, num, sm=False):
    return f'<div class="plates{" sm" if sm else ""}">' + ''.join(
        f'<figure><img src="{photo(s)}" style="object-position:{pos}"><figcaption><b>PL. {num}.{i+1}</b> &nbsp;{esc(c)}</figcaption></figure>'
        for i, (s, c, pos) in enumerate(items)) + '</div>'

# ── FIG. 05-A · the two lines, drawn from the ledger ───────────────────────────
def lines_figure(d):
    rows = d['ledger']; W = 652; top = 44; pitch = 40
    # from the ledger's own words: which line each sight has, and what a paid "skip" buys
    has = [(1, 1), (0, 1), (0, 0), (1, 1)]   # (ticket line, security line): Museums · St Peter's · Borghese · third-party
    s = [f'<svg viewBox="0 0 {W} {top + pitch*4 + 4}" xmlns="http://www.w3.org/2000/svg" font-family="Inter">']
    s.append(f'<text x="0" y="12" font-family="Mono" font-size="8.5" letter-spacing="1.2" fill="#6A5C42">FIG. 05-A · {esc(d["ledger_caption"]).upper()}</text>')
    s.append(f'<line x1="0" y1="{top-14}" x2="{W}" y2="{top-14}" stroke="#2B241A" stroke-width="1"/>')
    for x, lab in ((300, 'TICKET LINE'), (390, 'SECURITY LINE')):
        s.append(f'<text x="{x+7}" y="{top-20}" font-family="Mono" font-size="8" letter-spacing="1" fill="#6A5C42" text-anchor="middle">{lab}</text>')
    s.append(f'<text x="470" y="{top-20}" font-family="Mono" font-size="8" letter-spacing="1" fill="#6A5C42">WHAT THE REAL WAIT IS</text>')
    for i, r in enumerate(rows):
        y = top + i * pitch; chosen = i < 3
        s.append(f'<text x="0" y="{y+12}" font-size="11.5" font-weight="600" fill="#2B241A">{esc(r["opt"])}</text>')
        if r['sub']: s.append(f'<text x="0" y="{y+25}" font-size="8.5" fill="#6A5C42">{esc(r["sub"])}</text>')
        for (x, on) in zip((300, 390), has[i]):
            fill = ('#8A3324' if chosen else '#6A5C42') if on else 'none'
            s.append(f'<rect x="{x}" y="{y+4}" width="14" height="14" fill="{fill}" stroke="{"#8A3324" if chosen else "#6A5C42"}" stroke-width="1"/>')
        s.append(f'<text x="470" y="{y+14}" font-family="Mono" font-size="8.5" fill="{"#8A3324" if chosen else "#6A5C42"}">{esc(r["call"])}</text>')
        s.append(f'<line x1="0" y1="{y+pitch-6}" x2="{W}" y2="{y+pitch-6}" stroke="#D8C7A4" stroke-width=".6"/>')
    s.append('</svg>')
    return '<figure class="inst">%s<figcaption>■ the sight has this line &nbsp; □ it does not &nbsp;· a timed ticket skips the ticket line only; everyone clears security</figcaption></figure>' % ''.join(s)

d = CH['d05']
key05 = 'Reading: §-numbered prose<br><i class="mk">■</i> the line exists<br><b>wax red</b> = the call<br>PL. = evidence plate'
p1 = f'''<div class="pg">{hd(d, '05', key05)}<div class="abs">{d['standfirst']}</div>{lines_figure(d)}
  <div class="cols"><div class="c">{paras(d, [0, 1])}</div><div class="c">{paras(d, [2])}</div></div></div>'''
p2 = f'''<div class="pg"><div class="cols" style="border-top:0;padding-top:0"><div class="c">{paras(d, [3, 4])}</div><div>{call(d)}{forks(d)}</div></div>
  {notice(d)}
  {plates([('d05-gallery.jpg', 'The Borghese Gallery: a mandatory slot, no walk-ins — no line for a “skip” product to skip.', '50% 50%'),
           ('stpeters.jpg', 'St Peter’s: free entry; the wait is security, which only timing or the passage-tour out-schedules.', '50% 30%'),
           ('borghese.jpg', 'The Borghese’s mandatory reservation is the “skip the line” already.', '50% 50%')], '05')}</div>'''

d = CH['d01']
key01 = 'Reading: §-numbered prose<br><i class="mk">●</i> the picks<br>■ Termini<br>PL. = evidence plate'
svg01 = map_svg({'#F2F7F5': '#E4D6B8', '#0E6390': '#6A5C42', '#0B4E70': '#2B241A', '#A23520': '#8A3324', '#1B2622': '#2B241A', '#5B6B66': '#6A5C42'}, scale=1.35,
                fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'Inter, sans-serif'})
def legend(d):
    return '<div class="legend">' + ''.join(
        f'<div class="r"><div class="dot{" pick" if i < 2 else ""}"></div><div><div class="k">{r["opt"]}</div><div class="s">{esc(r["sub"])}</div><div class="v">{esc(r["call"])} to the core</div></div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
p3 = f'''<div class="pg">{hd(d, '01', key01)}<div class="abs">{d['standfirst']}</div>
  <figure class="mapf">{svg01}<figcaption>FIG. 01-A · {esc(d['figure_cap'].split('·',1)[-1].strip())}</figcaption></figure>
  <div class="cols"><div class="c">{paras(d, [0])}</div><div class="c">{paras(d, [1])}</div></div></div>'''
p4 = f'''<div class="pg"><div class="cols" style="border-top:0;padding-top:0;grid-template-columns:314px 314px"><div class="c">{paras(d, [2, 3])}{call(d)}</div>
    <div><span class="lab" style="font-family:'Mono';font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey);display:block;margin-bottom:4px">Key to fig. 01-A · {esc(d['ledger_caption'])}</span>{legend(d)}{forks(d)}</div></div>
  {notice(d)}
  {plates([('colosseum.jpg', 'The Colosseum — an outer edge of the core, twenty minutes from the centre on foot.', '50% 50%'),
           ('d01-lane.jpg', 'A lane inside the core: the walk home at midnight is the thing you came for.', '50% 40%'),
           ('forum.jpg', 'The Forum from above: one connected pedestrian district, not a metropolis.', '50% 50%')], '01', sm=True)}</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Rome — L\'Atlas</title><style>{CSS}</style></head><body>{p3}{p4}{p1}{p2}</body></html>'
write(html)
