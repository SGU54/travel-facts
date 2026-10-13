# Batch 16 — Image Manifest (thailandforamericans)

**How to use:** open a search link, pick a strong **landscape** shot, download the largest size into one folder — one image per slot, IN ORDER. Then:

```
node scripts/upload-batch.mjs <images-folder> articles/import-batch-16.json
```

**15 images.** Links are *searches*, not direct files. Rules: landscape ≥1600px, sharp, Unsplash/Pexels (free commercial), no recognizable faces, no brand/logo signage. Queries use real photo-tag words; if the first is thin, try the alternate. ⚠ = the exact scene is scarce free — grab the best on-theme shot from the wider query.

---


## 1 — `best-temples-in-thailand-hero`
**Want:** spectacular Thai temple, wide
- https://unsplash.com/s/photos/thailand-temple
- https://www.pexels.com/search/thailand%20temple/
- alt: https://unsplash.com/s/photos/wat-arun

## 2 — `best-temples-in-thailand-1`
**Want:** golden temple against blue sky
- https://unsplash.com/s/photos/golden-temple-thailand
- https://www.pexels.com/search/gold%20temple%20thailand/
- alt: https://unsplash.com/s/photos/grand-palace-bangkok

## 3 — `best-temples-in-thailand-2`
**Want:** White Temple (Wat Rong Khun) or Doi Suthep golden chedi (both famous — search well)
- https://unsplash.com/s/photos/white-temple-chiang-rai
- https://www.pexels.com/search/white%20temple%20thailand/
- alt: https://unsplash.com/s/photos/doi-suthep


## 4 — `thai-festivals-guide-hero`
**Want:** vibrant Thai festival (lanterns read best)
- https://unsplash.com/s/photos/thailand-festival
- https://www.pexels.com/search/lantern%20festival%20thailand/
- alt: https://unsplash.com/s/photos/songkran

## 5 — ⚠ `thai-festivals-guide-1`
**Want:** festival scene — lanterns, Songkran water, or a colorful procession (pick the strongest single image)
- https://unsplash.com/s/photos/sky-lanterns
- https://www.pexels.com/search/thailand%20festival/
- alt: https://unsplash.com/s/photos/thai-procession

## 6 — `thai-festivals-guide-2`
**Want:** sky lanterns (Yi Peng) or krathong floats on water
- https://unsplash.com/s/photos/floating-lanterns
- https://www.pexels.com/search/loy%20krathong/
- alt: https://unsplash.com/s/photos/lanterns-night-sky


## 7 — `best-markets-bangkok-hero`
**Want:** bustling Bangkok / Thai market
- https://unsplash.com/s/photos/bangkok-market
- https://www.pexels.com/search/thailand%20market/
- alt: https://unsplash.com/s/photos/night-market-thailand

## 8 — `best-markets-bangkok-1`
**Want:** colorful bustling market scene
- https://unsplash.com/s/photos/thai-market-stalls
- https://www.pexels.com/search/market%20stalls%20thailand/
- alt: https://unsplash.com/s/photos/street-market-asia

## 9 — `best-markets-bangkok-2`
**Want:** floating market, vendors in boats
- https://unsplash.com/s/photos/floating-market
- https://www.pexels.com/search/floating%20market/
- alt: https://unsplash.com/s/photos/damnoen-saduak


## 10 — `bangkok-nightlife-guide-hero`
**Want:** Bangkok skyline at night / rooftop
- https://unsplash.com/s/photos/bangkok-night-skyline
- https://www.pexels.com/search/bangkok%20night/
- alt: https://unsplash.com/s/photos/bangkok-rooftop

## 11 — `bangkok-nightlife-guide-1`
**Want:** rooftop bar overlooking a glittering skyline
- https://unsplash.com/s/photos/rooftop-bar-city
- https://www.pexels.com/search/rooftop%20bar%20skyline/
- alt: https://unsplash.com/s/photos/bangkok-skyline-night

## 12 — `bangkok-nightlife-guide-2`
**Want:** lively night market with food stalls & lights
- https://unsplash.com/s/photos/night-market-thailand
- https://www.pexels.com/search/night%20market%20food/
- alt: https://unsplash.com/s/photos/bangkok-street-night


## 13 — `thailand-weather-by-season-hero`
**Want:** bright sunny Thai landscape, blue sky
- https://unsplash.com/s/photos/thailand-beach-blue-sky
- https://www.pexels.com/search/thailand%20sunny/
- alt: https://unsplash.com/s/photos/thailand-landscape

## 14 — `thailand-weather-by-season-1`
**Want:** bright sunny beach or temple under clear sky
- https://unsplash.com/s/photos/thailand-sunny-beach
- https://www.pexels.com/search/tropical%20blue%20sky/
- alt: https://unsplash.com/s/photos/sunny-tropical-beach

## 15 — `thailand-weather-by-season-2`
**Want:** green lush Thai scene (rainy-season green)
- https://unsplash.com/s/photos/thailand-green-jungle
- https://www.pexels.com/search/thailand%20green%20nature/
- alt: https://unsplash.com/s/photos/rice-terrace-green


### After upload
IMAGE_SLOT comments become <figure><img> tags; hero featured_image already set.
