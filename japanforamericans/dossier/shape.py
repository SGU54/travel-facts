import json, re, collections
exec(open('mine.py').read().split("by = collections.defaultdict")[0])

def find(rx, label, limit=6):
    r = re.compile(rx, re.I)
    print(f"\n── {label}")
    n=0
    for a in arts:
        for m in r.finditer(plain(a)):
            s=max(0,m.start()-110); e=min(len(plain(a)),m.end()+110)
            print(f"   [{a['slug'][:34]:<34}] …{plain(a)[s:e].strip()}…")
            n+=1
            if n>=limit: return

find(r'two long (journeys|legs)|two bases|one long leg|two cities', 'trip shape: how many legs/bases')
find(r'(four|4) (long )?(journeys|legs)|break.?even|pays for itself', 'the pass break-even')
find(r'day trip', 'day trips as the unit', 4)
