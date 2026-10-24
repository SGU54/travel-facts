# Batch 11 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/trevi-fountain-guide-hero | Trevi Fountain floodlit at night (Oceanus + cascades) |
| 2 | image 2 | romeforamericans/articles/piazza-navona-guide-hero | Piazza Navona with Bernini's Four Rivers fountain |
| 3 | image 3 | romeforamericans/articles/spanish-steps-guide-hero | Spanish Steps with Trinità dei Monti (azaleas if available) |
| 4 | image 4 | romeforamericans/articles/walking-rome-guide-hero | A cobbled Rome lane / person walking the historic center |
| 5 | image 5 | romeforamericans/articles/most-beautiful-piazzas-rome-hero | Piazza del Popolo or Campidoglio from above |
| 6 | image 6 | romeforamericans/articles/best-walking-routes-rome-hero | Rome rooftops/streets from a viewpoint (Pincio or Gianicolo) |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-11.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
