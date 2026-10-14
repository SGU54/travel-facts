# maps.py — every vector figure, drawn from REAL numbers and REAL coordinates.
# Geography, distances and published hours are public facts; drawing our own
# figure from them is fine (SKILL non-negotiable 6). No stock art, no tiles.
#
# viewBox note (bug log #8): the body column is 652px (816 − 2×82), so figures
# are authored at 652 wide and scale to width:100%. Essential labels ≥ 9px.
# ─────────────────────────────────────────────────────────────────────────────
import math

C = {
 "ink":"#16140F", "accent":"#C9321D", "jade":"#137A64", "gilt":"#D9A520",
 "muted":"#514B42", "soft":"#8A8378", "line":"#D7CFBD", "panel":"#EAE3D3",
 "deep":"#8F2112", "paper":"#F3EDE0", "water":"#CFDDD8", "edge":"#E2D9C6",
}
W = 652
MONO = "'Space Mono',monospace"
DISP = "'Anton',sans-serif"
BODY = "'Source Serif 4',serif"

# ── real coordinates (lat, lon) ──────────────────────────────────────────────
GEO = {
 "Hà Giang":   (22.8025, 104.9784),
 "Sapa":       (22.3364, 103.8438),
 "Hanoi":      (21.0285, 105.8542),
 "Nội Bài":    (21.2212, 105.8072),
 "Hạ Long":    (20.9517, 107.0777),
 "Cát Bà":     (20.7275, 107.0483),
 "Ninh Bình":  (20.2506, 105.9745),
 "Phong Nha":  (17.5917, 106.2833),
 "Huế":        (16.4637, 107.5909),
 "Lăng Cô":    (16.2400, 108.0670),
 "Đà Nẵng":    (16.0544, 108.2022),
 "Hội An":     (15.8801, 108.3380),
 "An Bàng":    (15.9150, 108.3450),
 "Mỹ Sơn":     (15.7636, 108.1238),
 "Quy Nhơn":   (13.7830, 109.2197),
 "Nha Trang":  (12.2388, 109.1967),
 "Đà Lạt":     (11.9404, 108.4583),
 "Mũi Né":     (10.9333, 108.2833),
 "Ho Chi Minh City": (10.7769, 106.7009),
 "Tân Sơn Nhất": (10.8188, 106.6520),
 "Cần Thơ":    (10.0452, 105.7469),
 "Châu Đốc":   (10.7000, 105.1167),
 "Phú Quốc":   (10.2899, 103.9840),
 "Côn Đảo":    (8.6829, 106.6060),
}

def km(a, b):
    """great-circle distance between two named places, km"""
    (la1, lo1), (la2, lo2) = GEO[a], GEO[b]
    R = 6371; p = math.pi / 180
    dlat = (la2 - la1) * p; dlon = (lo2 - lo1) * p
    h = math.sin(dlat/2)**2 + math.cos(la1*p) * math.cos(la2*p) * math.sin(dlon/2)**2
    return 2 * R * math.asin(math.sqrt(h))

def miles(a, b): return km(a, b) * 0.621371

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def _proj(pts, w, h, pad):
    """equirectangular projection, aspect-corrected at the mean latitude."""
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
    """Printed floor: nothing a reader must read goes below 9px (6.75pt) on the
    652-unit board (quality-standard.md). A long apparatus line that would run
    off the board at that size wraps onto a second line instead of shrinking."""
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

# The season bands, from the corpus's own weather grid (best-time-to-visit,
# weather-by-region, phu-quoc-vs-nha-trang, con-dao, mui-ne). Values per month:
# 2 = the region's good window · 1 = workable with a caveat · 0 = its bad months
SEASON = {
 "NORTH  · Hanoi, the bay, Sapa":      [0,0,2,2,1,0,0,0,2,2,2,0],
 "CENTRE · Huế, Đà Nẵng, Hội An":      [1,2,2,2,2,2,2,2,0,0,0,1],
 "SOUTH  · Saigon, the delta":         [2,2,2,2,1,1,1,1,1,1,1,2],
 "PHÚ QUỐC":                           [2,2,2,2,0,0,0,0,0,0,2,2],
 "NHA TRANG":                          [2,2,2,2,2,2,2,2,0,0,0,0],
}
SEASON_NOTE = {
 "NORTH  · Hanoi, the bay, Sapa":  "cold grey drizzle Dec–Feb · hot and wettest Jun–Aug",
 "CENTRE · Huế, Đà Nẵng, Hội An":  "storm season Sep–Nov · Hội An floods most years",
 "SOUTH  · Saigon, the delta":     "dry Dec–Apr · afternoon downpours May–Nov",
 "PHÚ QUỐC":                       "dry Nov–Apr · rough sea May–Oct",
 "NHA TRANG":                      "dry Jan–Aug · wettest Oct–Nov",
}
SCOL = {2: C["jade"], 1: C["gilt"], 0: C["accent"]}
SOPA = {2: "0.9", 1: "0.55", 0: "0.45"}


# ═════════════════════════════════════════════════════════════════════════════
def fig_line():
    """THE figure. The country as the line it is, from real coordinates, with
    the three climates beside it. You cannot draw the right-hand half without
    having done the weather analysis."""
    h = 466
    pts = [GEO[k] for k in ("Sapa","Hanoi","Hạ Long","Ninh Bình","Huế","Đà Nẵng","Hội An",
                            "Nha Trang","Ho Chi Minh City","Cần Thơ","Phú Quốc","Côn Đảo","Hà Giang")]
    f = _proj(pts, 300, h, 34)
    p = _svg(h)
    # regional shading on the map half: north / centre / south by latitude
    def Y(lat): return f(lat, 106.0)[1]
    for lo, hi, col, lab in ((19.0, 23.6, SCOL[2], "NORTH"), (14.5, 19.0, C["gilt"], "CENTRE"), (8.3, 14.5, C["accent"], "SOUTH")):
        y0, y1 = Y(hi), Y(lo)
        p.append(f'<rect x="20" y="{y0:.1f}" width="270" height="{y1-y0:.1f}" fill="{col}" opacity="0.07"/>')
        p.append(_t(26, y0 + 13, lab, 8, C["soft"], ls="2"))
    # the spine: Hanoi → Huế → Đà Nẵng → Nha Trang → HCMC (the railway's cities)
    spine = ["Hanoi","Ninh Bình","Huế","Đà Nẵng","Nha Trang","Ho Chi Minh City"]
    pts_s = " ".join(f"{f(*GEO[k])[0]:.1f},{f(*GEO[k])[1]:.1f}" for k in spine)
    p.append(f'<polyline points="{pts_s}" fill="none" stroke="{C["ink"]}" stroke-width="2.2" stroke-linejoin="round"/>')
    # spokes
    for a, b in (("Hanoi","Sapa"),("Hanoi","Hạ Long"),("Ho Chi Minh City","Cần Thơ"),("Cần Thơ","Phú Quốc"),("Ho Chi Minh City","Côn Đảo"),("Hanoi","Hà Giang")):
        (x1,y1),(x2,y2) = f(*GEO[a]), f(*GEO[b])
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C["soft"]}" stroke-width="1" stroke-dasharray="3 3"/>')
    big = {"Hanoi","Ho Chi Minh City","Đà Nẵng"}
    side = {"Sapa":"end","Hà Giang":"start","Hạ Long":"start","Ninh Bình":"end","Huế":"end","Đà Nẵng":"start","Hội An":"start",
            "Nha Trang":"start","Ho Chi Minh City":"start","Cần Thơ":"end","Phú Quốc":"end","Côn Đảo":"start","Hanoi":"end"}
    for k in ("Sapa","Hà Giang","Hanoi","Hạ Long","Ninh Bình","Huế","Đà Nẵng","Hội An","Nha Trang","Ho Chi Minh City","Cần Thơ","Phú Quốc","Côn Đảo"):
        x, y = f(*GEO[k])
        r = 4.2 if k in big else 2.8
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.6"/>')
        an = side[k]; dx = 8 if an == "start" else -8
        dy = 3
        if k == "Hội An": dy = 11
        if k == "Đà Nẵng": dy = -4
        lab = "Saigon" if k == "Ho Chi Minh City" else k
        p.append(_t(x + dx, y + dy, _esc(lab), 9.5 if k in big else 8.5, C["ink"] if k in big else C["muted"], an, fam=BODY))
    # the one number
    d = km("Hanoi", "Ho Chi Minh City")
    p.append(_t(150, h - 10, f'HANOI → SAIGON {d:,.0f} KM · {d*0.621371:,.0f} MI, CROW FLIES', 9, C["soft"], "middle", ls="1.2"))
    # ── right half: the three climates, by month ───────────────────────────
    L, R, T = 330, 12, 34
    cw = (W - L - R) / 12.0
    for i, m in enumerate(MONTHS):
        p.append(_t(L + i*cw + cw/2, T - 10, m, 7.5, C["muted"], "middle"))
    rows = list(SEASON.items())[:3]
    rh = 44; gap = 30
    for ri, (name, vals) in enumerate(rows):
        y = T + 12 + ri * (rh + gap)
        p.append(_t(L, y - 2 + 0, _esc(name), 8, C["ink"], ls="1"))
        for i, v in enumerate(vals):
            x = L + i * cw
            p.append(f'<rect x="{x+1:.1f}" y="{y+4}" width="{cw-2:.1f}" height="22" fill="{SCOL[v]}" opacity="{SOPA[v]}"/>')
        p.append(_t(L, y + 42, _esc(SEASON_NOTE[name]), 7.5, C["soft"]))
    ly = T + 12 + 3 * (rh + gap) + 4
    for i, (v, lab) in enumerate(((2, "GOOD WINDOW"), (1, "WITH A CAVEAT"), (0, "BAD MONTHS"))):
        x = L + i * 112
        p.append(f'<rect x="{x}" y="{ly}" width="12" height="10" fill="{SCOL[v]}" opacity="{SOPA[v]}"/>')
        p.append(_t(x + 16, ly + 9, lab, 6.5, C["muted"], ls="0.6"))
    p.append(_t(L, ly + 32, "NO MONTH IS GREEN IN ALL THREE.", 7.5, C["accent"], ls="1"))
    p.append(_t(L, ly + 44, "MARCH–APRIL COMPROMISES LEAST; OCTOBER IS THE", 7.5, C["accent"], ls="1"))
    p.append(_t(L, ly + 56, "NORTH'S BEST AND THE CENTRE'S WORST, THE SAME WEEK.", 7.5, C["accent"], ls="1"))
    p.append(f'<line x1="310" y1="20" x2="310" y2="{h-20}" stroke="{C["line"]}"/>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_season():
    """Decision 02 and 09: the five coasts/regions by month, with the three
    holiday spikes that fill the seats."""
    h = 330
    L, R, T = 150, 14, 40
    cw = (W - L - R) / 12.0
    p = _svg(h)
    for i, m in enumerate(MONTHS):
        x = L + i * cw
        p.append(f'<line x1="{x:.1f}" y1="{T-8}" x2="{x:.1f}" y2="{T+5*34}" stroke="{C["line"]}"/>')
        p.append(_t(x + cw/2, T - 14, m, 8, C["muted"], "middle"))
    p.append(f'<line x1="{W-R:.1f}" y1="{T-8}" x2="{W-R:.1f}" y2="{T+5*34}" stroke="{C["line"]}"/>')
    for ri, (name, vals) in enumerate(SEASON.items()):
        y = T + ri * 34
        p.append(_t(L - 8, y + 15, _esc(name.split("·")[0].strip()), 8.5, C["ink"], "end", ls="1"))
        for i, v in enumerate(vals):
            x = L + i * cw
            p.append(f'<rect x="{x+1:.1f}" y="{y+2}" width="{cw-2:.1f}" height="22" fill="{SCOL[v]}" opacity="{SOPA[v]}" rx="1"/>')
    # holiday spikes — the fixed solar dates; Tết drawn for 2027 (4–10 Feb)
    yb = T + 5 * 34 + 8
    spikes = [(1 + 3/28, 1 + 10/28, "TẾT 2027 · 4–10 FEB", C["deep"]),
              (3 + 29/30, 4 + 2/31, "30 APR – 1 MAY", C["deep"]),
              (8 + 1/30, 8 + 5/30, "2–5 SEP", C["deep"])]
    for si, (s, e, lab, col) in enumerate(spikes):
        x0 = L + s * cw; x1 = L + e * cw
        p.append(f'<rect x="{x0:.1f}" y="{yb}" width="{max(x1-x0,3):.1f}" height="12" fill="{col}"/>')
        p.append(_t(x0, yb + 24 + (12 if si == 1 else 0), lab, 9, C["deep"], "start", ls="0.3"))
    p.append(_t(L - 8, yb + 10, "SEATS SELL OUT", 7.5, C["deep"], "end", ls="1"))
    ly = yb + 52
    for i, (v, lab) in enumerate(((2, "GOOD WINDOW"), (1, "WORKABLE WITH A CAVEAT"), (0, "BAD MONTHS"))):
        x = L + i * 150
        p.append(f'<rect x="{x}" y="{ly}" width="12" height="10" fill="{SCOL[v]}" opacity="{SOPA[v]}"/>')
        p.append(_t(x + 16, ly + 9, lab, 7, C["muted"], ls="1"))
    p.append(_t(L, ly + 28, "DRAWN FROM THE SITE'S OWN MONTH-BY-REGION WEATHER GRID · TẾT MOVES EVERY YEAR — THE BAR IS 2027'S", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_days():
    """Where the days go. Days on the ground = leave − 2 travel days; the
    arrival day is written off; each region change costs about half a day."""
    rows = [("10 days of leave", 10, 2, 1, 2, "two regions, one internal flight"),
            ("13 days of leave", 13, 2, 1, 3, "three regions, tightly"),
            ("17 days of leave", 17, 2, 1, 3, "three regions, with slack"),
            ("24 days of leave", 24, 2, 1, 4, "three regions plus what a fortnight cuts")]
    rh, top = 46, 36
    h = top + rh * len(rows) + 62
    L, R = 150, 36
    unit = (W - L - R) / 24.0
    p = _svg(h)
    legend = [(C["soft"], "CROSSING"), (C["gilt"], "ARRIVAL, LOST"), (C["accent"], "TRANSFERS"), (C["jade"], "DAYS THAT COUNT")]
    x = L
    for col, lab in legend:
        p.append(f'<rect x="{x}" y="10" width="11" height="10" fill="{col}" opacity="0.9"/>')
        p.append(_t(x + 15, 19, lab, 9, C["muted"], ls="0.3"))
        x += 128
    for i, (lab, leave, cross, arrive, moves, note) in enumerate(rows):
        y = top + i * rh
        p.append(_t(0, y + 14, lab, 10, C["ink"], fam=BODY))
        p.append(_t(0, y + 27, _esc(note), 7.5, C["soft"]))
        x0 = L
        segs = [(cross, C["soft"]), (arrive, C["gilt"]), (moves * 0.5, C["accent"])]
        count = leave - cross - arrive - moves * 0.5
        segs.append((count, C["jade"]))
        for d, col in segs:
            w = d * unit
            p.append(f'<rect x="{x0:.1f}" y="{y}" width="{w:.1f}" height="22" fill="{col}" opacity="0.9"/>')
            x0 += w
        p.append(_t(x0 - 6, y + 15, f'{count:g}', 9.5, C["paper"], "end"))
        p.append(_t(L + leave * unit + 6, y + 15, f'{leave}', 8.5, C["muted"]))
    p.append(_t(L, h - 10, "TWO DAYS TO CROSS, ONE TO ARRIVE, HALF A DAY PER MOVE · THE GREEN IS THE TRIP", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_visa():
    """The four binding fields on the e-visa form, and what each one locks."""
    h = 250
    p = _svg(h)
    boxes = [("1 · DURATION", "granted as requested,\nnot the 90-day maximum", "cannot be extended\nfrom inside Vietnam"),
             ("2 · ENTRIES", "single, or multiple\nfor a loop out and back", "a single entry is spent\nthe moment you leave"),
             ("3 · PORT IN", "the airport or crossing\nyou will actually use", "must match the gate,\nor you are refused"),
             ("4 · PORT OUT", "the airport, or the\nland or river crossing", "a river exit on an\nairport visa fails")]
    bw = 148; gap = (W - 4 * bw) / 3
    for i, (head, body, lock) in enumerate(boxes):
        x = i * (bw + gap)
        p.append(f'<rect x="{x:.1f}" y="30" width="{bw}" height="118" fill="{C["panel"]}" stroke="{C["edge"]}"/>')
        p.append(f'<rect x="{x:.1f}" y="30" width="{bw}" height="3" fill="{C["accent"]}"/>')
        p.append(_t(x + 10, 50, head, 8.5, C["accent"], ls="1.5"))
        for j, ln in enumerate(body.split("\n")):
            p.append(_t(x + 10, 70 + j * 14, _esc(ln), 9.5, C["ink"], fam=BODY))
        p.append(f'<line x1="{x+10:.1f}" y1="102" x2="{x+bw-10:.1f}" y2="102" stroke="{C["line"]}"/>')
        for j, ln in enumerate(lock.split("\n")):
            p.append(_t(x + 10, 118 + j * 13, _esc(ln), 8.5, C["deep"], fam=BODY))
        if i < 3:
            ax = x + bw + gap / 2
            p.append(_t(ax, 95, "→", 14, C["soft"], "middle"))
    p.append(_t(0, 175, "WHAT THE FORM SILENTLY DECIDES", 8, C["jade"], ls="2"))
    p.append(_t(0, 193, "how long the trip can be · whether Cambodia can be a loop · which end you land at · whether the Mekong boat is a way out", 9, C["ink"], fam=BODY))
    p.append(_t(0, 215, "ALL FOUR ARE SET BEFORE THE ROUTE IS; NONE CAN BE CHANGED FROM INSIDE THE COUNTRY · FEES: FIELD SHEET", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
LEGS = [
 # name, road/rail km, fly h door-to-door, train h, bus h   (corpus figures; door-to-door flight = 1h15–2h15 air + ~3h airports)
 ("Hanoi → Saigon",   1726, 5.3, 34.0, 32.0),
 ("Hanoi → Đà Nẵng",  764,  4.3, 16.0, 16.0),
 ("Saigon → Đà Nẵng", 960,  4.3, 17.0, 20.0),
 ("Hanoi → Sapa",     320,  None, 9.0, 5.5),
 ("Huế → Đà Nẵng",    100,  4.0, 3.0,  2.0),
 ("Saigon → Cần Thơ", 170,  None, None, 3.5),
]

def fig_legs():
    """The legs: distance against hours door to door, by mode. The 150/500-mile
    rule from the corpus drawn as two verticals."""
    h = 316
    L, R, T, B = 150, 22, 30, 50
    xmax = 1800; ymax = 36
    def X(kmv): return L + (W - L - R) * kmv / xmax
    def Y(hr): return T + (h - T - B) * (1 - hr / ymax)
    p = _svg(h)
    for hr in (0, 6, 12, 18, 24, 30, 36):
        p.append(f'<line x1="{L}" y1="{Y(hr):.1f}" x2="{W-R}" y2="{Y(hr):.1f}" stroke="{C["line"]}"/>')
        p.append(_t(L - 8, Y(hr) + 3, f'{hr}h', 8, C["muted"], "end"))
    for kmv in (0, 500, 1000, 1500):
        p.append(_t(X(kmv), h - B + 16, f'{kmv} km', 8, C["muted"], "middle"))
    # the corpus's thresholds: flying wins above ~500 miles (805 km), loses below ~150 miles (241 km)
    for kmv, lab, yy in ((241, "150 MI · BELOW THIS, NEVER FLY", T + 10), (805, "500 MI · ABOVE THIS, FLY", T + 24)):
        p.append(f'<line x1="{X(kmv):.1f}" y1="{T}" x2="{X(kmv):.1f}" y2="{h-B}" stroke="{C["accent"]}" stroke-dasharray="3 3"/>')
        p.append(_t(X(kmv) + 4, yy, lab, 7, C["accent"], ls="1"))
    marks = {"fly": (C["jade"], "FLY · DOOR TO DOOR"), "train": (C["ink"], "TRAIN"), "bus": (C["gilt"], "ROAD")}
    for name, kmv, fly, train, bus in LEGS:
        x = X(kmv)
        for mode, hr in (("fly", fly), ("train", train), ("bus", bus)):
            if hr is None: continue
            col = marks[mode][0]
            if mode == "fly":
                p.append(f'<circle cx="{x:.1f}" cy="{Y(hr):.1f}" r="4" fill="{col}"/>')
            elif mode == "train":
                p.append(f'<rect x="{x-3.5:.1f}" y="{Y(hr)-3.5:.1f}" width="7" height="7" fill="{col}"/>')
            else:
                p.append(f'<polygon points="{x:.1f},{Y(hr)-4.5:.1f} {x+4.5:.1f},{Y(hr)+3.5:.1f} {x-4.5:.1f},{Y(hr)+3.5:.1f}" fill="{col}"/>')
        top = max(v for v in (fly, train, bus) if v is not None)
        an = "middle"; dx = 0; dy = -9
        if name.startswith("Huế"): an = "end"; dx = -8; dy = 3
        if name.startswith("Saigon → C"): an = "start"; dx = 8; dy = 3
        p.append(_t(x + dx, Y(top) + dy, _esc(name), 7.5, C["muted"], an))
    lx = L
    for mode in ("fly", "train", "bus"):
        col, lab = marks[mode]
        p.append(f'<rect x="{lx}" y="{h-18}" width="9" height="9" fill="{col}"/>')
        p.append(_t(lx + 13, h - 10, lab, 7, C["muted"], ls="1"))
        lx += 130
    p.append(_t(W - R, T - 8, "HOURS ARE THE CORPUS'S DOOR-TO-DOOR FIGURES", 7, C["soft"], "end", ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_north():
    """The northern leg: Hanoi's three spokes, with the road time each costs."""
    h = 344
    keys = ("Hanoi","Sapa","Hạ Long","Cát Bà","Ninh Bình","Nội Bài","Hà Giang")
    f = _proj([GEO[k] for k in keys], W, h, 70)
    p = _svg(h)
    HX, HY = f(*GEO["Hanoi"])
    spokes = [("Sapa", "5–6 H ROAD · NO FLIGHT BACKUP", "2 travel days for 1 in the valley"),
              ("Hạ Long", "2.5–3 H ROAD, EACH WAY", "an overnight claims ~2 days"),
              ("Ninh Bình", "2 H ROAD OR RAIL", "one day, there and back"),
              ("Hà Giang", "7+ H · THEN A 3–4 DAY LOOP", "replaces Sapa, wants more")]
    for name, t1, t2 in spokes:
        x, y = f(*GEO[name])
        p.append(f'<line x1="{HX:.1f}" y1="{HY:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{C["accent"] if name!="Hà Giang" else C["soft"]}" stroke-width="{2.4 if name!="Hà Giang" else 1}" stroke-dasharray="{"" if name!="Hà Giang" else "4 3"}"/>')
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.6"/>')
        an = "start" if x > HX + 20 else ("end" if x < HX - 20 else "middle")
        dx = 9 if an == "start" else (-9 if an == "end" else 0)
        dy = -10 if y < HY else 16
        if name == "Ninh Bình": dy = 18; an = "middle"; dx = 0
        if name == "Hà Giang": dy = -8
        if name == "Sapa": an = "end"; dx = -10; dy = -4
        if name == "Hạ Long": dy = -30
        p.append(_t(x + dx, y + dy, _esc(name), 11, C["ink"], an, fam=BODY))
        p.append(_t(x + dx, y + dy + 13, t1, 9, C["accent"] if name!="Hà Giang" else C["soft"], an, ls="0.5"))
        p.append(_t(x + dx, y + dy + 25, t2, 9, C["muted"], an, fam=BODY))
    cx, cy = f(*GEO["Cát Bà"])
    p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.8" fill="{C["soft"]}"/>')
    p.append(_t(cx + 7, cy + 14, "Cát Bà · Lan Hạ", 8, C["soft"], fam=BODY))
    p.append(f'<circle cx="{HX:.1f}" cy="{HY:.1f}" r="8" fill="{C["deep"]}"/>')
    p.append(_t(HX - 14, HY + 4, "Hanoi", 12, C["ink"], "end", fam=BODY))
    nx, ny = f(*GEO["Nội Bài"])
    p.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="2.5" fill="{C["soft"]}"/>')
    p.append(_t(nx + 6, ny - 4, "Nội Bài · 45–60 min", 7.5, C["soft"], fam=BODY))
    p.append(_t(14, h - 12, "FROM COORDINATES · SOLID: THE THREE EXCURSIONS THAT COMPETE FOR A 4–5 DAY NORTHERN LEG", 7, C["soft"], ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_centre():
    """Huế, the pass, Đà Nẵng, Hội An, the beach, Mỹ Sơn: the three bases and
    their minutes, from coordinates."""
    h = 350
    keys = ("Huế","Lăng Cô","Đà Nẵng","Hội An","An Bàng","Mỹ Sơn")
    f = _proj([GEO[k] for k in keys], W, h - 40, 64)
    p = _svg(h)
    route = ["Huế","Lăng Cô","Đà Nẵng","Hội An"]
    pts = " ".join(f"{f(*GEO[k])[0]:.1f},{f(*GEO[k])[1]:.1f}" for k in route)
    p.append(f'<polyline points="{pts}" fill="none" stroke="{C["ink"]}" stroke-width="2" stroke-linejoin="round"/>')
    for a, b in (("Hội An","An Bàng"),("Hội An","Mỹ Sơn")):
        (x1,y1),(x2,y2) = f(*GEO[a]), f(*GEO[b])
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{C["soft"]}" stroke-dasharray="3 3"/>')
    labs = {"Huế": ("the Imperial City · 2 nights", "end", -10, 4),
            "Lăng Cô": ("Hải Vân Pass · train below the road, ~3 h Huế–Đà Nẵng", "end", -10, -8),
            "Đà Nẵng": ("city, airport, long beach", "start", 12, -14),
            "Hội An": ("Ancient Town · walk to everything", "start", 10, 14),
            "An Bàng": ("beach · 10–15 min by bicycle from the town", "end", -12, -6),
            "Mỹ Sơn": ("Mỹ Sơn · ~1 h west, go at opening", "end", -10, 14)}
    for k in keys:
        x, y = f(*GEO[k])
        big = k in ("Huế","Đà Nẵng","Hội An")
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if big else 3.2}" fill="{C["paper"] if not big else C["deep"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
        txt, an, dx, dy = labs[k]
        nm = k if k != "Lăng Cô" else ""
        if nm: p.append(_t(x + dx, y + dy, _esc(nm), 11, C["ink"], an, fam=BODY))
        p.append(_t(x + dx, y + dy + (13 if nm else 0), _esc(txt), 9, C["muted"], an, fam=BODY))
    # the minutes, stated
    d_hd = km("Hội An", "Đà Nẵng")
    p.append(_t(14, h - 28, f'HỘI AN ↔ ĐÀ NẴNG {d_hd:.0f} KM · ~45 MIN BY CAR · A DAY-TRIP BASE COSTS ~1.5 H ON THE ROAD PER VISIT', 9, C["accent"], ls="0.3"))
    p.append(_t(14, h - 12, "HỘI AN HAS NO AIRPORT AND NO STATION · EVERY VERSION OF THIS LEG PASSES THROUGH ĐÀ NẴNG", 9, C["soft"], ls="0.3"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_south():
    """The last block: what each ending costs in days, drawn to the same scale."""
    rows = [("Extra days in Saigon", 0, 0, "cost only themselves; Chợ Lớn, District 4, Củ Chi"),
            ("Mekong, Cần Thơ overnight", 2, 0, "the only version that is at Cái Răng while it runs"),
            ("Phú Quốc", 3, 1, "a flight each way; three or four nights to be worth it"),
            ("Côn Đảo", 4, 1, "thin flight schedule; three or four nights minimum"),
            ("Cambodia by river, Châu Đốc", 2, 0, "Cần Thơ → Châu Đốc → the boat; needs the visa's exit port")]
    rh, top = 40, 30
    h = top + rh * len(rows) + 44
    L, R = 220, 16
    unit = (W - L - R) / 6.0
    p = _svg(h)
    p.append(_t(L, 16, "DAYS THE BLOCK MUST ABSORB", 8, C["jade"], ls="2"))
    for i, (lab, days, fl, note) in enumerate(rows):
        y = top + i * rh
        p.append(_t(0, y + 13, _esc(lab), 10, C["ink"], fam=BODY))
        p.append(_t(0, y + 25, _esc(note), 7, C["soft"]))
        if days:
            p.append(f'<rect x="{L}" y="{y}" width="{days*unit:.1f}" height="18" fill="{C["accent"]}" opacity="0.85"/>')
            if fl:
                p.append(f'<rect x="{L+days*unit:.1f}" y="{y}" width="{fl*unit:.1f}" height="18" fill="{C["gilt"]}" opacity="0.9"/>')
            p.append(_t(L + (days + fl) * unit + 6, y + 13, f'{days}{"–"+str(days+1) if fl else ""} days', 8.5, C["muted"]))
        else:
            p.append(_t(L + 6, y + 13, "0 — nothing to absorb", 8.5, C["muted"]))
    p.append(f'<rect x="{L}" y="{h-18}" width="9" height="9" fill="{C["accent"]}" opacity="0.85"/>')
    p.append(_t(L + 13, h - 10, "ON THE GROUND", 7, C["muted"], ls="1"))
    p.append(f'<rect x="{L+120}" y="{h-18}" width="9" height="9" fill="{C["gilt"]}"/>')
    p.append(_t(L + 133, h - 10, "SPARE DAY FOR A THIN FLIGHT", 7, C["muted"], ls="1"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_beach():
    """Which beach is dry when. Five coasts, one strip each."""
    coasts = [("CENTRAL COAST · An Bàng, Đà Nẵng", [1,2,2,2,2,2,2,2,0,0,0,1]),
              ("NHA TRANG", [2,2,2,2,2,2,2,2,0,0,0,0]),
              ("PHÚ QUỐC", [2,2,2,2,0,0,0,0,0,0,2,2]),
              ("CÔN ĐẢO", [0,0,2,2,2,2,2,2,2,0,0,0]),
              ("MŨI NÉ · wind, not swimming", [2,2,2,2,1,1,1,1,1,1,2,2])]
    L, R, T = 215, 14, 36
    rh = 30
    h = T + rh * len(coasts) + 62
    cw = (W - L - R) / 12.0
    p = _svg(h)
    for i, m in enumerate(MONTHS):
        p.append(_t(L + i*cw + cw/2, T - 12, m, 8, C["muted"], "middle"))
    for ri, (name, vals) in enumerate(coasts):
        y = T + ri * rh
        p.append(_t(L - 8, y + 14, _esc(name), 7.5, C["ink"], "end", ls="0.5"))
        for i, v in enumerate(vals):
            x = L + i * cw
            p.append(f'<rect x="{x+1:.1f}" y="{y+2}" width="{cw-2:.1f}" height="20" fill="{SCOL[v]}" opacity="{SOPA[v]}" rx="1"/>')
    ly = T + rh * len(coasts) + 8
    for i, (v, lab) in enumerate(((2, "CALM AND RELIABLE"), (1, "WORKABLE"), (0, "ROUGH OR STORMS"))):
        x = L + i * 140
        p.append(f'<rect x="{x}" y="{ly}" width="12" height="10" fill="{SCOL[v]}" opacity="{SOPA[v]}"/>')
        p.append(_t(x + 16, ly + 9, lab, 7, C["muted"], ls="1"))
    p.append(_t(14, ly + 28, "SEP–OCT: NO COAST IS RELIABLE · NOV–DEC: ONLY PHÚ QUỐC · MAY–AUG: NOT PHÚ QUỐC", 9, C["accent"], ls="0.3"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_tet():
    """Tết 2027 on a calendar: the official week, and the fortnight of
    disruption either side of it that the corpus describes."""
    h = 228
    L, R, T = 40, 20, 50
    days = 42  # 24 Jan – 6 Mar 2027 (a Sunday-start grid is not needed; a strip is)
    import datetime as _d
    start = _d.date(2027, 1, 24)
    dw = (W - L - R) / days
    p = _svg(h)
    for i in range(days):
        d = start + _d.timedelta(days=i)
        x = L + i * dw
        p.append(f'<rect x="{x:.1f}" y="{T}" width="{dw-1:.1f}" height="30" fill="{C["panel"]}"/>')
        if d.day == 1 or i == 0:
            p.append(_t(x + 2, T - 8, d.strftime("%b").upper(), 8, C["muted"], ls="1"))
        if d.day in (1, 10, 20, 28) or d == _d.date(2027,2,6):
            p.append(_t(x + dw/2, T + 44, str(d.day), 7, C["soft"], "middle"))
    def X(date): return L + (date - start).days * dw
    # the surge: a week either side of the official holiday (corpus: "roughly a week either side")
    p.append(f'<rect x="{X(_d.date(2027,1,28)):.1f}" y="{T}" width="{X(_d.date(2027,2,18))-X(_d.date(2027,1,28)):.1f}" height="30" fill="{C["gilt"]}" opacity="0.5"/>')
    # the official holiday 4–10 Feb
    p.append(f'<rect x="{X(_d.date(2027,2,4)):.1f}" y="{T}" width="{X(_d.date(2027,2,11))-X(_d.date(2027,2,4)):.1f}" height="30" fill="{C["accent"]}" opacity="0.85"/>')
    tx = X(_d.date(2027,2,6)) + dw/2
    p.append(f'<line x1="{tx:.1f}" y1="{T-4}" x2="{tx:.1f}" y2="{T+34}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    p.append(_t(tx, T - 16, "TẾT · 6 FEB 2027", 8.5, C["ink"], "middle", ls="1"))
    p.append(_t(X(_d.date(2027,2,4)), T + 62, "OFFICIAL HOLIDAY 4–10 FEB", 7.5, C["accent"], ls="1"))
    p.append(_t(X(_d.date(2027,1,28)), T + 76, "THE TRAVEL SURGE RUNS ABOUT A WEEK EITHER SIDE: SEATS GO, FAMILY KITCHENS CLOSE, ATMS EMPTY", 7.5, C["muted"], ls="0.5"))
    p.append(_t(L, h - 26, "THE DATE MOVES WITH THE LUNAR CALENDAR · 2027 IS DRAWN; CHECK YOUR OWN YEAR", 9, C["soft"], ls="0.3"))
    p.append(_t(L, h - 12, "THE OFFICIAL SPAN IS SET BY GOVERNMENT ANNOUNCEMENT EACH YEAR", 9, C["soft"], ls="0.3"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_cash():
    """Where a card works and where it stops: the corpus names four cities.
    Everything else on the line is cash."""
    h = 256
    p = _svg(h)
    items = [("Hanoi", True), ("Sapa valley", False), ("Hạ Long boat bar", False), ("Ninh Bình", False),
             ("Huế", False), ("Đà Nẵng", True), ("Hội An", True), ("Nha Trang", False),
             ("Saigon", True), ("the delta", False), ("Phú Quốc resorts", False)]
    n = len(items); L, R = 20, 20
    sw = (W - L - R) / n
    y = 70
    p.append(f'<line x1="{L}" y1="{y}" x2="{W-R}" y2="{y}" stroke="{C["ink"]}" stroke-width="2"/>')
    for i, (name, card) in enumerate(items):
        x = L + i * sw + sw / 2
        col = C["jade"] if card else C["accent"]
        p.append(f'<circle cx="{x:.1f}" cy="{y}" r="{7 if card else 4}" fill="{col}"/>')
        p.append(_t(x, y + (26 if i % 2 == 0 else 40), _esc(name), 8.5, C["ink"], "middle", fam=BODY))
    p.append(_t(L, 30, "WHERE A FOREIGN CARD RELIABLY WORKS (HOTELS, CHAINS, MID-TO-UPPER RESTAURANTS)", 7.5, C["jade"], ls="1"))
    p.append(_t(L, 44, "EVERYWHERE ELSE ON THE LINE — AND EVERYTHING SMALL INSIDE THE FOUR CITIES — IS CASH", 7.5, C["accent"], ls="1"))
    # the ATM arithmetic as three bars: fee share at three withdrawal sizes (structure only, no figure)
    y2 = 148
    p.append(_t(L, y2 - 14, "THE ATM RULE, WITHOUT A NUMBER: A FLAT FEE DIVIDED BY WHAT YOU TAKE · BARS: FEES PAID, RELATIVE", 9, C["muted"], ls="0.3"))
    for i, (lab, frac) in enumerate((("five small withdrawals", 1.0), ("two medium", 0.4), ("one at the machine's cap", 0.2))):
        yy = y2 + i * 22
        p.append(_t(L, yy + 11, lab, 8.5, C["ink"], fam=BODY))
        p.append(f'<rect x="{L+200}" y="{yy}" width="{frac*380:.1f}" height="14" fill="{C["accent"]}" opacity="{0.85 - i*0.25}"/>')
        pass
    p.append(_t(L, h - 24, "THE FEE IS FLAT AND THE CAP IS LOW, SO THE COST PER DOLLAR IS SET BY HOW MUCH YOU TAKE AT ONCE", 9, C["soft"], ls="0.3"))
    p.append(_t(L, h - 10, "NO BANK'S TARIFF IS PRINTED HERE, ON PURPOSE", 9, C["soft"], ls="0.3"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_arrival():
    """The calendar day that goes missing, and what each airport costs on the
    way in. Depart Monday evening; land Wednesday morning."""
    h = 262
    p = _svg(h)
    L, R, T = 60, 20, 46
    span = W - L - R
    # 60 hours from Monday 18:00 EST
    def X(hr): return L + span * hr / 60.0
    for hr, lab in ((0, "MON 18:00"), (12, "TUE 06:00"), (24, "TUE 18:00"), (36, "WED 06:00"), (48, "WED 18:00"), (60, "THU 06:00")):
        p.append(f'<line x1="{X(hr):.1f}" y1="{T-6}" x2="{X(hr):.1f}" y2="{T+70}" stroke="{C["line"]}"/>')
        p.append(_t(X(hr), T - 12, lab, 9, C["muted"], "end" if hr == 60 else ("start" if hr == 0 else "middle")))
    p.append(_t(L, T + 8, "US EAST COAST CLOCK", 7, C["soft"], ls="1.5"))
    # the journey: 24h door to door, departs Mon 18:00 EST, lands Tue 18:00 EST = Wed 06:00 ICT (+12)
    p.append(f'<rect x="{X(0):.1f}" y="{T+14}" width="{X(24)-X(0):.1f}" height="16" fill="{C["ink"]}" opacity="0.85"/>')
    p.append(_t(X(12), T + 25, "22–26 H DOOR TO DOOR, ONE STOP", 7.5, C["paper"], "middle", ls="1"))
    p.append(_t(L, T + 48, "VIETNAM CLOCK (+12 H IN WINTER, +11 IN SUMMER)", 7, C["soft"], ls="1.5"))
    p.append(f'<rect x="{X(24):.1f}" y="{T+54}" width="{X(36)-X(24):.1f}" height="16" fill="{C["gilt"]}" opacity="0.9"/>')
    p.append(_t(X(30), T + 65, "WED MORNING: ARRIVAL DAY, WRITTEN OFF", 7.5, C["ink"], "middle", ls="0.8"))
    p.append(_t(X(24), T + 86, "YOU LEFT ON MONDAY; IT IS WEDNESDAY. THE DAY WENT INTO THE CROSSING.", 7.5, C["accent"], ls="0.5"))
    # airports
    y0 = T + 112
    p.append(_t(L, y0 - 4, "FROM THE GATE TO THE FIRST BED", 8, C["jade"], ls="2"))
    rows = [("Nội Bài · Hanoi", 16, 60, "45–60 min · Grab, or the 86 bus"),
            ("Tân Sơn Nhất · Saigon", 4, 50, "30–50 min · Grab pickup is upstairs, not at arrivals"),
            ("Đà Nẵng", 2, 15, "minutes to the city · ~45–60 min on to Hội An")]
    for i, (name, mi, mins, note) in enumerate(rows):
        yy = y0 + 10 + i * 26
        p.append(_t(L, yy + 11, _esc(name), 9.5, C["ink"], fam=BODY))
        p.append(f'<rect x="{L+150}" y="{yy}" width="{mins*1.6:.1f}" height="14" fill="{C["accent"]}" opacity="0.8"/>')
        p.append(_t(L + 150 + mins * 1.6 + 6, yy + 11, _esc(f"{mi} mi · {note}"), 7.5, C["muted"]))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_cities():
    """Two cities, where to sleep: the areas from real coordinates, scored by
    minutes to the core. Walk minutes = crow-flies km × 1.25 street factor at 4.5 km/h."""
    h = 316
    p = _svg(h)
    def walk(a, b):
        R = 6371; pp = math.pi / 180
        (la1,lo1),(la2,lo2) = a, b
        dx = (lo2-lo1)*pp*math.cos((la1+la2)*pp/2); dy = (la2-la1)*pp
        return round(R*math.hypot(dx,dy)*1.25/4.5*60)
    HANOI = {"Hoàn Kiếm": (21.0287,105.8524), "Old Quarter": (21.0345,105.8500), "French Quarter": (21.0240,105.8560),
             "Ba Đình": (21.0370,105.8340), "Tây Hồ": (21.0650,105.8230), "Long Biên": (21.0450,105.8700)}
    HCMC = {"Bến Thành": (10.7725,106.6980), "Dong Khoi": (10.7780,106.7030), "District 3": (10.7830,106.6870),
            "Phạm Ngũ Lão": (10.7680,106.6930), "District 4": (10.7640,106.7040), "Thảo Điền": (10.8050,106.7350), "Chợ Lớn": (10.7520,106.6520)}
    for ci, (title, core, pts) in enumerate((("HANOI · MINUTES ON FOOT TO HOÀN KIẾM", "Hoàn Kiếm", HANOI), ("SAIGON · MINUTES ON FOOT TO BẾN THÀNH", "Bến Thành", HCMC))):
        ox = ci * 326
        f = _proj(list(pts.values()), 326, h - 30, 48)
        p.append(_t(ox + 14, 20, title, 7.5, C["jade"], ls="1.5"))
        cx, cy = f(*pts[core]); cx += ox; cy += 24
        for r in (60, 110):
            p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="none" stroke="{C["line"]}" stroke-dasharray="3 3"/>')
        for name, ll in pts.items():
            x, y = f(*ll); x += ox; y += 24
            m = walk(pts[core], ll)
            if name == core:
                p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{C["deep"]}"/>')
                p.append(_t(x + 9, y + 4, _esc(name), 9, C["ink"], fam=BODY))
                continue
            col = C["jade"] if m <= 20 else (C["gilt"] if m <= 40 else C["accent"])
            p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{col}"/>')
            an = "start" if x > cx else "end"; dx = 8 if an == "start" else -8
            if x - ox < 70: an = "start"; dx = 8
            if x - ox > 256: an = "end"; dx = -8
            p.append(_t(x + dx, y + 3, _esc(f"{name} · {m}′"), 8.5, C["ink"], an, fam=BODY))
    p.append(f'<line x1="326" y1="10" x2="326" y2="{h-10}" stroke="{C["line"]}"/>')
    p.append(_t(14, h - 8, "GREEN ≤ 20 MIN · GOLD ≤ 40 · RED: A GRAB EVERY TIME · MINUTES AT 4.5 KM/H, STREET FACTOR 1.25", 7, C["soft"], ls="0.6"))
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_road():
    """Who carries the risk on each way of covering a road: legal × the legs it
    can cover, as a matrix."""
    h = 262
    p = _svg(h)
    cols = ["LEGAL?", "INSURER", "CITY", "HẢI VÂN", "HÀ GIANG", "LONG LEGS"]
    rows = [("Ride a rented bike yourself", ["NO", "YES", "–", "–", "–", "–"]),
            ("Pillion with an easy-rider", ["yes", "no", "·", "●", "●", "–"]),
            ("Car with a driver", ["yes", "no", "·", "●", "●", "slow"]),
            ("Grab (bike or car)", ["yes", "no", "●", "–", "–", "–"]),
            ("Train", ["yes", "no", "–", "●", "–", "●"]),
            ("Fly", ["yes", "no", "–", "–", "–", "●"])]
    L = 200; cw = (W - L) / len(cols); rh = 26; T = 44
    for j, c in enumerate(cols):
        p.append(_t(L + j * cw + cw/2, T - 10, c, 6.5, C["muted"], "middle", ls="0.5"))
    for i, (name, cells) in enumerate(rows):
        y = T + i * rh
        p.append(f'<line x1="0" y1="{y+rh-4}" x2="{W}" y2="{y+rh-4}" stroke="{C["line"]}"/>')
        p.append(_t(0, y + 14, _esc(name), 9.5, C["ink"] if i else C["deep"], fam=BODY))
        for j, v in enumerate(cells):
            x = L + j * cw + cw / 2
            if v == "●":
                p.append(f'<circle cx="{x:.1f}" cy="{y+10}" r="5" fill="{C["jade"]}"/>')
            elif v == "·":
                p.append(f'<circle cx="{x:.1f}" cy="{y+10}" r="3" fill="{C["gilt"]}"/>')
            elif v == "–":
                p.append(_t(x, y + 14, "–", 10, C["soft"], "middle"))
            else:
                col = C["accent"] if v in ("NO", "YES") else C["muted"]
                p.append(_t(x, y + 14, v, 8.5 if v in ("NO","YES") else 8, col, "middle", ls="1" if v in ("NO","YES") else None))
    p.append(_t(0, h - 38, "● COVERS IT WELL · COVERS IT – NOT THE TOOL · INSURER: MAY REFUSE THE BILL AFTER A CRASH", 9, C["soft"], ls="0.3"))
    p.append(_t(0, h - 24, "ONLY THE FIRST ROW IS THE ONE THE STATE DEPARTMENT CALLS ILLEGAL", 9, C["soft"], ls="0.3"))
    p.append(_t(0, h - 10, "EVERY LEG OF A FIRST TRIP IS REACHABLE WITHOUT THE FIRST ROW", 9, C["accent"], ls="0.3"))
    p.append('</svg>')
    return "".join(p)


# ── the registry build3.py reads ────────────────────────────────────────────
FIGURES = {
 "line":    (fig_line,    "The country as the line it is, drawn from coordinates, with the three climates beside it. No month is in season at both ends."),
 "season":  (fig_season,  "Five regions by month, with the three holiday spikes that sell out the seats. Tết is drawn for 2027."),
 "days":    (fig_days,    "Where the days go. Two to the crossing, one to arriving, half a day to every move: the green is the trip."),
 "visa":    (fig_visa,    "The four binding fields on the e-visa form, and what each one locks before the route exists."),
 "road":    (fig_road,    "Six ways to cover a road, scored on legality, the insurer, and which legs each one reaches."),
 "legs":    (fig_legs,    "The long legs: distance against hours door to door, by mode, with the corpus's 150- and 500-mile lines."),
 "north":   (fig_north,   "Hanoi's three spokes and the road hours each one costs. They compete for the same four or five days."),
 "centre":  (fig_centre,  "Huế, the pass, Đà Nẵng, Hội An and the beach, from coordinates. The base decides how often you drive this."),
 "south":   (fig_south,   "The last block: what each ending costs in days, to one scale. Only the city costs nothing to absorb."),
 "beach":   (fig_beach,   "Five coasts and the months their sea is calm. Phú Quốc and Nha Trang run opposite to each other."),
 "tet":     (fig_tet,     "Tết 2027 on the calendar: the official week, and the fortnight of disruption either side of it."),
 "cash":    (fig_cash,    "Where a foreign card reliably works, and the ATM rule that follows from a flat fee and a low cap."),
 "arrival": (fig_arrival, "The calendar day that goes into the crossing, and what each airport costs between the gate and the first bed."),
 "cities":  (fig_cities,  "Two cities, where to sleep: the areas from coordinates, scored by minutes on foot to the core."),
}
