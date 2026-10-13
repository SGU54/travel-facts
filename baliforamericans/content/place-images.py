#!/usr/bin/env python3
"""python3 place-images.py 01   reads batch-NN/picks.json {object-suffix: "candfile-stem" | [stem, batchdir]}
Copies picks to the volume's batch-NN/images/ as NN_<key>.jpg in the import file's order (hero, then body, per article),
re-encodes to max 2000px JPEG q85, and records the Unsplash ids in used-images.json."""
import json,os,sys
from PIL import Image
N=sys.argv[1]; H=os.path.dirname(os.path.abspath(__file__)); V='/Volumes/Untitled/travel-facts/baliforamericans/content'
picks=json.load(open(f'{H}/batch-{N}/picks.json')); arts=json.load(open(f'{H}/batch-{N}/import-batch-{N}.json'))['articles']
used=json.load(open(f'{H}/used-images.json')) if os.path.exists(f'{H}/used-images.json') else []
out=f'{V}/batch-{N}/images'; os.makedirs(out,exist_ok=True)
for f in os.listdir(out): os.remove(f'{out}/{f}')
i=0; credits=[]
for a in arts:
    for full in a['image_ids']:
        key=full.split('/')[-1]; p=picks[key]; stem,bd=(p,N) if isinstance(p,str) else p
        src=f'{V}/batch-{bd}/cand/{stem}.jpg'; man=json.load(open(f'{V}/batch-{bd}/cand/manifest.json'))
        k,n=stem.rsplit('__',1); e=next(x for x in man[k] if x['n']==int(n))
        i+=1; im=Image.open(src).convert('RGB'); im.thumbnail((2000,2000)); dest=f'{out}/{i:02d}_{key}.jpg'; im.save(dest,quality=85,optimize=True)
        used.append(e['id']); credits.append({'key':key,'unsplash_id':e['id'],'by':e['by'],'page':e['page'],'desc':e['desc']})
        print(f'{i:02d} {key}  <- {e["id"]} by {e["by"]}  {os.path.getsize(dest)//1024} KB')
json.dump(sorted(set(used)),open(f'{H}/used-images.json','w'),indent=0)
json.dump(credits,open(f'{H}/batch-{N}/image-credits.json','w'),indent=1,ensure_ascii=False)
