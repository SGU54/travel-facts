#!/usr/bin/env python3
"""audit-claims.py — the gate that was missing when livres-2026-09-26 shipped.

Every other gate in this tree reads geometry: how full a page is, whether a figure
is anchored, whether the rhythm breaks. None of them read what the book SAYS about
itself, so the 2026-09-26 edition shipped with all five gates green and:

  · Greece's contents page printing 0 for all 22 rows (target-counter was keyed to
    the <td>, and attr(href) resolves against the element the rule matches)
  · Greece's blurb promising "the twelve calls" over a list of nine
  · Turkey announcing "Four marks" above a list of three, and "five questions"
    above a contents page listing seven decisions
  · Turkey claiming the decisions are "one page each" when each runs three
  · Morocco announcing "Four symbols" above a list of five
  · ◆ meaning VOLATILE in three books and STABLE in Greece, and ● meaning
    ESTABLISHED in three books and "our arguable conclusion" in Thailand
  · ◆ printed as the running-footer ornament on every page of three books while
    also being the mark that means "re-check this before you travel"

Those are all mechanically checkable. This checks them.

Run:  python3 audit-claims.py <build-dir>
Exit: 0 clean, 1 if any check fails.
"""
import os, re, sys, html as _html

# ── the series mark key ─────────────────────────────────────────────────────────
# One meaning per glyph, fleet-wide. A book may use a SUBSET; it may not redefine.
SERIES = {'●': 'ESTABLISHED', '◇': 'OFFICIAL', '▲': 'SURVEYED',
          '◈': 'OUR CALL',    '◆': 'VOLATILE'}
GLYPHS = ''.join(SERIES)
WORDS = {w for w in SERIES.values()}
# words a book has historically used for a glyph that the series key renames
RETIRED = {'STRUCTURAL': '●', 'STABLE': None, 'DERIVED': None, 'MOVES': '◆'}

NUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
       'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
       'thirteen': 13, 'fourteen': 14, 'fifteen': 15}


def strip_tags(s):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def body_of(doc):
    """The document with its <style> blocks removed — prose only."""
    return re.sub(r'<style\b.*?</style>', ' ', doc, flags=re.S)


def css_of(doc):
    return ' '.join(re.findall(r'<style\b.*?</style>', doc, flags=re.S))


_ENT = {'●': ('&#9679;', '&#x25CF;'), '◇': ('&#9671;', '&#x25C7;'),
        '▲': ('&#9650;', '&#x25B2;'), '◈': ('&#9672;', '&#x25C8;'),
        '◆': ('&#9670;', '&#x25C6;')}


def _demoji(s):
    """Turn the five mark ENTITIES into their characters, and nothing else.

    Barcelona writes every mark as `&#9679;` rather than as the literal glyph, so
    the key matcher — which scans a character class — found no key at all and the
    mark-vocabulary check reported "cannot check" instead of checking. A blanket
    html.unescape() is not safe here: it would turn a book's `&lt;` into a real
    `<` and invent tags the matcher then skips over. Substitute only these five.
    """
    for ch, ents in _ENT.items():
        for e in ents:
            s = s.replace(e, ch)
    return s


def legend_marks(body):
    """(glyph, WORD) pairs from the book's own reading key.

    The five books write the key four different ways: a <p class="legend"|"bullet">
    per mark, a <li> per mark, a two-column table row in CAPS, and a two-column
    table row in sentence case (Thailand: "<b>Official.</b> A published rule…").
    All four put the glyph and its word adjacent, so match on that adjacency and
    normalise the word, rather than trying to recognise each container.
    """
    body = _demoji(body)
    found = []
    for m in re.finditer(rf'([{GLYPHS}])\s*(?:</span>|</td>|<span[^>]*>|<td[^>]*>|\s)*'
                         rf'(?:(<b>|<strong>))?\s*'
                         rf'([A-Za-z][A-Za-z]{{2,11}}(?:\s+[A-Za-z]{{3,5}})?)', body):
        raw, bold = m.group(3), m.group(2)
        # A key row either SHOUTS the word (four of the books), emboldens it
        # (Thailand now: "<b>Official.</b>"), or sits in a cell the book marks as
        # the key (Thailand before: `<td class="keymark">` + sentence case).
        # Requiring one of those keeps prose out: Morocco's "Anything marked ◆
        # moves." was otherwise read as a key row defining ◆ as MOVES.
        in_key = 'keymark' in body[max(0, m.start() - 90):m.start()] \
            or 'marklist' in body[max(0, m.start() - 400):m.start()]
        if not (raw.isupper() or bold or in_key):
            continue
        w = re.sub(r'\s+', ' ', raw).strip().rstrip('.').upper()
        cands = [w] + ([w.split()[0]] if ' ' in w else [])
        for c in cands:
            if c in WORDS or c in RETIRED:
                found.append((m.group(1), c)); break
    seen, out = set(), []
    for g, w in found:
        if (g, w) in seen:
            continue
        seen.add((g, w)); out.append((g, w))
    return out


def structural_counts(doc, body):
    """What the book demonstrably contains, with the signal each figure came from.

    Deliberately reports several signals rather than one number: Japan carries
    nine sections classed `decision` but lists eight numbered decisions, and no
    single signal is right for all five books. A count the gate cannot pin down
    is reported for a human, not failed.
    """
    sig = {}
    n = len(re.findall(r'<section[^>]*class="[^"]*\bdecision\b', body))
    if n:
        sig['sections classed decision'] = n
    ids = len(set(re.findall(r'id="d(\d\d)"', body)))
    if ids:
        sig['ids dNN'] = ids
    ordn = len(set(re.findall(r'(?:DECISION|Decision|decision)\s+0?(\d{1,2})\b', body)))
    if ordn:
        sig['numbered DECISION labels'] = ordn
    rom = set(re.findall(r'<span class="t">((?:I|V|X){1,5})\s*(?:&middot;|·)', body))
    if rom:
        sig['roman contents rows'] = len(rom)
    return sig


def check_marks(body, fails, warns):
    pairs = legend_marks(body)
    if not pairs:
        warns.append('no reading key found — cannot check mark vocabulary')
        return
    bad = [(g, w) for g, w in pairs if SERIES.get(g) != w]
    for g, w in bad:
        fails.append(f'mark vocabulary: {g} is labelled {w!r}; the series key says '
                     f'{SERIES.get(g, "(not a mark)")!r}')
    glyphs_used = sorted({g for g, _ in pairs}, key=GLYPHS.index)
    return glyphs_used


def check_declared_counts(body, doc, fails, warns):
    """FAIL only on the count this gate can settle; report the rest for review.

    The number of marks is settleable — the key is right there and lists them.
    "Seven decisions" is not: the phrase also occurs rhetorically ("four decisions
    land at once"), and the structural signals disagree with each other. Failing a
    build on a number the gate cannot actually resolve teaches people to ignore it.
    """
    text = strip_tags(body)
    n_key = len({g for g, _ in legend_marks(body)})
    for m in re.finditer(r'\b(' + '|'.join(NUM) + r')\s+(marks?|symbols?)\b', text, re.I):
        said = NUM[m.group(1).lower()]
        if n_key and said != n_key:
            ctx = text[max(0, m.start() - 70):m.end() + 30]
            fails.append(f'declared count: says "{m.group(0)}" but the reading key '
                         f'lists {n_key} — …{ctx}…')
    sig = structural_counts(doc, body)
    claims = [m.group(0) for m in re.finditer(
        r'\b(' + '|'.join(NUM) + r')\s+(decisions?|questions?|calls?|parts?)\b', text, re.I)]
    if claims:
        warns.append('counts stated in prose, for review: ' + ', '.join(
            f'"{c}"' for c in dict.fromkeys(claims)))
    if sig:
        warns.append('structural counts: ' + ' · '.join(f'{k}={v}' for k, v in sig.items()))
        if len(set(sig.values())) > 1:
            warns.append('the structural signals disagree — settle which is the '
                         'decision count before trusting any prose figure')



def check_figures(body, fails, warns):
    """Figure labels must be unique and in sequence, and no drawing twice.

    Rome shipped FIG. 3, 5, 9 and 10 each used for two different figures, a
    sequence running 1,3,2,3,4,5,8,9,11,6,7, no PL. 3 at all, and FOUR pairs of
    byte-identical artwork — including one chart drawn twice in the same chapter.
    A reader told to look at FIG. 5 has two places to look, and neither the
    layout gate (which checks image src) nor any other gate was watching labels.
    """
    import hashlib
    labels, arts = [], {}
    for m in re.finditer(r'<figure[^>]*class="[^"]*"[^>]*>(.*?)</figure>', body, re.S):
        seg = m.group(1)
        lm = re.search(r'<span class="fign">\s*([A-Z]{2,4}\.\s*\d+)\s*</span>', seg)
        if lm:
            labels.append(re.sub(r'\s+', ' ', lm.group(1)).strip())
        am = re.search(r'<svg.*?</svg>|<img[^>]*>', seg, re.S)
        if am:
            h = hashlib.md5(am.group(0).encode()).hexdigest()
            arts.setdefault(h, []).append(lm.group(1).strip() if lm else '(unlabelled)')
    if not labels:
        return
    dupes = sorted({l for l in labels if labels.count(l) > 1})
    for lab in dupes:
        fails.append(f'figure label "{lab}" is used {labels.count(lab)} times — '
                     f'a reference to it has more than one destination')
    # sequence, per series
    series = {}
    for lab in labels:
        k, num = lab.split('.')[0], int(re.sub(r'\D', '', lab))
        series.setdefault(k, []).append(num)
    for k, nums in series.items():
        want = set(range(1, max(nums) + 1))
        missing = sorted(want - set(nums))
        if missing:
            warns.append(f'{k}. numbering skips {missing} (runs to {max(nums)})')
        if nums != sorted(nums):
            warns.append(f'{k}. numbering is out of reading order: {nums}')
    repeated = {h: v for h, v in arts.items() if len(v) > 1}
    for h, v in repeated.items():
        warns.append(f'the same artwork is drawn {len(v)} times: {", ".join(v)}')


def check_ornaments(css, body, fails):
    """A provenance glyph may not also be decoration."""
    for m in re.finditer(r'@(bottom|top)-(left|center|right)\s*\{\s*content:\s*"([^"]*)"', css):
        lit = m.group(3)
        for esc in re.findall(r'\\([0-9a-fA-F]{2,6})', lit):
            ch = chr(int(esc, 16))
            if ch in SERIES:
                fails.append(f'@{m.group(1)}-{m.group(2)} prints {ch} '
                             f'({SERIES[ch]}) as furniture on every page')
        for ch in lit:
            if ch in SERIES:
                fails.append(f'@{m.group(1)}-{m.group(2)} prints {ch} '
                             f'({SERIES[ch]}) as furniture on every page')
    # a visible endmark carrying a mark glyph
    hidden = bool(re.search(r'\.endmark\s*\{[^}]*font-size:\s*0', css))
    ends = re.findall(r'class="endmark"[^>]*>([^<]{0,12})', body)
    if not hidden:
        for e in ends:
            for ch in _html.unescape(e):
                if ch in SERIES:
                    fails.append(f'.endmark renders {ch} ({SERIES[ch]}) as an '
                                 f'ornament in {len(ends)} places')
                    return


def check_contents(css, doc, pdf, fails, warns):
    # the static form of the Greece bug: the counter must sit on an element with href
    # The selector group must be BOUNDED. Unbounded, `[^{}]+` runs backwards
    # across whatever precedes each brace — in Rome that is 1.2 MB of base64
    # font data inside url(), and the scan never finished.
    for m in re.finditer(r'([^{}]{1,160})\{\s*content:\s*target-counter\(attr\(href[^)]*\)', css):
        sel = m.group(1).strip().split(',')[-1].strip()
        base = re.sub(r'::?(before|after)$', '', sel).strip()
        if not re.search(r'\ba$|\[href\]$', base):
            fails.append(f'contents counter is keyed to "{sel}" — attr(href) resolves '
                         f'against the matched element, so this prints 0')
        if 'url' in m.group(0):
            warns.append('target-counter uses attr(href url); this Paged.js wants attr(href)')
    if not (pdf and os.path.exists(pdf)):
        return
    try:
        import subprocess
        txt = subprocess.run(['pdftotext', '-layout', pdf, '-'],
                             capture_output=True, text=True, check=True).stdout
    except Exception as e:
        warns.append(f'cannot read the PDF text ({e})'); return
    pages = txt.split('\f')
    best, n = None, 0
    for p in pages:
        # Anchored and non-greedy at the START of the line, this backtracks over
        # every position of every long line — 44 pages of Rome took minutes. Only
        # the tail matters: whitespace then a folio then end of line.
        rows = re.findall(r'\s{2,}(\d{1,3})[ \t]*$', p, re.M)
        if len(rows) > n:
            best, n = rows, len(rows)
    if n >= 5:
        zeros = [r for r in best if r == '0']
        if len(zeros) >= 3:
            fails.append(f'contents page prints 0 for {len(zeros)} of {n} rows')
    else:
        warns.append('no contents page found in the PDF — a reference book needs one')
    # bookmarks
    try:
        import pypdf, warnings
        warnings.filterwarnings('ignore')
        r = pypdf.PdfReader(pdf)
        def count(o):
            t = 0
            for x in o:
                t += count(x) if isinstance(x, list) else 1
            return t
        if count(r.outline) == 0:
            fails.append(f'no PDF bookmarks — {len(r.pages)} pages with no outline')
    except Exception as e:
        warns.append(f'bookmark check skipped ({e})')


def main():
    build = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    html = None
    for name in ('dossier3.html', 'dossier.html'):
        if os.path.exists(os.path.join(build, name)):
            html = os.path.join(build, name); break
    if not html:
        print('  CLAIMS AUDIT — BLOCKED: no build HTML found'); return 1
    doc = open(html, encoding='utf-8').read()
    body, css = body_of(doc), css_of(doc)
    pdf = os.path.join(build, 'dossier.pdf')
    for cand in ('dossier-nav.pdf', 'dossier.pdf'):
        if os.path.exists(os.path.join(build, cand)):
            pdf = os.path.join(build, cand); break

    fails, warns = [], []
    glyphs = check_marks(body, fails, warns)
    check_declared_counts(body, doc, fails, warns)
    check_figures(body, fails, warns)
    check_ornaments(css, body, fails)
    check_contents(css, doc, pdf, fails, warns)

    print(f'  CLAIMS AUDIT — {os.path.basename(html)}'
          f'{" + " + os.path.basename(pdf) if os.path.exists(pdf) else ""}')
    print('  ' + '-' * 46)
    vocab_ok = not any('mark vocabulary' in f for f in fails)
    print(f'  {("✓" if vocab_ok else "✗") if glyphs else "·"} mark key         '
          f'{" ".join(g + " " + SERIES[g] for g in (glyphs or [])) or "—"}')
    for label, ok in (('declared counts', not any('declared count' in f for f in fails)),
                      ('figure labels', not any('figure label' in f for f in fails)),
                      ('ornaments', not any('furniture' in f or 'ornament' in f for f in fails)),
                      ('contents & outline', not any('contents' in f or 'bookmark' in f for f in fails))):
        print(f'  {"✓" if ok else "✗"} {label}')
    print('  ' + '-' * 46)
    for f in fails:
        print(f'  ✗ {f}')
    for w in warns:
        print(f'  · {w}')
    if fails:
        print('\n  INCONSISTENT — the book contradicts itself. Fix the ✗ rows.')
        return 1
    print('\n  CONSISTENT — what the book says about itself is true. Ships.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
