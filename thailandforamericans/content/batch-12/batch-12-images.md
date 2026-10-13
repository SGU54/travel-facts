# Batch 12 — Image Manifest (thailandforamericans)

**How to use:** open a search link, pick a strong **landscape** shot, download the largest size into one folder — one image per slot, IN ORDER. Then:

```
node scripts/upload-batch.mjs <images-folder> articles/import-batch-12.json
```

**14 images.** Links are *searches*, not direct files. Rules: landscape ≥1600px, sharp, Unsplash/Pexels (free commercial), no recognizable faces, no brand/logo signage.

**Two tips that fix most of the pain:**
1. Queries below use real photo-tag words (subject + place), not sentence fragments. If the first is thin, try the alternates.
2. A few briefs describe a *specific* scene that barely exists as a free photo (marked ⚠). For those, don't hunt the exact shot — grab the best on-theme image from the wider query. The article reads fine with a strong thematic image.

---


## 1 — `thai-cooking-class-guide-hero`
**Want:** Thai cooking class / curry being cooked
- https://unsplash.com/s/photos/thai-cooking-class
- https://www.pexels.com/search/thai%20cooking%20class/
- alt: https://unsplash.com/s/photos/thai-curry-cooking

## 2 — `thai-cooking-class-guide-1`
**Want:** hands cooking in a wok, fresh ingredients
- https://unsplash.com/s/photos/wok-cooking
- https://www.pexels.com/search/cooking%20wok%20thai/
- alt: https://unsplash.com/s/photos/stir-fry-pan

## 3 — `thai-cooking-class-guide-2`
**Want:** Thai herbs, chilies, curry paste close-up
- https://unsplash.com/s/photos/thai-spices
- https://www.pexels.com/search/chili%20herbs%20thai/
- alt: https://unsplash.com/s/photos/curry-paste


## 4 — `what-to-wear-thai-temples-hero`
**Want:** ornate Thai temple (Wat) exterior, wide
- https://unsplash.com/s/photos/thailand-temple
- https://www.pexels.com/search/thailand%20temple/
- alt: https://unsplash.com/s/photos/wat-bangkok

## 5 — ⚠ `what-to-wear-thai-temples-1`
**Want:** ideally a modestly-dressed visitor at a temple; if scarce, any tasteful tourist-at-Thai-temple shot (back/side, no clear face)
- https://unsplash.com/s/photos/temple-thailand-tourist
- https://www.pexels.com/search/tourist%20temple%20thailand/
- alt: https://unsplash.com/s/photos/woman-temple-asia

## 6 — ⚠ `what-to-wear-thai-temples-2`
**Want:** shoes/sandals outside a temple entrance (rare free — fall back to a temple doorway/steps shot)
- https://unsplash.com/s/photos/shoes-entrance
- https://www.pexels.com/search/shoes%20doorway/
- alt: https://unsplash.com/s/photos/temple-entrance-thailand


## 7 — `best-time-to-visit-thailand-hero`
**Want:** sunny Thai beach with longtail boat
- https://unsplash.com/s/photos/thailand-beach
- https://www.pexels.com/search/thailand%20beach%20longtail/
- alt: https://unsplash.com/s/photos/krabi

## 8 — `best-time-to-visit-thailand-1`
**Want:** bright blue-sky tropical beach (dry-season feel)
- https://unsplash.com/s/photos/tropical-beach-sunny
- https://www.pexels.com/search/thailand%20sunny%20beach/
- alt: https://unsplash.com/s/photos/thailand-island-beach

## 9 — `best-time-to-visit-thailand-2`
**Want:** lush green rice terraces / jungle (rainy-season green)
- https://unsplash.com/s/photos/thailand-rice-field
- https://www.pexels.com/search/rice%20terrace%20green/
- alt: https://unsplash.com/s/photos/jungle-thailand


## 10 — `thailand-for-americans-first-timer-guide-hero`
**Want:** iconic Bangkok temple or skyline (e.g. Wat Arun)
- https://unsplash.com/s/photos/bangkok
- https://www.pexels.com/search/bangkok%20temple/
- alt: https://unsplash.com/s/photos/wat-arun

## 11 — `thailand-for-americans-first-timer-guide-1`
**Want:** postcard Thailand — temple spire or island beach
- https://unsplash.com/s/photos/thailand
- https://www.pexels.com/search/thailand%20island/
- alt: https://unsplash.com/s/photos/phi-phi


## 12 — `how-many-days-in-thailand-hero`
**Want:** scenic Thailand landscape (temple or island)
- https://unsplash.com/s/photos/thailand-landscape
- https://www.pexels.com/search/thailand%20scenery/
- alt: https://unsplash.com/s/photos/thailand-view

## 13 — ⚠ `how-many-days-in-thailand-1`
**Want:** sweeping Thai vista (mountains or island panorama) — "montage" isn't searchable, so pick one strong wide landscape
- https://unsplash.com/s/photos/thailand-mountains
- https://www.pexels.com/search/thailand%20viewpoint/
- alt: https://unsplash.com/s/photos/chiang-mai-view

## 14 — ⚠ `how-many-days-in-thailand-2`
**Want:** traveler (back view) looking over a Thai landscape / viewpoint
- https://unsplash.com/s/photos/viewpoint-traveler
- https://www.pexels.com/search/backpacker%20viewpoint/
- alt: https://unsplash.com/s/photos/person-mountain-view


### After upload
IMAGE_SLOT comments become <figure><img> tags; hero featured_image already set.
