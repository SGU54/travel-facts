import json, re, collections
exec(open('mine.py').read().split("by = collections.defaultdict")[0])
by = collections.defaultdict(list)
for a in arts:
    c = a.get('category_slug') or (a.get('category') or {}).get('slug') or '?'
    by[c].append(a)
CW = {c: sum(W(a) for a in v) for c, v in by.items()}
def v(w): return 'STRONG' if w > 9000 else ('VIABLE' if w >= 5500 else 'THIN')

print("═══ SECOND PASS — regrouped framings ═══\n")
MERGE = [
 ("what moving around Japan actually costs  [rail pass + transit payment]",
  ['trains-and-jr-pass','getting-around','local-transit-ic-cards']),
 ("arrival: airport, transfer, and the first 24h  [+ connectivity + money]",
  ['flights-and-arrival','airports-and-transfers','connectivity','money-and-costs']),
 ("the two cities: basing in Tokyo vs Kyoto",
  ['tokyo-neighborhoods','tokyo','kyoto-neighborhoods','kyoto']),
 ("sleeping: ryokan, hotel, and which city to spend the splurge in",
  ['where-to-stay','ryokan-and-onsen']),
 ("the pre-departure admin layer  [visa/safety/etiquette only]",
  ['visas-and-documents','safety-and-health','etiquette-and-culture']),
]
for name, cats in MERGE:
    w = sum(CW.get(c,0) for c in cats)
    print(f"  {v(w):<7} {w:>6,}w   {name}")
print("""
  → the merge that matters: rail pass + IC card transit = one decision about what it
    costs to MOVE, which is also the vein thesis. Splitting them left both marginal.
""")
