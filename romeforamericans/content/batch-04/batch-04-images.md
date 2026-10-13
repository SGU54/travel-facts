# Batch 4 — image manifest

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/getting-around-rome-overview-hero | Person walking a cobbled Rome street / a tram passing a piazza |
| 2 | image 2 | romeforamericans/articles/rome-transport-tickets-roma-pass-hero | Rome metro entrance / yellow validation gate / ATAC bus |
| 3 | image 3 | romeforamericans/articles/rome-taxis-guide-hero | A white Rome taxi at a rank (roof TAXI sign visible) |
| 4 | image 4 | romeforamericans/articles/how-much-does-rome-cost-hero | Euro notes/coins with a Roman cafe or market scene (no faces) |
| 5 | image 5 | romeforamericans/articles/best-time-to-visit-rome-hero | Rome in a clear season — e.g. spring by the Spanish Steps or autumn light over the rooftops |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-04.json
```
Previews the mapping, waits for `y`. Expects 5 heroes, no in-body images.
