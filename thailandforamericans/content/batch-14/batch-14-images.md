# Batch 14 — Image Manifest (thailandforamericans)

**How to use:** open a search link, pick a strong **landscape** shot, download the largest size into one folder — one image per slot, IN ORDER. Then:

```
node scripts/upload-batch.mjs <images-folder> articles/import-batch-14.json
```

**15 images.** Links are *searches*, not direct files. Rules: landscape ≥1600px, sharp, Unsplash/Pexels (free commercial), no recognizable faces, no brand/logo signage. Queries use real photo-tag words; if the first is thin, try the alternate. ⚠ = the exact scene is scarce free — grab the best on-theme shot from the wider query.

---


## 1 — `pai-thailand-guide-hero`
**Want:** Pai valley / northern Thailand mountains
- https://unsplash.com/s/photos/pai-thailand
- https://www.pexels.com/search/pai%20thailand/
- alt: https://unsplash.com/s/photos/mae-hong-son

## 2 — `pai-thailand-guide-1`
**Want:** green valley with mountains and morning mist
- https://unsplash.com/s/photos/thailand-valley-mist
- https://www.pexels.com/search/thailand%20valley%20mountains/
- alt: https://unsplash.com/s/photos/rice-paddy-mountains

## 3 — `pai-thailand-guide-2`
**Want:** Pai Canyon at sunset, or a night walking-street food market
- https://unsplash.com/s/photos/pai-canyon
- https://www.pexels.com/search/canyon%20sunset%20thailand/
- alt: https://unsplash.com/s/photos/thailand-night-market


## 4 — `chiang-mai-lantern-festival-guide-hero`
**Want:** sky lanterns at night (Yi Peng)
- https://unsplash.com/s/photos/sky-lanterns
- https://www.pexels.com/search/lantern%20festival%20thailand/
- alt: https://unsplash.com/s/photos/yi-peng

## 5 — `chiang-mai-lantern-festival-guide-1`
**Want:** sky lanterns rising into the night
- https://unsplash.com/s/photos/floating-lanterns-night
- https://www.pexels.com/search/sky%20lanterns%20night/
- alt: https://unsplash.com/s/photos/lantern-festival

## 6 — `chiang-mai-lantern-festival-guide-2`
**Want:** candle-lit krathong floats on water (Loy Krathong)
- https://unsplash.com/s/photos/loy-krathong
- https://www.pexels.com/search/krathong%20floating/
- alt: https://unsplash.com/s/photos/floating-candles-water


## 7 — `tuktuks-taxis-thailand-hero`
**Want:** Thai tuk-tuk on a city street
- https://unsplash.com/s/photos/tuk-tuk-thailand
- https://www.pexels.com/search/tuk%20tuk%20bangkok/
- alt: https://unsplash.com/s/photos/tuk-tuk

## 8 — `tuktuks-taxis-thailand-1`
**Want:** colorful tuk-tuk, close/street level
- https://unsplash.com/s/photos/tuktuk-bangkok
- https://www.pexels.com/search/tuk%20tuk%20street/
- alt: https://unsplash.com/s/photos/three-wheeler-thailand

## 9 — ⚠ `tuktuks-taxis-thailand-2`
**Want:** taxis or a songthaew truck (songthaew is rare free — Bangkok pink/colored taxis work)
- https://unsplash.com/s/photos/bangkok-taxi
- https://www.pexels.com/search/thailand%20taxi/
- alt: https://unsplash.com/s/photos/songthaew


## 10 — `how-spicy-is-thai-food-hero`
**Want:** colorful spicy Thai dish
- https://unsplash.com/s/photos/thai-food
- https://www.pexels.com/search/thai%20food%20spicy/
- alt: https://unsplash.com/s/photos/thai-curry

## 11 — `how-spicy-is-thai-food-1`
**Want:** red & green Thai chilies (close-up)
- https://unsplash.com/s/photos/thai-chili
- https://www.pexels.com/search/red%20green%20chili/
- alt: https://unsplash.com/s/photos/chili-peppers

## 12 — `how-spicy-is-thai-food-2`
**Want:** steaming bowl of tom yum or som tum
- https://unsplash.com/s/photos/tom-yum
- https://www.pexels.com/search/tom%20yum%20soup/
- alt: https://unsplash.com/s/photos/som-tum


## 13 — `drinking-in-thailand-guide-hero`
**Want:** cold beer on a beach / bar table
- https://unsplash.com/s/photos/beer-beach
- https://www.pexels.com/search/beer%20beach/
- alt: https://unsplash.com/s/photos/cold-beer-bottle

## 14 — `drinking-in-thailand-guide-1`
**Want:** cold beer bottles on a beachside table at sunset
- https://unsplash.com/s/photos/beer-sunset-beach
- https://www.pexels.com/search/beer%20sunset/
- alt: https://unsplash.com/s/photos/beach-bar-drinks

## 15 — `drinking-in-thailand-guide-2`
**Want:** tasteful beach bar or rooftop bar scene
- https://unsplash.com/s/photos/beach-bar
- https://www.pexels.com/search/rooftop%20bar/
- alt: https://unsplash.com/s/photos/bar-sunset-tropical


### After upload
IMAGE_SLOT comments become <figure><img> tags; hero featured_image already set.
