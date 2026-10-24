# batch-12 — greeceforamericans (transport / logistics)

5 articles: renting-a-car-in-greece (IDP-critical), athens-airport-to-city-and-port, domestic-flights-in-greece, piraeus-port-guide, fast-vs-slow-ferries-greece.
Status: WRITTEN. cloud=dsrkwieur, 15 images. IDP fact prominent in the car article. Scope-clean (Rhodes refs removed).

## Next
1. SECOND GATE: paste second-gate-prompt.txt into 1–2 models (checks IDP + transport facts + scope); send findings.
2. Images: 15 per batch-12-images.md (named 01..15), then
   MEDIA_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-12.json  (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-12.json   (draft)
4. links → affiliates → review → publish.
