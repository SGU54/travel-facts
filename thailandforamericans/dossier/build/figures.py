# -*- coding: utf-8 -*-
"""figures.py — the drawn figures for Thailand, Covered.

d-draw.md, 2026-09-18: ONE root viewBox per figure, measured containment (every
label computed inside the bounds rather than eyeballed), an explicit fill on every
drawn shape, and no text below the 12px apparatus floor — 10px is permitted only
for axis ticks and column heads, which are labels on a scale rather than prose.

The column is 652px wide. Every viewBox is 652 units wide so one SVG unit is one
printed pixel and nothing is scaled at render time.
"""
import base64, os, re
from design import (PAPER, PAPER_DEEP, INK, INK_SOFT, RULE, ACCENT, ACCENT_DEEP,
                    BODY, DISPLAY)

_F = BODY.replace("'", "&#39;")


def _fontface() -> str:
    """Archivo, embedded in the SVG itself.

    Each figure ships as an <img src="data:image/svg+xml">, because Paged.js
    SPLITS an inline <svg> across pages regardless of break-inside:avoid — FIG. 3
    shipped with its first two column heads (Phuket, Koh Samui) stranded on the
    previous sheet and invisible. An <img> is an atomic replaced element and
    cannot be split. The cost is that an image is an isolated document: it cannot
    reach the page's webfont, so the face travels inside it or the figures set in
    a fallback grotesque that does not match the book.

    Archivo on Google Fonts is a variable font, so one file serves 400 and 600.
    """
    global _FONT_B64
    if _FONT_B64 is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fonts", "archivo-latin.woff2")
        with open(path, "rb") as fh:
            _FONT_B64 = base64.b64encode(fh.read()).decode()
    return ("<defs><style>@font-face{font-family:'Archivo';font-style:normal;"
            "font-weight:100 900;src:url(data:font/woff2;base64,"
            + _FONT_B64 + ")format('woff2');}</style></defs>")


_FONT_B64 = None


def as_img(svg: str) -> str:
    """Wrap a finished SVG as an atomic <img>, font included. Dimensions come from
    the viewBox, so a figure that changes shape cannot fall out of step with the
    box reserved for it."""
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    if not m:
        raise SystemExit("figure has no root viewBox — d-draw.md requires exactly one")
    w, h = m.group(1), m.group(2)
    alt = re.search(r'aria-label="([^"]*)"', svg)
    # Inline in HTML the parser implies the SVG namespace; a standalone image is
    # strict XML and must declare it, or the <img> silently fails to decode.
    if "xmlns=" not in svg:
        svg = svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
    svg = svg.replace(">", ">" + _fontface(), 1)
    b64 = base64.b64encode(svg.encode("utf-8")).decode()
    return (f'<img class="drawnimg" width="{w}" height="{h}" '
            f'alt="{alt.group(1) if alt else ""}" '
            f'src="data:image/svg+xml;base64,{b64}">')


def _t(x, y, s, size=12, fill=INK, anchor="start", weight=400, ls=0, style=""):
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x}" y="{y}" font-family="{_F}" font-size="{size}" '
            f'font-weight="{weight}" letter-spacing="{ls}" fill="{fill}" '
            f'text-anchor="{anchor}"{st}>{s}</text>')


def _box(x, y, w, h, fill, stroke, rx=2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')


def _arrow(x, y, w=10):
    """A small chevron between two legs. Explicit fill, as every shape must have."""
    return (f'<path d="M{x} {y-4} L{x+w} {y} L{x} {y+4} Z" fill="{INK_SOFT}" '
            f'stroke="none"/>')


# ─────────────────────────────────────────────────────── FIG. 2 · the legs ──
def fig_legs() -> str:
    """Decision 02. The cost of an un-serviced island is not distance; it is the
    number of separately-timetabled legs, doubled by the return."""
    o = [f'<svg viewBox="0 0 652 248" width="652" height="248" '
         f'role="img" aria-label="One serviced island is two legs; one '
         f'un-serviced island is three, each separately booked.">',
         f'<rect x="0" y="0" width="652" height="248" fill="{PAPER}"/>']

    # ── row A: the serviced island
    o.append(_t(0, 14, "ONE SERVICED ISLAND — PHUKET, SAMUI, AO NANG", 10,
                INK_SOFT, weight=600, ls="1.4"))
    ax, ay, ah = 0, 26, 36
    o += [_box(ax, ay, 250, ah, PAPER_DEEP, RULE),
          _t(ax + 12, ay + 22, "Flight · about 1h25", 12, INK),
          _arrow(258, ay + ah / 2),
          _box(276, ay, 186, ah, PAPER_DEEP, RULE),
          _t(288, ay + 22, "Road · 30–60 min", 12, INK),
          _t(474, ay + 22, "≈ half a day, door to door", 12, INK_SOFT)]
    o.append(_t(0, 82, "Two legs. One booking can cover both.", 12, INK_SOFT))

    # ── row B: the un-serviced four
    o.append(_t(0, 124, "ONE UN-SERVICED ISLAND — KOH TAO, KOH PHANGAN, "
                        "KOH LANTA, KOH CHANG", 10, ACCENT_DEEP,
                weight=600, ls="1.4"))
    by = 136
    for x, w, label in ((0, 196, "Flight"),
                        (210, 178, "Road to the pier"),
                        (402, 178, "Boat crossing")):
        o += [_box(x, by, w, ah, PAPER, ACCENT),
              _t(x + 12, by + 22, label, 12, INK)]
    o += [_arrow(196, by + ah / 2), _arrow(388, by + ah / 2)]

    # the bracket that makes the point: each leg has its own clock
    o.append(f'<path d="M0 {by+ah+9} L0 {by+ah+15} L580 {by+ah+15} L580 {by+ah+9}" '
             f'fill="none" stroke="{ACCENT}" stroke-width="1"/>')
    o.append(_t(0, by + ah + 34,
                "Three legs, each on its own timetable — and most often three "
                "separate bookings.", 12, INK))
    o.append(_t(0, by + ah + 54,
                "× 2. The same three again on the way back.", 12, ACCENT_DEEP,
                weight=600))
    o.append("</svg>")
    return "".join(o)


# ─────────────────────────────────────────────────────── FIG. 3 · the line ──
_PLACES = [("Phuket", 2), ("Koh Samui", 2), ("Ao Nang / Krabi", 1),
           ("Koh Lanta", 0), ("Koh Phangan", 0), ("Koh Tao", 0), ("Koh Chang", 0)]

# rows: (label, the state of each of the seven places)
#   2 = has it · 1 = on the mainland, not on the island · 0 = does not
_ROWS = [
    ("Its own airstrip",              [2, 2, 1, 0, 0, 0, 0]),
    ("A full hospital, not a clinic", [2, 2, 1, 0, 0, 0, 0]),
    ("Reached in one booked leg",     [2, 2, 1, 0, 0, 0, 0]),
    ("Grab, or a metered alternative",[2, 2, 2, 0, 0, 0, 0]),
]


def fig_line() -> str:
    """Decision 03. Four separately observed measures; the break falls in the same
    place in every one of them. That is the whole argument of the book."""
    LAB, X0, CW, RH = 196, 200, 62, 34
    top = 104                      # rotated column heads occupy 0..100
    H = top + RH * len(_ROWS) + 76
    o = [f'<svg viewBox="0 0 652 {H}" width="652" height="{H}" role="img" '
         f'aria-label="Four separately observed measures break between Ao Nang and '
         f'Koh Lanta, in the same place every time.">',
         f'<rect x="0" y="0" width="652" height="{H}" fill="{PAPER}"/>']

    # column heads, rotated so a 62px column can carry a 15-character name
    for i, (name, _) in enumerate(_PLACES):
        cx = X0 + i * CW + CW / 2
        o.append(f'<g transform="rotate(-90 {cx} {top-10})">'
                 + _t(cx, top - 10 + 4, name, 10, INK, weight=600) + "</g>")

    # the line itself — between the third place and the fourth
    sep = X0 + 3 * CW
    # stops ON the base rule: a 6px overhang below it read as a stray tick
    o.append(f'<line x1="{sep}" y1="{top-96}" x2="{sep}" y2="{top+RH*len(_ROWS)}" '
             f'stroke="{ACCENT}" stroke-width="1.5"/>')

    for r, (label, states) in enumerate(_ROWS):
        y = top + r * RH
        cy = y + RH / 2
        o.append(f'<rect x="0" y="{y}" width="652" height="{RH}" '
                 f'fill="{PAPER_DEEP if r % 2 else PAPER}" stroke="none"/>')
        o.append(_t(LAB - 14, cy + 4, label, 12, INK, anchor="end"))
        for i, s in enumerate(states):
            cx = X0 + i * CW + CW / 2
            if s == 2:
                o.append(f'<circle cx="{cx}" cy="{cy}" r="6.5" fill="{INK}" '
                         f'stroke="none"/>')
            elif s == 1:
                o.append(f'<path d="M{cx} {cy-6.5} A6.5 6.5 0 0 1 {cx} {cy+6.5} Z" '
                         f'fill="{INK}" stroke="none"/>')
                o.append(f'<circle cx="{cx}" cy="{cy}" r="6.5" fill="none" '
                         f'stroke="{INK}" stroke-width="1"/>')
            else:
                o.append(f'<circle cx="{cx}" cy="{cy}" r="6.5" fill="{PAPER}" '
                         f'stroke="{INK_SOFT}" stroke-width="1"/>')

    base = top + RH * len(_ROWS)
    o.append(f'<line x1="0" y1="{base}" x2="652" y2="{base}" stroke="{RULE}" '
             f'stroke-width="1"/>')
    # the key, so a reader never has to infer what a half-filled dot claims
    ky = base + 24
    o += [f'<circle cx="7" cy="{ky-4}" r="6.5" fill="{INK}" stroke="none"/>',
          _t(22, ky, "has it", 12, INK_SOFT),
          f'<path d="M104 {ky-10.5} A6.5 6.5 0 0 1 104 {ky+2.5} Z" fill="{INK}" '
          f'stroke="none"/>',
          f'<circle cx="104" cy="{ky-4}" r="6.5" fill="none" stroke="{INK}" '
          f'stroke-width="1"/>',
          _t(119, ky, "on the mainland, not on the island", 12, INK_SOFT),
          f'<circle cx="360" cy="{ky-4}" r="6.5" fill="{PAPER}" '
          f'stroke="{INK_SOFT}" stroke-width="1"/>',
          _t(375, ky, "does not", 12, INK_SOFT)]
    o.append(_t(0, base + 52,
                "Four separately observed measures. The break falls in the same place "
                "in every one of them.", 12, INK, weight=600))
    o.append("</svg>")
    return "".join(o)


# ──────────────────────────────────────────────────────── FIG. 4 · the gap ──
def fig_gap() -> str:
    """Decision 04. The Bangkok airport gap is not a transfer but a re-entry,
    and the road leg's spread is the measurement nobody plans against."""
    H = 252
    o = [f'<svg viewBox="0 0 652 {H}" width="652" height="{H}" role="img" '
         f'aria-label="Five steps between Bangkok\'s two airports, and the road '
         f'leg\'s 45-minute to two-and-a-half-hour spread.">',
         f'<rect x="0" y="0" width="652" height="{H}" fill="{PAPER}"/>']

    steps = [(104, ["Clear", "immigration"], False),
             (96,  ["Reclaim", "your bags"], False),
             (96,  ["Exit to", "landside"], False),
             (186, ["50 km across Bangkok", "BKK → DMK"], True),
             (126, ["Check in again", "from scratch"], False)]
    x, y, h = 0, 8, 54
    for w, lines, hot in steps:
        o.append(_box(x, y, w, h, PAPER if hot else PAPER_DEEP,
                      ACCENT if hot else RULE))
        o.append(_t(x + 10, y + 22, lines[0], 12, INK,
                    weight=600 if hot else 400))
        o.append(_t(x + 10, y + 39, lines[1], 12, INK_SOFT))
        x += w
        if x < 640:
            o.append(_arrow(x + 1, y + h / 2, 6))
            x += 8

    o.append(f'<path d="M0 {y+h+10} L0 {y+h+16} L640 {y+h+16} L640 {y+h+10}" '
             f'fill="none" stroke="{INK_SOFT}" stroke-width="1"/>')
    o.append(_t(0, y + h + 38,
                "None of it happens airside. No official minimum connection time "
                "is published for this.", 12, INK, weight=600))

    # The road leg, to scale: 0–150 minutes. The scale is inset to leave a label
    # column on the left, because the slower bar ENDS at the right edge of the
    # column — a label placed after it would be drawn outside the viewBox and
    # silently clipped. Measured containment means computing that, not noticing it.
    LABW = 110
    sx, sw, smax = LABW, 652 - LABW - 12, 150.0
    by = 158
    o.append(_t(0, by - 10, "THE ROAD LEG, TO SCALE · MINUTES", 10, INK_SOFT,
                weight=600, ls="1.4"))
    o.append(f'<line x1="{sx}" y1="{by+44}" x2="{sx+sw}" y2="{by+44}" '
             f'stroke="{RULE}" stroke-width="1"/>')
    for m in (0, 30, 60, 90, 120, 150):
        tx = sx + sw * m / smax
        o.append(f'<line x1="{tx}" y1="{by+44}" x2="{tx}" y2="{by+49}" '
                 f'stroke="{RULE}" stroke-width="1"/>')
        anchor = "middle" if 0 < m < 150 else ("start" if m == 0 else "end")
        o.append(_t(tx, by + 63, str(m), 10, INK_SOFT, anchor=anchor))

    for lo, hi, label, col, row in ((45, 60, "off-peak", INK_SOFT, 0),
                                    (90, 150, "in traffic", ACCENT_DEEP, 1)):
        # ACCENT_DEEP, not ACCENT: this bar ends at the column edge, so its
        # label is reversed out INSIDE it. Paper on accent measures 4.45:1 —
        # under AA for text this size. Paper on accent_deep measures 7.29:1.
        bx = sx + sw * lo / smax
        bw = sw * (hi - lo) / smax
        ry = by + row * 20
        o.append(f'<rect x="{bx}" y="{ry}" width="{bw}" height="14" rx="1" '
                 f'fill="{col}" stroke="none"/>')
        o.append(_t(sx - 12, ry + 11, label, 12, INK, anchor="end",
                    weight=600 if row else 400))
        o.append(_t(bx + bw + 7, ry + 11, f"{lo}–{hi}", 12, INK_SOFT)
                 if bx + bw + 46 < 652 else
                 _t(bx + bw - 7, ry + 11, f"{lo}–{hi}", 12, PAPER,
                    anchor="end", weight=600))
    o.append("</svg>")
    return "".join(o)


FIGURES = {
    "legs": (fig_legs, "FIG. 2",
             "The distance is not the cost. An island without an airstrip is "
             "three separately-timetabled legs each way, and the second island "
             "on an itinerary buys six of them."),
    "line": (fig_line, "FIG. 3",
             "Air access, medical capability, booking structure and ground "
             "transport are recorded by four different industries that do not "
             "consult one another. They break between the same two places."),
    "gap":  (fig_gap, "FIG. 4",
             "Forty-five minutes and two and a half hours are the same road on "
             "the same day; which one you get is set by when your inbound lands. "
             "The scale runs to 150 minutes."),
}


# ─────────────────────────────────────────────────── FIG. 5 · the calendar ──
_MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
           "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# (row label, months the corpus calls best, months the corpus says to avoid)
# Months are 1-indexed inclusive ranges, wrapping where the corpus wraps.
_CAL = [
    ("The Andaman coast",  [(11, 4)],  [(9, 10)],  "peak monsoon"),
    ("The Gulf coast",     [(5, 9)],   [(10, 12)], "wettest"),
    ("The north",          [(11, 2)],  [(2, 4)],   "burning season"),
    ("The country at large", [(11, 2)], [(3, 5)],  "hot, and punishing inland"),
]


def _months(rng):
    """Expand an inclusive month range, wrapping across the year boundary."""
    a, b = rng
    return list(range(a, b + 1)) if a <= b else list(range(a, 13)) + list(range(1, b + 1))


def fig_calendar() -> str:
    """The three answers, on one axis. The north's best months and its worst
    months overlap — which is the fact no beach calendar carries."""
    LAB, X0, CW, RH = 150, 158, 40, 44
    top = 26
    H = top + RH * len(_CAL) + 66
    o = [f'<svg viewBox="0 0 652 {H}" width="652" height="{H}" role="img" '
         f'aria-label="Two coasts with opposite wet seasons, and a northern '
         f'burning season that overlaps the north\'s own best months.">',
         f'<rect x="0" y="0" width="652" height="{H}" fill="{PAPER}"/>']

    for i, m in enumerate(_MONTHS):
        o.append(_t(X0 + i * CW + CW / 2, top - 10, m, 10, INK_SOFT,
                    anchor="middle", weight=600))

    for r, (label, best, avoid, avoid_label) in enumerate(_CAL):
        y = top + r * RH
        o.append(_t(LAB - 14, y + 17, label, 12, INK, anchor="end", weight=600))
        o.append(_t(LAB - 14, y + 33, avoid_label, 12, ACCENT_DEEP, anchor="end"))
        bset = {m for rng in best for m in _months(rng)}
        aset = {m for rng in avoid for m in _months(rng)}
        for i in range(12):
            mo, cx = i + 1, X0 + i * CW
            o.append(f'<rect x="{cx}" y="{y+6}" width="{CW-2}" height="13" rx="1" '
                     f'fill="{INK if mo in bset else PAPER_DEEP}" stroke="none"/>')
            o.append(f'<rect x="{cx}" y="{y+23}" width="{CW-2}" height="13" rx="1" '
                     f'fill="{ACCENT if mo in aset else PAPER_DEEP}" stroke="none"/>')

    base = top + RH * len(_CAL)
    ky = base + 22
    o += [f'<rect x="0" y="{ky-10}" width="28" height="13" rx="1" fill="{INK}" '
          f'stroke="none"/>', _t(36, ky, "the reporting calls it best", 12, INK_SOFT),
          f'<rect x="228" y="{ky-10}" width="28" height="13" rx="1" fill="{ACCENT}" '
          f'stroke="none"/>', _t(264, ky, "the reporting says avoid", 12, INK_SOFT)]
    o.append(_t(0, base + 50,
                "February and March are the north at its best and the north at "
                "its worst, in the same weeks.", 12, INK, weight=600))
    o.append("</svg>")
    return "".join(o)


FIGURES["calendar"] = (
    fig_calendar, "FIG. 5",
    "Three calendars, none of which governs the other two. A November trip that "
    "wants Chiang Mai and the Gulf islands has chosen the north's best month and "
    "the Gulf's wettest stretch at once.")
