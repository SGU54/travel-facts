#!/bin/zsh
# ./ship.sh NN  — seed this batch's new fact rows, publish its articles, run the image gate. Keys come from the site's env file.
set -e; N=$1; H=${0:A:h}; SITE=/Users/sg54/Desktop/travel-sites/baliforamericans; B=$H/batch-$N
cd $SITE; set -a; source apps/admin/.env.local; set +a
if [ -f $B/seed-batch-$N.json ]; then
  python3 -c "
import json,datetime
rows=json.load(open('$B/seed-batch-$N.json')); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump([{**r,'checked_at':now} for r in rows],open('$B/.seed.tmp','w'))"
  curl -s -o /dev/null -w "seed upsert: %{http_code}\n" -X POST "$NEXT_PUBLIC_SUPABASE_URL/rest/v1/facts?on_conflict=scope,key" -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" -H "Content-Profile: common" -H "Content-Type: application/json" -H "Prefer: resolution=merge-duplicates" --data @$B/.seed.tmp; rm -f $B/.seed.tmp
fi
curl -s -I "$NEXT_PUBLIC_SUPABASE_URL/rest/v1/facts?select=key&scope=eq.bali" -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" -H "Accept-Profile: common" -H "Prefer: count=exact" | grep -i content-range
node scripts/articles-batch.mjs update $B/publish-batch-$N.json --set-status --no-create 2>&1 | grep -E "updated|error"
node scripts/check-images.mjs 2>&1 | grep -E "manquante|existent|Articles"
curl -s -I "$NEXT_PUBLIC_SUPABASE_URL/rest/v1/articles?select=slug&status=eq.published" -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" -H "Accept-Profile: bali" -H "Prefer: count=exact" | grep -i content-range
