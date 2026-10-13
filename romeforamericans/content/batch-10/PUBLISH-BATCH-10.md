# Batch 10 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-10.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-10-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-10-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-10.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-10.json` to the admin import API. Lands as draft;
`category_slug`→`category_id` resolved against the DB. Re-running skips existing slugs.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (all ticket prices "check
current"; only the ~€1 Caravaggio light-box coin is stated); hero image loads; renders cleanly.
Then publish via admin.

## Re-check note (important for this batch)
This batch came back: Grok clean, DeepSeek clean, Gemini flagged 6 "frozen prices" + a "Pope
Francis" reference — ALL FABRICATED. Verified by grep: none of those strings exist in the
articles (only euro figure is the intentional ~€1 light-box coin; only Pope named is Sixtus IV
in the Capitoline founding). Gemini hallucinated quotes; all its flags were correctly rejected.
No changes were needed. The papal article deliberately says "the Pope" generically (current pope
is Leo XIV) so it won't date.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass across all batches at the end)
- Affiliate links + disclosure (one pass once programs are approved)
  - Note: papal-audience-st-peters-square has NO affiliate slot by design.

## Articles in this batch
1. st-peters-dome-climb (vatican)
2. how-early-arrive-vatican (vatican)
3. papal-audience-st-peters-square (vatican)
4. best-museums-rome-first-timers (museums-and-galleries)
5. capitoline-museums-guide (museums-and-galleries)
6. caravaggio-in-rome (museums-and-galleries)

## Done when
- [ ] 6 heroes uploaded to Cloudinary
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
