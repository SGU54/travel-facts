# -*- coding: utf-8 -*-
"""margins.py — the two opening text pages whose margins stood empty (owner, 2026-10-26: "page 4 et 7 sont un peu vides").
  p4 (Rome, Solved.): its closing field carried only the last paragraph — the paragraph joins the prose, the field goes;
     the margin carries two sentences of the chapter itself (Marta: the margin runs with the text).
  p7 (How to read this book): the margin carries the key to the four marks, and where every source and date is."""
from bs4 import BeautifulSoup

CSS = """
.mq{ border-top:3px solid var(--red); padding-top:8px; margin-bottom:22px; break-inside:avoid; }
.mq .lab{ display:block; font-size:9px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--red); margin-bottom:6px; }
.mq .big{ font-size:19px; line-height:22px; font-weight:700; letter-spacing:-.02em; font-stretch:92%; word-spacing:.09em; }
.mk4 .it{ display:grid; grid-template-columns:22px 1fr; padding:7px 0 8px; border-bottom:1px solid var(--line); font-size:11px; line-height:15px; }
.mk4 .it b{ display:block; font-size:12px; }
"""
PULLS = ['Everything here traces to a single organizing fact.',   # the chapter's own words
         'The promise is not that you’ll agree with every verdict. It’s that you’ll never be guessing.']
MARKS = [('●', 'Established', 'structural; true for years'), ('◇', 'Official', 'a regulated fare, a published rule'),
         ('▲', 'Surveyed', 'our own observation, dated'), ('◆', 'Volatile', 'a live figure: it lives on the Field Sheet')]

def apply(html):
    html = html.replace('</style>', CSS + '</style>', 1)
    sp = BeautifulSoup(html, 'html.parser')
    sec = sp.find('section', id='intro')
    if sec is not None:
        pg = sec.find(class_='pg'); prose = pg.find(class_='prose') if pg else None
        field = sec.find(class_='photo')
        if field is not None and 'typo' in (field.get('class') or []) and prose is not None:
            for p in field.select('.tail p'): prose.append(p.extract())
            field.decompose()
        aside = pg.find(class_='aside') if pg else None
        if aside is not None and not aside.get_text(strip=True):
            aside.append(BeautifulSoup(''.join(f'<div class="mq"><span class="lab">From this chapter</span><div class="big">{t}</div></div>' for t in PULLS), 'html.parser'))
    sec = sp.find('section', id='how-to-read-this-book')
    if sec is not None:
        aside = sec.select_one('.pg .aside')
        if aside is not None and not aside.get_text(strip=True):
            rows = ''.join(f'<div class="it"><i class="mk">{g}</i><div><b>{n}</b>{d}</div></div>' for g, n, d in MARKS)
            aside.append(BeautifulSoup(f'<div class="mq mk4"><span class="lab">Four marks</span>{rows}</div>'
                                       f'<div class="mq"><span class="lab">Where the sources are</span><div class="big">Every volatile figure sits on the Field Sheet with its official source and the date it was read.</div></div>', 'html.parser'))
    return str(sp)
