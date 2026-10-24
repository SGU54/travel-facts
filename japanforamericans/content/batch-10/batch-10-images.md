# Batch 10 — Image Manifest (japanforamericans · new itinerary articles)

8 hero images, no in-body images. Download in this order (matches `import-batch-10.array.json`), prefix every file `1_`…`8_` (ALL numbered so the upload script orders by numeric prefix), into `content/batch-10/images/`.

| # | slug-hero | What it should show | Suggested search |
|---|-----------|---------------------|------------------|
| 1 | 1-week-in-japan-itinerary | Shinkansen + Mt Fuji, or a classic Tokyo/Kyoto split image — the "essentials" feel | "Shinkansen Mt Fuji" |
| 2 | 5-days-in-japan-itinerary | A single iconic, focused shot (Fushimi Inari torii or Tokyo skyline) — short-trip punch | "Fushimi Inari torii gates" |
| 3 | 10-days-in-japan-itinerary | A varied/scenic shot suggesting range — e.g. Kyoto temple with hills, or a montage-style landscape | "Kyoto temple autumn" |
| 4 | 2-weeks-in-japan-itinerary | Something hinting at breadth incl. the west — Miyajima floating torii, or Himeji Castle | "Miyajima floating torii gate" |
| 5 | 3-weeks-in-japan-itinerary | Off-the-trail / mountain Japan — Japan Alps, Shirakawa-go thatched village, or Takayama street | "Shirakawa-go village" |
| 6 | japan-itinerary-ideas | A planning/map vibe — a Japan map, a rail map, or a traveler with a guidebook | "Japan travel map planning" |
| 7 | japan-second-trip-itinerary | A lesser-known destination — Kanazawa garden, Kumano Kodo trail, or a quiet onsen town | "Kanazawa Kenrokuen garden" |
| 8 | how-to-plan-first-japan-itinerary | Planning/prep imagery — itinerary notebook, Shinkansen platform, or a traveler at a station | "Tokyo station Shinkansen platform" |

(Full public_id = `japanforamericans/articles/<slug>-hero`; the upload script derives the folder from the import file's public_ids.)

## Upload + import
```
node scripts/upload-batch.mjs content/batch-10/images content/batch-10/import-batch-10.array.json
```
Confirm the script prints `media folder: japanforamericans/articles` and `Sorted by numeric prefix`, type `y`, then run the bulk import.

## IMPORTANT — these are NEW articles (creates, not updates)
- All 8 have `status: "draft"`. On import they should report **8 × created** (not "updated"). If your tool is the upsert-by-slug batch-update, that's fine — none of these slugs exist yet, so they'll be inserted as new draft rows.
- After import, they'll sit as **drafts**. Review, then publish when ready.

## Categories filled
- `itineraries-by-length`: +5 (5-day, 1-week, 10-day, 2-week, 3-week) — was 0
- `itineraries`: +2 (ideas hub, second-trip) — was thin
- `first-timer-itineraries`: +1 (how-to-plan) — was 1

## Note on image sourcing
Same rules as your earlier batches: avoid anything with identifiable people as the focus, avoid copyrighted/branded material, and favor clean landscape/landmark shots that crop well to a hero aspect ratio. Numbered prefixes are required for correct ordering.
