#!/usr/bin/env python3
"""
audit-layout.py — the layout intelligence gate.

The book gates measure whether pages are FULL. This one measures whether they
are LEGIBLE AS STRUCTURE: can a reader tell, without reading, what kind of
thing they are looking at? A dossier that passes audit-book and fails this one
is a well-packed wall of undifferentiated text.

Checks, on the built HTML (roles) and the rendered PDF (texture):

  1. ROLE COVERAGE   every decision carries an opener, a ledger and a verdict.
                     A decision without a visible verdict is the product's
                     core promise rendered invisible.
  2. ROLE DISTINCTION no two roles share a visual weight class (checked by the
                     CSS declaring distinct treatments for each role).
  3. TEXTURE RUN     no run of N+ consecutive pages with identical block
                     composition (all-prose pages are the failure mode).
  4. ANCHOR DENSITY  every spread (2pp) has at least one non-prose anchor:
                     an opener, ledger, verdict, figure or divider.
  5. FIGURE INTEGRITY every figure is claimed by exactly one chapter, and no
                     image is used twice (the substring-matcher bug).

Usage: python3 audit-layout.py <build-dir>
Exit 0 = CLEAN, 1 = flags.
"""
import re, sys, os, collections

BUILD = sys.argv[1] if len(sys.argv) > 1 else '.'
html = open(os.path.join(BUILD, 'dossier3.html'), encoding='utf-8').read()
css = html  # css is inlined
FLAGS = []

# ---------- 1. ROLE COVERAGE ----------
# Both the attribute quoting and the id scheme are per-book. This pattern
# demanded double quotes and ids of the form c01, so a book that writes
# <section class='dec chap' id='d02'> matched NOTHING: the gate reported
# "0 chapters, 0 decisions" on a 43-page book with nine of them, and every
# downstream check silently had no decisions to look at.
sections = re.findall(
    r'<section class=[\'"]([^\'"]*\bdec\b[^\'"]*)[\'"] id=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</section>',
    html, re.S)
# A decision is a section that reaches a verdict. Books mark them differently —
# some add a `decision` class, some number the id (c01 / d02) — so identify them
# by the thing that actually defines one rather than by a naming convention.
def _has_role(body, role):
    # the role's CLASS on any tag, either quoting. `ledger` is a <div> in one
    # book and a <table> in another; `opener` does not exist at all in a third,
    # which opens its chapters with an eyebrow and a standfirst instead.
    return re.search(r'class=[\'"][^\'"]*\b' + role + r'\b', body) is not None

ROLE_ALIASES = {
    # Rome opens every chapter with <div class="dnum">, a fourth name for the
    # same role; without the alias its nine decisions all read as openerless.
    # Barcelona opens with <div class="kicker"> over a <div class="standfirst">,
    # which is the same role again under two more names — all seven of its
    # decisions read as openerless until both were listed here.
    'opener':  ('opener', 'eyebrow', 'dnum', 'kicker', 'standfirst'),
    'ledger':  ('ledger',),
    'verdict': ('verdict',),
}
decisions = [(sid, body) for cls, sid, body in sections
             if 'decision' in cls or _has_role(body, 'verdict')]
missing = []
for sid, body in decisions:
    gaps = [role for role, names in ROLE_ALIASES.items()
            if not any(_has_role(body, n) for n in names)]
    if gaps:
        missing.append(f'{sid}: no {"/".join(gaps)}')
if missing:
    FLAGS.append('role coverage — ' + '; '.join(missing))

# ---------- 2. ROLE DISTINCTION ----------
# each role must declare its own visual treatment; if two roles resolve to the
# same rule block the reader cannot tell them apart.
roles = ['.opener', '.ledger', '.verdict', '.forks', 'figure', '.partdiv']
# Only a role the book ACTUALLY USES needs a declared treatment. This demanded
# styling for all six unconditionally, so a book with no part dividers — a
# perfectly ordinary shape — failed the gate for not styling an element it does
# not contain. Ask the document first.
def _role_used(role):
    if role == 'figure':
        return '<figure' in html
    return re.search(r'class=[\'"][^\'"]*\b' + re.escape(role[1:]) + r'\b', html) is not None

def _role_declared(role):
    if role == 'figure':
        # "figure" is a role, not a selector. A book may style it by tag, or by
        # the classes it puts ON its figures (.map, .photo, .plate …). Asking
        # only for a bare `figure{` rule flagged a book that styles every one of
        # its twenty figures through .map and .photo.
        classes = set()
        for attr in re.findall(r'<figure\s+class=[\'"]([^\'"]+)[\'"]', html):
            classes.update(attr.split())
        cands = ['figure'] + ['.' + c for c in classes]
        return any(c + '{' in css.replace(' ', '') or c + ' {' in css for c in cands)
    return role + '{' in css.replace(' ', '') or role + ' {' in css

undeclared = [r for r in roles if _role_used(r) and not _role_declared(r)]
if undeclared:
    FLAGS.append(f'role distinction — no styling declared for {undeclared}')

# The ledger vocabulary, taken from THIS book: every <th> column head and every
# .lcap caption inside a .ledger block. Letterspacing reaches pdftotext with gaps
# between the characters, so each probe matches with optional whitespace between
# letters — the same tolerance the FIG./PART patterns already use.
def _ledger_probes(h):
    # Scan the whole document, not per .ledger block: a non-greedy match from
    # <div class="ledger"> stops at the FIRST </div>, which is the .lcap caption's,
    # so the <th> heads it was after were never inside the captured text and the
    # probe list came back empty.
    out = set()
    for th in re.findall(r'<th[^>]*>(.*?)</th>', h, re.S):
        out.add(re.sub(r'<[^>]+>', '', th))
    # A column head is not always a <th>: one book writes its ledger heads as
    # <td class="led-h">, and has no <th> and no .lcap anywhere, so reading only
    # those two found nothing and every one of its fourteen ledgers went unseen.
    # Take any cell whose class marks it as a head.
    for td in re.findall(r'<td[^>]*class=[\'"][^\'"]*\b(?:led-h|lhead|head|lcap)\b[^\'"]*[\'"][^>]*>(.*?)</td>',
                         h, re.S):
        out.add(re.sub(r'<[^>]+>', '', td))
    for cap in re.findall(r'<div class=[\'"]lcap[\'"][^>]*>(.*?)</div>', h, re.S):
        out.add(re.sub(r'<[^>]+>', '', cap))
    probes = []
    for s in out:
        s = ' '.join(s.split()).upper()
        # a head this short is not distinctive — "CARD", "STEP", "MARK" occur in
        # ordinary prose and would mark every page as carrying a ledger
        if len(s) < 8:
            continue
        probes.append(r'\s*'.join(re.escape(c) for c in s if not c.isspace()))
    return probes

_LEDGER_PROBES = _ledger_probes(html)
_LEDGER_RE = re.compile('|'.join(_LEDGER_PROBES)) if _LEDGER_PROBES else None
# Length alone does not separate a column head from prose: heads like "SET PIECE",
# "APPROACH" and "WHAT HAPPENS" are ordinary English and matched 6 of this book's
# 69 body paragraphs, which would have inflated the anchored-page count and made
# the gate quietly permissive. What actually separates them is TYPOGRAPHY: a head
# sits alone on a short line, the same words in a sentence sit inside a long one.
# So match per line, and only on a line short enough to be a head.
_HEAD_LINE_MAX = 60

def _has_ledger(page_text):
    if not _LEDGER_RE:
        return False
    for line in page_text.upper().splitlines():
        line = line.strip()
        if line and len(line) <= _HEAD_LINE_MAX and _LEDGER_RE.search(line):
            return True
    return False

# ---------- 3 & 4. TEXTURE from the rendered PDF ----------
pdf = os.path.join(BUILD, 'dossier.pdf')
texture = []
if os.path.exists(pdf):
    try:
        from pypdf import PdfReader
        pages = PdfReader(pdf).pages
        # a page's texture = which anchors its text betrays
        for p in pages:
            t = (p.extract_text() or '')
            up = t.upper()
            marks = set()
            # A full-width photographic plate is an anchor and this never looked
            # for one: only FIG. n, THE CALL, PART x and DECISION n counted, so a
            # page carrying a plate and its caption read as bare prose. Both
            # patterns also tolerate letterspacing, which reaches pdftotext as
            # "F I G ." — the same trap audit-book.py's FIGLABEL already handles.
            if re.search(r'\bF\s*I\s*G\s*\.\s*\d', up):   marks.add('figure')
            if re.search(r'\bP\s*L\s*\.\s*[A-Z]\b', up):   marks.add('figure')
            # A photograph is an anchor whether or not its caption carries a
            # label. This check only ever read the TEXT layer, so a page holding
            # a full-column plate with an ordinary caption counted as bare prose
            # — six such spreads were reported here while every one of them had
            # an image on both pages. Ask the page what it actually draws.
            try:
                _res = p.get('/Resources')
                _xo = _res.get('/XObject').get_object() if _res and _res.get('/XObject') else {}
                if any(_xo[k].get_object().get('/Subtype') == '/Image' for k in _xo):
                    marks.add('figure')
            except Exception:
                pass
            if 'THE CALL' in up:                       marks.add('verdict')
            # letterspaced caps reach pdftotext as "PA R T O N E" — the same
            # trap audit-book.py's FIGLABEL already handles. Tolerate the gaps.
            if re.search(r'\bP\s*A\s*R\s*T\s+(?:O\s*N\s*E|T\s*W\s*O|'
                         r'T\s*H\s*R\s*E\s*E|F\s*O\s*U\s*R)\b', up):
                marks.add('divider')
            # The opener label is letterspaced in some books, so extraction gives
            # "D E C I S I O N  0 2" — the same trap FIG./PL./PART already
            # tolerate here. Without the tolerance a decision's own opening page
            # counted as bare prose.
            # Keep the NUMBER: the page text is upper-cased before matching, so a
            # bare "DECISION" also matches every prose use of the word — and in a
            # decision manual that is most pages. The number is what makes it an
            # opener label rather than a noun.
            if re.search(r'\bD\s*E\s*C\s*I\s*S\s*I\s*O\s*N\b[\s·.]*\d', up):
                marks.add('opener')
            # A ledger betrays itself by its column heads — but WHICH heads is a
            # property of the book, not of the format. This was a hardcoded list
            # from one destination (WHAT IT / WHO PAYS / THE MOVE …), so a book
            # whose columns read SITUATION / DO THIS had all 24 of its ledgers
            # counted as bare prose, and its densest page — three stacked ledgers —
            # was reported as a spread with no anchor at all. Read the actual
            # headings out of this book's own HTML instead (_LEDGER_PROBES).
            if _has_ledger(t):
                marks.add('ledger')
            texture.append(marks)

        # A chapter that is not a numbered decision still OPENS — with an
        # eyebrow, a display title and a standfirst, which is structure a reader
        # sees at a glance. Keying "opener" to the DECISION label alone missed
        # every one of those: in a book with 23 chapters of which 9 are
        # decisions, four chapter-opening pages were reported as bare prose.
        # Find them the book-agnostic way, by locating each section's own <h1>.
        for _cls, _sid, _body in sections:
            m = re.search(r'<h1[^>]*>(.*?)</h1>', _body, re.S)
            if not m:
                continue
            probe = ' '.join(re.sub(r'<[^>]+>', '', m.group(1)).split())[:34]
            if len(probe) < 10:
                continue
            # Escape each WORD and join with \s*. Escaping the whole probe first
            # does not work: re.escape also escapes spaces (they are significant
            # under re.VERBOSE), so substituting the space afterwards leaves the
            # backslash it added and the pattern becomes a literal "\s*" — which
            # matches nothing, ever.
            key = r'\s*'.join(re.escape(w) for w in probe.split())
            for pi, p in enumerate(pages):
                flat = ' '.join((p.extract_text() or '').split())
                if re.search(key, flat, re.I):
                    texture[pi].add('opener')
                    break
    except Exception as e:
        FLAGS.append(f'texture — could not read pdf ({e})')

if texture:
    # 3. longest run of pages with NO anchor at all
    run = best = 0
    for m in texture:
        run = run + 1 if not m else 0
        best = max(best, run)
    if best > 3:
        FLAGS.append(f'texture run — {best} consecutive pages with no structural anchor (want <=3)')

    # 4. anchor density per spread
    bare = []
    for i in range(0, len(texture) - 1, 2):
        if not (texture[i] | texture[i + 1]):
            bare.append(i + 1)
    if bare:
        FLAGS.append(f'anchor density — spreads with no anchor at all: {bare}')

# ---------- 5. STRANDED OPENER ----------
# Any chapter — decision or essay — that opens near the foot of a page with
# almost none of its body is a layout mistake the reader reads as an error.
# We locate each chapter by its real <h1> text, not by a decision-only pattern.
if os.path.exists(pdf):
    try:
        from pypdf import PdfReader as _R
        # Take the <h1> of every parsed section, not only of a <div class="opener">
        # — that markup is one book's; another opens its chapters with an eyebrow
        # and a standfirst and has no .opener anywhere, so this list came back
        # empty and the check silently had nothing to test.
        titles = []
        for _cls, _sid, _body in sections:
            _m = re.search(r'<h1[^>]*>(.*?)</h1>', _body, re.S)
            if _m:
                titles.append((_sid, re.sub(r'<[^>]+>', '', _m.group(1)).strip()))
        pages_txt = [(p.extract_text() or '') for p in _R(pdf).pages]
        # each probe keeps its section id: the id is how the chapter's real opening
        # page is looked up below, and a probes list that had dropped the short
        # titles could not be zipped back against `sections` without misaligning.
        probes = []
        for _sid, title in titles:
            probe = ' '.join(title.split())[:34]
            if len(probe) >= 8:
                # Same escaping trap as above: escape each word, join with \s+.
                probes.append((_sid, probe,
                               r'\s+'.join(re.escape(w) for w in probe.split())))
        # A CONTENTS page lists every chapter title, so it is the first page each
        # one appears on — and the "body" after a title there is the next line of
        # the table. Taking that first hit reported every chapter in the book as a
        # stranded opener. A page carrying three or more titles is a listing, not
        # an opening; skip it.
        flats = [' '.join(t.split()) for t in pages_txt]
        listing = {i for i, f in enumerate(flats)
                   if sum(1 for _, _, k in probes if re.search(k, f)) >= 3}

        # WHERE A CHAPTER OPENS IS NOT A TEXT SEARCH. Taking the first page whose
        # text contains the title, then breaking, measures whatever page happens
        # to MENTION the chapter first. On Barcelona that was a cross-reference in
        # the middle of another chapter — "the airport ticket connects to Day Zero"
        # — and "(The Plan)" in a failure-mode row, so two continuation pages
        # carrying 402 and 215 words were both reported as chapters opening with
        # 7 and 1. The PDF already knows: the contents links to every chapter, so
        # every chapter id is a named destination pointing at its real first page.
        # Trust that, and fall back to the text scan only where there is none.
        dest_page = {}
        try:
            _pages = _R(pdf).pages
            _idx = {_p.indirect_reference.idnum: _i for _i, _p in enumerate(_pages)}
            for _name, _d in (_R(pdf).named_destinations or {}).items():
                try:
                    _n = _idx.get(_d.page.idnum)
                    if _n is not None:
                        dest_page[_name.lstrip('/')] = _n + 1
                except Exception:
                    continue
        except Exception:
            dest_page = {}

        stranded = []
        for _sid, probe, key in probes:
            pi = dest_page.get(_sid)
            if pi:
                flat = flats[pi - 1]
                m = re.search(key, flat)
                # the destination is authoritative even if the title does not
                # extract cleanly (letterspaced display faces often do not)
                tail = flat[m.end():] if m else flat
            else:
                # PAGE 1 IS THE COVER, on either path. Rome's title chapter is a
                # real <section>, but Chromium writes a destination only for an
                # anchor something links to and nothing links to that one — so it
                # falls here, matches its own title on the cover, and 42 words of
                # title and subtitle read as a chapter opening with no body. The
                # guard has to sit on both branches, not just the dest lookup.
                for pi, flat in enumerate(flats, 1):
                    if pi == 1 or (pi - 1) in listing:
                        continue
                    m = re.search(key, flat)
                    if m:
                        tail = flat[m.end():]
                        break
                else:
                    continue
            if pi == 1:
                continue
            tail = re.sub(r'(DECISION \d+ OF \d+|MOROCCO FOR AMERICANS).*$', '', tail)
            if len(tail.split()) < 45:
                stranded.append(f'p{pi} "{probe[:26]}…" ({len(tail.split())}w)')
        if stranded:
            FLAGS.append('stranded opener — chapter opens with almost no body: '
                         + '; '.join(stranded))
    except Exception as e:
        FLAGS.append(f'stranded-opener check failed ({e})')

# ---------- 6. FIGURE INTEGRITY ----------
# The <img> need not follow the <figure> tag immediately: a plate is emitted as
# <figure class="plate" id="plate-A04"><img src=...>. Requiring `"><img` counted
# ZERO figures in a book holding eight, so both the duplicate-image check and the
# reported figure count were silently inert.
imgs = re.findall(r'<figure class="[^"]*"[^>]*>\s*<img src="([^"]+)"', html)
dupes = [k for k, n in collections.Counter(imgs).items() if n > 1]
if dupes:
    FLAGS.append(f'figure integrity — image used more than once: {dupes}')
# a figure must sit inside a chapter, never loose in the flow
loose = len(re.findall(r'</section>\s*<figure', html))
if loose:
    FLAGS.append(f'figure integrity — {loose} figure(s) outside any chapter')

# ---------- report ----------
print(f'LAYOUT AUDIT — {len(sections)} chapters, {len(decisions)} decisions, '
      f'{len(imgs)} figures, {len(texture)} pages')
if texture:
    anchored = sum(1 for m in texture if m)
    print(f'  anchored pages {anchored}/{len(texture)} · '
          f'roles seen: {sorted(set().union(*texture)) if any(texture) else "none"}')
if FLAGS:
    print('  FLAGS:')
    for f in FLAGS:
        print('   ⚠', f)
    print('\nLAYOUT NOT LEGIBLE — fix before render.')
    sys.exit(1)
print('\nCLEAN — structure reads at a glance. Ships.')
sys.exit(0)
