# batch-10 — greeceforamericans (remaining tier-1 pages)

5 articles: best-caldera-view-hotels-santorini, most-romantic-greek-islands, best-greek-islands-for-families, greece-trip-cost-from-us, santorini-to-mykonos.
With this batch, ALL tier-1 money pages are written. Status: WRITTEN. cloud=dsrkwieur, affiliate slots + disclosure, 15 images.

## ⚠ Scope note
The romantic + families articles were rewritten to stay IN SCOPE (Santorini/Mykonos/Crete/Naxos/Paros + Athens only).
Earlier drafts had drifted to Milos/Folegandros/Rhodes (not in facts.json) — now removed. The second gate re-checks this.
The cost article deliberately uses ranges/levers, NOT fixed prices (served live).

## Next
1. SECOND GATE: paste second-gate-prompt.txt into 1–2 models (checks scope + no-frozen-prices); send findings.
2. Images: 15 per batch-10-images.md (named 01..15), then
   CLOUDINARY_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-10.json  (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-10.json   (draft)
4. links → affiliates → review → publish.
