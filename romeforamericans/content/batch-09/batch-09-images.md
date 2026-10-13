# Batch 9 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | Cloudinary public_id | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/trastevere-neighborhood-guide-hero | Trastevere cobbled lane, ivy + ochre walls (daytime) |
| 2 | image 2 | romeforamericans/articles/centro-storico-neighborhood-guide-hero | Pantheon or Piazza Navona / a centro storico lane |
| 3 | image 3 | romeforamericans/articles/monti-neighborhood-guide-hero | Monti lane with boutiques, or Piazza della Madonna dei Monti |
| 4 | image 4 | romeforamericans/articles/testaccio-neighborhood-guide-hero | Testaccio Market stalls / street-food, or a classic trattoria |
| 5 | image 5 | romeforamericans/articles/jewish-ghetto-guide-hero | Portico d'Ottavia / Great Synagogue / Via del Portico d'Ottavia |
| 6 | image 6 | romeforamericans/articles/campo-de-fiori-guide-hero | Campo de' Fiori morning market with the Giordano Bruno statue |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos.
(Jewish Ghetto: choose a dignified architectural/streetscape image — avoid memorial-stone close-ups.)

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-09.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
