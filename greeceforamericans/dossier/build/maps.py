# -*- coding: utf-8 -*-
"""maps.py — every figure, drawn from geo.py's real coordinates. Own artwork only.

The cover and figures are COMPUTED: change a coordinate and they redraw. That is
what makes them unclonable (d-draw.md, cover.md). Palette tints come from design.py's
four origins; no new hues. Label placement uses the collision-safe reserver.
"""
import math
import geo
from design import (PAPER, INK, ACCENT, GILT, MUTED, SOFT, LINE, LINE_SOFT,
                    ZONE, STONE, DEEP, WATER, WIND)

MONO = "PlexMono"; DISP = "Cormorant"; BODY = "Spectral"

# ---- collision-safe label reserver (d-draw.md) ----
class _Boxes:
    def __init__(self): self.b=[]
    def _hit(self,x0,y0,x1,y1):
        return any(min(x1,a1)-max(x0,a0)>1 and min(y1,c1)-max(y0,c0)>1
                   for (a0,c0,a1,c1) in self.b)
    def add(self,x0,y0,x1,y1): self.b.append((x0,y0,x1,y1))
    def place(self,x,y,text,fs,anchor="start",tries=None):
        w=len(text)*fs*0.56; h=fs
        if tries is None:
            tries=[(0,0,anchor),(0,-fs-4,anchor),(0,fs+6,anchor),
                   (0,0,"end" if anchor=="start" else "start"),
                   (0,fs+8,"middle"),(0,-fs-10,"middle")]
        for dx,dy,an in tries:
            xx,yy=x+dx,y+dy
            x0=xx if an=="start" else (xx-w/2 if an=="middle" else xx-w)
            if not self._hit(x0,yy-h*0.78,x0+w,yy+h*0.24):
                self.add(x0,yy-h*0.78,x0+w,yy+h*0.24); return xx,yy,an
        x0=x if anchor=="start" else (x-w/2 if anchor=="middle" else x-w)
        self.add(x0,y-h*0.78,x0+w,y+h*0.24); return x,y,anchor

def _esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---- shared projection: lon/lat -> svg xy over a bounding box ----
def _proj(names, W, H, pad):
    lats=[geo.PLACES[n][0] for n in names]; lons=[geo.PLACES[n][1] for n in names]
    la0,la1=min(lats),max(lats); lo0,lo1=min(lons),max(lons)
    # keep aspect ~ real (cos-corrected)
    midlat=(la0+la1)/2; k=math.cos(midlat*math.pi/180)
    span_lo=(lo1-lo0)*k or 1e-6; span_la=(la1-la0) or 1e-6
    def xy(n):
        la,lo=geo.PLACES[n]
        x=pad+((lo-lo0)*k)/span_lo*(W-2*pad)
        y=pad+(la1-la)/span_la*(H-2*pad)   # north up
        return x,y
    return xy

# =====================================================================
# FIG — THE ROUTE GRAPH (the organising fact): nodes = islands, edges =
# real sea distances, edge weight = corpus ferry time. The spine figure.
# =====================================================================
def route_graph():
    W,H=660,320; pad=52
    nodes=["Piraeus","Paros","Naxos","Mykonos","Ios","Santorini","Milos","Crete"]
    xy=_proj(nodes,W,H,pad)
    # edges as the Cyclades trunk the corpus describes (hub Piraeus/Paros)
    edges=[("Piraeus","Paros"),("Piraeus","Mykonos"),("Paros","Naxos"),
           ("Paros","Mykonos"),("Naxos","Ios"),("Ios","Santorini"),
           ("Paros","Milos"),("Piraeus","Santorini"),("Piraeus","Crete")]
    box=_Boxes()
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>')
    # faint sea grid
    for gx in range(pad,W-pad+1,(W-2*pad)//5):
        s.append(f'<line x1="{gx}" y1="{pad}" x2="{gx}" y2="{H-pad}" stroke="{LINE_SOFT}" stroke-width="0.5"/>')
    # reserve node boxes first
    P={n:xy(n) for n in nodes}
    for n in nodes:
        x,y=P[n]; box.add(x-5,y-5,x+5,y+5)
    # draw edges with sea-distance labels
    for a,b in edges:
        (x1,y1),(x2,y2)=P[a],P[b]
        d=geo.sea_km(a,b)
        far = a=="Piraeus" and b in ("Santorini","Crete")
        col = ACCENT if not far else SOFT
        dash = "" if not far else ' stroke-dasharray="4 4"'
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{col}" stroke-width="{2.0 if not far else 1.3}"{dash} opacity="0.85"/>')
    # nodes
    for n in nodes:
        x,y=P[n]
        hub = n in ("Piraeus","Paros")
        r = 5.5 if hub else 4
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{DEEP if hub else ACCENT}" '
                 f'stroke="{PAPER}" stroke-width="1.5"/>')
        lx,ly,an=box.place(x+8,y+3,n,11,"start")
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="11" fill="{INK}" '
                 f'text-anchor="{an}" font-family="{DISP}" font-weight="600">{n}</text>')
    # a few key edge times, placed to avoid nodes
    times=[("Paros","Naxos","20 km · frequent"),("Ios","Santorini","short hop"),
           ("Piraeus","Santorini","237 km · fast 5h/slow 8h"),("Piraeus","Crete","320 km · fly 1h")]
    for a,b,lab in times:
        (x1,y1),(x2,y2)=P[a],P[b]; mx,my=(x1+x2)/2,(y1+y2)/2
        lx,ly,an=box.place(mx,my,lab,8.5,"middle")
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="8.5" fill="{MUTED}" '
                 f'text-anchor="{an}" font-family="{MONO}">{_esc(lab)}</text>')
    # legend
    s.append(f'<text x="{pad}" y="{H-16}" font-size="8" fill="{SOFT}" font-family="{MONO}" letter-spacing="0.14em">SOLID · SHORT RELIABLE HOP    DASHED · LONG CROSSING, FLY OR COMMIT A DAY</text>')
    s.append(f'<text x="{pad}" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.2em">THE CYCLADES TRUNK — NODES TO REAL SCALE</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — FLY vs FERRY: the same origin (Athens), the time cost of each
# island by ferry vs the 45-min flight. Draws WHY Santorini is flown.
# =====================================================================
def fly_vs_ferry():
    W,H=660,300; padL,padR,padT,padB=150,40,44,44
    rows=[("Mykonos",3.0,5.0,40),("Paros",3.0,4.0,None),("Naxos",4.0,5.0,None),
          ("Santorini",5.0,8.0,45),("Crete",None,9.0,60)]
    maxh=9.0
    plot_w=W-padL-padR
    def bx(h): return padL+(h/maxh)*plot_w
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # x grid (hours)
    for hh in range(0,10,2):
        x=bx(hh)
        s.append(f'<line x1="{x:.1f}" y1="{padT}" x2="{x:.1f}" y2="{H-padB}" stroke="{LINE_SOFT}" stroke-width="0.5"/>')
        s.append(f'<text x="{x:.1f}" y="{H-padB+16}" font-size="8" fill="{SOFT}" text-anchor="middle" font-family="{MONO}">{hh}h</text>')
    rh=(H-padT-padB)/len(rows)
    for i,(name,fast,slow,fly) in enumerate(rows):
        y=padT+i*rh+rh/2
        s.append(f'<text x="{padL-12}" y="{y+3:.1f}" font-size="12" fill="{INK}" text-anchor="end" font-family="{DISP}" font-weight="600">{name}</text>')
        # slow ferry bar (background), fast ferry bar (fore)
        if slow:
            s.append(f'<rect x="{padL}" y="{y-7:.1f}" width="{bx(slow)-padL:.1f}" height="14" fill="{STONE}" stroke="{LINE}" stroke-width="0.5"/>')
        if fast:
            s.append(f'<rect x="{padL}" y="{y-7:.1f}" width="{bx(fast)-padL:.1f}" height="14" fill="{WATER}" stroke="{ACCENT}" stroke-width="0.6"/>')
        # flight marker
        if fly:
            fx=bx(fly/60)
            s.append(f'<circle cx="{fx:.1f}" cy="{y:.1f}" r="4.5" fill="{ACCENT}" stroke="{PAPER}" stroke-width="1.5"/>')
            s.append(f'<text x="{fx+8:.1f}" y="{y+3:.1f}" font-size="8" fill="{DEEP}" font-family="{MONO}">{fly}m fly</text>')
        # slow-ferry endcap label
        if slow:
            s.append(f'<text x="{bx(slow)+6:.1f}" y="{y+3:.1f}" font-size="8" fill="{MUTED}" font-family="{MONO}">{slow:g}h slow</text>')
    s.append(f'<text x="{padL}" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.2em">HOURS FROM ATHENS — DOT = FLIGHT, BAR = FERRY</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — THE MELTEMI ASYMMETRY: the wind as the ground; the fast catamaran
# (cancellable) vs the crossing you already took (banked). The cover's engine.
# =====================================================================
def meltemi(as_cover=False, W=660, H=330):
    padT=44; padB=44; padL=54; padR=54
    col_inset=40            # how far the two route columns sit inside the frame
    row0=padT+34            # first node y
    if as_cover:
        padT=54; padB=54; col_inset=118   # pull columns well inside; fit the frame
        row0=padT+30
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    if not as_cover:
        s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # meltemi streamlines — N->S sweep (the wind hits north coasts). Behind everything.
    import random; random.seed(7)
    n_lines=13
    for i in range(n_lines):
        x0=padL+ (i/(n_lines-1))*(W-padL-padR)
        pts=[]
        y=padT-6
        while y<H-padB+6:
            drift=14*math.sin((y/46.0)+(i*0.5))
            pts.append(f"{x0+drift:.1f},{y:.1f}")
            y+=13
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WIND}" '
                 f'stroke-width="0.8" opacity="0.5"/>')
        # arrowhead at bottom
        s.append(f'<circle cx="{x0+14*math.sin((( H-padB)/46.0)+(i*0.5)):.1f}" cy="{H-padB:.1f}" r="1.4" fill="{WIND}" opacity="0.55"/>')
    # the two routes: same trip, two orders
    # left: end-on-Santorini (bad) — last leg is a fast catamaran the wind can kill
    # right: end-on-a-hub (good) — last leg already taken / short reliable hop
    def node(x,y,label,fill,r=5):
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{PAPER}" stroke-width="1.5"/>')
        s.append(f'<text x="{x}" y="{y-11}" font-size="9.5" fill="{INK}" text-anchor="middle" font-family="{DISP}" font-weight="600">{label}</text>')
    colgap=(W)/2
    rowgap = 74 if not as_cover else 78
    ys=[row0, row0+rowgap, row0+2*rowgap]
    # --- LEFT COLUMN: the gamble ---
    lx=padL+col_inset
    node(lx,ys[0],"Naxos",DEEP)
    node(lx,ys[1],"Mykonos",DEEP)
    node(lx,ys[2],"Santorini",ACCENT,6)
    for a,b in [(0,1),(1,2)]:
        last=(b==2)
        s.append(f'<line x1="{lx}" y1="{ys[a]}" x2="{lx}" y2="{ys[b]}" stroke="{ACCENT if not last else SOFT}" '
                 f'stroke-width="{2 if not last else 1.6}" {"stroke-dasharray=\"5 4\"" if last else ""}/>')
    # the fatal last leg to the airport
    apy=ys[2]+56
    s.append(f'<line x1="{lx}" y1="{ys[2]}" x2="{lx}" y2="{apy}" stroke="{SOFT}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    s.append(f'<text x="{lx}" y="{apy+16}" font-size="8" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">FAST CATAMARAN → FLIGHT HOME</text>')
    s.append(f'<text x="{lx}" y="{apy+28}" font-size="8" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}" font-weight="600">CANCELS IN HIGH WIND</text>')
    s.append(f'<text x="{lx}" y="{padT+8}" font-size="8" fill="{SOFT}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.14em">END ON SANTORINI</text>')
    # --- RIGHT COLUMN: the bank ---
    rx=W-padR-col_inset
    node(rx,ys[0],"Santorini",ACCENT,6)
    node(rx,ys[1],"Naxos",DEEP)
    node(rx,ys[2],"Athens",DEEP)
    for a,b in [(0,1),(1,2)]:
        last=(b==2)
        s.append(f'<line x1="{rx}" y1="{ys[a]}" x2="{rx}" y2="{ys[b]}" stroke="{ACCENT}" stroke-width="2"/>')
    s.append(f'<text x="{rx}" y="{ys[2]+20}" font-size="8" fill="{DEEP}" text-anchor="middle" font-family="{MONO}">BUFFER NIGHT · FLIGHT HOME</text>')
    s.append(f'<text x="{rx}" y="{ys[2]+32}" font-size="8" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}" font-weight="600">DEADLINE ALREADY SAFE</text>')
    s.append(f'<text x="{rx}" y="{padT+8}" font-size="8" fill="{SOFT}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.14em">END NEAR ATHENS</text>')
    if not as_cover:
        s.append(f'<text x="{W/2}" y="{H-14}" font-size="8" fill="{SOFT}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.12em">THE SAME FIVE ISLANDS · TWO ORDERS · ONE COSTS THE FLIGHT HOME</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — THE PACE LADDER: nights vs islands. The corpus rule drawn: 3 nights
# floor, 2-3 islands ceiling in 10 days. Shows the over-hopping trap.
# =====================================================================
def pace_ladder():
    W,H=660,270; padL,padR,padT,padB=48,48,44,40
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # x = days (0..10), each island block >=3 nights
    plot_w=W-padL-padR
    def dx(d): return padL+(d/10)*plot_w
    for d in range(0,11,2):
        x=dx(d)
        s.append(f'<line x1="{x:.1f}" y1="{padT}" x2="{x:.1f}" y2="{H-padB}" stroke="{LINE_SOFT}" stroke-width="0.5"/>')
        s.append(f'<text x="{x:.1f}" y="{H-padB+16}" font-size="8" fill="{SOFT}" text-anchor="middle" font-family="{MONO}">D{d}</text>')
    rows=[
        ("WORKS · 2 islands", [(0,4,"Naxos",WATER),(4,4,"Santorini",WATER)], 2, True),
        ("WORKS · 3 islands", [(0,3,"Paros",WATER),(3,3,"Naxos",WATER),(6,4,"Santorini",WATER)], 3, True),
        ("THE TRAP · 5 islands", [(0,2,"Mykonos",STONE),(2,2,"Paros",STONE),(4,2,"Naxos",STONE),(6,2,"Ios",STONE),(8,2,"Santorini",STONE)], 5, False),
    ]
    rh=(H-padT-padB)/len(rows)
    for i,(label,blocks,ni,ok) in enumerate(rows):
        y=padT+i*rh+8
        for (d0,dur,nm,fill) in blocks:
            x0=dx(d0); x1=dx(d0+dur)
            stroke=ACCENT if ok else SOFT
            s.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{x1-x0:.1f}" height="{rh-22:.1f}" '
                     f'fill="{fill}" stroke="{stroke}" stroke-width="0.7"/>')
            s.append(f'<text x="{(x0+x1)/2:.1f}" y="{y+(rh-22)/2+3:.1f}" font-size="8.5" fill="{DEEP if ok else MUTED}" '
                     f'text-anchor="middle" font-family="{DISP}" font-weight="600">{nm}</text>')
        s.append(f'<text x="{padL}" y="{y-3:.1f}" font-size="8" fill="{ACCENT if ok else SOFT}" font-family="{MONO}" letter-spacing="0.14em">{label}</text>')
    s.append(f'<text x="{padL}" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.2em">TEN DAYS · EACH BLOCK IS ONE ISLAND STAY (NIGHTS)</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — THE SEASON STRIP: month band; crowd & wind & openness. The season
# decision, seen. From when-to-go + meltemi facts.
# =====================================================================
def season_strip():
    W,H=660,210; padL,padR,padT,padB=48,20,42,36
    months=["APR","MAY","JUN","JUL","AUG","SEP","OCT"]
    # qualitative bands the corpus states: shoulder = May,Jun,Sep,Oct; peak+wind Jul,Aug
    crowd=[0.35,0.5,0.72,0.95,1.0,0.62,0.4]
    wind =[0.2,0.28,0.5,0.9,0.95,0.5,0.3]
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    cw=(W-padL-padR)/len(months)
    base=H-padB; top=padT+6; span=base-top
    # crowd bars
    for i,m in enumerate(months):
        x=padL+i*cw
        ch=crowd[i]*span
        peak = m in ("JUL","AUG")
        s.append(f'<rect x="{x+6:.1f}" y="{base-ch:.1f}" width="{cw-12:.1f}" height="{ch:.1f}" '
                 f'fill="{STONE if peak else WATER}" stroke="{ACCENT if not peak else SOFT}" stroke-width="0.6"/>')
        s.append(f'<text x="{x+cw/2:.1f}" y="{base+15:.1f}" font-size="9" fill="{INK if not peak else MUTED}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.1em">{m}</text>')
    # wind line
    pts=[]
    for i in range(len(months)):
        x=padL+i*cw+cw/2; y=base-wind[i]*span
        pts.append(f"{x:.1f},{y:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{DEEP}" stroke-width="1.6"/>')
    for i in range(len(months)):
        x=padL+i*cw+cw/2; y=base-wind[i]*span
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.4" fill="{DEEP}"/>')
    # shoulder markers
    s.append(f'<text x="{padL}" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">BARS · CROWD    LINE · MELTEMI WIND    SHOULDER = MAY JUN SEP OCT</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — THE ARRIVAL FLOW (Day Zero order-of-ops): plane -> Piraeus vs fly
# -> the decision tree of the first hours.
# =====================================================================
def arrival_flow():
    W,H=660,250
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    def box(x,y,w,h,label,sub="",fill=WATER,stroke=ACCENT):
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>')
        s.append(f'<text x="{x+w/2}" y="{y+h/2-(2 if sub else -3)}" font-size="10" fill="{DEEP}" text-anchor="middle" font-family="{DISP}" font-weight="600">{label}</text>')
        if sub:
            s.append(f'<text x="{x+w/2}" y="{y+h/2+12}" font-size="7.5" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{sub}</text>')
    def arrow(x1,y1,x2,y2,lab=""):
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ACCENT}" stroke-width="1.3"/>')
        s.append(f'<circle cx="{x2}" cy="{y2}" r="2" fill="{ACCENT}"/>')
        if lab: s.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2-4}" font-size="7.5" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{lab}</text>')
    box(250,20,160,40,"LAND AT ATH","transatlantic, ~morning",ZONE,GILT)
    arrow(330,60,330,88)
    box(250,88,160,36,"WHICH ISLAND FIRST?","the fork",fill=PAPER,stroke=DEEP)
    # left: near island by ferry
    arrow(250,106,150,150,"Cyclades")
    box(70,150,160,40,"FERRY FROM PIRAEUS","20-30m metro to port")
    # right: far island by air
    arrow(410,106,510,150,"Santorini/Crete")
    box(430,150,160,40,"CONNECT A FLIGHT","45m, same-day risk")
    arrow(150,190,300,222)
    arrow(510,190,360,222)
    box(250,222,160,26,"BUFFER THE RETURN","never same-day as the flight home",STONE,ACCENT)
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">DAY ZERO</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — WHERE TO STAY ON SANTORINI: the caldera-price gradient. A locator
# that argues the money decision (caldera view = premium).
# =====================================================================
def santorini_stay():
    W,H=660,260
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # stylised crescent (the caldera rim) computed as an arc; villages along it
    cx,cy,r=W*0.42,H*0.62,150
    # rim arc
    s.append(f'<path d="M {cx-140} {cy-40} A {r} {r} 0 0 1 {cx+120} {cy-96}" fill="none" stroke="{DEEP}" stroke-width="2"/>')
    s.append(f'<path d="M {cx-140} {cy-40} A {r} {r} 0 0 1 {cx+120} {cy-96}" fill="none" stroke="{WATER}" stroke-width="8" opacity="0.35"/>')
    box=_Boxes()
    # villages: (x,y, name, tier)  tier drives colour: caldera premium -> value
    villages=[("Oia",cx+120,cy-96,"CALDERA · TOP $$$"),
              ("Imerovigli",cx+40,cy-118,"CALDERA · QUIET $$$"),
              ("Fira",cx-40,cy-92,"CALDERA · HUB $$"),
              ("Firostefani",cx,cy-108,"CALDERA $$"),
              ("Pyrgos",cx-70,cy+20,"INLAND · VALUE $"),
              ("Kamari",cx+150,cy+40,"BEACH · VALUE $")]
    for nm,x,y,tier in villages:
        prem = "$$$" in tier
        s.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{ACCENT if prem else DEEP}" stroke="{PAPER}" stroke-width="1.5"/>')
        lx,ly,an=box.place(x+8,y+3,nm,11,"start")
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="11" fill="{INK}" text-anchor="{an}" font-family="{DISP}" font-weight="600">{nm}</text>')
        tx,ty,tan=box.place(x+8,y+15,tier,7.5,"start")
        s.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="7.5" fill="{ACCENT if prem else MUTED}" text-anchor="{tan}" font-family="{MONO}">{tier}</text>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">SANTORINI — THE PRICE IS THE VIEW, NOT THE ISLAND</text>')
    s.append(f'<text x="30" y="{H-14}" font-size="8" fill="{SOFT}" font-family="{MONO}" letter-spacing="0.12em">RIM VILLAGES CARRY THE CALDERA PREMIUM · INLAND AND BEACH RETURN THE SAME ISLAND FOR LESS</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# THE COVER — the sequence, with the cost of getting it wrong shown.
# Argues the thesis: a wind governs a trade you can only make in one order.
# =====================================================================
def cover():
    W,H=816,1056
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{DISP}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # full-page faint meltemi streamlines as the ground of the whole cover (behind all)
    import math as _m
    n_bg=26
    for i in range(n_bg):
        x0=40+(i/(n_bg-1))*(W-80)
        pts=[]; y=130
        while y<H-90:
            drift=18*_m.sin((y/70.0)+(i*0.4))
            pts.append(f"{x0+drift:.1f},{y:.1f}")
            y+=16
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{WIND}" stroke-width="0.7" opacity="0.35"/>')
    # top rule + imprint
    s.append(f'<text x="{W/2}" y="86" font-size="13" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.34em">MELTEMI PRESS · A DECISION MANUAL</text>')
    s.append(f'<line x1="120" y1="112" x2="{W-120}" y2="112" stroke="{GILT}" stroke-width="1"/>')
    # THE DEVICE — the meltemi asymmetry, large, as the ground of the page
    # <g transform> renders reliably in this Chromium; nested <svg viewBox> meet-scaling
    # misplaced the device here. Device is generated at 1:1, so a pure translate is exact.
    dev = meltemi(as_cover=True, W=W-140, H=380)
    s.append(f'<g transform="translate(70,150)">{_strip_svg(dev)}</g>')
    # a hairline framing the device
    s.append(f'<rect x="70" y="150" width="{W-140}" height="380" fill="none" stroke="{LINE}" stroke-width="0.8"/>')
    # TITLE
    s.append(f'<text x="{W/2}" y="708" font-size="106" fill="{INK}" text-anchor="middle" font-family="{DISP}" font-weight="600" letter-spacing="-0.01em">Greece,</text>')
    s.append(f'<text x="{W/2}" y="808" font-size="106" fill="{ACCENT}" text-anchor="middle" font-family="{DISP}" font-weight="600" letter-spacing="-0.01em">in Order.</text>')
    # SUBTITLE — leads on experience/pacing (the corpus's dominant edge), not money
    s.append(f'<text x="{W/2}" y="858" font-size="21" fill="{DEEP}" text-anchor="middle" font-family="{DISP}" font-weight="500" font-style="italic">Which islands are worth your week — and the one order that</text>')
    s.append(f'<text x="{W/2}" y="886" font-size="21" fill="{DEEP}" text-anchor="middle" font-family="{DISP}" font-weight="500" font-style="italic">keeps a cancelled ferry from costing you the flight home.</text>')
    # a filled base band carrying the imprint (adds deliberate ink weight, closes the page)
    s.append(f'<rect x="0" y="916" width="{W}" height="140" fill="{DEEP}"/>')
    s.append(f'<text x="{W/2}" y="972" font-size="12" fill="{PAPER}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.24em">FOR FIRST-TIME AMERICAN VISITORS</text>')
    s.append(f'<text x="{W/2}" y="1000" font-size="10" fill="{WIND}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.2em">THE BOOK · WHAT LASTS      +      THE FIELD SHEET · WHAT MOVES</text>')
    s.append(f'<line x1="120" y1="1022" x2="{W-120}" y2="1022" stroke="{GILT}" stroke-width="0.8"/>')
    s.append(f'<text x="{W/2}" y="1042" font-size="9" fill="{WIND}" text-anchor="middle" font-family="{MONO}" letter-spacing="0.3em">MELTEMI PRESS · EDITION 2026</text>')
    s.append("</svg>")
    return "".join(s)

def _strip_svg(svg):
    """Return inner content of an <svg ...>...</svg> for nesting."""
    i=svg.index(">")+1
    j=svg.rindex("</svg>")
    return svg[i:j]

# =====================================================================
# FIG — CRETE SCALE: the island against a Cyclades cluster, to show it is
# not a hop. Draws the "different mindset" fact from real proportions.
# =====================================================================
def crete_scale():
    W,H=660,270
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # Crete ~160 mi E-W; draw as a long bar with the two-hour-drive segment marked
    cx0=60; cy=150; bar_w=W-120
    # scale: full bar = 160 mi
    s.append(f'<rect x="{cx0}" y="{cy-16}" width="{bar_w}" height="32" rx="4" fill="{STONE}" stroke="{DEEP}" stroke-width="1.2"/>')
    s.append(f'<text x="{cx0+bar_w/2}" y="{cy+5}" font-size="13" fill="{DEEP}" text-anchor="middle" font-family="{DISP}" font-weight="600">CRETE — ~160 MILES END TO END</text>')
    # Chania -> Heraklion ~ 2h drive segment (about 90 mi of the 160)
    seg_w=bar_w*(90/160)
    s.append(f'<line x1="{cx0}" y1="{cy-30}" x2="{cx0+seg_w}" y2="{cy-30}" stroke="{ACCENT}" stroke-width="2.5"/>')
    s.append(f'<text x="{cx0+seg_w/2}" y="{cy-38}" font-size="8.5" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}">CHANIA → HERAKLION · ~2 h DRIVE</text>')
    s.append(f'<circle cx="{cx0}" cy="{cy-30}" r="3" fill="{ACCENT}"/><circle cx="{cx0+seg_w}" cy="{cy-30}" r="3" fill="{ACCENT}"/>')
    # a Cyclades cluster to scale beside/below: Paros-Naxos 20km ~ 12mi
    clus_y=cy+62; clus_w=bar_w*(20/160/1.6)  # 20km in mi over 160mi bar
    cxx=cx0
    s.append(f'<text x="{cx0}" y="{clus_y-14}" font-size="8" fill="{SOFT}" font-family="{MONO}" letter-spacing="0.14em">TO THE SAME SCALE · A WHOLE CYCLADES HOP:</text>')
    s.append(f'<circle cx="{cxx}" cy="{clus_y}" r="4" fill="{DEEP}"/>')
    s.append(f'<circle cx="{cxx+clus_w}" cy="{clus_y}" r="4" fill="{DEEP}"/>')
    s.append(f'<line x1="{cxx}" y1="{clus_y}" x2="{cxx+clus_w}" y2="{clus_y}" stroke="{ACCENT}" stroke-width="2"/>')
    s.append(f'<text x="{cxx-6}" y="{clus_y+4}" font-size="9" fill="{INK}" text-anchor="end" font-family="{DISP}" font-weight="600">Paros</text>')
    s.append(f'<text x="{cxx+clus_w+6}" y="{clus_y+4}" font-size="9" fill="{INK}" font-family="{DISP}" font-weight="600">Naxos</text>')
    s.append(f'<text x="{cxx+clus_w/2}" y="{clus_y+18}" font-size="8" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">20 km</text>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">CRETE IS NOT A CYCLADE WITH MORE SAND — IT IS A REGION</text>')
    s.append("</svg>")
    return "".join(s)

# =====================================================================
# FIG — THE WEEK SHAPE: the operational skeleton of a first week, with the
# buffer night marked. The Plan chapter's argument, drawn.
# =====================================================================
def week_shape():
    W,H=660,240
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    padL=40; padR=40; y=120
    plot=W-padL-padR
    # 10-day trip as a ribbon: Athens(3) | Island A(3) | Island B(3) | buffer(1)
    segs=[("ATHENS",3,ZONE,GILT),("ISLAND A",3,WATER,ACCENT),("ISLAND B",3,WATER,ACCENT),("BUFFER",1,STONE,DEEP)]
    total=sum(d for _,d,_,_ in segs)
    x=padL
    for name,d,fill,stroke in segs:
        w=plot*d/total
        s.append(f'<rect x="{x:.1f}" y="{y-26}" width="{w:.1f}" height="52" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        s.append(f'<text x="{x+w/2:.1f}" y="{y-2:.1f}" font-size="10.5" fill="{DEEP}" text-anchor="middle" font-family="{DISP}" font-weight="600">{name}</text>')
        s.append(f'<text x="{x+w/2:.1f}" y="{y+14:.1f}" font-size="8" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{d} {"night" if d==1 else "nights"}</text>')
        x+=w
    # arrows for the fragile transitions
    s.append(f'<text x="{padL}" y="{y-44}" font-size="8" fill="{SOFT}" font-family="{MONO}" letter-spacing="0.14em">FLY THE LONG LEG EARLY ·································· END NEAR ATHENS</text>')
    # the buffer callout
    bx=padL+plot*(9/total)+plot*(1/total)/2
    s.append(f'<line x1="{bx:.1f}" y1="{y+26}" x2="{bx:.1f}" y2="{y+52}" stroke="{ACCENT}" stroke-width="1"/>')
    s.append(f'<text x="{bx:.1f}" y="{y+66}" font-size="8" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}">THE NIGHT THAT SAVES THE FLIGHT</text>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">TEN DAYS · THE SHAPE, NOT A SCRIPT</text>')
    s.append("</svg>")
    return "".join(s)

def fail_cost():
    W,H=660,270
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    tiers=[
      ("COSTS THE TRIP OR A DAY","end on Santorini \u00b7 no buffer \u00b7 same-day dash off the flight",ACCENT,WATER,0.0),
      ("COSTS REAL MONEY","caldera-view room \u00b7 the USD prompt \u00b7 fast fare on a windy leg",DEEP,STONE,0.16),
      ("COSTS THE EXPERIENCE","too many islands \u00b7 peak season \u00b7 Crete as a hop \u00b7 the sunset scrum",MUTED,ZONE,0.32),
    ]
    padL=50; padR=50; top=54; th=54; gap=10
    for i,(label,ex,stroke,fill,inset) in enumerate(tiers):
        y=top+i*(th+gap)
        x0=padL+inset*(W-padL-padR)/2
        x1=W-padR-inset*(W-padL-padR)/2
        s.append(f'<rect x="{x0:.1f}" y="{y}" width="{x1-x0:.1f}" height="{th}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        s.append(f'<text x="{(x0+x1)/2:.1f}" y="{y+22}" font-size="10.5" fill="{stroke}" text-anchor="middle" font-family="{DISP}" font-weight="600">{label}</text>')
        s.append(f'<text x="{(x0+x1)/2:.1f}" y="{y+40}" font-size="8" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{ex}</text>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">EVERY FIRST-TIMER MISTAKE, SORTED BY WHAT IT COSTS</text>')
    s.append("</svg>")
    return "".join(s)

def athens_days():
    W,H=660,210
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">THE ATHENS ON-RAMP · TWO OR THREE DELIBERATE DAYS</text>')
    days=[("DAY 1","Acropolis at opening \u00b7 Agora \u00b7 the old quarter",ZONE,GILT),
          ("DAY 2","Acropolis Museum \u00b7 combo-ticket sites \u00b7 dinner",STONE,DEEP),
          ("DAY 3","Day trip \u2014 Sounion sunset or Delphi",WATER,ACCENT)]
    padL=40; padR=40; y=90; plot=W-padL-padR; bw=plot/3-10
    for i,(d,txt,fill,stroke) in enumerate(days):
        x=padL+i*(plot/3)
        s.append(f'<rect x="{x:.1f}" y="{y-24}" width="{bw:.1f}" height="70" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{y-4:.1f}" font-size="11" fill="{stroke}" text-anchor="middle" font-family="{DISP}" font-weight="600">{d}</text>')
        # wrap txt into <=2 lines
        words=txt.split(" "); mid=len(words)//2+1
        l1=" ".join(words[:mid]); l2=" ".join(words[mid:])
        s.append(f'<text x="{x+bw/2:.1f}" y="{y+16:.1f}" font-size="7.5" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{l1}</text>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{y+28:.1f}" font-size="7.5" fill="{MUTED}" text-anchor="middle" font-family="{MONO}">{l2}</text>')
    s.append(f'<text x="{W/2}" y="{y+62}" font-size="8" fill="{ACCENT}" text-anchor="middle" font-family="{MONO}">BUY THE COMBO TICKET AT A QUIETER SITE \u2014 SKIP THE ACROPOLIS LINE</text>')
    s.append("</svg>")
    return "".join(s)

def sunset_options():
    W,H=660,220
    s=[f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    s.append(f'<text x="30" y="26" font-size="8" fill="{ACCENT}" font-family="{MONO}" letter-spacing="0.18em">WATCHING THE CALDERA SUNSET \u2014 THREE PLANS AND ONE MISTAKE</text>')
    rows=[("OIA, AN HOUR EARLY","the postcard framing, earned with patience","ok",GILT,ZONE),
          ("A QUIET RIM PERCH","Imerovigli or Firostefani \u2014 room to breathe","good",ACCENT,WATER),
          ("A CATAMARAN BELOW","the caldera from the water \u2014 book ahead","good",DEEP,STONE),
          ("OIA AT 8PM, NO PLAN","the scrum, and the shuffle home in the dark","bad",SOFT,PAPER)]
    y0=48; rh=38
    for i,(label,note,tag,stroke,fill) in enumerate(rows):
        y=y0+i*rh
        s.append(f'<rect x="40" y="{y}" width="{W-80}" height="{rh-8}" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        s.append(f'<text x="52" y="{y+19}" font-size="10" fill="{stroke}" font-family="{DISP}" font-weight="600">{label}</text>')
        s.append(f'<text x="230" y="{y+19}" font-size="8" fill="{MUTED}" font-family="{MONO}">{note}</text>')
        glyph="\u2713" if tag in ("ok","good") else "\u2717"
        gc=ACCENT if tag=="good" else (GILT if tag=="ok" else SOFT)
        s.append(f'<text x="{W-56}" y="{y+19}" font-size="12" fill="{gc}" text-anchor="middle" font-family="{DISP}" font-weight="600">{glyph}</text>')
    s.append("</svg>")
    return "".join(s)

FIGURES = {
    "route": route_graph, "flyferry": fly_vs_ferry, "meltemi": lambda: meltemi(),
    "pace": pace_ladder, "season": season_strip, "arrival": arrival_flow,
    "santstay": santorini_stay, "crete": crete_scale, "week": week_shape,
    "failcost": fail_cost, "athens": athens_days, "sunset": sunset_options,
}

if __name__ == "__main__":
    import os
    os.makedirs("_figtest", exist_ok=True)
    for k,fn in FIGURES.items():
        open(f"_figtest/{k}.svg","w").write(fn())
    open("_figtest/cover.svg","w").write(cover())
    print("wrote", len(FIGURES)+1, "figures to _figtest/")
