# -*- coding: utf-8 -*-
"""build3.py — the assembler. Execs the content/design/maps/covers modules, embeds fonts,
emits dossier3.html: fixed-page front matter, then ONE flowed .flow div for the body
(decisions + chapters interleaved), Field Sheet as its own fixed section.
Furniture on flowed pages is applied by the RENDERER via header/footer template
(@page margin boxes fail silently in this Chromium) — see render3.py.
CSS lives in design.py (bug log #1). Marks and figures inline INSIDE prose (bug log #20,#21).
"""
import base64, os, re
import design, maps, covers
import content as K
import content2 as C2

BUILD = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BUILD, "fonts")

FONT_FILES = {
    "IM Fell English::normal::normal": "IMFellEnglish-Regular.ttf",
    "IM Fell English::italic::normal": "IMFellEnglish-Italic.ttf",
    "Sorts Mill Goudy::normal::normal": "SortsMillGoudy-Regular.ttf",
    "Sorts Mill Goudy::italic::normal": "SortsMillGoudy-Italic.ttf",
    "IBM Plex Mono::normal::normal": "IBMPlexMono-Regular.ttf",
    "IBM Plex Mono::normal::500": "IBMPlexMono-Medium.ttf",
}

def _font_face_block():
    out = []
    for key, fn in FONT_FILES.items():
        fam, style, weight = key.split("::")
        p = os.path.join(FONTS, fn)
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/ttf;base64,{b64}) format('truetype');font-display:block;}}"
        )
    return "\n".join(out)

# ---------- photo plates (user-supplied, embedded as base64) ----------
IMG = os.path.join(BUILD, "img")
_PHOTO_CACHE = {}
_PLATE_N = [0]
def _photo_b64(slot):
    if slot in _PHOTO_CACHE:
        return _PHOTO_CACHE[slot]
    p = os.path.join(IMG, f"{slot}.jpg")
    if not os.path.exists(p):
        return None
    with open(p, "rb") as f:
        b = base64.b64encode(f.read()).decode()
    _PHOTO_CACHE[slot] = b
    return b

def plate(slot, caption, tall=False):
    """A full-width photo plate with a numbered mono caption (PL. N).
    The PL. marker also registers as a visual break for the rhythm audit."""
    b = _photo_b64(slot)
    if not b:
        return ""
    _PLATE_N[0] += 1
    n = _PLATE_N[0]
    h = "3.3in" if tall else "2.55in"
    return (f'<figure class="photo"><img style="height:{h}" '
            f'src="data:image/jpeg;base64,{b}"/>'
            f'<figcaption><span class="fign">PL. {n}</span> \u00b7 {caption}</figcaption></figure>')

# ---------- figure rendering ----------
def fig_block(name, caption, fign):
    if not name:
        return ""
    svg = getattr(maps, name)()
    return (f'<figure class="map">{svg}'
            f'<figcaption><span class="fign">FIG. {fign}</span> \u00b7 {caption}</figcaption></figure>')

# ---------- decision rendering ----------
def render_decision(d, fign_map):
    parts = [f'<section class="dec">']
    parts.append(f'<div class="dnum">Decision {d["n"]} \u00b7 {d["cat"]}</div>')
    parts.append(f'<h1>{d["q"]}</h1>')
    parts.append(f'<p class="standfirst">{d["stand"]}</p>')
    # lede with dropcap
    parts.append(f'<p class="lede dropcap">{d["lede"]}</p>')
    body = list(d["body"])
    fig = d.get("fig")
    # place the figure INSIDE the prose, after the first body paragraph (bug log #20/#21)
    parts.append(f'<p>{body[0]}</p>')
    if fig:
        fign = fign_map[fig]
        parts.append(fig_block(fig, _figcap_for(fig), fign))
    for p in body[1:]:
        parts.append(f'<p>{p}</p>')
    # ledger table
    parts.append(f'<table class="ledger"><caption>{d["table_title"]}</caption>')
    cols = d["cols"].split(" \u00b7 ")
    parts.append('<tr>' + ''.join(f'<th{" class=num" if i==len(cols)-1 else ""}>{c}</th>' for i,c in enumerate(cols)) + '</tr>')
    for row in d["rows"]:
        opt, val = row[0], row[1]
        parts.append(f'<tr><td class="opt">{opt}</td><td class="num">{val}</td></tr>')
    parts.append('</table>')
    # verdict
    parts.append(f'<div class="verdict"><span class="lab">The call</span>{d["verdict"]}</div>')
    # for/against
    parts.append('<div class="forlist">')
    parts.append('<div class="y"><h4>Follow this if</h4><ul>' + ''.join(f'<li>{x}</li>' for x in d["for"]) + '</ul></div>')
    parts.append('<div class="n"><h4>Overrule it if</h4><ul>' + ''.join(f'<li>{x}</li>' for x in d["against"]) + '</ul></div>')
    parts.append('</div>')
    # note + xref
    if d.get("note"):
        parts.append(f'<div class="note">{d["note"]}</div>')
    if d.get("xref"):
        parts.append(f'<div class="xref">\u2192 {d["xref"]}</div>')
    parts.append('</section>')
    return "\n".join(parts)

# figure captions live with GROUND/STAY/PLAN chapters, but decisions reuse some; central lookup
_FIGCAPS = {
 "core_map":"The walkable core with the classic sights inside it, and Termini\u2019s 35-minute walk to the Pantheon drawn to scale. The \u201cbest-transport\u201d base sits outside the district it\u2019s meant to serve.",
 "transit_reality":"The two metro lines cross at Termini and run to the edges; the historic heart is the gap between them. Rome\u2019s transit is best understood as the hole in the middle.",
 "airport_strip":"Fiumicino to a central hotel, priced door-to-door. For a central base the train\u2019s €14 becomes €25\u201330 with the onward hop \u2014 competitive with the €55 fixed taxi. Only a Termini base makes the train win outright.",
 "ancient_flow":"The ancient half-day, two valid orders \u2014 and one 24-hour ticket that forbids pairing the cluster with the Vatican the same day.",
 "booking_calendar":"The one booking calendar four free articles never assemble: sights ordered by how far ahead they vanish. The top three punish a late booking with \u201csold out.\u201d",
 "eating_rule":"The ninety-second rule. Trap density is highest facing the monument, where frontage is dearest, and falls off within a short walk \u2014 the walk-time thesis, seen from the dinner table.",
 "daytrip_asymmetry":"The ancient-port choice by the day it costs: Ostia at roughly an hour round-trip on a metro ticket, Pompeii at twelve hours door-to-door. The famous name is the expensive default.",
}
def _figcap_for(name): return _FIGCAPS.get(name, "")

# ---------- chapter rendering ----------
def render_chapter(ch, kind="essay", fign_map=None, plate_html="", plate_after=1):
    parts = ['<section class="dec chap">']
    if ch.get("sub"):
        parts.append(f'<div class="dnum">{ch.get("kicker","Chapter")}</div>')
    parts.append(f'<h1>{ch["title"]}</h1>')
    if ch.get("sub"):
        parts.append(f'<p class="standfirst">{ch["sub"]}</p>')
    if ch.get("intro"):
        parts.append(f'<p class="lede">{ch["intro"]}</p>')
    body = ch.get("body", [])
    fig = ch.get("fig")
    if body:
        parts.append(f'<p class="{"dropcap" if not ch.get("intro") else ""}">{body[0]}</p>')
        for idx, p in enumerate(body[1:], start=1):
            parts.append(f'<p>{p}</p>')
            if plate_html and idx == plate_after:
                parts.append(plate_html)
        # if the chapter is short and plate wasn't placed, place it now
        if plate_html and plate_after >= len(body):
            parts.append(plate_html)
    if fig and fign_map:
        parts.append(fig_block(fig, ch.get("figcap",""), fign_map[fig]))
    parts.append("__CHAPTER_EXTRA__")
    parts.append('</section>')
    html = "\n".join(parts)
    return html

def render_before_fly(ch):
    rows = "".join(
        f'<tr><td class="num" style="color:var(--accent);white-space:nowrap;padding-right:14px;font-family:var(--mono);font-size:9px;letter-spacing:.06em;vertical-align:top">{w}</td>'
        f'<td style="padding-bottom:8px;line-height:1.5">{t}</td></tr>'
        for w,t in ch["items"])
    return f'<table class="ledger" style="margin-top:14px"><caption>The pre-departure list \u00b7 by deadline</caption>{rows}</table>'

def render_stay(ch, fign_map):
    out = []
    for nm, walk, txt in ch["hoods"]:
        out.append(f'<h3>{nm} <span style="font-family:var(--mono);font-size:10px;color:var(--deep)">\u00b7 {walk}</span></h3><p>{txt}</p>')
    # sleep tree figure
    tree = maps.sleep_tree()
    out.append(f'<figure class="map">{tree}<figcaption><span class="fign">FIG. {fign_map["sleep_tree"]}</span> \u00b7 {ch["tree_cap"]}</figcaption></figure>')
    return "\n".join(out)

def render_wallet(ch):
    rows = "".join(f'<div class="row"><span class="q">{q}</span><span class="a">{a}</span></div>' for q,a in ch["rows"])
    return f'<div class="wallet"><h3>Rome, on one card</h3>{rows}</div>'

def render_failure(ch, fign_map):
    out = []
    for gname, items in ch["groups"]:
        out.append(f'<h2>{gname}</h2>')
        lis = "".join(f'<li style="margin-bottom:7px"><strong style="font-family:var(--display)">{m}.</strong> {why}</li>' for m,why in items)
        out.append(f'<ul style="margin:0 0 6px 0;padding-left:16px;font-size:12.4px;line-height:1.5">{lis}</ul>')
    grid = maps.failure_grid()
    out.append(f'<figure class="map">{grid}<figcaption><span class="fign">FIG. {fign_map["failure_grid"]}</span> \u00b7 {ch["figcap"]}</figcaption></figure>')
    return "\n".join(out)

def render_refusals(ch):
    out = ['<div class="refuse">']
    for no, then in ch["items"]:
        out.append(f'<div class="item"><span class="no">{no}.</span> <span class="then">{then}</span></div>')
    out.append('</div>')
    return "\n".join(out)

def render_daytrips_menu(ch):
    out = []
    for nm, cost, txt in ch["items"]:
        out.append(f'<h3>{nm} <span style="font-family:var(--mono);font-size:9.5px;color:var(--deep);letter-spacing:.02em">\u00b7 {cost}</span></h3><p>{txt}</p>')
    out.append(f'<p>{ch["close"]}</p>')
    return "\n".join(out)

def render_field_sheet(ch):
    out = [f'<section class="page fs">']
    out.append(f'<h1 class="big">{ch["title"]}</h1>')
    out.append(f'<p class="standfirst">{ch["sub"]}</p>')
    out.append(f'<div class="note" style="margin-bottom:14px">{ch["method"]}</div>')
    out.append('<div class="fs-grid">')
    for sname, rows in ch["sections"]:
        out.append(f'<div class="fs-sec"><h2>{sname}</h2><table>')
        for k,v in rows:
            out.append(f'<tr><td class="k">{k}</td><td class="v">{v}</td></tr>')
        out.append('</table></div>')
    out.append('</div>')
    out.append('</section>')
    return "\n".join(out)

# ---------- TOC ----------
def render_toc(entries):
    out = ['<section class="page"><div class="runhead"><span>Contents</span><span>Rome, Solved.</span></div>']
    out.append('<div class="eyebrow">Contents</div><h1>What\u2019s inside</h1>')
    out.append('<div class="toc">')
    cur = None
    for part, title, pg in entries:
        if part != cur:
            out.append(f'<div class="part">{part}</div>'); cur = part
        out.append(f'<div class="row"><span class="t">{title}</span><span class="lead"></span><span class="pg">{pg}</span></div>')
    out.append('</div>')
    out.append('<div class="folio"><span>Rome, Solved.</span><span class="dot">\u25c6</span><span>ii</span></div>')
    out.append('</section>')
    return "\n".join(out)

def build():
    ff = _font_face_block()
    the_css = design.css(ff) + covers.cover_css()

    # assign figure numbers in reading order
    fig_order = ["cover_ring","core_map","transit_reality","airport_strip","ancient_flow",
                 "hood_locators","sleep_tree","booking_calendar","eating_rule","failure_grid","daytrip_asymmetry"]
    fign_map = {name: str(i+1) for i, name in enumerate(fig_order)}

    html = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
            f'<style>{the_css}</style></head><body>']

    # ---- COVER (own page) ----
    html.append(covers.cover_html())

    # ---- TOC ----
    toc_entries = [
        ("The ground", "How to read this book", "i"),
        ("The ground", "The one fact: a city you can walk across", "1"),
        ("The ground", "Why the obvious tool doesn\u2019t help", "3"),
        ("The decisions", "01 \u00b7 Where to sleep", "5"),
        ("The decisions", "02 \u00b7 Do you need transit tickets?", "7"),
        ("The decisions", "03 \u00b7 Train or taxi from the airport?", "9"),
        ("The decisions", "04 \u00b7 The ancient half-day", "11"),
        ("The decisions", "05 \u00b7 What \u201cskip the line\u201d skips", "13"),
        ("The decisions", "06 \u00b7 What to book, how far ahead", "15"),
        ("The decisions", "07 \u00b7 Cards, cash, and the reader prompt", "17"),
        ("The decisions", "08 \u00b7 The ninety-second eating rule", "19"),
        ("The decisions", "09 \u00b7 The fourth day: Ostia, not Pompeii", "21"),
        ("The city", "Before you fly", "23"),
        ("The city", "Day zero: the arrival", "24"),
        ("The city", "The rhythm of the week", "25"),
        ("The city", "Where to stay, assessed", "26"),
        ("The city", "Walking the quarters", "28"),
        ("The city", "The set pieces", "29"),
        ("The city", "The plan, as operations", "30"),
        ("The city", "Day trips, ranked by cost", "31"),
        ("The city", "Eating: the rule that outlives the list", "32"),
        ("Back matter", "Failure modes", "33"),
        ("Back matter", "The wallet card", "35"),
        ("Back matter", "What this book won\u2019t tell you", "36"),
        ("Back matter", "After the last tab", "37"),
        ("The annex", "The Field Sheet", "38"),
    ]
    html.append(render_toc(toc_entries))

    # ---- FLOWED BODY: opening, how-to, ground, transit, then decisions, then city chapters ----
    flow = ['<section class="flow">']

    # front essays that flow
    op = C2.OPENING
    a01 = plate("A01", "The compact core at golden hour \u2014 the Colosseum and the churches of the historic centre within a single frame. This is the kilometre and a half the whole book turns on: not a metropolis to be commuted across, but a district you walk.", tall=True)
    op_body = "".join(
        (f'<p class="dropcap">{p}</p>' + (a01 if i == 0 else ""))
        if i == 0 else f'<p>{p}</p>'
        for i, p in enumerate(op["body"]))
    flow.append(f'<section class="dec chap"><div class="eyebrow">Rome, Solved.</div>'
                f'<h1 class="big">{op["title"]}</h1><p class="standfirst">{op["sub"]}</p>'
                + op_body + '</section>')

    ch = C2.HOWTO
    flow.append(render_chapter(ch, fign_map=fign_map).replace("__CHAPTER_EXTRA__",""))

    # GROUND with cover_ring reused as figure + a photo plate
    g = C2.GROUND
    a02 = plate("A02", "A cobbled lane of the centro storico. In Rome the walk between sights is not overhead between destinations \u2014 it is the sightseeing, which is why where you sleep (Decision 01) decides how much of it you get.")
    flow.append(render_chapter(g, fign_map=fign_map, plate_html=a02, plate_after=1).replace("__CHAPTER_EXTRA__", ""))
    # transit reality
    tr = C2.TRANSIT_REALITY
    flow.append(render_chapter(tr, fign_map=fign_map).replace("__CHAPTER_EXTRA__",""))

    # DECISIONS 01-09
    for d in K.DECISIONS:
        flow.append(render_decision(d, fign_map))

    # CITY chapters
    bf = C2.BEFORE_FLY
    flow.append(render_chapter(bf, fign_map=fign_map).replace("__CHAPTER_EXTRA__", render_before_fly(bf)))
    flow.append(render_chapter(C2.DAY_ZERO, fign_map=fign_map).replace("__CHAPTER_EXTRA__",""))
    flow.append(render_chapter(C2.TIMING, fign_map=fign_map).replace("__CHAPTER_EXTRA__",""))
    flow.append(render_chapter(C2.STAY, fign_map=fign_map,
        plate_html=plate("A04", "Trastevere after dark \u2014 lantern light, ivy, and a table outdoors. This is the base you choose when evenings outrank mornings (Decision 01), and the trade it asks for is the bridge between you and the sights.", tall=True),
        plate_after=99).replace("__CHAPTER_EXTRA__", render_stay(C2.STAY, fign_map)))
    flow.append(render_chapter(C2.QUARTERS, fign_map=fign_map).replace("__CHAPTER_EXTRA__",""))
    flow.append(render_chapter(C2.SET_PIECES, fign_map=fign_map,
        plate_html=plate("A05", "The oculus of the Pantheon \u2014 the same shaft of light the ancient Romans stood under, falling through the only opening in the dome. The Pantheon survives not as a ruin but as a building; this is the half-hour that lingers for years.", tall=True),
        plate_after=1).replace("__CHAPTER_EXTRA__",""))
    flow.append(render_chapter(C2.PLAN, fign_map=fign_map,
        plate_html=plate("A03", "The Roman Forum from above \u2014 one connected archaeological half-day on unshaded stone. This is why it never shares a day with the Vatican (Decision 04), and why the Forum is walked first, at opening, before the heat and the buses."),
        plate_after=1).replace("__CHAPTER_EXTRA__",""))
    flow.append(render_chapter(C2.DAYTRIPS_MENU, fign_map=fign_map).replace("__CHAPTER_EXTRA__", render_daytrips_menu(C2.DAYTRIPS_MENU)))
    flow.append(render_chapter(C2.EATING_ESSAY, fign_map=fign_map,
        plate_html=plate("A06", "A plate of one of the four Roman classics \u2014 cucina povera done brilliantly, pecorino and pepper and little else. The dish you find by walking ninety seconds off the sight (Decision 08), where the kitchen survives on locals who would notice a wrong carbonara."),
        plate_after=1).replace("__CHAPTER_EXTRA__",""))

    # BACK MATTER
    flow.append(render_chapter(C2.FAILURE_MODES, fign_map=fign_map).replace("__CHAPTER_EXTRA__", render_failure(C2.FAILURE_MODES, fign_map)))
    flow.append(render_chapter(C2.WALLET, fign_map=fign_map).replace("__CHAPTER_EXTRA__", render_wallet(C2.WALLET)))
    flow.append(render_chapter(C2.REFUSALS, fign_map=fign_map).replace("__CHAPTER_EXTRA__", render_refusals(C2.REFUSALS)))
    cl = C2.CLOSING
    a07 = plate("A07", "St Peter\u2019s and the Tiber at dusk \u2014 the city that lived in forty browser tabs, simply around you, and better than the tabs promised. The payoff of deciding everything in advance is the walk home with nowhere you have to be.", tall=True)
    flow.append(f'<section class="dec chap"><h1>{cl["title"]}</h1>'
                + f'<p class="dropcap">{cl["body"][0]}</p>' + a07
                + "".join(f'<p>{p}</p>' for p in cl["body"][1:])
                + '</section>')

    flow.append('</section>')  # /flow
    html.append("\n".join(flow))

    # ---- FIELD SHEET (own fixed page) ----
    html.append(render_field_sheet(C2.FIELD_SHEET))

    html.append('</body></html>')
    out = "\n".join(html)
    with open(os.path.join(BUILD, "dossier3.html"), "w", encoding="utf-8") as f:
        f.write(out)
    return len(out), fign_map

if __name__ == "__main__":
    n, fm = build()
    print(f"dossier3.html written: {n:,} bytes")
    print(f"figures: {fm}")
