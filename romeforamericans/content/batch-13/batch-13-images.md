# Batch 13 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/fiumicino-vs-ciampino-hero | Airport terminal / plane / arrivals (generic Rome airport feel) |
| 2 | image 2 | romeforamericans/articles/leonardo-express-fiumicino-trains-hero | Leonardo Express / Trenitalia train at platform |
| 3 | image 3 | romeforamericans/articles/rome-metro-guide-hero | Rome metro station/train, or a metro sign (M) |
| 4 | image 4 | romeforamericans/articles/rome-buses-trams-guide-hero | Rome tram (Tram 8) or bus on a city street |
| 5 | image 5 | romeforamericans/articles/renting-a-car-in-rome-hero | Narrow Rome street with cars/scooters, or a ZTL sign |
| 6 | image 6 | romeforamericans/articles/florence-high-speed-train-hero | Frecciarossa/Italo high-speed train, or Florence Duomo skyline |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos/branding.
(Trains: avoid shots dominated by a single operator's logo where possible.)

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-13.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
