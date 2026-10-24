# Batch 2 — image manifest

Each article needs **one hero image**. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/st-peters-basilica-without-the-wait-hero | St. Peter's Basilica facade / dome across the square |
| 2 | image 2 | romeforamericans/articles/vatican-museums-sistine-chapel-tickets-hero | Vatican Museums gallery (e.g. Gallery of Maps corridor) |
| 3 | image 3 | romeforamericans/articles/borghese-gallery-booking-guide-hero | Borghese Gallery exterior or a Bernini sculpture detail |
| 4 | image 4 | romeforamericans/articles/best-day-trips-from-rome-by-train-hero | Italian high-speed train / scenic Umbrian or coastal rail view |
| 5 | image 5 | romeforamericans/articles/pompeii-day-trip-from-rome-hero | Pompeii ruins with Vesuvius behind |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-02.json
```
Previews the mapping, waits for `y`. Expects 5 heroes, no in-body images.
