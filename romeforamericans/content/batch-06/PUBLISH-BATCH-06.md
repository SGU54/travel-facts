# Batch 6 — Publishing guide

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-06.json` — 5 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-06-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 5 heroes per `batch-06-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-06.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-06.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (NO hotel/room/meal prices —
all "check current"); hero image loads; renders cleanly. Then publish via admin.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)

## Articles in this batch
1. rome-in-4-days (rome-in-4-plus-days)
2. rome-in-5-7-days (rome-in-4-plus-days)
3. best-boutique-hotels-rome (hotels-and-boutique)
4. budget-stays-rome (budget-and-family)
5. where-to-eat-roman-pasta-classics (roman-dishes)

## Milestone
This batch completes ALL 29 tier-1 articles (plus 1 tier-2). Batches 7+ are tier-2 depth pieces.

## Done when
- [ ] 5 heroes uploaded to Cloudinary
- [ ] 5 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
