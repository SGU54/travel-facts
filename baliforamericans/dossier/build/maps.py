# maps.py — every vector figure, drawn from REAL numbers and REAL coordinates.
# Geography, road distances (the corpus's own, in miles) and published hours are
# public facts; drawing our own figure from them is fine (SKILL non-negotiable 6).
# No stock art, no tiles. The corpus prints NO drive times, so neither does any
# figure here: distance is drawn as miles, time only as the corpus states it.
#
# viewBox note (bug log #8): the body column is 652px (816 − 2×82), so figures
# are authored at 652 wide and scale to width:100%. Essential labels ≥ 9px.
# ─────────────────────────────────────────────────────────────────────────────
import math

C = {
 "ink":"#1A1423", "accent":"#B3155E", "jade":"#262868", "gilt":"#D99412",
 "muted":"#564E63", "soft":"#7E7689", "line":"#E6E2EA", "panel":"#ECE9F1",
 "deep":"#8A0F47", "paper":"#F5F4F8", "water":"#D6E0F2", "edge":"#DDD8E4",
}
W = 652
MONO = "'Space Mono',monospace"
DISP = "'Bricolage Grotesque',sans-serif"
BODY = "'Hanken Grotesk',sans-serif"

# ── real coordinates (lat, lon) ──────────────────────────────────────────────
GEO = {
 "Airport":      (-8.7482, 115.1672),
 "Kuta":         (-8.7205, 115.1693),
 "Legian":       (-8.7050, 115.1680),
 "Seminyak":     (-8.6900, 115.1620),
 "Canggu":       (-8.6480, 115.1380),
 "Tanah Lot":    (-8.6212, 115.0868),
 "Jimbaran":     (-8.7900, 115.1630),
 "Uluwatu":      (-8.8291, 115.0849),
 "Balangan":     (-8.7920, 115.1230),
 "Nusa Dua":     (-8.8000, 115.2300),
 "Sanur":        (-8.6880, 115.2620),
 "Denpasar":     (-8.6705, 115.2126),
 "Ubud":         (-8.5069, 115.2625),
 "Tegallalang":  (-8.4312, 115.2790),
 "Tirta Empul":  (-8.4155, 115.3153),
 "Kintamani":    (-8.2740, 115.3620),
 "Mt Batur":     (-8.2420, 115.3750),
 "Toya Bungkah": (-8.2390, 115.4010),
 "Sidemen":      (-8.4700, 115.4400),
 "Besakih":      (-8.3740, 115.4510),
 "Mt Agung":     (-8.3430, 115.5080),
 "Padang Bai":   (-8.5300, 115.5080),
 "Candidasa":    (-8.5110, 115.5680),
 "Tirta Gangga": (-8.4120, 115.5870),
 "Lempuyang":    (-8.3910, 115.6310),
 "Amed":         (-8.3360, 115.6650),
 "Tulamben":     (-8.2740, 115.5930),
 "Munduk":       (-8.2650, 115.0680),
 "Ulun Danu":    (-8.2750, 115.1670),
 "Lovina":       (-8.1600, 115.0260),
 "Singaraja":    (-8.1120, 115.0880),
 "Lembongan":    (-8.6760, 115.4480),
 "Ceningan":     (-8.6950, 115.4560),
 "Toyapakeh":    (-8.6750, 115.4850),
 "Sampalan":     (-8.6700, 115.5300),
 "Kelingking":   (-8.7503, 115.4720),
 "Atuh":         (-8.7780, 115.6110),
 "Gili T":       (-8.3500, 116.0390),
 "Gili Air":     (-8.3600, 116.0800),
 "Bangsal":      (-8.3960, 116.0810),
 "Lombok airport": (-8.7573, 116.2767),
}

# the corpus's own road distances, in miles (bali-traffic-real-drive-times and the
# area guides). Stable facts; drive times are deliberately absent.
ROAD = {
 ("Airport","Kuta"):4, ("Airport","Seminyak"):7, ("Airport","Canggu"):12, ("Airport","Nusa Dua"):8,
 ("Airport","Sanur"):11, ("Airport","Uluwatu"):13, ("Airport","Ubud"):22, ("Airport","Sidemen"):35,
 ("Airport","Padang Bai"):35, ("Airport","Kintamani"):48, ("Airport","Munduk"):51, ("Airport","Amed"):61,
 ("Airport","Lovina"):62,
 ("Ubud","Tegallalang"):6, ("Ubud","Sanur"):14, ("Ubud","Canggu"):19, ("Ubud","Seminyak"):20, ("Ubud","Sidemen"):22,
 ("Ubud","Padang Bai"):23, ("Ubud","Kintamani"):27, ("Ubud","Besakih"):27, ("Ubud","Uluwatu"):34,
 ("Ubud","Munduk"):39, ("Ubud","Lempuyang"):45, ("Ubud","Amed"):49, ("Ubud","Nusa Dua"):26,
 ("Canggu","Uluwatu"):23, ("Canggu","Tanah Lot"):7, ("Seminyak","Uluwatu"):17, ("Seminyak","Kintamani"):45,
 ("Seminyak","Padang Bai"):32, ("Seminyak","Sanur"):12, ("Uluwatu","Jimbaran"):8, ("Uluwatu","Nusa Dua"):12,
 ("Sanur","Nusa Dua"):13, ("Sanur","Uluwatu"):21, ("Amed","Munduk"):93, ("Amed","Sanur"):51,
 ("Amed","Lempuyang"):9, ("Sidemen","Amed"):26, ("Munduk","Lovina"):12, ("Kuta","Seminyak"):4, ("Seminyak","Canggu"):7,
}
def road(a, b):
    return ROAD.get((a, b)) or ROAD.get((b, a))

def km(a, b):
    (la1, lo1), (la2, lo2) = GEO[a], GEO[b]
    R = 6371; p = math.pi / 180
    dlat = (la2 - la1) * p; dlon = (lo2 - lo1) * p
    h = math.sin(dlat/2)**2 + math.cos(la1*p) * math.cos(la2*p) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(h))

def miles(a, b): return km(a, b) * 0.621371

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _proj(pts, w, h, pad):
    lats = [p[0] for p in pts]; lons = [p[1] for p in pts]
    mlat = sum(lats) / len(lats)
    k = math.cos(math.radians(mlat))
    xs = [lon * k for lon in lons]
    x0, x1 = min(xs), max(xs); y0, y1 = min(lats), max(lats)
    dx = (x1 - x0) or 1e-6; dy = (y1 - y0) or 1e-6
    s = min((w - 2 * pad) / dx, (h - 2 * pad) / dy)
    cx = (x0 + x1) / 2; cy = (y0 + y1) / 2
    def f(lat, lon):
        return (w / 2 + (lon * k - cx) * s, h / 2 - (lat - cy) * s)
    return f

def _svg(h, extra=""):
    return [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}" {extra}>',
            f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>']

def _t(x, y, s, size=9, fill=None, anchor="start", fam=None, ls=None, extra=""):
    """Printed floor: nothing a reader must read goes below 9px on the 652-unit
    board (quality-standard.md). A long apparatus line wraps rather than shrinks."""
    fill = fill or C["ink"]
    size = max(size, 9)
    if ls is not None:
        try: ls = f"{min(float(ls), 0.8):.1f}"
        except ValueError: pass
    fam_a = f' font-family="{fam}"' if fam else ""
    ls_a = f' letter-spacing="{ls}"' if ls else ""
    est = len(s) * (size * (0.62 if not fam or 'Mono' in (fam or MONO) else 0.5) + (float(ls) if ls else 0))
    room = (W - x - 8) if anchor == "start" else (x - 8 if anchor == "end" else min(x, W - x) * 2 - 8)
    if est > room and " " in s and len(s) > 40:
        words = s.split(" "); half = len(s) // 2; acc = 0; cut = 0
        for i, w in enumerate(words):
            acc += len(w) + 1
            if acc >= half: cut = i + 1; break
        a, b = " ".join(words[:cut]), " ".join(words[cut:])
        return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{fam_a}{ls_a} {extra}>{a}</text>'
                f'<text x="{x:.1f}" y="{y + size + 4:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{fam_a}{ls_a} {extra}>{b}</text>')
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{fam_a}{ls_a} {extra}>{s}</text>')

MONTHS = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

# South Bali rainfall normals, inches per month, Denpasar station — the corpus's
# own figures (best-time-to-visit, shoulder-season, rainy-season). Where the
# corpus says "under 4" or "under 3" the bar is drawn at that ceiling.
RAIN = [14, 11, 9, 4, 3.9, 2.9, 1.0, 1.4, 2.5, 2.5, 5, 13]
# the three other calendars the corpus describes, scored 2 = yes / 1 = partly / 0 = no
CROWD = [2,1,0,0,0,0,2,2,0,0,0,2]          # northern summer peak + Christmas/New Year
WEST  = [0,0,0,1,2,2,2,2,2,1,0,0]          # west-facing surf coast clean (dry-season trade winds)
EAST  = [2,2,2,1,0,0,0,0,0,1,2,2]          # east-facing surf coast clean (wet-season NW wind)
SWELL = [0,0,0,0,0,1,2,2,1,0,0,0]          # the strait at its roughest, July–August (travel guides)

# ═════════════════════════════════════════════════════════════════════════════
def fig_island():
    """THE figure. The island from coordinates, the airport at its neck, and the
    corpus's road miles to every base drawn as rings. Short miles; the hours are
    the book."""
    h = 456
    keys = [k for k in GEO if k not in ("Gili T","Gili Air","Bangsal","Lombok airport","Atuh","Sampalan","Toyapakeh","Ceningan","Kelingking")]
    f = _proj([GEO[k] for k in keys], W, h, 46)
    p = _svg(h)
    AX, AY = f(*GEO["Airport"])
    # rings of road miles from the airport: drawn as straight-line scale from the
    # corpus's road figure, so the ring says "this many road miles", not a radius
    for mi, lab in ((15, "15"), (35, "35 ROAD MILES"), (60, "60")):
        # scale: pixels per road mile taken from Ubud (22 road miles) on the projected board
        ux, uy = f(*GEO["Ubud"]); ppm = math.hypot(ux - AX, uy - AY) / 22.0
        r = mi * ppm
        p.append(f'<circle cx="{AX:.1f}" cy="{AY:.1f}" r="{r:.1f}" fill="none" stroke="{C["line"]}" stroke-dasharray="3 4"/>')
        if mi == 60: pass
        elif mi == 35: p.append(_t(AX - r * 0.71 - 4, AY - r * 0.71 - 2, lab, 7.5, C["soft"], "end", ls="1"))
        else: p.append(_t(AX + r * 0.71 + 4, AY - r * 0.71 - 2, lab, 7.5, C["soft"], "start", ls="1"))
    groups = {
      "south": ["Kuta","Seminyak","Canggu","Uluwatu","Nusa Dua","Sanur","Jimbaran","Tanah Lot"],
      "centre": ["Ubud","Tegallalang","Kintamani","Sidemen","Besakih"],
      "far": ["Munduk","Lovina","Amed","Padang Bai","Tulamben","Lempuyang","Singaraja","Ulun Danu"],
    }
    col = {"south": C["accent"], "centre": C["jade"], "far": C["gilt"]}
    off = {"Kuta":(8,3,"start"), "Seminyak":(-8,3,"end"), "Canggu":(8,-4,"start"), "Uluwatu":(10,10,"start"),
           "Nusa Dua":(8,12,"start"), "Sanur":(8,3,"start"), "Jimbaran":(8,-6,"start"), "Tanah Lot":(-8,-6,"end"),
           "Ubud":(10,4,"start"), "Tegallalang":(10,-2,"start"), "Kintamani":(12,10,"start"), "Sidemen":(10,12,"start"),
           "Besakih":(-10,-4,"end"), "Munduk":(-8,-4,"end"), "Lovina":(8,-6,"start"), "Amed":(8,-2,"start"),
           "Padang Bai":(8,12,"start"), "Tulamben":(8,-4,"start"), "Lempuyang":(8,10,"start"), "Singaraja":(8,-4,"start"),
           "Ulun Danu":(8,12,"start")}
    for g, names in groups.items():
        for n in names:
            x, y = f(*GEO[n]); dx, dy, an = off[n]
            big = n in ("Ubud","Seminyak","Uluwatu","Sanur","Munduk","Amed","Canggu","Nusa Dua")
            p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if big else 3}" fill="{col[g]}" stroke="{C["paper"]}" stroke-width="1.2"/>')
            rm = road("Airport", n)
            lab = f"{n}" + (f" · {rm} mi" if rm else "")
            p.append(_t(x + dx, y + dy, _esc(lab), 9.5 if big else 8.5, C["ink"] if big else C["muted"], an, fam=BODY))
    # the two volcanoes as triangles
    for v in ("Mt Batur","Mt Agung"):
        x, y = f(*GEO[v])
        p.append(f'<path d="M{x:.1f},{y-7:.1f} l6,11 l-12,0 z" fill="none" stroke="{C["muted"]}" stroke-width="1.2"/>')
        p.append(_t(x + (12 if v == "Mt Agung" else -12), y + 2, v.upper(), 7.5, C["soft"], "start" if v == "Mt Agung" else "end", ls="1"))
    # the Nusa islands
    for n in ("Lembongan",):
        x, y = f(*GEO[n]); p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{C["water"]}" stroke="{C["jade"]}" stroke-width="1.4"/>')
        p.append(_t(x + 7, y + 3, "Nusa Lembongan · by boat", 8.5, C["muted"], fam=BODY))
    # the airport
    p.append(f'<rect x="{AX-6:.1f}" y="{AY-6:.1f}" width="12" height="12" fill="{C["ink"]}"/>')
    p.append(_t(AX - 10, AY + 4, "AIRPORT", 8.5, C["ink"], "end", ls="1"))
    p.append(_t(10, 14, "FROM COORDINATES · ROAD MILES FROM THE AIRPORT ARE THE SITE'S OWN · NO DRIVE TIMES", 7, C["soft"], ls="1"))
    ly = h - 12
    for i, (g, lab) in enumerate((("south","THE SOUTH · 4–13 MILES"),("centre","THE CENTRE · 22–48"),("far","THE FAR SIDE · 35–62"))):
        x = 10 + i * 200
        p.append(f'<circle cx="{x+5}" cy="{ly-3}" r="4.5" fill="{col[g]}"/>')
        p.append(_t(x + 15, ly, lab, 8, C["muted"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_nights():
    """Where the nights go. The corpus's own estimate: the first two days slow,
    the last partly spent leaving; a base needs three nights."""
    rows = [("5 nights", 5, "about three good days · one base"),
            ("7 nights", 7, "about five good days · two bases"),
            ("10 nights", 10, "about eight good days · three bases"),
            ("14 nights", 14, "about twelve good days · four bases")]
    rh, top = 46, 36
    h = top + rh * len(rows) + 64
    L, R = 196, 36
    unit = (W - L - R) / 14.0
    p = _svg(h)
    legend = [(C["gilt"], "SLOW: THE FIRST TWO DAYS"), (C["soft"], "PARTLY SPENT LEAVING"), (C["jade"], "GOOD DAYS")]
    x = L
    for colr, lab in legend:
        p.append(f'<rect x="{x}" y="10" width="11" height="10" fill="{colr}" opacity="0.9"/>')
        p.append(_t(x + 15, 19, lab, 8.5, C["muted"], ls="0.3"))
        x += 170
    for i, (lab, n, note) in enumerate(rows):
        y = top + i * rh
        p.append(_t(0, y + 14, lab, 10, C["ink"], fam=BODY))
        p.append(_t(0, y + 27, _esc(note), 7.5, C["soft"]))
        good = {5:3, 7:5, 10:8, 14:12}[n]
        segs = [(2, C["gilt"]), (good, C["jade"]), (n - 2 - good, C["soft"])]
        x0 = L
        for d, colr in segs:
            w = d * unit
            if w <= 0: continue
            p.append(f'<rect x="{x0:.1f}" y="{y}" width="{w:.1f}" height="22" fill="{colr}" opacity="0.9"/>')
            x0 += w
        p.append(_t(L + 2 * unit + good * unit - 6, y + 15, f'{good}', 9.5, C["paper"], "end"))
        # bases ticks: one per three nights
        bases = {5:1, 7:2, 10:3, 14:4}[n]
        for b in range(bases):
            bx = L + (b * n / bases) * unit
            p.append(f'<line x1="{bx:.1f}" y1="{y+24}" x2="{bx:.1f}" y2="{y+30}" stroke="{C["accent"]}" stroke-width="1.5"/>')
        p.append(_t(L + n * unit + 6, y + 15, f'{n}', 8.5, C["muted"]))
    p.append(_t(0, h - 24, "TICKS: THE BASES THOSE NIGHTS BUY, AT THREE NIGHTS EACH · AN ESTIMATE, NOT A MEASUREMENT", 7, C["soft"], ls="1"))
    p.append(_t(0, h - 10, "THE FLIGHT ADDS A CALENDAR DAY EACH WAY, AND A DAY AT HOME BEFORE WORK", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_order():
    """THE HOOK figure. Ten nights drawn twice: the order most people book, and
    the order the three pinned points impose. Same nights, different trip."""
    h = 312
    p = _svg(h)
    L, R = 24, 24
    span = W - L - R
    unit = span / 11.0
    def strip(y, title, blocks, pins, cost):
        p.append(_t(L, y - 8, title, 8.5, C["jade"], ls="1.5"))
        x = L
        for n, lab, colr in blocks:
            w = n * unit
            p.append(f'<rect x="{x:.1f}" y="{y}" width="{w-2:.1f}" height="26" fill="{colr}" opacity="0.88"/>')
            p.append(_t(x + w/2 - 1, y + 17, lab, 9, C["ink"] if colr == C["water"] else C["paper"], "middle", ls="0.5"))
            x += w
        for pi, (px, lab, colr) in enumerate(pins):
            xx = L + px * unit
            an = "end" if px > 7 else "start"
            p.append(f'<line x1="{xx:.1f}" y1="{y-2}" x2="{xx:.1f}" y2="{y+34}" stroke="{colr}" stroke-width="2"/>')
            p.append(_t(xx + (4 if an == "start" else -4), y + 44 + (12 if pi == 2 else 0), lab, 8, colr, an, ls="0.3"))
        p.append(_t(L, y + 74, cost, 9, C["deep"], fam=BODY))
    strip(36, "THE ORDER MOST PEOPLE BOOK · COAST FIRST, THE ISLAND LAST",
          [(4, "BEACH, SOUTH", C["accent"]), (3, "UBUD", C["jade"]), (3, "ISLAND", C["water"]), (1, "FLY", C["ink"])],
          [(0, "LAND, 16 H OUT OF STEP", C["gilt"]), (10, "BOAT BACK, SAME DAY AS THE FLIGHT", C["deep"])],
          "a dawn body clock spent on a beach · the one weather-dependent link sits against the flight home · 22 miles inland on the last morning")
    strip(172, "THE ORDER THE PINNED POINTS IMPOSE · INLAND FIRST, BOAT IN THE MIDDLE, THE AIRPORT'S COAST LAST",
          [(3, "UBUD", C["jade"]), (3, "ISLAND", C["water"]), (4, "BEACH, SOUTH", C["accent"]), (1, "FLY", C["ink"])],
          [(0, "DAWN WAKING AMONG THE TERRACES", C["gilt"]), (6, "BOAT BACK, FOUR DAYS OF SLACK", C["jade"]), (10, "7–11 MI TO THE AIRPORT", C["jade"])],
          "the same ten nights · a cancelled boat costs a beach day, not the flight · the last drive is the shortest on the island")
    p.append(_t(L, h - 10, "ONE BLOCK = ONE NIGHT · PINS: THE ARRIVAL HOUR, THE SEA, THE AIRPORT RUN", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_season():
    """Four calendars that do not agree: the rain, the crowd, the surf coast,
    the sea. Drawn from the corpus's own normals and its coast-by-season rule."""
    h = 378
    L, R, T = 150, 14, 40
    cw = (W - L - R) / 12.0
    p = _svg(h)
    for i, m in enumerate(MONTHS):
        x = L + i * cw
        p.append(f'<line x1="{x:.1f}" y1="{T-8}" x2="{x:.1f}" y2="{T+96+4*30}" stroke="{C["line"]}"/>')
        p.append(_t(x + cw/2, T - 14, m, 8, C["muted"], "middle"))
    p.append(f'<line x1="{W-R:.1f}" y1="{T-8}" x2="{W-R:.1f}" y2="{T+96+4*30}" stroke="{C["line"]}"/>')
    # rain bars
    mx = 14.0; bh = 80
    p.append(_t(L - 8, T + 12, "RAIN, INCHES", 8.5, C["ink"], "end", ls="1"))
    p.append(_t(L - 8, T + 24, "SOUTH BALI NORMALS", 7, C["soft"], "end", ls="1"))
    for i, v in enumerate(RAIN):
        x = L + i * cw; hh = bh * v / mx
        p.append(f'<rect x="{x+3:.1f}" y="{T + bh - hh:.1f}" width="{cw-6:.1f}" height="{hh:.1f}" fill="{C["jade"]}" opacity="0.75"/>')
        inside = hh > 60
        p.append(_t(x + cw/2, (T + bh - hh + 12) if inside else (T + bh - hh - 3), f'{v:g}', 8, C["paper"] if inside else C["muted"], "middle"))
    rows = [("CROWDED", CROWD, C["accent"]), ("WEST SURF CLEAN", WEST, C["jade"]), ("EAST SURF CLEAN", EAST, C["jade"]), ("STRAIT ROUGHEST", SWELL, C["deep"])]
    for ri, (name, vals, colr) in enumerate(rows):
        y = T + 96 + ri * 30
        p.append(_t(L - 8, y + 15, name, 8.5, C["ink"], "end", ls="1"))
        for i, v in enumerate(vals):
            if v == 0: continue
            x = L + i * cw
            p.append(f'<rect x="{x+1:.1f}" y="{y+3}" width="{cw-2:.1f}" height="20" fill="{colr}" opacity="{0.85 if v==2 else 0.4}" rx="1"/>')
    yb = T + 96 + 4 * 30 + 10
    spikes = [(0 + 12/31, 0 + 14/31, "GALUNGAN 13 JAN", C["gilt"]),
              (2 + 5/31, 2 + 15/31, "NYEPI 8 MAR + EID · 6–15 MAR", C["deep"]),
              (7 + 10/31, 7 + 12/31, "GALUNGAN 11 AUG", C["gilt"]),
              (11 + 23/31, 11 + 31/31, "CHRISTMAS", C["accent"])]
    for si, (s, e, lab, colr) in enumerate(spikes):
        x0 = L + s * cw; x1 = L + e * cw
        p.append(f'<rect x="{x0:.1f}" y="{yb}" width="{max(x1-x0,3):.1f}" height="10" fill="{colr}"/>')
        an = "end" if si == 3 else "start"
        p.append(_t(x1 if an == "end" else x0, yb + 22 + (12 if si == 1 else 0), lab, 7.5, colr, an, ls="0.3"))
    p.append(_t(L - 8, yb + 9, "2027 DATES", 7.5, C["deep"], "end", ls="1"))
    p.append(_t(L, h - 10, "RAIN: DENPASAR NORMALS · COASTS AND STRAIT AS THE SITE STATES THEM", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_stack():
    """The entry stack as a timeline: five separate systems, five separate
    windows, counted back from the hour you land."""
    h = 336
    p = _svg(h)
    L, R, T = 20, 20, 44
    span = W - L - R
    # x axis: months out → the hour you land (log-ish: 6 months, 3 months, 6 weeks, 3 days, landing)
    ticks = [(0.00, "6 MONTHS OUT"), (0.28, "FLIGHTS BOOKED"), (0.58, "6 WEEKS"), (0.84, "72 HOURS"), (1.0, "LANDING")]
    for fx, lab in ticks:
        x = L + fx * span
        p.append(f'<line x1="{x:.1f}" y1="{T-8}" x2="{x:.1f}" y2="{T+196}" stroke="{C["line"]}"/>')
        p.append(_t(x, T - 14, lab, 7.5, C["muted"], "end" if fx == 1 else ("start" if fx == 0 else "middle"), ls="0.5"))
    NL = 118  # name column
    items = [
      ("PASSPORT", 0.00, 0.12, "six months beyond landing, two blank visa pages; renew FIRST", C["deep"]),
      ("VISA (e-VOA)", 0.28, 0.58, "official site, after flights and the final passport; valid for entry 90 days", C["accent"]),
      ("LEVY", 0.30, 0.84, "Love Bali, by card; voucher per person, kept offline", C["jade"]),
      ("ARRIVAL CARD", 0.84, 0.97, "opens only in the last 72 h; the QR for immigration and customs", C["gilt"]),
      ("CUSTOMS", 0.97, 1.00, "medicine declared → red channel with the prescription", C["ink"]),
    ]
    for i, (name, a, b, note, colr) in enumerate(items):
        y = T + 8 + i * 38
        x0 = L + a * span; x1 = L + b * span
        p.append(f'<rect x="{x0:.1f}" y="{y}" width="{max(x1-x0,6):.1f}" height="10" fill="{colr}" opacity="0.85" rx="2"/>')
        p.append(_t(x0 if a < 0.6 else x1, y - 3, name, 8, colr, "start" if a < 0.6 else "end", ls="1.2"))
        p.append(_t(x0 if a < 0.6 else x1, y + 21, _esc(note), 8, C["muted"], "start" if a < 0.6 else "end", fam=BODY))
    y2 = T + 212
    p.append(_t(L, y2, "WHAT THE STACK SILENTLY FIXES", 8, C["jade"], ls="2"))
    p.append(_t(L, y2 + 18, "the outer edge of the trip: 30 days, counted not rounded · the onward ticket you must already hold · one passport for every form", 9, C["ink"], fam=BODY))
    p.append(_t(L, y2 + 46, "FIVE SYSTEMS, FIVE SITES · ONE CANNOT BE DONE EARLY, ONE CANNOT BE DONE LATE · FEES: SHEET", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_road():
    """Five ways to cover a Bali road, scored on the licence chain, the insurer
    and which journeys each one reaches."""
    h = 290
    p = _svg(h)
    cols = ["LEGAL, CAR LICENCE", "THE INSURER", "SHORT HOPS", "FULL DAY OUT", "DARK OR RAIN"]
    rows = [("Rent a scooter", ["no — unlicensed", "may refuse the bill", "yes", "tiring", "no"]),
            ("Pillion on Grab / Gojek bike", ["yes — not driving", "ordinary passenger", "yes", "no", "no"]),
            ("App car, Blue Bird taxi", ["yes", "ordinary passenger", "yes", "patchy outside the south", "yes"]),
            ("Car with a driver, by the day", ["yes", "ordinary passenger", "overkill", "YES — the default", "yes"]),
            ("Self-drive rental car", ["yes, with the IDP", "check the policy", "yes", "yes, and the blame after a crash", "no"])]
    L = 170; cw = (W - L) / 5; rh = 32; T = 44
    for j, c in enumerate(cols):
        p.append(_t(L + j * cw + cw/2, T - 22, c, 7, C["muted"], "middle", ls="0.8"))
    for i, (name, cells) in enumerate(rows):
        y = T + i * rh
        p.append(f'<rect x="0" y="{y-16}" width="{W}" height="{rh}" fill="{C["panel"] if i%2==0 else C["paper"]}"/>')
        p.append(_t(4, y + 4, name, 10, C["ink"], fam=BODY))
        for j, cell in enumerate(cells):
            good = cell.lower().startswith(("yes","ordinary")) and "blame" not in cell
            bad = cell.lower().startswith(("no","may","tiring","overkill","check"))
            colr = C["jade"] if good else (C["accent"] if bad else C["muted"])
            p.append(_t(L + j * cw + cw/2, y + 4, cell, 7.5, colr, "middle", fam=BODY))
    p.append(_t(L + 4 * cw + cw/2, T + 4 * rh + 4, "", 7.5, C["muted"], "middle"))
    y = T + 5 * rh + 10
    p.append(_t(0, y, "THE CHAIN, IN THE CORPUS'S WORDS", 8, C["jade"], ls="2"))
    p.append(_t(0, y + 17, "the licence class is fixed at home → it decides what a police stop costs → both bear on what the insurer says after a crash", 9, C["ink"], fam=BODY))
    p.append(_t(0, y + 32, "→ and a remote base is what makes the scooter tempting in the first place", 9, C["ink"], fam=BODY))
    p.append(_t(0, h - 10, "A PERMIT TRANSLATES THE LICENCE YOU HOLD; IT ADDS NO CLASS · MAXIMA AND FEES: FIELD SHEET", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_boat():
    """The water: Sanur to the Nusa islands, Padang Bai and Amed to the Gilis,
    Lombok's airport as the way round. From coordinates; crossing times as the
    site's travel guides give them."""
    h = 330
    keys = ["Sanur","Padang Bai","Amed","Lembongan","Toyapakeh","Sampalan","Kelingking","Gili T","Gili Air","Bangsal","Lombok airport","Ubud","Airport","Candidasa","Nusa Dua"]
    f = _proj([GEO[k] for k in keys], W, h, 40)
    p = _svg(h)
    def P(k): return f(*GEO[k])
    routes = [("Sanur","Toyapakeh","~30 MIN · PENIDA", C["jade"], ""), ("Sanur","Lembongan","35–45 MIN · LEMBONGAN", C["jade"], ""),
              ("Lembongan","Toyapakeh","~10 MIN", C["muted"], "3 3"), ("Padang Bai","Gili T","~1.5 H · OPEN STRAIT", C["accent"], ""),
              ("Amed","Gili T","SHORTEST SEA ROUTE", C["accent"], "4 3"), ("Bangsal","Gili T","SHORT HOP", C["jade"], "3 3"),
              ("Lombok airport","Bangsal","1 H 40 – 2 H BY ROAD", C["muted"], "2 3"), ("Padang Bai","Sampalan","SLOW FERRY", C["muted"], "5 4")]
    for a, b, lab, colr, dash in routes:
        (x1,y1),(x2,y2) = P(a), P(b)
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{colr}" stroke-width="{2 if not dash else 1.3}" stroke-dasharray="{dash}"/>')
        mx, my = (x1+x2)/2, (y1+y2)/2
        dy = -6 if a in ("Sanur","Padang Bai") and b in ("Toyapakeh","Gili T") else 12
        if a == "Sanur" and b == "Toyapakeh": dy = 14
        if a == "Sanur" and b == "Lembongan": dy = 27
        if a == "Lembongan": continue
        if a == "Bangsal": continue
        an = "middle"
        if a == "Lombok airport": an = "end"; mx += 70
        p.append(_t(mx, my + dy, lab, 7.5, colr, an, ls="0.5"))
    # the flight
    (x1,y1),(x2,y2) = P("Airport"), P("Lombok airport")
    p.append(f'<path d="M{x1:.1f},{y1:.1f} Q{(x1+x2)/2:.1f},{min(y1,y2)+120:.1f} {x2:.1f},{y2:.1f}" fill="none" stroke="{C["ink"]}" stroke-width="1.2" stroke-dasharray="6 3"/>')
    p.append(_t((x1+x2)/2, min(y1,y2) + 34, "SHORT FLIGHT · SEPARATE TICKET, OWN BAGGAGE RULES", 7.5, C["ink"], "middle", ls="0.5"))
    labels = {"Sanur":(-8,-6,"end"),"Padang Bai":(-8,-6,"end"),"Amed":(-8,-4,"end"),"Lembongan":(-6,-12,"end"),"Toyapakeh":(10,14,"start"),
              "Sampalan":(10,4,"start"),"Kelingking":(8,12,"start"),"Gili T":(0,-10,"middle"),"Gili Air":(10,4,"start"),"Bangsal":(10,14,"start"),
              "Lombok airport":(0,16,"middle"),"Ubud":(-8,-4,"end"),"Airport":(-8,10,"end"),"Candidasa":(8,12,"start"),"Nusa Dua":(8,12,"start")}
    names = {"Toyapakeh":"Nusa Penida · Toyapakeh · 10 min from Lembongan","Sampalan":"Sampalan","Gili T":"Gili Trawangan","Lembongan":"Nusa Lembongan","Kelingking":"Kelingking","Lombok airport":"Lombok airport"}
    for k, (dx, dy, an) in labels.items():
        x, y = P(k)
        port = k in ("Sanur","Padang Bai","Amed","Bangsal")
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if port else 3.2}" fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="{1.8 if port else 1.2}"/>')
        p.append(_t(x + dx, y + dy, _esc(names.get(k, k)), 9 if port or k in ("Ubud","Airport") else 8, C["ink"] if port else C["muted"], an, fam=BODY))
    p.append(_t(10, 16, "FROM COORDINATES · CROSSING TIMES AS THE SITE'S SOURCES GIVE THEM · RED: THE OPEN STRAIT", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_buffer():
    """Where the island leg sits, and what a cancelled boat costs in each place."""
    h = 230
    p = _svg(h)
    L, R = 24, 24; span = W - L - R; unit = span / 11.0
    def strip(y, title, blocks, boat_days, verdict, colr):
        p.append(_t(L, y - 8, title, 8.5, C["jade"], ls="1.5"))
        x = L
        for n, lab, cc in blocks:
            w = n * unit
            p.append(f'<rect x="{x:.1f}" y="{y}" width="{w-2:.1f}" height="22" fill="{cc}" opacity="0.88"/>')
            p.append(_t(x + w/2 - 1, y + 15, lab, 8.5, C["ink"] if cc == C["water"] else C["paper"], "middle", ls="0.5"))
            x += w
        for d in boat_days:
            xx = L + d * unit
            p.append(f'<path d="M{xx:.1f},{y+24} l5,8 l-10,0 z" fill="{C["deep"]}"/>')
        p.append(_t(L, y + 48, verdict, 9, colr, fam=BODY))
    strip(40, "ISLAND LEG IN THE MIDDLE · BOATS ON DAYS 4 AND 7",
          [(3,"UBUD",C["jade"]),(3,"ISLAND",C["water"]),(4,"COAST",C["accent"]),(1,"FLY",C["ink"])], [3, 6],
          "a cancelled return boat on day 7 costs one beach day; three remain before the flight", C["jade"])
    strip(128, "ISLAND LEG AT THE END · BOAT BACK ON DAY 10",
          [(4,"COAST",C["accent"]),(3,"UBUD",C["jade"]),(3,"ISLAND",C["water"]),(1,"FLY",C["ink"])], [7, 10],
          "the same cancellation costs the international flight; from the Nusa islands the only way back is by sea", C["deep"])
    p.append(_t(L, h - 10, "TRIANGLES: THE CROSSINGS · THE SITE'S MARGIN: A FULL DAY; TWO IN JULY, AUGUST OR THE WET MONTHS", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_spokes():
    """Road miles to the same sights from two bases. The base decides what a day
    can hold, because a day holds three or four stops in one direction."""
    h = 318
    p = _svg(h)
    sights = [("Tegallalang terraces", "Ubud", 6, None), ("Kintamani / Batur", "Ubud", 27, 45), ("Sidemen", "Ubud", 22, None),
              ("Besakih", "Ubud", 27, None), ("Munduk", "Ubud", 39, None), ("Amed", "Ubud", 49, None),
              ("Uluwatu temple", "Seminyak", 17, 34), ("Tanah Lot", "Canggu", 7, None), ("Padang Bai (the Gili boat)", "Seminyak", 32, 23)]
    L = 190; T = 40; rh = 24; maxmi = 50.0; bw = W - L - 70
    p.append(_t(L, T - 18, "ROAD MILES, THE SITE'S OWN · FROM UBUD (INDIGO) AND FROM THE SOUTH COAST (MAGENTA)", 7, C["soft"], ls="1"))
    rows = [("Tegallalang terraces", 6, None), ("Kintamani / Mount Batur", 27, 45), ("Sidemen valley", 22, None), ("Besakih", 27, None),
            ("Munduk & the lakes", 39, None), ("Amed", 49, None), ("Padang Bai, the Gili port", 23, 32), ("Uluwatu temple", 34, 17), ("Tanah Lot", None, 7)]
    for i, (name, ub, so) in enumerate(rows):
        y = T + i * rh
        p.append(_t(L - 8, y + 11, _esc(name), 9.5, C["ink"], "end", fam=BODY))
        if ub is not None:
            p.append(f'<rect x="{L}" y="{y}" width="{bw*ub/maxmi:.1f}" height="7" fill="{C["jade"]}" opacity="0.85"/>')
            p.append(_t(L + bw*ub/maxmi + 4, y + 7, f'{ub}', 8, C["jade"]))
        if so is not None:
            p.append(f'<rect x="{L}" y="{y+8}" width="{bw*so/maxmi:.1f}" height="7" fill="{C["accent"]}" opacity="0.85"/>')
            p.append(_t(L + bw*so/maxmi + 4, y + 15, f'{so}', 8, C["accent"]))
    y = T + 9 * rh + 12
    p.append(_t(0, y, "THE RULE THE SITE GIVES, WITHOUT A CLOCK", 8, C["jade"], ls="2"))
    p.append(_t(0, y + 17, "three or four stops in one direction, never doubling back through the busy south; the drive back is part of the day", 9, C["ink"], fam=BODY))
    p.append(_t(0, h - 10, "SOUTH-COAST BARS: FROM SEMINYAK, EXCEPT TANAH LOT FROM CANGGU · THREE LONG DAYS IS A COMMUTE", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_temples():
    """The four famous temples are in four corners. Which one is a short outing
    depends entirely on the base — a map, from coordinates."""
    h = 320
    keys = ["Uluwatu","Tanah Lot","Besakih","Lempuyang","Ubud","Seminyak","Canggu","Amed","Sidemen","Airport","Sanur","Tirta Empul","Nusa Dua"]
    f = _proj([GEO[k] for k in keys], W, h, 48)
    p = _svg(h)
    pairs = [("Seminyak","Uluwatu",17),("Canggu","Tanah Lot",7),("Ubud","Besakih",27),("Amed","Lempuyang",9),("Ubud","Lempuyang",45),("Seminyak","Besakih",None)]
    for a, b, mi in pairs:
        (x1,y1),(x2,y2) = f(*GEO[a]), f(*GEO[b])
        strong = mi is not None and mi <= 27
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C["jade"] if strong else C["accent"]}" stroke-width="{2 if strong else 1.2}" stroke-dasharray="{"" if strong else "4 3"}"/>')
        if mi:
            ox, oy = {("Ubud","Besakih"):(-34,-2), ("Ubud","Lempuyang"):(26,-12), ("Seminyak","Uluwatu"):(-36,-2), ("Amed","Lempuyang"):(-14,-4), ("Canggu","Tanah Lot"):(6,-4)}.get((a,b),(4,-4))
            p.append(_t((x1+x2)/2 + ox, (y1+y2)/2 + oy, f'{mi} MI', 8, C["jade"] if strong else C["accent"], ls="0.5"))
    temples = {"Uluwatu":"Uluwatu · cliff, sunset, kecak", "Tanah Lot":"Tanah Lot · sea rock, go in the morning", "Besakih":"Besakih · the mother temple", "Lempuyang":"Lempuyang · one photograph, a queue"}
    off = {"Uluwatu":(-8,14,"end"),"Tanah Lot":(-8,-6,"end"),"Besakih":(-10,-8,"end"),"Lempuyang":(8,14,"start")}
    for k, lab in temples.items():
        x, y = f(*GEO[k]); dx, dy, an = off[k]
        p.append(f'<path d="M{x:.1f},{y-7:.1f} l6,11 l-12,0 z" fill="{C["deep"]}"/>')
        p.append(_t(x + dx, y + dy, _esc(lab), 9, C["ink"], an, fam=BODY))
    for k, (dx, dy, an) in {"Ubud":(8,4,"start"),"Seminyak":(-8,4,"end"),"Canggu":(-8,-4,"end"),"Amed":(8,12,"start"),"Sidemen":(8,12,"start"),"Sanur":(8,12,"start"),"Nusa Dua":(8,12,"start")}.items():
        x, y = f(*GEO[k])
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{C["jade"]}"/>')
        p.append(_t(x + dx, y + dy, k, 9, C["muted"], an, fam=BODY))
    ax, ay = f(*GEO["Airport"]); p.append(f'<rect x="{ax-5:.1f}" y="{ay-5:.1f}" width="10" height="10" fill="{C["ink"]}"/>')
    p.append(_t(10, 16, "FROM COORDINATES · SOLID: A SHORT OUTING FROM THAT BASE · DASHED: A DAY'S DRIVING FOR ONE", 7, C["soft"], ls="1"))
    p.append(_t(10, h - 10, "THE INNER COURTYARDS ARE FOR WORSHIPPERS; EVERY VISIT IS TO THE SETTING, DRESSED FOR IT", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_march():
    """March 2027 on the calendar: Nyepi inside a national holiday cluster, and
    the arrival rule drawn on it."""
    h = 268
    p = _svg(h)
    L, T = 40, 50; cw = (W - L - 20) / 7.0; rh = 30
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    for i, d in enumerate(days): p.append(_t(L + i * cw + cw/2, T - 10, d, 8, C["muted"], "middle", ls="1"))
    # March 2027 starts on a Monday
    kind = {8:("NYEPI", C["deep"]), 10:("EID", C["accent"]), 11:("EID", C["accent"]), 9:("LEAVE", C["gilt"]), 12:("LEAVE", C["gilt"]), 15:("LEAVE", C["gilt"]), 6:("SAT", C["panel"]), 7:("SUN", C["panel"]), 13:("SAT", C["panel"]), 14:("SUN", C["panel"]), 25:("LEAVE", C["gilt"]), 26:("GOOD FRI", C["accent"])}
    for d in range(1, 32):
        col = (d - 1) % 7; row = (d - 1) // 7
        x = L + col * cw; y = T + row * rh
        lab, colr = kind.get(d, ("", None))
        if colr:
            p.append(f'<rect x="{x+1:.1f}" y="{y+1}" width="{cw-2:.1f}" height="{rh-2}" fill="{colr}" opacity="{0.9 if colr!=C["panel"] else 1}" rx="2"/>')
        p.append(_t(x + 5, y + 12, str(d), 9, C["paper"] if colr and colr != C["panel"] else C["ink"]))
        if lab and colr != C["panel"]: p.append(_t(x + cw - 4, y + 24, lab, 7, C["paper"], "end", ls="0.8"))
    # the arrival rule
    y = T + 5 * rh + 14
    p.append(_t(L, y, "THE RULE THE SITE GIVES", 8, C["jade"], ls="2"))
    p.append(_t(L, y + 16, "land a full day before Nyepi, not the evening before: the closure runs 6 a.m. to 6 a.m., the flight crosses the date line,", 9, C["ink"], fam=BODY))
    p.append(_t(L, y + 30, "and a connection that slips by a few hours lands on the wrong side of it", 9, C["ink"], fam=BODY))
    p.append(_t(L, h - 10, "NO WORKING DAY FROM SAT 6 TO MON 15 MARCH 2027 · NYEPI MOVES EVERY YEAR (19 MARCH IN 2026)", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_hubs():
    """No nonstop exists. The hubs, by the length of the second leg into Bali,
    as the site's October 2026 schedule snapshot gives them."""
    h = 300
    p = _svg(h)
    hubs = [("Singapore", 3.5, "W+E", "several airlines"), ("Kuala Lumpur · Bangkok · Manila", 3.0, "W", "listed, times vary"), ("Hong Kong · Taipei", 5.5, "W", "on the Pacific line"),
            ("Tokyo · Seoul", 7.5, "W", "splits the journey evenly"), ("Dubai · Doha", 10, "E", "East Coast"), ("Istanbul", 13, "E", "longest")]
    L = 230; T = 40; rh = 30; bw = W - L - 120; mx = 13.0
    p.append(_t(L, T - 18, "HOURS, SECOND LEG INTO BALI · AFTER THE LONG FLIGHT FROM THE US", 7, C["soft"], ls="1"))
    for i, (name, hrs, side, note) in enumerate(hubs):
        y = T + i * rh
        p.append(_t(L - 8, y + 11, _esc(name), 9.5, C["ink"], "end", fam=BODY))
        colr = C["jade"] if side.startswith("W") else C["accent"]
        p.append(f'<rect x="{L}" y="{y}" width="{bw*hrs/mx:.1f}" height="14" fill="{colr}" opacity="0.85"/>')
        p.append(_t(L + bw*hrs/mx + 5, y + 11, f'{hrs:g} h · {note}' if hrs != 3.0 else f'{note}', 8, C["muted"]))
    y = T + 6 * rh + 10
    p.append(_t(0, y, "WEST OVER THE PACIFIC (INDIGO) OR EAST THROUGH THE GULF (MAGENTA)", 8, C["jade"], ls="1"))
    p.append(_t(0, y + 18, "from the East Coast the two are about as short. The site's four questions: how long is the final leg and how many a day fly it;", 9, C["ink"], fam=BODY))
    p.append(_t(0, y + 32, "would the connection survive an hour's delay; one ticket or two; and what local hour you land", 9, C["ink"], fam=BODY))
    p.append(_t(0, h - 10, "SNAPSHOT OCTOBER 2026; ROUTES CHANGE · BALI IS UTC+8, NO CLOCK CHANGE: +12/13 NEW YORK, +15/16 LA", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_arrival():
    """The calendar day that goes into the crossing, and the arrival hour
    deciding the first bed."""
    h = 250
    p = _svg(h)
    L, R, T = 60, 20, 46
    span = W - L - R
    def X(hr): return L + span * hr / 60.0
    for hr, lab in ((0, "FRI 22:00"), (12, "SAT 10:00"), (24, "SAT 22:00"), (36, "SUN 10:00"), (48, "SUN 22:00"), (60, "MON 10:00")):
        p.append(f'<line x1="{X(hr):.1f}" y1="{T-6}" x2="{X(hr):.1f}" y2="{T+70}" stroke="{C["line"]}"/>')
        p.append(_t(X(hr), T - 12, lab, 9, C["muted"], "end" if hr == 60 else ("start" if hr == 0 else "middle")))
    p.append(_t(L, T + 8, "LOS ANGELES CLOCK", 7, C["soft"], ls="1.5"))
    p.append(f'<rect x="{X(0):.1f}" y="{T+14}" width="{X(26)-X(0):.1f}" height="16" fill="{C["ink"]}" opacity="0.85"/>')
    p.append(_t(X(13), T + 25, "TWO FLIGHTS, ONE HUB, A DAY AND MORE", 7.5, C["paper"], "middle", ls="1"))
    p.append(_t(L, T + 48, "BALI CLOCK (+15 H ON LOS ANGELES IN WINTER, +16 IN SUMMER)", 7, C["soft"], ls="1.5"))
    p.append(f'<rect x="{X(26):.1f}" y="{T+54}" width="{X(40)-X(26):.1f}" height="16" fill="{C["gilt"]}" opacity="0.9"/>')
    p.append(_t(X(33), T + 65, "SUNDAY: WRITTEN OFF", 7.5, C["ink"], "middle", ls="0.8"))
    p.append(_t(X(26), T + 86, "YOU LEFT ON FRIDAY; IT IS SUNDAY. THE DAY WENT INTO THE DATE LINE.", 7.5, C["accent"], ls="0.5"))
    y0 = T + 110
    p.append(_t(L, y0 - 4, "THE ARRIVAL HOUR DECIDES THE FIRST BED", 8, C["jade"], ls="2"))
    rows = [("Lands by early afternoon", "Ubud, 22 miles, or anywhere · the day is already written off"),
            ("Lands at dusk", "the south coast, 4–11 miles · Ubud waits until morning"),
            ("Lands late at night", "Kuta, Jimbaran or Sanur, the shortest drives · move on after breakfast")]
    for i, (a, b) in enumerate(rows):
        yy = y0 + 10 + i * 20
        p.append(_t(L, yy + 8, a, 9.5, C["ink"], fam=BODY))
        p.append(_t(L + 190, yy + 8, _esc(b), 8.5, C["muted"], fam=BODY))
    p.append(_t(L, h - 8, "ROAD MILES, THE SITE'S OWN · GRAB'S LOUNGE IS AT THE INTERNATIONAL TERMINAL", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_chain():
    """The health chain: each link is manageable alone; the book draws how they
    connect when something goes wrong."""
    h = 258
    p = _svg(h)
    boxes = [("1 · THE BAG", "narcotic class: banned,\nprescription or not;\npsychotropic 60 days;\nordinary 90 days", "ADHD stimulants and\nCBD are the US cases"),
             ("2 · THE BORDER", "medicine → red channel;\ndeclare it on the card;\nnon-compliant is seized", "no published list\nexists to look it up"),
             ("3 · THE CLINIC", "deposit before treatment;\nmostly cash; ambulance\n45 min or more", "a taxi is the\nambulance"),
             ("4 · THE POLICY", "you pay, then claim;\nscooter clause; evacuation\nclause; transfers extra", "Medicare pays\nnothing abroad")]
    bw = 148; gap = (W - 4 * bw) / 3
    for i, (head, body, lock) in enumerate(boxes):
        x = i * (bw + gap)
        p.append(f'<rect x="{x:.1f}" y="30" width="{bw}" height="130" fill="{C["panel"]}" stroke="{C["edge"]}"/>')
        p.append(f'<rect x="{x:.1f}" y="30" width="{bw}" height="3" fill="{C["accent"]}"/>')
        p.append(_t(x + 10, 50, head, 8.5, C["accent"], ls="1.5"))
        for j, ln in enumerate(body.split("\n")):
            p.append(_t(x + 10, 68 + j * 13, _esc(ln), 9, C["ink"], fam=BODY))
        p.append(f'<line x1="{x+10:.1f}" y1="{124}" x2="{x+bw-10:.1f}" y2="124" stroke="{C["line"]}"/>')
        for j, ln in enumerate(lock.split("\n")):
            p.append(_t(x + 10, 140 + j * 12, _esc(ln), 8.5, C["deep"], fam=BODY))
        if i < 3:
            p.append(_t(x + bw + gap / 2, 100, "→", 14, C["soft"], "middle"))
    p.append(_t(0, 188, "WHAT BREAKS THE CHAIN", 8, C["jade"], ls="2"))
    p.append(_t(0, 206, "the base is the fifth link: how far the villa is from a clinic, and whether a scooter was the only way to dinner, were decided at booking", 9, C["ink"], fam=BODY))
    p.append(_t(0, h - 10, "RABIES IS DECIDED BEFORE YOU FLY · AFTER A BITE: WASH, THEN A CLINIC THE SAME DAY", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_bill():
    """The small percentages that land on the same dollar, and which of them are
    decided at home. Structure only: the site prints no daily budget."""
    h = 300
    p = _svg(h)
    L = 210; T = 40; rh = 34; bw = 300
    rows = [("Foreign transaction fee", 3, "YOUR BANK · REMOVED AT HOME BY THE CARD YOU CARRY", C["accent"]),
            ("Dynamic currency conversion", 4, "THE TERMINAL · DECLINE; PAY IN RUPIAH", C["accent"]),
            ("Local tax, food, drink, rooms", 10, "BADUNG AND GIANYAR · ON THE BILL, NOT ON THE MENU", C["jade"]),
            ("Service charge, hotels", None, "THE BUSINESS'S OWN RATE · TO THE STAFF BY REGULATION", C["jade"]),
            ("Entertainment tax, bars and spas", 40, "SET AT 40% IN 2024, CONTESTED · READ THE VENUE'S PRICE", C["deep"]),
            ("Unlicensed changer, ATM operator", None, "NO PRIMARY FIGURE · THE LICENCE NUMBER AND THE BANK LOGO", C["muted"])]
    p.append(_t(L, T - 18, "PERCENT OF THE SAME DOLLAR · BARS ARE DRAWN ONLY WHERE A REGULATION STATES THE RATE", 7, C["soft"], ls="1"))
    for i, (name, pct, note, colr) in enumerate(rows):
        y = T + i * rh
        p.append(_t(L - 8, y + 11, name, 9.5, C["ink"], "end", fam=BODY))
        if pct is not None:
            p.append(f'<rect x="{L}" y="{y}" width="{bw*pct/40:.1f}" height="12" fill="{colr}" opacity="0.85"/>')
            p.append(_t(L + bw*pct/40 + 5, y + 10, f'{pct}%' if pct not in (3,4) else ("~3%" if pct==3 else "the spread"), 8.5, colr))
        else:
            p.append(f'<rect x="{L}" y="{y}" width="40" height="12" fill="none" stroke="{colr}" stroke-dasharray="3 3"/>')
        p.append(_t(L, y + 22, note, 7, C["soft"], ls="0.8"))
    y = T + 6 * rh + 12
    p.append(_t(0, y, "WHAT AN AMERICAN CANNOT USE: QRIS. SIX ASIAN COUNTRIES ARE CONNECTED; THE US IS NOT", 8, C["jade"], ls="1"))
    p.append(_t(0, y + 18, "so the working methods are two: a card without a foreign fee for the large items, and rupiah notes, counted by the zeros, for the small", 9, C["ink"], fam=BODY))
    p.append('</svg>')
    return "".join(p)

# ═════════════════════════════════════════════════════════════════════════════
def fig_bases():
    """Nine bases scored on identical criteria: road miles to the airport and to
    Ubud, whether you can walk to dinner, and the season that works."""
    h = 330
    p = _svg(h)
    cols = ["AIRPORT, MI", "UBUD, MI", "WALK TO DINNER", "SURF SEASON", "FAMILIES"]
    rows = [("Seminyak", "7", "20", "yes", "dry", "fine"), ("Canggu", "12", "19", "spread out", "dry", "surfers"),
            ("Uluwatu / the Bukit", "13", "34", "no — a drive apart", "dry", "steps to every beach"),
            ("Sanur", "11", "14", "yes, flat", "wet", "YES · boats leave here"), ("Nusa Dua", "8", "26", "inside the resort", "wet", "YES · little traffic"),
            ("Ubud centre", "22", "—", "yes, congested", "no beach", "older children"), ("Ubud villages", "22+", "—", "a ride", "no beach", "pool matters"),
            ("Sidemen · Amed", "35 · 61", "22 · 49", "no", "—", "a longer trip"), ("Munduk", "51", "39", "no", "—", "sweater, walkers"),
            ("Nusa Lembongan", "boat", "boat", "yes, small", "—", "wet landing")]
    L = 150; cw = (W - L) / 5; T = 40; rh = 24
    for j, c in enumerate(cols): p.append(_t(L + j * cw + cw/2, T - 16, c, 7, C["muted"], "middle", ls="1"))
    for i, row in enumerate(rows):
        y = T + i * rh
        p.append(f'<rect x="0" y="{y-14}" width="{W}" height="{rh}" fill="{C["panel"] if i%2==0 else C["paper"]}"/>')
        p.append(_t(4, y + 4, row[0], 9.5, C["ink"], fam=BODY))
        for j, cell in enumerate(row[1:]):
            colr = C["jade"] if cell.lower().startswith("yes") else (C["accent"] if cell.lower().startswith("no") else C["muted"])
            p.append(_t(L + j * cw + cw/2, y + 4, cell, 8, colr, "middle", fam=BODY))
    p.append(_t(0, h - 24, "ROAD MILES ARE THE SITE'S OWN · SURF SEASON: THE COAST THE WIND FAVOURS · NO HOTEL IS NAMED", 7, C["soft"], ls="1"))
    p.append(_t(0, h - 10, "THE QUESTION TO ASK OF EVERY BASE: WHAT IS IT FAR FROM", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)

FIGURES = {
 "island":  (fig_island,  "The island from coordinates, the airport at its neck, and the site's own road miles to every base. Nothing is far in miles; the hours are the subject of this book."),
 "nights":  (fig_nights,  "Where the nights go. The first two days are slow, the last is partly spent leaving, and a base needs three nights: the ticks are the bases each length buys."),
 "order":   (fig_order,   "The same ten nights, in two orders. The three pins are the points the trip cannot move; the second order puts each of them where it costs least."),
 "season":  (fig_season,  "Four calendars that do not agree: the rain, the crowd, the coast the surf is on, and the months the strait is roughest. July is dry, full and rough at once."),
 "stack":   (fig_stack,   "The entry stack as a timeline. Five systems, five sites; the passport must be settled first and the arrival card cannot be done before the last three days."),
 "road":    (fig_road,    "Five ways to cover a Bali road, scored on the licence chain, the insurer and which journeys each one reaches. The car-only licence row is the one most Americans are in."),
 "boat":    (fig_boat,    "The water, from coordinates. The Nusa crossings from Sanur, the open strait to the Gilis, and the flight to Lombok as the only route that does not answer to the harbour master's sailing approval."),
 "buffer":  (fig_buffer,  "Where the island leg sits decides what a cancelled boat costs: a beach day in one order, the flight home in the other."),
 "spokes":  (fig_spokes,  "The same sights from two bases, in the site's road miles. A day holds three or four stops in one direction, so the base decides what the day can contain."),
 "temples": (fig_temples, "Four famous temples in four corners, from coordinates. Each is a short outing from one base and a day's driving from the others; few trips need all four."),
 "march":   (fig_march,   "March 2027 on the calendar: Nyepi on the 8th inside a national holiday cluster that runs from the 6th to the 15th without a working day."),
 "hubs":    (fig_hubs,    "No nonstop exists. The hubs by the length of the second leg into Bali, from the site's October 2026 schedule snapshot; west or east, the layover is a real choice."),
 "arrival": (fig_arrival, "The calendar day that goes into the date line, and the arrival hour deciding how far the first bed should be from the airport."),
 "chain":   (fig_chain,   "The health chain. Each link is manageable alone; the book draws how they connect when something goes wrong, and where the base joins them."),
 "bill":    (fig_bill,    "The small percentages that land on the same dollar. Two are decided at home, two are regulations, one is contested, and none is a daily budget."),
 "bases":   (fig_bases,   "Nine bases on identical criteria: road miles to the airport and to Ubud, whether you can walk to dinner, the coast the season favours, and who each suits."),
}
