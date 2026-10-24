# Batch 4 — Publishing guide

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-04.json` — 5 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-04-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 5 heroes per `batch-04-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-04.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-04.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (transit/pass prices,
daily budgets, exchange rate all "check current"); hero image loads; renders cleanly.
Then publish via the admin.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)

## Articles in this batch
1. getting-around-rome-overview (getting-around-basics)
2. rome-transport-tickets-roma-pass (metro-bus-tram)
3. rome-taxis-guide (taxis-and-transfers)
4. how-much-does-rome-cost (money-and-costs)
5. best-time-to-visit-rome (when-to-go)

## Done when
- [ ] 5 heroes uploaded to R2
- [ ] 5 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
