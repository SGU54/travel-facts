# Batch 6 — image manifest

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/rome-in-4-days-hero | Rome panorama with a day-trip feel (rooftops + a train or countryside hint) |
| 2 | image 2 | romeforamericans/articles/rome-in-5-7-days-hero | Relaxed Roman scene — a quiet piazza, market, or long-stay neighborhood street |
| 3 | image 3 | romeforamericans/articles/best-boutique-hotels-rome-hero | Stylish boutique hotel interior or a charming converted-palazzo facade |
| 4 | image 4 | romeforamericans/articles/budget-stays-rome-hero | Cozy budget room / characterful guesthouse or hostel common area |
| 5 | image 5 | romeforamericans/articles/where-to-eat-roman-pasta-classics-hero | A plate of cacio e pepe or carbonara, rustic trattoria table |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-06.json
```
Previews the mapping, waits for `y`. Expects 5 heroes, no in-body images.
