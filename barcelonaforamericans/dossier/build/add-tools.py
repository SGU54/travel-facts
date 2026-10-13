#!/usr/bin/env python3
"""add-tools.py — insert the "Before you book" spread into a finished dossier.

The review's standing criticism was that the books explain WHY well and finish HOW
inconsistently. This adds the three things that were missing fleet-wide: an ordered
checklist of the book's own calls, the questions that settle them said out loud,
and two worked trips with their assumptions printed rather than implied.

The checklist rows are GENERATED from calls.json, which was read out of each book's
own verdict blocks, and each row's folio is a Paged.js target-counter pointing at
the chapter. So the checklist cannot drift from the chapters, and cannot cite a
page that moved — the same guarantee the contents page gets.

Run:  python3 add-tools.py <book> <build-dir>
"""
import json, os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tools_content import BOOKS  # noqa: E402

CALLS = json.load(open(os.path.join(HERE, 'calls.json'), encoding='utf-8'))

# Per book: how its sections, headings and tables are written, so the new spread
# is indistinguishable from the pages around it. Getting this wrong is visible.
SKIN = {
    'rome': dict(
        sec='<section class="dec chap" id="{id}">',
        head='<div class="dnum">{eyebrow}</div><h1>{title}</h1>'
             '<p class="standfirst">{sf}</p>',
        end='</section>',
        table='<table class="ledger"><caption>{cap}</caption>{rows}</table>',
        hrow='<tr><th>{a}</th><th>{b}</th><th class="num">{c}</th></tr>',
        row='<tr><td class="opt">{a}</td><td>{b}</td><td class="num">{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
    'greece': dict(
        sec='<section class="dec chap" id="{id}" data-ref="{id}">',
        head='<div class="eyebrow">{eyebrow}</div><h1 class="t">{title}</h1>'
             '<span class="rh-src">{rh}</span><div class="standfirst">{sf}</div>',
        end='<div class="endmark"></div></section>',
        table='<table class="ledger">{rows}</table>',
        hrow='<tr><td class="led-h">{a}</td><td class="led-h">{b}</td><td class="led-h r">{c}</td></tr>',
        row='<tr><td class="k">{a}</td><td>{b}</td><td class="r">{c}</td></tr>',
        h2='<h2 class="s">{t}</h2>', p='<p>{t}</p>'),
    'morocco': dict(
        sec='<section class="dec chap essay" id="{id}" data-ref="{id}">',
        head='<div class="openpack"><div class="opener essayop"><p class="okind">{eyebrow}</p>'
             '<h1>{title}</h1><div class="orule"></div></div><span class="rh-src">{rh}</span>'
             '<span class="pos-src">{eyebrow}</span><p class="lead">{sf}</p></div>',
        end='</section>',
        table='<div class="ledger"><table>{rows}</table></div>',
        hrow='<tr><th>{a}</th><th>{b}</th><th>{c}</th></tr>',
        row='<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
    'turkey': dict(
        sec='<section class="dec chap" id="{id}">',
        head='<div class="opener"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1>'
             '<span class="rh-src">{rh}</span><p class="standfirst">{sf}</p><hr class="oprule"></div>',
        end='<p class="endmark">&#9670;</p></section>',
        table='<table><thead>{head}</thead><tbody>{rows}</tbody></table>',
        hrow='<tr><th>{a}</th><th>{b}</th><th>{c}</th></tr>',
        row='<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
    'japan': dict(
        sec='<section class="chap" id="{id}">',
        head='<div class="opener"><div class="okind">{eyebrow}</div><h1>{title}</h1>'
             '<div class="orule"></div></div><span class="rh-src">{rh}</span>'
             '<span class="pos-src">{eyebrow}</span><p class="standfirst">{sf}</p>',
        end='<div class="endmark">&#9670;</div></section>',
        table='<div class="ledger"><div class="lcap">{cap}</div><table>{rows}</table></div>',
        hrow='<tr><th>{a}</th><th>{b}</th><th>{c}</th></tr>',
        row='<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
    'barcelona': dict(
        sec='<section class="dec chap" id="{id}">',
        head='<span class="rh-src">{rh}</span><div class="kicker">{eyebrow}</div>'
             '<h1>{title}</h1><div class="standfirst">{sf}</div>',
        end='</section>',
        table='<table class="ledger"><caption>{cap}</caption>'
              '<thead>{head}</thead><tbody>{rows}</tbody></table>',
        hrow='<tr><th>{a}</th><th>{b}</th><th class="num">{c}</th></tr>',
        row='<tr><td><span class="opt">{a}</span></td>'
            '<td><span class="sub">{b}</span></td><td class="num">{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
    'thailand': dict(
        sec='<section class="essay" id="{id}" data-ref="{id}">',
        head='<span class="navtitle">{rh}</span><span class="position"></span>'
             '<p class="eyebrow">{eyebrow}</p><h1 class="q">{title}</h1>'
             '<p class="standfirst">{sf}</p>',
        end='<p class="endmark">◆</p></section>',
        table='<table class="ledger"><caption>{cap}</caption><tbody>{rows}</tbody></table>',
        hrow='<tr><td class="k"><b>{a}</b></td><td><b>{b}</b></td><td><b>{c}</b></td></tr>',
        row='<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td></tr>',
        h2='<h2>{t}</h2>', p='<p>{t}</p>'),
}

CSS = '''
/* ─── the "Before you book" spread ──────────────────────────────────────────
   Added 2026-09-29. The review's finding was that the books finish WHY and not
   HOW. The checklist folios are target-counters into the chapters, so they move
   when the chapters move; the counter hangs off the <a>, never the cell. */
.ckl a::after{ content:target-counter(attr(href), page); }
.ckl a{ text-decoration:none; color:inherit; }
.askbox{ break-inside:avoid; margin:13px 0 0 0; padding:9px 0 0 0;
  border-top:1px solid currentColor; }
.askbox > .who{ font-size:.78em; letter-spacing:.14em; text-transform:uppercase;
  opacity:.72; margin:0 0 6px 0; }
.askbox ul{ margin:0; padding-left:1.05em; }
.askbox li{ margin:0 0 4px 0; }
/* These tables are LISTS, not instruments. Japan (and Morocco) style .ledger with
   break-inside:avoid so an instrument is never split; a nine-row checklist is
   taller than the space after an opener, so Paged.js pushed it sheet after sheet
   and left the opener and the standfirst each alone on a near-empty page. */
#beforeyoubook .ledger, #beforeyoubook table{ break-inside:auto; break-before:auto; }
/* Keep a trip's name and its assumptions with the first rows of its table, but
   let the table itself break — pinning the whole block cost Turkey a tail page. */
.trip{ margin:15px 0 0 0; }
.trip .tname{ font-weight:600; margin:0 0 3px 0; break-after:avoid; }
.trip .tassume{ font-size:.86em; opacity:.78; margin:0 0 7px 0; break-after:avoid; }
.trip .twhy{ font-size:.9em; margin:7px 0 0 0; opacity:.9; break-before:avoid; }
/* The fallback table is four rows. Split, it sheds three onto a stub page;
   whole, it is half a sheet and closes the spread. Keep it whole. */
.fbwrap{ break-inside:avoid; }
'''


def esc(s):
    return html.escape(s, quote=False)


def build(book, calls):
    s, C = SKIN[book], BOOKS[book]
    # ── A. the checklist, generated from the book's own verdicts
    rows = [s['hrow'].format(a='DECIDE', b='THE CALL THIS BOOK MAKES', c='PAGE')]
    for i, c in enumerate(calls, 1):
        call = c['call'] or '—'
        # NO character budget. This line used to read
        #     if len(call) > 96: call = call[:93].rsplit(' ', 1)[0] + '…'
        # and it shipped sentences cut mid-clause into the summary table of SIX
        # books — "say euros, use…", "dinner on…", "and treat a…". An outside
        # reader found two of them in the Barcelona PDF in about ten minutes.
        # The cell is a table column: it wraps. There was never anything to cap.
        # Worse, each book's generated table was pasted back into its source, so
        # the damage froze and a rebuild could not undo it.
        rows.append(s['row'].format(
            a=esc(c['q'].rstrip('?') + '?'), b=esc(call),
            c=f'<span class="ckl"><a href="#{c["id"]}"></a></span>'))
    # rows[0] IS the header row (built above). Passing the whole list as `rows`
    # AND rows[0] as `head` emitted it twice — the repeated <thead> row inside
    # <tbody> that the same outside review reported. The turkey branch below
    # already sliced it off; the default never did.
    tbl = s['table'].format(rows=''.join(rows[1:]), head=rows[0], cap='Decide these first')
    if book == 'turkey':
        tbl = s['table'].format(head=rows[0], rows=''.join(rows[1:]), cap='')
    if book == 'barcelona':
        # this build's table has a real <thead>; leaving the head in rows too
        # printed the column titles twice, once as a header and once as a row.
        # The caption must not repeat the <h1> either — this build prints both,
        # so "DECIDE THESE FIRST" came out twice, three lines apart.
        tbl = s['table'].format(head=rows[0], rows=''.join(rows[1:]),
                                cap='The seven calls, in the order they bind')

    # ── B. the questions
    asks = []
    for who, qs in C['questions']:
        lis = ''.join(f'<li>{esc(q)}</li>' for q in qs)
        asks.append(f'<div class="askbox"><p class="who">{esc(who)}</p><ul>{lis}</ul></div>')

    # ── C. the worked trips
    trips = []
    for name, assume, legs, why in C['trips']:
        # Column heads are not decoration here. They name the unit — which is one
        # of these books' own stated rules — and they are also what tells the
        # layout gate a page carries an instrument rather than bare prose.
        lhead = s['hrow'].format(a='WHEN', b='WHAT HAPPENS', c='')
        lrows = lhead + ''.join(s['row'].format(a=esc(a), b=esc(b), c='') for a, b in legs)
        # the name already prints above as .tname; a caption repeats it
        t = s['table'].format(rows=lrows, head=lhead, cap='')
        trips.append(f'<div class="trip"><p class="tname">{esc(name)}</p>'
                     f'<p class="tassume">{esc(assume)}</p>{t}'
                     f'<p class="twhy">{esc(why)}</p></div>')

    # ── D. the fallbacks — a plan with none is finished only for a good day
    fhead = s['hrow'].format(a='WHEN THIS HAPPENS', b='DO THIS', c='')
    frows = fhead + ''.join(s['row'].format(a=esc(a), b=esc(b), c='') for a, b in C['fallbacks'])
    ftbl = s['table'].format(rows=frows, head=fhead, cap='')

    body = (s['head'].format(eyebrow='BEFORE YOU BOOK', title='Decide these first',
                             rh='BEFORE YOU BOOK', sf=esc(C['intro']))
            + tbl
            + s['h2'].format(t=esc(C['qheading'])) + s['p'].format(t=esc(C['qintro']))
            + ''.join(asks)
            + s['h2'].format(t=esc(C['tripheading'])) + s['p'].format(t=esc(C['tripintro']))
            + ''.join(trips)
            + '<div class="fbwrap">' + s['h2'].format(t=esc(C['fbheading']))
            + ftbl + '</div>')
    return s['sec'].format(id='beforeyoubook') + body + s['end']


TOCROW = {
    'rome':     '<div class="row"><span class="t"><a href="#beforeyoubook">Before you book — decide these first</a></span>'
                '<span class="lead"></span><span class="pg" data-ref="beforeyoubook">'
                '<a href="#beforeyoubook"></a></span></div>',
    'greece':   '<tr><td class="n">·</td><td><a href="#beforeyoubook">Before you book — decide these first</a></td>'
                '<td class="pg"><a href="#beforeyoubook"></a></td></tr>',
    'morocco':  '<tr><td class="n">·</td><td><a href="#beforeyoubook">Before you book — decide these first</a></td>'
                '<td class="pg"><a href="#beforeyoubook"></a></td></tr>',
    'thailand': '<tr><td class="n">·</td><td><a href="#beforeyoubook">Before you book — decide these first</a></td>'
                '<td class="pg"><a href="#beforeyoubook"></a></td></tr>',
    'turkey':   '<li><span class="t">BEFORE YOU BOOK</span><span class="d"></span>'
                '<span class="n"><a href="#beforeyoubook"></a></span></li>',
    'japan':    '<li><span class="tnum">BOOK</span><a href="#beforeyoubook">Before you book — decide these first</a>'
                '<span class="tdot"></span><span class="tpg"><a href="#beforeyoubook"></a></span></li>',
    # Barcelona's contents is a <nav> of bare anchors; the folio comes from the
    # stylesheet's own `.toc a::after` target-counter, so the row needs no cell.
    'barcelona': '<a href="#beforeyoubook"><span class="num">\u00b7</span>'
                 '<span class="t">Before you book \u2014 decide these first</span>'
                 '<span class="dots"></span></a>',
}
# the contents row goes immediately before this row, so it lands in reading order
BEFORE_ROW = {
    'rome':     r'<div class="part">The annex</div>',
    'greece':   r'<tr><td class="n">·</td><td><a href="#fs">',
    'morocco':  r'<tr><td class="n">·</td><td><a href="#fsheet">',
    'thailand': r'<tr><td class="n">·</td><td><a href="#fs">',
    'turkey':   r'<li><span class="t">FIELD SHEET</span>',
    'japan':    r'<li[^>]*><span class="tnum">BACK</span>',
    'barcelona': r'<a href="#fs">',
}


def add_toc_row(book, d):
    if 'href="#beforeyoubook"' in d:
        return d
    m = re.search(BEFORE_ROW[book], d)
    assert m, f'{book}: cannot find the contents row to sit before'
    return d[:m.start()] + TOCROW[book] + d[m.start():]


def main():
    book, build_dir = sys.argv[1], os.path.abspath(sys.argv[2])
    p = os.path.join(build_dir, 'dossier3.html')
    d = open(p, encoding='utf-8').read()
    if 'id="beforeyoubook"' in d:
        print(f'  {book}: already present'); return 0
    sec = build(book, CALLS[book])

    k = d.find('</style>')
    d = d[:k] + CSS + d[k:]

    # place it immediately before the field sheet — the last thing you read
    # before you start booking, and next to the numbers you will book against.
    # Japan's sheet is a separate document, so there it sits before the back
    # matter instead, which is the same position in the reader's hands.
    anchor = None
    for pat in (r'<section[^>]*id="fs"', r'<section[^>]*id="fsheet"',
                r'<section[^>]*id="field-sheet"',
                r'<section[^>]*id="what-goes-wrong-by-what-it-costs"'):
        m = re.search(pat, d)
        if m:
            anchor = m.start(); break
    assert anchor, 'nowhere obvious to place the spread'
    d = d[:anchor] + sec + '\n' + d[anchor:]

    # A chapter absent from the contents is a chapter with no bookmark and no
    # way in — exactly the navigation defect this edition set out to fix.
    d = add_toc_row(book, d)
    open(p, 'w', encoding='utf-8').write(d)
    print(f'  {book}: spread inserted ({len(CALLS[book])} calls, '
          f'{sum(len(q[1]) for q in BOOKS[book]["questions"])} questions, '
          f'{len(BOOKS[book]["trips"])} trips)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
