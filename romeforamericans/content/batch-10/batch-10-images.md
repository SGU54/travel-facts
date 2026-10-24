# Batch 10 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/st-peters-dome-climb-hero | View from St Peter's dome over the square, or the dome itself |
| 2 | image 2 | romeforamericans/articles/how-early-arrive-vatican-hero | Vatican Museums gallery / Sistine area / St Peter's Square crowds |
| 3 | image 3 | romeforamericans/articles/papal-audience-st-peters-square-hero | St Peter's Square colonnade + obelisk (audience crowd, no identifiable faces) |
| 4 | image 4 | romeforamericans/articles/best-museums-rome-first-timers-hero | A grand Rome museum gallery / Borghese or Vatican interior |
| 5 | image 5 | romeforamericans/articles/capitoline-museums-hero | Capitoline Wolf, Marcus Aurelius bronze, or the Constantine colossus fragments |
| 6 | image 6 | romeforamericans/articles/caravaggio-in-rome-hero | San Luigi dei Francesi interior / a Caravaggio chapel (or church facade) |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.
(Caravaggio: a church interior or facade is safer than a tight reproduction of the painting.)

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-10.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
