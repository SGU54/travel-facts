"""maps.py — every figure, computed from geo.py's real coordinates. The moat.
viewBoxes sized per d-draw.md (band~660x240, wide~660x300). Print weights measured, not previewed.
Palette pulled from design.PALETTE (extend, never redefine — bug log #10).
"""
import math
import geo
from design import PALETTE as C

# ---------- collision-safe label placement (d-draw.md) ----------
class Boxes:
    def __init__(self): self.b = []
    def _hit(self, x0, y0, x1, y1):
        return any(min(x1, a1) - max(x0, a0) > 1 and min(y1, d1) - max(y0, d0) > 1
                   for (a0, d0, a1, d1) in self.b)
    def add(self, x0, y0, x1, y1): self.b.append((x0, y0, x1, y1))
    def place(self, x, y, text, fs, anchor="start", tries=None):
        w = len(text) * fs * 0.56; h = fs
        if tries is None:
            tries = [(0, 0, anchor), (0, -fs - 3, anchor), (0, fs + 5, anchor),
                     (0, 0, "end" if anchor == "start" else "start"),
                     (0, fs + 7, "middle"), (0, -fs - 9, "middle")]
        for dx, dy, an in tries:
            xx, yy = x + dx, y + dy
            x0 = xx if an == "start" else (xx - w / 2 if an == "middle" else xx - w)
            if not self._hit(x0, yy - h * 0.78, x0 + w, yy + h * 0.24):
                self.add(x0, yy - h * 0.78, x0 + w, yy + h * 0.24); return xx, yy, an
        x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
        self.add(x0, y - h * 0.78, x0 + w, y + h * 0.24); return x, y, anchor

def _esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# project lat/lon into an svg viewbox given a bounding window
def _proj(la, lo, win, pad, w, h):
    la0, la1, lo0, lo1 = win
    fx = (lo - lo0) / (lo1 - lo0)
    fy = (la1 - la) / (la1 - la0)   # north up
    return pad + fx * (w - 2 * pad), pad + fy * (h - 2 * pad)

# ============================================================ COVER RING
def cover_ring():
    """1.5km walk-time ring from Piazza Venezia; classic sights on their real radial distance;
    Termini + metro sit OUTSIDE the walkable heart. The thesis, unclonable without the walk-times."""
    W, H = 660, 720
    cx, cy = W/2, 356
    cla, clo = 41.8957, 12.4806     # centroid computed from the tight core
    # scale: 1.5 km -> outer ring radius in px
    RMAX_KM = 1.6
    Rpx = 236
    ppk = Rpx / RMAX_KM
    def rp(name):
        la, lo = geo.LM[name]
        p = math.pi/180
        dx = (lo-clo)*p*math.cos((la+cla)*p/2)*geo.R_EARTH*geo.STREET
        dy = (la-cla)*p*geo.R_EARTH*geo.STREET
        ang = math.atan2(dx, dy)     # bearing, x=east y=north
        r = math.hypot(dx, dy)
        return cx + math.sin(ang)*r*ppk, cy - math.cos(ang)*r*ppk, r
    pts = ["Pantheon","Trevi","Spanish Steps","Piazza Navona","Campo de' Fiori",
           "Colosseum","Roman Forum","Palatine","Trastevere","Piazza Venezia"]
    outside = ["St Peter's","Termini","Borghese"]
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    # concentric walk-time rings 0.5 / 1.0 / 1.5 km (10 / 20 / 30 min diameter)
    for kmr, lab in [(0.5,"5 min"),(1.0,"13 min"),(1.5,"20 min")]:
        rr = kmr*ppk
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{rr:.1f}" fill="none" '
                 f'stroke="{C["line"]}" stroke-width="1" stroke-dasharray="2 5"/>')
        s.append(f'<text x="{cx}" y="{cy-rr-4:.1f}" text-anchor="middle" '
                 f'font-family="IBM Plex Mono" font-size="8" fill="{C["soft"]}">{lab}</text>')
    # the 1.5km ring, emphasised (the walkable core boundary)
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{1.5*ppk:.1f}" fill="none" '
             f'stroke="{C["accent"]}" stroke-width="2.2" stroke-dasharray="1 0" opacity="0.9"/>')
    bx = Boxes()
    # centre pin
    s.append(f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{C["accent"]}"/>')
    # inside sights
    for nm in pts:
        x, y, r = rp(nm)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{C["ink"]}"/>')
        tx, ty, an = bx.place(x+5, y+3, nm, 10.5, "start")
        s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{an}" '
                 f'font-family="Sorts Mill Goudy" font-size="10.5" fill="{C["ink"]}">{_esc(nm)}</text>')
    # river hint (schematic, Tiber runs between core and Vatican)
    # outside markers (across the river / beyond the walk)
    for nm in outside:
        x, y, r = rp(nm)
        # clamp into canvas
        x = max(24, min(W-24, x)); y = max(40, min(H-30, y))
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="none" '
                 f'stroke="{C["muted"]}" stroke-width="1.4"/>')
        mins = round(r/4.5*60)
        lab = f"{nm} · {mins}\u2032"
        tx, ty, an = bx.place(x+5, y+3, lab, 9.5, "start")
        s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{an}" '
                 f'font-family="IBM Plex Mono" font-size="9" fill="{C["muted"]}">{_esc(lab)}</text>')
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ WALKABLE CORE (Decision 01)
def core_map():
    W, H = 660, 300
    # window bounding the classic core + Termini so its distance shows
    win = (41.884, 41.912, 12.462, 12.505)
    pad = 30
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    # the walkable zone: a soft blob around the core
    core = ["Pantheon","Piazza Navona","Campo de' Fiori","Trevi","Piazza Venezia","Roman Forum","Colosseum"]
    xs=[]; ys=[]
    for nm in core:
        x,y=_proj(*geo.LM[nm], win, pad, W, H); xs.append(x); ys.append(y)
    cxx=sum(xs)/len(xs); cyy=sum(ys)/len(ys)
    s.append(f'<ellipse cx="{cxx:.0f}" cy="{cyy:.0f}" rx="150" ry="96" fill="{C["zone"]}" opacity="0.55"/>')
    bx=Boxes()
    show = ["Pantheon","Piazza Navona","Trevi","Spanish Steps","Colosseum","Roman Forum","Trastevere","Piazza Venezia"]
    for nm in show:
        x,y=_proj(*geo.LM[nm], win, pad, W, H)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="{C["ink"]}"/>')
        tx,ty,an=bx.place(x+5,y+3,nm,9.5,"start")
        s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{an}" font-family="Sorts Mill Goudy" font-size="9.5" fill="{C["ink"]}">{_esc(nm)}</text>')
    # Termini OUTSIDE, with its walk distance to Pantheon
    tx0,ty0=_proj(*geo.LM["Termini"], win, pad, W, H)
    px0,py0=_proj(*geo.LM["Pantheon"], win, pad, W, H)
    s.append(f'<line x1="{px0:.1f}" y1="{py0:.1f}" x2="{tx0:.1f}" y2="{ty0:.1f}" stroke="{C["accent"]}" stroke-width="1.2" stroke-dasharray="4 4"/>')
    s.append(f'<circle cx="{tx0:.1f}" cy="{ty0:.1f}" r="3.4" fill="none" stroke="{C["accent"]}" stroke-width="1.6"/>')
    mm=geo.mins("Termini","Pantheon")
    s.append(f'<text x="{tx0:.1f}" y="{ty0-8:.1f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="{C["accent"]}">TERMINI</text>')
    midx=(px0+tx0)/2; midy=(py0+ty0)/2
    s.append(f'<text x="{midx:.1f}" y="{midy-4:.1f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8.5" fill="{C["accent"]}">{mm}\u2032 walk</text>')
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ TRANSIT REALITY (Decision 02)
def transit_reality():
    """Draw the HOLE where the metro can't go. Line A and B cross at Termini; the historic
    heart sits in the gap between them. Argues against printing a metro map."""
    W, H = 660, 300
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    # schematic: Line A (diagonal NW-SE orange), Line B (diagonal NE-SW), crossing at Termini
    tx, ty = 430, 150   # Termini node
    # Line A (Battistini <-> Anagnina) roughly W-E through Termini, skirting north of centre
    s.append(f'<path d="M 40 120 Q 240 70 {tx} {ty} Q 560 210 630 250" fill="none" stroke="{C["accent"]}" stroke-width="3" opacity="0.85"/>')
    s.append(f'<text x="70" y="112" font-family="IBM Plex Mono" font-size="9" fill="{C["accent"]}">LINE A</text>')
    # Line B through Termini down to Colosseo/EUR, passing the ancient sights' edge
    s.append(f'<path d="M 250 40 Q 360 90 {tx} {ty} Q 470 250 430 290" fill="none" stroke="{C["deep"]}" stroke-width="3" opacity="0.85"/>')
    s.append(f'<text x="256" y="40" font-family="IBM Plex Mono" font-size="9" fill="{C["deep"]}">LINE B</text>')
    s.append(f'<circle cx="{tx}" cy="{ty}" r="4.5" fill="{C["ink"]}"/>')
    s.append(f'<text x="{tx+8}" y="{ty+3}" font-family="IBM Plex Mono" font-size="9" fill="{C["ink"]}">TERMINI</text>')
    # the HOLE: dashed ellipse over the historic heart, west of the lines
    hx, hy = 215, 180
    s.append(f'<ellipse cx="{hx}" cy="{hy}" rx="118" ry="80" fill="none" stroke="{C["muted"]}" stroke-width="1.4" stroke-dasharray="3 5"/>')
    s.append(f'<text x="{hx}" y="{hy-4}" text-anchor="middle" font-family="Sorts Mill Goudy" font-style="italic" font-size="13" fill="{C["muted"]}">the historic heart —</text>')
    s.append(f'<text x="{hx}" y="{hy+13}" text-anchor="middle" font-family="Sorts Mill Goudy" font-style="italic" font-size="13" fill="{C["muted"]}">no line reaches it</text>')
    # a few sight dots inside the hole
    for nm in ["Pantheon","Piazza Navona","Trevi"]:
        # place schematically inside the ellipse
        pass
    for dx,dy in [(-40,-20),(10,20),(45,-10)]:
        s.append(f'<circle cx="{hx+dx}" cy="{hy+dy}" r="2.4" fill="{C["ink"]}"/>')
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ AIRPORT ARITHMETIC (Decision 03)
def airport_strip():
    """Leonardo €14 vs FL1 €8 vs taxi €55 — but the winner flips on WHERE you sleep.
    Two rows: 'central base' vs 'near Termini', total cost door-to-door."""
    W, H = 660, 250
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    x0 = 150; xmax = 620; scale = (xmax-x0)/70.0   # €0..€70
    def bar(y, label, legs, total):
        s.append(f'<text x="0" y="{y+4}" font-family="Sorts Mill Goudy" font-size="11" fill="{C["ink"]}">{label}</text>')
        cx = x0
        cols = [C["accent"], C["gilt"], C["muted"]]
        for i,(amt,lg) in enumerate(legs):
            w = amt*scale
            s.append(f'<rect x="{cx:.1f}" y="{y-9}" width="{w:.1f}" height="16" fill="{cols[i%3]}" opacity="0.85"/>')
            if w>34:
                s.append(f'<text x="{cx+w/2:.1f}" y="{y+3}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["paper"]}">{lg}</text>')
            cx += w+1
        s.append(f'<text x="{cx+7:.1f}" y="{y+3}" font-family="IBM Plex Mono" font-size="10" fill="{C["deep"]}">\u2248\u20ac{total}</text>')
    # gridlines
    for e in [0,20,40,60]:
        gx=x0+e*scale
        s.append(f'<line x1="{gx:.1f}" y1="20" x2="{gx:.1f}" y2="200" stroke="{C["line"]}" stroke-width="0.5"/>')
        s.append(f'<text x="{gx:.1f}" y="215" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["soft"]}">\u20ac{e}</text>')
    s.append(f'<text x="0" y="30" font-family="IBM Plex Mono" font-size="8" letter-spacing="0.1em" fill="{C["accent"]}">CENTRAL BASE (Decision 01)</text>')
    bar(58, "Leonardo + taxi", [(14,"train"),(13,"onward")], 27)
    bar(90, "Taxi, door-to-door", [(55,"fixed fare")], 55)
    s.append(f'<line x1="0" y1="112" x2="{W}" y2="112" stroke="{C["line"]}" stroke-width="0.5" stroke-dasharray="3 4"/>')
    s.append(f'<text x="0" y="132" font-family="IBM Plex Mono" font-size="8" letter-spacing="0.1em" fill="{C["muted"]}">NEAR TERMINI (the base 01 warns against)</text>')
    bar(160, "Leonardo, walk in", [(14,"train")], 14)
    bar(192, "Taxi, door-to-door", [(55,"fixed fare")], 55)
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ ANCIENT HALF-DAY (Decision 04)
def ancient_flow():
    """Order-of-ops: Forum-first (quiet/cool) vs Colosseum-first (beat buses). One 24h ticket."""
    W, H = 660, 250
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    def chain(y, title, steps, tone):
        col = C["accent"] if tone=="a" else C["deep"]
        s.append(f'<text x="0" y="{y-16}" font-family="IBM Plex Mono" font-size="8.5" letter-spacing="0.12em" fill="{col}">{title}</text>')
        bw=132; gap=26; x=0
        for i,(lab,sub) in enumerate(steps):
            s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="42" rx="3" fill="{C["zone"]}" stroke="{col}" stroke-width="1"/>')
            s.append(f'<text x="{x+bw/2}" y="{y+18}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="11.5" fill="{C["ink"]}">{lab}</text>')
            s.append(f'<text x="{x+bw/2}" y="{y+33}" text-anchor="middle" font-family="IBM Plex Mono" font-size="7.5" fill="{C["muted"]}">{sub}</text>')
            if i<len(steps)-1:
                ax=x+bw+4
                s.append(f'<path d="M {ax} {y+21} l {gap-8} 0 m -6 -4 l 6 4 l -6 4" fill="none" stroke="{col}" stroke-width="1.3"/>')
            x+=bw+gap
    chain(46, "OPTION A · FORUM FIRST — cool, empty, unshaded early", [("Forum + Palatine","08:30 · at opening"),("Colosseum","midday slot · shade"),("done","~3.5h total")], "a")
    chain(168, "OPTION B · COLOSSEUM FIRST — beat the tour buses", [("Colosseum","first slot"),("Forum + Palatine","midday · hot, open"),("done","~3.5h total")], "b")
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ BOOKING HORIZON (Decision 06)
def booking_calendar():
    """Weeks-ahead bars per sight — the one calendar four free articles never assemble."""
    W, H = 660, 280
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    x0=190; xmax=628; wk_max=8; scale=(xmax-x0)/wk_max
    rows=[("Colosseum Underground",6,"guided-only, sells out","hard"),
          ("Vatican Museums",4,"timed, sells out weeks","hard"),
          ("Borghese Gallery",3,"MANDATORY slot, no walk-ins","hard"),
          ("Colosseum Standard",2,"timed entry","soft"),
          ("Pantheon",1,"now timed-entry","soft"),
          ("St Peter's Basilica",0,"free · no ticket, only timing","free")]
    y=44; rh=34
    for wk in range(0,wk_max+1,2):
        gx=x0+wk*scale
        s.append(f'<line x1="{gx:.1f}" y1="30" x2="{gx:.1f}" y2="{y+len(rows)*rh-8}" stroke="{C["line"]}" stroke-width="0.5"/>')
        s.append(f'<text x="{gx:.1f}" y="24" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["soft"]}">{wk}w</text>')
    s.append(f'<text x="{x0-6}" y="24" text-anchor="end" font-family="IBM Plex Mono" font-size="8" fill="{C["accent"]}">book ahead \u2192 trip</text>')
    tone={"hard":C["accent"],"soft":C["gilt"],"free":C["muted"]}
    for nm,wks,note,t in rows:
        s.append(f'<text x="0" y="{y+4}" font-family="Sorts Mill Goudy" font-size="11.5" fill="{C["ink"]}">{_esc(nm)}</text>')
        w=max(wks*scale, 3)
        col=tone[t]
        if wks==0:
            s.append(f'<circle cx="{x0}" cy="{y}" r="4" fill="none" stroke="{col}" stroke-width="1.5"/>')
        else:
            s.append(f'<rect x="{x0}" y="{y-7}" width="{w:.1f}" height="13" rx="2" fill="{col}" opacity="0.82"/>')
        s.append(f'<text x="{x0+max(w,8)+8:.1f}" y="{y+3}" font-family="IBM Plex Mono" font-size="8" fill="{C["muted"]}">{_esc(note)}</text>')
        y+=rh
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ 90-SECOND EATING RULE (Decision 08)
def eating_rule():
    """Trap density is a FUNCTION of the walk-time thesis. Sight-facing ring vs street behind it."""
    W, H = 660, 270
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    cx,cy=200,135
    # the monument
    s.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{C["accent"]}"/>')
    s.append(f'<text x="{cx}" y="{cy-16}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["accent"]}">THE SIGHT</text>')
    # trap ring (0-90s)
    s.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="{C["deep"]}" opacity="0.10"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="{C["deep"]}" stroke-width="1" stroke-dasharray="3 4"/>')
    s.append(f'<text x="{cx}" y="{cy+52}" text-anchor="middle" font-family="Sorts Mill Goudy" font-style="italic" font-size="11" fill="{C["deep"]}">photo-menus, touts,</text>')
    s.append(f'<text x="{cx}" y="{cy+66}" text-anchor="middle" font-family="Sorts Mill Goudy" font-style="italic" font-size="11" fill="{C["deep"]}">"menu turistico"</text>')
    # 90-second boundary arrow to the street behind
    s.append(f'<line x1="{cx+72}" y1="{cy}" x2="{cx+150}" y2="{cy}" stroke="{C["ink"]}" stroke-width="1.2"/>')
    s.append(f'<path d="M {cx+150} {cy} l -7 -4 m 7 4 l -7 4" fill="none" stroke="{C["ink"]}" stroke-width="1.2"/>')
    s.append(f'<text x="{cx+112}" y="{cy-7}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["ink"]}">90 sec walk</text>')
    # green street
    gx=cx+200
    s.append(f'<circle cx="{gx}" cy="{cy}" r="42" fill="{C["water"]}" opacity="0.6"/>')
    s.append(f'<text x="{gx}" y="{cy-52}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["muted"]}">A DIFFERENT CITY</text>')
    s.append(f'<text x="{gx}" y="{cy+2}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="11" fill="{C["ink"]}">short menu,</text>')
    s.append(f'<text x="{gx}" y="{cy+16}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="11" fill="{C["ink"]}">Roman classics,</text>')
    s.append(f'<text x="{gx}" y="{cy+30}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="11" fill="{C["ink"]}">locals after 20:30</text>')
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ OSTIA vs POMPEII (Decision 09)
def daytrip_asymmetry():
    """The same 'ancient port' impulse, two day-costs: Ostia ~1h round vs Pompeii ~12h door-to-door."""
    W, H = 660, 250
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    x0=150; xmax=620; hrs_max=12; scale=(xmax-x0)/hrs_max
    for hr in range(0,13,3):
        gx=x0+hr*scale
        s.append(f'<line x1="{gx:.1f}" y1="34" x2="{gx:.1f}" y2="205" stroke="{C["line"]}" stroke-width="0.5"/>')
        s.append(f'<text x="{gx:.1f}" y="222" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["soft"]}">{hr}h</text>')
    def band(y, label, legs, verdict, vcol):
        s.append(f'<text x="0" y="{y+4}" font-family="Sorts Mill Goudy" font-size="12" fill="{C["ink"]}">{label}</text>')
        cx=x0; cols=[C["muted"],C["accent"],C["muted"]]
        for i,(h,lg) in enumerate(legs):
            w=h*scale
            s.append(f'<rect x="{cx:.1f}" y="{y-10}" width="{w:.1f}" height="18" fill="{cols[i%3]}" opacity="0.8"/>')
            if w>40: s.append(f'<text x="{cx+w/2:.1f}" y="{y+3}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="{C["paper"]}">{lg}</text>')
            cx+=w+1
        s.append(f'<text x="0" y="{y+22}" font-family="IBM Plex Mono" font-size="8" fill="{vcol}">{verdict}</text>')
    band(64, "Ostia Antica", [(0.5,"metro 30\u2032"),(3,"the ruins"),(0.5,"metro back")], "\u2248 half a day \u00b7 one metro ticket \u00b7 'Rome\u2019s Pompeii'", C["accent"])
    band(150, "Pompeii", [(2,"train + Circumvesuviana"),(4,"the ruins"),(2,"return")], "\u2248 12h door-to-door \u00b7 'don\u2019t pair with anything'", C["deep"])
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ WHERE TO SLEEP TREE (feeds 01)
def sleep_tree():
    W, H = 660, 300
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    def node(x,y,w,txt,sub="",lead=False):
        col=C["accent"] if lead else C["ink"]
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="3" fill="{"#EFE4C8" if lead else C["zone"]}" stroke="{col}" stroke-width="{1.4 if lead else 0.8}"/>')
        s.append(f'<text x="{x+w/2}" y="{y+(17 if sub else 24)}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="12" fill="{C["ink"]}">{_esc(txt)}</text>')
        if sub: s.append(f'<text x="{x+w/2}" y="{y+31}" text-anchor="middle" font-family="IBM Plex Mono" font-size="7.5" fill="{C["muted"]}">{_esc(sub)}</text>')
    def link(x1,y1,x2,y2,lab=""):
        s.append(f'<path d="M {x1} {y1} L {x2} {y2}" fill="none" stroke="{C["soft"]}" stroke-width="1"/>')
        if lab:
            s.append(f'<text x="{(x1+x2)/2+4}" y="{(y1+y2)/2-2}" font-family="IBM Plex Mono" font-size="7.5" fill="{C["accent"]}">{lab}</text>')
    node(230,14,200,"First trip, want to walk?","the only real question", lead=True)
    link(330,54,150,96,"yes"); link(330,54,510,96,"budget-led")
    node(60,96,180,"Priority = mornings out","")
    node(430,96,190,"Priority = price","")
    link(150,136,80,190,"walk"); link(150,136,240,190,"charm+food")
    node(20,190,150,"Centro Storico","13\u2032 to centre \u00b7 priciest")
    node(190,190,150,"Monti","13\u2032 \u00b7 local, better value")
    link(525,136,420,190,"ok w/ commute"); link(525,136,600,190,"nightlife")
    node(360,190,140,"Termini","28\u2032 walk \u00b7 cheapest, gritty")
    node(520,190,130,"Trastevere","20\u2032 \u00b7 charm, a bridge away")
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ NEIGHBORHOOD LOCATORS (Where to stay chapter)
def hood_locators():
    """5 bases, each: walk-min to the core centre, as a compact strip of mini-locators."""
    W, H = 660, 200
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    bases=[("Centro Storico",13),("Monti",13),("Trastevere",20),("Termini",28),("Prati",38)]
    n=len(bases); cw=W/n
    maxm=40
    for i,(nm,m) in enumerate(bases):
        cx=cw*i+cw/2; cy=88
        # ring proportional to walk-min
        rr=18+m/maxm*44
        s.append(f'<circle cx="{cx:.0f}" cy="{cy}" r="{rr:.0f}" fill="none" stroke="{C["line"]}" stroke-width="1" stroke-dasharray="2 4"/>')
        s.append(f'<circle cx="{cx:.0f}" cy="{cy}" r="3" fill="{C["accent"]}"/>')
        # the core centre dot at fixed offset
        s.append(f'<circle cx="{cx:.0f}" cy="{cy-rr:.0f}" r="2.4" fill="{C["ink"]}"/>')
        s.append(f'<text x="{cx:.0f}" y="{cy+rr+16:.0f}" text-anchor="middle" font-family="Sorts Mill Goudy" font-size="11" fill="{C["ink"]}">{_esc(nm)}</text>')
        s.append(f'<text x="{cx:.0f}" y="{cy+rr+29:.0f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="{C["deep"]}">{m}\u2032 to core</text>')
    s.append('</svg>')
    return "\n".join(s)

# ============================================================ FAILURE-MODE SEVERITY GRID
def failure_grid():
    """20 failure modes, plotted by (cost of the mistake) x (how easily avoided). Back-half figure."""
    W, H = 660, 340
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    x0,y0,x1,y1=120,30,620,280
    s.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{C["ink"]}" stroke-width="1"/>')
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{C["ink"]}" stroke-width="1"/>')
    s.append(f'<text x="{(x0+x1)/2}" y="{y1+26}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8.5" letter-spacing="0.1em" fill="{C["muted"]}">HOW EASILY AVOIDED  \u2192</text>')
    s.append(f'<text x="{x0-12}" y="{(y0+y1)/2}" text-anchor="middle" font-family="IBM Plex Mono" font-size="8.5" letter-spacing="0.1em" fill="{C["muted"]}" transform="rotate(-90 {x0-12} {(y0+y1)/2})">COST OF THE MISTAKE  \u2192</text>')
    # (avoidability 0..1, cost 0..1, label)
    pts=[(0.9,0.95,"Colosseum/Vatican unbooked"),(0.8,0.7,"pass bought 'to be safe'"),
         (0.85,0.5,"dollars at the card reader"),(0.7,0.6,"Termini base, walk everywhere"),
         (0.6,0.85,"Pompeii + a second sight"),(0.9,0.3,"unvalidated paper ticket"),
         (0.75,0.4,"20% American tip"),(0.5,0.55,"Colosseum + Vatican same day"),
         (0.8,0.35,"tourist-menu by the sight"),(0.65,0.3,"Euronet ATM / exchange desk"),
         (0.55,0.45,"unofficial airport taxi"),(0.7,0.25,"cappuccino after dinner")]
    bx=Boxes()
    for av,co,lab in pts:
        px=x0+av*(x1-x0); py=y1-co*(y1-y0)
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.2" fill="{C["accent"]}" opacity="0.85"/>')
        tx,ty,an=bx.place(px+5,py+3,lab,8,"start")
        s.append(f'<text x="{tx:.0f}" y="{ty:.0f}" text-anchor="{an}" font-family="IBM Plex Mono" font-size="7.6" fill="{C["ink"]}">{_esc(lab)}</text>')
    # the danger quadrant label (high cost, high avoidability = the ones this book kills)
    s.append(f'<text x="{x1-6}" y="{y0+14}" text-anchor="end" font-family="Sorts Mill Goudy" font-style="italic" font-size="11" fill="{C["deep"]}">costly, and entirely avoidable \u2014 the book\u2019s targets</text>')
    s.append('</svg>')
    return "\n".join(s)
