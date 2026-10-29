# -*- coding: utf-8 -*-
"""rome_writer.py — the writer's answers to Ruth's Rome filings (studio, 2026-10-26), applied to rome-book.json
before composing: _studio/writer/rome-edits.json (each edit: Ruth's id, chapter, block, field, exact old → new, source),
closures.json (B3: what closes and what a strike means). An edit that no longer matches stops the build."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(HERE, '_studio', 'writer')

def _get(obj, path):
    for part in re.findall(r'[^.\[\]]+|\[\d+\]', path):
        obj = obj[int(part[1:-1])] if part.startswith('[') else obj[part]
    return obj
def _set(obj, path, val):
    parts = re.findall(r'[^.\[\]]+|\[\d+\]', path); *head, last = parts
    for part in head: obj = obj[int(part[1:-1])] if part.startswith('[') else obj[part]
    if last.startswith('['): obj[int(last[1:-1])] = val
    else: obj[last] = val

def write(CH):
    by = {c['id']: c for c in CH}
    for e in json.load(open(os.path.join(W, 'rome-edits.json'), encoding='utf-8')):
        b = by[e['chapter_id']]['blocks'][e['block']]; f = e.get('field', 'text')
        cur = _get(b, f)
        if cur.count(e['old']) != 1: raise SystemExit(f"rome_writer: {e['id']} no longer matches once in {e['chapter_id']}[{e['block']}].{f}")
        _set(b, f, cur.replace(e['old'], e['new']))
        if b.get('t') == 'line' and f == 'text' and b.get('runs'):   # a line keeps its styled runs: replace inside one run, else one run
            runs = b['runs']; hit = [r for r in runs if e['old'] in r[2]]
            if hit: hit[0][2] = hit[0][2].replace(e['old'], e['new'])
            else: b['runs'] = [[runs[0][0], runs[0][1], b['text']]]
    cl = json.load(open(os.path.join(W, 'closures.json'), encoding='utf-8'))
    ch = by[cl['chapter_id']]; at = next(i for i, b in enumerate(ch['blocks']) if b.get('t') == 'p' and cl['after_old'] in b.get('text', ''))
    paras = re.findall(r'<p>(.*?)</p>', cl['html'], re.S)
    for k, t in enumerate(paras): ch['blocks'].insert(at + 1 + k, {'t': 'p', 'text': t.strip()})
    return CH

def fieldsheet():
    return json.load(open(os.path.join(W, 'fieldsheet.json'), encoding='utf-8'))
