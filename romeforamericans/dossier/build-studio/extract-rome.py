# -*- coding: utf-8 -*-
"""extract-rome.py — the shipped *Rome, Solved.* (64 pp) as structured chapters.

No source for the shipped edition exists on this machine, so the book is read back
from its own PDF: every text line with its face and size, every image with its page
and box, every vector figure as an SVG carrying its paths and its text labels at
their printed positions. Roles are inferred from the book's own typographic contract
(the styles catalogued on 2026-10-25):

  kicker      IBM Plex Mono 6.0, letterspaced, at the top of a chapter page
  h1          IM Fell English 29.2
  standfirst  IM Fell English Italic 12.8
  body        Sorts Mill Goudy 10.0 (10.5 for the drop-cap paragraph)
  marks       Menlo 6.4 glyphs ●◇▲◆ inside body lines
  ledger      Plex 6.4 caption · Plex Medium 6.4 heads · Fell 9.8 rows · Plex 8.2 values
  the call    Plex 6.0 "THE CALL" · Fell 9.6 lead · Goudy 9.6 rest
  forks       Type3 6.0 "FOLLOW THIS IF" / "OVERRULE IT IF" · Goudy 8.7 items, "—" bullets
  note        Goudy 8.5 · xref Plex 7.5 "→ …"
  captions    Plex 6.0 "FIG. n ·" / "PL. n ·" / band captions under images
  sections    Plex 6.8 labels (checklist), Plex Medium 8.2 letterspaced (failure tiers),
              Fell 14.2 (place cards), Fell 9.3 + Goudy 9.3 (failure items), Fell 9.0 +
              Plex 7.9 (wallet lines), Goudy 9.0/9.3/9.5 list items

Output: rome-book.json (chapters → blocks), _rome-preview.md (to read), figures/*.svg,
img/ (the book's photographs by page).
"""
import pymupdf, re, json, os, html as H
from collections import defaultdict

PDF = '/Users/sg54/travel-sites/_etsy/rome/files/rome-solved.pdf'
OUT = os.path.dirname(os.path.abspath(__file__)); os.chdir(OUT)
os.makedirs('figures', exist_ok=True); os.makedirs('img', exist_ok=True)
doc = pymupdf.open(PDF)
MARKS = {'●', '◇', '▲', '◆', '◈', '○'}

def unspace(t):
    """'D E C I S I O N 0 1 · B A S E' -> 'DECISION 01 · BASE' (letterspaced caps extract with spaces)."""
    if re.fullmatch(r'(?:\S ?)+', t) and ' ' in t and all(len(w) <= 1 for w in t.replace('  ', '|').split(' ') if w != ''):
        return t.replace('  ', '\x00').replace(' ', '').replace('\x00', ' ')
    return t

def face(s):
    f = s['font'].split('+')[-1]
    if 'fell' in f.lower(): return 'fell-it' if 'Italic' in f else 'fell'
    if 'Goudy' in f: return 'goudy-it' if 'Italic' in f else 'goudy'
    if 'Plex' in f: return 'plex-md' if 'Medium' in f else 'plex'
    if 'Menlo' in f: return 'mark'
    if 'Courier' in f: return 'furniture'
    if 'Type3' in f: return 't3'
    return f

# ── 1 · every line of every page, with role hints ──────────────────────────────
pages = []
for pno, p in enumerate(doc, 1):
    lines = []; images = []
    for b in p.get_text('dict')['blocks']:
        if b.get('type') == 1:
            images.append({'bbox': [round(v) for v in b['bbox']]}); continue
        for l in b.get('lines', []):
            spans = [s for s in l['spans'] if s['text'].strip() or s['text'] == ' ']
            if not spans or not ''.join(s['text'] for s in spans).strip(): continue
            # inline runs: body text with mark glyphs → one line, marks wrapped
            runs = []
            for s in spans:
                fc = face(s); t = s['text']
                if fc == 'mark' and t.strip() in MARKS: runs.append(('mk', t.strip()))
                elif fc == 't3' and t.strip() in ('→', '—'): runs.append(('txt', t))
                else: runs.append(('txt', t))
            s0 = max(spans, key=lambda s: len(s['text'].strip()))
            txt = ''.join((f'<i class="mk">{t}</i>' if k == 'mk' else H.escape(t, quote=False)) for k, t in runs)
            lines.append({'face': face(s0), 'size': round(s0['size'], 1), 'x': round(l['bbox'][0]), 'y': round(l['bbox'][1]),
                          'x1': round(l['bbox'][2]), 'y1': round(l['bbox'][3]), 'text': txt.strip(), 'raw': ''.join(s['text'] for s in spans).strip(),
                          'runs': [(face(s), round(s['size'], 1), s['text']) for s in spans]})
    lines.sort(key=lambda l: (l['y'], l['x']))
    drs = p.get_drawings()
    rules = sorted({round(dr['rect'].y0) for dr in drs if dr['rect'].height < 2 and dr['rect'].width > 100 and 70 < dr['rect'].y0 < 720})
    pages.append({'page': pno, 'lines': lines, 'images': images, 'drawings': drs, 'rules': rules})

# ── 2 · photographs, by page ───────────────────────────────────────────────────
seen = {}
for pno, p in enumerate(doc, 1):
    for k, im in enumerate(p.get_images(full=True)):
        if im[0] in seen: continue
        info = doc.extract_image(im[0]); fn = f'img/p{pno:02d}-{k}.{info["ext"]}'
        open(fn, 'wb').write(info['image']); seen[im[0]] = fn
img_by_page = defaultdict(list)   # per page: (bbox, file), in the order the images are placed
for pno, p in enumerate(doc, 1):
    for inf in p.get_image_info(xrefs=True):
        if inf['xref'] in seen: img_by_page[pno].append((pymupdf.Rect(inf['bbox']), seen[inf['xref']]))

# ── 3 · figures: a vector region above a "FIG. n ·" caption → SVG ──────────────
def colour(c):
    if c is None: return 'none'
    return '#%02X%02X%02X' % tuple(int(round(v * 255)) for v in c[:3])

def fig_svg(pg, y0, y1, x0=40, x1=575):
    """Drawings and text within the band y0..y1 of the page, as one SVG in page points."""
    # crop to the content: the drawings' and labels' vertical extent, with a little air
    ys = [v for dr in pg['drawings'] for v in (dr['rect'].y0, dr['rect'].y1) if y0 - 6 <= (dr['rect'].y0 + dr['rect'].y1) / 2 <= y1 + 6 and not (dr['rect'].width > 500 and dr['rect'].height > 700) and dr['rect'].width < 480]
    ys += [v for l in pg['lines'] if y0 <= l['y'] and l['y1'] <= y1 and l['face'] != 'furniture' and not (l['face'] == 'plex' and l['size'] == 6.0 and l['raw'].startswith(('FIG.', 'PL.'))) for v in (l['y'], l['y1'])]
    if ys: y0, y1 = max(y0, min(ys) - 10), min(y1, max(ys) + 10)
    W, Hh = x1 - x0, y1 - y0
    parts = [f'<svg viewBox="0 0 {W:.0f} {Hh:.0f}" xmlns="http://www.w3.org/2000/svg" data-figure="1">']
    for dr in pg['drawings']:
        r = dr['rect']
        if r.y1 < y0 or r.y0 > y1 or (r.width > 500 and r.height > 700): continue   # the page ground
        # keep a drawing whose vertical centre sits in the band (a ring's box may poke past the band's edges)
        if not (y0 - 6 <= (r.y0 + r.y1) / 2 <= y1 + 6): continue
        fill = colour(dr.get('fill')) if dr.get('fill') is not None else 'none'
        stroke = colour(dr.get('color')) if dr.get('color') is not None else 'none'
        sw = dr.get('width') or 0
        op = dr.get('fill_opacity', 1) if dr.get('fill') is not None else 1
        dash = dr.get('dashes')
        dash_attr = ''
        if dash and dash not in ('[] 0', '[]'):
            nums = re.findall(r'[\d.]+', dash.split(']')[0]); dash_attr = f' stroke-dasharray="{" ".join(nums)}"' if nums else ''
        d = []; cur = None
        def P(pt): return f'{pt.x-x0:.1f},{pt.y-y0:.1f}'
        def near(a, b): return a is not None and abs(a.x - b.x) < 0.05 and abs(a.y - b.y) < 0.05
        for it in dr['items']:
            k = it[0]
            if k == 'l':
                if not near(cur, it[1]): d.append('M' + P(it[1]))
                d.append('L' + P(it[2])); cur = it[2]
            elif k == 're':
                rr = it[1]; d.append(f'M{rr.x0-x0:.1f},{rr.y0-y0:.1f} h{rr.width:.1f} v{rr.height:.1f} h{-rr.width:.1f} Z'); cur = None
            elif k == 'qu':
                q = it[1]; d.append(f'M{P(q.ul)} L{P(q.ur)} L{P(q.lr)} L{P(q.ll)} Z'); cur = None
            elif k == 'c':
                p1, p2, p3, p4 = it[1:5]
                if not near(cur, p1): d.append('M' + P(p1))
                d.append(f'C{P(p2)} {P(p3)} {P(p4)}'); cur = p4
        if not d: continue
        if dr.get('closePath'): d.append('Z')
        parts.append(f'<path d="{" ".join(d)}" fill="{fill}" fill-opacity="{op:.2f}" stroke="{stroke}" stroke-width="{sw:.2f}"{dash_attr} data-role="{"fill" if fill != "none" and stroke == "none" else "line"}"/>')
    for l in pg['lines']:
        if l['y'] < y0 or l['y1'] > y1 or l['face'] == 'furniture': continue
        if l['face'] == 'plex' and l['size'] == 6.0 and l['raw'].startswith(('FIG.', 'PL.')): continue
        cls = 'lab' if l['face'].startswith('goudy') else ('mono' if l['face'].startswith('plex') else 'lab')
        it = ' font-style="italic"' if l['face'].endswith('-it') else ''
        wt = ' font-weight="600"' if l['face'] == 'plex-md' or l['size'] >= 9 else ''
        parts.append(f'<text x="{l["x"]-x0:.1f}" y="{l["y1"]-y0-1.5:.1f}" font-size="{l["size"]:.1f}" class="{cls}"{it}{wt}>{H.escape(l["raw"], quote=False)}</text>')
    parts.append('</svg>')
    return '\n'.join(parts)

# ── 4 · chapters: a kicker at the top of a page opens one ──────────────────────
def is_kicker(l): return l['face'] == 'plex' and l['size'] == 6.0 and l['y'] < 120 and l['x'] < 80 and ' ' in l['raw'] and len(l['raw']) > 6 and not l['raw'].startswith(('FIG', 'PL'))
chapters = []; cur = None
for pg in pages:
    pno = pg['page']
    if pno == 1: chapters.append({'id': 'cover', 'kicker': '', 'title': 'Rome, Solved.', 'pages': [1], 'blocks': []}); continue
    lines = pg['lines']
    kick = next((l for l in lines if is_kicker(l)), None)
    h1s = [l for l in lines if l['face'] == 'fell' and l['size'] in (29.2, 33.0)]
    if h1s and (kick or h1s[0]['size'] == 33.0):
        title = ' '.join(l['raw'] for l in h1s if l['y'] < h1s[0]['y'] + 80)
        flat = kick['raw'].replace(' ', '') if kick else 'INTRO'
        m = re.match(r'DECISION(\d\d)·(.+)', flat)
        if m: kicker = f'Decision {m.group(1)} · {m.group(2).title()}'; cid = f'd{m.group(1)}'
        else:
            kicker = {'CONTENTS': 'Contents', 'CHAPTER': 'Chapter', 'BEFOREYOUBOOK': 'Before you book', 'INTRO': ''}.get(flat, flat.title())
            cid = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:28]
        cur = {'id': cid, 'kicker': kicker, 'title': title, 'pages': [pno], 'blocks': [], 'rules': {}}; chapters.append(cur)
        if pno == 3: cur['id'] = 'intro'
    elif pno == 60:
        cur = {'id': 'after-the-last-tab', 'kicker': 'Chapter', 'title': 'After the last tab', 'pages': [pno], 'blocks': []}; chapters.append(cur)
    elif cur: cur['pages'].append(pno)
    else: continue
    cur.setdefault('rules', {})[pno] = pg['rules']
    # ── blocks on this page, in reading order (two-column fork panels are re-joined) ──
    skip_y = set()
    # images with their captions
    for im in pg['images']:
        cap = next((l for l in lines if l['face'] == 'plex' and l['size'] == 6.0 and l['y'] >= im['bbox'][3] - 2 and l['y'] <= im['bbox'][3] + 16 and not is_kicker(l)), None)
        caps = [cap] + ([m for m in lines if cap and m['face'] == 'plex' and m['size'] == 6.0 and cap['y'] < m['y'] <= cap['y'] + 14 and m['x'] < 80] if cap else [])
        # the file whose placed box matches this image block
        cands = img_by_page[pno]; src = None
        if cands:
            bb = pymupdf.Rect(im['bbox']); cy = (bb.y0 + bb.y1) / 2
            best = min(cands, key=lambda c: abs((c[0].y0 + c[0].y1) / 2 - cy))
            src = best[1]; cands.remove(best)
        kind = 'plate' if cap and cap['raw'].startswith('PL.') else 'band'
        cur['blocks'].append({'t': 'photo', 'page': pno, 'y': im['bbox'][1], 'src': src, 'kind': kind, 'cap': ' '.join(c['raw'] for c in caps) if cap else '', 'bbox': im['bbox']})
        for c in caps:
            if c: skip_y.add(id(c))
    # figures: a FIG. caption with drawings above it
    for l in lines:
        if l['face'] == 'plex' and l['size'] == 6.0 and l['raw'].startswith('FIG.'):
            caplines = [l] + [m for m in lines if m['face'] == 'plex' and m['size'] == 6.0 and l['y'] < m['y'] <= l['y'] + 22 and not m['raw'].startswith('FIG.')]
            # the region: from the previous body/standfirst/image line above to the caption
            above = [m['y1'] for m in lines if m['y1'] < l['y'] - 2 and (m['face'] in ('goudy', 'fell-it') and m['size'] >= 9.6 or m['face'] == 'fell' and m['size'] >= 12)]
            above += [im['bbox'][3] for im in pg['images'] if im['bbox'][3] < l['y']]
            y0 = (max(above) + 6) if above else 72; y1 = l['y'] - 2
            svg = fig_svg(pg, y0, y1)
            fid = re.match(r'FIG\. (\d+)', l['raw']).group(1)
            open(f'figures/fig{fid}-p{pno}.svg', 'w').write(svg)
            cur['blocks'].append({'t': 'figure', 'page': pno, 'y': y0, 'svg_file': f'figures/fig{fid}-p{pno}.svg', 'cap': ' '.join(unspace(c['raw']) for c in caplines), 'fig': int(fid)})
            for c in caplines: skip_y.add(id(c))
    # text roles
    para = None
    def flush():
        global para
        if para: cur['blocks'].append(para); para = None
    i = 0; L = [l for l in lines if l['face'] != 'furniture' and id(l) not in skip_y and not is_kicker(l) and not (l['face'] == 'fell' and l['size'] in (29.2, 33.0, 39.0))]
    dropcap = next((l['raw'] for l in lines if l['face'] == 'fell' and l['size'] == 39.0), '')
    # drop lines that are inside a figure region (they are in the SVG)
    figs = [b for b in cur['blocks'] if b['t'] == 'figure' and b['page'] == pno]
    def in_fig(l): return any(b['y'] - 1 <= l['y'] and l['y'] <= next(m for m in lines if m['raw'].startswith(f'FIG. {b["fig"]}'))['y'] for b in figs)
    L = [l for l in L if not in_fig(l)]
    while i < len(L):
        l = L[i]; f, s, t = l['face'], l['size'], l['text']
        if f == 'fell-it' and s == 12.8:
            flush(); cur['blocks'].append({'t': 'standfirst', 'page': pno, 'y': l['y'], 'text': t}); j = i + 1
            while j < len(L) and L[j]['face'] == 'fell-it' and L[j]['size'] == 12.8: cur['blocks'][-1]['text'] += ' ' + L[j]['text']; j += 1
            i = j; continue
        if f in ('goudy', 'fell') and s in (10.0, 10.5) and not (f == 'fell' and s == 10.5 and len(l['raw']) < 3):
            # body line; a 39px drop cap initial was skipped, so the 10.5 line is a paragraph start
            if para and (l['y'] - para['_y1'] > 9 or s == 10.5 and para['_size'] != 10.5): flush()
            prev_p = next((b for b in reversed(cur['blocks']) if b['t'] == 'p'), None)
            if para is None and not dropcap and prev_p and prev_p['page'] == pno - 1 \
               and re.match(r'[a-z”’]', re.sub('<[^>]+>', '', t).lstrip()[:1] or 'X') and not any(b['page'] == pno and b['t'] not in ('photo', 'figure') for b in cur['blocks']):
                cur['blocks'].remove(prev_p); para = prev_p; para['text'] += ' ' + t; para['_y1'] = l['y1']; para['_size'] = s; i += 1; continue
            if para is None:
                if dropcap: t = H.escape(dropcap, quote=False) + t; dropcap = ''
                para = {'t': 'p', 'page': pno, 'y': l['y'], 'text': t, '_y1': l['y1'], '_size': s}
            else: para['text'] += ' ' + t; para['_y1'] = l['y1']
            i += 1; continue
        flush()
        if f == 'plex' and s == 6.4 and l['raw'] == l['raw'].upper() and not l['raw'].startswith(('WALK', 'WHO', 'SIGHT')):
            # ledger: caption, heads (plex-md 6.4), rows (fell 9.8 + plex 8.2 on the same y)
            ledger = {'t': 'ledger', 'page': pno, 'y': l['y'], 'caption': l['raw'], 'heads': [], 'rows': []}; j = i + 1
            while j < len(L) and L[j]['face'] == 'plex-md' and L[j]['size'] == 6.4: ledger['heads'].append(L[j]['raw']); j += 1
            # Collect first, then pair (owner review 2026-10-25): a value set a hair above its
            # label used to land on the previous row, and a label wrapped in the shipped narrow
            # column became one row per line. Labels group by line gap; each value (its wrapped
            # lines merged) goes to the row whose vertical span is nearest.
            opts, vals = [], []
            while j < len(L) and ((L[j]['face'] == 'fell' and L[j]['size'] == 9.8) or (L[j]['face'] == 'plex' and L[j]['size'] == 8.2)):
                (opts if L[j]['face'] == 'fell' else vals).append(L[j]); j += 1
            groups = []
            for m in sorted(opts, key=lambda m: m['y']):
                if groups and m['y'] - groups[-1]['y1'] < 26 and not groups[-1]['text'].rstrip().endswith('</i>'):
                    groups[-1]['text'] += ('' if groups[-1]['text'].endswith('-') else ' ') + m['text']; groups[-1]['y1'] = m['y']
                else: groups.append({'text': m['text'], 'y0': m['y'], 'y1': m['y']})
            vgroups = []
            for m in sorted(vals, key=lambda m: m['y']):
                if vgroups and m['y'] - vgroups[-1]['y1'] < 12 and abs(m['y'] - vgroups[-1]['y1']) > 0: vgroups[-1]['raw'] += ' ' + m['raw']; vgroups[-1]['y1'] = m['y']
                else: vgroups.append({'raw': m['raw'], 'y0': m['y'], 'y1': m['y']})
            ledger['rows'] = [{'opt': g['text'], 'vals': []} for g in groups]
            for v in vgroups:
                if not groups: break
                vc = (v['y0'] + v['y1']) / 2
                k = min(range(len(groups)), key=lambda k: 0 if groups[k]['y0'] - 4 <= vc <= groups[k]['y1'] + 4 else min(abs(vc - groups[k]['y0']), abs(vc - groups[k]['y1'])))
                ledger['rows'][k]['vals'].append(v['raw'])
            cur['blocks'].append(ledger); i = j; continue
        if f == 'plex' and s == 6.0 and l['raw'].replace(' ', '') == 'THECALL':
            call = {'t': 'call', 'page': pno, 'y': l['y'], 'lead': '', 'rest': ''}; j = i + 1
            while j < len(L) and L[j]['size'] == 9.6 and L[j]['face'] in ('fell', 'goudy'):
                if L[j]['face'] == 'fell': call['lead'] += (' ' if call['lead'] else '') + L[j]['text']
                else: call['rest'] += (' ' if call['rest'] else '') + L[j]['text']
                j += 1
            cur['blocks'].append(call); i = j; continue
        if f == 't3' and s == 6.0 and unspace(l['raw']).startswith(('FOLLOW', 'OVERRULE')):
            # the two fork columns share rows; gather every 8.7 line below, split by x
            j = i + 1
            heads = [l] + [m for m in L[i + 1:] if m['face'] == 't3' and m['size'] == 6.0]
            items = [m for m in L if m['size'] == 8.7 and m['y'] > l['y'] and m['y'] < l['y'] + 120]
            def col(ms, left): return [m for m in ms if (m['x'] < 300) == left]
            forks = []
            for lab, ms in (('Follow this if', col(items, True)), ('Overrule it if', col(items, False))):
                bullets = sorted([m['y'] for m in ms if m['raw'] == '—'])
                groups = {b: [] for b in bullets}
                for m in ms:
                    if m['raw'] == '—': continue
                    b = max([b for b in bullets if b <= m['y'] + 3], default=bullets[0] if bullets else m['y'])
                    groups.setdefault(b, []).append(m)
                for b in sorted(groups):
                    txt = ' '.join(m['text'] for m in sorted(groups[b], key=lambda m: (m['y'], m['x']))).strip()
                    if txt: forks.append({'lab': lab, 'text': txt})
            # re-split: items are "condition → consequence"; two per column in the shipped book
            cur['blocks'].append({'t': 'forks', 'page': pno, 'y': l['y'], 'items': forks})
            used = set(id(m) for m in items) | set(id(m) for m in heads)
            L = [m for m in L if id(m) not in used]; continue
        if f == 'goudy' and s == 8.5:
            note = {'t': 'note', 'page': pno, 'y': l['y'], 'text': t}; j = i + 1
            while j < len(L) and L[j]['face'] == 'goudy' and L[j]['size'] == 8.5: note['text'] += ' ' + L[j]['text']; j += 1
            cur['blocks'].append(note); i = j; continue
        if f == 'plex' and s == 7.5 and l['raw'].startswith('→'):
            cur['blocks'].append({'t': 'xref', 'page': pno, 'y': l['y'], 'text': l['raw']}); i += 1; continue
        # everything else: keep as a styled line for the chapter-specific composers
        cur['blocks'].append({'t': 'line', 'page': pno, 'y': l['y'], 'x': l['x'], 'face': f, 'size': s, 'text': t, 'runs': l['runs']}); i += 1
    flush()

# order blocks by page then y; join fork items to "condition → consequence" pairs
for ch in chapters:
    ch['blocks'].sort(key=lambda b: (b['page'], b['y']))
    for b in ch['blocks']:
        b.pop('_y1', None); b.pop('_size', None)
json.dump(chapters, open('rome-book.json', 'w'), indent=1, ensure_ascii=False)

# ── preview ────────────────────────────────────────────────────────────────────
with open('_rome-preview.md', 'w') as f:
    for ch in chapters:
        f.write(f"\n## [{ch['id']}] {ch['kicker']} — {ch['title']}  (pp {ch['pages'][0]}–{ch['pages'][-1]})\n")
        for b in ch['blocks']:
            t = b['t']
            if t == 'p': f.write(f"- p{b['page']} P: {re.sub('<[^>]+>', '', b['text'])[:110]}…\n")
            elif t == 'line': f.write(f"- p{b['page']} LINE {b['face']} {b['size']} x{b['x']}: {b['text'][:90]}\n")
            elif t == 'ledger': f.write(f"- p{b['page']} LEDGER «{b['caption']}» heads={b['heads']} rows={len(b['rows'])}: {[r['opt'][:30] + ' ' + str(r['vals']) for r in b['rows']][:5]}\n")
            elif t == 'forks': f.write(f"- p{b['page']} FORKS: {[(i['lab'][:3], i['text'][:50]) for i in b['items']]}\n")
            elif t == 'photo': f.write(f"- p{b['page']} PHOTO {b['kind']} {b['src']} bbox={b['bbox']} «{b['cap'][:70]}»\n")
            elif t == 'figure': f.write(f"- p{b['page']} FIGURE {b['svg_file']} «{b['cap'][:90]}»\n")
            else: f.write(f"- p{b['page']} {t.upper()}: {re.sub('<[^>]+>', '', str(b.get('text') or b.get('lead')))[:110]}\n")
print(len(chapters), 'chapters:', [(c['id'], len(c['blocks'])) for c in chapters])
