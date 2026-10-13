# batch-01 — greeceforamericans (Stage 4 — finishing)

Body images FIXED (cloud=dsrkwieur, folder=greeceforamericans). Now adds internal links + affiliates.

## What changed in this drop
- import-batch-01.json: affiliate slots converted to Barcelona format
  (<!-- AFFILIATE_SLOT: program=… context="…" -->) + mandatory disclosure paragraph in each.
- links-map.json → put in scripts/ (33 anchor phrases; batch-1 slugs live now, future slugs skipped until they exist).
- site.ts → replace packages/config/site.ts. Adds affiliates.disclosure + fixes cloud default to 'dsrkwieur'.

## Finish the batch (repo root)
1. Re-import the articles (adds affiliate slots + disclosure to the live rows):
     node scripts/articles-batch.mjs update <path>/import-batch-01.json
2. Internal links (links-map.json already in scripts/):
     node scripts/inject-links.mjs            # dry run — review
     node scripts/inject-links.mjs --apply
3. Affiliate slots render via the admin/affiliate step using THIS site's IDs
   (program + context are in the comments; never hardcode another site's ID).
4. Final review in admin → keep DRAFT until you're happy → PUBLISH.
5. First batch only: submit /sitemap.xml in Google Search Console.
