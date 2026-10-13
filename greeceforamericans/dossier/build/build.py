# -*- coding: utf-8 -*-
"""build.py — assembles dossier3.html. Portable (BUILD = this dir).

DOM contract the renderer (render-paged.py) and gates expect:
  · one <div class="flow"> holds every chapter
  · each chapter is <section class="dec chap" id=..> with data-ref
  · each section emits ONE invisible <span class="rh-src"> after its H1 (bug #35)
  · figures are <figure class="map"> emitted INSIDE the prose after their intro para
  · every chapter ends with <div class="endmark">
  · the cover is a separate .coverpage div (page:cover, full bleed)
  · figures numbered by APPEARANCE ORDER, each emitted once (guarded)
"""
import os
from design import css
import maps
from content import DECISIONS
from prose import CHAPTERS_BEFORE, CHAPTERS_AFTER
from fieldsheet import FIELD_SHEET

BUILD = os.path.dirname(os.path.abspath(__file__))

# ---- figure emit guard + appearance-order numbering ----
_FIGN = {}
def fignum(key):
    if key not in _FIGN:
        _FIGN[key] = len(_FIGN) + 1
    return _FIGN[key]

FIG_CAPTIONS = {
  "route":   "The Cyclades trunk, nodes plotted to real geographic scale. Solid edges are the short, frequent, conventional-ferry hops that anchor the middle of a trip; dashed edges are the long crossings you fly or commit a day to. Paros–Naxos is 20&nbsp;km; Piraeus–Santorini is 237.",
  "arrival": "Day Zero as a decision, not a scramble. The fork — near island by ferry through Piraeus, or far island by air — is one you settle from home; the constant on both branches is a buffered return, never a same-day connection against the flight home.",
  "flyferry":"Hours from Athens by ferry (bars) against the domestic flight (dots). On the long crossings the flight saves a day outright; the fast ferry earns its premium only on the middle-distance outbound hops, not the short ones and not the long ones.",
  "pace":    "Ten days, each block one island stay. Two or three islands leave room to arrive; five is the trap our own reporting names — five airports' worth of logistics and no island. The floor is three nights; below it you are commuting.",
  "season":  "Crowd (bars) and meltemi wind (line) across the season. July and August peak together — most crowded, most expensive, windiest, and hardest on the fast ferries. The shoulder months trade almost nothing for calmer everything.",
  "santstay":"Santorini's price gradient: the caldera-rim villages carry the sunset premium; inland and beach bases return the same island, food, and light for markedly less. On this island the base decision is the money decision.",
  "meltemi": "The same five islands in two orders. End on Santorini and your final, most fragile leg — a fast catamaran the meltemi cancels — sits against the one deadline you can't rebook. End near Athens and the deadline is already safe.",
  "crete":   "Crete to scale against a single Cyclades hop. At ~160 miles end to end — a two-hour drive between its two main cities alone — the island holds more than a hopping week can reach. The whole Paros–Naxos crossing would fit inside one leg of it.",
  "week":    "The first week as an operational shape, not an hour-by-hour script. Fixed points — Athens, one or two island stays, the buffer night — with flexible hops between. The buffer is the slack that keeps a cancelled ferry from becoming a missed plane.",
  "failcost":"The failure modes, sorted by consequence rather than topic — the thing a website of separate articles cannot assemble. Guard the top tier first: the mistakes that cost the trip or a whole day outrank the ones that cost only money or a little polish.",
  "athens":  "Two or three days in Athens as an on-ramp, not a transit. The load-bearing move is the combination ticket bought at a quieter site, which turns the Acropolis's longest queue into a walk-through — and a third day buys a day trip, not more city.",
  "sunset":  "The signature evening, four ways. Three of them deliver the caldera glow with room to enjoy it; the fourth — arriving at eight with no plan — delivers the crowd and the shuffle home. Every big Santorini sight rewards being early or late, never midday.",
}

def esc(s): return s

def fig_block(key, fig_after=None):
    """Emit a figure exactly once, numbered by appearance order."""
    n = fignum(key)
    svg = maps.FIGURES[key]() if key in maps.FIGURES else None
    if svg is None:
        return ""
    cap = FIG_CAPTIONS.get(key, "")
    return (f'<figure class="map" id="fig-{key}">{svg}'
            f'<figcaption><span class="fign">FIG.&nbsp;{n}</span>&nbsp;&nbsp;{cap}</figcaption></figure>')

def rh(text):
    return f'<span class="rh-src">{text}</span>'

# ---- PHOTOGRAPHS: real plates keyed to decisions. Opening bands anchor each
# decision visually; the computed figure still carries the analysis mid-argument.
# klass: "wide" (opening band, 3.3in) or "closing" (fed tail plate, 4.35in).
PHOTO_DIR = "photos/opt"
PHOTOS = {
  "d01": ("A01.jpg", "A Hellenic Seaways high-speed catamaran at a Cycladic quay. This is the vessel class the summer meltemi cancels first — and the one a rushed itinerary leans on for its tightest connection."),
  "d02": ("A02.jpg", "Evening traffic off the islands — a sailboat and a coaster sharing calm water at dusk. The reliable middle of a trip is built from short, frequent crossings like these, not dashes across the map."),
  "d03": ("A03.jpg", "A conventional Golden Star car ferry pulling away from Paros, open decks full. Slower than the catamaran by an hour or two — and the boat that still sails when the wind shuts the fast fleet down."),
  "d04": ("A04.jpg", "Naousa, on Paros — whitewash, blue shutters, and a working harbour rather than a stage set. Our own reporting reserves its warmest language for islands like this, not for the two famous names."),
  "d05": ("A05.jpg", "A single stretch of the Cretan coast, mountains running to the horizon. The scale is the argument: this is a region to settle into, not an island to append to a hopping week."),
  "d06": ("A06.jpg", "A caldera-rim terrace on Santorini. The view is real — and it is what the premium buys. The same island, food, and light are available a short walk inland for markedly less."),
  "d08": ("A08.jpg", "The Acropolis in late-afternoon light. Two or three days in Athens is the on-ramp, not a transit — and the big sights reward the early or late hour, never the midday heat and crowd."),
  "d09": ("A07.jpg", "Oia at dusk, the whole village lit. The signature evening — and, with no plan, the signature crowd. A quiet rim perch or a boat below buys the same glow with room to enjoy it."),
}
_PHOTO_EMITTED = set()

def photo_block(did, klass="wide"):
    """Emit a decision's photograph once, as an opening band or a fed closing plate."""
    if did not in PHOTOS or did in _PHOTO_EMITTED:
        return ""
    _PHOTO_EMITTED.add(did)
    fn, cap = PHOTOS[did]
    src = f"{PHOTO_DIR}/{fn}"
    return (f'<figure class="photo {klass}"><img src="{src}" alt="">'
            f'<figcaption>{cap}</figcaption></figure>')

def endmark():
    return '<div class="endmark"></div>'

# ---- render a body-block list (shared by decisions and prose chapters) ----
def render_blocks(blocks, marks_legend=False):
    out = []
    first_p_done = False
    for b in blocks:
        kind = b[0]
        if kind == "p":
            html = b[1]
            # tag the first paragraph of a chapter for the drop cap (handled via span in text)
            out.append(f'<p>{html}</p>')
        elif kind == "h2":
            out.append(f'<h2 class="s">{b[1]}</h2>')
        elif kind == "h3":
            out.append(f'<h3 class="s">{b[1]}</h3>')
        elif kind == "fig":
            out.append(fig_block(b[1]))
        elif kind == "aside":
            title, html = b[1]
            out.append(f'<div class="aside"><span class="at">{title}</span>{html}</div>')
        elif kind == "pull":
            out.append(f'<p class="pull">{b[1]}</p>')
        elif kind == "note":
            out.append(f'<div class="note">{b[1]}</div>')
        elif kind == "marks":
            out.append(MARKS_LEGEND)
        elif kind == "forlist":
            items = "".join(f'<li>{x}</li>' for x in b[1])
            out.append(f'<ul class="forlist">{items}</ul>')
        elif kind == "forlist_num":
            items = "".join(f'<li>{x}</li>' for x in b[1])
            out.append(f'<ul class="forlist num">{items}</ul>')
    return "".join(out)

MARKS_LEGEND = """
<ul class="marklist">
  <li><span class="mk est">● STRUCTURAL</span> geography and physics — true for years, won't change</li>
  <li><span class="mk stb">◆ STABLE</span> the ordering or the rule holds; any live figure lives on the Field Sheet</li>
  <li><span class="mk off">◇ OFFICIAL</span> a published rule or government advisory</li>
  <li><span class="mk sur">▲ SURVEYED 06/25</span> our own dated observation, from the articles behind this book</li>
</ul>
"""

# ---- ledger + verdict for a decision ----
def render_ledger(ledger):
    if not ledger:
        return ""
    title = ledger[0]; c1 = ledger[1]; c2 = ledger[2]; rows = ledger[3]
    body = []
    for r in rows:
        k = r[0]; v = r[1]
        body.append(f'<tr><td class="k">{k}</td><td>{v}</td></tr>')
    return (f'<table class="ledger"><tr><td class="led-h" colspan="1">{c1}</td>'
            f'<td class="led-h">{c2}</td></tr>{"".join(body)}</table>')

def render_verdict(v):
    if not v:
        return ""
    lead, body = v
    return (f'<div class="verdict"><span class="vq">The call</span>'
            f'<div class="vlead">{lead}</div><p>{body}</p></div>')

# ---- a prose chapter (opening, essays, etc.) ----
def chapter_section(ch, first=False):
    cls = "dec chap" if not first else "dec chap"
    fm = ' fm' if ch.get("fm") else ''
    parts = [f'<section class="{cls}{fm}" id="{ch["id"]}" data-ref="{ch["id"]}">']
    parts.append(f'<div class="eyebrow">{ch["eyebrow"]}</div>')
    parts.append(f'<h1 class="t">{ch["q"]}</h1>')
    parts.append(rh(ch["eyebrow"].split("·")[0].strip() if "·" in ch["eyebrow"] else ch["eyebrow"]))
    if ch.get("standfirst"):
        parts.append(f'<div class="standfirst">{ch["standfirst"]}</div>')
    parts.append(render_blocks(ch["body"]))
    parts.append(endmark())
    parts.append('</section>')
    return "".join(parts)

# ---- a decision (also a chapter) ----
def decision_section(d):
    parts = [f'<section class="dec chap" id="{d["id"]}" data-ref="{d["id"]}">']
    parts.append(f'<div class="eyebrow">{d["eyebrow"]}&nbsp;&nbsp;·&nbsp;&nbsp;DECISION {d["num"]}</div>')
    parts.append(f'<h1 class="t">{d["q"]}</h1>')
    parts.append(rh(f'DECISION {d["num"]}'))
    parts.append(f'<div class="standfirst">{d["standfirst"]}</div>')
    parts.append(photo_block(d["id"], "wide"))   # opening band — visual entry
    parts.append(render_blocks(d["body"]))
    parts.append(render_ledger(d.get("ledger")))
    parts.append(render_verdict(d.get("verdict")))
    parts.append(endmark())
    parts.append('</section>')
    return "".join(parts)

# ---- the contents page (real folios via target-counter) ----
def contents_section():
    rows = []
    rows.append('<tr class="part"><td colspan="3">The trip</td></tr>')
    order = [("open","Opening — the contract"),("howto","How to read this"),
             ("ground","The Ground — Greece is a network"),("before","Before you fly"),
             ("dayzero","Day Zero — the arrival"),("timing","When to go")]
    for i,(iid,label) in enumerate(order):
        rows.append(f'<tr><td class="n">{i:02d}</td><td><a href="#{iid}">{label}</a></td>'
                    f'<td class="pg"><a href="#{iid}"></a></td></tr>')
    rows.append('<tr class="part"><td colspan="3">The decisions</td></tr>')
    for d in DECISIONS:
        rows.append(f'<tr><td class="n">{d["num"]}</td><td><a href="#{d["id"]}">{d["q"]}</a></td>'
                    f'<td class="pg"><a href="#{d["id"]}"></a></td></tr>')
    rows.append('<tr class="part"><td colspan="3">The rest of the trip</td></tr>')
    order2 = [("eating","Eating — the durable rule"),("stay","Where to stay"),
              ("plan","The Plan — the week as operations"),("failures","Failure modes, by cost"),
              ("back","What this book won't tell you"),("closing","Envoi"),
              ("fs","The Field Sheet")]
    for i,(iid,label) in enumerate(order2):
        rows.append(f'<tr><td class="n">·</td><td><a href="#{iid}">{label}</a></td>'
                    f'<td class="pg"><a href="#{iid}"></a></td></tr>')
    body = "".join(rows)
    return (f'<section class="dec chap fm" id="contents" data-ref="contents">'
            f'<div class="eyebrow">CONTENTS</div>'
            f'<h1 class="t">What\'s inside, and where.</h1>'
            f'{rh("CONTENTS")}'
            f'<div class="standfirst">A decision manual, in reading order — the trip, the twelve calls at its heart, and the dated companion.</div>'
            f'<table class="toc">{body}</table>'
            f'{endmark()}</section>')

# ---- the Field Sheet (annex) ----
def fieldsheet_section():
    fs = FIELD_SHEET
    parts = [f'<section class="dec chap fs" id="{fs["id"]}" data-ref="{fs["id"]}">']
    parts.append(f'<div class="eyebrow">{fs["eyebrow"]}</div>')
    parts.append(f'<h1 class="t">{fs["q"]}</h1>')
    parts.append(rh("FIELD SHEET"))
    parts.append(f'<div class="standfirst">{fs["standfirst"]}</div>')
    for p in fs["intro"]:
        parts.append(f'<p>{p}</p>')
    for title, rows in fs["sections"]:
        parts.append(f'<h2 class="s">{title}</h2>')
        body = []
        for item, confirm, where in rows:
            body.append(f'<tr><td class="k">{item}</td><td>{confirm}</td>'
                        f'<td class="r">{where}</td></tr>')
        parts.append(f'<table class="ledger"><tr>'
                     f'<td class="led-h">Item</td><td class="led-h">What to confirm</td>'
                     f'<td class="led-h r">Where / mark</td></tr>{"".join(body)}</table>')
    parts.append(endmark())
    parts.append('</section>')
    return "".join(parts)

# ---- the cover ----
def cover_div():
    return f'<div class="coverpage">{maps.cover()}</div>'

# ================= ASSEMBLE =================
def build():
    # order: cover, front matter (opening, howto, contents), ground..timing,
    #        decisions, eating..closing, field sheet
    flow_parts = []
    # front matter chapters
    flow_parts.append(chapter_section(CHAPTERS_BEFORE[0], first=True))   # opening
    flow_parts.append(chapter_section(CHAPTERS_BEFORE[1]))               # how to read
    flow_parts.append(contents_section())                               # contents
    for ch in CHAPTERS_BEFORE[2:]:                                      # ground..timing
        flow_parts.append(chapter_section(ch))
    for d in DECISIONS:                                                 # the decisions
        flow_parts.append(decision_section(d))
    for ch in CHAPTERS_AFTER:                                           # eating..closing
        flow_parts.append(chapter_section(ch))
    flow_parts.append(fieldsheet_section())                            # field sheet

    flow = '<div class="flow">' + "".join(flow_parts) + '</div>'

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Greece, in Order.</title>
<style>{css()}</style>
</head><body>
{cover_div()}
{flow}
</body></html>"""

    out = os.path.join(BUILD, "dossier3.html")
    open(out, "w", encoding="utf-8").write(html)
    # report + figure appearance order
    import re
    words = len(re.sub("<[^>]+>", " ", flow).split())
    print(f"built dossier3.html · ~{words} words in flow · {len(_FIGN)} figures: "
          + ", ".join(f"{k}=FIG.{v}" for k,v in _FIGN.items()))
    return out

if __name__ == "__main__":
    build()
