# Batch 7 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-07.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-07-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-07-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-07.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-07.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (all ticket prices/hours
"check current"); hero image loads; renders cleanly. Then publish via admin.

## Note on the Pantheon
The Pantheon article correctly states it now has PAID, TIMED entry (verified twice against
official sources — all visitors, even free-entry, must book a timed slot). If any AI re-check
flags this as "paid but not timed," that flag is wrong; keep the timed-entry wording.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)

## Articles in this batch
1. pantheon-visiting-guide (ancient-rome)
2. roman-forum-guide (ancient-rome)
3. colosseum-underground-arena-floor (ancient-rome)
4. appia-antica-guide (ancient-rome)
5. capitoline-hill-vittoriano (ancient-rome)
6. castel-santangelo-guide (vatican)

## Done when
- [ ] 6 heroes uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
