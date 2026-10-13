"""figures_new.py — FIG.4-8, our own artwork, drawn from the batch fact blocks.

Every one argues something the free corpus states nowhere in one place, and every
one is drawn from real values (real 2027 dates; the actual NULLs in the fact
blocks). The recurring device is deliberate: where a figure would print a number,
and no authority publishes one, the figure prints the ABSENCE — that is the
book's organising fact rendered as a drawing rather than asserted as a sentence.

Mono is the apparatus face; the accent carries the load-bearing element only.
"""
import datetime as _dt
from design import P

MONO = "Space Mono, monospace"
BODY = "Gelasio, Georgia, serif"


# ---------------------------------------------------------------- helpers
def _w(text, fs, ls=0.0):
    """Space Mono is monospace: advance is a fixed fraction of the em."""
    return len(text) * (fs * 0.6 + ls)


def _t(x, y, s, fs=11, fill=None, anchor="start", ls=0.0, face=MONO, weight=None,
       style=None, op=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    w = f' font-weight="{weight}"' if weight else ""
    st = f' font-style="{style}"' if style else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}"{a} font-family="{face}" font-size="{fs}"'
            f'{l}{w}{st} fill="{fill or P["ink"]}"{o}>{s}</text>')


def _box(x, y, w, h, fill="none", stroke=None, sw=1.0, dash=None, op=None, r=0):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    rr = f' rx="{r}"' if r else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{rr} '
            f'fill="{fill}" stroke="{stroke or "none"}" stroke-width="{sw}"{d}{o}/>')


def _line(x1, y1, x2, y2, stroke=None, sw=1.0, dash=None, op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke or P["ink"]}" stroke-width="{sw}"{d}{o}/>')


def _svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">{body}</svg>')


# ================================================================ FIG.4  D-01
def fig_connection():
    """Transit reality: draw the HOLE where the published minimum should be.

    transit.ist_minimum_connection_time = NULL, transit.saw_minimum_connection_time
    = NULL — in BOTH models. The figure prints that null as a gap you can see.
    """
    W, H = 800, 396
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736

    # ---- lane A: one ticket
    yA = 96
    o += [_t(92, yA - 26, "ONE TICKET", 10, P["accent"], ls=2.4, weight=700),
          _t(214, yA - 26, "the carrier chose the gap, and underwrites it", 9.5,
             P["muted"], ls=0.6)]
    o += [_box(L, yA, R - L, 34, fill=P["zone"], stroke=P["line"], sw=1)]
    o += [_t(L + 14, yA + 22, "ARRIVE", 10, P["ink"], ls=1.4),
          _t((L + R) / 2, yA + 22, "CARRIER'S OWN MINIMUM APPLIES", 10, P["ink"],
             anchor="middle", ls=1.4),
          _t(R - 14, yA + 22, "DEPART", 10, P["ink"], anchor="end", ls=1.4)]
    o += [_t(L, yA + 56, "Miss it and the carrier re-routes or refunds — its rule, its risk.",
             11, P["read"], face=BODY)]

    # ---- lane B: separate tickets
    yB = 228
    o += [_t(92, yB - 52, "SEPARATE TICKETS", 10, P["accent"], ls=2.4, weight=700),
          _t(300, yB - 52, "nobody has chosen the gap", 9.5, P["muted"], ls=0.6)]

    steps = ["ARRIVE", "PASSPORT", "RECLAIM BAG", "RE-CHECK", "SECURITY", "DEPART"]
    n = len(steps)
    seg = (R - L) / n
    for i, s in enumerate(steps):
        x = L + i * seg
        o.append(_box(x, yB, seg, 34, fill="none", stroke=P["line"], sw=1))
        o.append(_t(x + seg / 2, yB + 22, s, 8.5, P["ink"], anchor="middle", ls=0.8))
    o.append(_box(L, yB, R - L, 34, fill="none", stroke=P["ink"], sw=1.2))

    # the bracket over the whole span — this is the hole
    yb = yB - 12
    o += [_line(L, yb, R, yb, P["accent"], 2.2),
          _line(L, yb, L, yb + 8, P["accent"], 2.2),
          _line(R, yb, R, yb + 8, P["accent"], 2.2)]
    o.append(_t((L + R) / 2, yb - 9, "HOW LONG DOES THIS NEED TO BE?", 11,
                P["accent"], anchor="middle", ls=2.0, weight=700))

    o += [_t(L, yB + 62, "No published minimum connection time exists at Istanbul Airport,", 11,
             P["read"], face=BODY),
          _t(L, yB + 80, "and none at Sabiha Gökçen — for any connection type, in either direction.", 11,
             P["read"], face=BODY),
          _t(L, yB + 104, "The figures in circulation trace back to neither airport operator nor the regulator.", 11,
             P["ink"], face=BODY, style="italic")]

    o.append(_line(L, H - 34, R, H - 34, P["line"], 1))
    o.append(_t(L, H - 16, "SOURCE: SHY-YOLCU · BOTH AIRPORT OPERATORS PUBLISH NO FIGURE", 8,
                P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


# ================================================================ FIG.5  D-02
def fig_exposure():
    """The exposure ladder: four rungs, and the price of three of them is NULL
    in the fact block (er_visit, fracture, inpatient_night, walkin_clinic)."""
    W, H = 800, 444
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    cx1, cx2 = 330, 545          # column starts: WHAT IT COSTS / WHAT A POLICY ANSWERS

    o += [_t(L, 44, "WHERE YOU LAND", 9, P["muted"], ls=2.2),
          _t(cx1, 44, "PUBLISHED PRICE", 9, P["muted"], ls=2.2),
          _t(cx2, 44, "WHAT A STANDARD POLICY ANSWERS", 9, P["muted"], ls=2.2)]
    o.append(_line(L, 54, R, 54, P["ink"], 1.2))

    rungs = [
        ("NÖBETÇI PHARMACY", "24h duty rota, by district",
         "n/a", "out of pocket, trivial"),
        ("ECZANE", "dispenses without prescription",
         "n/a", "out of pocket"),
        ("WALK-IN CLINIC", "private, same day",
         None, "reimbursed on receipts"),
        ("PRIVATE HOSPITAL", "estimate, deposit, prepayment",
         None, "often SECONDARY to your US plan"),
        ("INPATIENT NIGHT", "private room",
         None, "direct billing only if pre-approved"),
        ("AIR AMBULANCE", "repatriation",
         None, "the line that decides the trip"),
    ]
    y = 82
    for name, sub, price, ans in rungs:
        o.append(_t(L, y, name, 10.5, P["ink"], ls=1.2, weight=700))
        o.append(_t(L, y + 14, sub, 9, P["muted"], ls=0.4))
        if price:
            o.append(_t(cx1, y, price, 10, P["muted"], ls=1.0))
        else:
            # the NULL, drawn
            o.append(_line(cx1, y - 4, cx1 + 132, y - 4, P["accent"], 1.4))
            o.append(_t(cx1, y + 14, "NOT PUBLISHED", 8.5, P["accent"], ls=1.6))
        o.append(_t(cx2, y, ans, 9.5, P["read"], ls=0.4))
        o.append(_line(L, y + 26, R, y + 26, P["line"], 0.8))
        y += 46

    o.append(_t(L, y + 16,
                "Ballooning, scooters and quads, diving and tandem paragliding are the standard",
                11, P["read"], face=BODY))
    o.append(_t(L, y + 34,
                "exclusions — the activities a first trip is most likely to buy.", 11,
                P["ink"], face=BODY, style="italic"))

    o.append(_line(L, H - 30, R, H - 30, P["line"], 1))
    o.append(_t(L, H - 12,
                "SOURCE: 2025 HEALTH-TOURISM REGULATION · STANDARD US TRAVEL-POLICY WORDINGS", 8,
                P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


# ================================================================ FIG.6  D-04
def fig_export_gate():
    """The export gate. The whole point: customs.age_threshold is
    'No fixed numerical age or cut-off date is stated' — so the tree has no
    numeric branch, which is exactly what the traveller expects to find."""
    W, H = 800, 424
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    midx = (L + R) / 2

    o.append(_box(midx - 150, 34, 300, 40, fill=P["zone"], stroke=P["ink"], sw=1.2))
    o.append(_t(midx, 59, "THE OBJECT IN YOUR HAND", 11, P["ink"], anchor="middle", ls=2.0,
                weight=700))

    o.append(_line(midx, 74, midx, 104, P["ink"], 1.4))
    o.append(_box(midx - 232, 104, 464, 52, fill="none", stroke=P["accent"], sw=1.6))
    o.append(_t(midx, 126, "IS IT OF A PREHISTORIC OR HISTORIC PERIOD,", 10.5, P["accent"],
                anchor="middle", ls=1.4, weight=700))
    o.append(_t(midx, 144, "AND OF CULTURAL OR SCIENTIFIC VALUE?", 10.5, P["accent"],
                anchor="middle", ls=1.4, weight=700))

    o.append(_t(midx + 244, 134, "NO AGE", 9, P["accent"], anchor="start", ls=1.4))
    o.append(_t(midx + 244, 148, "IS STATED", 9, P["accent"], anchor="start", ls=1.4))

    # branches
    yb = 156
    o.append(_line(midx, yb, midx, yb + 22, P["ink"], 1.2))
    o.append(_line(L + 92, yb + 22, R - 92, yb + 22, P["ink"], 1.2))
    for x in (L + 92, R - 92):
        o.append(_line(x, yb + 22, x, yb + 44, P["ink"], 1.2))

    def leaf(x0, title, colour, lines):
        b = [_box(x0, yb + 44, 260, 40, fill="none", stroke=colour, sw=1.4),
             _t(x0 + 130, yb + 69, title, 10.5, colour, anchor="middle", ls=1.8, weight=700)]
        yy = yb + 108
        for ln in lines:
            b.append(_t(x0, yy, ln, 9.5, P["read"], ls=0.3))
            yy += 17
        return b

    o += leaf(L - 38, "YES — PROTECTED", P["accent"], [
        "Export prohibited in principle (Art. 32).",
        "Only a state museum's classification decides.",
        "A vendor's certificate has no legal force.",
        "Unauthorised export: 5 to 12 years.",
    ])
    o += leaf(R - 222, "NO — ORDINARY GOODS", P["ink"], [
        "Leaves with you; declare it regardless.",
        "$800 US personal exemption, 48h abroad.",
        "A receipt proves price, never permission.",
        "US bars archaeological material to 2031.",
    ])

    o.append(_line(L, H - 54, R, H - 54, P["line"], 1))
    o.append(_t(midx, H - 34,
                "The traveller looks for the age that separates the two boxes. Turkish law states none.",
                11, P["ink"], anchor="middle", face=BODY, style="italic"))
    o.append(_t(L, H - 12,
                "SOURCE: LAW 2863 ARTICLES 3, 23, 25, 32 · US CULTURAL PROPERTY RESTRICTION", 8,
                P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


# ================================================================ FIG.7  TIMING
def fig_calendar():
    """The month strip, computed from the real 2027 dates in batch-17."""
    W, H = 800, 286
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    y0, band = 118, 40

    start = _dt.date(2027, 1, 1)
    end = _dt.date(2027, 6, 30)
    span = (end - start).days

    def x(d):
        return L + (d - start).days / span * (R - L)

    # month ticks
    for m in range(1, 7):
        d = _dt.date(2027, m, 1)
        o.append(_line(x(d), y0 - 10, x(d), y0 + band + 10, P["line"], 1))
        o.append(_t(x(d) + 5, y0 - 44, d.strftime("%B").upper(), 9, P["muted"], ls=1.8))
    o.append(_box(L, y0, R - L, band, fill=P["zone"], stroke=P["line"], sw=1))

    def mark(a, b, label, colour, above=True, hatch=False):
        xa, xb = x(a), x(b)
        blk = [_box(xa, y0, max(xb - xa, 2), band, fill=colour, op=0.16 if hatch else 0.30)]
        blk.append(_line(xa, y0, xa, y0 + band, colour, 1.6))
        blk.append(_line(xb, y0, xb, y0 + band, colour, 1.6))
        ly = y0 - 16 if above else y0 + band + 30
        blk.append(_t((xa + xb) / 2, ly, label, 9.5, colour, anchor="middle", ls=1.4,
                      weight=700))
        return blk

    o += mark(_dt.date(2027, 2, 8), _dt.date(2027, 3, 8), "RAMADAN", P["gilt"],
              above=False, hatch=True)
    o += mark(_dt.date(2027, 3, 8), _dt.date(2027, 3, 11), "RAMAZAN BAYRAMI", P["accent"])
    o += mark(_dt.date(2027, 5, 15), _dt.date(2027, 5, 19), "KURBAN BAYRAMI", P["accent"])

    o.append(_t(L, y0 + band + 62,
                "Both Bayrams begin with a half-day: offices, banks and government close at 13:00",
                11, P["read"], face=BODY))
    o.append(_t(L, y0 + band + 80,
                "on the arife, the day before the dates above. The Grand Bazaar shuts on day one.",
                11, P["read"], face=BODY))

    o.append(_line(L, H - 30, R, H - 30, P["line"], 1))
    o.append(_t(L, H - 12,
                "SOURCE: RELIGIOUS AFFAIRS CALENDAR · PUBLIC-HOLIDAY STATUTE · DATES FOR 2027", 8,
                P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


# ================================================================ FIG.8  THE PLAN
def fig_operations():
    """The week as constraint-ordered operations — and the same week planned the
    other way round, where the constraints arrive as surprises."""
    W, H = 800, 320
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    colw = 296

    ops = ["EVERY MOVE IS A BOOKING DECISION",
           "MOST MOVES PASS THROUGH ISTANBUL",
           "ISTANBUL HAS TWO AIRPORTS, FAR APART",
           "CASH NEED FOLLOWS HOW YOU TRAVEL"]
    sights = ["PICK THE SIGHTS", "FIT THE MOVES AROUND THEM",
              "DISCOVER THE CONNECTION", "DISCOVER THE OTHER AIRPORT"]

    def column(x0, head, items, colour, verdict, vcolour):
        b = [_t(x0, 44, head, 10, colour, ls=2.2, weight=700),
             _line(x0, 54, x0 + colw, 54, colour, 1.4)]
        yy = 84
        for i, s in enumerate(items):
            b.append(_box(x0, yy - 16, colw, 32, fill="none", stroke=P["line"], sw=1))
            b.append(_t(x0 + 12, yy + 4, f"{i+1}", 9, colour, ls=1.0, weight=700))
            b.append(_t(x0 + 30, yy + 4, s, 9, P["ink"], ls=0.5))
            if i < len(items) - 1:
                b.append(_line(x0 + colw / 2, yy + 16, x0 + colw / 2, yy + 32,
                               P["line"], 1.2))
            yy += 42
        b.append(_box(x0, yy - 14, colw, 34, fill="none", stroke=vcolour, sw=1.5))
        b.append(_t(x0 + colw / 2, yy + 8, verdict, 10, vcolour, anchor="middle",
                    ls=1.6, weight=700))
        return b

    o += column(L, "ORDER THE CONSTRAINTS FIRST", ops, P["ink"],
                "THE WEEK PLANS ITSELF", P["ink"])
    o += column(R - colw, "ORDER THE SIGHTS FIRST", sights, P["muted"],
                "THE CONSTRAINTS ARRIVE LATE", P["accent"])

    o.append(_t((L + R) / 2, 186, "vs", 13, P["muted"], anchor="middle", face=BODY,
                style="italic"))

    o.append(_line(L, H - 30, R, H - 30, P["line"], 1))
    o.append(_t(L, H - 12, "THE SAME WEEK, PLANNED IN TWO ORDERS", 8, P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


NEW = {
    "FIG-4": (fig_connection, 800, 396),
    "FIG-5": (fig_exposure, 800, 444),
    "FIG-6": (fig_export_gate, 800, 424),
    "FIG-7": (fig_calendar, 800, 286),
    "FIG-8": (fig_operations, 800, 320),
}




# ================================================================ FIG  D-06
def fig_channels():
    """Where a card refusal is actually decided, and which channel carries the fix."""
    W, H = 800, 392
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    o.append(_t(L, 44, "A CARD IS REFUSED IN A SHOP. WHERE WAS THAT DECIDED?", 10.5,
                P["ink"], ls=1.8, weight=700))
    seg = [("THE TERMINAL", 0), ("THE MERCHANT", 0), ("YOUR OWN BANK", 5), ("THE NETWORK", 1)]
    total = sum(n for _, n in seg) or 1
    x, y, bw = L, 70, R - L
    for name, n in seg:
        w = bw * n / total
        if w > 0:
            o.append(_box(x, y, w, 30, fill=P["accent"] if n >= 5 else P["stone"],
                          stroke=P["ink"], sw=1, op=0.9 if n >= 5 else 1))
            o.append(_t(x + w / 2, y + 20, str(n), 12, P["paper"] if n >= 5 else P["ink"],
                        anchor="middle", weight=700))
        x += w
    o.append(_t(L, y + 52, "TERMINAL 0  ·  MERCHANT 0  ·  YOUR OWN BANK 5  ·  NETWORK 1", 9,
                P["muted"], ls=1.6))
    o.append(_line(L, y + 68, R, y + 68, P["line"], 1))

    o.append(_t(L, y + 100, "AND WHICH CHANNEL CARRIES THE REMEDY", 10.5, P["ink"], ls=1.8,
                weight=700))
    rows = [("A verification code", "TEXT"), ("A call-back to release a hold", "VOICE"),
            ("Raising a daily limit", "VOICE OR APP"), ("Enabling international use", "APP, OVER DATA")]
    yy = y + 128
    for label, ch in rows:
        o.append(_t(L, yy, label, 10, P["read"], ls=0.4))
        col = P["ink"] if "DATA" in ch else P["accent"]
        o.append(_t(R, yy, ch, 9.5, col, anchor="end", ls=1.6, weight=700))
        o.append(_line(L, yy + 9, R, yy + 9, P["line"], 0.8))
        yy += 30
    o.append(_t(L, yy + 20, "Three of the four need the number you turned off at the airport.",
                11, P["ink"], face=BODY, style="italic"))
    o.append(_line(L, H - 30, R, H - 30, P["line"], 1))
    o.append(_t(L, H - 12, "SOURCE: THE ORDINARY REFUSAL CAUSES · ISSUER RULES ARE NOT PUBLISHED",
                8, P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


# ================================================================ FIG  D-07
def fig_doortodoor():
    """The comparison people run vs the comparison that decides it."""
    W, H = 800, 372
    o = [_box(0, 0, W, H, fill=P["paper"])]
    L, R = 92, 736
    o.append(_t(L, 44, "THE COMPARISON EVERYONE RUNS", 10, P["muted"], ls=2.2))
    o.append(_box(L, 56, 150, 26, fill=P["stone"], stroke=P["ink"], sw=1))
    o.append(_t(L + 75, 74, "THE SECTOR", 9, P["ink"], anchor="middle", ls=1.2))
    o.append(_box(L, 90, R - L, 26, fill=P["zone"], stroke=P["line"], sw=1))
    o.append(_t(L + (R - L) / 2, 108, "THE OVERNIGHT COACH", 9, P["ink"], anchor="middle", ls=1.2))

    o.append(_line(L, 138, R, 138, P["ink"], 1.2))
    o.append(_t(L, 168, "THE COMPARISON THAT DECIDES IT", 10, P["accent"], ls=2.2, weight=700))

    parts = [("TO THE AIRPORT", 1.5), ("BAG-DROP CUT-OFF", 1.0), ("SECURITY", 0.8),
             ("WALK TO GATE", 0.7), ("SECTOR", 1.6), ("RECLAIM", 0.8), ("INTO THE CITY", 1.4)]
    tot = sum(w for _, w in parts)
    x, y = L, 186
    for i, (name, w) in enumerate(parts):
        ww = (R - L) * w / tot
        o.append(_box(x, y, ww, 30, fill=P["stone"] if name != "SECTOR" else P["accent"],
                      stroke=P["ink"], sw=0.9, op=1 if name != "SECTOR" else 0.9))
        o.append(_t(x + ww / 2, y + 46, name, 7.5, P["muted"], anchor="middle", ls=0.6))
        x += ww
    o.append(_t(L, y - 8, "FLIGHT, DOOR TO DOOR", 8.5, P["muted"], ls=1.6))

    y2 = 268
    parts2 = [("TERMINAL", 1.2), ("THE JOURNEY, OVERNIGHT", 6.4), ("TERMINAL", 1.2)]
    tot2 = sum(w for _, w in parts2)
    x = L
    for name, w in parts2:
        ww = (R - L) * w / tot2
        o.append(_box(x, y2, ww, 30, fill=P["zone"], stroke=P["ink"], sw=0.9))
        o.append(_t(x + ww / 2, y2 + 20, name, 8, P["ink"], anchor="middle", ls=0.8))
        x += ww
    o.append(_t(L, y2 - 8, "COACH, DOOR TO DOOR — AND NO CONNECTION INSIDE THE FUNNEL", 8.5,
                P["accent"], ls=1.6))
    o.append(_line(L, H - 30, R, H - 30, P["line"], 1))
    o.append(_t(L, H - 12,
                "PROPORTIONS ARE STRUCTURAL, NOT A TIMETABLE — NO OFFICIAL SOURCE PUBLISHES ONE",
                8, P["muted"], ls=1.6))
    return _svg(W, H, "".join(o))


NEW["FIG-9"] = (fig_channels, 800, 392)
NEW["FIG-10"] = (fig_doortodoor, 800, 372)

if __name__ == "__main__":
    import pathlib, re
    for k, (fn, w, h) in NEW.items():
        s = fn()
        pathlib.Path(f"figures/{k}.svg").write_text(s, encoding="utf-8")
        print(f"{k}: {w}x{h}  {len(s)} bytes  texts={s.count('<text')}")
