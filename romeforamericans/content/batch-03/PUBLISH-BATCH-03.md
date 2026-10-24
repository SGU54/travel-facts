# Batch 3 — Publishing guide

Same flow as Batch 2: images → import → review → publish. **No internal links, no
affiliates** (both deferred to end of project). From the site repo root, with
`apps/admin/.env.local` present. Schema is `rome`.

## Files
- `import-batch-03.json` — 5 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-03-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 5 heroes per `batch-03-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-03.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-03.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (all prices "check current");
hero image loads; renders cleanly. Then publish via the admin.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)

## Articles in this batch
1. roman-dishes-to-try (roman-dishes)
2. best-trattorias-rome (trattorias-and-dining)
3. best-gelato-rome (coffee-gelato-aperitivo)
4. rome-in-2-days (rome-in-1-3-days)
5. rome-in-3-days (rome-in-1-3-days)

## Done when
- [ ] 5 heroes uploaded to R2
- [ ] 5 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
