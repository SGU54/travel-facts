# -*- coding: utf-8 -*-
"""atelier-loop.py — model 2: the maquettiste looks at every rendered page and
reaches for a lever, until no page breaks a rule or the levers run out.

  compose (briefs + levers) → render → read _pages.json → decide → repeat

Rules a page must satisfy (atelier/references/gates.md, model 2):
  R1  no chapter end-piece alone on a page         (closeblock in compose; measured here)
  R2  no prose page with an empty margin           → reserve item / detail crop / wide
  R3  no chapter's last page under 60 % fill       → closing plate (fill pass sizes it)
  R4  no stub before a decision's hero             → prose moves after the hero
  R5  no page under 40 % that is not a designed closer

Usage: python3 atelier-loop.py [build-dir] [--max 4]
"""
import json, os, subprocess, sys

BUILD = os.path.abspath(next((a for a in sys.argv[1:] if not a.startswith('--')), os.path.dirname(os.path.abspath(__file__))))
MAX = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else 4
os.chdir(BUILD)
TOP, BOT = 92, 984          # the body column on the sheet
H = BOT - TOP

def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:]); raise SystemExit(f'failed: {cmd}')
    return r.stdout

def load_levers():
    return json.load(open('levers.json')) if os.path.exists('levers.json') else {}

def save_levers(L):
    json.dump(L, open('levers.json', 'w'), indent=1, ensure_ascii=False)

def dp_index(dp):
    try: return int(dp.split(':')[1])
    except Exception: return None

def analyse(pages, briefs, L):
    """Return (changed, report). Mutates L."""
    changed = False; rep = []
    chapters = briefs['chapters']
    # pages by section: last page index per section, elements per page
    last_page = {}
    for pg in pages:
        for e in pg['els']:
            if e['sec']: last_page[e['sec']] = pg['page']
    used_reserve = {sid: {m['reserve'] for m in L.get('margin', {}).get(sid, [])} for sid in chapters}

    for k, pg in enumerate(pages):
        els = pg['els']
        if not els: continue
        secs = {e['sec'] for e in els if e['sec']}
        if not secs or secs <= {'fs', 'contents'} or pg['page'] == 1: continue
        bottom = max(e['bottom'] for e in els)
        fill = (min(bottom, BOT) - TOP) / H
        prose = [e for e in els if e['tag'] == 'p' and e['left'] < 300 and 'ref' not in e['cls'] and 'cap' not in e['cls']]
        prose_px = sum(e['bottom'] - e['top'] for e in prose)
        has_mg = any('mg' in e['cls'].split() for e in els)
        has_plate = any(('photo' in e['cls'] or 'bleed' in e['cls'] or 'halfband' in e['cls']) for e in els)
        has_fig = any('figx' in e['cls'] for e in els)
        has_opener = any('opener6' in e['cls'] for e in els)
        main = max(secs, key=lambda s: sum(e['bottom'] - e['top'] for e in els if e['sec'] == s))
        b = chapters.get(main, {})
        if b.get('skip'): continue

        # R2 · a prose page whose margin is empty
        if prose_px >= 200 and not has_mg and not has_plate and not has_fig:
            starts = [e for e in prose if e['sec'] == main and not e['split'] and dp_index(e['dp']) is not None]
            if starts:
                i = dp_index(starts[0]['dp'])
                reserve = b.get('reserve', [])
                k_free = next((j for j in range(len(reserve)) if j not in used_reserve.get(main, set())), None)
                margin = L.setdefault('margin', {}).setdefault(main, [])
                if k_free is not None:
                    margin.append({'before': i, 'reserve': k_free}); used_reserve.setdefault(main, set()).add(k_free)
                    rep.append(f'p{pg["page"]} {main}: empty margin → reserve {k_free} before ¶{i}'); changed = True
                elif not any(m.get('before') == i for m in margin):
                    margin.append({'before': i, 'reserve': 99, 'pos': '20% 50%'})   # 99 = detail crop fallback
                    rep.append(f'p{pg["page"]} {main}: empty margin, reserve exhausted → detail crop before ¶{i}'); changed = True

        # R4 · a stub between a decision's page A and its hero page
        if b.get('kind') == 'decision' and not has_opener and fill < 0.40 and k + 1 < len(pages):
            nxt = pages[k + 1]['els']
            opens_hero = nxt and (('bleed' in nxt[0]['cls']) or ('pagetop' in nxt[0]['cls'])) and nxt[0]['sec'] == main
            if opens_hero and L.get('para_on_A', {}).get(main) is not False:
                L.setdefault('para_on_A', {})[main] = False
                rep.append(f'p{pg["page"]} {main}: stub before the hero ({fill:.0%}) → prose after the hero'); changed = True
                continue

        # R3 / R5 · a chapter's last page, short, with no plate closing it
        if last_page.get(main) == pg['page'] and fill < 0.60 and not has_plate and not has_opener:
            if not L.get('add_closer', {}).get(main) and main not in ('then', 'beforeyoubook', 'wallet', 'howto'):
                L.setdefault('add_closer', {})[main] = True
                rep.append(f'p{pg["page"]} {main}: last page {fill:.0%} → closing plate'); changed = True
            elif fill < 0.40 and main not in L.get('tight', []):
                L.setdefault('tight', []).append(main)
                rep.append(f'p{pg["page"]} {main}: last page {fill:.0%} with plate → tight'); changed = True

        # R1 · report (compose welds the end-pieces; this only reports a survivor)
        kinds = {e['cls'].split()[0] if e['cls'] else e['tag'] for e in els if e['sec'] == main}
        if kinds and kinds <= {'c6', 'forks', 'volrow', 'photo', 'endmark', 'closeblock'} and not prose and fill < 0.35:
            rep.append(f'p{pg["page"]} {main}: end-pieces alone ({fill:.0%}) — survived the closeblock')
    return changed, rep

def main():
    briefs = json.load(open('briefs.json'))
    L = load_levers()
    sh('python3 build-html.py')                      # fresh raw once; compose keeps re-reading it
    if os.path.exists('dossier3.raw.html'): os.remove('dossier3.raw.html')
    for it in range(1, MAX + 1):
        print(f'── iteration {it} ──')
        print(sh('python3 compose.py .').strip())
        out = sh('python3 render-both.py .')
        print('\n'.join(l for l in out.splitlines() if l.startswith('paginated') or 'page map' in l))
        pages = json.load(open('_pages-dossier.pdf.json'))
        changed, rep = analyse(pages, briefs, L)
        for r in rep: print('  ', r)
        save_levers(L)
        if not changed:
            print('clean: no lever left to pull'); break
    print('levers:', json.dumps(L, ensure_ascii=False))

if __name__ == '__main__':
    main()
