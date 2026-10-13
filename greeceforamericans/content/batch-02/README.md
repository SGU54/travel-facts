# batch-02 — greeceforamericans

5 articles: where-to-stay-Athens, greece-with-kids, luxury-greece, greece-on-a-budget, 7-day-itinerary.
Status: WRITTEN. Cloud name correct (dsrkwieur) from the start; affiliate slots + disclosure in place; correction #1 applied.

## Next steps
1. SECOND GATE: paste second-gate-prompt.txt into 1–2 strong models (incl. one that isn't me). Send findings back.
2. After fixes: download 15 images per batch-02-images.md (named 01..15), then:
   CLOUDINARY_FOLDER=greeceforamericans node scripts/upload-batch.mjs <images-folder> <path>/import-batch-02.json   (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-02.json    (draft)
4. inject-links (links-map grows as more slugs go live) → affiliates → review → publish.
