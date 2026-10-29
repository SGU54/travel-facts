# -*- coding: utf-8 -*-
"""pack-edition.py — the maquettiste's own two-column pagination.

Paged.js cannot paginate CSS multicol (content longer than a page spills into extra
columns instead of onto the next page — seen on Rome's first Édition render), so the
two-column body of Clàudia Ferrer's hand is packed here, line by line, before Paged.js
sees it:

  1. MEASURE  every paragraph of the composed book is rendered once, at column width,
              with each word in a span; the words' tops give the line breaks. Blocks
              (sidebars, forks, notes, cards) are measured whole at column width;
              figures, plates and tables at the full measure.
  2. PACK     each chapter flows into pages of two 314px columns under an 892px body:
              lines pour into column 1, then column 2, then a new page; a paragraph
              splits at a line boundary (never leaving fewer than two lines on either
              side, three after a drop cap); a block never splits; a full-measure item
              closes the open columns — which are then BALANCED — and takes the measure.
  3. EMIT     explicit pages (.pg) of explicit columns (.row2 > .col), which Paged.js
              only has to stack. No multicol remains.

Reads dossier3.html (compose-edition.py); writes dossier3.paged.html + _pack.json.
Hyphenation is off in this hand (a split word cannot be re-split the browser's way).
"""
import re, json, os, sys
from bs4 import BeautifulSoup, NavigableString, Tag
from playwright.sync_api import sync_playwright

BUILD = os.path.dirname(os.path.abspath(__file__)); os.chdir(BUILD)
SRC = 'dossier3.html'; OUT = 'dossier3.paged.html'
H_BODY = 892 - 14; LINE = 16; P_GAP = 9; COL = 314; MEASURE = 652   # 14px of safety against rounding
doc = open(SRC, encoding='utf-8').read()
soup = BeautifulSoup(doc, 'lxml')
css = soup.find('style').string

# ── 1 · collect the flow of every chapter ──────────────────────────────────────
def tokens(p_html):
    """Words of a paragraph's inner HTML, inline tags kept whole inside a token."""
    toks = []; buf = ''; depth = 0
    for part in re.split(r'(<[^>]+>|\s+)', p_html):
        if part is None or part == '': continue
        if part.startswith('<'):
            buf += part
            if part.startswith('</'): depth -= 1
            elif not part.endswith('/>'): depth += 1
        elif part.isspace():
            if depth == 0 and buf: toks.append(buf); buf = ''
            elif depth: buf += ' '
        else: buf += part
    if buf: toks.append(buf)
    return toks

chapters = []
for sec in soup.find_all('section', class_='chap'):
    ch = {'id': sec.get('id'), 'cls': ' '.join(sec.get('class', [])), 'parts': []}
    for el in sec.children:
        if isinstance(el, NavigableString): continue
        cls = el.get('class', []) or []
        if 'pg' in cls or 'cover' in cls or 'fs' in cls:
            ch['parts'].append({'k': 'fixed', 'html': str(el)}); continue
        if 'body2' in cls:
            for c in el.children:
                if isinstance(c, NavigableString): continue
                if c.name == 'p': ch['parts'].append({'k': 'p', 'html': c.decode_contents(), 'cls': ' '.join(c.get('class', []) or [])})
                else: ch['parts'].append({'k': 'block', 'html': str(c)})
            continue
        if cls and any(x in cls for x in ('cards', 'asks', 'list', 'wont', 'fb', 'tier')):
            for c in el.children:
                if isinstance(c, NavigableString): continue
                if c.name == 'div' and 'cards' in (c.get('class') or []):
                    for cc in c.children:
                        if isinstance(cc, Tag): ch['parts'].append({'k': 'block', 'html': str(cc)})
                else: ch['parts'].append({'k': 'block', 'html': str(c)})
            continue
        ch['parts'].append({'k': 'wide', 'html': str(el)})
    chapters.append(ch)

# ── 2 · measure ────────────────────────────────────────────────────────────────
mhtml = ['<!doctype html><html><head><meta charset="utf-8"><style>', css,
         f'.mcol{{width:{COL}px}} .mwide{{width:{MEASURE}px}} .m{{position:absolute;left:0;top:0;visibility:hidden;padding:0.5px 0}} .w{{display:inline}} body{{margin:0}} p{{hyphens:manual !important}}',
         '</style></head><body>']
idx = []
for ci, ch in enumerate(chapters):
    for pi, part in enumerate(ch['parts']):
        if part['k'] == 'p':
            toks = tokens(part['html']); part['toks'] = toks
            inner = ' '.join(f'<span class="w" data-i="{i}">{t}</span>' for i, t in enumerate(toks))
            mhtml.append(f'<div class="m mcol" id="m-{ci}-{pi}"><p class="{part["cls"]}">{inner}</p></div>')
        elif part['k'] == 'block': mhtml.append(f'<div class="m mcol" id="m-{ci}-{pi}">{part["html"]}</div>')
        elif part['k'] == 'wide': mhtml.append(f'<div class="m mwide" id="m-{ci}-{pi}">{part["html"]}</div>')
        else: continue
        idx.append((ci, pi, part['k']))
mhtml.append('</body></html>')
open('_measure.html', 'w', encoding='utf-8').write(re.sub(r'<img src="[^"]*"', '<img', ''.join(mhtml)))   # heights come from CSS; no photo needs loading
with sync_playwright() as pw:
    b = pw.chromium.launch(args=['--no-sandbox']); pg = b.new_page(viewport={'width': 900, 'height': 1200})
    pg.goto('file://' + os.path.join(BUILD, '_measure.html'), wait_until='domcontentloaded', timeout=180000)
    pg.evaluate('() => document.fonts.ready'); pg.wait_for_timeout(300)
    res = pg.evaluate("""() => { const out = {}; document.querySelectorAll('.m').forEach(m => {
        const p = m.querySelector('p'); const r = {h: Math.round(m.getBoundingClientRect().height - 1)};
        if (p && m.querySelector('.w')) { const tops = []; let last = null;
          m.querySelectorAll('.w').forEach((w, i) => { const rc = w.getClientRects()[0]; const t = rc ? Math.round(rc.top) : null; if (t !== null && (last === null || t > last + 4)) { tops.push(i); last = t; } });
          r.starts = tops; r.ph = Math.round(p.getBoundingClientRect().height); }
        out[m.id] = r; }); return out; }""")
    b.close()
for ci, pi, k in idx:
    r = res[f'm-{ci}-{pi}']; part = chapters[ci]['parts'][pi]
    if k == 'p': part['starts'] = r.get('starts', [0]); part['nlines'] = len(part['starts']); part['h'] = r.get('ph', LINE)
    else: part['h'] = r['h']
json.dump([{k: v for k, v in p.items() if k != 'html'} for ch in chapters for p in ch['parts'] if p['k'] != 'fixed'], open('_pack.json', 'w'))

# ── 3 · pack ───────────────────────────────────────────────────────────────────
def p_part_html(part, a, b, first, last):
    toks = part['toks']; s, e = part['starts'][a], (part['starts'][b] if b < part['nlines'] else len(toks))
    cls = (part['cls'] if first else '') + (' cont' if not first else '') + ('' if last else ' frag')
    return f'<p class="{cls.strip()}">{" ".join(toks[s:e])}</p>'

def part_units(part):
    """A paragraph as splittable line units; a block as one unit."""
    if part['k'] == 'p':
        n = part['nlines']; return [{'part': part, 'line': i, 'h': LINE + (P_GAP if i == n - 1 else 0)} for i in range(n)]
    return [{'part': part, 'h': part['h'] + 8}]

MIN_LINES = 2
def pour(units, cap1, cap2):
    """Pour units into two columns of the given capacities; returns (col1, col2, rest).
    A paragraph may break between lines but never leaves < MIN_LINES on a side (3 after a drop cap)."""
    cols = [[], []]; caps = [cap1, cap2]; rest = list(units); c = 0
    while rest and c < 2:
        u = rest[0]
        if u['h'] <= caps[c] or (caps[c] >= [cap1, cap2][c] - 0.5 and 'line' not in u):   # a block taller than an empty column is placed anyway
            cols[c].append(rest.pop(0)); caps[c] -= u['h']; continue
        # does not fit: a block → next column; a line → the paragraph splits here if the orphan/widow rule allows
        if 'line' not in u:
            # a block that no longer fits column 2 but fits under column 1 sits there (a note at the foot of a column)
            if c == 1 and u['h'] <= caps[0]:
                cols[0].append(rest.pop(0)); caps[0] -= u['h']; continue
            c += 1; continue
        part = u['part']; placed = [x for x in cols[c] if x['part'] is part]
        minfirst = 3 if 'lede' in part.get('cls', '') else MIN_LINES
        if len(placed) < minfirst:                        # too few lines here: move them all to the next column
            for x in placed: cols[c].remove(x); caps[c] += x['h']
            rest = placed + rest
        c += 1
    return cols[0], cols[1], rest

def render_cols(col):
    out = []; i = 0
    while i < len(col):
        u = col[i]
        if 'line' not in u: out.append(u['part']['html']); i += 1; continue
        part = u['part']; a = u['line']; j = i
        while j + 1 < len(col) and col[j + 1]['part'] is part: j += 1
        b = col[j]['line'] + 1
        out.append(p_part_html(part, a, b, a == 0, b == part['nlines'])); i = j + 1
    return ''.join(out)

def balance(units):
    """Split a unit list into two columns of near-equal height, at an allowed boundary."""
    total = sum(u['h'] for u in units); best = None
    acc = 0
    for i in range(1, len(units)):
        acc += units[i - 1]['h']
        u, v = units[i - 1], units[i]
        if 'line' in u and 'line' in v and u['part'] is v['part']:
            k = u['line'] + 1; n = u['part']['nlines']; minfirst = 3 if 'lede' in u['part'].get('cls', '') else MIN_LINES
            if k < minfirst or n - k < MIN_LINES: continue
        d = abs(acc - (total - acc))
        if best is None or d < best[0]: best = (d, i)
    i = best[1] if best else len(units)
    return units[:i], units[i:]

pages_html = []
def pack_chapter(ch, HB):
    """Pack one chapter under a body height HB; returns (pages, last_fill, n_flow_pages)."""
    sec_pages = []; st = {'cur': [], 'R': HB, 'open': [], 'cap': None, 'nflow': 0, 'last_fill': 1.0}
    def close_row(balanced=True):
        if not st['open']: return
        if balanced: c1, c2 = balance(st['open'])
        else: c1, c2, _ = pour(st['open'], st['cap'], st['cap'])
        h = max(sum(u['h'] for u in c1), sum(u['h'] for u in c2))
        st['cur'].append(f'<div class="row2"><div class="col">{render_cols(c1)}</div><div class="col">{render_cols(c2)}</div></div>')
        st['R'] -= h + 6; st['open'] = []; st['cap'] = None
    def new_page():
        if st['cur']:
            sec_pages.append('<div class="pg">' + ''.join(st['cur']) + '</div>'); st['nflow'] += 1; st['last_fill'] = 1 - st['R'] / HB
        st['cur'] = []; st['R'] = HB
    closers = [p for p in ch['parts'] if p['k'] == 'wide' and 'class="plate tall"' in p['html']]
    for part in ch['parts']:
        if part in closers: continue
        if part['k'] == 'fixed':
            close_row(); new_page(); sec_pages.append(part['html']); st['cur'] = []; st['R'] = 0; continue
        if part['k'] == 'wide':
            close_row(); h = part['h'] + 10
            lead_in = part['html'].lstrip().startswith(('<h2', '<p class="t"'))
            if h > st['R'] or (lead_in and st['R'] - h < 160): new_page()
            st['cur'].append(part['html']); st['R'] -= h; continue
        units = part_units(part)
        if st['cap'] is None:
            if st['R'] < 3 * LINE: new_page()
            st['cap'] = st['R']
        st['open'] += units
        c1, c2, rest = pour(st['open'], st['cap'], st['cap'])
        while rest:
            st['cur'].append(f'<div class="row2"><div class="col">{render_cols(c1)}</div><div class="col">{render_cols(c2)}</div></div>')
            new_page(); st['open'] = rest; st['cap'] = st['R']
            c1, c2, rest = pour(st['open'], st['cap'], st['cap'])
    close_row()
    for cp in closers:
        room = st['R'] - 24
        if room >= 170:
            h = min(420, room - 30); st['cur'].append(cp['html'].replace('<img ', f'<img style="height:{h}px" ', 1)); st['R'] -= h + 40
        else:
            new_page(); st['cur'].append(cp['html'].replace('<img ', '<img style="height:760px" ', 1)); st['R'] -= 800
    new_page()
    return sec_pages, st['last_fill'], st['nflow']

for ch in chapters:
    HB = H_BODY; sec_pages, last_fill, nflow = pack_chapter(ch, HB)
    # feather: a chapter whose last page would be a stub is repacked under a lower body height,
    # so the remainder spreads over its pages instead of dribbling onto the last one
    tries = 0
    while last_fill < 0.40 and nflow >= 2 and tries < 8:
        HB = int(HB - max(40, (0.62 - last_fill) * H_BODY / nflow)); tries += 1
        sec_pages, last_fill, nflow = pack_chapter(ch, HB)
    pages_html.append(f'<section class="{ch["cls"]}" id="{ch["id"]}">' + ''.join(sec_pages) + '</section>')

extra_css = '''
.row2{ display:grid; grid-template-columns:314px 314px; column-gap:24px; align-items:start; margin-bottom:6px; }
.row2 .col > *:last-child{ margin-bottom:0; }
.row2 .col > p{ margin:0 0 9px; text-align:justify; } .row2 .col > p.cont{ text-indent:0; } .row2 .col > p.frag{ text-align-last:justify; margin-bottom:0; }
p{ hyphens:manual; }
figure.plate img[style]{ object-position:50% 50%; }
.body2{ column-count:1; }
'''
head = doc.split('<body>', 1)[0].replace('</style>', extra_css + '</style>')
open(OUT, 'w', encoding='utf-8').write(head + '<body>\n' + '\n'.join(pages_html) + '\n</body></html>')
npages = sum(p.count('<div class="pg"') + p.count('class="pg ') for p in pages_html)
print(f'packed: {len(chapters)} chapters -> {OUT}; ~{npages} pages of flow')
