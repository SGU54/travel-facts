import json, re
exec(open('mine.py').read().split("by = collections.defaultdict")[0])

# the organising fact's four component facts
F = {
 'trip shape: two bases / two long legs': r'two bases|two cities|two long (journeys|legs)|one shinkansen ride|base in just two',
 'pass break-even needs ~4 legs':         r'break.?even|pays for itself|four long|4 long|worth it for your|don.t buy it by default',
 'the Oct-2023 price rise (why advice is stale)': r'price (rise|increase)|rose from|¥29,650|29,650|no longer pays|since the price',
 'day trips run on LOCAL lines, not the pass': r'day trip',
}
hits = {}
for k, rx in F.items():
    r = re.compile(rx, re.I)
    hits[k] = {a['slug'] for a in arts if r.search(plain(a))}
    print(f"  {len(hits[k]):>3} / {len(arts)} articles — {k}")

sets = list(hits.values())
allfour = set.intersection(*sets)
anythree = {s for s in set.union(*sets) if sum(s in h for h in sets) >= 3}
print(f"\n  articles joining ALL FOUR: {len(allfour)}  {sorted(allfour) if allfour else ''}")
print(f"  articles joining any THREE: {len(anythree)}  {sorted(anythree)}")
print(f"\n  → the facts are everywhere; the CONNECTION is in {len(allfour)} of {len(arts)} articles.")
