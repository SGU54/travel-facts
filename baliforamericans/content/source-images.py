#!/usr/bin/env python3
"""Source image candidates for a batch from Unsplash, refusing every paid 'Unsplash+' result.
usage: python3 source-images.py 01      (reads batch-01/image-queries.json: {object-suffix: query})
Candidates land on the VOLUME (never in the git repo): .../batch-NN/cand/<key>__<n>.jpg + manifest.json
Lesson from Vietnam: results flagged plus/premium or served from plus.unsplash.com are watermarked previews."""
import json,os,subprocess,sys,urllib.parse
N=sys.argv[1]; H=os.path.dirname(os.path.abspath(__file__))
OUT=f'/Volumes/Untitled/travel-facts/baliforamericans/content/batch-{N}/cand'; os.makedirs(OUT,exist_ok=True)
Q=json.load(open(f'{H}/batch-{N}/image-queries.json')); PER=int(sys.argv[2]) if len(sys.argv)>2 else 4
man={}
used=set(json.load(open(f'{H}/used-images.json'))) if os.path.exists(f'{H}/used-images.json') else set()
for key,query in Q.items():
    url='https://unsplash.com/napi/search/photos?query='+urllib.parse.quote(query)+'&per_page=30&orientation=landscape'
    raw=subprocess.run(['curl','-s','-H','Accept-Version: v1',url],capture_output=True,text=True).stdout
    try: res=json.loads(raw).get('results',[])
    except Exception: print(key,'SEARCH FAILED'); continue
    clean=[r for r in res if not r.get('plus') and not r.get('premium') and r['urls']['raw'].split('/')[2]=='images.unsplash.com' and r['id'] not in used and r.get('width',0)>=2400]
    man[key]=[]
    for i,r in enumerate(clean[:PER],1):
        dest=f'{OUT}/{key}__{i}.jpg'
        subprocess.run(['curl','-s','-o',dest,r['urls']['raw']+'&w=2000&fm=jpg&q=85'],check=False)
        man[key].append({'n':i,'id':r['id'],'desc':(r.get('description') or r.get('alt_description') or '')[:90],'by':r['user']['name'],'page':r['links']['html'],'w':r.get('width'),'h':r.get('height')})
    print(f'{key}: {len(clean)} clean of {len(res)} ({len(res)-len(clean)} rejected), took {len(man[key])}')
json.dump(man,open(f'{OUT}/manifest.json','w'),indent=1,ensure_ascii=False)
