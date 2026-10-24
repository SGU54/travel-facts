# Batch 03 — Image Manifest (thailandforamericans)

**How to use:** Download one image per entry below, **in this exact order**, into a single folder. Then:

```
node scripts/upload-batch.mjs <your-images-folder> articles/import-batch-03.json
```

**15 images expected** (5 heroes + 10 in-body). Candidate links are pages to pick from, not direct downloads. Choose **landscape, ≥1600px**, sharp. Unsplash & Pexels = free commercial, no attribution. **No recognizable faces, no brand/logo signage.**

---

## 1 — `thailandforamericans/articles/3-days-in-bangkok-itinerary-hero`
**Brief:** An iconic Bangkok scene — Grand Palace or Wat Arun glowing, the city behind. Bright, inviting.
- https://unsplash.com/s/photos/bangkok%20grand%20palace
- https://www.pexels.com/search/bangkok%20temple/

## 2 — `thailandforamericans/articles/3-days-in-bangkok-itinerary-1`
**Brief:** Grand Palace or Wat Arun glowing, with the Bangkok skyline beyond.
- https://unsplash.com/photos/wat-arun-temple-on-chao-phraya-river-bangkok-wd3tQvk0WXA
- https://unsplash.com/s/photos/wat%20arun
- https://www.pexels.com/search/wat%20arun/

## 3 — `thailandforamericans/articles/3-days-in-bangkok-itinerary-2`
**Brief:** A bustling Bangkok market, OR a rooftop bar view over the skyline at dusk.
- https://unsplash.com/s/photos/bangkok%20rooftop%20skyline
- https://unsplash.com/s/photos/bangkok%20market
- https://www.pexels.com/search/bangkok%20night/

---

## 4 — `thailandforamericans/articles/best-thailand-itinerary-first-timers-hero`
**Brief:** A bright, iconic Thailand scene that signals "first big trip" — temple, beach, or sweeping landscape.
- https://unsplash.com/s/photos/thailand
- https://www.pexels.com/search/thailand/

## 5 — `thailandforamericans/articles/best-thailand-itinerary-first-timers-1`
**Brief:** A bold, aspirational Thailand image — temple spire or turquoise bay, bright daylight.
- https://unsplash.com/s/photos/thailand%20travel
- https://www.pexels.com/search/thailand%20travel/

## 6 — `thailandforamericans/articles/best-thailand-itinerary-first-timers-2`
**Brief:** A scene evoking the north-vs-south choice — a northern temple/mountain or an island beach (pick one strong shot).
- https://unsplash.com/s/photos/chiang%20mai%20temple
- https://unsplash.com/s/photos/thailand%20island%20beach
- https://www.pexels.com/search/thailand%20scenery/

---

## 7 — `thailandforamericans/articles/beaches-only-thailand-itinerary-hero`
**Brief:** A dreamy Thai beach — clear shallow water, a longtail boat, soft sand. The "all beaches" hero.
- https://unsplash.com/s/photos/thailand%20beach
- https://www.pexels.com/search/thailand%20beach/

## 8 — `thailandforamericans/articles/beaches-only-thailand-itinerary-1`
**Brief:** A dreamy Thai beach with clear shallow water and a longtail boat.
- https://unsplash.com/s/photos/thailand%20longtail%20beach
- https://www.pexels.com/search/longtail%20boat%20beach/

## 9 — `thailandforamericans/articles/beaches-only-thailand-itinerary-2`
**Brief:** A wide, map-like aerial suggesting island-hopping across turquoise sea (multiple islands/boats).
- https://unsplash.com/s/photos/thailand%20islands%20aerial
- https://www.pexels.com/search/thailand%20aerial%20islands/

---

## 10 — `thailandforamericans/articles/domestic-flights-thailand-hero`
**Brief:** A plane on the tarmac or a bright wing-over-tropics view — travel/aviation feel. No airline branding.
- https://unsplash.com/s/photos/airplane%20wing%20tropical
- https://www.pexels.com/search/airplane%20travel/

## 11 — `thailandforamericans/articles/domestic-flights-thailand-1`
**Brief:** A plane on the tarmac or a wing view, bright and travel-y (no readable airline logos).
- https://unsplash.com/s/photos/airplane%20tarmac
- https://www.pexels.com/search/airplane%20tarmac/

## 12 — `thailandforamericans/articles/domestic-flights-thailand-2`
**Brief:** Aerial view of tropical Thai islands from a plane window.
- https://unsplash.com/s/photos/islands%20from%20plane%20window
- https://www.pexels.com/search/island%20aerial%20window/

---

## 13 — `thailandforamericans/articles/bangkok-to-islands-transport-hero`
**Brief:** A longtail boat or passenger ferry heading toward a Thai island over turquoise water.
- https://unsplash.com/s/photos/thailand%20ferry%20island
- https://www.pexels.com/search/thailand%20boat/

## 14 — `thailandforamericans/articles/bangkok-to-islands-transport-1`
**Brief:** A longtail boat heading toward a Thai island, OR a ferry on turquoise water.
- https://unsplash.com/s/photos/longtail%20boat%20thailand
- https://www.pexels.com/search/longtail%20boat%20thailand/

## 15 — `thailandforamericans/articles/bangkok-to-islands-transport-2`
**Brief:** A passenger ferry approaching a Gulf island like Koh Samui.
- https://unsplash.com/s/photos/thailand%20ferry
- https://www.pexels.com/search/passenger%20ferry%20tropical/

---

### After upload
Once all 15 are in R2, the `<!-- IMAGE_SLOT_n -->` comments get replaced with `<figure><img ...></figure>` (descriptive alt, URLs from the public_ids). The 5 hero `featured_image`s are already set in `import-batch-03.json`.
