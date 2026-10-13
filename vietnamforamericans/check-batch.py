#!/usr/bin/env python3
"""Pre-gate guards for a vietnamforamericans batch. Catches the defect classes the
second gate has found repeatedly, so they never reach the gate (or a live page).

  python3 check-batch.py content/batch-NN/import-batch-NN.json
"""
import json,re,sys,glob,os,collections
BASE=os.path.dirname(os.path.abspath(__file__))
P=sys.argv[1]; fails=[]; warns=[]
b=json.load(open(P))

# 1. WITHHOLDING — refusing the reader's core answer is an automatic TRUST 0.
#    Hit twice (batch 2 money/tipping, batch 4 flights/domestic-flights).
WITHHOLD=[r"we (are not going to|will not|deliberately do not|do not) (print|quote|give|list)",
          r"quoting figures here would be", r"a number frozen in (an|this) article",
          r"no point (printing|quoting)", r"we are not printing"]
for a in b['articles']:
    txt=re.sub(r'<[^>]+>',' ',a['content'])
    for pat in WITHHOLD:
        m=re.search(pat,txt,re.I)
        if m: fails.append(f"WITHHOLDING  {a['slug']}: \"{txt[max(0,m.start()-60):m.start()+90].strip()}\"")

# 1b. TITLE-PROMISE REFUSAL — the strongest form of withholding. A title that
#     promises a list, a price or a pick, answered with a refusal. (batch 7)
PROMISE=re.compile(r"\b(best|top|which|how much|cost|price|cheapest)\b", re.I)
REFUSE=[r"rather than nam\w+", r"we (will not|do not|are not going to) (name|list|rank|recommend)",
        r"nam\w+ no \w+", r"this (article|guide) (will not|does not) (name|list|rank)"]
for a in b['articles']:
    if not PROMISE.search(a['title']): continue
    txt=re.sub(r'<[^>]+>',' ',a['content'])
    for pat in REFUSE:
        m=re.search(pat,txt,re.I)
        if m: fails.append(f"TITLE-PROMISE {a['slug']}: title promises a pick but body says \"{txt[max(0,m.start()-50):m.start()+100].strip()}\"")

# 2. CERTAINTY ESCALATION on claims the fact layer qualifies.
HEDGED={'may not pay':'insurance', 'you will likely':'overstay', 'can run empty':'ATMs'}
ABS=[r"\bvoids insurance\b", r"\bguarantee[sd]?\b.{0,40}\bsafe", r"\bnobody will be offended\b",
     r"\bis entirely avoidable\b", r"\bthe single most common\b", r"\balways sells? out\b",
     r"\bthe leading cause of\b"]
for a in b['articles']:
    txt=re.sub(r'<[^>]+>',' ',a['content'])+' '+a.get('excerpt','')
    for pat in ABS:
        m=re.search(pat,txt,re.I)
        if m: fails.append(f"CERTAINTY    {a['slug']}: \"{txt[max(0,m.start()-70):m.start()+80].strip()}\"")

# 3. ONE FACT KEY -> ONE DISPLAY TEXT, across the whole published corpus.
seen=collections.defaultdict(set)
for f in sorted(glob.glob(f"{BASE}/content/batch-*/import-batch-*.json")):
    for a in json.load(open(f))['articles']:
        for m in re.finditer(r'data-fact="([^"]+)">([^<]+)</span>',a['content']):
            seen[m.group(1)].add(m.group(2))
for k,v in seen.items():
    if len(v)>1: fails.append(f"SPAN CLASH   {k}: {sorted(v)}")

# 4. Spanned keys must exist in facts.json.
facts=json.load(open(f"{BASE}/facts.json")); keys=set()
def walk(n):
    if isinstance(n,list): [walk(x) for x in n]
    elif isinstance(n,dict):
        if 'fact_key' in n and 'value' in n: keys.add(n['fact_key']); return
        [walk(v) for v in n.values()]
walk(facts)
for k in seen:
    if k not in keys: fails.append(f"UNKNOWN KEY  {k} spanned but absent from facts.json")

# 5. Word count against the doctrine band.
for a in b['articles']:
    w=len(re.sub(r'<[^>]+>',' ',a['content']).split())
    if not (800<=w<=1600): fails.append(f"LENGTH       {a['slug']}: {w} words outside 800-1600")

# 6. EXCERPT GUARD. Two defects shipped past this script in batch 16 because it only read
#    a.content. The excerpt is a promise the body has to keep, and nothing else checks it.
NUMWORD=r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|fifty|hundred)"
PRICE=[rf"\b(?:less|more)\s+than\s+(?:a|an|{NUMWORD}|\d)[\w\s-]{{0,12}}\b(?:dollar|cent|buck|euro|pound)s?\b",
       r"[$€£]\s?\d", rf"\b(?:{NUMWORD}|\d+)\s+dollars?\b", r"\bdong\b.{0,12}\d", r"\b\d[\d,]*\s*(?:dong|VND|USD)\b"]
ABSX=[r"\bonly exists?\b", r"\bnowhere else\b", r"\bnever\b", r"\balways\b", r"\bevery\b", r"\bthe only\b"]
COUNT=re.compile(rf"\b({NUMWORD}|\d+)\s+(dishes|parts|areas|ways|versions|options|reasons|things|places|stops)\b", re.I)
for a in b['articles']:
    ex=a.get('excerpt','') or ''
    body=re.sub(r'<[^>]+>',' ',a['content'])
    for pat in PRICE:
        m=re.search(pat,ex,re.I)
        if m: fails.append(f"EXCERPT PRICE {a['slug']}: \"{m.group(0)}\" — excerpts are prose; no frozen prices")
    for pat in ABSX:
        m=re.search(pat,ex,re.I)
        if m: warns.append(f"EXCERPT ABS   {a['slug']}: \"{m.group(0)}\" — absolute in excerpt, check the body agrees")
    m=COUNT.search(ex)
    if m: warns.append(f"EXCERPT COUNT {a['slug']}: promises \"{m.group(0)}\" — count them in the body by hand")
    if len(ex.split())>45: fails.append(f"EXCERPT LONG {a['slug']}: {len(ex.split())} words")
    if not ex.strip(): fails.append(f"EXCERPT NONE {a['slug']}")

print(f"checked {len(b['articles'])} articles, {len(seen)} distinct fact keys")
if warns:
    print(f"\n{len(warns)} THING(S) TO CHECK BY HAND (not failures):"); [print("  "+w) for w in warns]
if fails:
    print(f"\n{len(fails)} PROBLEM(S):"); [print("  "+f) for f in fails]; sys.exit(1)
print("all guards passed")
