# Batch 8 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-08.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-08-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-08-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-08.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-08.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (attraction/train/tour prices
"check current"; the one €1.50 ATAC fare carries a check-current caveat); hero image loads;
renders cleanly. Then publish via admin.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)

## Articles in this batch (all day-trips category)
1. tivoli-day-trip
2. ostia-antica-day-trip
3. orvieto-day-trip
4. florence-day-trip-from-rome
5. castelli-romani-day-trip
6. naples-from-rome

## Done when
- [ ] 6 heroes uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
