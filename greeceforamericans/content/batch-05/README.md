# batch-05 — greeceforamericans (the Santorini cluster)

5 articles: santorini-first-timers-guide, best-things-to-do-in-santorini, santorini-sunset-guide, santorini-best-beaches, santorini-cruise-stop-guide.
Interlink + funnel to where-to-stay-in-santorini (batch 1). Status: WRITTEN. cloud=dsrkwieur, affiliate slots + disclosure, 15 images.

## Next
1. SECOND GATE: paste second-gate-prompt.txt into 1–2 models; send findings.
2. Images: 15 per batch-05-images.md (named 01..15), then
   CLOUDINARY_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-05.json  (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-05.json   (draft)
4. links → affiliates → review → publish.
