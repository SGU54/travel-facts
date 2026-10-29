#!/usr/bin/env python3
"""dash-pass.py — bring an over-dashed manuscript under the ai-smell threshold.

Rome prints 19.2 em-dashes per 1,000 words of prose against a gate threshold of
8.0 — more than twice the next book in the fleet. The dash is doing three
different jobs and the reader cannot tell which: a parenthetical aside, a
colon's announcement, and a comma's pause.

This converts by JOB, not by position:
  · a matched PAIR around an aside      → parentheses, or commas if the aside
                                          carries no comma of its own
  · a single dash before which/and/but… → a comma (it was a pause)
  · a single dash before a clause that  → a colon, but only if the sentence does
    explains the one before it            not already carry one

That last guard exists because the equivalent pass on Greece produced seven
sentences ending in two colons: the rule fired on sentences that already had
one. Everything here is dry-runnable and every edit is verified afterwards.

Run:  python3 dash-pass.py <build-dir> [--apply] [--target N]
"""
import os, re, sys, html as _html

LEAD_COMMA = re.compile(r'^(which|and|but|so|or|because|though|while|whereas|'
                        r'not|with|for|after|before|then|though)\b', re.I)
# What, following a parenthetical, means a clause is resuming rather than a
# predicate continuing. Verbs are deliberately absent: "(…) are twenty minutes"
# must not take a comma.
CLAUSE_AFTER = re.compile(r'^(and|but|or|yet|so|which|who|because|though|'
                          r'although|while|whereas|when|we|you|they|it)\b', re.I)


def prose_paragraphs(doc):
    """The exact <p> blocks the ai-smell gate reads: inside a .dec/.dec chap
    section, not inside a table, figure or svg, at least five words."""
    spans = []
    for m in re.finditer(r'<(?:section|div)\s+class="((?:dec chap|dec)[^"]*)"[^>]*>(.*?)'
                         r'(?=<(?:section|div)\s+class="(?:dec chap|dec)\b|$)', doc, re.S):
        base = m.start(2)
        body = m.group(2)
        blocked = []
        for bm in re.finditer(r'<table.*?</table>|<figure.*?</figure>|<svg.*?</svg>',
                              body, re.S):
            blocked.append((bm.start(), bm.end()))
        for pm in re.finditer(r'<p[^>]*>(.*?)</p>', body, re.S):
            if any(s <= pm.start(1) < e for s, e in blocked):
                continue
            txt = " ".join(_html.unescape(re.sub(r'<[^>]+>', '', pm.group(1))).split())
            if len(txt.split()) >= 5:
                spans.append((base + pm.start(1), base + pm.end(1)))
    return spans


def convert_sentence(s, mode):
    """mode: 'pairs' | 'singles'. Returns (new_sentence, dashes_removed)."""
    n = s.count('—')
    if n == 0:
        return s, 0
    if mode == 'pairs':
        if n < 2:
            return s, 0
        out, removed = s, 0
        # take dashes two at a time, left to right
        while out.count('—') >= 2:
            i = out.index('—')
            j = out.index('—', i + 1)
            aside = out[i + 1:j].strip()
            if not aside or len(aside.split()) > 16:
                break
            left = out[:i].rstrip()
            right = out[j + 1:].lstrip()
            if ',' in aside:
                # Whether the closing dash was also a clause boundary decides
                # whether a comma replaces it. Two shapes hide here:
                #   "a hard fact — a fare, a rule — we mark it"   → boundary, comma
                #   "those sights — the Colosseum, … — are 20 min" → apposition, NO
                # Adding one unconditionally put a comma between every subject and
                # its verb ("the sights (…), are"). Only a conjunction, relative
                # pronoun or pronoun subject after the aside marks a real boundary.
                sep = ',' if CLAUSE_AFTER.match(right) else ''
                new = f'{left} ({aside}){sep} {right}'
            else:
                new = f'{left}, {aside}, {right}'
            out, removed = new, removed + 2
        return out, removed
    # singles
    if n != 1:
        return s, 0
    i = s.index('—')
    left, right = s[:i].rstrip(), s[i + 1:].lstrip()
    if not right or not left:
        return s, 0
    if LEAD_COMMA.match(right):
        return f'{left}, {right}', 1
    if ':' in s or ';' in s:
        return f'{left}, {right}', 1
    return f'{left}: {right}', 1


def process(text, budget, mode):
    """Convert sentences in `text` until `budget` dashes are removed."""
    parts = re.split(r'((?<=[.!?])\s+)', text)
    removed = 0
    for k in range(0, len(parts), 2):
        if removed >= budget:
            break
        new, r = convert_sentence(parts[k], mode)
        if r:
            parts[k] = new; removed += r
    return ''.join(parts), removed


DEFECTS = [(r',\s*,', 'double comma'), (r':\s*:', 'double colon'),
           (r',\s*:', 'comma-colon'), (r':\s*,', 'colon-comma'),
           (r'\(\s*\)', 'empty parens'), (r'\s+[,.;:]', 'space before punctuation'),
           (r'\(\s', 'space after ('), (r'\s\)', 'space before )'),
           (r'[a-z]\(', 'no space before ('), (r':\s*[.!?]', 'colon then stop'),
           (r'\(\s*[a-z][^)]*$', 'unclosed paren')]


def main():
    build = os.path.abspath(sys.argv[1])
    apply = '--apply' in sys.argv
    target = int(sys.argv[sys.argv.index('--target') + 1]) if '--target' in sys.argv else 70
    p = os.path.join(build, 'dossier3.html')
    doc = open(p, encoding='utf-8').read()
    spans = prose_paragraphs(doc)
    total = sum(doc[a:b].count('—') for a, b in spans)
    words = sum(len(re.sub(r'<[^>]+>', '', doc[a:b]).split()) for a, b in spans)
    print(f'  {len(spans)} prose paragraphs · {words} words · {total} em-dashes '
          f'({1000*total/words:.1f}/1k) · target {target} ({1000*target/words:.1f}/1k)')
    need = total - target
    if need <= 0:
        print('  already under target'); return 0

    # pass 1: pairs (two dashes per edit), then pass 2: singles
    new_doc, done, log = doc, 0, []
    for mode in ('pairs', 'singles'):
        out, shift = [], 0
        cur = new_doc
        for a, b in spans:
            a2, b2 = a + shift, b + shift
            seg = cur[a2:b2]
            if done >= need:
                continue
            fixed, r = process(seg, need - done, mode)
            if r:
                cur = cur[:a2] + fixed + cur[b2:]
                shift += len(fixed) - len(seg)
                done += r
                log.append((mode, r, re.sub(r'<[^>]+>', '', fixed)[:90]))
        new_doc = cur
        # spans have moved; recompute for the second pass
        spans = prose_paragraphs(new_doc)
    left = sum(new_doc[a:b].count('—') for a, b in spans)
    print(f'  removed {done} → {left} remain ({1000*left/words:.1f}/1k)')

    bad = []
    for a, b in spans:
        seg = _html.unescape(re.sub(r'<[^>]+>', '', new_doc[a:b]))
        for rx, name in DEFECTS:
            for m in re.finditer(rx, seg):
                bad.append((name, seg[max(0, m.start()-55):m.end()+35]))
    print(f'  defect scan: {len(bad)} suspect sites')
    for name, ctx in bad[:12]:
        print(f'    ! {name}: …{ctx.strip()}…')
    # sentence count must not change
    def nsent(x):
        return len(re.findall(r'[.!?](?:\s|$)', _html.unescape(re.sub(r'<[^>]+>', '', x))))
    before = sum(nsent(doc[a:b]) for a, b in prose_paragraphs(doc))
    after = sum(nsent(new_doc[a:b]) for a, b in spans)
    print(f'  sentences: {before} → {after} {"OK" if before == after else "CHANGED — investigate"}')
    for mode, r, sample in log[:6]:
        print(f'    [{mode}] -{r}  {sample}…')

    if apply and not bad and before == after:
        open(p, 'w', encoding='utf-8').write(new_doc)
        print('  APPLIED')
    elif apply:
        print('  NOT APPLIED — defects or sentence drift; fix the rules first')
        return 1
    else:
        print('  dry run only (pass --apply)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
