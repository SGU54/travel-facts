# Batch 1 — image manifest

Each article needs **one hero image**. Download them in THIS exact order and put
them in a single folder, then run the upload script (below). Order matters — the
script matches images to public_ids by download order.

| # | Download order | media keys (auto-set by script) | Suggested subject |
|---|----------------|--------------------------------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/colosseum-tickets-without-getting-scammed-hero | Colosseum exterior, golden hour, no crowds in front |
| 2 | image 2 | romeforamericans/articles/colosseum-forum-palatine-combined-ticket-hero | Roman Forum looking toward the Colosseum |
| 3 | image 3 | romeforamericans/articles/rome-in-1-day-hero | Iconic wide Rome cityscape (rooftops + a dome) |
| 4 | image 4 | romeforamericans/articles/where-to-stay-rome-first-visit-hero | Charming Trastevere or Monti street, warm light |
| 5 | image 5 | romeforamericans/articles/rome-airport-to-city-center-hero | Leonardo Express train / Termini, or a Rome taxi |

## Sourcing
Use license-clean images (Unsplash, Pexels, or your own). Landscape orientation,
≥1600px wide, evocative but not text-heavy. Avoid recognizable faces and logos.

## Upload (from repo root, with apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> travel-facts/romeforamericans/import-batch-01.json
# or: npm run upload-batch -- <images-folder> import-batch-01.json
```
The script previews the image→public_id mapping and waits for `y` before uploading.
If the count doesn't match (it expects 5 heroes, no in-body images), it stops and shows both lists.
