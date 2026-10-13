# Batch 5 — image manifest

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/common-scams-in-rome-hero | Busy Rome tourist crowd / pickpocket-awareness scene (no identifiable faces) |
| 2 | image 2 | romeforamericans/articles/best-neighborhoods-to-stay-rome-hero | Rome rooftops across neighborhoods, or a characterful residential street |
| 3 | image 3 | romeforamericans/articles/skip-the-line-tickets-rome-hero | Queue/entrance at the Colosseum or Vatican (line vs entry) |
| 4 | image 4 | romeforamericans/articles/roma-pass-omnia-card-worth-it-hero | A transit/ticket scene or montage of major sights (Colosseum + St Peter's) |
| 5 | image 5 | romeforamericans/articles/trastevere-after-dark-hero | Trastevere lanes at night, lanterns and restaurant tables |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-05.json
```
Previews the mapping, waits for `y`. Expects 5 heroes, no in-body images.
