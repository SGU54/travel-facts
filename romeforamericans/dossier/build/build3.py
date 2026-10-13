#!/usr/bin/env python3
# build3.py — the assembler. Execs the modules, resolves {FIG_*}/{PHOTO_*} slots via the
# fig()/photo() renderers, orders the pages, writes dossier3.html. Portable BUILD path.
import os, re, sys
BUILD = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, BUILD)

import design2, maps, illus, covers, content, content2, content3, content4, content5, prose

# ── slot resolution ──────────────────────────────────────────────────────────
# FIG slots → a fig()-wrapped SVG with a FIG. n caption; PHOTO slots → photo() or "".
FIGS = {
 "FIG_RING":      lambda: maps.fig(maps.GFX_RING(),   "The classic-sights core, one kilometre around the Pantheon — walk-times as published."),
 "FIG_TRANSIT":   lambda: maps.fig(maps.GFX_TRANSIT(),"Metro lines A and B to scale; the historic centre sits in the gap between them."),
 "FIG_ARRIVAL":   lambda: maps.fig(maps.GFX_ARRIVAL(),"Fiumicino to the centre, four ways, on one time axis. Fares live on the Field Sheet."),
 "FIG_WEEK":      lambda: maps.fig(maps.GFX_WEEK(),   "The sights' own week — closures cluster on Mondays and Sundays; Wednesday belongs to the square."),
 "FIG_MONTHS":    lambda: maps.fig(maps.GFX_MONTHS(), "Heat, crowds and price across the year; the two shoulder windows bracketed."),
 "FIG_FLOW_COL":  lambda: maps.fig(maps.GFX_FLOW_COL(),"The ancient core as one sequence — high ground first, one combined ticket throughout."),
 "FIG_SECTION":   lambda: maps.fig(illus.ILLUS_SECTION(),"The Colosseum in section — what each of the three tickets actually reaches."),
 "FIG_FLOW_VAT":  lambda: maps.fig(maps.GFX_FLOW_VAT(),"The Vatican as one operation — book, screen, Museums, basilica, dome, in order."),
 "FIG_TRAP":      lambda: maps.fig(maps.GFX_TRAP(),   "The rent ring: within 120 m of each famous square the view is on the bill; the escape is a block."),
 "FIG_DAYTRIPS":  lambda: maps.fig(maps.MAP_DAYTRIPS(),"Every day-trip priced by rail-minutes, centre to centre — the axis the verdicts stand on."),
 "FIG_LEAKS":     lambda: maps.fig(maps.GFX_LEAKS(),"Where the money actually goes — ordered by size, and by which page decides it."),
 "FIG_TREE":      lambda: maps.fig(maps.GFX_TREE(),   "The base decision, compressed to the four questions that separate the neighborhoods."),
 "FIG_DAY1":      lambda: maps.fig(maps.MAP_DAY(1),   "Day one on foot — the ancient core, then the Baroque centre, then the river at dusk."),
 "FIG_DAY2":      lambda: maps.fig(maps.MAP_DAY(2),   "Day two — the Vatican in the morning, the long diagonal home in the afternoon."),
 "FIG_DAY3":      lambda: maps.fig(maps.MAP_DAY(3),   "Day three — the Borghese by appointment, then the quarters where Rome eats."),
}
# Class per slot, set from the measured free space on each target page.
PHOTO_CLS = {"A04":"strip", "A05":"strip", "A06":"strip", "A08":"strip"}

def resolve(html):
    def sub(m):
        key=m.group(1)
        if key in FIGS: return FIGS[key]()
        if key.startswith("PHOTO_"):
            slot=key.split("_",1)[1]
            return content4.photo(slot, content4.CAPTIONS.get(slot,""),
                                  cls=PHOTO_CLS.get(slot,"band"))
        return m.group(0)
    return re.sub(r"\{(FIG_[A-Z0-9_]+|PHOTO_[A-Z0-9]+)\}", sub, html)

# ── page wrapper ─────────────────────────────────────────────────────────────
def page(inner, folio_l, folio_r, n, cls=""):
    body=resolve(inner)
    fol=(f'<div class="folio"><span>{folio_l}</span>'
         f'<span class="n">{n}</span><span>{folio_r}</span></div>') if n else ""
    return f'<section class="page {cls}">{body}{fol}</section>'

# ── decision pages ──
DEC = {d["n"]: content.decision_page(d) for d in content.DECISIONS}

# ── the running order ────────────────────────────────────────────────────────
RUN = []  # (inner_html, folio_left, folio_right, cls)  — folio number auto-assigned
def add(inner, l="ROME, SOLVED.", r="", cls=""): RUN.append((inner, l, r, cls))

# front matter
add(prose.OPENING,     r="THE CONTRACT")
add(prose.HOWTO,       r="HOW TO READ")
add(prose.CONTENTS({}),r="CONTENTS")
# chapter 1 — the ground
add(content2.GROUND_1, r="THE GROUND")
add(content2.GROUND_2, r="THE GROUND")
add(content2.GROUND_3, r="THE GROUND")
# chapter 2 — before you fly
add(content4.BEFORE,   r="BEFORE YOU FLY")
# chapter 3 — day zero
add(content5.DAYZERO_1,r="DAY ZERO")
# chapter 4 — timing
add(content5.TIMING_1, r="TIMING")
add(content5.TIMING_2, r="TIMING")
add(content5.HORIZONS, r="HORIZONS")
# the decisions (14) — each its own page
for k in [f"{i:02d}" for i in range(1,15)]:
    add(DEC[k], r=f"DECISION {k}", cls="dec")
# chapter 5 — set pieces
add(content3.SET_COL_1, r="SET PIECES")
add(content3.SET_COL_2, r="SET PIECES")
add(content3.SET_VAT_1, r="SET PIECES")
add(content3.SET_VAT_2, r="SET PIECES")
# chapter 6 — eating
add(content3.EATING_1, r="EATING")
add(content3.EATING_2, r="EATING")
# chapter 7 — money
add(content3.MONEY,    r="MONEY")
# chapter 8 — the plan
add(content5.PLAN_1,   r="THE PLAN")
add(content5.PLAN_2,   r="THE PLAN")
add(content5.PLAN_3,   r="THE PLAN")
# chapter 11 — where to stay
add(content5.STAY_ASSESS_1(),r="WHERE TO STAY")
add(content5.STAY_ASSESS_2(),r="WHERE TO STAY")
add(content5.STAY_TREE(),   r="WHERE TO STAY")
# chapter 10 — the fourth day
add(content3.FOURTH_1, r="THE FOURTH DAY")
add(content3.FOURTH_2, r="THE FOURTH DAY")
# chapter 9 — failure modes
for p in content2.failure_pages():
    add(p, r="FAILURE MODES")
# chapter 12 — the kit
add(content5.KIT,      r="THE KIT")
# back matter
add(prose.BACKMATTER,  r="THE REFUSALS")
# the field sheet (own banner)
add(content5.FS_1, l="THE FIELD SHEET", r="§1 · VERIFIED", cls="fs")
add(content5.FS_2, l="THE FIELD SHEET", r="§2 · CONFIRM",  cls="fs")
add(content5.FS_3, l="THE FIELD SHEET", r="§3 · CALENDAR", cls="fs")
# closing
add(prose.CLOSING,     r="CLOSING")

# ── emit ─────────────────────────────────────────────────────────────────────
pages=[]
_s=content4._img64("A01")
_strip=(f'<div class="covstrip"><img src="{_s}" style="object-position:{content4.POS["A01"]}"/></div>'
        if _s else "")
pages.append(f'<section class="cov">{resolve(covers.COVER(_strip))}</section>')  # cover, no folio
folio=1
for inner,l,r,cls in RUN:
    pages.append(page(inner,l,r,folio,cls)); folio+=1

html=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Rome, Solved.</title><style>{design2.CSS}</style></head>
<body>{''.join(pages)}</body></html>"""

out=f"{BUILD}/dossier3.html"
open(out,"w").write(html)
print(f"pages: {folio-1} numbered + cover = {folio} total")
print(f"figures placed: {maps._fign[0]}   photos placed: {content4._photn[0]}")
print(f"wrote {out}  ({len(html)//1024} KB)")
