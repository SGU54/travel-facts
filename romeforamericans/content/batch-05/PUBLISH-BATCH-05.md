# Batch 5 — Publishing guide

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-05.json` — 5 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-05-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 5 heroes per `batch-05-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-05.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-05.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (no ticket/pass prices
frozen — all "check current"); hero image loads; renders cleanly. Then publish via admin.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)
  - Note: common-scams-in-rome has NO affiliate slot by design (trust-builder).

## Articles in this batch
1. common-scams-in-rome (safety-and-scams)
2. best-neighborhoods-to-stay-rome (best-areas-to-stay)
3. skip-the-line-tickets-rome (tickets-and-passes)
4. roma-pass-omnia-card-worth-it (tickets-and-passes)
5. trastevere-after-dark (trastevere)

## Done when
- [ ] 5 heroes uploaded to Cloudinary
- [ ] 5 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
