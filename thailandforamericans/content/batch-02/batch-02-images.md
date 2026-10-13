# Batch 02 — Image Manifest (thailandforamericans)

**How to use this:** Download one image per entry below, **in this exact order**, into a single folder. Then run:

```
node scripts/upload-batch.mjs <your-images-folder> articles/import-batch-02.json
```

The script maps your folder (sorted by download order) to these Cloudinary public_ids, previews the mapping, and uploads only after you confirm. **15 images expected** (5 heroes + 10 in-body).

**Picking rules for every image:** candidate links are pages to pick from, not direct downloads. Choose **landscape, ≥1600px**, sharp. Unsplash & Pexels = free commercial, no attribution. **No recognizable faces, no brand/logo signage.**

---

## 1 — `thailandforamericans/articles/10-day-thailand-itinerary-hero`
**Brief:** A montage-feel hero that signals a multi-region Thailand trip — temple, mountains, and sea if possible; otherwise an iconic, bright Thailand scene.
- https://unsplash.com/s/photos/thailand
- https://www.pexels.com/search/thailand/

## 2 — `thailandforamericans/articles/10-day-thailand-itinerary-1`
**Brief:** Wide, inviting establishing shot of Thailand — Bangkok temple or riverside, bright daylight.
- https://unsplash.com/photos/wat-arun-temple-on-chao-phraya-river-bangkok-wd3tQvk0WXA
- https://unsplash.com/s/photos/bangkok%20temple
- https://www.pexels.com/search/bangkok%20temple/

## 3 — `thailandforamericans/articles/10-day-thailand-itinerary-2`
**Brief:** Mountain temple Doi Suthep with its golden chedi, OR elephants in a green sanctuary setting.
- https://unsplash.com/s/photos/doi%20suthep
- https://unsplash.com/s/photos/elephant%20sanctuary%20thailand
- https://www.pexels.com/search/doi%20suthep/

---

## 4 — `thailandforamericans/articles/2-weeks-in-thailand-itinerary-hero`
**Brief:** A sweeping Thailand landscape that reads "epic trip" — temple, mountain, or sea, bright and aspirational.
- https://unsplash.com/s/photos/thailand%20landscape
- https://www.pexels.com/search/thailand%20landscape/

## 5 — `thailandforamericans/articles/2-weeks-in-thailand-itinerary-1`
**Brief:** A combined temple-and-sea or temple-and-mountain image evoking the whole-country range.
- https://unsplash.com/s/photos/thailand%20temple%20mountain
- https://www.pexels.com/search/thailand%20scenery/

## 6 — `thailandforamericans/articles/2-weeks-in-thailand-itinerary-2`
**Brief:** Chiang Rai's White Temple (Wat Rong Khun), OR a misty northern Thailand mountain scene.
- https://unsplash.com/s/photos/white%20temple%20chiang%20rai
- https://unsplash.com/s/photos/chiang%20rai
- https://www.pexels.com/search/white%20temple%20thailand/

---

## 7 — `thailandforamericans/articles/where-to-stay-in-phuket-hero`
**Brief:** A sweeping Phuket coastline — beach and headland, turquoise water, daytime.
- https://unsplash.com/s/photos/phuket
- https://www.pexels.com/search/phuket/

## 8 — `thailandforamericans/articles/where-to-stay-in-phuket-1`
**Brief:** A Phuket beach with a headland or viewpoint (Kata/Karon feel), bright daylight.
- https://unsplash.com/s/photos/phuket%20beach
- https://www.pexels.com/search/phuket%20beach/

## 9 — `thailandforamericans/articles/where-to-stay-in-phuket-2`
**Brief:** Colorful Sino-Portuguese shophouses of Phuket Old Town.
- https://unsplash.com/s/photos/phuket%20old%20town
- https://www.pexels.com/search/phuket%20old%20town/

---

## 10 — `thailandforamericans/articles/where-to-stay-in-krabi-hero`
**Brief:** Krabi's limestone karsts rising from turquoise water with longtail boats.
- https://unsplash.com/s/photos/krabi
- https://www.pexels.com/search/krabi/

## 11 — `thailandforamericans/articles/where-to-stay-in-krabi-1`
**Brief:** Krabi/Ao Nang limestone karsts and turquoise water with longtail boats in the foreground.
- https://unsplash.com/s/photos/ao%20nang%20krabi
- https://www.pexels.com/search/krabi%20longtail%20boat/

## 12 — `thailandforamericans/articles/where-to-stay-in-krabi-2`
**Brief:** Railay West beach at sunset — longtail boats and towering cliffs.
- https://unsplash.com/s/photos/railay%20beach
- https://www.pexels.com/search/railay%20beach/

---

## 13 — `thailandforamericans/articles/best-island-resorts-thailand-hero`
**Brief:** A luxurious Thai beachfront resort pool overlooking the sea (no recognizable guests).
- https://unsplash.com/s/photos/thailand%20resort%20pool
- https://www.pexels.com/search/thailand%20resort/

## 14 — `thailandforamericans/articles/best-island-resorts-thailand-1`
**Brief:** An infinity pool or beachfront villa deck overlooking a tropical Thai sea.
- https://unsplash.com/s/photos/infinity%20pool%20tropical
- https://www.pexels.com/search/beachfront%20resort/

## 15 — `thailandforamericans/articles/best-island-resorts-thailand-2`
**Brief:** A serene Koh Samui beach resort with palms and calm water.
- https://unsplash.com/s/photos/koh%20samui%20beach
- https://www.pexels.com/search/koh%20samui/

---

### After upload
Once all 15 are in Cloudinary, the `<!-- IMAGE_SLOT_n -->` comments get replaced with `<figure><img ...></figure>` (descriptive alt text, URLs from the public_ids). The 5 hero `featured_image`s are already set in `import-batch-02.json`.
