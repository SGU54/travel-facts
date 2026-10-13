# Batch 8 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/tivoli-day-trip-hero | Villa d'Este fountains terraced gardens, or Hadrian's Villa Canopus pool |
| 2 | image 2 | romeforamericans/articles/ostia-antica-day-trip-hero | Ostia Antica ancient street/ruins or its black-and-white mosaics |
| 3 | image 3 | romeforamericans/articles/orvieto-day-trip-hero | Orvieto Duomo golden mosaic façade, or the town on its cliff |
| 4 | image 4 | romeforamericans/articles/florence-day-trip-from-rome-hero | Florence Duomo / Ponte Vecchio / skyline from Piazzale Michelangelo |
| 5 | image 5 | romeforamericans/articles/castelli-romani-day-trip-hero | Castel Gandolfo over Lake Albano, or Frascati vineyards/wine |
| 6 | image 6 | romeforamericans/articles/naples-from-rome-hero | Naples bay with Vesuvius, or the historic-center streets / pizza |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-08.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
