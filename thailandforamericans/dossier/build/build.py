# -*- coding: utf-8 -*-
"""build.py — emit dossier3.html for Thailand, Covered.

The book in reading order: cover, the key page, the calendar essay (which governs
the decisions that follow it), eight decisions, three closing essays.

Enforces, at build time, the things the 2026-09-18 pass found shipped:
  · a ledger row whose length differs from `cols` FAILS the build. Rome p12 shipped
    three headers over two-cell rows because `cols` was a free string.
  · a provenance token that is not substituted FAILS the build. Japan printed
    `{EST}` literally eleven times because the blocks were plain strings.
"""
import base64, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from design import CSS
from figures import FIGURES, as_img
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))


def marks(t: str) -> str:
    for k, v in C.MARKS.items():
        t = t.replace("{" + k + "}", v)
    return t


def check(html: str):
    """Fail the build rather than ship the artefact."""
    import glob
    declared = {d["plate"]["slot"] for d in
                list(C.DECISIONS) + C.ESSAYS_FRONT + C.ESSAYS_BACK
                + [C.ESSAY_RISK, C.REFUSALS] if d.get("plate")}
    ondisk = {os.path.basename(f)[:-4] for f in
              glob.glob(os.path.join(HERE, "img", "A*.jpg"))}
    if declared != ondisk:
        raise SystemExit(
            f"BUILD FAILED — plate files and plate declarations disagree. "
            f"declared-not-on-disk: {sorted(declared-ondisk)} · "
            f"on-disk-not-declared: {sorted(ondisk-declared)}")
    leftover = re.findall(r"\{(est|off|sur|vol)\}", html)
    if leftover:
        raise SystemExit(f"BUILD FAILED — unsubstituted provenance tokens: {set(leftover)}")
    tabled = [e for e in C.ESSAYS_FRONT + C.ESSAYS_BACK
              + [C.REFUSALS, C.ESSAY_RISK] if e.get("cols")]
    for d in list(C.DECISIONS) + tabled:
        n = len(d["cols"])
        for i, row in enumerate(d["rows"]):
            if len(row) != n:
                raise SystemExit(
                    f"BUILD FAILED — decision {d['n']} row {i} has {len(row)} cells "
                    f"for {n} headers {d['cols']}. Do not pad, do not invent a value.")
        if d.get("colw") and len(d["colw"]) != n:
            raise SystemExit(
                f"BUILD FAILED — decision {d['n']} declares {len(d['colw'])} column "
                f"widths for {n} headers.")


def ledger(d) -> str:
    # table-layout:fixed splits unspecified columns evenly across what is left,
    # so naming only the first column is enough for the common shape: a short
    # label against sentences. A decision may override with `colw`.
    n = len(d["cols"])
    cw = d.get("colw") or (["label"] + [""] * (n - 1))
    cols = "".join(f'<col class="{c}">' if c else "<col>" for c in cw)
    th = "".join(f"<th>{c}</th>" for c in d["cols"])
    trs = []
    for i, row in enumerate(d["rows"]):
        hot = i == d.get("decisive_row")
        cls = ' class="decisive"' if hot else ""
        # cells carry provenance marks too — a figure in a ledger needs its
        # source stated more, not less, than the same figure in a sentence
        cells = [marks(c) for c in row]
        if hot:
            # The row is named in TEXT, never colour alone — but the wording is
            # DATA, not a CSS content string. "changes the choice" is false on an
            # essay ledger, which carries no choice to change.
            cells[0] += (f'<span class="dx">· '
                         f'{d.get("decisive_label", "changes the choice")}</span>')
        tds = "".join(f"<td>{c}</td>" for c in cells)
        trs.append(f"<tr{cls}>{tds}</tr>")
    # wrapped in its role container: roles.md names opener / ledger / verdict /
    # forks / partdiv, and the layout gate looks for exactly those names
    return (f'<div class="ledger"><table class="ledger">'
            f'<caption>{d["table_title"]}</caption>'
            f"<colgroup>{cols}</colgroup>"
            f"<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>")


def howto() -> str:
    H = C.HOWTO
    blocks = "".join(
        f'<div class="ht"><div class="k">{t}</div><p>{marks(b)}</p></div>'
        for t, b in H["blocks"])
    key = "".join(
        f'<tr><td class="keymark">{C.MARKS[k]}</td><td>{v}</td></tr>'
        for k, v in C.MARK_KEY)
    return f"""
<section class="front" id="howto" data-ref="howto">
  <span class="navtitle">How to read this</span>
  <span class="position"></span>
  <p class="eyebrow">{H['eyebrow']}</p>
  <h1>{H['title']}</h1>
  <p class="standfirst">{H['standfirst']}</p>
  <div class="htgrid">{blocks}</div>
  <table class="ledger keytable"><caption>The marks, and what each one claims</caption>
    <colgroup><col class="tiny"><col></colgroup>
    <tbody>{key}</tbody></table>
</section>"""


def cover_device() -> str:
    """The cover PROMISES; the interior proves. cover.md allows one device, at most
    three labels, and nothing below 24px at cover size — so the device carries the
    pattern and no axis labels at all. What the reader sees is seven places, four
    marks each, and a rule where the marks stop. FIG. 3 inside is the proof.
    A type-only cover was the previous state and it argued nothing."""
    rows = []
    for name, states, after_rule in C.COVER_DEVICE:
        dots = "".join(
            '<span class="cd cd-full"></span>' if x == 2 else
            ('<span class="cd cd-half"></span>' if x == 1 else
             '<span class="cd cd-none"></span>') for x in states)
        rule = ' cd-break' if after_rule else ''
        rows.append(f'<div class="cdrow{rule}"><span class="cdname">{name}</span>'
                    f'<span class="cddots">{dots}</span></div>')
    return f'<div class="device">{"".join(rows)}</div>'


def partdiv(P) -> str:
    """A part divider that carries the part's contents. The book had no contents
    of any kind before these — forty pages with no way in."""
    items = "".join(
        f'<div class="pi"><span class="pik">{k}</span>'
        f'<span class="piv">{v}</span></div>' for k, v in P["items"])
    return f"""
<section class="partdiv" id="{P['id']}" data-ref="{P['id']}">
  <span class="navtitle">{P['nav']}</span>
  <span class="position"></span>
  <p class="eyebrow">{P['eyebrow']}</p>
  <h1>{P['title']}</h1>
  <p class="standfirst">{P['blurb']}</p>
  <div class="pilist">{items}</div>
</section>"""


def essay(e) -> str:
    """An essay carries reporting the corpus supports but that is NOT a decision.
    It therefore has no verdict box and no fork lists — offering a call on
    material that holds no choice is how the previous edition padded."""
    table = ledger(e) if e.get("cols") else ""
    return f"""
<section class="essay" id="{e['id']}" data-ref="{e['id']}">
  <span class="navtitle">{e['nav']}</span>
  <span class="position"></span>
  <p class="eyebrow">{e['eyebrow']}</p>
  <h1 class="q">{e['q']}</h1>
  <p class="standfirst">{e['scope']}</p>
  <div class="prose">{prose(e)}</div>
  <div class="close">{plate(e) if e.get("plate_at") == "close" else ""}{table}
  {figure(e)}
  <p class="caption">{marks(e['note'])}</p>
  <p class="endmark">◆</p></div>
</section>"""


def fieldsheet() -> str:
    """Two cut-out cards, 3.25 x 4.5in, per c-write.md. Essential text, so the
    12px floor applies here exactly as it does in the body — a pocket card that
    has to be squinted at is not a pocket card."""
    F = C.FIELD_SHEET
    cards = []
    for c in F["cards"]:
        items = "".join(
            f'<li><span class="ck">{k}</span> {marks(v)}</li>' for k, v in c["items"])
        cards.append(f'<div class="card"><div class="cardhead">{c["title"]}</div>'
                     f'<p class="cardsub">{c["sub"]}</p><ul>{items}</ul></div>')
    return f"""
<section class="front fieldsheet" id="{F['id']}" data-ref="{F['id']}">
  <span class="navtitle">{F['nav']}</span>
  <span class="position"></span>
  <p class="eyebrow">{F['eyebrow']}</p>
  <h1 class="q">{F['q']}</h1>
  <p class="standfirst">{F['scope']}</p>
  <div class="cards">{"".join(cards)}</div>
  <p class="caption">{marks(F['note'])}</p>
</section>"""


_PLATE_CACHE = {}


def plate(d) -> str:
    """One photograph, embedded so the PDF is self-contained.

    The plate letter comes from the SLOT, never from page order. Rome lettered by
    page, so A06 printed as PL. F and A07 as PL. E — two names for one slot, and
    "swap E and G" meant different things to the person picking and the person
    reading.
    """
    p = d.get("plate")
    if not p:
        return ""
    slot = p["slot"]
    if slot not in _PLATE_CACHE:
        path = os.path.join(HERE, "img", f"{slot}.jpg")
        if not os.path.exists(path):
            raise SystemExit(f"BUILD FAILED — plate {slot} has no file at {path}. "
                             f"A paid PDF does not ship a placeholder.")
        with open(path, "rb") as fh:
            _PLATE_CACHE[slot] = ("data:image/jpeg;base64,"
                                  + base64.b64encode(fh.read()).decode())
    letter = chr(64 + int(slot[1:]))
    return (f'<figure class="photo" data-slot="{slot}">'
            f'<img src="{_PLATE_CACHE[slot]}" alt="">'
            f'<figcaption><span class="figlabel">PL. {letter}</span> '
            f'{marks(p["caption"])}</figcaption></figure>')


def prose(d) -> str:
    """The argument, with its plate sitting WITH the paragraph it argues for —
    never at the top of the page by default. Greece put every plate at the top and
    the result read like a stock header; on one page the caption and the paragraph
    beneath it were about different islands."""
    out = [f'<p class="lede">{marks(d["lede"])}</p>']
    after = -1 if d.get("plate_at") == "close" else d.get("plate", {}).get("after", -1)
    for i, para in enumerate(d["body"]):
        out.append(f"<p>{marks(para)}</p>")
        if i == after:
            out.append("</div>" + plate(d) + '<div class="prose">')
    return "".join(out)


def figure(d) -> str:
    """A decision carries at most one drawn figure, named by key. A key with no
    drawing behind it stops the build rather than emitting nothing — that is the
    failure mode this whole project keeps finding."""
    key = d.get("fig")
    if not key:
        return ""
    if key not in FIGURES:
        raise SystemExit(f"BUILD FAILED — decision {d['n']} asks for figure "
                         f"'{key}', which is not drawn in figures.py.")
    draw, label, cap = FIGURES[key]
    # as_img, not the raw <svg>: Paged.js splits an inline SVG across pages and
    # break-inside:avoid does not stop it. See figures._fontface().
    return (f'<figure class="drawn">{as_img(draw())}'
            f'<figcaption><span class="figlabel">{label}</span> {marks(cap)}'
            f'</figcaption></figure>')


def decision(d) -> str:
    forks = (
        '<div class="forks">'
        '<div><div class="k">Follow this if</div><ul>'
        + "".join(f"<li>{x}</li>" for x in d["for"]) + "</ul></div>"
        '<div><div class="k">Overrule it if</div><ul>'
        + "".join(f"<li>{x}</li>" for x in d["against"]) + "</ul></div></div>"
    )
    return f"""
<section class="dec chap decision" id="c{d['n']}" data-ref="c{d['n']}">
  <span class="navtitle">{d['nav']}</span>
  <span class="position">Decision {d['n']} of 08</span>
  <p class="eyebrow">{d['cat']} · decision {d['n']}</p>
  <h1 class="q">{d['q']}</h1>
  <p class="standfirst">{d['scope']}</p>

  <div class="opener">
    <div class="k">The call, and the exception</div>
    <p>{marks(d['open_call'])}</p>
    <p>{marks(d['open_exception'])}</p>
  </div>

  <div class="prose">{prose(d)}</div>

  {ledger(d)}
  {figure(d) if d.get("fig_at") != "close" else ""}

  <div class="verdict"><div class="k">The call</div><p>{marks(d['call'])}</p></div>
  {forks}
  <div class="close">{figure(d) if d.get("fig_at") == "close" else ""}
  <p class="caption">{marks(d['note'])}</p>
  <p class="endmark">◆</p></div>
</section>"""


def main():
    decs = (howto()
            + "".join(essay(e) for e in C.ESSAYS_FRONT)
            + partdiv(C.PARTS[0])
            + "".join(decision(d) for d in C.DECISIONS)
            + partdiv(C.PARTS[1])
            + essay(C.ESSAY_RISK)
            + "".join(essay(e) for e in C.ESSAYS_BACK)
            + essay(C.REFUSALS) + fieldsheet())
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{C.BOOK}</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body><div class="cover">
  <span class="booktitle">{C.BOOK}</span>
  <div class="wrap">
    <p class="press">{C.PRESS}</p>
    <h1>Thailand,<br>Covered.</h1>
    <p class="promise">{C.COVER_PROMISE}</p>
  </div>
  {cover_device()}
  <div class="foot">thailandforamericans.com &middot; edition 2026.09</div>
</div><div class="flow">{decs}</div>
</body></html>"""
    check(html)
    out = os.path.join(HERE, "dossier3.html")
    open(out, "w", encoding="utf-8").write(html)
    n_e = len(C.ESSAYS_FRONT) + len(C.ESSAYS_BACK)
    print(f"  wrote {out}  ({len(html):,} bytes, {len(C.DECISIONS)} decisions, "
          f"{n_e} essays)")


main()
