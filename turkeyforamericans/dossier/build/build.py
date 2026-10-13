"""build.py — manuscript markdown -> dossier3.html (engine-pure; no polyfill here).

Running order is NOT invented: it is the page map already committed in
dossier-images.md (A02 The Ground ~p6, A03 Day Zero ~p11, A04 Set Pieces ~p17,
A05 Eating ~p20, decisions pp21-30 with A06 at Buying ~p27, A07 Failure Modes
~p35, A08 Closing ~p40).

A01 was briefed as the cover. The cover is now a computed device (cover.md), so
A01 opens THE GROUND — which is the chapter whose thesis it already argued.
"""
import re, pathlib, html as _html
from design import css, TITLE
from cover import cover_svg

D = pathlib.Path(__file__).parent
OUT = D / "dossier3.html"

# ---------------------------------------------------------------- plates
PLATES = {
    "A01": ("THE GROUND",
            "Anatolia at the scale the itineraries do not show. The distance in this "
            "frame is the reason the sequence in this book matters more than the list "
            "of places in it."),
    "A02": ("THE VACUUM",
            "This is the board you leave from, and everything on it is published: "
            "carrier, time, gate, status, to the minute. The number this chapter is "
            "about — how much time a connection at Istanbul needs — is posted on no "
            "board at either Istanbul airport, and never has been. The board is not "
            "withholding it. No authority has ever set it."),
    "A03": ("ONE AIRPORT, TWO HOURS",
            "A single terminal is a building, not a distance. Between an "
            "international arrival and a domestic departure sit passport control, "
            "the belt, and a walk of this order."),
    "A04": ("THE BALLOON IS WEATHER",
            "Flown from a distance the fleet reads as a schedule. It is not one. "
            "The wind decides the night before, and no operator can sell you "
            "certainty they do not have."),
    "A05": ("READ THE COUNTER",
            "The trays are the menu and the type of place is legible before you sit "
            "down. This is the whole method: the room tells you what it is, which is "
            "why this book names no restaurants."),
    "A06": ("THE SAME TABLE",
            "What may leave the country and what may not are sold side by side, by "
            "the same seller, at the same table. Nothing on it is labelled with the "
            "distinction that matters at the airport."),
    "A07": ("BEFORE ANYTHING HAS GONE WRONG",
            "The ordinary road on an ordinary afternoon. Everything in this chapter "
            "begins here, which is the point: none of it announces itself."),
    "A08": ("WHAT THE DECIDING WAS FOR",
            "Late light, and nothing left to resolve. The chapters before this one "
            "exist so that this hour is not spent on a phone."),
}

# figure key -> (file, caption) ; placed inside the decision that argues it
FIGS = {
    "FIG-1": ("figures/FIG-1-istanbul-funnel.svg",
              "Every internal move funnels through Istanbul. Cappadocia and Ephesus "
              "are 658 km apart — further from each other than either is from the hub "
              "that connects them."),
    "FIG-2": ("figures/FIG-2-four-gates.svg",
              "Four separate thresholds, four different authorities, four different "
              "ages. Only one of them is the one that binds you, and it is not the "
              "one the rental desk quotes."),
    "FIG-3": ("figures/FIG-3-fee-stack.svg",
              "The stack a single withdrawal passes through. Each layer is disclosed "
              "somewhere; no screen shows the total, which is the only number that "
              "matters."),
    "FIG-4": ("figures/FIG-4.svg",
              "On one ticket the carrier has chosen the gap and underwrites its own "
              "choice. On separate tickets the gap is yours \u2014 and no authority "
              "publishes how long it needs to be."),
    "FIG-5": ("figures/FIG-5.svg",
              "Four of the six rungs have no published price anywhere. The standard "
              "exclusions cluster on precisely the activities a first trip is most "
              "likely to buy."),
    "FIG-6": ("figures/FIG-6.svg",
              "The tree has no numeric branch, because the law states no age. That "
              "absence is why the hundred-year rule in circulation cannot be the "
              "test, whatever the seller says it is."),
    "FIG-7": ("figures/FIG-7.svg",
              "The 2027 dates, drawn to scale. Both Bayrams open with a half-day "
              "closure from 13:00 the day before \u2014 the part that catches a "
              "traveller mid-errand."),
    "FIG-9": ("figures/FIG-9.svg",
              "A refusal is almost never decided where it is felt. Five of the six ordinary "
              "causes sit at your own bank, and three of the four remedies travel on the "
              "channel most travellers switch off at the airport."),
    "FIG-10": ("figures/FIG-10.svg",
              "The sector is not the journey. Set the flight's real components beside the "
              "coach and the gap narrows; the row that does not appear in either bar is "
              "which one passes through the funnel."),
    "FIG-8": ("figures/FIG-8.svg",
              "The same week, ordered two ways. One of them produces a plan; the "
              "other produces the same constraints, arriving late."),
}

# running order: (part, section heading, eyebrow, plates[], figure, drop)
ORDER = [
    ("part1", "OPENING",                     None,                None,    None),
    ("part1", "HOW TO READ THIS",            None,                None,    None),
    ("part1", "THE GROUND",                  "PART ONE · GROUND", ["A01", "A02"], "FIG-1"),
    ("part1", "BEFORE YOU FLY",              "PART ONE · GROUND", None,    None),
    ("part1", "DAY ZERO",                    "PART ONE · GROUND", ["A03"], None),
    ("part1", "TIMING",                      "PART ONE · GROUND", None,    "FIG-7"),
    ("part1", "MONEY",                       "PART ONE · GROUND", None,    None),
    ("part4", "THE SET PIECES",              "PART TWO · ON THE GROUND", ["A04"], None),
    ("part4", "EATING",                      "PART TWO · ON THE GROUND", ["A05"], None),
    ("DECISIONS", None, None, None, None),
    ("part2", "THE HORIZONS",                "PART FOUR · OPERATIONS", None, None),
    ("part2", "THE PLAN",                    "PART FOUR · OPERATIONS", None, "FIG-8"),
    ("part2", "FAILURE MODES",               "PART FOUR · OPERATIONS", ["A07"], None),
    ("part2", "KIT",                         "PART FOUR · OPERATIONS", None, None),
    ("part2", "WHAT THIS BOOK WON'T TELL YOU", "PART FOUR · OPERATIONS", None, None),
    ("part2", "CLOSING",                     "PART FOUR · OPERATIONS", ["A08"], None),
    ("part2", "FIELD SHEET — the dated annex", "ANNEX", None, None),
]

DEC_FIG = {"I": "FIG-4", "II": "FIG-5", "III": "FIG-2",
           "IV": "FIG-6", "V": "FIG-3",
           "VI": "FIG-9", "VII": "FIG-10"}   # every decision argues with a figure
DEC_PLATE = {"IV": "A06"}

PLATE_AT = (4, 11)          # paragraph indices a chapter's plates hang off
_EMITTED = {}


def fignum(key):
    if key not in _EMITTED:
        _EMITTED[key] = len(_EMITTED) + 1
    return _EMITTED[key]


# ---------------------------------------------------------------- inline
def inline(s: str) -> str:
    s = _html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", lambda m: f'<span class="mark">{m.group(1)}</span>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = s.replace("->", "&rarr;").replace("→", "&rarr;")
    return s


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ---------------------------------------------------------------- parsing
def read_part(name):
    return (D / f"C-manuscript-{name}.md").read_text(encoding="utf-8")


def split_sections(text, level="## "):
    """-> [(heading, body_lines)]"""
    out, cur, buf = [], None, []
    for ln in text.split("\n"):
        if ln.startswith(level) and not ln.startswith(level + "#"):
            if cur is not None:
                out.append((cur, buf))
            cur, buf = ln[len(level):].strip(), []
        elif cur is not None:
            buf.append(ln)
    if cur is not None:
        out.append((cur, buf))
    return out


def blocks(lines):
    """group body lines into typed blocks"""
    out, buf, mode = [], [], "p"

    def flush():
        nonlocal buf, mode
        if buf:
            out.append((mode, buf))
        buf, mode = [], "p"

    for ln in lines:
        s = ln.rstrip()
        if s.strip() == "---":
            flush()
            continue
        if not s.strip():
            flush()
            continue
        if s.startswith("### "):
            flush()
            out.append(("h2", [s[4:].strip()]))
            continue
        if re.match(r"\d+\.\s", s.strip()) or s.strip().startswith("`\u25cf") \
                or s.strip().startswith("`\u25c7") or s.strip().startswith("`\u25c6"):
            flush()
            mode = "li"
            buf.append(s)
            continue
        if mode == "li" and not s.lstrip().startswith("|"):
            buf.append(s)
            continue
        if s.lstrip().startswith("|"):
            if mode != "table":
                flush()
                mode = "table"
            buf.append(s.strip())
            continue
        if mode == "table":
            flush()
        buf.append(s)
    flush()
    return out


def render_table(rows):
    rows = [r for r in rows if not re.fullmatch(r"\|[\s|:-]+\|", r)]
    cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
    head, body = cells[0], cells[1:]
    h = "".join(f"<th>{inline(c)}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


CLOSING_PLATES = set()      # a forced closing plate on A07 left a 3% page — reverted


def plate_html(key, closing=False):
    label, cap = PLATES[key]
    letter = chr(64 + int(key[1:]))          # letter by SLOT (bug #17)
    cls = "photo closing" if closing else "photo"
    return (f'<figure class="{cls}"><img src="img/{key}.jpg" alt="">'
            f'<figcaption><b>PL. {letter} — {label}</b> &nbsp;{cap}</figcaption></figure>')


def fig_html(key):
    src, cap = FIGS[key]
    n = fignum(key)
    svg = (D / src).read_text(encoding="utf-8")
    svg = re.sub(r'<\?xml[^>]*\?>', '', svg).strip()
    svg = re.sub(r'\swidth="\d+"\s+height="\d+"', '', svg, count=1)
    return (f'<figure class="map">{svg}'
            f'<figcaption><b>FIG. {n}</b> &nbsp;{cap}</figcaption></figure>')


def render_body(bl, plates=None, fig=None, drop=True, fig_after=99):
    """emit blocks; visuals go INSIDE the flow after their paragraph (#22)."""
    plates = list(plates or [])
    out, pcount, first = [], 0, drop
    pending_h2 = None
    for mode, buf in bl:
        if mode == "h2":
            pending_h2 = buf[0]
            continue
        if mode == "table":
            out.append(render_table(buf))
            continue
        if mode == "li":
            txt = " ".join(x.strip() for x in buf)
            m = re.match(r"(\d+)\.\s+(.*)", txt)
            if m:
                out.append(f'<p class="kit"><span class="kitnum">{m.group(1)}</span>'
                           f'{inline(m.group(2))}</p>')
            else:
                out.append(f'<p class="legend">{inline(txt)}</p>')
            continue
        txt = " ".join(buf).strip()
        if not txt:
            continue
        cls = ""
        if txt.startswith("**Verified at press time"):
            out.append(f'<p class="dated">{inline(txt.strip("*"))}</p>')
            continue
        if txt.startswith("**Then it's"):
            cls = ' class="fork"'
        elif first:
            cls = ' class="dropcap"'
        para = f"<p{cls}>{inline(txt)}</p>"
        if pending_h2:
            # H2 + its first paragraph as ONE break-inside:avoid box:
            # paged.js will not honour break-after:avoid between siblings.
            out.append(f'<div class="subwrap"><div class="sub"><h2>{inline(pending_h2)}</h2>'
                       f'{para}</div></div>')
            pending_h2 = None
        else:
            out.append(para)
        first = False
        pcount += 1
        if fig and pcount == fig_after:
            out.append(fig_html(fig))
            fig = None
        if plates and pcount in PLATE_AT and plates[0] not in CLOSING_PLATES:
            out.append(plate_html(plates.pop(0)))
    while plates:
        k = plates.pop(0)
        out.append(plate_html(k, closing=k in CLOSING_PLATES))
    if fig:
        out.append(fig_html(fig))
    return "\n".join(out)


def take_standfirst(bl):
    """the first italic-only block is the standfirst"""
    if bl and bl[0][0] == "p":
        t = " ".join(bl[0][1]).strip()
        if t.startswith("*") and t.endswith("*") and not t.startswith("**"):
            t = t.strip("*").strip()
            t = re.sub(r"^Standfirst:\s*", "", t)
            return t, bl[1:]
    return None, bl


def chapter(sec_id, eyebrow, title, sf, body_html, annex=False, first=False):
    cls = "dec chap fs" if annex else "dec chap"
    if first:
        cls += " first"
    eb = f'<p class="eyebrow">{inline(eyebrow)}</p>' if eyebrow else ""
    sfh = f'<p class="standfirst">{inline(sf)}</p>' if sf else ""
    return f"""<section class="{cls}" id="{sec_id}">
<div class="opener">{eb}<h1>{inline(title)}</h1><span class="rh-src">{_html.escape(title)}</span>{sfh}<hr class="oprule">
</div>
{body_html}
<p class="endmark">&#9670;</p>
</section>"""


# ---------------------------------------------------------------- decisions
def decisions_html():
    txt = read_part("part3")
    parts = split_sections(txt, "## ")          # "I · TRANSIT"
    out, toc = [], []
    for eyebrow, lines in parts:
        roman = eyebrow.split("·")[0].strip()
        body = "\n".join(lines)
        m = re.search(r"^# (.+)$", body, re.M)
        title = m.group(1).strip()
        rest = body[m.end():]
        bl = blocks(rest.split("\n"))
        sf, bl = take_standfirst(bl)
        sid = "d-" + slug(roman)
        toc.append((sid, f"{roman} · {title}"))
        bh = render_body(bl,
                         plates=[DEC_PLATE[roman]] if roman in DEC_PLATE else None,
                         fig=DEC_FIG.get(roman), drop=True, fig_after=99)
        out.append(chapter(sid, eyebrow, title, sf, bh))
    return "\n".join(out), toc


# ---------------------------------------------------------------- main
def main():
    cache = {p: {h: b for h, b in split_sections(read_part(p))}
             for p in ("part1", "part2", "part3", "part4")}
    body, toc, first = [], [], True
    for part, head, eyebrow, plates, fig in ORDER:
        if part == "DECISIONS":
            dh, dtoc = decisions_html()
            body.append(dh)
            toc.append(("SEP", "THE DECISIONS"))
            toc.extend(dtoc)
            first = False
            continue
        lines = cache[part].get(head)
        if lines is None:
            raise SystemExit(f"MISSING SECTION: {part} / {head}")
        bl = blocks(lines)
        sf, bl = take_standfirst(bl)
        title = head.split(" — ")[0]
        sid = slug(title)
        annex = head.startswith("FIELD SHEET")
        toc.append((sid, title))
        bh = render_body(bl, plates=plates, fig=fig, drop=not annex)
        body.append(chapter(sid, eyebrow, title, sf, bh, annex=annex, first=first))
        first = False

    rows = []
    for sid, label in toc:
        if sid == "SEP":
            rows.append(f'<li class="sep"><span class="t"><b>{label}</b></span></li>')
        else:
            rows.append(f'<li><span class="t">{inline(label)}</span><span class="d"></span>'
                        f'<span class="n"><a href="#{sid}"></a></span></li>')

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{TITLE}</title><style>{css()}</style></head><body>
<div class="coverpage">{cover_svg()}</div>
<section class="chap fm" id="contents">
<div class="opener"><p class="eyebrow">CONTENTS</p><h1>What is in this book</h1>
<span class="rh-src">Contents</span><hr class="oprule"></div>
<ul class="toc">{''.join(rows)}</ul>
<p class="endmark">&#9670;</p>
</section>
<div class="flow">
{chr(10).join(body)}
</div>
</body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    print("wrote", OUT, OUT.stat().st_size, "bytes | sections:", len(toc),
          "| figures:", len(_EMITTED))


if __name__ == "__main__":
    main()
