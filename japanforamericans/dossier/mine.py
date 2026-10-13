import json, re, collections

arts = json.load(open('corpus.json'))
arts = arts if isinstance(arts, list) else arts.get('articles', [])

def strip_guide(html):
    # rule: remove every span.guide AND the sentence containing it (site->product pointer,
    # not destination signal — counting it inflates whatever swamps the list guessed)
    txt = html
    # find guide spans, blank out the surrounding sentence
    for m in list(re.finditer(r'<span class="guide"[^>]*>.*?</span>', txt)):
        s = txt.rfind('.', 0, m.start()); s = 0 if s < 0 else s+1
        e = txt.find('.', m.end()); e = len(txt) if e < 0 else e+1
        txt = txt[:s] + ' ' * (e-s) + txt[e:]
    return txt

def plain(a):
    t = strip_guide(a.get('content') or '')
    return re.sub(r'<[^>]+>', ' ', t)

def W(a): return len(plain(a).split())

by = collections.defaultdict(list)
for a in arts:
    c = a.get('category_slug') or (a.get('category') or {}).get('slug') or '?'
    by[c].append(a)

print("═══ CATEGORY INVENTORY ═══")
for c in sorted(by, key=lambda k: -sum(W(a) for a in by[k])):
    print(f"  {len(by[c]):3}  {sum(W(a) for a in by[c]):6,}w  {c}")
total = sum(W(a) for a in arts)
print(f"\n  TOTAL: {total:,} words across {len(arts)} articles (guide-spans stripped)")
print(f"  YIELD ESTIMATE: {len(arts)} x 0.5 = ~{int(len(arts)*0.5)} pages")

EDGES = {
 'MONEY':      r'\b(cost|costs|price|prices|pricing|yen|¥|cheap|cheaper|expensive|save|saving|fee|fees|budget|pay|paid|fare|fares|discount|worth it|value|afford|spend|spending)\b',
 'EXTRACTION': r'\b(tourist trap|trap|markup|marked up|overcharge|overpriced|scam|commission|surcharge|upsell|rip.?off|tout|touts|inflated|gouge|hidden fee|catch)\b',
 'BREAKAGE':   r'\b(sold out|sells out|sell out|cancel|cancelled|cancellation|miss|missed|delay|delayed|closed|closes|fully booked|booked out|strand|stranded|fail|fails|failed|suspend|suspended|refuse|refused|queue|queues|stuck|unavailable|breaks down)\b',
 'EXPERIENCE': r'\b(crowd|crowded|crowds|quiet|atmosphere|memorable|disappointing|overrated|underrated|beautiful|magical|serene|authentic|worth the|special|charm|charming|rewarding)\b',
}
print("\n═══ DOMINANT EDGE (raw cue tally) ═══")
tal = {}
for name, rx in EDGES.items():
    r = re.compile(rx, re.I)
    tal[name] = sum(len(r.findall(plain(a))) for a in arts)
for name, n in sorted(tal.items(), key=lambda kv: -kv[1]):
    bar = '█' * int(40*n/max(tal.values()))
    print(f"  {name:<11} {n:>5}  {bar}")
