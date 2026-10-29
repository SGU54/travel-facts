# -*- coding: utf-8 -*-
"""audit-atelier.py — the Atelier's scriptable checks (atelier/references/gates.md).

Runs on the COMPOSED dossier3.html + briefs.json (+ dossier.pdf for the font gate).
It does not replace the owner's look; it catches what a script can.

Usage: python3 audit-atelier.py [build-dir]
"""
import json, os, re, sys, html as H

BUILD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.chdir(BUILD)
doc = open('dossier3.html', encoding='utf-8').read()
briefs = json.load(open('briefs.json', encoding='utf-8'))
fails, warns = [], []

def txt(s): return re.sub(r'\s+', ' ', H.unescape(re.sub('<[^>]+>', ' ', s))).strip()

def section(sid):
    m = re.search(r'<section class="[^"]*" id="%s">(.*?)</section>' % re.escape(sid), doc, re.S)
    return m.group(1) if m else None

# 1 · alternation — from the briefed sequence
seq = [t for t in re.split(r'[\s·]+', briefs.get('sequence', '')) if t and t != 'cover']
letters = ''.join(c for c in ''.join(seq) if c in 'ABCDEF' or c == '×')
run = re.findall(r'(A{3,}|B{3,}|C{3,}|E{3,}|F{3,})', ''.join(seq).replace('×7', ''))
if run: fails.append(f'alternation: {run} three times running in the sequence')

for sid, b in briefs['chapters'].items():
    if b.get('skip'): continue
    sec = section(sid)
    if sec is None: fails.append(f'{sid}: no composed section'); continue
    prose = txt(re.sub(r'<div class="c6 ticket">.*?</div></div>', ' ', sec, flags=re.S))
    # 2 · hero present
    hero = b.get('hero', {})
    if not hero: fails.append(f'{sid}: brief names no hero')
    elif hero.get('type') == 'band' and 'c6 bleed' not in sec and 'c6 halfband' not in sec:
        fails.append(f'{sid}: hero is a band but no bleed/half-band rendered')
    elif hero.get('type') == 'figure' and 'figx' not in sec:
        fails.append(f'{sid}: hero is a figure but no figure rendered')
    elif hero.get('type') == 'number' and '<div class="dnum">' not in sec:
        fails.append(f'{sid}: hero is a number but no dnum rendered')
    elif hero.get('type') == 'pull' and 'opull' not in sec:
        fails.append(f'{sid}: hero is a pull but no opener pull rendered')
    # 3 · verdict first (decisions)
    if b['kind'] == 'decision':
        t = sec.find('class="c6 ticket"'); p = sec.find('<p class="c4"')
        if t < 0: fails.append(f'{sid}: no verdict ticket')
        elif p >= 0 and p < t: fails.append(f'{sid}: prose starts before the verdict ticket')
        if 'c6 ledgerx' not in sec: fails.append(f'{sid}: no ledger instrument')
        if b.get('decides_row') is not None and 'row decides' not in sec:
            fails.append(f'{sid}: decisive row briefed but not marked')
    # 4 · pull integrity — verbatim in this chapter's prose
    for key in ('pull',):
        if b.get(key):
            if b[key]['text'] not in prose: fails.append(f'{sid}: pull not verbatim in prose: {b[key]["text"]!r}')
    if hero.get('type') == 'pull' and hero['text'] not in prose:
        fails.append(f'{sid}: opener pull not verbatim in prose: {hero["text"]!r}')
    # 5 · image jobs — no column-width photo under a title
    after_opener = sec.split('class="c6 opener6">', 1)[-1]
    m_close = re.search(r'</div>\s*</div>\s*(<[a-z]+ class="[^"]*")', after_opener)
    if m_close and m_close.group(1).startswith('<figure class="photo'):
        fails.append(f'{sid}: a column-width photo sits directly under the opener (the old recipe)')
    if 'photo band' in sec: fails.append(f'{sid}: an old head band survived composition')
    # 6 · margin — a chapter with marks in its prose carries the key
    if '<span class="mk' in sec and 'Marks on this page' not in sec and sid not in ('howto',):
        warns.append(f'{sid}: prose carries marks but no marks key in the margin')

# 7 · fonts — only the briefed families in the PDF
try:
    import pymupdf
    if os.path.exists('dossier.pdf'):
        fam = set()
        for p in pymupdf.open('dossier.pdf'):
            for f in p.get_fonts(full=True):
                n = f[3].split('+')[-1]
                if n: fam.add(n)
        allowed = ('Anton', 'SortsMillGoudy', 'IBMPlexMono', 'PublicSans', 'NotoSansSymbols2')
        bad = sorted(n for n in fam if not n.startswith(allowed))
        if bad: fails.append(f'fonts: system fallbacks embedded: {bad}')
except ImportError:
    warns.append('fonts: pymupdf missing, gate skipped')

for w in warns: print('warn ', w)
for f in fails: print('FAIL ', f)
print(f'atelier audit: {len(fails)} fail · {len(warns)} warn · {sum(1 for b in briefs["chapters"].values() if not b.get("skip"))} chapters')
sys.exit(1 if fails else 0)
