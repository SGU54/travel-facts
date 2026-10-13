#!/usr/bin/env python3
"""state-bump.py NN — mark batch NN published in state.json (slugs from its meta.json)."""
import json,sys,pathlib
H=pathlib.Path(__file__).parent; N=sys.argv[1]
S=json.load(open(H/'../state.json')); M=json.load(open(H/f'batch-{N}/meta.json'))
slugs=[m['slug'] for m in (M if isinstance(M,list) else M.get('articles',M.values()))] if not isinstance(M,dict) or 'articles' in M else list(M.keys())
key=[k for k in S if 'published' in k and isinstance(S[k],list)][0]
S[key]=S[key]+[s for s in slugs if s not in S[key]]
S['batch']=int(N); S['batch_status']='published'
json.dump(S,open(H/'../state.json','w'),indent=1,ensure_ascii=False); print(key,len(S[key]))
