#!/usr/bin/env python3
# build3.py — execs the content modules → dossier3.html
# The CSS is in design2.py (bug log #1). Never inline a style block here.
# ─────────────────────────────────────────────────────────────────────────────
import os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from design2 import CSS
from content import DECISIONS
from prose import ESSAYS, BACK
from content2 import OPERATIONS
from content3 import EXTRAS
from maps import FIGURES
from covers import cover_svg

# ── figure emit guard: one draw each, numbered by APPEARANCE order (bug #28) ──
_NUM, _DRAWN = {}, set()

def fignum(key):
    if key not in _NUM:
        _NUM[key] = len(_NUM) + 1
    return _NUM[key]

def fig_block(key):
    """Emit a figure exactly once. Returns '' on a repeat."""
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


XREF_RE = re.compile(r'\bDecision (0[1-9])\b(?! of)')

def xref(t):
    """Turn a bare 'Decision 02' into a live reference that prints its page."""
    return XREF_RE.sub(
        lambda m: f'<a class="xref" href="#c{m.group(1)}">Decision {m.group(1)}</a>', t)

def subst_marks(t):
    """The reasoning blocks are plain strings, so {EST}-style tokens never
    interpolated and printed literally in the book. Substitute at build time."""
    for k, v in MARKS.items():
        t = t.replace(k, v)
    return t

MARK_RE = re.compile(r"<span class='mk (?:est|off|sur|vol)'>[^<]*</span>")

def season_marks(html_block):
    """One mark per prose paragraph, parked at the end. Ledger cells untouched."""
    def fix(m):
        inner = m.group(2)   # group 1 is the named 'attrs' group
        marks = MARK_RE.findall(inner)
        if not marks:
            return m.group(0)
        stripped = MARK_RE.sub("", inner)
        stripped = re.sub(r"\s+([.,;:])", r"\1", stripped).rstrip()
        return f"<p{m.group('attrs')}>{stripped} {marks[0]}</p>"
    return re.sub(r"<p(?P<attrs>[^>]*)>(.*?)</p>", fix, html_block, flags=re.S)



# The TOC's left rail. v1 printed kind[:3], which gave "THE" seven times; this
# names the book's actual parts instead.
TOC_RAIL = {
 "The contract":"OPEN", "How to read it":"OPEN",
 "The ground":"GROUND", "Before you fly":"BEFORE", "Day zero":"BEFORE",
 "The rhythm":"ON THE GROUND", "The set pieces":"ON THE GROUND",
 "Where to stay":"ON THE GROUND", "The plan":"ON THE GROUND",
 "The horizons":"ON THE GROUND", "The kit":"ON THE GROUND",
 "Eating":"ON THE GROUND", "Money":"ON THE GROUND",
 "Failure modes":"BACK", "Back matter":"BACK", "Closing":"BACK",
}

_PLATES_DONE = set()

def plate(slot, caption):
    """A photographic plate: full column, 3:2, emitted INSIDE the prose (layout.md
    defect 3). Letter by SLOT, never by page order (bug log #17)."""
    if slot in _PLATES_DONE:
        return ""
    _PLATES_DONE.add(slot)
    letter = chr(64 + int(slot[1:]))
    return (f'<figure class="plate" id="plate-{slot}">'
            f'<img src="img/{slot}.jpg" alt="{html.escape(caption)}">'
            f'<figcaption><span class="fnum">PL. {letter}</span> &nbsp;{caption}</figcaption>'
            f'</figure>')

def srcs(rh, pos=""):
    out = f'<span class="rh-src">{html.escape(rh)}</span>'
    if pos:
        out += f'<span class="pos-src">{html.escape(pos)}</span>'
    return out

# ── sections ─────────────────────────────────────────────────────────────────
def essay(e, idx_total=None):
    sid = re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')
    p = [f'<section class="chap" id="{sid}">']
    p.append('<div class="opener">')
    p.append(f'<div class="okind">{html.escape(e["kind"])}</div>')
    p.append(f'<h1>{e["title"]}</h1>')
    p.append('<div class="orule"></div></div>')
    p.append(srcs(e["title"], e["kind"]))
    if e.get("standfirst"):
        p.append(f'<p class="standfirst">{e["standfirst"]}</p>')

    body = xref(season_marks(subst_marks(e["body"].strip())))
    # a chapter's PLATE goes inside the prose too, deeper than the figure
    if e.get("plate"):
        parts = body.split('</p>')
        at = min(e.get("plate_after", 3), max(0, len(parts) - 1))
        body = ('</p>'.join(parts[:at]) + '</p>'
                + plate(e["plate"], e["plate_cap"])
                + '</p>'.join(parts[at:]))
    # a chapter's figure goes INSIDE the prose, after the 2nd paragraph (layout.md)
    if e.get("fig"):
        parts = body.split('</p>')
        at = min(2, max(0, len(parts) - 1))
        body = '</p>'.join(parts[:at]) + '</p>' + fig_block(e["fig"]) + '</p>'.join(parts[at:])
    p.append(body)
    p.append('<div class="endmark">&#9670;</div>')
    p.append('</section>')
    return "".join(p)


def decision(d, total):
    # markup convention the shipped gates read: id="cNN", class carries "decision"
    sid = f'c{d["n"]}'
    p = [f'<section class="dec chap decision" id="{sid}">']
    p.append('<div class="opener">')
    p.append(f'<div class="onum">{d["n"]}</div>')
    p.append(f'<div class="okind">{html.escape(d["cat"])}</div>')
    p.append(f'<h1>{d["q"]}</h1>')
    p.append('<div class="orule"></div></div>')
    p.append(srcs(f'{d["cat"]} — {d["q"]}', f'Decision {d["n"]} of {total:02d}'))

    p.append(season_marks(f'<p class="lede">{d["lede"]}</p>'))

    # the figure sits under the paragraph that introduced the problem
    if d.get("fig"):
        p.append(fig_block(d["fig"]))

    # ROLE: ledger — the instrument
    p.append('<div class="ledger">')
    p.append(f'<div class="lcap">{d["table_title"]}</div>')
    p.append(f'<table><tr><th>{html.escape(d["cols"].split(" · ")[0])}</th>'
             f'<th style="text-align:right">{html.escape(d["cols"].split(" · ")[-1])}</th></tr>')
    for left, right in d["rows"]:
        # ledger cells go through the token substitution too — a row written as a
        # plain string would otherwise print "{EST}" in the book
        p.append(f'<tr><td>{subst_marks(left)}</td><td>{subst_marks(right)}</td></tr>')
    p.append('</table></div>')

    # ROLE: reasoning — the argument between the instrument and the call
    if d.get("reasoning"):
        p.append(xref(season_marks(subst_marks(d["reasoning"]))))

    if d.get("plate"):
        p.append(plate(d["plate"], d["plate_cap"]))

    # ROLE: verdict — must outweigh the prose
    p.append('<div class="verdict"><span class="vlab">The call</span>'
             f'<p>{xref(d["verdict"])}</p></div>')

    # ROLE: forks — labelled by MEANING (roles.md)
    # Wrapped with the note + endmark as one atomic tail: pp.30/32/36 of the first
    # printing each carried nothing but the note, orphaned off the previous page.
    p.append('<div class="dtail">')
    p.append('<div class="forks">')
    p.append('<div class="fork f"><b>When the other call is right</b><ul>'
             + "".join(f'<li>{x}</li>' for x in d["for"]) + '</ul></div>')
    p.append('<div class="fork a"><b>When ours is wrong for you</b><ul>'
             + "".join(f'<li>{x}</li>' for x in d["against"]) + '</ul></div>')
    p.append('</div>')

    # a tail figure rides INSIDE the atomic tail so it lands on the tail page,
    # which is where the thin chapters were ending at ~37% fill
    if d.get("tailfig"):
        p.append(fig_block(d["tailfig"]))

    p.append(f'<div class="note">{xref(subst_marks(d["note"]))}</div>')
    p.append('<div class="endmark">&#9670;</div>')
    p.append('</div>')          # /dtail
    p.append('</section>')
    return "".join(p)


def toc(entries):
    p = ['<section class="chap toc" id="contents">']
    p.append('<div class="opener"><div class="okind">Contents</div>'
             '<h1>What is in this book</h1><div class="orule"></div></div>')
    p.append(srcs("Contents", "Contents"))
    p.append('<ol>')
    prev = None
    for kind, title, sid in entries:
        # the rail groups; print it only when the part changes, so it reads as a
        # section break rather than the same word stamped down the margin
        shown = "" if kind == prev else kind
        prev = kind
        p.append(f'<li{" class=\"tgroup\"" if shown else ""}>'
                 f'<span class="tnum">{html.escape(shown)}</span>'
                 f'<a href="#{sid}">{title}</a>'
                 f'<span class="tdot"></span>'
                 f'<span class="tpg"><a href="#{sid}"></a></span></li>')
    p.append('</ol>')
    p.append('<div class="endmark">&#9670;</div></section>')
    return "".join(p)


FIELD_SHEET_ROWS = [
 ("Japan Rail Pass — 7-day ordinary", "&#165;50,000"),
 ("Japan Rail Pass — 7-day Green", "&#165;70,000"),
 ("Overseas-agency price from 1 Oct 2026 — ordinary", "&#165;53,000"),
 ("Overseas-agency price from 1 Oct 2026 — Green", "&#165;74,000"),
 ("Tokyo &#8594; Kyoto, reserved ordinary (Hikari)", "about &#165;13,850"),
 ("Nozomi supplement, Tokyo &#8594; Kyoto", "about &#165;4,960"),
 ("IC card maximum stored balance", "&#165;20,000"),
 ("IC card deposit (unregistered, refundable)", "&#165;500"),
 ("Tokyo Subway Ticket — 24 / 48 / 72h", "&#165;1,000 / 1,500 / 2,000"),
 ("Kyoto Subway &amp; Bus One-Day Pass", "about &#165;1,100"),
 ("Welcome Suica validity", "28 days"),
]

def field_sheet(standalone=False):
    p = ['<section class="chap fs" id="field-sheet">']
    kind = 'Japan, Worked Out. &#183; reissued quarterly' if standalone else 'The annex'
    p.append(f'<div class="opener"><div class="okind">{kind}</div>'
             '<h1>Field Sheet</h1><div class="orule"></div></div>')
    p.append(srcs("Field Sheet", "Field Sheet"))
    p.append('<p class="standfirst">Every volatile figure in one place, dated. '
             'When this disagrees with the book, this is right and the book is old.</p>')
    if standalone:
        # The URL is printed IN the sheet, which is why it must be generic — the
        # same PDF goes to every buyer, so it cannot carry a per-buyer link.
        p.append('<div class="renew">'
                 '<div class="lcap">This sheet expires. The next one is free.</div>'
                 '<p>Reissued every quarter. To pull the current one, go to '
                 '<b>japanforamericans.com/guide/sheet</b> and enter the email you '
                 'bought the guide with.</p></div>')
        p.append('<p>This sheet is the short half of a two-document set. The book argues '
                 'the decisions and is built to stay true for about two years; this sheet '
                 'carries the numbers those arguments run on and is reissued every quarter. '
                 'Print it, or keep it on the phone &#8212; it is the half you want with you '
                 'at a ticket window.</p>')
    p.append('<p>Checked September 2026. Rail prices are official and were confirmed against '
             'the operator&#8217;s own price page; the 1 October 2026 rise applies to '
             'overseas-agency purchases only and not to the official booking site. '
             'Re-check before you buy &#8212; the method in Decision 02 outlives every number '
             'in this table.</p>')
    p.append('<table><tr><th>Figure</th><th>Value</th></tr>')
    for k, v in FIELD_SHEET_ROWS:
        p.append(f'<tr><td>{k}</td><td>{v}</td></tr>')
    p.append('</table>')
    p.append('<div class="endmark">&#9670;</div></section>')
    return "".join(p)


def main():
    total = len(DECISIONS)
    entries, body = [], []

    for e in ESSAYS:
        sid = re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid))
    for e in OPERATIONS:
        sid = re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid))
    for e in EXTRAS:
        sid = re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid))
    for d in DECISIONS:
        entries.append((d["n"], d["q"], f'c{d["n"]}'))
    for e in BACK:
        sid = re.sub(r'[^a-z0-9]+', '-', e["title"].lower()).strip('-')
        entries.append((TOC_RAIL.get(e["kind"], "·"), e["title"], sid))

    # cover — NOT inside .flow. Inside the flow it inherits the default page box
    # (892px content) and a 1056px full-bleed div spills its foot onto page 2,
    # producing an unfurnished sheet that fails the furniture gate.
    cover_html = f'<div class="coverpage">{cover_svg()}</div>'

    # opening + how-to-read, then contents, then the rest
    body.append(essay(ESSAYS[0]))
    body.append(essay(ESSAYS[1]))
    body.append(toc(entries))
    for e in ESSAYS[2:]:
        body.append(essay(e))
    for e in OPERATIONS:
        body.append(essay(e))
    for e in EXTRAS:
        body.append(essay(e))
    for d in DECISIONS:
        body.append(decision(d, total))
    for e in BACK:
        body.append(essay(e))

    doc = (
      '<!doctype html><html lang="en"><head><meta charset="utf-8">'
      '<title>Japan, Worked Out.</title>'
      f'<style>{CSS}</style></head><body>'
      f'{cover_html}<div class="flow">{"".join(body)}</div>'
      '</body></html>'
    )
    # ── the Field Sheet, as its own document ────────────────────────────────
    sheet = (
      '<!doctype html><html lang="en"><head><meta charset="utf-8">'
      '<title>Japan, Worked Out. — Field Sheet</title>'
      f'<style>{CSS}</style></head><body>'
      f'<div class="flow">{field_sheet(standalone=True)}</div>'
      '</body></html>'
    )
    sheet_out = os.path.join(HERE, "fieldsheet.html")
    with open(sheet_out, "w", encoding="utf-8") as f:
        f.write(sheet)
    print(f"wrote {sheet_out}  ({os.stat(sheet_out).st_size:,} bytes)")

    out = os.path.join(HERE, "dossier3.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)

    # bug log #2: printing a number is NOT evidence the file was written
    st = os.stat(out)
    words = len(re.sub(r'<[^>]+>', ' ', doc).split())
    print(f"wrote {out}")
    print(f"  bytes   {st.st_size:,}")
    print(f"  mtime   {st.st_mtime}")
    print(f"  words   ~{words:,}")
    print(f"  figures drawn: {sorted(_DRAWN)}")
    print(f"  sections: {doc.count('<section')}  decisions: {total}")
    undrawn = set(FIGURES) - _DRAWN
    if undrawn:
        print(f"  !! figures defined but never emitted: {sorted(undrawn)}")

if __name__ == "__main__":
    main()
