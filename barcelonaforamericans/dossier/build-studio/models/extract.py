# -*- coding: utf-8 -*-
"""extract.py — the two pilot chapters as structured JSON every model builds from."""
import re, json, html as H
from bs4 import BeautifulSoup
out = {}
for sid in ('d06', 'd01'):
    s = BeautifulSoup(open(f'_src-{sid}.html', encoding='utf-8').read(), 'lxml')
    sec = s.section
    d = {}
    d['kicker'] = sec.find(class_='kicker').get_text(' ', strip=True)
    d['title'] = sec.h1.get_text(' ', strip=True)
    d['standfirst'] = sec.find(class_='standfirst').decode_contents().strip()
    fig = sec.find('figure')
    d['figure_svg'] = str(fig.svg) if fig and fig.svg else None
    d['figure_cap'] = fig.figcaption.get_text(' ', strip=True) if fig and fig.svg else None
    t = sec.find('table')
    d['ledger_caption'] = t.caption.get_text(' ', strip=True)
    d['ledger_head'] = [th.get_text(strip=True) for th in t.thead.find_all('th')]
    rows = []
    for tr in t.tbody.find_all('tr'):
        td = tr.find_all('td')
        opt = td[0].find(class_='opt'); sub = td[0].find(class_='sub')
        for mk in td[0].find_all(class_='mk'): mk.decompose()
        rows.append({'opt': opt.decode_contents().strip(), 'sub': re.sub(r'^\s*—\s*', '', sub.get_text(' ', strip=True)) if sub else '', 'call': td[1].get_text(' ', strip=True)})
    d['ledger'] = rows
    paras = []
    for p in sec.find_all('p', recursive=False):
        paras.append(p.decode_contents().strip())
    d['paras'] = paras
    v = sec.find(class_='verdict').p
    d['verdict_strong'] = v.strong.get_text(' ', strip=True)
    v.strong.decompose()
    d['verdict_rest'] = v.decode_contents().strip()
    fa = []
    for col in sec.find(class_='fa').find_all(class_='col'):
        fa.append({'lab': col.find(class_='lab').get_text(strip=True), 'strong': col.p.strong.get_text(' ', strip=True), 'text': re.sub(r'^\s*', '', col.p.decode_contents().replace(str(col.p.strong), '', 1)).strip()})
    d['forks'] = fa
    note = sec.find(class_='note')
    xref = note.find(class_='xref'); d['note_xref'] = xref.get_text(' ', strip=True) if xref else ''
    if xref: xref.decompose()
    vol = note.find('span', class_='vol')
    d['volatile'] = bool(vol)
    if vol: vol.decompose()
    txt = note.decode_contents()
    txt = re.sub(r"<span class='mk off'>[^<]*</span>", '<i class="mk off">◇</i>', txt)
    txt = re.sub(r"<span class='mk est'>[^<]*</span>", '<i class="mk est">●</i>', txt)
    d['note'] = re.sub(r'^\s*—\s*', '', re.sub(r'\s+', ' ', txt)).strip()
    photos = []
    for f in sec.find_all('figure'):
        if f.img:
            photos.append({'src': f.img['src'], 'cap': re.sub(r'^PL\. \w+\s*', '', f.figcaption.get_text(' ', strip=True))})
    d['photos'] = photos
    out[sid] = d
json.dump(out, open('chapters.json', 'w'), indent=1, ensure_ascii=False)
for sid, d in out.items():
    print(sid, d['title'], len(d['paras']), 'paras', [len(p) for p in d['paras']], 'rows', len(d['ledger']), 'photos', [p['src'] for p in d['photos']], 'svg', bool(d['figure_svg']))
    print('  verdict:', d['verdict_strong'][:80]); print('  note:', d['note'][:120]); print('  forks:', [(f['lab'], f['strong']) for f in d['forks']])
