# Batch 7 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/pantheon-visiting-guide-hero | Pantheon interior dome + oculus, light beam |
| 2 | image 2 | romeforamericans/articles/roman-forum-guide-hero | Roman Forum columns with the Arch of Septimius Severus / Temple of Saturn |
| 3 | image 3 | romeforamericans/articles/colosseum-underground-arena-floor-hero | Colosseum interior showing the underground hypogeum / arena floor |
| 4 | image 4 | romeforamericans/articles/appia-antica-guide-hero | Via Appia Antica — ancient basalt road lined with pines/tombs |
| 5 | image 5 | romeforamericans/articles/capitoline-hill-vittoriano-hero | Piazza del Campidoglio star pavement, or the Vittoriano from Piazza Venezia |
| 6 | image 6 | romeforamericans/articles/castel-santangelo-guide-hero | Castel Sant'Angelo across the Tiber with the angel bridge |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-07.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
