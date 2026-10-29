# -*- coding: utf-8 -*-
"""compose.py — the Atelier's maquettiste pass for this build (model 2).

Reads dossier3.raw.html (build-html.py's output), briefs.json (the Art Director's
per-chapter briefs, with a RESERVE of apparatus per chapter) and levers.json (what
the measured loop in atelier-loop.py decided after looking at the rendered pages),
recomposes every briefed chapter on the 6-column grid with the house vocabulary, and
writes dossier3.html for render-both.py.

Usage:  python3 compose.py [build-dir]

Levers (levers.json, all optional, all additive):
  tight        [sid, …]              the chapter set one notch tighter (.tight2)
  add_closer   {sid: true}           a closing plate appended; the renderer's fill
                                     pass sizes it to the page it closes
  margin       {sid: [{before: i, reserve: k}, …]}   reserve item k floats beside ¶ i
  wide         {sid: [i, …]}         ¶ i set full measure (nothing for its margin)
  para_on_A    {sid: false}          decision: no prose on page A (stub seen)
"""
import json, os, re, sys, html as H
from bs4 import BeautifulSoup, NavigableString

BUILD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(BUILD)

RAW = 'dossier3.raw.html'
if not os.path.exists(RAW):
    os.rename('dossier3.html', RAW)
doc = open(RAW, encoding='utf-8').read()
briefs = json.load(open('briefs.json', encoding='utf-8'))
LEV = json.load(open('levers.json', encoding='utf-8')) if os.path.exists('levers.json') else {}
BOOK = briefs['book']
soup = BeautifulSoup(doc, 'lxml')
WRITEBACK = []

MARKS = [('est', '●', 'Established — structural, true for years'),
         ('off', '◇', 'Official — a published rule or fare'),
         ('sur', '▲', 'Surveyed — our own dated observation'),
         ('call', '◈', 'Our call — a judgment, not a finding'),
         ('vol', '◆', 'Volatile — a live figure; see the Field Sheet')]
MARK_KEYS = {k for k, _, _ in MARKS}

def el(tag, cls=None, html=None, **attrs):
    t = soup.new_tag(tag, **attrs)
    if cls: t['class'] = cls.split()
    if html is not None:
        frag = BeautifulSoup(html, 'lxml')
        body = frag.body or frag
        for c in list(body.children):
            t.append(c)
    return t

def text(t):
    return re.sub(r'\s+', ' ', t.get_text(' ')).strip() if t else ''

def inner(t):
    return ''.join(str(c) for c in t.contents) if t else ''

def stub_size(s):
    n = len(s)
    return 48 if n <= 3 else 38 if n <= 4 else 30 if n <= 6 else 24 if n <= 9 else 18

def mk_marks(used):
    box = el('div', 'app')
    box.append(el('div', 'k', 'Marks on this page'))
    m = el('div', 'marks')
    for key, g, label in MARKS:
        if used and key not in used: continue
        m.append(el('div', None, f'<span class="g {key}">{g}</span><span>{label}</span>'))
    box.append(m)
    return box

def mk_ref(k, html):
    box = el('div', 'app')
    box.append(el('div', 'k', k))
    box.append(el('p', 'ref', html))
    return box

def strip_pl(cap):
    return re.sub(r'<span class="pl">.*?</span>\s*(&nbsp;)?', '', cap).strip()

def mk_inset(src, label, cap, pos=None):
    f = el('figure', 'inset')
    img = el('img', None, src=src, width='1100', height='733', decoding='sync', loading='eager')
    if pos: img['style'] = f'object-position:{pos}'
    f.append(img)
    f.append(el('figcaption', 'cap', f'<span class="pl">{label}</span>{strip_pl(cap)}'))
    return f

def mk_pull(s):
    return el('div', 'pull', s)

def mk_caption(label, cap):
    return el('p', 'cap', f'<span class="pl">{label}</span>{strip_pl(cap)}')

def mk_bleed(src):
    d = el('div', 'c6 bleed')
    d.append(el('img', None, src=src, width='1800', height='1200', decoding='sync', loading='eager'))
    d.append(el('div', 'tear'))
    return d

def mk_halfband(src, cap):
    f = el('figure', 'c6 halfband')
    f.append(el('img', None, src=src, width='1800', height='1200', decoding='sync', loading='eager'))
    f.append(el('figcaption', None, cap))
    return f

def mk_closer(src, cap, pos=None):
    """A closing plate the renderer's fill pass will size to the page it closes."""
    f = el('figure', 'photo wide c6 detail')
    f.append(el('img', None, src=src, width='1100', height='733', decoding='sync', loading='eager'))
    if pos: f['style'] = f'--pos:{pos}'
    f.append(el('figcaption', None, f'<span class="pl">PL. ·</span> &nbsp;{strip_pl(cap)}'))
    return f

def wrap(items):
    w = el('div', 'mg mgw')
    for e in items: w.append(e)
    return w

def used_marks(section):
    return {c for m in section.select('.mk') for c in m.get('class', []) if c in MARK_KEYS}

def plate_label(fig):
    pl = fig.select_one('.pl') if fig else None
    return text(pl) if pl else 'PL.'

def reserve_item(b, k, label='Pl.', cap=''):
    r = b.get('reserve', [])
    if k >= len(r): return None
    it = r[k]
    if it['type'] == 'pull': return mk_pull(it['text'])
    if it['type'] == 'inset': return mk_inset(it['src'], it.get('label', label), it.get('cap', cap), it.get('pos'))
    return None

def lever_margin(sid, b, add, band_src, band_cap, closer_src, closer_cap):
    for m in LEV.get('margin', {}).get(sid, []):
        it = reserve_item(b, m['reserve'], 'Pl. · detail', band_cap or closer_cap)
        if it is None:   # reserve exhausted → a detail crop of a plate the chapter owns
            src = band_src or closer_src
            if src:
                it = mk_inset(src, 'Pl. · detail', band_cap or closer_cap, m.get('pos', '20% 50%'))
        if it is not None:
            add(m['before'], it, before=True)

# ──────────────────────────────────────────────────────────────────────────
def compose_decision(sec, b):
    sid = sec['id']
    kicker = text(sec.select_one('.kicker'))
    h1 = inner(sec.select_one('h1'))
    lede = inner(sec.select_one('.standfirst'))
    band = sec.select_one('figure.photo.band')
    band_src = band.img['src'] if band else None
    band_cap = inner(band.figcaption) if band else ''
    figure = next((f for f in sec.find_all('figure', recursive=False) if 'photo' not in (f.get('class') or [])), None)
    ledger = sec.select_one('table.ledger')
    paras = [p for p in sec.find_all('p', recursive=False)]
    verdict = sec.select_one('.verdict p')
    fa = sec.select_one('.fa')
    cols = fa.select('.col')
    fors = [inner(p) for p in cols[0].select('p')]
    againsts = [inner(p) for p in cols[1].select('p')]
    note = sec.select_one('.note')
    closer = next((f for f in sec.select('figure.photo') if 'band' not in f.get('class', [])), None)
    closer_src = closer.img['src'] if closer else None
    closer_cap = inner(closer.figcaption) if closer else ''
    closer_pl = plate_label(closer) if closer else 'PL.'
    num = re.search(r'Decision (\d+)', kicker).group(1)
    cat = kicker.split('·')[-1].strip()
    marks = used_marks(sec)
    hero = b.get('hero', {})

    new = el('section', 'dec chap decision at', id=sid)
    if sid in LEV.get('tight', []): new['class'].append('tight2')
    new.append(el('span', 'rh-src', f'Decision {num} · {cat}'))

    # A · the opener pack
    op = el('div', 'c6 opener6')
    left = el('div', 'oleft')
    left.append(el('div', 'kicker', f'Decision {num} · {cat}'))
    left.append(el('h1', None, h1))
    left.append(el('div', 'standfirst', lede))
    op.append(left)
    op.append(el('div', 'dnum', f'{num}<small>{cat} · of {BOOK["ncalls"]} calls</small>'))
    new.append(op)

    # the verdict ticket
    exc = (againsts if b.get('exception', 'against') == 'against' else fors)
    exc_html = exc[0] if exc else ''
    tk = el('div', 'c6 ticket')
    st = el('div', 'stub')
    big = b['stub']['big']
    st.append(el('div', 'big', big, style=f'font-size:{stub_size(big)}px'))
    st.append(el('div', 'lab', b['stub']['lab']))
    tk.append(st)
    mn = el('div', 'main')
    mn.append(el('p', 'vlab', 'The call'))
    mn.append(el('p', 'verdict', inner(verdict)))
    if exc_html:
        mn.append(el('p', 'exc', f'<b>The exception that changes it.</b> {exc_html}'))
    tk.append(mn)
    new.append(tk)

    # the ledger, as an instrument
    cap = text(ledger.caption)
    ths = [text(t) for t in ledger.select('thead th')]
    lg = el('div', 'c6 ledgerx')
    lg.append(el('div', 'lcap', f'<span>{cap}</span><span>{" · ".join(ths)}</span>'))
    rows = el('div', 'rows')
    for i, tr in enumerate(ledger.select('tbody tr')):
        tds = tr.find_all('td')
        opt = tds[0].select_one('.opt'); sub = tds[0].select_one('.sub')
        r = el('div', 'row' + (' decides' if b.get('decides_row') == i else ''))
        r.append(el('div', 'site', f'<b>{inner(opt) if opt else inner(tds[0])}</b><i>{inner(sub) if sub else ""}</i>'))
        r.append(el('div', 'call', inner(tds[1])))
        rows.append(r)
    lg.append(rows)
    new.append(lg)

    # apparatus, by paragraph slot
    slots = {}
    def add(i, e, before=False):
        slots.setdefault(i, {'before': [], 'after': []})['before' if before else 'after'].append(e)
    for m in b.get('margin', []):
        if m.get('marks'): add(m.get('after', 0), mk_marks(marks))
        else: add(m.get('after', 0), mk_ref(m['k'], m['html']))
    inset_from = None
    if b.get('inset') and closer_src and b['inset'].get('src', 'closer') == 'closer':
        add(b['inset'].get('after', 1), mk_inset(closer_src, closer_pl, closer_cap)); inset_from = 'closer'
    elif b.get('inset') and band_src and b['inset'].get('src') == 'band':
        add(b['inset'].get('after', 1), mk_inset(band_src, 'Pl.', band_cap)); inset_from = 'band'
    if b.get('pull'):
        add(b['pull'].get('after', 2), mk_pull(b['pull']['text']))
    lever_margin(sid, b, add, band_src, band_cap, closer_src, closer_cap)
    wide = set(LEV.get('wide', {}).get(sid, []))

    # page A: the first paragraph stays unless the loop saw it strand (para_on_A false)
    break_after = b.get('break_after', 0)
    if LEV.get('para_on_A', {}).get(sid) is False:
        break_after = -1
    state = {'band_used': False, 'figure': figure}
    def emit_hero():
        if hero.get('type') == 'band' and band_src and inset_from != 'band':
            new.append(mk_bleed(band_src)); new.append(wrap([mk_caption('Pl. · ' + b.get('band_label', ''), band_cap)]))
            state['band_used'] = True
        elif hero.get('type') == 'figure' and state['figure'] is not None:
            fg = state['figure'].extract(); fg['class'] = ['c6', 'figx', 'pagetop']; new.append(fg); state['figure'] = None
        elif band_src and inset_from != 'band':
            new.append(mk_halfband(band_src, band_cap)); state['band_used'] = True
    if break_after < 0: emit_hero()

    n = len(paras)
    body = new
    for i, p in enumerate(paras):
        p = p.extract(); p['class'] = (p.get('class') or []) + ['c4'] + (['pa'] if i <= break_after else []) + (['wide'] if i in wide else [])
        p['data-p'] = f'{sid}:{i}'
        s = slots.pop(i, {'before': [], 'after': []})
        items = s['before'] + s['after']      # a margin item floats at the top of the paragraph that FOLLOWS it
        if i == n - 1:
            body = el('div', 'c6 closeblock'); new.append(body)   # last ¶ + forks + volatile row travel together
        if items: body.append(wrap(items))
        body.append(p)
        if i == break_after: emit_hero()
    for k in sorted(slots):
        items = slots[k]['before'] + slots[k]['after']
        if items: body.append(wrap(items))
    if state['figure'] is not None:
        fg = state['figure'].extract(); fg['class'] = ['c6', 'figx']; new.append(fg)

    fk = el('div', 'c6 forks')
    fk.append(el('div', 'fork a', '<h4>When the default holds</h4>' + ''.join(f'<p>{x}</p>' for x in fors)))
    fk.append(el('div', 'fork b', "<h4>When it doesn't</h4>" + ''.join(f'<p>{x}</p>' for x in againsts)))
    body.append(fk)
    vr = el('div', 'c6 volrow')
    if b.get('stamp'): vr.append(el('div', 'stamp', b['stamp']))
    vr.append(el('p', None, inner(note)))
    body.append(vr)

    if closer is not None and inset_from != 'closer' and b.get('closer', 'keep') == 'keep':
        c = closer.extract(); c['class'] = c.get('class', []) + ['c6']; new.append(c)
    elif LEV.get('add_closer', {}).get(sid):
        src = closer_src if (inset_from != 'closer' and closer_src) else (band_src or closer_src)
        if src:
            reused = (src == band_src and state['band_used']) or (src == closer_src and inset_from == 'closer')
            new.append(mk_closer(src, closer_cap if src == closer_src else band_cap, '30% 50%' if reused else None))
            WRITEBACK.append(f'{sid}: closing plate added from {os.path.basename(src)}')
    sec.replace_with(new)

# ──────────────────────────────────────────────────────────────────────────
def compose_essay(sec, b):
    sid = sec['id']
    kicker = sec.select_one('.kicker'); h1 = sec.select_one('h1'); lede = sec.select_one('.standfirst')
    band = sec.select_one('figure.photo.band')
    band_src = band.img['src'] if band else None
    band_cap = inner(band.figcaption) if band else ''
    closer = next((f for f in sec.select('figure.photo') if 'band' not in f.get('class', [])), None)
    closer_src = closer.img['src'] if closer else None
    closer_cap = inner(closer.figcaption) if closer else ''
    closer_pl = plate_label(closer) if closer else 'PL.'
    marks = used_marks(sec)
    hero = b.get('hero', {})

    new = el('section', 'dec chap at essay', id=sid)
    if sid in LEV.get('tight', []): new['class'].append('tight2')
    rh = sec.select_one('.rh-src')
    new.append(el('span', 'rh-src', inner(rh) if rh else text(h1)))

    op = el('div', 'c6 opener6')
    left = el('div', 'oleft')
    if kicker: left.append(kicker.extract())
    left.append(h1.extract())
    if lede: left.append(lede.extract())
    op.append(left)
    if hero.get('type') == 'number':
        op.append(el('div', 'dnum', f'{hero["value"]}<small>{hero["label"]}</small>'))
    elif hero.get('type') == 'pull':
        op.append(el('div', 'opull', hero['text']))
    new.append(op)
    band_used = False
    if hero.get('type') == 'band' and band_src:
        new.append(mk_halfband(band_src, band_cap)); band_used = True
    if band is not None: band.decompose()
    if closer is not None and b.get('closer') == 'drop':
        closer.decompose(); closer = None; closer_src = None

    slots = {}
    def add(i, e, before=False):
        slots.setdefault(i, {'before': [], 'after': []})['before' if before else 'after'].append(e)
    for m in b.get('margin', []):
        if m.get('marks'): add(m.get('after', 0), mk_marks(marks))
        else: add(m.get('after', 0), mk_ref(m['k'], m['html']))
    if b.get('inset'):
        if b['inset'].get('src') == 'band' and band_src and not band_used:
            add(b['inset'].get('after', 0), mk_inset(band_src, 'Pl.', band_cap)); band_used = True
        elif closer_src:
            add(b['inset'].get('after', 0), mk_inset(closer_src, closer_pl, closer_cap)); closer.decompose(); closer = None; closer_src = None
    if b.get('pull'):
        add(b['pull'].get('after', 1), mk_pull(b['pull']['text']))
    lever_margin(sid, b, add, band_src, band_cap, closer_src, closer_cap)
    wide = set(LEV.get('wide', {}).get(sid, []))

    i = -1
    for node in list(sec.children):
        if isinstance(node, NavigableString): continue
        if node.name == 'span' and 'rh-src' in node.get('class', []): continue
        node = node.extract()
        cls = node.get('class') or []
        if node.name == 'p':
            i += 1; node['class'] = cls + ['c4'] + (['wide'] if i in wide else []); node['data-p'] = f'{sid}:{i}'
            s = slots.pop(i, {'before': [], 'after': []}); items = s['before'] + s['after']
            if items: new.append(wrap(items))
            new.append(node); continue
        if node.name == 'figure' and 'photo' in cls:
            node['class'] = cls + ['c6']; new.append(node); continue
        if node.name == 'figure':
            node['class'] = cls + ['c6', 'figx']; new.append(node); continue
        if node.name in ('h2', 'h3'):
            node['class'] = cls + (['c6'] if b.get('instrument') else ['c4']); new.append(node); continue
        if node.name in ('ul', 'table', 'div'):
            node['class'] = cls + (['c6'] if b.get('instrument', True) else ['c4']); new.append(node); continue
        node['class'] = cls + ['c4']; new.append(node)
    for k in sorted(slots):
        items = slots[k]['before'] + slots[k]['after']
        if items: new.append(wrap(items))
    if LEV.get('add_closer', {}).get(sid) and closer is None and band_src:
        new.append(mk_closer(band_src, band_cap, '30% 50%' if band_used else None))
        WRITEBACK.append(f'{sid}: closing plate added from {os.path.basename(band_src)}')
    sec.replace_with(new)

# ──────────────────────────────────────────────────────────────────────────
n = 0
for sid, b in briefs['chapters'].items():
    sec = soup.find('section', id=sid)
    if sec is None:
        print('!! no section', sid); continue
    if b.get('skip'): continue
    if b['kind'] == 'decision': compose_decision(sec, b)
    else: compose_essay(sec, b)
    n += 1

out = str(soup)
def _img_fix(m):   # the compositor's regexes want src FIRST; lxml sorts attributes
    attrs = dict(re.findall(r'([a-z-]+)="([^"]*)"', m.group(0)))
    src = attrs.pop('src', '')
    rest = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
    return f'<img src="{src}" {rest}/>'
out = re.sub(r'<img [^>]*/?>', _img_fix, out)
out = re.sub(r"(?<!class=\"mk vol\">)(?<!class='mk vol'>)(?<!class=\"g vol\">)◆", '<span class="mk vol">◆</span>', out)
head = doc.split('<body')[0]
body = out[out.index('<body'):]
open('dossier3.html', 'w', encoding='utf-8').write(head + body)
for w in WRITEBACK: print('  writeback:', w)
print(f'composed {n} chapters -> dossier3.html ({len(head)+len(body):,} bytes)')
