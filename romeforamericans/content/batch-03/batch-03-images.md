# Batch 3 — image manifest

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/roman-dishes-to-try-hero | A classic Roman pasta (cacio e pepe / carbonara) plated, rustic table |
| 2 | image 2 | romeforamericans/articles/best-trattorias-rome-hero | Cozy Roman trattoria interior or a Testaccio/|
| 3 | image 3 | romeforamericans/articles/best-gelato-rome-hero | Artisanal gelato in covered metal tubs, natural colors |
| 4 | image 4 | romeforamericans/articles/rome-in-2-days-hero | Rome skyline / a walkable piazza scene (e.g. Trevi or rooftops) |
| 5 | image 5 | romeforamericans/articles/rome-in-3-days-hero | Iconic wide Rome view (St. Peter's dome or the Forum at golden hour) |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-03.json
```
Previews the mapping, waits for `y`. Expects 5 heroes, no in-body images.
