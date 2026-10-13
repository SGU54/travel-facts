# -*- coding: utf-8 -*-
"""Stage D, second pass — two more figures to break the text run.
(1) the month strip: when to go, coarse bands (no drifting numbers)
(2) the booking-horizon bar: how far ahead each thing must be booked
Both are STRUCTURAL claims (● established) — no volatile figures on the page."""

PAPER="#F2F7F5"; INK="#1B2622"; ACCENT="#0E6390"; DEEP="#0B4E70"
GILT="#E0A828"; BRASS="#A23520"; LINE="#D3DED9"; MUTED="#5B6B66"

# ── FIGURE: the month strip ────────────────────────────────────────────────
# bands from the corpus's own coarse climate/crowd reading — deliberately
# non-numeric so it can't go stale.
MONTHS = [
    ("JAN","cold"),("FEB","cold"),("MAR","good"),("APR","good"),
    ("MAY","best"),("JUN","best"),("JUL","hot"),("AUG","hot"),
    ("SEP","best"),("OCT","best"),("NOV","good"),("DEC","cold"),
]
BAND = {
    "best": (GILT,   "sweet spot"),
    "good": (ACCENT, "shoulder"),
    "hot":  (BRASS,  "peak heat &amp; crowds"),
    "cold": ("#8FA8A2", "quiet, sea out"),
}

def month_strip():
    W,H = 620, 180
    pad_l, pad_t = 8, 34
    cell = (W - pad_l*2) / 12
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    for i,(m,b) in enumerate(MONTHS):
        x = pad_l + i*cell
        col,_ = BAND[b]
        h = 54
        s.append(f'<rect x="{x+1.5:.1f}" y="{pad_t}" width="{cell-3:.1f}" height="{h}" fill="{col}" opacity="{0.92 if b=="best" else 0.66}"/>')
        s.append(f'<text x="{x+cell/2:.1f}" y="{pad_t+h+15}" fill="{INK}" font-size="9.5" text-anchor="middle" font-family="Plex, monospace" letter-spacing="0.5">{m}</text>')
    # legend
    lx = pad_l; ly = pad_t + 92
    for key in ["best","good","hot","cold"]:
        col,label = BAND[key]
        s.append(f'<rect x="{lx}" y="{ly-8}" width="11" height="11" fill="{col}" opacity="{0.92 if key=="best" else 0.66}"/>')
        s.append(f'<text x="{lx+16}" y="{ly+1}" fill="{MUTED}" font-size="9" font-family="Public, sans-serif">{label}</text>')
        lx += 22 + len(label)*5.6 + 26
    s.append(f'<text x="{pad_l}" y="{20}" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">THE YEAR, COARSELY \u2014 WHAT CHANGES IS HEAT, CROWDS, AND WHETHER THE SEA IS IN PLAY</text>')
    s.append('</svg>')
    return '\n'.join(s)

# ── FIGURE: booking horizons ───────────────────────────────────────────────
# how far ahead each thing must be committed. Structural, not price.
HORIZONS = [
    ("Sagrada Fam\u00edlia slot",        10, "the binding constraint", True),
    ("Park G\u00fcell slot",              6,  "weeks ahead", True),
    ("Hotel (peak / centenary yr)",  8,  "weeks ahead for the good stock", False),
    ("Licensed apartment (HUTB)",    8,  "weeks \u2014 shrinking supply books early", False),
    ("Day-trip rail seat",           1,  "days \u2014 walk-up is fine", False),
    ("Palau / Mir\u00f3 / museum slot",   1,  "day before is plenty", False),
]
def horizons():
    W,H = 620, 250
    left = 168; right = W-30; top = 40
    maxw = 12.0   # weeks scale
    row = 30
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="0" y="18" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">HOW FAR AHEAD \u2014 THE ONLY TWO THAT TRULY BIND ARE IN GOLD</text>')
    # scale ticks
    for wk in [0,2,4,6,8,10,12]:
        x = left + (wk/maxw)*(right-left)
        s.append(f'<line x1="{x:.1f}" y1="{top-8}" x2="{x:.1f}" y2="{top+len(HORIZONS)*row-14}" stroke="{LINE}" stroke-width="1"/>')
        s.append(f'<text x="{x:.1f}" y="{top-13}" fill="{MUTED}" font-size="7.5" text-anchor="middle" font-family="Plex, monospace">{wk}w</text>')
    for i,(name,wk,note,binding) in enumerate(HORIZONS):
        y = top + i*row
        col = GILT if binding else ACCENT
        bw = (wk/maxw)*(right-left)
        s.append(f'<text x="{left-10}" y="{y+4}" fill="{INK}" font-size="10" text-anchor="end" font-family="Public, sans-serif" font-weight="{700 if binding else 400}">{name}</text>')
        s.append(f'<rect x="{left}" y="{y-6}" width="{max(bw,3):.1f}" height="12" fill="{col}" opacity="{0.9 if binding else 0.55}" rx="1.5"/>')
        # keep the note inside the canvas: if it would run past the right edge,
        # set it INSIDE the bar, right-aligned, in ink rather than muted.
        approx = len(note)*4.3
        if left+max(bw,3)+8+approx > W-6:
            s.append(f'<text x="{left+bw-8:.1f}" y="{y+4}" fill="{INK}" font-size="8" '
                     f'text-anchor="end" font-family="Public, sans-serif">{note}</text>')
        else:
            s.append(f'<text x="{left+max(bw,3)+8:.1f}" y="{y+4}" fill="{MUTED}" font-size="8" font-family="Public, sans-serif">{note}</text>')
    s.append('</svg>')
    return '\n'.join(s)

open('assets/fig-months.svg','w').write(month_strip())
open('assets/fig-horizons.svg','w').write(horizons())
print("wrote fig-months.svg + fig-horizons.svg")

# ── FIGURE: the four traps across a trip (the hero chapter's visual) ────────
def traps_timeline():
    W,H = 620, 250
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="0" y="16" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">WHERE EACH ONE MEETS YOU \u2014 FOUR MOMENTS, FOUR MOODS, NEVER ADDED UP</text>')
    # the trip spine
    y = 116
    x0, x1 = 46, W-40
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="2.5"/>')
    s.append(f'<text x="{x0-6}" y="{y+4}" fill="{MUTED}" font-size="8" text-anchor="end" font-family="Plex, monospace">ARRIVE</text>')
    s.append(f'<text x="{x1+4}" y="{y+4}" fill="{MUTED}" font-size="8" font-family="Plex, monospace">FLY</text>')
    stops = [
        (0.06, "Airport gate", "the metro ticket\nyours doesn't cover", "up"),
        (0.34, "Any terminal", "\u201cpay in dollars?\u201d\nsay euros \u2014 every time", "down"),
        (0.60, "The blue ATM", "tourist machine,\nlayered fees", "up"),
        (0.88, "Check-out", "the bed tax nobody\nquoted you", "down"),
    ]
    for frac,label,note,dirn in stops:
        x = x0 + frac*(x1-x0)
        s.append(f'<circle cx="{x:.1f}" cy="{y}" r="6.5" fill="{BRASS}" stroke="{DEEP}" stroke-width="1.5"/>')
        if dirn=="up":
            ly = y-22; ty = y-52
            s.append(f'<line x1="{x:.1f}" y1="{y-8}" x2="{x:.1f}" y2="{ly}" stroke="{LINE}" stroke-width="1"/>')
            s.append(f'<text x="{x:.1f}" y="{ty}" fill="{INK}" font-size="10" text-anchor="middle" font-family="Public, sans-serif" font-weight="700">{label}</text>')
            for i,ln in enumerate(note.split("\n")):
                s.append(f'<text x="{x:.1f}" y="{ty+12+i*11}" fill="{MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">{ln}</text>')
        else:
            ly = y+22; ty = y+40
            s.append(f'<line x1="{x:.1f}" y1="{y+8}" x2="{x:.1f}" y2="{ly}" stroke="{LINE}" stroke-width="1"/>')
            s.append(f'<text x="{x:.1f}" y="{ty}" fill="{INK}" font-size="10" text-anchor="middle" font-family="Public, sans-serif" font-weight="700">{label}</text>')
            for i,ln in enumerate(note.split("\n")):
                s.append(f'<text x="{x:.1f}" y="{ty+12+i*11}" fill="{MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">{ln}</text>')
    s.append(f'<text x="{W/2:.0f}" y="{H-10}" fill="{ACCENT}" font-size="9" text-anchor="middle" font-family="Public, sans-serif" font-style="italic">Each is defensible alone. The pattern is the product.</text>')
    s.append('</svg>')
    return '\n'.join(s)

open('assets/fig-traps.svg','w').write(traps_timeline())
print("wrote fig-traps.svg")

# ── FIGURE: Zone 1 and the hole (The Ground) ───────────────────────────────
def zone_hole():
    W,H = 620, 205
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="0" y="16" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">ONE INTEGRATED SYSTEM \u2014 WITH ONE GAP, SITED WHERE YOU\u2019RE MOST RUSHED</text>')
    cx, cy, r = 250, 112, 66
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACCENT}" opacity="0.10" stroke="{ACCENT}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx}" y="{cy-6}" fill="{DEEP}" font-size="15" text-anchor="middle" font-family="Anton, sans-serif" letter-spacing="0.5">ZONE 1</text>')
    s.append(f'<text x="{cx}" y="{cy+10}" fill="{MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">metro \u00b7 bus \u00b7 tram \u00b7 funicular \u00b7 local rail</text>')
    s.append(f'<text x="{cx}" y="{cy+24}" fill="{MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">one ticket covers essentially everything</text>')
    # the airport, outside, with a broken link
    ax, ay = 500, 112
    s.append(f'<line x1="{cx+r}" y1="{cy}" x2="{ax-26}" y2="{ay}" stroke="{BRASS}" stroke-width="2" stroke-dasharray="6 5"/>')
    # the break mark
    mx = (cx+r+ax-26)/2
    s.append(f'<line x1="{mx-7}" y1="{ay-11}" x2="{mx+7}" y2="{ay+11}" stroke="{BRASS}" stroke-width="2.5"/>')
    s.append(f'<line x1="{mx+7}" y1="{ay-11}" x2="{mx-7}" y2="{ay+11}" stroke="{BRASS}" stroke-width="2.5"/>')
    s.append(f'<text x="{mx}" y="{ay-20}" fill="{BRASS}" font-size="8.5" text-anchor="middle" font-family="Plex, monospace" letter-spacing="0.8">T-CASUAL STOPS HERE</text>')
    s.append(f'<circle cx="{ax}" cy="{ay}" r="24" fill="{GILT}" opacity="0.85" stroke="{DEEP}" stroke-width="1.5"/>')
    s.append(f'<text x="{ax}" y="{ay+4}" fill="{INK}" font-size="10" text-anchor="middle" font-family="Public, sans-serif" font-weight="700">BCN</text>')
    s.append(f'<text x="{ax}" y="{ay+40}" fill="{INK}" font-size="9.5" text-anchor="middle" font-family="Public, sans-serif" font-weight="700">Airport metro</text>')
    s.append(f'<text x="{ax}" y="{ay+52}" fill="{MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">its own ticket, each way</text>')
    s.append('</svg>')
    return '\n'.join(s)

# ── FIGURE: the five-day shape (The Plan) ──────────────────────────────────
def week_shape():
    W,H = 620, 200
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="0" y="16" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">THREE ANCHORS, TWO FREE DAYS \u2014 THE SHAPE, NOT THE LIST</text>')
    days = [
        ("DAY 1", "Sagrada, then\nthe old city", "anchor"),
        ("DAY 2", "Park G\u00fcell,\nthen downhill", "anchor"),
        ("DAY 3", "market \u00b7 hill \u00b7 sea\nabsorbs overflow", "free"),
        ("DAY 4", "the day trip\nfull clear day", "anchor"),
        ("DAY 5", "no agenda\nthe city itself", "free"),
    ]
    x0 = 22; wcell = (W-44)/5; top = 42; bh = 74
    for i,(d,note,kind) in enumerate(days):
        x = x0 + i*wcell
        anchor = kind=="anchor"
        col = GILT if anchor else ACCENT
        s.append(f'<rect x="{x+5:.1f}" y="{top}" width="{wcell-10:.1f}" height="{bh}" fill="{col}" opacity="{0.85 if anchor else 0.20}" rx="3"/>')
        s.append(f'<text x="{x+wcell/2:.1f}" y="{top+19}" fill="{INK if anchor else DEEP}" font-size="11" text-anchor="middle" font-family="Anton, sans-serif" letter-spacing="0.5">{d}</text>')
        for j,ln in enumerate(note.split("\n")):
            s.append(f'<text x="{x+wcell/2:.1f}" y="{top+36+j*12}" fill="{INK if anchor else MUTED}" font-size="8.5" text-anchor="middle" font-family="Public, sans-serif">{ln}</text>')
        tag = "BOOKED / FIXED" if anchor else "FLOATS"
        s.append(f'<text x="{x+wcell/2:.1f}" y="{top+bh+15}" fill="{BRASS if anchor else MUTED}" font-size="7.5" text-anchor="middle" font-family="Plex, monospace" letter-spacing="0.6">{tag}</text>')
    s.append(f'<text x="{W/2:.0f}" y="{H-16}" fill="{ACCENT}" font-size="9" text-anchor="middle" font-family="Public, sans-serif" font-style="italic">The beach is never a day \u2014 it is whichever afternoon turns warm.</text>')
    s.append('</svg>')
    return '\n'.join(s)

open('assets/fig-zone.svg','w').write(zone_hole())
open('assets/fig-week.svg','w').write(week_shape())
print("wrote fig-zone.svg + fig-week.svg")

# ── FIGURE: the consequence ladder (Failure Modes) ─────────────────────────
def consequence_ladder():
    W,H = 620, 215
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="0" y="16" fill="{BRASS}" font-size="8.5" font-family="Plex, monospace" letter-spacing="1.6">GROUPED BY WHAT IT COSTS \u2014 THE ONLY ORDERING THAT HELPS YOU TRIAGE</text>')
    tiers = [
        ("COSTS YOU MONEY", "recoverable \u00b7 annoying \u00b7 compounding", 6, "#8FA8A2"),
        ("COSTS YOU A DAY", "unrecoverable \u00b7 one of five", 5, ACCENT),
        ("COSTS THE TRIP\u2019S SHAPE", "unrecoverable \u00b7 colours everything", 4, BRASS),
    ]
    x0 = 34; top = 40; bh = 46; gap = 10
    for i,(label,sub,count,col) in enumerate(tiers):
        y = top + i*(bh+gap)
        wfrac = 0.52 + i*0.19
        w = (W-70)*wfrac
        s.append(f'<rect x="{x0}" y="{y}" width="{w:.0f}" height="{bh}" fill="{col}" opacity="{0.16+i*0.14}" stroke="{col}" stroke-width="1.4" rx="3"/>')
        s.append(f'<text x="{x0+14}" y="{y+21}" fill="{DEEP}" font-size="12" font-family="Anton, sans-serif" letter-spacing="0.5">{label}</text>')
        s.append(f'<text x="{x0+14}" y="{y+36}" fill="{MUTED}" font-size="8.5" font-family="Public, sans-serif">{sub}</text>')
        s.append(f'<text x="{x0+w-14:.0f}" y="{y+28}" fill="{col if i else MUTED}" font-size="15" text-anchor="end" font-family="Anton, sans-serif">{count}</text>')
    s.append(f'<text x="{W/2:.0f}" y="{H-10}" fill="{ACCENT}" font-size="9" text-anchor="middle" font-family="Public, sans-serif" font-style="italic">A website of separate articles cannot sort mistakes this way. That is the point of a book.</text>')
    s.append('</svg>')
    return '\n'.join(s)

open('assets/fig-consequence.svg','w').write(consequence_ladder())
print("wrote fig-consequence.svg")
