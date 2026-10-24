# Batch 15 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/colosseum-vs-vatican-where-to-stay-hero | Split-feel: Colosseum + St Peter's, or a Monti/Prati street |
| 2 | image 2 | romeforamericans/articles/staying-near-termini-hero | Roma Termini station exterior / a hotel street near it |
| 3 | image 3 | romeforamericans/articles/where-to-stay-trastevere-hero | Trastevere cobbled lane with guesthouse/B&B façades |
| 4 | image 4 | romeforamericans/articles/hotels-with-a-view-rome-hero | Hotel rooftop terrace overlooking Rome domes/skyline |
| 5 | image 5 | romeforamericans/articles/family-friendly-stays-rome-hero | Bright apartment living room / family-friendly interior |
| 6 | image 6 | romeforamericans/articles/apartment-vs-hotel-rome-hero | Roman apartment interior with a window over rooftops |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos/brand signage.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-15.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
