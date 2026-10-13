#!/bin/zsh
# ./links.sh — plan internal links, drop junk anchors (links-deny.json + any single word), inject.
set -e; H=${0:A:h}; SITE=/Users/sg54/Desktop/travel-sites/baliforamericans
cd $SITE; set -a; source apps/admin/.env.local; set +a; export SUPABASE_URL=$NEXT_PUBLIC_SUPABASE_URL
node scripts/pick-links.mjs --plan $H/../article-list.json --apply 2>&1 | tail -2
python3 - <<PY
import json
p='scripts/links-map.json'; m=json.load(open(p)); deny=set(json.load(open('$H/links-deny.json')))
m2=[x for x in m if x['phrase'].lower() not in deny and len(x['phrase'].split())>1]
extra=json.load(open('$H/links-extra.json')); have={x['phrase'].lower() for x in m2}; m2+=[x for x in extra if x['phrase'].lower() not in have]
json.dump(m2,open(p,'w'),indent=1,ensure_ascii=False); print(len(m),'->',len(m2)); [print('  ',x['phrase'],'->',x['slug']) for x in m2]
PY
node scripts/inject-links.mjs --apply 2>&1 | tail -1
