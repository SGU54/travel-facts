# Batch 16 — image manifest + curated candidate links (TEST: Option 1)

One hero per article (project standard). For each: the **brief**, then **candidate
links** from Unsplash / Pexels / Wikimedia. NOTE: most are *photo pages* or *pre-filtered
gallery pages* to PICK from — click through, download manually, and eyeball each for
license (Unsplash/Pexels = free commercial, no attribution; Wikimedia = check the specific
licence), resolution (≥1600px landscape), and NO recognizable faces / brand signage.
Download your chosen 6 into one folder in THIS order, then run the upload script.

---

## 1. rome-with-kids-itinerary  →  romeforamericans/articles/rome-with-kids-itinerary-hero
**Brief:** Family-friendly Rome — Villa Borghese park greenery, kids/gelato, or a bright
playful Rome scene (avoid identifiable children's faces).
- Unsplash gallery (Villa Borghese): https://unsplash.com/s/photos/villa-borghese
- Unsplash gallery (Rome gelato): https://unsplash.com/s/photos/rome-gelato
- Pexels gallery (Villa Borghese / Rome park): https://www.pexels.com/search/villa%20borghese/
- Wikimedia (Villa Borghese): https://commons.wikimedia.org/wiki/Category:Villa_Borghese_(park)

## 2. rainy-day-rome-itinerary  →  romeforamericans/articles/rainy-day-rome-itinerary-hero
**Brief:** Rainy Rome — wet cobblestones reflecting lights, umbrellas, the Pantheon in rain,
or a moody museum/interior. Atmospheric, not gloomy.
- Unsplash gallery (Rome rain): https://unsplash.com/s/photos/rome-rain
- Unsplash gallery (Pantheon Rome interior): https://unsplash.com/s/photos/pantheon-rome
- Pexels gallery (Rome rain): https://www.pexels.com/search/rome%20rain/
- Wikimedia (Rain in Rome): https://commons.wikimedia.org/wiki/Category:Rain_in_Rome

## 3. rome-month-by-month  →  romeforamericans/articles/rome-month-by-month-hero
**Brief:** Seasonal Rome — a four-season or evocative weather shot; spring blossoms over a
monument, or a classic skyline that reads "any time of year."
- Unsplash photo page (Rome city, golden hour): https://unsplash.com/photos/a-clock-on-a-pole-in-front-of-a-building-7phf_exn-t8
- Unsplash gallery (Rome skyline): https://unsplash.com/s/photos/rome-skyline
- Pexels photo page (Rome sunset skyline): https://www.pexels.com/photo/stunning-view-of-rome-at-sunset-showing-historic-architecture-33101555/
- Wikimedia (Rome panoramas): https://commons.wikimedia.org/wiki/Category:Panoramics_of_Rome

## 4. rome-in-summer  →  romeforamericans/articles/rome-in-summer-hero
**Brief:** Summer Rome — bright blue-sky heat, a nasone fountain, sun on travertine, or a
sun-drenched piazza. Conveys warmth/light.
- Unsplash gallery (Rome summer): https://unsplash.com/s/photos/rome-summer
- Unsplash gallery (Rome fountain / nasone): https://unsplash.com/s/photos/rome-fountain
- Pexels gallery (Rome summer): https://www.pexels.com/search/rome%20summer/
- Wikimedia (Nasoni / drinking fountains Rome): https://commons.wikimedia.org/wiki/Category:Nasoni_in_Rome

## 5. evening-walk-centro-storico  →  romeforamericans/articles/evening-walk-centro-storico-hero
**Brief:** Rome at night — floodlit Trevi Fountain, the Pantheon lit, or a lamplit cobbled
lane / Navona after dark. The romantic blue-hour mood.
- Pexels photo page (Trevi at night): https://www.pexels.com/photo/the-famous-trevi-fountain-in-italy-5067076/
- Unsplash gallery (Trevi fountain): https://unsplash.com/s/photos/trevi
- Unsplash gallery (Rome night): https://unsplash.com/s/photos/rome-night
- Wikimedia (Rome at night): https://commons.wikimedia.org/wiki/Category:Rome_at_night

## 6. mistakes-americans-make-in-rome  →  romeforamericans/articles/mistakes-americans-make-in-rome-hero
**Brief:** A relatable tourist-in-Rome scene — someone with a map/camera at a sight, a
crowded piazza, or a classic "first-timer" vantage (no identifiable faces).
- Unsplash gallery (Rome tourist): https://unsplash.com/s/photos/rome-tourist
- Unsplash gallery (Colosseum, classic): https://unsplash.com/s/photos/colosseum-rome
- Pexels gallery (Rome travel): https://www.pexels.com/search/rome%20travel/
- Wikimedia (Tourists in Rome): https://commons.wikimedia.org/wiki/Category:Tourists_in_Rome

---

## Specific verified photo pages worth a look (from search)
- Colosseum, clean no-people (Unsplash, David Köhler): https://unsplash.com/photos/colosseum-arena-photography-VFRTXGw1VjU
- Colosseum, looking up (Unsplash, M. van Leeuwen): https://unsplash.com/photos/the-colosseum-rome-upGZ5p92SHU
- Trevi at night (Pexels, Max Avans): https://www.pexels.com/photo/the-famous-trevi-fountain-in-italy-5067076/
- Rome sunset skyline (Pexels, Ecem Arslan): https://www.pexels.com/photo/stunning-view-of-rome-at-sunset-showing-historic-architecture-33101555/

## Upload (from repo root, apps/admin/.env.local present), after picking & downloading 6 in order
```
node scripts/upload-batch.mjs <images-folder> import-batch-16.json
```
Previews the mapping, waits for `y`. Expects 6 heroes, no in-body images.

## ⚠ Test-run caveats (as discussed)
- These are pages to PICK from, not guaranteed direct-download file URLs.
- Verify each chosen image: live, ≥1600px landscape, license OK, no faces/brands.
- Gallery links return many options; the specific photo pages are pre-vetted single shots.
