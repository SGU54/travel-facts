#!/usr/bin/env python3
"""figs2.py — the five diagrams the decisions were missing.

Four of the eight decisions carried a drawn figure; five did not, and those five
ran as unbroken prose. Each diagram here has to argue something the paragraphs
would otherwise have to carry alone — a figure that merely decorates is worse
than the white space it replaces.

Canvas: 652 wide, matching the book's existing drawn figures (they ship as
atomic <img> at width="652", because Paged.js fragments inline SVG). Height
varies per figure: these are instruments, not a fixed band.

Palette and type are the book's own — accent #D81264, deep #9C0C48,
ink #241A21, muted #6B5F66, rule #DCCFC0 on #F7F1E4 paper.
"""
import os

W = 652
PAPER, INK = "#F7F1E4", "#241A21"
ACCENT, DEEP = "#D81264", "#9C0C48"
MUTED, RULE = "#6B5F66", "#DCCFC0"
PANEL = "#EFE5D2"
SANS = "'Archivo','Helvetica Neue',sans-serif"

HERE = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, *, size=11, fill=INK, anchor="start", weight="400", ls=None,
        upper=False, style=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    w = f' font-weight="{weight}"' if weight != "400" else ""
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}"{a} font-family="{SANS}" '
            f'font-size="{size}"{w}{l}{st} fill="{fill}">'
            f'{esc(s.upper() if upper else s)}</text>')


def rule(x1, y1, x2, y2, *, color=RULE, w=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{w}"{d}/>')


def box(x, y, w, h, *, fill="none", stroke=None, sw=1, op=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'fill="{fill}"{s}{o}/>')


def tick(x, y, ok):
    """A pass or fail mark, in the book's own two colours."""
    if ok:
        return (f'<path d="M {x-4:.1f} {y:.1f} L {x-1:.1f} {y+3.5:.1f} '
                f'L {x+5:.1f} {y-4:.1f}" fill="none" stroke="{DEEP}" '
                f'stroke-width="2" stroke-linecap="round"/>')
    return (f'<path d="M {x-4:.1f} {y-4:.1f} L {x+4:.1f} {y+4:.1f} '
            f'M {x+4:.1f} {y-4:.1f} L {x-4:.1f} {y+4:.1f}" fill="none" '
            f'stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>')


def head(body, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" '
            f'width="{W}" height="{h}">\n'
            f'<rect width="{W}" height="{h}" fill="{PAPER}"/>\n'
            + "\n".join(body) + "\n</svg>\n")


# ── c01 · what you may drive ─────────────────────────────────────────────────
def fig_drive():
    """Four gates, two vehicles. The scooter fails the two that matter, and the
    failure is the same failure twice — the endorsement is what the insurer
    reads."""
    H = 292
    b = [txt(0, 16, "Four gates. The car clears them; the scooter clears two.",
             size=11.5, fill=MUTED)]
    cols = [("Home licence", 150), ("IDP 1949", 250), ("Motorcycle\nendorsement", 370),
            ("Insurer pays", 520)]
    y0 = 56
    for name, x in cols:
        for i, line in enumerate(name.split("\n")):
            b.append(txt(x, y0 + i * 12, line, size=9, fill=MUTED,
                         anchor="middle", ls=.8, upper=True))
    b.append(rule(0, y0 + 26, W, y0 + 26, color=INK, w=1.4))
    rows = [("Car", [True, True, None, True],
             "the ordinary licence you already hold"),
            ("Scooter", [True, True, False, False],
             "and the endorsement is the gate the insurer reads")]
    y = y0 + 62
    for label, marks, note in rows:
        b.append(txt(0, y, label, size=15, weight="600", fill=INK))
        for (name, x), ok in zip(cols, marks):
            if ok is None:
                b.append(txt(x, y, "n/a", size=9.5, fill=MUTED, anchor="middle"))
            else:
                b.append(tick(x, y - 4, ok))
        b.append(txt(0, y + 20, note, size=11, fill=MUTED))
        b.append(rule(0, y + 34, W, y + 34))
        y += 62
    b.append(txt(0, y + 10,
                 "The third gate is the whole decision: without the endorsement the "
                 "ride is uninsured,", size=11.5, fill=DEEP))
    b.append(txt(0, y + 26,
                 "not merely unlicensed — and that is a hospital bill, not a fine.",
                 size=11.5, fill=DEEP))
    return head(b, H)


# ── c05 · what you are exposed to ────────────────────────────────────────────
def fig_exposure():
    """The exposure people insure against is not the one that empties the
    account. Drawn on one axis so the gap is the argument."""
    H = 284
    b = [txt(0, 16, "What people insure for, against what actually costs.",
             size=11.5, fill=MUTED)]
    x0, x1, y = 130, W - 40, 62
    b.append(txt(x0, y - 18, "cheap", size=9, fill=MUTED, ls=.8, upper=True))
    b.append(txt(x1, y - 18, "ruinous", size=9, fill=MUTED, anchor="end",
                 ls=.8, upper=True))
    b.append(rule(x0, y, x1, y, color=INK, w=1.2))
    items = [("A stolen phone", .04, MUTED, "what the policy is bought for"),
             ("A clinic visit", .12, MUTED, "paid at the desk, reclaimed later"),
             ("A night in hospital", .38, ACCENT, "paid before discharge"),
             ("Air evacuation", .95, ACCENT, "the line item the policy exists for")]
    yy = y + 40
    for name, t, col, note in items:
        cx = x0 + t * (x1 - x0)
        b.append(rule(x0, yy, cx, yy, color=col, w=1.6))
        b.append(f'<circle cx="{cx:.1f}" cy="{yy:.1f}" r="5" fill="{col}"/>')
        b.append(txt(0, yy + 4, name, size=12.5, weight="600", fill=INK))
        b.append(txt(x1, yy - 10, note, size=9.5, fill=MUTED, anchor="end"))
        yy += 34
    b.append(rule(0, yy + 2, W, yy + 2))
    b.append(txt(0, yy + 22,
                 "Only the bottom two are worth a policy, and only one of them "
                 "is why you read the exclusions.", size=11.5, fill=DEEP))
    return head(b, H)


# ── c06 · Bangkok, where to sleep ────────────────────────────────────────────
def fig_bangkok():
    """Central is not the variable. Being on the rail line is."""
    H = 240
    b = [txt(0, 16, "Where you sleep is a rail question, not a map question.",
             size=11.5, fill=MUTED)]
    L, R, T, B = 150, W - 110, 48, 176
    b.append(box(L, T, R - L, B - T, stroke=RULE))
    b.append(rule((L + R) / 2, T, (L + R) / 2, B, color=RULE))
    b.append(rule(L, (T + B) / 2, R, (T + B) / 2, color=RULE))
    b.append(box(L, T, (R - L) / 2, (B - T) / 2, fill=PANEL, op=.85))
    b.append(txt((L + R) / 2, T - 12, "on the BTS or MRT", size=9, fill=MUTED,
                 anchor="middle", ls=.8, upper=True))
    b.append(txt((L + R) / 2, B + 22, "off the line", size=9, fill=MUTED,
                 anchor="middle", ls=.8, upper=True))
    b.append(txt(L - 12, T + 14, "looks central", size=9, fill=MUTED,
                 anchor="end", ls=.8, upper=True))
    b.append(txt(L - 12, B - 6, "looks far", size=9, fill=MUTED,
                 anchor="end", ls=.8, upper=True))
    marks = [(.26, .28, "Sukhumvit / Silom", DEEP, "central and on the line"),
             (.74, .30, "Riverside", ACCENT, "central, and a boat or a jam away"),
             (.26, .74, "Ari / Phaya Thai", DEEP, "further out, and quicker"),
             (.74, .78, "Khao San", ACCENT, "neither")]
    for tx, ty, name, col, note in marks:
        x = L + tx * (R - L)
        y = T + ty * (B - T)
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{col}"/>')
        b.append(txt(x, y - 10, name, size=10.5, weight="600", fill=INK,
                     anchor="middle"))
        b.append(txt(x, y + 16, note, size=8.5, fill=MUTED, anchor="middle"))
    b.append(rule(0, B + 42, W, B + 42))
    b.append(txt(0, H - 10,
                 "The top-left quadrant is the whole answer; the rest is a taxi "
                 "sitting still.", size=11.5, fill=DEEP))
    return head(b, H)


# ── c07 · the temple door, and the elephant ──────────────────────────────────
def fig_door():
    """Two gates that look alike and are not. One is binary and enforced at a
    door; the other is a spectrum nobody enforces at all."""
    H = 238
    b = [txt(0, 16, "One is checked at a door. The other is never checked.",
             size=11.5, fill=MUTED)]
    # left: the door — binary
    b.append(txt(0, 52, "The temple door", size=13, weight="600", fill=INK))
    b.append(box(0, 64, 250, 96, fill=PANEL))
    b.append(rule(125, 64, 125, 160, color=RULE))
    b.append(txt(62, 88, "admitted", size=9, fill=DEEP, anchor="middle",
                 ls=.8, upper=True))
    b.append(txt(188, 88, "turned away", size=9, fill=ACCENT, anchor="middle",
                 ls=.8, upper=True))
    b.append(txt(62, 114, "shoulders", size=11, fill=INK, anchor="middle"))
    b.append(txt(62, 130, "and knees covered", size=11, fill=INK, anchor="middle"))
    b.append(txt(188, 114, "anything less,", size=11, fill=INK, anchor="middle"))
    b.append(txt(188, 130, "at the busy sites", size=11, fill=INK, anchor="middle"))
    b.append(txt(0, 180, "Binary, and settled before you arrive.",
                 size=10.5, fill=MUTED))
    # right: the elephant — a spectrum
    b.append(txt(300, 52, "The elephant venue", size=13, weight="600", fill=INK))
    x0, x1, y = 300, W - 18, 104
    b.append(rule(x0, y, x1, y, color=INK, w=1.2))
    for t, lab, col in ((0.0, "riding", ACCENT), (0.45, "bathing", MUTED),
                        (1.0, "observation only", DEEP)):
        x = x0 + t * (x1 - x0)
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{col}"/>')
        anc = "start" if t == 0 else ("end" if t == 1 else "middle")
        b.append(txt(x, y - 12, lab, size=10, fill=col, anchor=anc))
    b.append(txt(x0, y + 26, "No door, no check, and every venue calls itself",
                 size=10.5, fill=MUTED))
    b.append(txt(x0, y + 40, "a sanctuary. The word carries no standard.",
                 size=10.5, fill=MUTED))
    b.append(txt(x0, 180, "A spectrum, and it is yours to place yourself on.",
                 size=10.5, fill=MUTED))
    b.append(rule(0, 200, W, 200))
    b.append(txt(0, 222,
                 "Confusing the two is the error: people dress for the temple and "
                 "improvise the elephant.", size=11.5, fill=DEEP))
    return head(b, H)


# ── c08 · ordering well ──────────────────────────────────────────────────────
def fig_eating():
    """Four layers. The one that cannot be booked is the one worth eating in,
    which is why a booking-shaped plan selects against it."""
    H = 300
    b = [txt(0, 16, "Four layers, and the bookable ones are the weakest.",
             size=11.5, fill=MUTED)]
    rows = [("The hotel restaurant", 1.0, 0.25, "bookable from home"),
            ("The tourist-strip kitchen", 0.85, 0.35, "bookable, and priced for it"),
            ("The shophouse", 0.25, 0.80, "walk in, one page of menu"),
            ("The stall", 0.0, 1.0, "no booking exists to make")]
    x0, x1 = 250, W - 70
    y = 60
    for name, bookable, quality, note in rows:
        b.append(txt(0, y + 4, name, size=12.5, weight="600", fill=INK))
        b.append(txt(0, y + 20, note, size=9.5, fill=MUTED))
        bw = (x1 - x0) * bookable
        qw = (x1 - x0) * quality
        b.append(box(x0, y - 8, bw, 9, fill=MUTED, op=.55))
        b.append(box(x0, y + 5, qw, 9, fill=ACCENT, op=.85))
        y += 44
    b.append(rule(0, y - 8, W, y - 8))
    b.append(box(x0, y + 6, 14, 8, fill=MUTED, op=.55))
    b.append(txt(x0 + 20, y + 14, "how bookable", size=9.5, fill=MUTED))
    b.append(box(x0 + 120, y + 6, 14, 8, fill=ACCENT, op=.85))
    b.append(txt(x0 + 140, y + 14, "how good", size=9.5, fill=MUTED))
    b.append(txt(0, y + 40,
                 "The two bars run opposite. Any plan built on reservations "
                 "selects the top two rows.", size=11.5, fill=DEEP))
    return head(b, H)


FIGURES = {
    "fig-drive.svg":    fig_drive,
    "fig-exposure.svg": fig_exposure,
    "fig-bangkok.svg":  fig_bangkok,
    "fig-door.svg":     fig_door,
    "fig-eating.svg":   fig_eating,
}


def main():
    out = os.path.join(HERE, "img")
    os.makedirs(out, exist_ok=True)
    for name, fn in FIGURES.items():
        svg = fn()
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(svg)
        h = svg.split('height="')[-1].split('"')[0]
        print(f"   {name:<20}{len(svg):>6} bytes   652 x {h}")


if __name__ == "__main__":
    main()
