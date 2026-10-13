# maps.py — every vector figure, drawn from REAL numbers and REAL coordinates.
# Geography and fares are public facts; drawing our own figure from them is fine
# (SKILL non-negotiable 6). No stock art, no platform map tiles.
#
# viewBox note (bug log #8): a figure that renders small is almost always the
# viewBox, not the CSS. The body column is 652px (816 − 2×82), so figures are
# authored at 652 wide and scale to width:100%.
# ─────────────────────────────────────────────────────────────────────────────
import math

C = {
 "ink":"#242A33", "accent":"#1B3670", "gilt":"#B89547", "muted":"#5C6068",
 "line":"#E1D7C2", "panel":"#EAE2D0", "deep":"#16305F", "paper":"#F5EFE1",
 "sakura":"#C87F94", "water":"#CBD6E0", "soft":"#8A8E97",
}
W = 652
MONO = "'IBM Plex Mono',monospace"
DISP = "'Zen Old Mincho',serif"

# ── real coordinates (lat, lon) ──────────────────────────────────────────────
GEO = {
 "Tokyo":      (35.6812, 139.7671),
 "Kyoto":      (34.9858, 135.7588),
 "Shin-Osaka": (34.7332, 135.5003),
 "Nara":       (34.6796, 135.8180),
 "Hakone":     (35.2324, 139.1069),
 "Nikko":      (36.7198, 139.6982),
 "Kamakura":   (35.3192, 139.5468),
 "Hiroshima":  (34.3975, 132.4753),
 "Narita":     (35.7719, 140.3928),
 "Haneda":     (35.5494, 139.7798),
}

# Yamanote loop — real station coordinates, in running order
YAMANOTE = [
 ("Tokyo",      35.6812, 139.7671),
 ("Akihabara",  35.6984, 139.7731),
 ("Ueno",       35.7141, 139.7774),
 ("Ikebukuro",  35.7295, 139.7109),
 ("Shinjuku",   35.6896, 139.7006),
 ("Shibuya",    35.6580, 139.7016),
 ("Shinagawa",  35.6285, 139.7387),
 ("Shimbashi",  35.6665, 139.7583),
]


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


# ═════════════════════════════════════════════════════════════════════════════
def fig_breakeven():
    """THE figure. Cumulative point-to-point fares vs the flat pass price.
    Real numbers: ¥13,850 per Tokyo–Kyoto-length leg, ¥50,000 for the 7-day pass."""
    h = 300
    L, R, T, B = 58, 22, 24, 46
    fare, passp, nmax = 13850, 50000, 6
    ymax = 90000
    def X(n): return L + (W - L - R) * n / nmax
    def Y(v): return T + (h - T - B) * (1 - v / ymax)
    cross = passp / fare                       # 3.61 legs

    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    # y grid
    for v in range(0, ymax + 1, 15000):
        y = Y(v)
        p.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{C["line"]}" stroke-width="1"/>')
        p.append(f'<text x="{L-8}" y="{y+3:.1f}" font-size="8.5" fill="{C["muted"]}" text-anchor="end">'
                 f'&#165;{v//1000}k</text>')
    # x ticks
    for n in range(nmax + 1):
        p.append(f'<text x="{X(n):.1f}" y="{h-B+16}" font-size="8.5" fill="{C["muted"]}" '
                 f'text-anchor="middle">{n}</text>')
    p.append(f'<text x="{(L+W-R)/2:.1f}" y="{h-B+33}" font-size="8" fill="{C["soft"]}" '
             f'text-anchor="middle" letter-spacing="1.6">LONG JOURNEYS IN A SEVEN-DAY WINDOW</text>')

    # the pass — flat line
    p.append(f'<line x1="{L}" y1="{Y(passp):.1f}" x2="{W-R}" y2="{Y(passp):.1f}" '
             f'stroke="{C["gilt"]}" stroke-width="2.2"/>')
    p.append(f'<text x="{W-R-4}" y="{Y(passp)-7:.1f}" font-size="8.5" fill="{C["gilt"]}" '
             f'text-anchor="end" letter-spacing="1.2">THE PASS &#8212; &#165;50,000 FLAT</text>')
    # pay-as-you-go — cumulative
    pts = " ".join(f"{X(n):.1f},{Y(fare*n):.1f}" for n in range(nmax + 1))
    p.append(f'<polyline points="{pts}" fill="none" stroke="{C["accent"]}" stroke-width="2.2"/>')
    for n in range(nmax + 1):
        p.append(f'<circle cx="{X(n):.1f}" cy="{Y(fare*n):.1f}" r="2.6" fill="{C["accent"]}"/>')
    p.append(f'<text x="{X(4.6):.1f}" y="{Y(fare*6)-14:.1f}" font-size="8.5" fill="{C["accent"]}" '
             f'letter-spacing="1.2">PAY PER JOURNEY</text>')

    # the crossing
    p.append(f'<line x1="{X(cross):.1f}" y1="{T}" x2="{X(cross):.1f}" y2="{h-B}" '
             f'stroke="{C["ink"]}" stroke-width="1" stroke-dasharray="3 3"/>')
    p.append(f'<circle cx="{X(cross):.1f}" cy="{Y(passp):.1f}" r="4.4" fill="{C["paper"]}" '
             f'stroke="{C["ink"]}" stroke-width="1.6"/>')
    p.append(f'<text x="{X(cross)+8:.1f}" y="{Y(passp)+17:.1f}" font-size="9" fill="{C["ink"]}" '
             f'letter-spacing="1.2">BREAK-EVEN &#8776; 3.6</text>')

    # where the classic trip sits
    p.append(f'<rect x="{X(0):.1f}" y="{T}" width="{X(2)-X(0):.1f}" height="{h-B-T}" '
             f'fill="{C["accent"]}" opacity="0.055"/>')
    p.append(f'<text x="{X(1):.1f}" y="{T+15}" font-size="8.5" fill="{C["accent"]}" '
             f'text-anchor="middle" letter-spacing="1.2">THE CLASSIC FIRST TRIP</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_corridor():
    """The route graph: two hubs, one long leg, day-trip spokes. Real coordinates,
    real journey times."""
    h = 330
    f = _proj([GEO[k] for k in ("Tokyo","Kyoto","Nara","Hakone","Nikko","Kamakura","Hiroshima")],
              W, h, 62)
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')

    TX, TY = f(*GEO["Tokyo"]); KX, KY = f(*GEO["Kyoto"])
    # the one long leg
    p.append(f'<line x1="{KX:.1f}" y1="{KY:.1f}" x2="{TX:.1f}" y2="{TY:.1f}" '
             f'stroke="{C["accent"]}" stroke-width="3"/>')
    mx, my = (TX + KX) / 2, (TY + KY) / 2
    p.append(f'<rect x="{mx-52:.1f}" y="{my-9:.1f}" width="104" height="18" fill="{C["paper"]}"/>')
    p.append(f'<text x="{mx:.1f}" y="{my+3:.1f}" font-size="8.5" fill="{C["accent"]}" '
             f'text-anchor="middle" letter-spacing="1.1">2H15 &#183; &#165;13,850</text>')

    spokes = [("Nikko","Tokyo","2h"), ("Hakone","Tokyo","1h30"),
              ("Kamakura","Tokyo","1h"), ("Nara","Kyoto","45m")]
    for a, hub, t in spokes:
        ax, ay = f(*GEO[a]); hx, hy = f(*GEO[hub])
        p.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{ax:.1f}" y2="{ay:.1f}" '
                 f'stroke="{C["soft"]}" stroke-width="1.2" stroke-dasharray="4 3"/>')
        p.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="3.4" fill="{C["paper"]}" '
                 f'stroke="{C["muted"]}" stroke-width="1.4"/>')
        dy = -9 if ay < hy else 15
        p.append(f'<text x="{ax:.1f}" y="{ay+dy:.1f}" font-size="9" fill="{C["muted"]}" '
                 f'text-anchor="middle">{a} <tspan fill="{C["soft"]}">{t}</tspan></text>')

    for nm, col in (("Tokyo", C["deep"]), ("Kyoto", C["deep"])):
        x, y = f(*GEO[nm])
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{col}"/>')
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="none" stroke="{col}" '
                 f'stroke-width="1" opacity=".45"/>')
        p.append(f'<text x="{x:.1f}" y="{y-20:.1f}" font-size="12" fill="{C["ink"]}" '
                 f'text-anchor="middle" font-family="{DISP}">{nm}</text>')

    p.append(f'<text x="14" y="{h-14}" font-size="8" fill="{C["soft"]}" letter-spacing="1.6">'
             f'SOLID: THE ONE LONG LEG &#183; DASHED: DAY TRIPS, ON LOCAL LINES</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_days():
    """Where the days actually go — the day-trip substitution, as bars."""
    rows = [("5 days, no day trips", 4, 0), ("5 days, one day trip", 3, 1),
            ("5 days, three day trips", 2, 3), ("10 days, two day trips", 7, 2)]
    rh, top = 40, 34
    h = top + rh * len(rows) + 30
    L, R = 172, 22
    unit = (W - L - R) / 10.0
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    p.append(f'<text x="{L}" y="18" font-size="8" fill="{C["accent"]}" letter-spacing="1.6">'
             f'DAYS IN THE CITIES YOU FLEW FOR</text>')
    p.append(f'<text x="{W-R}" y="18" font-size="8" fill="{C["soft"]}" letter-spacing="1.6" '
             f'text-anchor="end">DAYS SPENT TRAVELLING OUT</text>')
    for i, (lab, keep, out) in enumerate(rows):
        y = top + i * rh
        p.append(f'<text x="0" y="{y+16:.1f}" font-size="10" fill="{C["ink"]}">{_esc(lab)}</text>')
        p.append(f'<rect x="{L}" y="{y:.1f}" width="{keep*unit:.1f}" height="20" '
                 f'fill="{C["accent"]}" opacity="0.86"/>')
        p.append(f'<rect x="{L+keep*unit:.1f}" y="{y:.1f}" width="{out*unit:.1f}" height="20" '
                 f'fill="{C["sakura"]}" opacity="0.8"/>')
        p.append(f'<text x="{L+keep*unit-6:.1f}" y="{y+14:.1f}" font-size="9.5" fill="{C["paper"]}" '
                 f'text-anchor="end">{keep}</text>')
        if out:
            p.append(f'<text x="{L+(keep+out)*unit-6:.1f}" y="{y+14:.1f}" font-size="9.5" '
                     f'fill="{C["paper"]}" text-anchor="end">{out}</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_season():
    """The year as a strip: what each window asks of you."""
    months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    h = 214
    L, R, T = 18, 18, 46
    cw = (W - L - R) / 12.0
    bands = [
        # label, start-month-index(+frac), width in months, colour, row
        ("BLOOM &#183; book ~6 months out", 2.6, 1.0, C["sakura"], 0),
        ("GOLDEN WEEK &#183; do not move cities", 3.9, 0.35, C["gilt"], 1),
        ("RAINY SEASON", 5.0, 1.5, C["water"], 2),
        ("OBON &#183; do not move cities", 7.4, 0.25, C["gilt"], 1),
        ("FOLIAGE &#183; book 2&#8211;3 months out", 10.4, 0.8, C["accent"], 0),
        ("LOW SEASON &#183; cheapest, clearest", 0.0, 2.0, C["deep"], 3),
    ]
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    for i, m in enumerate(months):
        x = L + i * cw
        p.append(f'<line x1="{x:.1f}" y1="{T-10}" x2="{x:.1f}" y2="{h-26}" stroke="{C["line"]}" '
                 f'stroke-width="1"/>')
        p.append(f'<text x="{x+cw/2:.1f}" y="{T-16}" font-size="8.5" fill="{C["muted"]}" '
                 f'text-anchor="middle">{m}</text>')
    p.append(f'<line x1="{W-R:.1f}" y1="{T-10}" x2="{W-R:.1f}" y2="{h-26}" stroke="{C["line"]}"/>')
    rowh = 30
    for lab, start, width, col, row in bands:
        x = L + start * cw; w = width * cw; y = T + row * rowh
        p.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="17" fill="{col}" '
                 f'opacity="0.92" rx="1.5"/>')
        tx = x + w + 7
        anchor = "start"
        if tx > W - R - 120:
            tx = x - 7; anchor = "end"
        p.append(f'<text x="{tx:.1f}" y="{y+12.5:.1f}" font-size="8.5" fill="{C["ink"]}" '
                 f'text-anchor="{anchor}">{lab}</text>')
    p.append(f'<text x="{L}" y="{h-8}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'BLOOM DATES SHIFT WITH THE WINTER &#8212; TREAT EVERY BAND AS A WINDOW, NOT A DATE</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_tokyo():
    """The Yamanote loop from real station coordinates — the line you sleep on."""
    h = 340
    pts = [(la, lo) for _, la, lo in YAMANOTE]
    f = _proj(pts, W, h, 78)
    xy = [f(la, lo) for _, la, lo in YAMANOTE]
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    ring = " ".join(f"{x:.1f},{y:.1f}" for x, y in xy)
    p.append(f'<polygon points="{ring}" fill="{C["accent"]}" opacity="0.05"/>')
    p.append(f'<polygon points="{ring}" fill="none" stroke="{C["accent"]}" stroke-width="2.6" '
             f'stroke-linejoin="round"/>')
    cx = sum(x for x, _ in xy) / len(xy); cy = sum(y for _, y in xy) / len(xy)
    for (nm, _, _), (x, y) in zip(YAMANOTE, xy):
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6" fill="{C["paper"]}" '
                 f'stroke="{C["deep"]}" stroke-width="2"/>')
        ang = math.atan2(y - cy, x - cx)
        lx = x + math.cos(ang) * 22; ly = y + math.sin(ang) * 22
        anchor = "start" if lx > x else "end"
        if abs(lx - x) < 6: anchor = "middle"
        p.append(f'<text x="{lx:.1f}" y="{ly+3:.1f}" font-size="9.5" fill="{C["ink"]}" '
                 f'text-anchor="{anchor}">{nm}</text>')
    p.append(f'<text x="{cx:.1f}" y="{cy-6:.1f}" font-size="11" fill="{C["muted"]}" '
             f'text-anchor="middle" font-family="{DISP}">the Yamanote loop</text>')
    p.append(f'<text x="{cx:.1f}" y="{cy+11:.1f}" font-size="8.5" fill="{C["soft"]}" '
             f'text-anchor="middle" letter-spacing="1.2">SLEEP ON IT</text>')
    p.append(f'<text x="14" y="{h-12}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'DRAWN FROM STATION COORDINATES &#183; SPACING IS GEOGRAPHIC, NOT SCHEMATIC</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_arrival():
    """Airport choice vs landing time — the variable that actually decides day one."""
    h = 226
    L, R, T = 92, 22, 40
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    hours = [(13, "13:00"), (16, "16:00"), (19, "19:00"), (22, "22:00")]
    span = (W - L - R)
    def X(hr): return L + span * (hr - 12) / 11.0
    for hr, lab in hours:
        p.append(f'<line x1="{X(hr):.1f}" y1="{T-8}" x2="{X(hr):.1f}" y2="{h-40}" '
                 f'stroke="{C["line"]}"/>')
        p.append(f'<text x="{X(hr):.1f}" y="{T-14}" font-size="8.5" fill="{C["muted"]}" '
                 f'text-anchor="middle">{lab}</text>')
    rows = [("HANEDA", 0.5, C["accent"], "~30 min in"), ("NARITA", 1.5, C["gilt"], "~60&#8211;90 min in")]
    for nm, ri, col, note in rows:
        y = T + ri * 52
        p.append(f'<text x="0" y="{y+13:.1f}" font-size="10" fill="{C["ink"]}">{nm}</text>')
        p.append(f'<text x="0" y="{y+26:.1f}" font-size="8" fill="{C["soft"]}">{note}</text>')
        # usable-evening bar shrinks with a later landing
        for hr in range(13, 23):
            frac = max(0.0, min(1.0, (21.0 - hr - (0.6 if nm == "NARITA" else 0.0)) / 8.0))
            if frac <= 0: continue
            bw = span / 11.0 * 0.82
            bh = 20 * frac
            p.append(f'<rect x="{X(hr)-bw/2:.1f}" y="{y+18-bh:.1f}" width="{bw:.1f}" '
                     f'height="{bh:.1f}" fill="{col}" opacity="0.8"/>')
    p.append(f'<text x="0" y="{h-14}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'BAR HEIGHT = USABLE EVENING LEFT AFTER THE TRANSFER &#183; LANDING TIME OUTRANKS AIRPORT</text>')
    p.append('</svg>')
    return "".join(p)


FIGURES = {
 "breakeven": (fig_breakeven, "The break-even, drawn. Pay-as-you-go against the flat pass price."),
 "corridor":  (fig_corridor,  "The corridor a first trip travels."),
 "days-ledger": (fig_days,    "What a day trip subtracts from the cities you flew for."),
 "season-grid": (fig_season,  "The year, and what each window asks of you."),
 "tokyo-lines": (fig_tokyo,   "The Yamanote loop, from station coordinates."),
 "arrival":   (fig_arrival,   "Usable evening remaining, by airport and landing time."),
}


# ═════════════════════════════════════════════════════════════════════════════
def fig_season_compare():
    """Spring against autumn on the four axes the decision actually turns on.
    Every value is stated in Decision 04 / the season corpus."""
    h = 250
    L, R, T = 150, 22, 44
    rows = [
        ("window it holds",      "about one week",      "several weeks",   0.18, 0.92),
        ("booking lead",         "~6 months",           "2-3 months",      0.95, 0.42),
        ("forecast before you book", "none until Feb",  "not needed",      0.10, 0.90),
        ("price",                "the year's peak",     "high, not peak",  0.95, 0.62),
    ]
    rh = 40
    colw = (W - L - R) / 2 - 14
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    p.append(f'<text x="{L}" y="{T-20}" font-size="9" fill="{C["sakura"]}" letter-spacing="2">SPRING &#183; BLOOM</text>')
    p.append(f'<text x="{L+colw+28}" y="{T-20}" font-size="9" fill="{C["accent"]}" letter-spacing="2">LATE AUTUMN</text>')
    for i, (lab, a, b, af, bf) in enumerate(rows):
        y = T + i * rh
        p.append(f'<text x="0" y="{y+11:.0f}" font-size="9.5" fill="{C["muted"]}">{_esc(lab)}</text>')
        for x0, txt, frac, col in ((L, a, af, C["sakura"]), (L+colw+28, b, bf, C["accent"])):
            p.append(f'<rect x="{x0}" y="{y+15:.0f}" width="{colw*frac:.0f}" height="5" fill="{col}" opacity=".85"/>')
            p.append(f'<rect x="{x0}" y="{y+15:.0f}" width="{colw:.0f}" height="5" fill="none" stroke="{C["line"]}"/>')
            p.append(f'<text x="{x0}" y="{y+11:.0f}" font-size="9.5" fill="{C["ink"]}">{_esc(txt)}</text>')
    p.append(f'<text x="0" y="{h-10}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'BAR LENGTH = HOW MUCH THE SEASON ASKS OF YOU &#183; SHORTER IS EASIER TO PLAN</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
KYOTO = {
 "Kyoto Station":(34.9858,135.7588), "Kinkaku-ji":(35.0394,135.7292),
 "Ginkaku-ji":(35.0270,135.7982), "Kiyomizu-dera":(34.9949,135.7851),
 "Fushimi Inari":(34.9671,135.7727), "Arashiyama":(35.0094,135.6668),
 "Nijo Castle":(35.0142,135.7481), "Gion":(35.0037,135.7752),
}

def fig_kyoto():
    """Why Kyoto is a bus city: the two subway lines against where the sights are.
    Real coordinates; the subway lines are drawn on their real axes."""
    h = 320
    f = _proj(list(KYOTO.values()), W, h, 76)
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    # Karasuma line: north-south, through Kyoto Station's longitude
    ksx, _ = f(35.0, 135.7588)
    p.append(f'<line x1="{ksx:.1f}" y1="34" x2="{ksx:.1f}" y2="{h-46}" stroke="{C["accent"]}" stroke-width="3"/>')
    p.append(f'<text x="{ksx+7:.1f}" y="46" font-size="8.5" fill="{C["accent"]}" letter-spacing="1.2">KARASUMA LINE</text>')
    # Tozai line: east-west, on its real latitude
    _, tzy = f(35.0110, 135.76)
    p.append(f'<line x1="30" y1="{tzy:.1f}" x2="{W-30}" y2="{tzy:.1f}" stroke="{C["accent"]}" stroke-width="3"/>')
    p.append(f'<text x="34" y="{tzy-8:.1f}" font-size="8.5" fill="{C["accent"]}" letter-spacing="1.2">TOZAI LINE</text>')
    for nm, (la, lo) in KYOTO.items():
        x, y = f(la, lo)
        hub = nm == "Kyoto Station"
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7 if hub else 4.4}" '
                 f'fill="{C["deep"] if hub else C["paper"]}" stroke="{C["deep"]}" stroke-width="1.8"/>')
        dy = -11 if y < h/2 else 16
        # paper backing so a subway line can never strike through a label
        wpx = 5.6 * len(nm) + 10
        p.append(f'<rect x="{x-wpx/2:.1f}" y="{y+dy-9:.1f}" width="{wpx:.1f}" height="12" '
                 f'fill="{C["paper"]}"/>')
        p.append(f'<text x="{x:.1f}" y="{y+dy:.1f}" font-size="9.5" fill="{C["ink"]}" '
                 f'text-anchor="middle">{_esc(nm)}</text>')
    p.append(f'<text x="30" y="{h-12}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'TWO SUBWAY LINES, AND ALMOST NOTHING ON THEM &#183; THE BUSES DO THE WORK</text>')
    p.append('</svg>')
    return "".join(p)


# ═════════════════════════════════════════════════════════════════════════════
def fig_eat_layers():
    """The four eating layers against what it takes to get in. The upside sits
    in the two layers you cannot book from abroad — which IS the verdict."""
    h = 236
    L, R, T = 16, 22, 52
    rows = [
        ("the destination restaurant", 0.96, "booked, months, often impossible", C["sakura"]),
        ("the counter",                0.10, "walk in &#183; ticket machine",     C["accent"]),
        ("the izakaya",                0.12, "walk in",                           C["accent"]),
        ("depachika &amp; konbini",    0.02, "no booking at all",                 C["accent"]),
    ]
    bw = W - L - R - 180
    p = [f'<svg viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" font-family="{MONO}">']
    p.append(f'<rect width="{W}" height="{h}" fill="{C["paper"]}"/>')
    p.append(f'<text x="{L}" y="{T-26}" font-size="8.5" fill="{C["soft"]}" letter-spacing="1.6">'
             f'EFFORT REQUIRED TO GET IN &#8212;&#8594;</text>')
    p.append(f'<rect x="{L+176}" y="{T-16}" width="{bw*0.30:.0f}" height="{4*40-14}" '
             f'fill="{C["accent"]}" opacity="0.055"/>')
    p.append(f'<text x="{L+176+8}" y="{T-6}" font-size="8" fill="{C["accent"]}" letter-spacing="1.3">'
             f'WHERE THE UPSIDE IS</text>')
    for i, (lab, frac, how, col) in enumerate(rows):
        y = T + i * 40
        p.append(f'<text x="{L}" y="{y+13:.0f}" font-size="10" fill="{C["ink"]}">{lab}</text>')
        p.append(f'<rect x="{L+176}" y="{y+4:.0f}" width="{bw*frac:.0f}" height="13" fill="{col}" opacity=".85"/>')
        p.append(f'<text x="{L+176+bw*frac+8:.0f}" y="{y+14:.0f}" font-size="9" fill="{C["muted"]}">{how}</text>')
    p.append(f'<text x="{L}" y="{h-10}" font-size="8" fill="{C["soft"]}" letter-spacing="1.5">'
             f'BOOK THE TOP ROW. LEAVE THE REST OPEN.</text>')
    p.append('</svg>')
    return "".join(p)


FIGURES["season-compare"] = (fig_season_compare, "Spring against late autumn, on the four axes the decision turns on.")
FIGURES["kyoto-bus"]      = (fig_kyoto,          "Kyoto's two subway lines, and where the sights actually are.")
FIGURES["eat-layers"]     = (fig_eat_layers,     "The four layers, by what it takes to get in.")
