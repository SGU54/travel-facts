# -*- coding: utf-8 -*-
"""eye.py — the before/after sheets for the owner's look (atelier/references/gates.md).

For every chapter: the previous release's pages on the top row, the new build's
pages on the bottom row, same size. Chapters are located in each PDF by their
title text (openers) and running head (continuations).

Usage: python3 eye.py <before.pdf> <after.pdf> [out-dir]
"""
import os, re, sys
import pymupdf
from PIL import Image, ImageDraw

before, after = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else '_eye'
os.makedirs(out, exist_ok=True)
DPI = 48

CHAPTERS = [  # (id, opener title as printed, running-head text)
    ('contract', 'THE CONTRACT', 'THE CONTRACT'), ('howto', 'HOW TO READ THIS', 'HOW TO READ THIS'),
    ('contents', 'CONTENTS', 'CONTENTS'), ('ground', 'THE GROUND', 'THE GROUND'),
    ('fly', 'BEFORE YOU FLY', 'BEFORE YOU FLY'), ('dayzero', 'DAY ZERO', 'DAY ZERO'),
    ('timing', 'TIMING', 'TIMING'), ('setpieces', 'THE SET PIECES', 'THE SET PIECES'),
    ('d01', 'WHERE TO BASE', 'DECISION 01'), ('d02', 'THE APARTMENT QUESTION', 'DECISION 02'),
    ('d03', 'THE MONEY-TRAP WEB', 'DECISION 03'), ('d05', 'SEQUENCING THE DAYS', 'DECISION 04'),
    ('d06', 'THE GAUDÍ FORK', 'DECISION 05'), ('d07', 'WHICH DAY TRIP', 'DECISION 06'),
    ('d08', 'HOW NOT TO EAT LIKE A TOURIST', 'DECISION 07'), ('horizons', 'THE HORIZONS', 'THE HORIZONS'),
    ('risk', 'HOW WORRIED SHOULD YOU BE?', 'HOW WORRIED'), ('plan', 'THE PLAN', 'THE PLAN'),
    ('fail', 'FAILURE MODES', 'FAILURE MODES'), ('wallet', 'THE WALLET CARD', 'THE WALLET CARD'),
    ('back', "WHAT THIS WON'T TELL YOU", "WHAT THIS WON"), ('then', 'BARCELONA, THEN', 'BARCELONA, THEN'),
    ('beforeyoubook', 'DECIDE THESE FIRST', 'BEFORE YOU BOOK'),
]

def pages_by_chapter(pdf):
    d = pymupdf.open(pdf); cur = None; m = {}
    for i, p in enumerate(d):
        t = p.get_text().upper().replace('\n', ' ')
        big = [s['text'].upper() for b in p.get_text('dict')['blocks'] for l in b.get('lines', []) for s in l['spans'] if s['size'] >= 26]
        bigt = ' '.join(big)
        hit = None
        for cid, title, rh in CHAPTERS:
            if title.replace(' ', '') in bigt.replace(' ', ''): hit = cid; break
        if hit is None:
            head = t[:160]
            for cid, title, rh in CHAPTERS:
                if rh in head: hit = cid; break
        if hit: cur = hit
        if cur: m.setdefault(cur, []).append(i)
    return d, m

db, mb = pages_by_chapter(before)
da, ma = pages_by_chapter(after)

def tiles(d, idx):
    out = []
    for i in idx:
        pix = d[i].get_pixmap(dpi=DPI); out.append(Image.frombytes('RGB', [pix.width, pix.height], pix.samples))
    return out

summary = []
for cid, title, _ in CHAPTERS:
    tb, ta = tiles(db, mb.get(cid, [])), tiles(da, ma.get(cid, []))
    if not tb and not ta: continue
    w, h = (tb or ta)[0].size
    n = max(len(tb), len(ta), 1)
    sheet = Image.new('RGB', (n * (w + 8) + 8, 2 * (h + 8) + 60), '#2b2b2b')
    dr = ImageDraw.Draw(sheet)
    dr.text((8, 6), f'{cid} · {title}   BEFORE (2026-10-20 release) {len(tb)}pp', fill='#eee')
    dr.text((8, h + 8 + 34), f'AFTER (atelier) {len(ta)}pp', fill='#eee')
    for k, t in enumerate(tb): sheet.paste(t, (8 + k * (w + 8), 24))
    for k, t in enumerate(ta): sheet.paste(t, (8 + k * (w + 8), h + 8 + 52))
    sheet.save(os.path.join(out, f'{cid}.png'))
    summary.append((cid, len(tb), len(ta)))
print('chapter  before  after')
for cid, nb, na in summary: print(f'{cid:14s} {nb:5d} {na:6d}')
print(f'total {sum(x[1] for x in summary)} -> {sum(x[2] for x in summary)}  (sheets in {out}/)')
