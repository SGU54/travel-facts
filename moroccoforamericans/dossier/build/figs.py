#!/usr/bin/env python3
"""figs.py — every diagram in the book, emitted at ONE standard canvas.

Why this exists
---------------
The eight diagrams were hand-authored at eight different sizes (viewBox heights
286 to 430 on a constant 680 width) and the stylesheet papered over it with
`figure.map img { height:auto; max-height:3.5in; object-fit:contain }`. That cap
bites on every one of them, and `contain` scales rather than crops, so the book
ships eight figures at FIVE different rendered heights — 3.50, 3.46, 3.05, 3.05,
2.91in — three of which float inside a full-column border with ~0.65in of bare
paper either side. A reader turning pages sees a figure that changes size and
inset each time it appears. That is the "cluttered" complaint, located.

The standard
------------
One canvas: 1300 x 640, drawn at the full column width of 6.92in, so the figure
is 3.41in of drawing plus its caption — 4.00in of column, every time, and the
1px border always sits flush on the drawing. `max-height` comes off the
stylesheet; nothing is capped, so nothing varies.

Maps get a fitted projection, not a fixed one
---------------------------------------------
A true-scale Morocco is not a wide shape. Measured off the four cities in the
original fig1 (which recovers to 68.6 px/deg lat and 57.2 px/deg lon, i.e. an
honest cos(33.5 deg) correction), the open-jaw extent is 4.07 deg of latitude by
4.00 of longitude — an aspect of 0.82:1, TALLER than square. It cannot fill a
2.03:1 frame, and stretching it to fit would be a lie about distance.

So each map is projected at true scale into whatever height it needs, and the
width it does not use becomes a panel that states the consequence the map
implies. That is the point of the wider canvas: not padding, a second column
that makes the figure argue rather than merely depict. fig2 needs almost none of
it (Marrakech-Zagora-Merzouga is naturally 2.64:1, wider than the frame); fig1
and fig6 need most of it.
"""
import math, os, sys

W, H = 1300, 640                       # the standard canvas

# A figure's APPARENT type size is size/W, not size — the drawing is always
# painted into the same 6.92in of column. The originals were authored on a
# 680-wide canvas, so a 14px label rendered at 14/680 x 6.92in = 0.14in ~ 10pt,
# a touch larger than the book's 9.6pt body. On this 1300-wide canvas the same
# number renders at 5pt and the panel is unreadable. So every size, radius,
# stroke and letter-spacing below is authored in the ORIGINAL 680 units and
# multiplied by SC on the way out.
SC = W / 680.0
PAPER, INK = "#f5efe2", "#241a12"
MUTED, LINE = "#8a7a5f", "#d8cbb0"
GREEN, BRASS, SAFFRON = "#16614f", "#9c6b3f", "#c8912f"
SLATE, PANEL_EDGE = "#7d8ba3", "#e1d6bd"
MONO = "'IBM Plex Mono',monospace"
SERIF = "Georgia,serif"

HERE = os.path.dirname(os.path.abspath(__file__))

# ── primitives ───────────────────────────────────────────────────────────────

def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def txt(x, y, s, *, size=11, fill=INK, font=SERIF, anchor="start",
        weight="400", ls=None, upper=False):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls * SC:.2f}"' if ls is not None else ""
    w = f' font-weight="{weight}"' if weight != "400" else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}"{a} font-family="{font}" '
            f'font-size="{size * SC:.1f}"{w}{l} fill="{fill}">'
            f'{esc(s.upper() if upper else s)}</text>')

def title(s):
    """The figure's own title band, identical on every diagram."""
    return txt(W / 2, 30, s, size=12, fill=BRASS, font=MONO, anchor="middle",
               ls=2.2, upper=True)

def footnote(s):
    return txt(W - 30, H - 16, s, size=10, fill=MUTED, font=MONO, anchor="end")

def rule(x1, y1, x2, y2, *, color=LINE, w=1.4, dash=None, cap=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    c = f' stroke-linecap="{cap}"' if cap else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{w * SC:.2f}"{d}{c}/>')

def dot(x, y, r, fill):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * SC:.1f}" fill="{fill}"/>'

def box(x, y, w, h, *, fill="none", stroke=None, sw=1.2, op=None, rx=None):
    s = f' stroke="{stroke}" stroke-width="{sw * SC:.2f}"' if stroke else ""
    o = f' opacity="{op}"' if op is not None else ""
    r = f' rx="{rx}"' if rx else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'fill="{fill}"{s}{o}{r}/>')

def head(body):
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">\n'
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>\n'
            + "\n".join(body) + "\n</svg>\n")



def wrap(x, y, width, s, *, size=11, fill=INK, font=SERIF, lead=1.45):
    """SVG <text> does not wrap. Break on a character budget derived from the
    rendered size — approximate, but the columns here are generous enough that
    an approximate break is invisible."""
    per = max(8, int(width / (size * SC * 0.47)))
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        if len(cur) + len(w_) + 1 <= per:
            cur = (cur + " " + w_).strip()
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return "\n".join(txt(x, y + i * size * SC * lead, l, size=size, fill=fill,
                          font=font) for i, l in enumerate(lines))


# ── the argument panel ───────────────────────────────────────────────────────

def panel(x, y, w, heading, rows, *, foot=None):
    """A stack of {label, value, gloss} rows. This is what the map's unused
    width is for: the consequence, stated, beside the geography that implies it."""
    G = SC                                    # gaps scale with the type
    out = [txt(x, y, heading, size=10, fill=BRASS, font=MONO, ls=1.8, upper=True),
           rule(x, y + 13 * G, x + w, y + 13 * G, color=BRASS, w=1.4)]
    cy = y + 46 * G
    for label, value, gloss in rows:
        out.append(txt(x, cy, label, size=13, weight="600", fill=INK))
        if value:
            out.append(txt(x + w, cy, value, size=10, fill=GREEN, font=MONO,
                           anchor="end", ls=.6, upper=True))
        if gloss:
            out.append(txt(x, cy + 17 * G, gloss, size=11, fill=MUTED))
        cy += (26 if not gloss else 45) * G
        out.append(rule(x, cy - 15 * G, x + w, cy - 15 * G, color=LINE, w=1))
    if foot:
        out.append(txt(x, cy + 4 * G, foot, size=10.5, fill=BRASS))
    return out

# ── true-scale projection, fitted to a box ───────────────────────────────────

def projector(places, bx, by, bw, bh):
    """Fit lat/lon points into (bx,by,bw,bh) at TRUE scale — one degree of
    latitude is the same number of pixels everywhere, and longitude is shrunk
    by cos(mean latitude). Returns the mapping and the box it actually filled,
    which is narrower or shorter than the one offered whenever the geography
    is not the same shape as the frame."""
    lats = [p[0] for p in places.values()]
    lons = [p[1] for p in places.values()]
    cos = math.cos(math.radians(sum(lats) / len(lats)))
    dlat = max(lats) - min(lats)
    dlon = (max(lons) - min(lons)) * cos
    s = min(bw / dlon, bh / dlat) if dlat and dlon else 1.0
    uw, uh = dlon * s, dlat * s
    ox = bx + (bw - uw) / 2 if bw / max(dlon, 1e-9) > s else bx
    oy = by + (bh - uh) / 2
    def f(lat, lon):
        return (ox + (lon - min(lons)) * cos * s, oy + (max(lats) - lat) * s)
    return f, (ox, oy, uw, uh)

CITY = {  # decimal degrees
    "Marrakech":   (31.63, -8.01), "Merzouga":  (31.10, -4.01),
    "Fez":         (34.04, -5.00), "Casablanca":(33.57, -7.59),
    "Chefchaouen": (35.17, -5.27), "Zagora":    (30.33, -5.84),
    "Ouarzazate":  (30.93, -6.91), "Essaouira": (31.51, -9.77),
    "Imlil":       (31.14, -7.92), "Tangier":   (35.78, -5.81),
    "Rabat":       (34.02, -6.83),
}

def place(f, name, *, r=7, fill=GREEN, label=None, note=None, side="above",
          size=14, lsize=9):
    """A city: dot, name, and an optional mono note under it."""
    x, y = f(*CITY[name])
    out = [dot(x, y, r, fill)]
    dy = (-r - 7) * SC if side == "above" else (r + 15) * SC
    out.append(txt(x, y + dy, label or name, size=size, weight="600",
                   fill=INK, anchor="middle"))
    if note:
        ny = y + (dy - 12 * SC if side == "above" else dy + 12 * SC)
        out.append(txt(x, ny, note, size=lsize, fill=BRASS, font=SERIF,
                       anchor="middle", upper=True))
    return out

def minor(f, name):
    x, y = f(*CITY[name])
    return [dot(x, y, 3, LINE),
            txt(x, y - 9 * SC, name, size=10, fill=MUTED, anchor="middle")]


# ═════════════════════════════════════════════════════════════════════════════
#  the eight existing figures, re-laid-out into the standard canvas
# ═════════════════════════════════════════════════════════════════════════════

def fig1_route():
    """Open jaw. The map is 0.82:1, so it takes the left third and the panel
    carries the arithmetic that makes the open jaw worth asking for."""
    pts = {k: CITY[k] for k in ("Marrakech", "Merzouga", "Fez",
                                "Casablanca", "Chefchaouen")}
    # 440 not 500: Merzouga is the southernmost point and carries a note
    # BELOW its label, which ran off the canvas at the taller box.
    f, (ox, oy, uw, uh) = projector(pts, 74, 80, 430, 440)
    b = [title("The open-jaw line · fly into one city, out of another")]
    mk, mz, fz = f(*CITY["Marrakech"]), f(*CITY["Merzouga"]), f(*CITY["Fez"])
    b.append(f'<path d="M {mk[0]:.1f} {mk[1]:.1f} L {mz[0]:.1f} {mz[1]:.1f} '
             f'L {fz[0]:.1f} {fz[1]:.1f}" fill="none" stroke="{BRASS}" '
             f'stroke-width="2.6" stroke-dasharray="1 7" stroke-linecap="round"/>')
    b.append(f'<path d="M {mk[0]:.1f} {mk[1]:.1f} L {fz[0]:.1f} {fz[1]:.1f}" '
             f'fill="none" stroke="{LINE}" stroke-width="1.4" '
             f'stroke-dasharray="5 6"/>')
    b += minor(f, "Casablanca") + minor(f, "Chefchaouen")
    b += place(f, "Marrakech", fill=GREEN, note="arrive · RAK")
    b += place(f, "Merzouga", fill=SAFFRON, note="the desert night", side="below")
    b += place(f, "Fez", fill=GREEN, note="depart · FEZ")
    b.append(txt(74, H - 14, "true scale · cos(lat) corrected",
                 size=9, fill=MUTED, font=MONO, upper=True))
    b += panel(600, 96, 640, "What the open jaw buys", [
        ("Marrakech → Merzouga → Fez", "~1,030 km",
         "One direction. Every night is somewhere you have not slept."),
        ("Flying home from Marrakech instead", "~1,560 km",
         "Fez → Marrakech adds a leg you have effectively already driven."),
        ("What the open jaw removes", "6–7 h",
         "One driving day, and the night at the end of it."),
    ], foot="Ask for it by name: two one-way fares, not a return.")
    return head(b)


def sy_note():
    return 502 - 26   # just above the strip rule in fig2


def fig2_desert():
    """Merzouga vs Zagora. This geography IS wide (2.64:1), so the map takes
    most of the frame and the panel shrinks to a single column of numbers."""
    # 2.64:1 — wider than the frame, so it takes the full width and the panel
    # goes underneath as a strip rather than beside it as a column.
    pts = {k: CITY[k] for k in ("Marrakech", "Ouarzazate", "Zagora", "Merzouga")}
    f, (ox, oy, uw, uh) = projector(pts, 70, 96, 1160, 300)
    b = [title("Two deserts, one decision · drive time is the real cost")]
    mk = f(*CITY["Marrakech"])
    for name, col, dash in (("Merzouga", SAFFRON, "1 7"), ("Zagora", GREEN, "1 7")):
        p = f(*CITY[name])
        b.append(f'<path d="M {mk[0]:.1f} {mk[1]:.1f} L {p[0]:.1f} {p[1]:.1f}" '
                 f'fill="none" stroke="{col}" stroke-width="2.6" '
                 f'stroke-dasharray="{dash}" stroke-linecap="round"/>')
    b += minor(f, "Ouarzazate")
    b += place(f, "Marrakech", fill=GREEN)
    b += place(f, "Merzouga", fill=SAFFRON, note="Erg Chebbi · the postcard dunes",
               side="below")
    b += place(f, "Zagora", fill=GREEN, note="nearer · smaller, rockier", side="below")
    b.append(txt(W - 70, sy_note(), "true scale · drive hours are honest estimates",
                 size=9, fill=MUTED, font=MONO, anchor="end", upper=True))
    # the strip: two options side by side, each way by road
    sy = 502
    b.append(rule(70, sy, W - 70, sy, color=BRASS, w=1.4))
    b.append(txt(70, sy - 12, "Each way, by road", size=10, fill=BRASS,
                 font=MONO, ls=1.8, upper=True))
    for i, (name, hrs, gloss, col) in enumerate((
            ("Merzouga", "9–10 h", "Erg Chebbi. 150 m dunes. One night there, not two.", SAFFRON),
            ("Zagora", "6–7 h", "Rocky hammada. Nearer, and the dunes are modest.", GREEN))):
        x = 70 + i * 600
        b.append(txt(x, sy + 34, name, size=16, weight="600", fill=INK))
        b.append(txt(x + 520, sy + 34, hrs, size=12, fill=col, font=MONO,
                     anchor="end", ls=.8, upper=True))
        b.append(txt(x, sy + 58, gloss, size=12.5, fill=MUTED))
    b.append(rule(70, sy + 84, W - 70, sy + 84, color=LINE))
    b.append(txt(70, sy + 110,
                 "The drive is not the cost of the trip — it is the trip. "
                 "Budget it as a day, in both directions.", size=12.5, fill=BRASS))
    return head(b)


def fig3_year():
    """Twelve months. Chart-shaped, so the wider canvas is simply more room."""
    b = [title("The shape of the year · Marrakech–desert–Fez")]
    months = "J F M A M J J A S O N D".split()
    band = [(SLATE, .50, "mild day, cold night"), (SLATE, .50, ""),
            (SAFFRON, .55, "workable"), (GREEN, .92, "the sweet spot"),
            (GREEN, .92, ""), (BRASS, .50, "hot inland"), (BRASS, .50, ""),
            (BRASS, .50, ""), (SAFFRON, .55, ""), (GREEN, .92, ""),
            (GREEN, .92, ""), (SLATE, .50, "")]
    x0, x1, top, bh = 70, W - 70, 116, 386
    gw = (x1 - x0) / 12
    for i, (m, (col, op, _)) in enumerate(zip(months, band)):
        x = x0 + i * gw
        b.append(box(x + 3, top, gw - 6, bh, fill=col, op=op))
        b.append(txt(x + gw / 2, top + bh + 26, m, size=12, fill=INK,
                     font=MONO, anchor="middle"))
    # A legend row, not labels floating over the bars: the four bands recur
    # (the sweet spot happens twice), so naming them in place either repeats
    # itself or crowds — at this type size the spans collided outright.
    ly = top + bh + 62
    b.append(rule(x0, ly - 26, x1, ly - 26, color=LINE))
    lx = x0
    for col, op, lab in ((GREEN, .92, "the sweet spot"), (SAFFRON, .55, "workable"),
                         (BRASS, .50, "hot inland"), (SLATE, .50, "mild day, cold night")):
        b.append(box(lx, ly - 11 * SC, 13 * SC, 13 * SC, fill=col, op=op))
        b.append(txt(lx + 19 * SC, ly, lab, size=10.5, fill=INK, font=MONO,
                     ls=.9, upper=True))
        lx += (len(lab) * 7.4 + 42) * SC
    b.append(txt(x0, ly + 42,
                 "Coastal Essaouira stays mild when inland exceeds 100°F — the "
                 "one month-proof move in the book.",
                 size=12, fill=BRASS))
    return head(b)


def fig4_moneyweb():
    """Four leaks around one centre. Wide frame suits it: two leaks a side."""
    b = [title("Four leaks, one web · none of them illegal")]
    cx, cy = W / 2, 318
    b.append(dot(cx, cy, 52, "#eee6d4"))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="52" fill="none" '
             f'stroke="{BRASS}" stroke-width="1.6"/>')
    b.append(txt(cx, cy - 4, "Your", size=15, weight="600", fill=INK, anchor="middle"))
    b.append(txt(cx, cy + 16, "money", size=15, weight="600", fill=INK, anchor="middle"))
    leaks = [
        (-1, -1, "The closed currency", "you can't buy dirham before you fly"),
        (1, -1, "Dynamic conversion", "the terminal offers dollars"),
        (-1, 1, "The commission chain", "the guide is paid by the shop"),
        (1, 1, "The anchor price", "the first number is a test, not a tag"),
    ]
    for sx, sy, name, gloss in leaks:
        ex = cx + sx * 258
        ey = cy + sy * 162
        b.append(rule(cx + sx * 54, cy + sy * 22, ex - sx * 12, ey,
                      color=SAFFRON, w=2, dash="1 6", cap="round"))
        anc = "end" if sx < 0 else "start"
        tx = ex - sx * 20
        b.append(txt(tx, ey - 6, name, size=14, weight="600", fill=INK, anchor=anc))
        b.append(txt(tx, ey + 15, gloss, size=11.5, fill=MUTED, anchor=anc))
    b.append(rule(70, H - 62, W - 70, H - 62, color=LINE))
    b.append(txt(70, H - 36,
                 "Each is legal, and each is a default you must actively "
                 "refuse. Refusing all four is the skill.",
                 size=12.5, fill=BRASS))
    return head(b)


def fig5_horizons():
    """A booking calendar, earliest first. Naturally the widest figure here."""
    b = [title("What to book, and when · the whole calendar")]
    x0, x1, y = 90, W - 90, 150
    b.append(txt(x0, y - 26, "earliest", size=10, fill=MUTED, font=MONO,
                 ls=2, upper=True))
    b.append(txt(x1, y - 26, "on the day", size=10, fill=MUTED, font=MONO,
                 anchor="end", ls=2, upper=True))
    b.append(rule(x0, y, x1, y, color=BRASS, w=1.6))
    rows = [(0.00, "Open-jaw flights", "as early as you can", SAFFRON, 8.5),
            (0.30, "Medina riads · spring and autumn", "2–3 months", SAFFRON, 7.5),
            (0.52, "Desert trip · private driver", "1–2 months", GREEN, 6.5),
            (0.74, "Al Boraq high-speed seats", "weeks", GREEN, 5.5),
            (1.00, "Trains, coaches, monuments", "on the day", SLATE, 5.0)]
    for i, (t, name, when, col, r) in enumerate(rows):
        x = x0 + t * (x1 - x0)
        ry = y + 66 + i * 76
        b.append(rule(x, y + 6, x, ry - 16, color=LINE, w=1, dash="3 5"))
        b.append(dot(x, y, r, col))
        anc = "start" if t < 0.75 else "end"
        tx = x if t < 0.75 else x
        b.append(txt(tx, ry, name, size=14.5, weight="600", fill=INK, anchor=anc))
        b.append(txt(tx, ry + 21, when, size=10.5, fill=col, font=MONO,
                     anchor=anc, ls=.8, upper=True))
    b.append(txt(x0, H - 24,
                 "Almost nothing needs booking early. The two things that do "
                 "are the two that cannot be replaced on arrival.",
                 size=12.5, fill=BRASS))
    return head(b)


def fig6_third():
    """Where a fourth stop sits against the loop. 1.19:1 — panel on the right."""
    pts = {k: CITY[k] for k in ("Marrakech", "Merzouga", "Fez",
                                "Chefchaouen", "Essaouira", "Imlil")}
    f, (ox, oy, uw, uh) = projector(pts, 74, 92, 520, 480)
    b = [title("The one more thing · where each option sits")]
    mk, mz, fz = f(*CITY["Marrakech"]), f(*CITY["Merzouga"]), f(*CITY["Fez"])
    b.append(f'<path d="M {mk[0]:.1f} {mk[1]:.1f} L {mz[0]:.1f} {mz[1]:.1f} '
             f'L {fz[0]:.1f} {fz[1]:.1f}" fill="none" stroke="{LINE}" '
             f'stroke-width="7" stroke-linecap="round"/>')
    b.append(txt((mk[0] + fz[0]) / 2 - 14, (mk[1] + fz[1]) / 2,
                 "the classic loop", size=10, fill=MUTED, font=MONO,
                 anchor="middle", ls=1.4, upper=True))
    for n in ("Marrakech", "Merzouga", "Fez"):
        b += place(f, n, r=6, fill=GREEN, size=12.5)
    # Imlil sits 55 km from Marrakech — at true scale their labels collide, so
    # the three optional stops are labelled away from the loop, not above it.
    for n, label, anchor, dx, dy in (("Chefchaouen", "Chefchaouen", "middle", 0, -14),
                                     ("Essaouira", "Essaouira", "start", -4, 22),
                                     ("Imlil", "High Atlas", "middle", 0, 22)):
        x, y = f(*CITY[n])
        b.append(dot(x, y, 6, SAFFRON))
        b.append(txt(x + dx, y + dy, label, size=12.5, weight="600",
                     fill=INK, anchor=anchor))
    b.append(txt(74, H - 14, "true scale · cos(lat) corrected",
                 size=9, fill=MUTED, font=MONO, upper=True))
    b += panel(680, 100, 560, "What each one costs the loop", [
        ("Chefchaouen", "+1 night", "4 h by road from Fez, and back the same way."),
        ("Essaouira", "+0 nights", "A day trip from Marrakech. Nothing is displaced."),
        ("High Atlas", "+0 nights", "A day trip from Marrakech. Same as above."),
    ], foot="Only one of the three actually spends a night of the trip.")
    return head(b)


def fig7_transport():
    """Three tools, three jobs. Rows — the wider canvas gives the gloss room."""
    b = [title("Three tools, three jobs · not interchangeable")]
    rows = [("ONCF train", GREEN,
             "Casablanca · Rabat · Fez · Marrakech · Tangier",
             "The calm spine — but it stops where the rail line stops."),
            ("CTM / Supratours coach", SAFFRON,
             "Chefchaouen · Essaouira · the off-rail towns",
             "Fills the gaps. Small luggage fee, paid at the station."),
            ("Private driver", BRASS,
             "the desert loop · the open jaw",
             "Content, not transit — priciest, and right exactly once.")]
    y = 124
    for name, col, where, gloss in rows:
        b.append(rule(70, y - 26, W - 70, y - 26, color=LINE))
        b.append(box(70, y - 12, 5, 62, fill=col))
        b.append(txt(92, y + 4, name, size=15.5, weight="600", fill=INK))
        b.append(txt(92, y + 27, where, size=11, fill=col, font=MONO, ls=.7,
                     upper=True))
        b.append(txt(92, y + 50, gloss, size=12.5, fill=MUTED))
        y += 160
    b.append(rule(70, y - 26, W - 70, y - 26, color=BRASS, w=1.4))
    b.append(txt(70, y + 4,
                 "Match the tool to the leg. Force one tool onto every leg and "
                 "one of them costs you a day.", size=12.5, fill=BRASS))
    return head(b)


def fig8_risk():
    """Frequency, not severity. A single axis — wide by nature."""
    b = [title("Where the risk actually sits")]
    x0, x1, y = 90, W - 150, 118
    b.append(txt(x0, y - 22, "rarely happens", size=10, fill=MUTED, font=MONO,
                 ls=2, upper=True))
    b.append(txt(x1, y - 22, "happens constantly", size=10, fill=MUTED,
                 font=MONO, anchor="end", ls=2, upper=True))
    b.append(rule(x0, y, x1, y, color=LINE, w=1.6))
    rows = [("Violent crime against tourists", .05, GREEN, "rare", 5.0),
            ("Being scammed outright", .28, GREEN, "uncommon", 6.2),
            ("Aggressive touting", .62, SAFFRON, "routine", 8.0),
            ("Pickpocketing in crowds", .48, SAFFRON, "ordinary city risk", 7.0),
            ("Overcharging", .95, BRASS, "constant", 9.4)]
    for i, (name, t, col, tag, r) in enumerate(rows):
        cy = y + 62 + i * 84
        cx = x0 + t * (x1 - x0)
        b.append(rule(x0, cy, cx, cy, color=col, w=1.4, dash=None))
        b.append(dot(cx, cy, r, col))
        b.append(txt(x0, cy - 14, name, size=14, weight="600", fill=INK))
        b.append(txt(W - 70, cy - 14, tag, size=10, fill=col, font=MONO,
                     anchor="end", ls=.9, upper=True))
    b.append(rule(70, H - 58, W - 70, H - 58, color=LINE))
    b.append(txt(70, H - 32,
                 "Frequency, not severity. The advisory speaks to the top line; "
                 "your trip meets the bottom two.", size=12.5, fill=BRASS))
    return head(b)




# ═════════════════════════════════════════════════════════════════════════════
#  six chapters carried no figure at all — these are the arguments they make
# ═════════════════════════════════════════════════════════════════════════════

def fig9_entry():
    """c04. Two columns and a strip. The point is that the only hard deadline
    is imposed by airlines, not by Morocco — so nothing at the border makes
    anyone prepare, and people therefore prepare for nothing."""
    b = [title("What Morocco asks of an American passport")]
    CW = 520
    cols = [(90, "Required", GREEN,
             [("A valid passport", "that is the whole legal test"),
              ("Nothing else at the border", "no visa, no application, no fee"),
              ("Nothing paid on arrival", "admission up to 90 days, stamped")]),
            (690, "Not required", SLATE,
             [("An AEVM authorisation", "exists — not for US, UK or EU travellers"),
              ("Any advance paperwork", "which is exactly why people do none"),
              ("Any deadline at all", "no application means nothing to miss")])]
    for x, h, col, items in cols:
        b.append(txt(x, 96, h, size=10.5, fill=col, font=MONO, ls=1.8, upper=True))
        b.append(rule(x, 110, x + CW, 110, color=col, w=1.6))
        y = 164
        for name, gloss in items:
            b.append(txt(x, y, name, size=13, weight="600", fill=INK))
            b.append(txt(x, y + 18 * SC, gloss, size=10.5, fill=MUTED))
            b.append(rule(x, y + 34 * SC, x + CW, y + 34 * SC, color=LINE, w=1))
            y += 56 * SC
    sy = 452
    b.append(box(90, sy, W - 180, 96, fill="#eee6d4", stroke=SAFFRON, sw=1.6))
    b.append(txt(114, sy + 34, "The one real deadline", size=10.5, fill=SAFFRON,
                 font=MONO, ls=1.8, upper=True))
    b.append(txt(114, sy + 68, "Six months of passport validity — set by the "
                 "airline, not by Morocco.", size=13.5, weight="600", fill=INK))
    b.append(txt(90, H - 22,
                 "Because no visa forces a date, most people think about none of "
                 "it. Entry is the easy part; boarding is not.",
                 size=12, fill=BRASS))
    return head(b)


def fig10_shapes():
    """c07. Three trip shapes. Only one never repeats a leg — which is what the
    base decision is actually about."""
    b = [title("Three shapes · only one never repeats a leg")]
    x0, x1 = 150, W - 150
    shapes = [
        ("Marrakech only", [("Marrakech", 0.0)], False, GREEN,
         "One city and one Atlas day trip. No desert, no second city."),
        ("Marrakech in, Fez out", [("Marrakech", 0.0), ("Desert", 0.52), ("Fez", 1.0)],
         False, GREEN,
         "You pack once and keep moving forward. Nothing is driven twice."),
        ("One fixed base", [("Marrakech", 0.0), ("Desert", 0.52)], True, BRASS,
         "The desert road, out and back. That return leg is a day."),
    ]
    y = 132
    for name, stops, back, col, gloss in shapes:
        b.append(txt(150, y - 26 * SC, name, size=13.5, weight="600", fill=INK))
        far = max(s[1] for s in stops)
        b.append(rule(x0, y, x0 + (x1 - x0) * far, y, color=col, w=2.4))
        for label, t_ in stops:
            x = x0 + t_ * (x1 - x0)
            b.append(dot(x, y, 6, col))
            b.append(txt(x, y + 22 * SC, label, size=11, fill=MUTED, anchor="middle"))
        if back:
            xa, xz = x0 + far * (x1 - x0), x0
            b.append(f'<path d="M {xa:.1f} {y - 12 * SC:.1f} '
                     f'Q {(xa + xz) / 2:.1f} {y - 46 * SC:.1f} {xz:.1f} {y - 12 * SC:.1f}" '
                     f'fill="none" stroke="{BRASS}" stroke-width="{2.2 * SC:.2f}" '
                     f'stroke-dasharray="{3 * SC:.1f} {5 * SC:.1f}"/>')
            b.append(txt((xa + xz) / 2, y - 50 * SC, "driven back", size=10.5,
                         fill=BRASS, font=MONO, anchor="middle", ls=.8, upper=True))
        b.append(txt(x1, y - 26 * SC, gloss, size=11, fill=MUTED, anchor="end"))
        y += 156
    b.append(rule(90, H - 62, W - 90, H - 62, color=BRASS, w=1.4))
    b.append(txt(90, H - 32,
                 "The base question is really: which city do you end in? That is "
                 "the one the open-jaw ticket turns on.", size=12.5, fill=BRASS))
    return head(b)


def fig11_payment():
    """c11. Two guides, two directions of payment. Follow the arrow."""
    b = [title("Follow the money, not the badge alone")]
    lanes = [(160, "The licensed guide", GREEN,
              ("You", "pay a rate agreed in advance"),
              ("The guide", "works for whoever paid him"),
              "So his interest is showing you the city well — that is the transaction "
              "you bought."),
             (400, "The faux guide", BRASS,
              ("The shop", "pays a commission on what you buy"),
              ("The guide", "works for whoever paid him"),
              "So his interest is delivering you to the shop, not showing you "
              "anything at all.")]
    BW, GAP = 250, 90
    for y, name, col, left, right, gloss in lanes:
        b.append(txt(90, y - 52 * SC, name, size=14, weight="600", fill=INK))
        x = 90
        for who, what in (left, right):
            b.append(box(x, y - 26 * SC, BW * SC, 52 * SC, fill="none",
                         stroke=col, sw=1.4))
            b.append(txt(x + BW * SC / 2, y - 4 * SC, who, size=12.5,
                         weight="600", fill=INK, anchor="middle"))
            b.append(txt(x + BW * SC / 2, y + 14 * SC, what, size=10.5,
                         fill=MUTED, anchor="middle"))
            if who == left[0]:
                ax = x + BW * SC
                b.append(rule(ax + 10, y, ax + GAP * SC - 26, y, color=col, w=2.4))
                b.append(f'<path d="M {ax + GAP * SC - 26:.1f} {y - 7 * SC:.1f} '
                         f'L {ax + GAP * SC - 4:.1f} {y:.1f} '
                         f'L {ax + GAP * SC - 26:.1f} {y + 7 * SC:.1f} Z" fill="{col}"/>')
            x += (BW + GAP) * SC
        b.append(txt(90, y + 58 * SC, gloss, size=11.5, fill=col))
    b.append(rule(90, H - 76, W - 90, H - 76, color=BRASS, w=1.4))
    b.append(txt(90, H - 44,
                 "Both men know the city. Only one of them is paid by you, and "
                 "that is the entire difference.", size=12.5, fill=BRASS))
    b.append(txt(90, H - 18, "Ask to see the badge. A genuine guide shows it "
                 "without hesitating.", size=11, fill=MUTED))
    return head(b)


def fig12_queue():
    """c12. Two axes, and one quadrant that answers both worries at once."""
    b = [title("The queue is a review that cannot be bought")]
    L, R, T, B_ = 430, 870, 110, 470
    b.append(box(L, T, R - L, B_ - T, fill="none", stroke=LINE, sw=1.2))
    b.append(rule((L + R) / 2, T, (L + R) / 2, B_, color=LINE, w=1))
    b.append(rule(L, (T + B_) / 2, R, (T + B_) / 2, color=LINE, w=1))
    b.append(txt((L + R) / 2, T - 20 * SC, "high turnover", size=10.5, fill=MUTED,
                 font=MONO, anchor="middle", ls=1.4, upper=True))
    b.append(txt((L + R) / 2, B_ + 32 * SC, "the food sits", size=10.5, fill=MUTED,
                 font=MONO, anchor="middle", ls=1.4, upper=True))
    for xx, anc, lab in ((L - 26 * SC, "end", "the menu faces locals"),
                         (R + 26 * SC, "start", "the menu faces visitors")):
        b.append(txt(xx, (T + B_) / 2, lab, size=10.5, fill=MUTED, font=MONO,
                     anchor=anc, ls=1.4, upper=True))
    # label OUTSIDE the grid, gloss under it — inside the cell there is not
    # room for either at a readable size.
    marks = [(.75, .25, "The busy local stall", GREEN, 9, "start", 1,
              "Answers both worries at once"),
             (.25, .25, "The quiet local place", SAFFRON, 6, "end", -1,
              "Fair value; the food has waited"),
             (.75, .75, "The main-square terrace", BRASS, 6, "start", 1,
              "Busy — priced for people passing"),
             (.25, .75, "The “cooperative”", BRASS, 6, "end", -1,
              "Someone is paid to bring you")]
    for tx, ty, label, col, r, anc, sgn, gloss in marks:
        x = L + tx * (R - L)
        y = T + ty * (B_ - T)
        b.append(dot(x, y, r, col))
        lx = x + sgn * 118 * SC
        b.append(rule(x + sgn * (r + 4) * SC, y, lx - sgn * 10 * SC, y,
                      color=col, w=1, dash=f"{3*SC:.1f} {4*SC:.1f}"))
        b.append(txt(lx, y - 3 * SC, label, size=12.5, weight="600", fill=INK,
                     anchor=anc))
        b.append(txt(lx, y + 15 * SC, gloss, size=10.5, fill=MUTED, anchor=anc))
    b.append(rule(90, H - 62, W - 90, H - 62, color=BRASS, w=1.4))
    b.append(txt(90, H - 32,
                 "One quadrant settles hygiene and value with the same "
                 "observation. Look for the line.",
                 size=12.5, fill=BRASS))
    return head(b)


def fig13_arrival():
    """c17. Four problems land at once, each with an answer you can settle now.
    Four columns — stacking the two answers under a shared timeline put every
    label on top of its neighbour."""
    b = [title("The first three hours · decided now, or decided tired")]
    x0, y = 96, 150
    CW = (W - 2 * x0) / 4
    b.append(rule(x0, y, W - x0, y, color=BRASS, w=1.6))
    steps = [("Landing", "An eSIM, bought before you left home",
              "Twenty minutes, your passport, and a queue"),
             ("The first cash", "A bank ATM in the arrivals hall",
              "A kiosk, and “charge in dollars” accepted"),
             ("The ride in", "A transfer your riad arranged, price agreed",
              "A fare haggled while holding your luggage"),
             ("The last lane", "Someone meets you and walks you in",
              "A car that cannot reach the door")]
    for i, (name, good, bad) in enumerate(steps):
        cx = x0 + i * CW + CW / 2
        b.append(dot(cx, y, 7, GREEN))
        b.append(txt(cx, y - 24 * SC, name, size=13, weight="600", fill=INK,
                     anchor="middle"))
        if i:
            b.append(rule(x0 + i * CW, y - 52 * SC, x0 + i * CW, H - 96,
                          color=LINE, w=1))
        b.append(wrap(cx - CW / 2 + 22, y + 56 * SC, CW - 44, good,
                      size=11.5, fill=GREEN))
        b.append(wrap(cx - CW / 2 + 22, y + 176 * SC, CW - 44, bad,
                      size=11.5, fill=BRASS))
    b.append(txt(x0, y + 56 * SC - 26 * SC, "decided now", size=10, fill=GREEN,
                 font=MONO, ls=1.4, upper=True))
    b.append(txt(x0, y + 176 * SC - 26 * SC, "decided tired", size=10, fill=BRASS,
                 font=MONO, ls=1.4, upper=True))
    b.append(rule(90, H - 76, W - 90, H - 76, color=BRASS, w=1.4))
    b.append(txt(90, H - 44,
                 "The web works on people solving four problems at once with "
                 "luggage in their hands.", size=12.5, fill=BRASS))
    b.append(txt(90, H - 18,
                 "Every answer on the top row can be settled weeks earlier, from "
                 "your sofa.", size=11, fill=MUTED))
    return head(b)


def fig14_customs():
    """c18. All four habits are cheap AND noticed. That clustering is the
    argument — not the list, which the chapter already gives in a table."""
    b = [title("Four habits · all of them cost nothing")]
    L, R, T, B_ = 330, 970, 112, 474
    b.append(box(L, T, R - L, B_ - T, fill="none", stroke=LINE, sw=1.2))
    for i in (1, 2):
        b.append(rule(L + i * (R - L) / 3, T, L + i * (R - L) / 3, B_, color=LINE, w=1))
        b.append(rule(L, T + i * (B_ - T) / 3, R, T + i * (B_ - T) / 3, color=LINE, w=1))
    b.append(box(L, T, (R - L) / 3, (B_ - T) / 3, fill=GREEN, op=.07))
    b.append(txt(L, T - 20 * SC, "costs you nothing", size=10.5, fill=MUTED,
                 font=MONO, ls=1.4, upper=True))
    b.append(txt(R, T - 20 * SC, "costs you effort", size=10.5, fill=MUTED,
                 font=MONO, anchor="end", ls=1.4, upper=True))
    b.append(txt(L - 24 * SC, T + 8 * SC, "noticed", size=10.5, fill=MUTED,
                 font=MONO, anchor="end", ls=1.4, upper=True))
    b.append(txt(L - 24 * SC, B_, "unnoticed", size=10.5, fill=MUTED,
                 font=MONO, anchor="end", ls=1.4, upper=True))
    marks = [(.08, .07, "Dress modestly", "shoulders and knees, looser not tighter"),
             (.18, .30, "Carry a light scarf", "one outfit, two contexts"),
             (.06, .53, "Right hand to eat and give", "nobody corrects you — which is why it lands"),
             (.20, .76, "Ask before photographing", "in a market a camera is a transaction")]
    for tx, ty, label, gloss in marks:
        x, y = L + tx * (R - L), T + ty * (B_ - T)
        b.append(dot(x, y, 7, GREEN))
        b.append(txt(x + 18 * SC, y - 3 * SC, label, size=12.5, weight="600", fill=INK))
        b.append(txt(x + 18 * SC, y + 14 * SC, gloss, size=10.5, fill=MUTED))
    # the overcorrection, plotted where it belongs: expensive and unnoticed
    ox, oy = L + .70 * (R - L), T + .90 * (B_ - T)
    b.append(dot(ox, oy, 7, BRASS))
    b.append(txt(ox + 18 * SC, oy - 3 * SC, "Dressing as a costume", size=12.5,
                 weight="600", fill=INK))
    b.append(txt(ox + 18 * SC, oy + 14 * SC, "nobody asked for this", size=10.5,
                 fill=BRASS))
    b.append(rule(90, H - 62, W - 90, H - 62, color=BRASS, w=1.4))
    b.append(txt(90, H - 32,
                 "Every habit worth having sits in one corner: free, and noticed. "
                 "The aim is respect, not performance.", size=12.5, fill=BRASS))
    return head(b)

FIGURES = {
    "fig1-route.svg":     fig1_route,
    "fig2-desert.svg":    fig2_desert,
    "fig3-year.svg":      fig3_year,
    "fig4-moneyweb.svg":  fig4_moneyweb,
    "fig5-horizons.svg":  fig5_horizons,
    "fig6-third.svg":     fig6_third,
    "fig7-transport.svg": fig7_transport,
    "fig8-risk.svg":      fig8_risk,
    "fig9-entry.svg":     fig9_entry,
    "fig10-shapes.svg":   fig10_shapes,
    "fig11-payment.svg":  fig11_payment,
    "fig12-queue.svg":    fig12_queue,
    "fig13-arrival.svg":  fig13_arrival,
    "fig14-customs.svg":  fig14_customs,
}


def main():
    apply = "--apply" in sys.argv
    print(f"standard canvas {W}x{H}  (ratio {W/H:.3f} → {6.92:.2f} x "
          f"{6.92*H/W:.2f}in in the column)\n")
    for name, fn in FIGURES.items():
        svg = fn()
        path = os.path.join(HERE, name)
        old = os.path.getsize(path) if os.path.exists(path) else 0
        if apply:
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"   {name:<20} {len(svg):>6} bytes  (was {old})"
              f"{'  WRITTEN' if apply else ''}")
    print(("\nWROTE " if apply else "\nDRY RUN — pass --apply to write. ")
          + f"{len(FIGURES)} figures, all at {W}x{H}.")


if __name__ == "__main__":
    main()
