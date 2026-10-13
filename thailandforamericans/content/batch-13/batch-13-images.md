# Batch 13 — Image Manifest (thailandforamericans)

**How to use:** open a search link, pick a strong **landscape** shot, download the largest size into one folder — one image per slot, IN ORDER. Then:

```
node scripts/upload-batch.mjs <images-folder> articles/import-batch-13.json
```

**15 images.** Links are *searches*, not direct files. Rules: landscape ≥1600px, sharp, Unsplash/Pexels (free commercial), no recognizable faces, no brand/logo signage.

**Two tips:**
1. Queries use real photo-tag words (subject + place), not sentence fragments. If the first is thin, try the alternate.
2. A few briefs describe a *composite* scene that isn't a single photo (marked ⚠). Don't hunt the exact thing — grab the best on-theme landscape from the wider query. Good news: most of this batch is famous landmarks that photograph well.

---


## 1 — `bangkok-vs-islands-vs-north-hero`
**Want:** iconic Thailand scene (Bangkok temple or skyline works as the lead)
- https://unsplash.com/s/photos/bangkok-temple
- https://www.pexels.com/search/bangkok%20thailand/
- alt: https://unsplash.com/s/photos/wat-arun

## 2 — ⚠ `bangkok-vs-islands-vs-north-1`
**Want:** "city + beach + mountain" isn't one photo — pick one strong wide Thailand landscape (an island viewpoint reads best)
- https://unsplash.com/s/photos/thailand-island-aerial
- https://www.pexels.com/search/thailand%20aerial/
- alt: https://unsplash.com/s/photos/thailand-landscape

## 3 — ⚠ `bangkok-vs-islands-vs-north-2`
**Want:** island beach OR a northern temple (either works — pick the stronger single image)
- https://unsplash.com/s/photos/thailand-beach
- https://www.pexels.com/search/thailand%20temple%20mountain/
- alt: https://unsplash.com/s/photos/chiang-mai-temple


## 4 — `ayutthaya-guide-hero`
**Want:** Ayutthaya temple ruins, wide
- https://unsplash.com/s/photos/ayutthaya
- https://www.pexels.com/search/ayutthaya/
- alt: https://unsplash.com/s/photos/ayutthaya-temple

## 5 — `ayutthaya-guide-1`
**Want:** brick ruins and prang towers at Ayutthaya
- https://unsplash.com/s/photos/ayutthaya-ruins
- https://www.pexels.com/search/ayutthaya%20ruins/
- alt: https://unsplash.com/s/photos/ancient-temple-thailand

## 6 — `ayutthaya-guide-2`
**Want:** the Buddha head in tree roots, Wat Mahathat (famous — searches well)
- https://unsplash.com/s/photos/buddha-head-tree-roots
- https://www.pexels.com/search/buddha%20head%20tree/
- alt: https://unsplash.com/s/photos/wat-mahathat


## 7 — `kanchanaburi-river-kwai-guide-hero`
**Want:** Bridge over the River Kwai / Kanchanaburi river scene
- https://unsplash.com/s/photos/river-kwai
- https://www.pexels.com/search/kanchanaburi/
- alt: https://unsplash.com/s/photos/kanchanaburi-bridge

## 8 — `kanchanaburi-river-kwai-guide-1`
**Want:** the bridge itself, or the Death Railway
- https://unsplash.com/s/photos/bridge-river-kwai
- https://www.pexels.com/search/river%20kwai%20bridge/
- alt: https://unsplash.com/s/photos/death-railway

## 9 — ⚠ `kanchanaburi-river-kwai-guide-2`
**Want:** train on the Death Railway hugging the cliff (specific — if thin, any scenic Thailand train/railway-in-jungle shot)
- https://unsplash.com/s/photos/thailand-train-railway
- https://www.pexels.com/search/train%20jungle%20railway/
- alt: https://unsplash.com/s/photos/death-railway-train


## 10 — `khao-yai-national-park-guide-hero`
**Want:** Khao Yai jungle / national park vista
- https://unsplash.com/s/photos/khao-yai
- https://www.pexels.com/search/khao%20yai/
- alt: https://unsplash.com/s/photos/thailand-jungle

## 11 — `khao-yai-national-park-guide-1`
**Want:** lush jungle canopy / forest viewpoint
- https://unsplash.com/s/photos/jungle-viewpoint
- https://www.pexels.com/search/thailand%20rainforest/
- alt: https://unsplash.com/s/photos/forest-canopy-green

## 12 — ⚠ `khao-yai-national-park-guide-2`
**Want:** wild elephant OR hornbill (pick whichever searches strongest — both are on-theme)
- https://unsplash.com/s/photos/wild-elephant
- https://www.pexels.com/search/hornbill/
- alt: https://unsplash.com/s/photos/asian-elephant-forest


## 13 — `chiang-mai-vs-chiang-rai-hero`
**Want:** northern Thai temple or misty mountains
- https://unsplash.com/s/photos/chiang-mai
- https://www.pexels.com/search/chiang%20mai/
- alt: https://unsplash.com/s/photos/chiang-mai-temple

## 14 — `chiang-mai-vs-chiang-rai-1`
**Want:** northern Thai temple or misty mountain landscape
- https://unsplash.com/s/photos/northern-thailand-mountains
- https://www.pexels.com/search/chiang%20mai%20mountains/
- alt: https://unsplash.com/s/photos/misty-mountains-thailand

## 15 — `chiang-mai-vs-chiang-rai-2`
**Want:** the White Temple, Wat Rong Khun (famous — searches well)
- https://unsplash.com/s/photos/white-temple-chiang-rai
- https://www.pexels.com/search/white%20temple%20thailand/
- alt: https://unsplash.com/s/photos/wat-rong-khun


### After upload
IMAGE_SLOT comments become <figure><img> tags; hero featured_image already set.
