# batch-09 — greeceforamericans (food & drink cluster)

5 articles: greek-food-what-to-order, how-to-eat-at-a-greek-taverna, greek-wine-guide, best-food-experiences-athens, greek-coffee-cafe-culture.
Tipping framed per facts.json (5-10%, not US-style). Status: WRITTEN. cloud=dsrkwieur, affiliate slots + disclosure, 15 images.

## Next
1. SECOND GATE: paste second-gate-prompt.txt into 1–2 models (key check: tipping 5-10% not 18-20%); send findings.
2. Images: 15 per batch-09-images.md (named 01..15), then
   MEDIA_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-09.json  (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-09.json   (draft)
4. links → affiliates → review → publish.
