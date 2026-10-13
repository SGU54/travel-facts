# Batch 01 — Image Manifest (thailandforamericans)

**How to use this:** Download one image for each entry below, **in this exact order**, into a single folder. Then run:

```
node scripts/upload-batch.mjs <your-images-folder> articles/import-batch-01.json
```

The script maps your folder (sorted by download order) to these Cloudinary public_ids, previews the mapping, and uploads only after you confirm. If the count doesn't match (15 images expected), it stops and shows both lists.

**Picking rules for every image:**
- The candidate links are **pages to pick from**, not guaranteed direct downloads.
- Unsplash & Pexels = free for commercial use, no attribution required.
- Choose **landscape, ≥1600px wide**, sharp.
- **No recognizable faces** and **no brand/logo signage** (standing rule for this site).
- For the insurance/scooter and "comparing options" shots especially: keep them generic — no readable license plates, no identifiable people.

**Total images to source: 15** (5 heroes + 10 in-body).

---

## 1 — `thailandforamericans/articles/7-day-thailand-itinerary-hero`
**Brief:** Iconic, welcoming establishing shot that says "Thailand trip" — a temple spire or the Bangkok riverside, bright and inviting.
- https://unsplash.com/photos/wat-arun-temple-on-chao-phraya-river-bangkok-wd3tQvk0WXA
- https://unsplash.com/s/photos/thailand%20temple
- https://www.pexels.com/search/thailand%20temple/

## 2 — `thailandforamericans/articles/7-day-thailand-itinerary-1`
**Brief:** Wide establishing shot of Bangkok at dusk — temple spires against the modern skyline.
- https://unsplash.com/photos/wat-arun-temple-illuminated-at-sunset-with-colorful-sky-MKVGJ4d3E6c
- https://unsplash.com/s/photos/bangkok-skyline
- https://www.pexels.com/search/bangkok%20skyline/

## 3 — `thailandforamericans/articles/7-day-thailand-itinerary-2`
**Brief:** A longtail boat anchored off a limestone karst in the Andaman Sea (the southern-islands leg).
- https://unsplash.com/s/photos/railay%20longtail%20boat
- https://unsplash.com/s/photos/phang%20nga%20bay
- https://www.pexels.com/search/longtail%20boat%20thailand/

---

## 4 — `thailandforamericans/articles/where-to-stay-in-bangkok-hero`
**Brief:** Bangkok cityscape that reads "where to stay" — high-rises, ideally with the BTS Skytrain or river in frame, golden hour.
- https://unsplash.com/s/photos/bangkok%20city
- https://www.pexels.com/search/bangkok%20city/

## 5 — `thailandforamericans/articles/where-to-stay-in-bangkok-1`
**Brief:** The BTS Skytrain gliding past Bangkok high-rises at golden hour.
- https://unsplash.com/s/photos/bangkok%20skytrain
- https://www.pexels.com/search/bangkok%20bts%20skytrain/

## 6 — `thailandforamericans/articles/where-to-stay-in-bangkok-2`
**Brief:** A lively Bangkok street-food scene at night with neon and food carts (no recognizable faces).
- https://unsplash.com/s/photos/bangkok%20street%20food%20night
- https://www.pexels.com/search/bangkok%20street%20food/

---

## 7 — `thailandforamericans/articles/which-thai-island-is-right-for-you-hero`
**Brief:** A turquoise Andaman bay with limestone karsts — the "which island" decision image.
- https://unsplash.com/s/photos/thailand%20island
- https://www.pexels.com/search/thailand%20island/

## 8 — `thailandforamericans/articles/which-thai-island-is-right-for-you-1`
**Brief:** Turquoise Andaman bay with limestone karsts (Phi Phi / Phang Nga feel), bright daylight.
- https://unsplash.com/s/photos/phi%20phi%20islands
- https://www.pexels.com/search/phi%20phi%20island/

## 9 — `thailandforamericans/articles/which-thai-island-is-right-for-you-2`
**Brief:** A quiet longtail-dotted beach with clear shallow water, fewer crowds (calm island contrast).
- https://unsplash.com/s/photos/koh%20lanta%20beach
- https://unsplash.com/s/photos/quiet%20thailand%20beach
- https://www.pexels.com/search/thailand%20quiet%20beach/

---

## 10 — `thailandforamericans/articles/best-esim-sim-thailand-hero`
**Brief:** A traveler's phone held up with a Thai backdrop (beach or Bangkok street) — connectivity theme. Keep any face out of frame or from behind.
- https://unsplash.com/s/photos/phone%20travel%20thailand
- https://www.pexels.com/search/phone%20travel/

## 11 — `thailandforamericans/articles/best-esim-sim-thailand-1`
**Brief:** A traveler checking their phone with a Thai beach or Bangkok street behind (hands/phone focus, no clear face).
- https://unsplash.com/s/photos/holding%20phone%20street
- https://www.pexels.com/search/holding%20smartphone%20travel/

## 12 — `thailandforamericans/articles/best-esim-sim-thailand-2`
**Brief:** Close-up of a phone showing a map app (generic map UI, no readable personal data).
- https://unsplash.com/s/photos/phone%20map%20app
- https://www.pexels.com/search/smartphone%20map/

---

## 13 — `thailandforamericans/articles/travel-insurance-thailand-hero`
**Brief:** A scooter/motorbike parked on a scenic Thai island road — the classic "risk" image, calm and clean. No people, no readable plates.
- https://unsplash.com/s/photos/scooter%20thailand%20island
- https://www.pexels.com/search/scooter%20thailand/

## 14 — `thailandforamericans/articles/travel-insurance-thailand-1`
**Brief:** A rented scooter parked by a tropical road or beach (reinforces the motorbike-risk point). Generic, no identifiable rider.
- https://unsplash.com/s/photos/motorbike%20thailand%20beach
- https://www.pexels.com/search/motorbike%20thailand/

## 15 — `thailandforamericans/articles/travel-insurance-thailand-2`
**Brief:** A traveler comparing options on a laptop (hands-on-keyboard / over-shoulder, no clear face, no brand screens). A neutral "planning" shot.
- https://unsplash.com/s/photos/laptop%20planning%20travel
- https://www.pexels.com/search/planning%20trip%20laptop/

---

### After upload
Once `upload-batch.mjs` confirms all 15 are in Cloudinary, the `<!-- IMAGE_SLOT_n -->` comments in the article HTML get replaced with `<figure><img ...></figure>` tags (descriptive alt text, URLs built from the public_ids). The 5 `featured_image` heroes are already set in `import-batch-01.json`.
