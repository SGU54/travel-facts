# -*- coding: utf-8 -*-
"""add-outline.py — PDF bookmarks for the Affiche book, from the page map."""
import json, pymupdf, re
pages = json.load(open('_pages-affiche.json'))
first = {}
for pg in pages:
    for e in pg['els']:
        if e['sec'] and e['sec'] not in first: first[e['sec']] = pg['page']
titles = {}
for m in re.finditer(r'<section class="[^"]*" id="([^"]+)">.*?<span class="rh-src">([^<]*)</span>', open('dossier3.html', encoding='utf-8').read(), re.S):
    titles[m.group(1)] = m.group(2)
doc = pymupdf.open('dossier.pdf'); toc = [[1, 'Cover', 1]]
for sid, p in sorted(first.items(), key=lambda kv: kv[1]):
    if sid == 'fs': continue
    lvl = 2 if sid.startswith('d0') else 1
    toc.append([lvl, titles.get(sid, sid), p])
doc.set_toc(toc); doc.save('dossier.outlined.pdf'); doc.close()
import os; os.replace('dossier.outlined.pdf', 'dossier.pdf'); print('outline:', len(toc), 'entries')
