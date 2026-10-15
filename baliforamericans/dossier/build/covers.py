# covers.py — the cover device.
# The test (cover.md): could this cover sit on any book about Bali? It must be
# reproducible ONLY by someone who did this book's analysis.
#
# Bali's organising fact is SHORT MILES, LONG DAYS: an island eighty-nine miles
# wide whose distances are counted in hours, with three pinned points — the
# arrival hour, the sea, the airport run — deciding where the nights go. So the
# cover draws the real island from coordinates with the airport at its neck
# and the bases at their true positions, and under it the one strip that says
# it in a look: ten nights in the order the pins impose, with the three pins
# drawn. One device, three labels, promise line at 22px.
# ─────────────────────────────────────────────────────────────────────────────
from maps import GEO, _proj

PAPER = "#F5F4F8"; INK = "#1A1423"; MAG = "#B3155E"; INDIGO = "#262868"
GILT = "#D99412"; DEEP = "#8A0F47"; SOFT = "#7E7689"; PANEL = "#ECE9F1"; WATER = "#D6E0F2"
CW, CH = 816, 1056
MONO = "'Space Mono',monospace"; DISP = "'Bricolage Grotesque',sans-serif"; BODY = "'Hanken Grotesk',sans-serif"


def cover_svg():
    p = [f'<svg viewBox="0 0 {CW} {CH}" xmlns="http://www.w3.org/2000/svg">']
    p.append(f'<rect width="{CW}" height="{CH}" fill="{PAPER}"/>')
    # the day strip, the site's one recurring mark: night, dawn, day, dusk, night
    p.append('<defs><linearGradient id="day" x1="0" x2="1"><stop offset="0" stop-color="#12143A"/><stop offset=".14" stop-color="#2A2C7C"/><stop offset=".24" stop-color="#B3155E"/><stop offset=".31" stop-color="#F7A614"/><stop offset=".44" stop-color="#8FB8FF"/><stop offset=".58" stop-color="#4B7BE0"/><stop offset=".72" stop-color="#F7A614"/><stop offset=".80" stop-color="#B3155E"/><stop offset=".90" stop-color="#2A2C7C"/><stop offset="1" stop-color="#12143A"/></linearGradient></defs>')
    p.append(f'<rect x="0" y="0" width="{CW}" height="22" fill="url(#day)"/>')

    # ── the island, from real coordinates, filling the upper two-thirds ─────
    keys = ("Airport","Kuta","Seminyak","Canggu","Tanah Lot","Uluwatu","Nusa Dua","Sanur","Ubud",
            "Kintamani","Sidemen","Padang Bai","Amed","Munduk","Lovina","Singaraja","Lembongan","Besakih","Tulamben","Lempuyang")
    f = _proj([GEO[k] for k in keys], 640, 560, 60)
    def P(k):
        x, y = f(*GEO[k]); return x + 88, y + 70
    AX, AY = P("Airport")
    # rings of road miles from the airport (scale from the Ubud road distance)
    ux, uy = P("Ubud"); ppm = ((ux-AX)**2 + (uy-AY)**2) ** 0.5 / 22.0
    for mi, op in ((15, .9), (35, .7), (60, .5)):
        p.append(f'<circle cx="{AX:.1f}" cy="{AY:.1f}" r="{mi*ppm:.1f}" fill="none" stroke="{INDIGO}" stroke-width="1.2" stroke-dasharray="4 6" opacity="{op}"/>')
    # the spokes to every base, weight by group
    groups = {MAG: ("Kuta","Seminyak","Canggu","Uluwatu","Nusa Dua","Sanur","Tanah Lot"),
              INDIGO: ("Ubud","Kintamani","Sidemen","Besakih"),
              GILT: ("Munduk","Lovina","Amed","Padang Bai","Tulamben","Lempuyang","Singaraja")}
    for col, names in groups.items():
        for n in names:
            x, y = P(n)
            p.append(f'<line x1="{AX:.1f}" y1="{AY:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="1" opacity=".35"/>')
    for col, names in groups.items():
        for n in names:
            x, y = P(n)
            big = n in ("Ubud","Seminyak","Uluwatu","Sanur","Munduk","Amed","Canggu")
            p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8 if big else 4.5}" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
    lx, ly = P("Lembongan")
    p.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="6" fill="{WATER}" stroke="{INDIGO}" stroke-width="2"/>')
    p.append(f'<rect x="{AX-9:.1f}" y="{AY-9:.1f}" width="18" height="18" fill="{INK}"/>')
    # at most three labels, ≥24px (cover.md)
    for k, lab, dx, dy, an in (("Ubud","UBUD",18,10,"start"),("Seminyak","SEMINYAK",-18,10,"end"),("Amed","AMED",18,10,"start")):
        x, y = P(k)
        p.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="26" fill="{INK}" text-anchor="{an}" font-family="{DISP}" font-weight="700" letter-spacing="1">{lab}</text>')

    # ── the strip: ten nights in the order the pins impose ───────────────────
    L, T = 64, 672
    unit = (CW - 2 * L) / 11.0
    for n, col in ((3, INDIGO), (3, WATER), (4, MAG), (1, INK)):
        p.append(f'<rect x="{L:.1f}" y="{T}" width="{n*unit-3:.1f}" height="30" fill="{col}" opacity="0.92"/>')
        L += n * unit
    L = 64
    for px, col in ((0, GILT), (6, INDIGO), (10, INDIGO)):
        x = L + px * unit
        p.append(f'<line x1="{x:.1f}" y1="{T-8}" x2="{x:.1f}" y2="{T+38}" stroke="{col}" stroke-width="3"/>')
    p.append(f'<text x="{L}" y="{T-16}" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">TEN NIGHTS · INLAND, THEN THE SEA, THEN THE AIRPORT\'S COAST · THE THREE PINS</text>')

    # ── the title block ──────────────────────────────────────────────────────
    p.append(f'<line x1="60" y1="760" x2="{CW-60}" y2="760" stroke="{INDIGO}" stroke-width="2"/>')
    p.append(f'<text x="60" y="744" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">A DECISION MANUAL &#183; FIRST TRIP &#183; FOR AMERICANS</text>')
    p.append(f'<text x="60" y="856" font-size="104" fill="{INK}" font-family="{DISP}" font-weight="800" letter-spacing="-1">Bali,</text>')
    p.append(f'<text x="60" y="946" font-size="78" fill="{MAG}" font-family="{DISP}" font-weight="800" letter-spacing="-1">in Its Own Time.</text>')
    # the promise line — the dominant edge is TIME and ORDER, not money
    p.append(f'<text x="60" y="988" font-size="22" fill="{INK}" font-family="{BODY}" font-style="italic">'
             f'Ninety miles wide, measured in hours. One boat that answers to the sea.</text>')
    p.append(f'<text x="60" y="1017" font-size="22" fill="{INK}" font-family="{BODY}" font-style="italic">'
             f'Where the nights go, and in what order.</text>')
    p.append(f'<text x="60" y="1040" font-size="12" fill="{SOFT}" font-family="{MONO}" letter-spacing="1">BALI FOR AMERICANS</text>')
    p.append(f'<text x="{CW-60}" y="1040" font-size="12" fill="{SOFT}" text-anchor="end" font-family="{MONO}" letter-spacing="1">FIRST EDITION &#183; 2026</text>')
    p.append('</svg>')
    return "".join(p)
