# Batch 15 — Image Manifest (thailandforamericans)

**How to use:** open a search link, pick a strong **landscape** shot, download the largest size into one folder — one image per slot, IN ORDER. Then:

```
node scripts/upload-batch.mjs <images-folder> articles/import-batch-15.json
```

**15 images.** Links are *searches*, not direct files. Rules: landscape ≥1600px, sharp, Unsplash/Pexels (free commercial), no recognizable faces, no brand/logo signage. Queries use real photo-tag words; if the first is thin, try the alternate. ⚠ = the exact scene is scarce free — grab the best on-theme shot from the wider query.

---


## 1 — `elephant-tourism-ethics-thailand-hero`
**Want:** elephant in a natural setting
- https://unsplash.com/s/photos/elephant-thailand
- https://www.pexels.com/search/elephant%20thailand/
- alt: https://unsplash.com/s/photos/asian-elephant

## 2 — `elephant-tourism-ethics-thailand-1`
**Want:** elephants roaming free in nature/sanctuary
- https://unsplash.com/s/photos/elephant-sanctuary
- https://www.pexels.com/search/elephant%20nature/
- alt: https://unsplash.com/s/photos/elephant-jungle

## 3 — ⚠ `elephant-tourism-ethics-thailand-2`
**Want:** a mahout with an elephant (specific — if thin, any close elephant-and-person care shot, no clear face)
- https://unsplash.com/s/photos/mahout-elephant
- https://www.pexels.com/search/elephant%20care/
- alt: https://unsplash.com/s/photos/elephant-bathing


## 4 — `isan-northeast-thailand-guide-hero`
**Want:** rural Thai rice fields / countryside
- https://unsplash.com/s/photos/thailand-rice-field
- https://www.pexels.com/search/thailand%20countryside/
- alt: https://unsplash.com/s/photos/isan-thailand

## 5 — ⚠ `isan-northeast-thailand-guide-1`
**Want:** Isan rural scene — rice fields, local market, or Khmer ruin (Isan is under-photographed; rice fields search best)
- https://unsplash.com/s/photos/rice-field-thailand
- https://www.pexels.com/search/thailand%20rural%20village/
- alt: https://unsplash.com/s/photos/khmer-temple-thailand

## 6 — `isan-northeast-thailand-guide-2`
**Want:** som tum / grilled chicken / sticky rice (Isan food)
- https://unsplash.com/s/photos/som-tum
- https://www.pexels.com/search/papaya%20salad/
- alt: https://unsplash.com/s/photos/thai-grilled-chicken


## 7 — `railay-beach-guide-hero`
**Want:** Railay limestone cliffs and beach
- https://unsplash.com/s/photos/railay-beach
- https://www.pexels.com/search/railay/
- alt: https://unsplash.com/s/photos/krabi-cliffs

## 8 — `railay-beach-guide-1`
**Want:** limestone cliffs over turquoise water with longtail boats
- https://unsplash.com/s/photos/krabi-longtail
- https://www.pexels.com/search/thailand%20limestone%20cliffs/
- alt: https://unsplash.com/s/photos/railay-cliffs

## 9 — `railay-beach-guide-2`
**Want:** Phra Nang Beach, dramatic cliffs & clear water
- https://unsplash.com/s/photos/phra-nang-beach
- https://www.pexels.com/search/krabi%20beach/
- alt: https://unsplash.com/s/photos/thailand-cliff-beach


## 10 — `best-beaches-in-thailand-hero`
**Want:** stunning Thai beach, turquoise water
- https://unsplash.com/s/photos/thailand-beach
- https://www.pexels.com/search/thailand%20beach/
- alt: https://unsplash.com/s/photos/thailand-island

## 11 — `best-beaches-in-thailand-1`
**Want:** white sand, turquoise water, cliffs
- https://unsplash.com/s/photos/thailand-white-sand-beach
- https://www.pexels.com/search/tropical%20beach%20cliffs/
- alt: https://unsplash.com/s/photos/phi-phi-beach

## 12 — `best-beaches-in-thailand-2`
**Want:** quiet palm-fringed beach, calm clear water
- https://unsplash.com/s/photos/palm-beach-thailand
- https://www.pexels.com/search/palm%20beach%20calm/
- alt: https://unsplash.com/s/photos/empty-tropical-beach


## 13 — `trekking-northern-thailand-hero`
**Want:** misty northern Thai mountains / jungle trail
- https://unsplash.com/s/photos/northern-thailand-mountains
- https://www.pexels.com/search/thailand%20jungle%20trek/
- alt: https://unsplash.com/s/photos/chiang-mai-mountains

## 14 — `trekking-northern-thailand-1`
**Want:** trekkers on a jungle trail, misty mountains
- https://unsplash.com/s/photos/jungle-trek
- https://www.pexels.com/search/hiking%20jungle/
- alt: https://unsplash.com/s/photos/rainforest-hiking

## 15 — ⚠ `trekking-northern-thailand-2`
**Want:** hill-tribe village OR a mountain viewpoint (village is sensitive/scarce — a mountain viewpoint reads well and is safer)
- https://unsplash.com/s/photos/thailand-mountain-viewpoint
- https://www.pexels.com/search/thailand%20mountains/
- alt: https://unsplash.com/s/photos/northern-thailand-village


### After upload
IMAGE_SLOT comments become <figure><img> tags; hero featured_image already set.
