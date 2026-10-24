# Batch 03 — Image Manifest (japanforamericans · Kyoto cluster)

One hero per article, no in-body images. Download in this order (matches `import-batch-03.array.json`), prefix `1_`…`4_`, drop in `content/batch-03/images/`.

| # | public_id | Article | What it should show | Suggested search |
|---|-----------|---------|---------------------|------------------|
| 1 | `japanforamericans/articles/where-to-stay-in-kyoto-hero` | Where to Stay in Kyoto | Gion lantern-lit wooden street at dusk, or Higashiyama old lane | "Gion Kyoto street evening" / "Higashiyama old street" |
| 2 | `japanforamericans/articles/best-things-to-do-in-kyoto-hero` | Best Things to Do in Kyoto | Kinkaku-ji golden pavilion on the pond, or Fushimi Inari torii tunnel | "Kinkaku-ji golden pavilion" / "Fushimi Inari torii gates" |
| 3 | `japanforamericans/articles/best-day-trips-from-kyoto-hero` | Best Day Trips from Kyoto | Nara deer with Todai-ji, or Himeji Castle white facade | "Nara deer Todai-ji" / "Himeji Castle" |
| 4 | `japanforamericans/articles/getting-around-kyoto-hero` | Getting Around Kyoto | Kyoto city bus on a street, or a Higashiyama walking lane with people | "Kyoto city bus street" / "Kyoto Higashiyama walking street" |

## Upload
From the repo root:
```
node scripts/upload-batch.mjs content/batch-03/images content/batch-03/import-batch-03.array.json
```
Confirm the preview reads `media folder: japanforamericans/articles`, then `y`.

## Then
Bulk-import `import-batch-03.array.json` in the admin. All 4 categories match the live schema → expect 4 × "created" with working heroes. No remap.
