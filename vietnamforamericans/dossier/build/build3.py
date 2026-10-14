#!/usr/bin/env python3
# build3.py — execs the content modules → dossier3.html (+ the compile templates)
# The CSS is in design2.py (bug log #1). Never inline a style block here.
#
# OUTPUTS
#   dossier3.html        the whole book incl. the Field Sheet — what the legacy
#                        gates, emit-manuscript and add-nav read
#   fieldsheet.html      the sheet alone (Japan convention; fssplit also works)
#   book.template.html   the book with {{claim:id}} tokens, for compile-guide.py
#   sheet.template.html  the sheet with tokens
#   evidence.json is NOT written here — see evidence.py
# ─────────────────────────────────────────────────────────────────────────────
import os, re, sys, html, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from design2 import CSS
from content import DECISIONS
from prose import ESSAYS, BACK
from content2 import OPERATIONS
from content3 import EXTRAS
from maps import FIGURES
from covers import cover_svg
from evidence import CLAIMS, SHEET_ROWS, RELEASE_DATE, EDITION

TITLE = "Vietnam, End to End."
SITE = "vietnamforamericans.com"

# ── figure emit guard: one draw each, numbered by APPEARANCE order (bug #28) ──
_NUM, _DRAWN = {}, set()

def fignum(key):
    if key not in _NUM:
        _NUM[key] = len(_NUM) + 1
    return _NUM[key]

def fig_block(key):
    if key in _DRAWN or key not in FIGURES:
        return ""
    _DRAWN.add(key)
    fn, cap = FIGURES[key]
    n = fignum(key)
    return (f'<figure class="fig" id="fig-{key}">{fn()}'
            f'<figcaption><span class="fnum">FIG.{n}</span> &nbsp;{cap}</figcaption></figure>')


MARKS = {"{EST}": "<span class='mk est'>&#9679;</span>",
         "{OFF}": "<span class='mk off'>&#9671;</span>",
         "{SUR}": "<span class='mk sur'>&#9650;</span>",
         "{VOL}": "<span class='mk vol'>&#9670;</span>"}

XREF_RE = re.compile(r'\bDecision (0[1-9]|1[0-9])\b(?! of)')

def xref(t):
    return XREF_RE.sub(
        lambda m: f'<a class="xref" href="#c{m.group(1)}">Decision {m.group(1)}</a>', t)

def subst_marks(t):
    for k, v in MARKS.items():
        t = t.replace(k, v)
    return t

CLAIM_RE = re.compile(r'\{C:([a-z0-9-]+)\}')
_USED_CLAIMS = {}

def subst_claims(t, mode):
    """mode='final' → the display.book text, html-escaped as compile-guide does;
    mode='template' → the {{claim:id}} token for compile-guide.py."""
    def rep(m):
        cid = m.group(1)
        if cid not in CLAIMS:
            raise KeyError(f"unknown claim {cid}")
        _USED_CLAIMS[cid] = _USED_CLAIMS.get(cid, 0) + 1
        if mode == "template":
            return "{{claim:" + cid + "}}"
        return html.escape(CLAIMS[cid]["display"]["book"], quote=True)
    return CLAIM_RE.sub(rep, t)

MARK_RE = re.compile(r"<span class='mk (?:est|off|sur|vol)'>[^<]*</span>")

def season_marks(block):
    """One mark per prose paragraph, parked at the end. Ledger cells untouched."""
    def fix(m):
        inner = m.group(2)
        marks = MARK_RE.findall(inner)
        if not marks:
            return m.group(0)
        stripped = MARK_RE.sub("", inner)
        stripped = re.sub(r"\s+([.,;:])", r"\1", stripped).rstrip()
        return f"<p{m.group('attrs')}>{stripped} {marks[0]}</p>"
    return re.sub(r"<p(?P<attrs>[^>]*)>(.*?)</p>", fix, block, flags=re.S)


TOC_RAIL = {
 "The contract":"OPEN", "How to read it":"OPEN",
 "The ground":"GROUND", "Before you fly":"BEFORE", "Day zero":"BEFORE",
 "The rhythm":"ON THE GROUND", "The set pieces":"ON THE GROUND",
 "Where to stay":"ON THE GROUND", "The plan":"ON THE GROUND",
 "The horizons":"ON THE GROUND", "The kit":"ON THE GROUND",
 "Eating":"ON THE GROUND", "Risk":"ON THE GROUND",
 "Failure modes":"BACK", "Back matter":"BACK", "Closing":"BACK",
}

_PLATES_DONE = set()

def plate(slot, caption):
    if slot in _PLATES_DONE:
        return ""
    _PLATES_DONE.add(slot)
    letter = chr(64 + int(slot[1:]))
    return (f'<figure class="photo" id="plate-{slot}">'
            f'<img src="img/{slot}.jpg" alt="{html.escape(caption)}">'
            f'<figcaption><span class="fnum">PL. {letter}</span> &nbsp;{caption}</figcaption>'
            f'</figure>')

def srcs(rh, pos=""):
    out = f'<span class="rh-src" data-content-audit="furniture">{html.escape(rh)}</span>'
    if pos:
        out += f'<span class="pos-src" data-content-audit="furniture">{html.escape(pos)}</span>'
    return out

def pack(parts, body_html, floor=55):
    """Bind the opener to enough body that it cannot strand (build-traps #4):
    accumulate paragraphs until >= `floor` words ride inside the pack."""
    import re as _re
    chunks = _re.split(r'(?<=</p>)', body_html)
    acc, i = 0, 0
    while i < len(chunks) and acc < floor:
        acc += len(_re.sub(r'<[^>]+>', ' ', chunks[i]).split()); i += 1
    head = "".join(chunks[:i]); rest = "".join(chunks[i:])
    return '<div class="pack">' + "".join(parts) + head + '</div>' + rest

def sid_of(e):
    return re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')

# ── sections ─────────────────────────────────────────────────────────────────
FRESH = {"the-ground", "failure-modes", "contents"}

def essay(e, mode):
    sid = sid_of(e)
    fresh = " fresh" if (e.get("fresh") or sid in FRESH or e["kind"] in ("The ground","Failure modes")) else ""
    p = [f'<section class="dec chap{fresh}" id="{sid}">']
    op = ['<div class="opener">',
          f'<div class="okind">{html.escape(e["kind"])}</div>',
          f'<h1>{e["title"]}</h1>',
          '<div class="orule"></div></div>',
          srcs(e["title"], e["kind"])]
    if e.get("standfirst"):
        op.append(f'<p class="standfirst">{e["standfirst"]}</p>')
    body = xref(season_marks(subst_marks(subst_claims(e["body"].strip(), mode))))
    if e.get("plate"):
        parts = body.split('</p>')
        at = min(e.get("plate_after", 3), max(0, len(parts) - 1))
        body = ('</p>'.join(parts[:at]) + '</p>' + plate(e["plate"], e["plate_cap"])
                + '</p>'.join(parts[at:]))
    if e.get("fig"):
        parts = body.split('</p>')
        at = min(e.get("fig_after", 2), max(0, len(parts) - 1))
        body = '</p>'.join(parts[:at]) + '</p>' + fig_block(e["fig"]) + '</p>'.join(parts[at:])
    p.append(pack(op, body))
    p.append('<div class="endmark">&#10070;</div>')
    p.append('</section>')
    return "".join(p)


def decision(d, total, mode):
    sid = f'c{d["n"]}'
    cols = d["cols"]
    assert isinstance(cols, list) and len(cols) == 2, d["n"]
    for r in d["rows"]:
        assert len(r) == len(cols), f'decision {d["n"]}: row arity {len(r)} != {len(cols)}: {r[0][:40]}'
    fresh = " fresh" if d["n"] == "01" else ""
    p = [f'<section class="dec chap{fresh}" id="{sid}">']
    p.append('<div class="pack"><div class="opener">')
    p.append(f'<div class="onum">{d["n"]}</div>')
    p.append(f'<div class="okind">{html.escape(d["cat"])}</div>')
    p.append(f'<h1>{d["q"]}</h1>')
    p.append('<div class="orule"></div></div>')
    p.append(srcs(f'{d["cat"]} — {d["q"]}', f'Decision {d["n"]} of {total:02d}'))
    p.append(season_marks(f'<p class="lede">{subst_claims(subst_marks(d["lede"]), mode)}</p>'))
    p.append('</div>')
    if d.get("fig"):
        p.append(fig_block(d["fig"]))
    # ROLE: ledger. Wide right column when any right cell is long.
    wide = any(len(r[1]) > 34 for r in d["rows"])
    p.append(f'<div class="ledger{" wrap" if wide else ""}">')
    p.append(f'<div class="lcap">{d["table_title"]}</div>')
    p.append(f'<table><tr><th>{html.escape(cols[0])}</th>'
             f'<th{"" if wide else " style=\"text-align:right\""}>{html.escape(cols[1])}</th></tr>')
    for left, right in d["rows"]:
        p.append(f'<tr><td>{subst_marks(left)}</td><td>{subst_marks(right)}</td></tr>')
    p.append('</table></div>')
    if d.get("reasoning"):
        p.append(xref(season_marks(subst_marks(subst_claims(d["reasoning"], mode)))))
    p.append('<div class="verdict"><span class="vlab">The call</span>'
             f'<p>{xref(subst_claims(d["verdict"], mode))}</p></div>')
    p.append('<div class="dtail">')
    p.append('<div class="forks">')
    p.append('<div class="fork f"><b>When the other call is right</b><ul>'
             + "".join(f'<li>{x}</li>' for x in d["for"]) + '</ul></div>')
    p.append('<div class="fork a"><b>When ours is wrong for you</b><ul>'
             + "".join(f'<li>{x}</li>' for x in d["against"]) + '</ul></div>')
    p.append('</div>')
    if d.get("tailfig"):
        p.append(fig_block(d["tailfig"]))
    p.append(f'<div class="note">{xref(subst_marks(subst_claims(d["note"], mode)))}</div>')
    p.append('</div>')
    if d.get("plate"):
        p.append(plate(d["plate"], d["plate_cap"]))
    p.append('<div class="endmark">&#10070;</div>')
    p.append('</section>')
    return "".join(p)


def toc(entries, sheet_separate=False):
    p = ['<section class="dec chap toc fresh" id="contents">']
    p.append('<div class="opener"><div class="okind">Contents</div>'
             '<h1>What is in this book</h1><div class="orule"></div></div>')
    p.append(srcs("Contents", "Contents"))
    p.append('<ol>')
    prev = None
    for kind, title, sid in entries:
        shown = "" if kind == prev else kind
        prev = kind
        if sid == "field-sheet":
            p.append(f'<li{" class=\"tgroup\"" if shown else ""}>'
                     f'<span class="tnum">{html.escape(shown)}</span>'
                     f'<span>{title}</span><span class="tdot"></span>'
                     f'<span class="tpg"><span class="sep">separate sheet</span></span></li>')
            continue
        p.append(f'<li{" class=\"tgroup\"" if shown else ""}>'
                 f'<span class="tnum">{html.escape(shown)}</span>'
                 f'<a href="#{sid}" class="row">{title}'
                 f'<span class="tdot"></span></a></li>')
    p.append('</ol>')
    p.append('<div class="endmark">&#10070;</div></section>')
    return "".join(p)


def field_sheet(mode, standalone=False):
    """The dated companion. Every row is bound to a claim's display.sheet text."""
    def sheet(cid):
        _USED_CLAIMS[cid] = _USED_CLAIMS.get(cid, 0) + 1
        if mode == "template":
            return "{{claim:" + cid + "}}"
        return html.escape(CLAIMS[cid]["display"]["sheet"], quote=True)
    p = ['<section class="dec chap fs" id="field-sheet">']
    kind = f'{TITLE} &#183; reissued quarterly' if standalone else 'The companion'
    p.append(f'<div class="opener"><div class="okind">{kind}</div>'
             '<h1>Field Sheet</h1><div class="orule"></div></div>')
    p.append(srcs("Field Sheet", f"Edition {EDITION}"))
    p.append('<p class="standfirst">Every volatile figure in one place, dated. When this '
             'disagrees with the book, this is right and the book is old.</p>')
    if standalone:
        p.append('<div class="renew">'
                 '<div class="lcap">This sheet expires. The next one is free.</div>'
                 f'<p>Issued {RELEASE_DATE}. Reissued every quarter. To pull the current one, go to '
                 f'<b>{SITE}/guide/sheet</b> and enter the email you bought the manual with.</p></div>')
        p.append('<p>This sheet is the short half of a two-document set. The book argues '
                 'the decisions and is built to stay true for about two years; this sheet '
                 'carries the numbers those arguments run on and is reissued every quarter. '
                 'Print it, or keep it on the phone &#8212; it is the half you want with you '
                 'at a counter.</p>')
    p.append(f'<p>Checked {RELEASE_DATE}. Each row names the source it was read from, as a '
             'clickable address, and the decision it can reverse. A row marked <em>confirm in '
             'your travel week</em> is a figure no primary source publishes as a schedule: the '
             'sheet tells you where to look rather than printing a number it cannot stand behind.</p>')
    cur = None
    for group, label, cid, src, flips in SHEET_ROWS:
        if group != cur:
            p.append(f'<h2>{html.escape(group)}</h2>')
            cur = group
        url = src or None
        shown_url = html.escape(url).replace("/", "/&#8203;") if url else ""
        src_html = (f'<div class="fssrc"><a href="{html.escape(url)}">{shown_url}</a></div>' if url else '')
        flips_html = f'<div class="fsflip">{html.escape(flips)}</div>' if flips else ''
        p.append(f'<div class="fsrow"><div class="fslab">{label}</div>'
                 f'<div class="fsval">{sheet(cid)}</div>{src_html}{flips_html}</div>')
    p.append('<div class="endmark">&#10070;</div></section>')
    return "".join(p)


def assemble(mode):
    """mode: 'final' (dossier3.html) or 'template' (compile-guide input)."""
    global _NUM, _DRAWN, _PLATES_DONE, _USED_CLAIMS
    _NUM, _DRAWN, _PLATES_DONE, _USED_CLAIMS = {}, set(), set(), {}
    total = len(DECISIONS)
    entries, body = [], []
    for e in ESSAYS:
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid_of(e)))
    for e in OPERATIONS:
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid_of(e)))
    for e in EXTRAS:
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid_of(e)))
    for d in DECISIONS:
        entries.append((d["n"], d["q"], f'c{d["n"]}'))
    for e in BACK:
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid_of(e)))
    entries.append(("COMPANION", "Field Sheet", "field-sheet"))

    cover_html = f'<div class="coverpage">{cover_svg()}</div>'
    body.append(essay(ESSAYS[0], mode))
    body.append(essay(ESSAYS[1], mode))
    body.append(toc(entries))
    for e in ESSAYS[2:]:
        body.append(essay(e, mode))
    for e in OPERATIONS:
        body.append(essay(e, mode))
    for e in EXTRAS:
        body.append(essay(e, mode))
    for d in DECISIONS:
        body.append(decision(d, total, mode))
    for e in BACK:
        body.append(essay(e, mode))
    head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>{TITLE}</title>'
            f'<style>{CSS}</style></head><body>')
    book = head + f'{cover_html}<div class="flow">{"".join(body)}</div></body></html>'
    book_used = dict(_USED_CLAIMS)
    _USED_CLAIMS = {}
    sheet = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
             f'<title>{TITLE} — Field Sheet</title>'
             f'<style>{CSS}</style></head><body>'
             f'<div class="flow">{field_sheet(mode, standalone=True)}</div>'
             '</body></html>')
    sheet_used = dict(_USED_CLAIMS)
    return book, sheet, book_used, sheet_used


def main():
    book, sheet, bu, su = assemble("final")
    tbook, tsheet, _, _ = assemble("template")
    for name, doc in (("dossier3.html", book), ("fieldsheet.html", sheet),
                      ("book.template.html", tbook), ("sheet.template.html", tsheet)):
        out = os.path.join(HERE, name)
        with open(out, "w", encoding="utf-8") as f:
            f.write(doc)
        st = os.stat(out)
        print(f"wrote {name}  {st.st_size:,} B  mtime {st.st_mtime:.0f}")
    words = len(re.sub(r'<[^>]+>', ' ', book).split())
    print(f"  words   ~{words:,}")
    print(f"  figures drawn: {sorted(_DRAWN)}")
    print(f"  plates: {sorted(_PLATES_DONE)}")
    print(f"  sections: {book.count('<section')}  decisions: {len(DECISIONS)}")
    print(f"  claims bound in book: {len(bu)}  in sheet: {len(su)}")
    undrawn = set(FIGURES) - _DRAWN
    if undrawn:
        print(f"  !! figures defined but never emitted: {sorted(undrawn)}")
    missing = [c for c in CLAIMS if CLAIMS[c].get("critical") and CLAIMS[c]["display"].get("book") and c not in bu]
    if missing:
        print(f"  !! critical claims with book text NOT bound in the book: {missing}")
    json.dump({"book": bu, "sheet": su}, open(os.path.join(HERE, "_claims-used.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
