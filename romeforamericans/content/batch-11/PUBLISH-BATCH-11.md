# Batch 11 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-11.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-11-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-11-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-11.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-11.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen; hero image loads; renders
cleanly. Then publish via admin.

## ★ Important currency note — the Trevi Fountain
The Trevi article reflects the NEW 2026 system (verified vs CNN + official sources, Feb 2026):
- The PIAZZA stays free to view anytime.
- The close-up BASIN area is a ticketed, crowd-controlled zone with a small fee, ~9am–10pm.
- After 10pm the barriers open and the basin is FREE for all (the key insider tip).
All three AIs confirmed this is accurate — do not "revert" it to an all-free description.
This is the kind of fact that dates: re-verify the fee/hours before any major site refresh.

## Re-check outcome
Grok + DeepSeek clean on all 6; Gemini flagged 2 (both fair, both applied): made Route 5
consistent with the Trevi fee (mostly-free, basin free after 10pm), and softened the Spanish
Steps fine wording to "check current." No factual errors found.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)

## Articles in this batch
1. trevi-fountain-guide (piazzas-and-fountains)
2. piazza-navona-guide (piazzas-and-fountains)
3. spanish-steps-guide (piazzas-and-fountains)
4. walking-rome-guide (walking-rome)
5. most-beautiful-piazzas-rome (piazzas-and-fountains)
6. best-walking-routes-rome (walking-rome)

## Done when
- [ ] 6 heroes uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
