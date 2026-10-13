# Batch 17 — image manifest + curated candidate links (FINAL SIX)

One hero per article. Unsplash + Pexels only (per the test feedback — Wikimedia dropped to
avoid unverified category links). Links are photo-pages or pre-filtered gallery pages to PICK
from — verify each: live, >=1600px landscape, license OK (Unsplash/Pexels free commercial,
no attribution), NO recognizable faces / brand signage. Download chosen 6 in THIS order.

---

## 1. is-rome-safe  →  romeforamericans/articles/is-rome-safe-hero
**Brief:** Reassuring, pleasant Rome street/piazza scene — sunny, calm, people enjoying the
city (NOT crime/police imagery; the article is "aware not afraid"). A welcoming centro view.
- Unsplash gallery (Rome street): https://unsplash.com/s/photos/rome-street
- Unsplash gallery (Rome piazza): https://unsplash.com/s/photos/rome-piazza
- Pexels gallery (Rome street): https://www.pexels.com/search/rome%20street/

## 2. tipping-in-italy  →  romeforamericans/articles/tipping-in-italy-hero
**Brief:** An Italian cafe/restaurant bill, espresso with coins on a saucer, or a cozy
trattoria table — money/dining context, warm not transactional.
- Unsplash gallery (Italian cafe): https://unsplash.com/s/photos/italian-cafe
- Unsplash gallery (espresso coins): https://unsplash.com/s/photos/espresso-bar
- Pexels gallery (restaurant bill / euro): https://www.pexels.com/search/euro%20coins/

## 3. esquilino-termini-guide  →  romeforamericans/articles/esquilino-termini-guide-hero
**Brief:** Santa Maria Maggiore (the basilica facade/interior mosaics) or a Piazza Vittorio /
Esquilino street scene. The area's worthwhile face, not the station.
- Unsplash gallery (Santa Maria Maggiore): https://unsplash.com/s/photos/santa-maria-maggiore
- Unsplash gallery (Rome basilica): https://unsplash.com/s/photos/rome-basilica
- Pexels gallery (Rome church interior): https://www.pexels.com/search/rome%20basilica/

## 4. ostiense-street-art-guide  →  romeforamericans/articles/ostiense-street-art-guide-hero
**Brief:** Bold large-scale street-art mural on an industrial wall (Ostiense vibe), or the
Gazometro / converted-industrial scene. Colorful, urban, edgy.
- Unsplash gallery (Rome street art): https://unsplash.com/s/photos/rome-street-art
- Unsplash gallery (street art mural): https://unsplash.com/s/photos/street-art-mural
- Pexels gallery (street art Italy): https://www.pexels.com/search/street%20art%20mural/

## 5. fine-dining-rome  →  romeforamericans/articles/fine-dining-rome-hero
**Brief:** An elegant plated fine-dining dish, a refined restaurant table setting, or a
rooftop-restaurant view-with-table. Upscale, special-occasion feel.
- Unsplash gallery (fine dining plate): https://unsplash.com/s/photos/fine-dining
- Unsplash gallery (restaurant table elegant): https://unsplash.com/s/photos/restaurant-table
- Pexels gallery (gourmet plating): https://www.pexels.com/search/fine%20dining/

## 6. testaccio-food-market  →  romeforamericans/articles/testaccio-food-market-hero
**Brief:** A market food stall / street-food scene — trapizzino, suppli, pizza al taglio, or a
colorful covered-market produce stall. Appetizing, lively, local.
- Unsplash gallery (Italian street food): https://unsplash.com/s/photos/italian-street-food
- Unsplash gallery (food market stall): https://unsplash.com/s/photos/food-market
- Pexels gallery (Italian street food): https://www.pexels.com/search/italian%20street%20food/

---

## Upload (from repo root, apps/admin/.env.local present), after picking & downloading 6 in order
```
node scripts/upload-batch.mjs <images-folder> import-batch-17.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.

## Caveats
- Pages to PICK from, not guaranteed direct-download URLs.
- Verify each: live, >=1600px landscape, license OK, no faces/brands.
- is-rome-safe: deliberately choose a WELCOMING image, not crime/police imagery.
