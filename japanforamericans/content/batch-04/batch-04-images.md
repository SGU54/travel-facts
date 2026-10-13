# Batch 04 — Image Manifest (japanforamericans · money pages)

Two heroes, no in-body images. Download in this order (matches `import-batch-04.array.json`), prefix `1_`/`2_`, drop in `content/batch-04/images/`.

| # | public_id | Article | What it should show | Suggested search |
|---|-----------|---------|---------------------|------------------|
| 1 | `japanforamericans/articles/japan-itinerary-7-days-hero` | Japan in 7 Days | Shinkansen with Mt Fuji, or a classic Tokyo+Kyoto composite feel (bullet train is ideal — ties the itinerary together) | "Shinkansen Mt Fuji" / "bullet train Japan countryside" |
| 2 | `japanforamericans/articles/best-places-to-visit-in-japan-hero` | Best Places to Visit in Japan | Iconic wide Japan shot — Fushimi Inari torii, Mt Fuji over a pagoda (Chureito), or Kinkaku-ji | "Chureito Pagoda Mt Fuji" / "Fushimi Inari torii" |

## Upload
```
node scripts/upload-batch.mjs content/batch-04/images content/batch-04/import-batch-04.array.json
```
Confirm `Cloudinary folder: japanforamericans/articles`, then `y`.

## Then
Bulk-import `import-batch-04.array.json`. Both categories match the live schema → expect 2 × "created."

### Category note
`best-places-to-visit-in-japan` is filed under **`plan-your-trip`** (top-of-funnel overview). If you'd rather it sit under `itineraries` or `first-timer-itineraries`, change the one `category_slug` value in the JSON before importing — both are valid slugs in your schema.
