import json, re, collections
exec(open('mine.py').read().split("by = collections.defaultdict")[0])  # reuse loaders

by = collections.defaultdict(list)
for a in arts:
    c = a.get('category_slug') or (a.get('category') or {}).get('slug') or '?'
    by[c].append(a)
CW = {c: sum(W(a) for a in v) for c, v in by.items()}

CAND = [
 ("how many bases, and in what order",      ['itineraries-by-length','first-timer-itineraries','itineraries','day-trips','plan-your-trip']),
 ("eating well without the reservation system", ['what-to-eat','where-to-eat','food-and-drink']),
 ("which sights actually earn the day",     ['things-to-do','temples-and-shrines']),
 ("where to sleep: ryokan, hotel, or neither", ['where-to-stay','ryokan-and-onsen']),
 ("where to base yourself in Tokyo",        ['tokyo-neighborhoods','tokyo']),
 ("when to come / which weeks to avoid",    ['when-to-go']),
 ("does the rail pass pay for itself",      ['trains-and-jr-pass','getting-around']),
 ("paying for transit: card, pass or ticket",['local-transit-ic-cards']),
 ("the admin layer before you fly",         ['visas-and-documents','connectivity','money-and-costs','safety-and-health','etiquette-and-culture']),
 ("which airport, and getting out of it",   ['flights-and-arrival','airports-and-transfers']),
 ("Kyoto: where to stay and how to move",   ['kyoto-neighborhoods','kyoto']),
]
def verdict(w): return 'STRONG' if w > 9000 else ('VIABLE' if w >= 5500 else 'THIN')

print("═══ DECISION SHORTLIST ═══")
rows = []
for name, cats in CAND:
    w = sum(CW.get(c,0) for c in cats)
    rows.append((w, name, cats, verdict(w)))
for w, name, cats, v in sorted(rows, reverse=True):
    print(f"  {v:<7} {w:>6,}w   {name}")
    print(f"          ← {', '.join(cats)}")
print()
strong = [r for r in rows if r[3]=='STRONG']; viable=[r for r in rows if r[3]=='VIABLE']; thin=[r for r in rows if r[3]=='THIN']
print(f"  {len(strong)} STRONG · {len(viable)} VIABLE · {len(thin)} THIN")
print(f"  buildable decisions: {len(strong)+len(viable)}")
print(f"  words in buildable decisions: {sum(r[0] for r in strong+viable):,} of {sum(CW.values()):,} ({100*sum(r[0] for r in strong+viable)//sum(CW.values())}% of corpus)")
print("\n  REFUSALS (THIN — do not write, they will pad):")
for w,name,cats,v in sorted(thin, reverse=True): print(f"    {w:>6,}w  {name}")
