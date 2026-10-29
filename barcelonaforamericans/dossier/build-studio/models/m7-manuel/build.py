# -*- coding: utf-8 -*-
"""MODEL 7 — LE MANUEL · Oriol Pich, the technical-manual designer.
The chapter is a procedure. Every option has a colour and keeps it everywhere — on
the tab bar, in the decision tree, on the map, in the parts list. The hero is the
DECISION TREE drawn from the verdict and the forks; the ledger is a parts list; the
forks are TROUBLESHOOTING; the volatile note is a CAUTION. Photographs carry numbered
callouts that point at what the ledger names."""
import sys, os, re; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

OPT = ['#0E6390', '#E0A828', '#A23520', '#5B6B66']     # option colours, in ledger order
CSS = PAGE + MARKS + '''
@font-face{font-family:'PlexSans';src:url('%(F)sIBMPlexSans.ttf');font-weight:100 700;font-stretch:85% 100%;}
@font-face{font-family:'PlexSans';src:url('%(F)sIBMPlexSans-Italic.ttf');font-weight:100 700;font-stretch:85% 100%;font-style:italic;}
@font-face{font-family:'Barlow';src:url('%(F)sBarlowCondensed-SemiBold.ttf');font-weight:600;}
@font-face{font-family:'Barlow';src:url('%(F)sBarlowCondensed-Medium.ttf');font-weight:500;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Medium.ttf');font-weight:500;}
@font-face{font-family:'Plex';src:url('%(H)sIBMPlexMono-Regular.ttf');}
@font-face{font-family:'Public';src:url('%(F)sIBMPlexSans.ttf');font-weight:100 700;}
:root{ --paper:#F7F7F4; --ink:#1B2622; --grey:#5B6B66; --line:#C9D1CD; --o1:#0E6390; --o2:#E0A828; --o3:#A23520; --o4:#5B6B66; }
@page{ @top-left{ content:"BARCELONA, WITHOUT THE TRAPS."; font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); text-transform:uppercase; }
       @bottom-left{ content:"BARCELONA FOR AMERICANS"; font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Barlow'; font-weight:600; font-size:12px; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'PlexSans'; font-size:10.5px; line-height:15px; color:var(--ink); }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.tabs{ display:grid; grid-template-columns:repeat(4,1fr); column-gap:6px; margin-bottom:14px; }
.tabs .t{ height:26px; display:flex; align-items:center; padding:0 9px; color:#fff; font-family:'Mono'; font-size:8px; letter-spacing:.1em; text-transform:uppercase; }
.tabs .t.o2{ color:var(--ink); }
.hd{ display:grid; grid-template-columns:1fr 201.3px; column-gap:24px; align-items:end; margin-bottom:12px; }
h1{ font-family:'Barlow'; font-weight:600; font-size:52px; line-height:.92; letter-spacing:.005em; text-transform:uppercase; margin:0 0 8px; }
.sf{ font-size:13px; line-height:18px; font-weight:400; margin:0; width:520px; }
.meta{ font-family:'Mono'; font-size:8px; line-height:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--grey); border-left:2px solid var(--ink); padding-left:10px; }
.meta b{ color:var(--ink); font-weight:500; }
figure{ margin:0; }
figure.tree{ margin:0 0 12px; border-top:1px solid var(--ink); padding-top:8px; } figure.tree svg{ display:block; width:100%; height:auto; }
figure.tree figcaption, figure.mapf figcaption{ font-family:'Mono'; font-size:8px; letter-spacing:.08em; text-transform:uppercase; color:var(--grey); margin-top:4px; }
.res{ display:grid; grid-template-columns:118px 1fr; column-gap:16px; border:1.5px solid var(--ink); padding:10px 14px; margin:0 0 14px; align-items:start; }
.res .lab{ font-family:'Barlow'; font-weight:600; font-size:20px; line-height:20px; text-transform:uppercase; }
.res .big{ font-weight:600; font-size:12.5px; line-height:16px; margin:0 0 4px; }
.res p{ margin:0; }
.cols{ display:grid; grid-template-columns:314px 314px; column-gap:24px; align-items:start; }
.cols p{ margin:0 0 8px; text-align:left; hyphens:auto; }
.parts{ border-top:1.5px solid var(--ink); }
.parts .lab, .ts .lab, .cal .lab{ font-family:'Barlow'; font-weight:600; font-size:15px; line-height:18px; text-transform:uppercase; display:block; padding:6px 0 4px; }
.parts .r{ display:grid; grid-template-columns:22px 1fr 150px; column-gap:10px; padding:6px 0; border-top:1px solid var(--line); align-items:start; }
.parts .sw{ width:16px; height:16px; margin-top:1px; }
.parts .opt{ font-weight:600; font-size:11px; line-height:14px; } .parts .sub{ font-size:9.5px; line-height:13px; color:var(--grey); }
.parts.narrow .r{ grid-template-columns:14px 1fr; column-gap:8px; } .parts.narrow .sw{ width:12px; height:12px; } .parts.narrow .v{ grid-column:2; padding-top:3px; }
.parts .v{ font-family:'Mono'; font-size:8.5px; line-height:12px; letter-spacing:.04em; text-transform:uppercase; padding-top:2px; }
.shots{ display:grid; grid-template-columns:314px 314px; column-gap:24px; margin:14px 0 0; }
.shot{ position:relative; } .shot img{ display:block; width:100%; height:176px; object-fit:cover; }
.shot .co{ position:absolute; width:20px; height:20px; border-radius:50%; background:#fff; color:var(--ink); font-family:'Barlow'; font-weight:600; font-size:13px; display:flex; align-items:center; justify-content:center; border:1.5px solid var(--ink); }
.shot .co::after{ content:''; position:absolute; left:50%; top:100%; width:1.5px; height:var(--l,22px); background:#fff; transform:translateX(-50%); }
.shot figcaption{ font-size:9.5px; line-height:13px; margin-top:6px; } .shot figcaption b{ font-family:'Barlow'; font-weight:600; font-size:12px; }
.ts{ border-top:1.5px solid var(--ink); margin-top:14px; }
.ts .r{ display:grid; grid-template-columns:170px 1fr; column-gap:14px; padding:6px 0; border-top:1px solid var(--line); }
.ts .k{ font-weight:600; font-size:10.5px; } .ts p{ margin:0; }
.cal{ margin-top:14px; border:1.5px solid var(--o3); display:grid; grid-template-columns:118px 1fr; column-gap:14px; padding:8px 12px; }
.cal .lab{ color:var(--o3); padding:0; } .cal p{ margin:0; font-size:10px; line-height:14px; } .cal .x{ color:var(--grey); }
figure.mapf svg{ display:block; width:100%; height:auto; }
'''.replace('%(F)s', FONTS).replace('%(H)s', HOUSE)

def tabs(d):
    return '<div class="tabs">' + ''.join(f'<div class="t o{i+1}" style="background:{OPT[i]}">{i+1} · {esc(re.sub("<[^>]+>", "", r["opt"]).split(" — ")[0].split(":")[0].split(" (")[0])}</div>' for i, r in enumerate(d['ledger'])) + '</div>'

def hd(d, meta):
    return f'<span class="rh-src">{esc(d["kicker"])}</span>{tabs(d)}<div class="hd"><div><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div></div><div class="meta">{meta}</div></div>'

def res(d):
    return f'<div class="res"><div class="lab">Result</div><div><div class="big">{esc(d["verdict_strong"])}</div><p>{d["verdict_rest"]}</p></div></div>'

def parts(d):
    return '<div class="parts"><span class="lab">Parts list · %s</span>' % esc(d['ledger_caption']) + ''.join(
        f'<div class="r"><div class="sw" style="background:{OPT[i]}"></div><div><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div></div><div class="v" style="color:{OPT[i] if i != 1 else "#8a6410"}">{esc(r["call"])}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'

def ts(d):
    return '<div class="ts"><span class="lab">Troubleshooting</span>' + ''.join(f'<div class="r"><div class="k">{esc(f["strong"])}</div><p>{f["text"]}</p></div>' for f in d['forks']) + '</div>'

def cal(d):
    lab = '<i class="mk">◆</i> Caution 2026' if d['volatile'] else 'Changed'
    return f'<div class="cal"><span class="lab">{lab}</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'

def shot(src, items, cap, pos='50% 50%'):
    cos = ''.join(f'<div class="co" style="left:{x}%;top:{y}%;--l:{l}px">{n}</div>' for n, x, y, l in items)
    return f'<figure class="shot"><div style="position:relative"><img src="{photo(src)}" style="object-position:{pos}">{cos}</div><figcaption>{cap}</figcaption></figure>'

# ── the decision tree (SVG) — nodes from the ledger and the forks, nothing invented ──
def tree(nodes, edges, W=652, H=300, cap=''):
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="PlexSans">']
    s.append('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1B2622"/></marker></defs>')
    for (a, b, lab) in edges:
        ax, ay, aw, ah = nodes[a][:4]; bx, by, bw, bh = nodes[b][:4]
        x1, y1 = ax + aw / 2, ay + ah; x2, y2 = bx + bw / 2, by
        if abs(x1 - x2) < 2: s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>')
        else:
            my = (y1 + y2) / 2
            s.append(f'<path d="M{x1},{y1} L{x1},{my} L{x2},{my} L{x2},{y2}" fill="none" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>')
        if lab:
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 3
            s.append(f'<rect x="{lx-len(lab)*2.6-4}" y="{ly-8}" width="{len(lab)*5.2+8}" height="12" fill="#F7F7F4"/>')
            s.append(f'<text x="{lx}" y="{ly+1}" font-family="Mono" font-size="7.5" fill="#1B2622" text-anchor="middle" letter-spacing=".5">{lab}</text>')
    for k, (x, y, w, h, title, sub, col, kind) in nodes.items():
        if kind == 'q':
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#F7F7F4" stroke="#1B2622" stroke-width="1.2"/>')
            s.append(f'<text x="{x+w/2}" y="{y+h/2+4}" font-size="9.5" font-weight="600" fill="#1B2622" text-anchor="middle">{title}</text>')
        elif kind == 'start':
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#1B2622"/>')
            s.append(f'<text x="{x+w/2}" y="{y+h/2+3.5}" font-family="Mono" font-size="8" fill="#fff" text-anchor="middle" letter-spacing="1">{title}</text>')
        else:
            tc = '#1B2622' if col == OPT[1] else '#fff'
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/>')
            s.append(f'<text x="{x+10}" y="{y+16}" font-size="10.5" font-weight="600" fill="{tc}">{title}</text>')
            if sub: s.append(f'<text x="{x+10}" y="{y+29}" font-family="Mono" font-size="7.5" fill="{tc}" letter-spacing=".5">{sub}</text>')
    s.append('</svg>')
    return f'<figure class="tree">{"".join(s)}<figcaption>{cap}</figcaption></figure>'

d = CH['d06']; P = d['paras']
N = {  # x, y, w, h, title, sub, colour, kind
 'start': (246, 0, 160, 22, 'FIRST TRIP · GAUDÍ', '', '', 'start'),
 'n1': (206, 46, 240, 38, '1 · Sagrada Família — the interior', 'NON-NEGOTIABLE · MORNING SLOT', OPT[0], 'o'),
 'n2': (206, 108, 240, 38, '2 · Park Güell — the monumental zone', 'BOOKED · EARLY', OPT[1], 'o'),
 'q2': (486, 108, 166, 38, 'Crowds ruin things for you?', '', '', 'q'),
 'a2': (486, 170, 166, 38, 'The free park + a viewpoint', 'CENTENARY-YEAR FALLBACK', OPT[3], 'o'),
 'n3': (206, 170, 240, 38, '3 · One house: Batlló or La Pedrera', 'PICK ONE · TWO IS SATURATION', OPT[2], 'o'),
 'q3': (0, 170, 170, 38, 'Modernisme is why you came?', '', '', 'q'),
 'a3': (0, 232, 170, 38, 'Both houses', 'AN ENTHUSIAST’S CALL', OPT[3], 'o'),
 'n4': (206, 232, 240, 38, 'The rest — from the street', 'VICENS · PALAU GÜELL · FAÇADES · FREE', OPT[3], 'o'),
}
E = [('start', 'n1', ''), ('n1', 'n2', ''), ('n2', 'n3', 'NO'), ('n2', 'q2', ''), ('q2', 'a2', 'YES'), ('n3', 'n4', 'STOP'), ('n3', 'q3', ''), ('q3', 'a3', 'YES')]
# fix: q2 sits beside n2; route edges from the side instead of bottom for the two side questions
def tree06():
    s = tree(N, [e for e in E if e[0] not in ('n2', 'n3') or e[1] in ('n3', 'n4')], H=276, cap='FIG. 05 · The Gaudí procedure — the verdict and its two forks as a tree. Colours follow the parts list.')
    # side edges drawn as straight horizontal arrows
    side = ('<line x1="446" y1="127" x2="484" y2="127" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<line x1="206" y1="189" x2="172" y2="189" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<line x1="569" y1="146" x2="569" y2="168" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<text x="560" y="161" font-family="Mono" font-size="7.5" text-anchor="end" letter-spacing=".5">YES</text>'
            '<line x1="85" y1="208" x2="85" y2="230" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<text x="76" y="223" font-family="Mono" font-size="7.5" text-anchor="end" letter-spacing=".5">YES</text>')
    return s.replace('</svg>', side + '</svg>')
E06 = [('start', 'n1', ''), ('n1', 'n2', ''), ('n2', 'n3', ''), ('n3', 'n4', 'STOP')]
def tree06b():
    s = tree(N, E06, H=276, cap='FIG. 05 · The Gaudí procedure — the verdict and its two forks as a tree. Colours follow the parts list.')
    side = ('<line x1="446" y1="127" x2="484" y2="127" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<line x1="206" y1="189" x2="172" y2="189" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<line x1="569" y1="146" x2="569" y2="168" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<text x="562" y="161" font-family="Mono" font-size="7.5" text-anchor="end" letter-spacing=".5">YES</text>'
            '<line x1="85" y1="208" x2="85" y2="230" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
            '<text x="78" y="223" font-family="Mono" font-size="7.5" text-anchor="end" letter-spacing=".5">YES</text>')
    return s.replace('</svg>', side + '</svg>')

meta06 = 'Procedure <b>05 · Tickets</b><br>Reader: first trip, 3–5 days<br>Colour = option (parts list)<br>Callouts ① ② = what the ledger names'
d06 = f'''<div class="pg">{hd(d, meta06)}
  {tree06b()}
  {res(d)}
  <div class="cols"><div><p>{P[0]}</p><p>{P[1]}</p></div><div><p>{P[2]}</p></div></div>
</div>
<div class="pg">
  {parts(d)}
  <div class="cols" style="margin-top:14px"><div><p>{P[3]}</p></div><div><p>{P[4]}</p></div></div>
  <div class="shots">
    {shot('A04.jpg', [(1, 44, 30, 24)], '<b>1</b> &nbsp;Sagrada Família — the nave: the one building unlike any you have seen. Timed; book the morning slot.', '50% 40%')}
    {shot('p-d06.jpg', [(2, 26, 58, 22), (3, 70, 22, 22)], '<b>2</b> &nbsp;Park Güell — the mosaic terrace. &nbsp;<b>3</b> &nbsp;The city view the ticket buys. Timed and slotted; ride up.', '50% 55%')}
  </div>
  {ts(d)}
  {cal(d)}
</div>'''

d = CH['d01']; P = d['paras']
N1 = {
 'start': (246, 0, 160, 22, 'FIRST TRIP · WHERE TO SLEEP', '', '', 'start'),
 'q1': (226, 44, 200, 34, 'Atmosphere is the point, and you sleep through noise?', '', '', 'q'),
 'a1': (470, 44, 182, 34, '2 · El Born', 'THE MEDIEVAL CITY · BAR NOISE', OPT[1], 'o'),
 'q2': (226, 102, 200, 34, 'Will you actually be at the beach?', '', '', 'q'),
 'a2': (470, 102, 182, 34, '3 · Barceloneta / Poblenou', 'SAND AT THE DOOR · A COMMUTE TO THE REST', OPT[2], 'o'),
 'q3': (226, 160, 200, 34, 'Real prices, one metro hop is fine?', '', '', 'q'),
 'a3': (470, 160, 182, 34, '4 · Poble-sec', 'BUDGET · BELOW MONTJUÏC', OPT[3], 'o'),
 'a0': (226, 218, 200, 38, '1 · Eixample — the default', 'CENTRAL · QUIET · GAUDÍ ON FOOT', OPT[0], 'o'),
}
def tree01():
    s = tree(N1, [('start', 'q1', ''), ('q1', 'q2', 'NO'), ('q2', 'q3', 'NO'), ('q3', 'a0', 'NO')], H=262,
             cap='FIG. 01 · The base procedure — three questions from the verdict; say no to all three and the default holds.')
    side = ''.join(f'<line x1="426" y1="{y}" x2="468" y2="{y}" stroke="#1B2622" stroke-width="1.2" marker-end="url(#a)"/>'
                   f'<rect x="436" y="{y-12}" width="22" height="11" fill="#F7F7F4"/><text x="447" y="{y-3}" font-family="Mono" font-size="7.5" text-anchor="middle" letter-spacing=".5">YES</text>'
                   for y in (61, 119, 177))
    return s.replace('</svg>', side + '</svg>')
N1['q1'] = N1['q1'][:4] + ('Atmosphere the point · sleep through noise?',) + N1['q1'][5:]
svg01 = map_svg({'#F2F7F5': '#EDF0EE', '#0B4E70': '#1B2622', '#5B6B66': '#5B6B66'}, scale=1.5,
                fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'PlexSans, sans-serif'})
# colour each neighbourhood dot by its option (ledger order): Eixample 1, El Born 2, beach 3, Poble-sec 4, the rest grey
def recolour(svg):
    cols = {'Eixample': OPT[0], 'El Born': OPT[1], 'Barceloneta': OPT[2], 'Poblenou': OPT[2], 'Poble-sec': OPT[3]}
    def rep(m):
        circ, name = m.group(1), m.group(3)
        circ = re.sub(r'fill="#[0-9A-Fa-f]+"', 'fill="%s"' % cols.get(name, '#B9C2BD'), circ)
        return circ + m.group(2) + name + m.group(4)
    return re.sub(r'(<circle[^>]*/>)(\s*<text[^>]*>)([^<]+)(</text>)', rep, svg)
svg01 = recolour(svg01).replace('fill="#A23520"', 'fill="#5B6B66"')
meta01 = 'Procedure <b>01 · Base</b><br>Reader: first-timer, 3–5 days<br>Colour = option (parts list)<br>Map dots take the option colour'
d01 = f'''<div class="pg">{hd(d, meta01)}
  {tree01()}
  {res(d)}
  <div class="cols"><div><p>{P[0]}</p><p>{P[2]}</p></div><div><p>{P[1]}</p></div></div>
</div>
<div class="pg">
  <div class="cols" style="grid-template-columns:426.7px 201.3px"><figure class="mapf">{svg01}<figcaption>Fig. 01-A · {esc(d['figure_cap'].split('·',1)[-1].strip())}</figcaption></figure>{parts(d).replace('class="parts"', 'class="parts narrow"')}</div>
  {ts(d)}
  {cal(d)}
  <div class="shots" style="margin-top:14px">{shot('A03.jpg', [(1, 50, 50, 22)], '<b>1</b> &nbsp;The grid from above: the geometry that makes the Eixample the default is invisible from the street.', '50% 50%')}{shot('h-contract.jpg', [(2, 50, 40, 22)], '<b>2</b> &nbsp;The medieval lanes south-east of the grid: El Born’s trade, atmosphere for quiet.', '50% 50%')}</div>
</div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Model 7 — Le Manuel</title><style>{CSS}</style></head><body>{d06}{d01}</body></html>'
write(html)
