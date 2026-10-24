# Batch 12 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/italian-etiquette-for-americans-hero | Romans at a café / espresso bar / piazza social scene |
| 2 | image 2 | romeforamericans/articles/what-to-wear-rome-dress-code-hero | Well-dressed person on a Rome street, or church entrance |
| 3 | image 3 | romeforamericans/articles/what-to-pack-for-rome-hero | Flat-lay travel packing / suitcase with Rome essentials |
| 4 | image 4 | romeforamericans/articles/esim-sim-wifi-rome-hero | Phone with map on a Rome street / person navigating |
| 5 | image 5 | romeforamericans/articles/basic-italian-phrases-rome-hero | Rome café menu / chalkboard, or friendly shopkeeper scene |
| 6 | image 6 | romeforamericans/articles/cash-cards-tipping-rome-hero | Euro notes/coins, card payment at a café, or a bill on a table |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-12.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
