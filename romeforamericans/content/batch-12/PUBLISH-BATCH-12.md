# Batch 12 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-12.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-12-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-12-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-12.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-12.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen; hero loads; renders cleanly.
Then publish via admin.

## ★ Currency note — ETIAS (will date)
The packing article states the CURRENT (mid-2026) entry status: US citizens need only a valid
passport; ETIAS is NOT yet required (delayed to late 2026); "check official status before travel."
Verified vs official EU sources. This WILL change when ETIAS launches — re-verify before any
major site refresh. All three AIs confirmed the current handling is correct.

## Re-check outcome
Grok + DeepSeek clean on all 6; Gemini flagged 2 (both fair, both applied):
- Dress code: tightened the bottom-line scarf line (a scarf covers shoulders, not knees) to
  match the article's own earlier, accurate advice.
- Packing: sharpened the ETIAS closing line so it doesn't imply ETIAS can currently derail a
  trip (only the passport can right now); kept the "check before you travel" caution.
No factual errors found; eSIM + ETIAS + tipping all verified accurate.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)
  - Note: all 6 of these are pure info/etiquette — NO affiliate slots by design.

## Articles in this batch
1. italian-etiquette-for-americans (etiquette-and-culture)
2. what-to-wear-rome-dress-code (etiquette-and-culture)
3. what-to-pack-for-rome (packing-and-connectivity)
4. esim-sim-wifi-rome (packing-and-connectivity)
5. basic-italian-phrases-rome (etiquette-and-culture)
6. cash-cards-tipping-rome (money-and-costs)

## Done when
- [ ] 6 heroes uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
