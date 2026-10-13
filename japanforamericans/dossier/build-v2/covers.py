# covers.py — the cover device.
# The test (cover.md): could this cover sit on any book about Japan? It must be
# reproducible ONLY by someone who did this book's analysis.
#
# Japan's organising fact is a NUMBER COLLISION — the trip has two long legs, the
# pass needs about four. So the cover draws the real corridor (real coordinates,
# real fare) and then draws the two phantom legs the pass would require, which the
# trip never travels. The gap between the solid line and the ghost IS the thesis.
# ─────────────────────────────────────────────────────────────────────────────
import math
from maps import GEO, _proj

PAPER = "#F5EFE1"; INDIGO = "#16305F"; INK = "#242A33"
GILT = "#B89547"; SAKURA = "#C87F94"; MIST = "#7E93B8"

CW, CH = 816, 1056


def cover_svg():
    p = [f'<svg viewBox="0 0 {CW} {CH}" xmlns="http://www.w3.org/2000/svg">']
    # full bleed indigo field — ink coverage, not a title on a blank sheet (bug #23)
    p.append(f'<rect width="{CW}" height="{CH}" fill="{INDIGO}"/>')

    # faint aizome wash — concentric arcs, the dyer's vat
    for i in range(14):
        r = 210 + i * 46
        p.append(f'<circle cx="{CW*0.5:.0f}" cy="410" r="{r}" fill="none" stroke="{MIST}" '
                 f'stroke-width="0.7" opacity="{0.10 - i*0.006:.3f}"/>')

    # ── the corridor, from real coordinates ──────────────────────────────────
    keys = ("Tokyo", "Kyoto", "Nara", "Hakone", "Nikko", "Kamakura")
    f = _proj([GEO[k] for k in keys], CW, 520, 150)
    def P(k):
        x, y = f(*GEO[k]); return x, y + 150          # drop into the upper field

    TX, TY = P("Tokyo"); KX, KY = P("Kyoto")

    # day-trip spokes — the local lines, dashed and quiet
    for a, hub in (("Nikko","Tokyo"), ("Hakone","Tokyo"), ("Kamakura","Tokyo"), ("Nara","Kyoto")):
        ax, ay = P(a); hx, hy = P(hub)
        p.append(f'<line x1="{hx:.1f}" y1="{hy:.1f}" x2="{ax:.1f}" y2="{ay:.1f}" '
                 f'stroke="{MIST}" stroke-width="1" stroke-dasharray="3 4" opacity=".55"/>')
        p.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.6" fill="{MIST}" opacity=".8"/>')

    # the TWO legs the trip really travels — solid gold, out and back
    p.append(f'<line x1="{TX:.1f}" y1="{TY:.1f}" x2="{KX:.1f}" y2="{KY:.1f}" '
             f'stroke="{GILT}" stroke-width="3.4" stroke-linecap="round"/>')

    # The phantom legs were drawn along the same bearing and ran off the sheet,
    # which read as a stray dotted line rather than as the argument. Replaced by an
    # explicit leg-count motif below the map: two solid (what you travel) against
    # four outlined (what the pass needs). Legible in one look, which is the test.

    for nm in ("Tokyo", "Kyoto"):
        x, y = P(nm)
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="{PAPER}"/>')
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="none" stroke="{PAPER}" '
                 f'stroke-width="1" opacity=".38"/>')
        p.append(f'<text x="{x:.1f}" y="{y-24:.1f}" font-size="15" fill="{PAPER}" '
                 f'text-anchor="middle" font-family="\'Zen Old Mincho\',serif" '
                 f'letter-spacing="1.5">{nm}</text>')

    # the arithmetic, stated on the face of the book
    _mx, _my = (TX+KX)/2, (TY+KY)/2
    p.append(f'<rect x="{_mx-74:.1f}" y="{_my-32:.1f}" width="148" height="20" fill="{INDIGO}"/>')
    p.append(f'<text x="{(TX+KX)/2:.1f}" y="{(TY+KY)/2 - 18:.1f}" font-size="10" fill="{GILT}" '
             f'text-anchor="middle" font-family="\'IBM Plex Mono\',monospace" letter-spacing="2">'
             f'ONE LEG &#183; &#165;13,850</text>')

    # ── the leg-count motif: the whole book in one row of bars ───────────────
    bx, by, bw, bh, gap = 96, 604, 92, 13, 14
    for k in range(4):
        x = bx + k * (bw + gap)
        if k < 2:
            p.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" fill="{GILT}"/>')
        else:
            p.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" fill="none" '
                     f'stroke="{GILT}" stroke-width="1.1" stroke-dasharray="3 3" opacity=".75"/>')
    p.append(f'<text x="{bx}" y="{by - 13}" font-size="9.5" fill="{PAPER}" '
             f'font-family="\'IBM Plex Mono\',monospace" letter-spacing="2.4">'
             f'YOUR TRIP: TWO LONG LEGS</text>')
    p.append(f'<text x="{bx + 2*(bw+gap)}" y="{by + bh + 18}" font-size="9.5" fill="{MIST}" '
             f'font-family="\'IBM Plex Mono\',monospace" letter-spacing="2.4">'
             f'THE PASS NEEDS FOUR</text>')

    # ── the title block ──────────────────────────────────────────────────────
    p.append(f'<line x1="96" y1="742" x2="{CW-96}" y2="742" stroke="{GILT}" stroke-width="1.4" '
             f'opacity=".8"/>')
    p.append(f'<text x="96" y="726" font-size="10.5" fill="{MIST}" '
             f'font-family="\'IBM Plex Mono\',monospace" letter-spacing="4.5">'
             f'A DECISION MANUAL &#183; FIRST TRIP</text>')

    p.append(f'<text x="96" y="826" font-size="72" fill="{PAPER}" '
             f'font-family="\'Zen Old Mincho\',serif" letter-spacing="-0.5">Japan,</text>')
    p.append(f'<text x="96" y="906" font-size="72" fill="{GILT}" '
             f'font-family="\'Zen Old Mincho\',serif" letter-spacing="-0.5">Worked Out.</text>')

    # the thesis, in one line, as the subtitle
    p.append(f'<text x="96" y="952" font-size="13.5" fill="{MIST}" '
             f'font-family="\'Spectral\',serif" font-style="italic">'
             f'Your trip has two long train journeys in it.</text>')
    p.append(f'<text x="96" y="973" font-size="13.5" fill="{MIST}" '
             f'font-family="\'Spectral\',serif" font-style="italic">'
             f'The rail pass needs four.</text>')

    # foot rule + imprint
    p.append(f'<line x1="96" y1="1004" x2="{CW-96}" y2="1004" stroke="{MIST}" stroke-width="0.8" '
             f'opacity=".45"/>')
    p.append(f'<text x="96" y="1026" font-size="9" fill="{MIST}" '
             f'font-family="\'IBM Plex Mono\',monospace" letter-spacing="2.6">'
             f'JAPAN FOR AMERICANS</text>')
    p.append(f'<text x="{CW-96}" y="1026" font-size="9" fill="{MIST}" text-anchor="end" '
             f'font-family="\'IBM Plex Mono\',monospace" letter-spacing="2.6">'
             f'FIRST EDITION</text>')
    p.append('</svg>')
    return "".join(p)
