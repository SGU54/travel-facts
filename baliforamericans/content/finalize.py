#!/usr/bin/env python3
"""python3 finalize.py NN
1. Fact spans: every data-fact key must carry ONE canonical inner text across the whole site (the DB value
   replaces the span text at render). Registry: ../fact-spans.json. A mismatch stops the run.
2. Converts every <!-- IMAGE_SLOT_n: ... --> comment into a real <figure><img> via a parser (never string surgery).
3. Appends this batch's NEW fact rows to ../baliforamericans-facts.sql (append-only) and writes seed-batch-NN.json.
4. Writes publish-batch-NN.json."""
import json,os,re,sys,datetime
from bs4 import BeautifulSoup, Comment
N=sys.argv[1]; H=os.path.dirname(os.path.abspath(__file__)); B=f'{H}/batch-{N}'; ROOT=os.path.abspath(f'{H}/..')
imp=json.load(open(f'{B}/import-batch-{N}.json')); meta={m['slug']:m for m in json.load(open(f'{B}/meta.json'))}
F=json.load(open(f'{ROOT}/facts.json')); REC={r['fact_key']:r for k,v in F.items() if not k.startswith('_') for r in v.values()}
regp=f'{ROOT}/fact-spans.json'; reg=json.load(open(regp)) if os.path.exists(regp) else {}
new={}; err=0
for a in imp['articles']:
    soup=BeautifulSoup(a['content'],'html.parser')
    for sp in soup.select('span.fact[data-fact]'):
        k=sp['data-fact']; t=sp.get_text()
        if k in reg and reg[k]['text']!=t: print(f'✗ {a["slug"]}: span {k} reads "{t}" but the site value is "{reg[k]["text"]}"'); err+=1
        elif k in new and new[k]['text']!=t: print(f'✗ {a["slug"]}: span {k} has two texts in this batch: "{t}" vs "{new[k]["text"]}"'); err+=1
        elif k not in reg: new.setdefault(k,{'text':t,'first_slug':a['slug'],'batch':N})
    n=0
    for c in soup.find_all(string=lambda s:isinstance(s,Comment)):
        m=re.match(r'\s*IMAGE_SLOT_(\d+):',c)
        if not m: continue
        i=m.group(1); alt=meta[a['slug']].get(f'alt{i}'); assert alt, f'no alt{i} for {a["slug"]}'
        fig=soup.new_tag('figure'); img=soup.new_tag('img',src=f'https://img.sgfleetmedia.com/cdn-cgi/image/format=auto,width=1200/baliforamericans/articles/{a["slug"]}-{i}',alt=alt,loading='lazy'); fig.append(img); c.replace_with(fig); n+=1
    assert n==len(a['image_ids'])-1,(a['slug'],n)
    a['content']=str(soup)
if err: sys.exit(1)
assert 'IMAGE_SLOT' not in json.dumps(imp)
json.dump(imp,open(f'{B}/import-batch-{N}.json','w'),indent=1,ensure_ascii=False)
if new:
    q=lambda s:s.replace("'","''")
    sqlp=f'{ROOT}/baliforamericans-facts.sql'
    head='' if os.path.exists(sqlp) else "-- travel-facts/baliforamericans/baliforamericans-facts.sql\n-- Append-only seed of every fact spanned in baliforamericans.com articles. Idempotent upserts.\n-- scope = 'bali' = SITE.dbSchema. The DB value REPLACES the span text at render, so each key has one canonical wording.\n"
    rows=[]; blk=[f"\n-- Batch-{N} — {datetime.date.today()}\n"]
    for k,v in new.items():
        r=REC[k]; st='verified' if r['status']=='verified' and r['source_kind']=='primary' else 'provisional'
        rows.append({'scope':'bali','key':k,'value':v['text'],'status':st,'source_url':r['source_url']})
        blk.append(f"-- {k} — {v['first_slug']}\ninsert into common.facts (scope, key, value, status, checked_at, source_url)\nvalues ('bali', '{k}', '{q(json.dumps(v['text'],ensure_ascii=False))}'::jsonb, '{st}', now(),\n        '{q(r['source_url'])}')\non conflict (scope, key) do update set\n  value = excluded.value, status = excluded.status,\n  checked_at = excluded.checked_at, source_url = excluded.source_url;\n")
    open(sqlp,'a').write(head+'\n'.join(blk)); json.dump(rows,open(f'{B}/seed-batch-{N}.json','w'),indent=1,ensure_ascii=False)
    reg.update(new); json.dump(reg,open(regp,'w'),indent=1,ensure_ascii=False)
json.dump({'preserve_status':False,'allow_create':False,'articles':[{'slug':a['slug'],'status':'published'} for a in imp['articles']]},open(f'{B}/publish-batch-{N}.json','w'),indent=1)
print(f'✓ batch {N}: {len(new)} new fact keys, figures converted, publish file written')
