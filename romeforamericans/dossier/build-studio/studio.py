# -*- coding: utf-8 -*-
"""studio.py — the studio of three on Rome (2026-10-26; from Barcelona's studio.py): what Brunner filed and Marta ruled,
applied at compose time after brunner_set. Logged in desk.md.

  Marta: captions are sentence case (a caption is a sentence, never a label);
         a label in capitals holds six words or fewer — a longer one is set in lower case;
         display type keeps a word space of at least 0.2 em (tracking tightens letters, not words).
  Brunner: US house style (brunner_set.us_house) — spelling, Decision NN, months, quotes, lang en-US.
"""
import os, re, sys, json
sys.path.insert(0, os.path.expanduser('~/.claude/skills/atelier/scripts'))
from brunner_set import us_house
from bs4 import BeautifulSoup

CAPTIONS = '.photo .cap, figcaption, .mapwrap .cap, .cut'
LABELS = ['.poster .under', '.cover .bar', '.cover .stamp', '.stack .v', '.ribbon .v', '.stack .lab', '.vol .lab', '.sideq .lab',
          '.note .lab', '.li .dl', '.tier .k', '.ask .who', '.days .k', '.dayrow .k', '.card .tag', '.fs .fsdate', '.fstable th',
          '.poster .slug span', '.fsnote', '.photo.duo .cap', '.gloss', '.poster .lab', '.forks .lab', '.xr .lab', 'h3 small', '.tocs', '.vol .lab', '.wl .v']
DISPLAY_TIGHT = 'h1, .thesis, .cover .title, .poster .giant, .tier .n, .days .n, .dayrow .n, .card.front .g, .seven .n, .g, .photo.duo .dw .word'
DISPLAY = 'h2, h3, .poster .big, .stack .opt, .forks .q, .sideq .big19, .ribbon .opt, .fail .head, .tier .h, .seven .c, .trip .tname, .trip .day b, .fb .it .w, .toc .num, .days .t, .dayrow .h, .rules2 .big, .foot .big'
CSS = f"""
/* studio — Marta's rulings on Brunner's proof (desk.md, 2026-10-25) */
{CAPTIONS}{{ text-transform:none !important; letter-spacing:.01em !important; }}
.lc, .stack .it .v.lc, .stack .it.pick .v.lc{{ text-transform:none !important; letter-spacing:.02em !important; }}
{DISPLAY_TIGHT}{{ word-spacing:.16em; }}
{DISPLAY}{{ word-spacing:.09em; }}
.toc .fsrow{{ display:grid; grid-template-columns:52px 1fr auto; column-gap:16px; }}
"""
def studio(html):
    html = html.replace('</style>', CSS + 'a.pref{ color:inherit; text-decoration:none; } a.pref::after{ content:attr(data-page); }\n</style>', 1)
    # the shipped edition printed "Failure modes, p. ○" (a counter that never resolved): a real link, numbered at render
    try:   # the cover counts the pages it ships with (the last render's page map; one more render settles it)
        n = len(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_pages-affiche.json'))))
        html = re.sub(r'\b\d{2} pages · 7 decisions', f'{n} pages · 7 decisions', html)
    except Exception: pass
    html = us_house(html)
    sp = BeautifulSoup(html, 'html.parser')
    # a paragraph or a display line never ends on one word: the last two words travel together (each nine letters or fewer)
    for el in sp.select('p, li, h1, h2, h3, .sf, .thesis, .big, .big19, .q, .c, .h, .opt, .tname, .head, .t'):
        if el.find_parent('svg') or el.find(['p', 'li', 'div']): continue
        ts = [x for x in el.find_all(string=True) if x.strip()]
        if not ts: continue
        last = ts[-1]; m = re.search(r'(\S{1,12}) (\S{1,14}\s*)$', str(last))
        if m and not str(last).endswith('\u00a0'): last.replace_with(str(last)[:m.start()] + m.group(1) + '\u00a0' + m.group(2))
    for tx in sp.select('svg text, svg tspan'):   # durations on a figure: 1 h, 38 min (house style), never 1h / 38m
        for n in tx.find_all(string=True, recursive=False):
            new = re.sub(r'\b(\d+)h\b', r'\1 h', re.sub(r'\b(\d+)m\b', r'\1 min', str(n)))
            if new != str(n): n.replace_with(new)
    # text typed in capitals (figure titles, a transcribed label) over six words: sentence case, names kept
    _all = sp.get_text(' ')
    # a name: a capital mid-sentence on a word never written in lower case
    _low = set(re.findall(r"\b[a-zà-ü’']+\b", _all))
    NAMES = {w for w in re.findall(r"(?<=[a-z,;] )[A-Z][a-zà-ü’']+", _all) if w.lower() not in _low} | {w for w in re.findall(r"\b[A-Z]*\d[A-Z0-9]*\b", _all)}   # a capital mid-sentence is a name; codes with digits (R5, T1) stay
    def _sent(t):
        def fix(m):
            w = m.group(0); lw = w.lower()
            hit = next((n for n in NAMES if n.lower() == lw), None)
            return hit or lw
        out = re.sub(r"[A-Za-zÀ-ÿ0-9’']+", fix, t)
        return re.sub(r'^(\W*)(\w)', lambda m: m.group(1) + m.group(2).upper(), out)
    for n in list(sp.find_all(string=True)):
        tx = str(n)
        if n.parent.name in ('style', 'script'): continue
        letters = re.sub(r'[^A-Za-zÀ-ÿ]', '', tx)
        if len(tx.split()) > 6 and letters and letters.isupper(): n.replace_with(_sent(tx))
    for n in list(sp.find_all(string=True)):   # Title Case transcribed from capitals ("Costs You The Trip, Or A Whole Day"): sentence case
        tx = str(n); ws = re.findall(r"[A-Za-z’']+", tx)
        if len(ws) >= 4 and all(w[0].isupper() for w in ws) and re.search(r'\b(?:The|Or|A|You|Of|And)\b', tx) and not tx.isupper():
            n.replace_with(re.sub(r'^(\W*)(\w)', lambda m: m.group(1) + m.group(2).upper(), tx.lower()))
        elif re.search(r"’Ll\b|’S\b|’T\b", tx): n.replace_with(re.sub(r"’(Ll|S|T)\b", lambda m: '’' + m.group(1).lower(), tx))
    # nothing prints twice (fidelity TWICE): a poster foot that repeats its thesis or a paragraph of its chapter goes
    _nz = lambda t: re.sub(r'\W+', ' ', t).strip().lower()
    for sec in sp.find_all('section'):
        paras = {_nz(x.get_text(' ')) for x in sec.find_all('p') if not x.find_parent(class_='poster')}
        for po in sec.select('.poster'):
            th = po.select_one('.thesis'); th_t = _nz(th.get_text(' ')) if th else ''
            for el in po.select('.foot .big, .foot p'):
                t = _nz(el.get_text(' '))
                if t and (t == th_t or t in paras): el.decompose()
    for sel in LABELS:
        for el in sp.select(sel):
            if len(el.get_text(' ', strip=True).split()) > 6: el['class'] = (el.get('class') or []) + ['lc']
    out = str(sp)
    out = re.sub(r'Failure modes,(?:\s|\u00a0)*p\.(?:\s|\u2009|\u00a0)*(?:<i class="mk">)?○(?:</i>)?', '<a class="pref" href="#failure-modes-p">Failure modes, p.\u00a0</a>', out)
    return out
