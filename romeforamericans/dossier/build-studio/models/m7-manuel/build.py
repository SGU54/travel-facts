# -*- coding: utf-8 -*-
"""ROME · Oriol Pich — LE MANUEL, in La Tavola's palette. The decision is a procedure; every option keeps its colour."""
import sys, os, re; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from common import *

OPT = ['#8A3324', '#C9A94A', '#6A5C42', '#8A7A5A', '#B8A98A']   # option colours, ledger order (La Tavola)
TXT = ['#fff', '#2B241A', '#fff', '#fff', '#2B241A']
CSS = PAGE + MARKS + '''
@font-face{font-family:'PlexSans';src:url('%(F)sIBMPlexSans.ttf');font-weight:100 700;font-stretch:85%% 100%%;}
@font-face{font-family:'PlexSans';src:url('%(F)sIBMPlexSans-Italic.ttf');font-weight:100 700;font-stretch:85%% 100%%;font-style:italic;}
@font-face{font-family:'Barlow';src:url('%(F)sBarlowCondensed-SemiBold.ttf');font-weight:600;}
@font-face{font-family:'Barlow';src:url('%(F)sBarlowCondensed-Medium.ttf');font-weight:500;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'Mono';src:url('%(H)sIBMPlexMono-Medium.ttf');font-weight:500;}
@font-face{font-family:'Plex';src:url('%(H)sIBMPlexMono-Regular.ttf');}
@font-face{font-family:'Public';src:url('%(F)sIBMPlexSans.ttf');font-weight:100 700;}
:root{ --paper:#EFE4CC; --ink:#2B241A; --grey:#6A5C42; --line:#D8C7A4; --o1:#8A3324; --o3:#8A3324; }
@page{ @top-left{ content:"ROME, SOLVED."; font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); }
       @top-right{ content:string(rh, last); font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); text-transform:uppercase; }
       @bottom-left{ content:"ROME FOR AMERICANS"; font-family:'Mono'; font-size:8px; letter-spacing:.14em; color:var(--grey); }
       @bottom-right{ content:counter(page); font-family:'Barlow'; font-weight:600; font-size:12px; color:var(--ink); } }
html,body{ background:var(--paper); } .pagedjs_sheet{ background:var(--paper); }
body{ font-family:'PlexSans'; font-size:10.5px; line-height:15px; color:var(--ink); }
i.mk{ color:var(--o1); font-weight:400; }
.pg{ break-before:page; } .pg:first-child{ break-before:auto; }
.tabs{ display:grid; grid-auto-flow:column; grid-auto-columns:1fr; column-gap:6px; margin-bottom:14px; }
.tabs .t{ height:26px; display:flex; align-items:center; padding:0 9px; font-family:'Mono'; font-size:7.5px; letter-spacing:.08em; text-transform:uppercase; white-space:nowrap; overflow:hidden; }
.hd{ display:grid; grid-template-columns:1fr 201.3px; column-gap:24px; align-items:end; margin-bottom:12px; }
h1{ font-family:'Barlow'; font-weight:600; font-size:44px; line-height:.92; letter-spacing:.005em; text-transform:uppercase; margin:0 0 8px; }
.sf{ font-size:13px; line-height:18px; margin:0; width:520px; }
.meta{ font-family:'Mono'; font-size:8px; line-height:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--grey); border-left:2px solid var(--ink); padding-left:10px; }
.meta b{ color:var(--ink); font-weight:500; }
figure{ margin:0; }
figure.tree{ margin:0 0 12px; border-top:1px solid var(--ink); padding-top:8px; } figure.tree svg{ display:block; width:100%%; height:auto; }
figure.tree figcaption, figure.mapf figcaption{ font-family:'Mono'; font-size:8px; letter-spacing:.08em; text-transform:uppercase; color:var(--grey); margin-top:4px; }
.res{ display:grid; grid-template-columns:118px 1fr; column-gap:16px; border:1.5px solid var(--ink); padding:10px 14px; margin:0 0 14px; align-items:start; }
.res .lab{ font-family:'Barlow'; font-weight:600; font-size:20px; line-height:20px; text-transform:uppercase; }
.res .big{ font-weight:600; font-size:12.5px; line-height:16px; margin:0 0 4px; } .res p{ margin:0; }
.cols{ display:grid; grid-template-columns:314px 314px; column-gap:24px; align-items:start; }
.cols p{ margin:0 0 8px; text-align:left; hyphens:auto; }
.parts{ border-top:1.5px solid var(--ink); }
.parts .lab, .ts .lab, .cal .lab{ font-family:'Barlow'; font-weight:600; font-size:15px; line-height:18px; text-transform:uppercase; display:block; padding:6px 0 4px; }
.parts .r{ display:grid; grid-template-columns:22px 1fr 150px; column-gap:10px; padding:6px 0; border-top:1px solid var(--line); align-items:start; }
.parts.narrow .r{ grid-template-columns:14px 1fr; column-gap:8px; } .parts.narrow .sw{ width:12px; height:12px; } .parts.narrow .v{ grid-column:2; padding-top:3px; }
.parts .sw{ width:16px; height:16px; margin-top:1px; }
.parts .opt{ font-weight:600; font-size:11px; line-height:14px; } .parts .sub{ font-size:9.5px; line-height:13px; color:var(--grey); }
.parts .v{ font-family:'Mono'; font-size:8.5px; line-height:12px; letter-spacing:.04em; text-transform:uppercase; padding-top:2px; }
.shots{ display:grid; grid-template-columns:314px 314px; column-gap:24px; margin:14px 0 0; }
.shot{ position:relative; } .shot img{ display:block; width:100%%; height:140px; object-fit:cover; }
.shot .co{ position:absolute; width:20px; height:20px; border-radius:50%%; background:#fff; color:var(--ink); font-family:'Barlow'; font-weight:600; font-size:13px; display:flex; align-items:center; justify-content:center; border:1.5px solid var(--ink); }
.shot .co::after{ content:''; position:absolute; left:50%%; top:100%%; width:1.5px; height:var(--l,22px); background:#fff; transform:translateX(-50%%); }
.shot figcaption{ font-size:9.5px; line-height:13px; margin-top:6px; }
.shots.big{ grid-template-columns:1fr; row-gap:18px; margin-top:0; } .shots.big img{ height:330px; } .shots.big figcaption{ font-size:10.5px; line-height:15px; } .shot figcaption b{ font-family:'Barlow'; font-weight:600; font-size:12px; }
.ts{ border-top:1.5px solid var(--ink); margin-top:14px; }
.ts .r{ display:grid; grid-template-columns:200px 1fr; column-gap:14px; padding:5px 0; border-top:1px solid var(--line); }
.ts .k{ font-weight:600; font-size:10.5px; } .ts .k b{ display:block; font-family:'Mono'; font-size:7.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--o1); font-weight:500; } .ts p{ margin:0; }
.cal{ margin-top:14px; border:1.5px solid var(--o3); display:grid; grid-template-columns:118px 1fr; column-gap:14px; padding:8px 12px; }
.cal .lab{ color:var(--o3); padding:0; } .cal p{ margin:0; font-size:10px; line-height:14px; } .cal .x{ color:var(--grey); }
figure.mapf svg{ display:block; width:100%%; height:auto; }
''' % {'F': FONTS, 'H': HOUSE}

def tabs(d):
    return '<div class="tabs">' + ''.join(f'<div class="t" style="background:{OPT[i]};color:{TXT[i]}">{i+1} · {esc(r["opt"].split(" — ")[0])}</div>' for i, r in enumerate(d['ledger'])) + '</div>'
def hd(d, meta):
    return f'<span class="rh-src">{esc(d["kicker"])}</span>{tabs(d)}<div class="hd"><div><h1>{esc(d["title"])}</h1><div class="sf">{d["standfirst"]}</div></div><div class="meta">{meta}</div></div>'
def res(d): return f'<div class="res"><div class="lab">Result</div><div><div class="big">{esc(d["verdict_strong"])}</div><p>{d["verdict_rest"]}</p></div></div>'
def parts(d, narrow=False, tail=''):
    return f'<div class="parts{" narrow" if narrow else ""}"><span class="lab">Parts list · %s</span>' % esc(d['ledger_caption']) + ''.join(
        f'<div class="r"><div class="sw" style="background:{OPT[i]}"></div><div><div class="opt">{r["opt"]}</div><div class="sub">{esc(r["sub"])}</div></div><div class="v" style="color:{OPT[i] if i != 1 else "#8a6410"}">{esc(r["call"])}{tail}</div></div>'
        for i, r in enumerate(d['ledger'])) + '</div>'
def ts(d): return '<div class="ts"><span class="lab">Troubleshooting</span>' + ''.join(f'<div class="r"><div class="k"><b>{esc(f["lab"])}</b>{esc(f["strong"])}</div><p>{esc(f["text"])}</p></div>' for f in d['forks']) + '</div>'
def cal(d): return f'<div class="cal"><span class="lab"><i class="mk">◆</i> Caution 2026</span><p>{d["note"]} <span class="x">{esc(d["note_xref"])}</span></p></div>'
def shot(src, items, cap, pos='50% 50%'):
    cos = ''.join(f'<div class="co" style="left:{x}%;top:{y}%;--l:{l}px">{n}</div>' for n, x, y, l in items)
    return f'<figure class="shot"><div style="position:relative"><img src="{photo(src)}" style="object-position:{pos}">{cos}</div><figcaption>{cap}</figcaption></figure>'

def tree(nodes, edges, side, W=652, H=300, cap=''):
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="PlexSans">',
         '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2B241A"/></marker></defs>']
    for a, b, lab in edges:
        ax, ay, aw, ah = nodes[a][:4]; bx, by, bw, bh = nodes[b][:4]
        x1, y1 = ax + aw / 2, ay + ah; x2, y2 = bx + bw / 2, by
        if abs(x1 - x2) < 2: s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2B241A" stroke-width="1.2" marker-end="url(#a)"/>')
        else:
            my = (y1 + y2) / 2; s.append(f'<path d="M{x1},{y1} L{x1},{my} L{x2},{my} L{x2},{y2}" fill="none" stroke="#2B241A" stroke-width="1.2" marker-end="url(#a)"/>')
        if lab:
            lx, ly = x1, (y1 + y2) / 2 + 3
            s.append(f'<rect x="{lx+4}" y="{ly-9}" width="{len(lab)*5.2+6}" height="12" fill="#EFE4CC"/><text x="{lx+7}" y="{ly}" font-family="Mono" font-size="7.5" fill="#2B241A" letter-spacing=".5">{lab}</text>')
    for k, (x, y, w, h, title, sub, col, kind, tc) in nodes.items():
        if kind == 'q':
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#EFE4CC" stroke="#2B241A" stroke-width="1.2"/>')
            lines = title.split('|')
            for j, ln in enumerate(lines): s.append(f'<text x="{x+w/2}" y="{y+h/2+4+(j-(len(lines)-1)/2)*11}" font-size="9" font-weight="600" fill="#2B241A" text-anchor="middle">{ln}</text>')
        elif kind == 'start':
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#2B241A"/><text x="{x+w/2}" y="{y+h/2+3.5}" font-family="Mono" font-size="8" fill="#EFE4CC" text-anchor="middle" letter-spacing="1">{title}</text>')
        else:
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/><text x="{x+10}" y="{y+16}" font-size="10.5" font-weight="600" fill="{tc}">{title}</text>')
            if sub: s.append(f'<text x="{x+10}" y="{y+29}" font-family="Mono" font-size="7.5" fill="{tc}" letter-spacing=".5">{sub}</text>')
    s.append(side); s.append('</svg>')
    return f'<figure class="tree">{"".join(s)}<figcaption>{cap}</figcaption></figure>'

def arrow(x1, y1, x2, y2, lab=''):
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2B241A" stroke-width="1.2" marker-end="url(#a)"/>'
    if lab: out += f'<rect x="{min(x1,x2)+8}" y="{y1-13}" width="{len(lab)*5.2+6}" height="11" fill="#EFE4CC"/><text x="{min(x1,x2)+11}" y="{y1-4}" font-family="Mono" font-size="7.5" letter-spacing=".5">{lab}</text>'
    return out

# ── Decision 01: three questions from the forks; say no to all and the default holds ──
d = CH['d01']; P = d['paras']
N = {'start': (226, 0, 200, 22, 'FIRST TRIP · WHERE TO SLEEP', '', '', 'start', ''),
     'q1': (206, 42, 240, 34, 'Serial day-trips by rail,|barely seeing Rome?', '', '', 'q', ''),
     'a1': (480, 42, 172, 34, '5 · Near Termini', 'EARNS ITS PLACE · 28′', OPT[4], 'o', TXT[4]),
     'q2': (206, 98, 240, 34, 'A large full-service hotel,|specifically?', '', '', 'q', ''),
     'a2': (480, 98, 172, 34, '4 · Prati (or Termini)', 'THE CORE HAS FEW · 38′', OPT[3], 'o', TXT[3]),
     'q3': (206, 154, 240, 34, 'Evenings and atmosphere|outrank the ruins?', '', '', 'q', ''),
     'a3': (480, 154, 172, 34, '3 · Trastevere', 'BRIDGE AND ALL · 20′', OPT[2], 'o', TXT[2]),
     'q4': (206, 210, 240, 34, 'Does the budget allow|Centro Storico?', '', '', 'q', ''),
     'a4': (480, 210, 172, 34, '1 · Centro Storico', 'POSTCARD ROME · 13′', OPT[0], 'o', TXT[0]),
     'a0': (206, 266, 240, 34, '2 · Monti', 'LOCAL FEEL · 13′', OPT[1], 'o', TXT[1])}
E = [('start', 'q1', ''), ('q1', 'q2', 'NO'), ('q2', 'q3', 'NO'), ('q3', 'q4', 'NO'), ('q4', 'a0', 'NO')]
side01 = ''.join(arrow(446, y, 478, y, 'YES') for y in (59, 115, 171, 227))
meta01 = 'Procedure <b>01 · Base</b><br>Reader: first trip, 3 nights<br>Colour = option (parts list)<br>Walk-times in minutes to the core'
d01 = f'''<div class="pg">{hd(d, meta01)}{tree(N, E, side01, H=304, cap='FIG. 01 · The base procedure — four questions from the verdict and its forks; no to all four and Monti holds.')}{res(d)}
  <div class="cols"><div><p>{P[0]}</p></div><div><p>{P[1]}</p></div></div>
</div>
<div class="pg">
  <div class="cols" style="grid-template-columns:426.7px 201.3px"><figure class="mapf">{map_svg({'#F2F7F5': '#E4D6B8', '#0B4E70': '#2B241A', '#0E6390': OPT[0], '#A23520': '#2B241A', '#1B2622': '#2B241A', '#5B6B66': '#6A5C42'}, scale=1.4, fonts={'Plex, monospace': 'Mono, monospace', 'Public, sans-serif': 'PlexSans, sans-serif'})}<figcaption>Fig. 01-A · {esc(d['figure_cap'].split('·',1)[-1].strip())}</figcaption></figure>{parts(d, narrow=True, tail=' to the core')}</div>
  <div class="cols" style="margin-top:12px"><div><p>{P[2]}</p></div><div><p>{P[3]}</p></div></div>
  {ts(d)}{cal(d)}</div>
<div class="pg"><div class="shots big">{shot('d01-band.jpg', [(1, 22, 55, 22), (2, 74, 40, 22)], '<b>1</b> &nbsp;The Colosseum — an outer edge of the core, twenty minutes’ walk from the centre. &nbsp;<b>2</b> &nbsp;St Peter’s — the Prati side, thirty-eight minutes.', '50% 50%')}{shot('d01-lane.jpg', [(3, 50, 62, 22)], '<b>3</b> &nbsp;The lane inside the core: the walk home at midnight is not travel overhead. It is the thing you came for.', '50% 40%')}</div></div>'''

# ── Decision 05: which line does the sight have, and what does a paid skip buy? ──
d = CH['d05']; P = d['paras']
N5 = {'start': (226, 0, 200, 22, 'A SIGHT · WHICH LINE?', '', '', 'start', ''),
      'q1': (206, 42, 240, 34, 'Is admission free?|(St Peter’s)', '', '', 'q', ''),
      'a1': (480, 42, 172, 34, '2 · Security only', 'GO EARLY · OR PASSAGE-TOUR', OPT[1], 'o', TXT[1]),
      'q2': (206, 98, 240, 34, 'Mandatory slot, no walk-ins?|(Borghese)', '', '', 'q', ''),
      'a2': (480, 98, 172, 34, '3 · No line to skip', 'JUST BOOK AHEAD', OPT[2], 'o', TXT[2]),
      'q3': (206, 154, 240, 34, 'Timed, sells out weeks ahead?|(Vatican Museums)', '', '', 'q', ''),
      'a3': (480, 154, 172, 34, '1 · Book the official timed ticket', 'SKIPS THE TICKET LINE', OPT[0], 'o', TXT[0]),
      'q4': (206, 210, 240, 34, 'Someone sells you|“skip the line”?', '', '', 'q', ''),
      'a4': (480, 210, 172, 34, '4 · The timed ticket + a markup', 'A TOUR OR A MARKUP · NEVER MAGIC', OPT[3], 'o', TXT[3]),
      'a0': (206, 266, 240, 34, 'Everyone still clears security', 'NO PRODUCT SKIPS THE CHECK ITSELF', OPT[4], 'o', TXT[4])}
E5 = [('start', 'q1', ''), ('q1', 'q2', 'NO'), ('q2', 'q3', 'NO'), ('q3', 'q4', 'NO'), ('q4', 'a0', 'EITHER WAY')]
side05 = ''.join(arrow(446, y, 478, y, 'YES') for y in (59, 115, 171, 227))
meta05 = 'Procedure <b>05 · Vatican</b><br>Reader: first trip<br>Colour = sight (parts list)<br>Callouts ① ② = what the ledger names'
d05 = f'''<div class="pg">{hd(d, meta05)}{tree(N5, E5, side05, H=304, cap='FIG. 05 · The two-lines procedure — each sight answered from the ledger; the last node is true of all of them.')}{res(d)}
  <div class="cols"><div><p>{P[0]}</p></div><div><p>{P[1]}</p></div></div></div>
<div class="pg">{parts(d)}
  <div class="cols" style="margin-top:14px"><div><p>{P[2]}</p><p>{P[3]}</p></div><div><p>{P[4]}</p></div></div>
  {cal(d)}{ts(d)}</div>
<div class="pg"><div class="shots big">{shot('d05-gallery.jpg', [(1, 40, 60, 22)], '<b>1</b> &nbsp;The Borghese Gallery — mandatory timed reservation, hard cap, no walk-ins: your “skip the line” already.', '50% 45%')}{shot('stpeters.jpg', [(2, 50, 44, 22)], '<b>2</b> &nbsp;St Peter’s — free; the wait is the square’s security line, out-scheduled by timing or the passage-tour.', '50% 30%')}</div></div>'''

html = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Rome — Le Manuel</title><style>{CSS}</style></head><body>{d01}{d05}</body></html>'
write(html)
