"""Stage D.5 — the cover as a COMPUTED figure (cover.md), not a photograph.

Thesis: in Turkey the number you need does not exist.
Device: the book's own instrument on its face, with the load-bearing cells BLANK,
standing on the funnel geometry that forces the sequence. Both halves are computed
from real data — the distances from real coordinates at build time, the blanks from
the five shipped decisions. Nobody who has not done this analysis can redraw it.
"""
import math
from design import P

# real coordinates — the same geo the funnel figure is drawn from
GEO = {
    "Istanbul":   (41.0082, 28.9784),
    "Cappadocia": (38.6431, 34.8286),   # Goreme
    "Ephesus":    (37.9410, 27.3400),   # Selcuk
    "Antalya":    (36.8969, 30.7133),
}


def km(a, b):
    (la1, lo1), (la2, lo2) = GEO[a], GEO[b]
    R = 6371.0
    p1, p2 = math.radians(la1), math.radians(la2)
    dp, dl = math.radians(la2 - la1), math.radians(lo2 - lo1)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return round(2 * R * math.asin(math.sqrt(h)))


# the five blanks — one per shipped decision. The value column is EMPTY by design.
ROWS = [
    ("I",   "MINIMUM CONNECTION, IST / SAW"),
    ("II",  "WHAT THE POLICY PAYS ON A BALLOON"),
    ("III", "THE LICENCE AGE THAT BINDS YOU"),
    ("IV",  "THE AGE AT WHICH IT CANNOT LEAVE"),
    ("V",   "THE REAL COST OF HOLDING LIRA"),
]

W, H = 816.0, 1056.0


def _proj():
    """equirectangular, fitted to the four points with margin — real geography."""
    lats = [v[0] for v in GEO.values()]
    lons = [v[1] for v in GEO.values()]
    la0 = math.radians(sum(lats) / len(lats))
    xs = [lo * math.cos(la0) for lo in lons]
    x0, x1, y0, y1 = min(xs), max(xs), min(lats), max(lats)
    bx0, bx1, by0, by1 = 96.0, 720.0, 508.0, 700.0     # the band the map sits in
    sx = (bx1 - bx0) / (x1 - x0)
    sy = (by1 - by0) / (y1 - y0)
    s = min(sx, sy)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    mx, my = (bx0 + bx1) / 2, (by0 + by1) / 2

    def f(name):
        la, lo = GEO[name]
        return (mx + (lo * math.cos(la0) - cx) * s, my - (la - cy) * s)
    return f


def cover_svg():
    f = _proj()
    ist, cap, eph, ant = (f(n) for n in ("Istanbul", "Cappadocia", "Ephesus", "Antalya"))
    d_ic, d_ie, d_ce = km("Istanbul", "Cappadocia"), km("Istanbul", "Ephesus"), km("Cappadocia", "Ephesus")

    def line(a, b, w, op, dash=""):
        return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                f'stroke="{P["ink"]}" stroke-width="{w}" opacity="{op}"{dash}/>')

    def dot(pt, r=3.2):
        return f'<circle cx="{pt[0]:.1f}" cy="{pt[1]:.1f}" r="{r}" fill="{P["ink"]}"/>'

    def lbl(pt, t, dx=0, dy=-11, anchor="middle"):
        return (f'<text x="{pt[0]+dx:.1f}" y="{pt[1]+dy:.1f}" text-anchor="{anchor}" '
                f'font-family="Space Mono, monospace" font-size="8.5" letter-spacing="1.8" '
                f'fill="{P["ink"]}">{t}</text>')

    # ---- the absent ledger: 5 rows, value cell struck blank
    rows = []
    y = 298.0
    for num, label in ROWS:
        rows.append(
            f'<text x="96" y="{y}" font-family="Space Mono, monospace" font-size="9" '
            f'letter-spacing="1.6" fill="{P["accent"]}">{num}</text>'
            f'<text x="128" y="{y}" font-family="Space Mono, monospace" font-size="9" '
            f'letter-spacing="1.5" fill="{P["ink"]}" opacity="0.82">{label}</text>'
            f'<line x1="556" y1="{y+2.5:.1f}" x2="720" y2="{y+2.5:.1f}" '
            f'stroke="{P["accent"]}" stroke-width="1.1" opacity="0.9"/>'
            f'<line x1="96" y1="{y+15:.1f}" x2="720" y2="{y+15:.1f}" '
            f'stroke="{P["line"]}" stroke-width="0.8"/>')
        y += 36.0

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}">
<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" fill="{P['paper']}"/>

<text x="96" y="104" font-family="Space Mono, monospace" font-size="9" letter-spacing="3.4"
  fill="{P['accent']}">A DECISION MANUAL FOR A FIRST TRIP</text>

<text x="93" y="212" font-family="Anton, sans-serif" font-size="76" letter-spacing="-1.6"
  fill="{P['ink']}">TURKEY, WORKED OUT.</text>

<text x="96" y="256" font-family="Space Mono, monospace" font-size="8.5" letter-spacing="2.2"
  fill="{P['muted']}">THE NUMBERS THIS TRIP TURNS ON, AND WHERE THEY ARE PUBLISHED</text>
{''.join(rows)}
<text x="720" y="{y+4:.0f}" text-anchor="end" font-family="Space Mono, monospace"
  font-size="8.5" letter-spacing="1.6" fill="{P['muted']}">NOT PUBLISHED. ANYWHERE.</text>

<!-- the ground: the funnel that forces the sequence, computed from real coordinates -->
{line(ist, cap, 1.0, 0.30)}{line(ist, eph, 1.0, 0.30)}{line(ist, ant, 1.0, 0.18)}
{line(cap, eph, 1.6, 0.85, ' stroke-dasharray="5 4"')}
{dot(ist, 4.0)}{dot(cap)}{dot(eph)}{dot(ant, 2.4)}
{lbl(ist, 'ISTANBUL', 0, -13)}{lbl(cap, 'CAPPADOCIA', 0, 18)}
{lbl(eph, 'EPHESUS', 0, 18)}{lbl(ant, 'ANTALYA', 0, 17)}
<text x="{(cap[0]+eph[0])/2:.0f}" y="{(cap[1]+eph[1])/2-9:.0f}" text-anchor="middle"
  font-family="Space Mono, monospace" font-size="9.5" letter-spacing="1.4"
  fill="{P['accent']}">{d_ce} KM</text>
<text x="{(ist[0]+cap[0])/2+16:.0f}" y="{(ist[1]+cap[1])/2:.0f}"
  font-family="Space Mono, monospace" font-size="8" letter-spacing="1.2"
  fill="{P['muted']}">{d_ic} KM</text>
<text x="{(ist[0]+eph[0])/2-16:.0f}" y="{(ist[1]+eph[1])/2:.0f}" text-anchor="end"
  font-family="Space Mono, monospace" font-size="8" letter-spacing="1.2"
  fill="{P['muted']}">{d_ie} KM</text>

<line x1="96" y1="742" x2="720" y2="742" stroke="{P['ink']}" stroke-width="1.4"/>
<text x="96" y="790" font-family="Gelasio, Georgia, serif" font-style="italic" font-size="19"
  fill="{P['ink']}">The two places you came for are {d_ce} km apart —</text>
<text x="96" y="818" font-family="Gelasio, Georgia, serif" font-style="italic" font-size="19"
  fill="{P['ink']}">further from each other than either is from Istanbul.</text>
<text x="96" y="846" font-family="Gelasio, Georgia, serif" font-style="italic" font-size="19"
  fill="{P['ink']}">Every internal move is routed through it, and no authority</text>
<text x="96" y="874" font-family="Gelasio, Georgia, serif" font-style="italic" font-size="19"
  fill="{P['ink']}">states how much time the connection needs.</text>

<text x="96" y="962" font-family="Space Mono, monospace" font-size="8.5" letter-spacing="2.6"
  fill="{P['muted']}">SEVEN DECISIONS, WORKED</text>
<text x="720" y="962" text-anchor="end" font-family="Space Mono, monospace" font-size="8.5"
  letter-spacing="2.6" fill="{P['accent']}">TURKEYFORAMERICANS.COM</text>
</svg>'''


if __name__ == "__main__":
    print("IST-CAP", km("Istanbul", "Cappadocia"),
          "| IST-EPH", km("Istanbul", "Ephesus"),
          "| CAP-EPH", km("Cappadocia", "Ephesus"))
