# Batch 14 — image manifest (6 articles)

One hero image per article. Download in THIS order into one folder, then run the upload script.

| # | Order | media keys | Suggested subject |
|---|-------|----------------------|-------------------|
| 1 | image 1 | romeforamericans/articles/roman-coffee-culture-hero | Espresso on a marble bar counter / Italian caffè interior |
| 2 | image 2 | romeforamericans/articles/best-aperitivo-rome-hero | Aperol Spritz / aperitivo spread at golden hour |
| 3 | image 3 | romeforamericans/articles/rooftop-bars-rome-hero | Rome rooftop terrace at sunset with skyline/dome view |
| 4 | image 4 | romeforamericans/articles/avoid-tourist-trap-restaurants-rome-hero | Authentic trattoria interior, or a Roman pasta dish |
| 5 | image 5 | romeforamericans/articles/where-to-eat-trastevere-testaccio-hero | Trastevere lane with restaurant tables, or a plate of cacio e pepe |
| 6 | image 6 | romeforamericans/articles/best-markets-rome-hero | Colorful Rome market stall (produce/Testaccio/Campo de' Fiori) |

License-clean (Unsplash/Pexels/own), landscape, ≥1600px, no recognizable faces/logos/brand signage.

## Upload (from repo root, apps/admin/.env.local present)
```
node scripts/upload-batch.mjs <images-folder> import-batch-14.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.
