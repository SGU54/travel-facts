# Batch 01 — Image Manifest (japanforamericans)

Download these in order and drop them in one folder. The order matches `import-batch-01.json` exactly, so `upload-batch.mjs <folder> import-batch-01.json` will assign each to the right `public_id`. One hero per article, no in-body images this batch.

To force order, prefix filenames `1_`, `2_`, … `7_`.

| # | public_id | Article | What it should show | Suggested source search |
|---|-----------|---------|---------------------|--------------------------|
| 1 | `japanforamericans/articles/do-americans-need-visa-japan-hero` | Do Americans Need a Visa for Japan? | US passport with a Japan airport immigration / arrival backdrop; clean, bright | "US passport Japan airport immigration" |
| 2 | `japanforamericans/articles/flights-to-japan-from-us-hero` | Flights to Japan from the US | JAL or ANA wide-body aircraft at gate, or airliner over Tokyo skyline | "ANA JAL aircraft airport" / "airplane over Tokyo" |
| 3 | `japanforamericans/articles/is-japan-safe-for-americans-hero` | Is Japan Safe for American Travelers? | Calm, orderly Japanese street at dusk (e.g. quiet Tokyo neighborhood, people walking safely) | "quiet Tokyo street evening safe" |
| 4 | `japanforamericans/articles/money-in-japan-cash-cards-ic-hero` | Money in Japan | Japanese yen banknotes and coins, or a Suica/IC card being tapped at a ticket gate | "Japanese yen cash" / "Suica IC card tap gate" |
| 5 | `japanforamericans/articles/best-time-to-visit-japan-hero` | Best Time to Visit Japan | Cherry blossoms over a temple OR autumn maples in Kyoto (a seasonal split shot is ideal) | "cherry blossoms Japan temple" / "Kyoto autumn foliage" |
| 6 | `japanforamericans/articles/japan-etiquette-for-americans-hero` | Japan Etiquette | Shoes removed at a ryokan/temple entrance, or a polite bow greeting | "shoes removed ryokan entrance" / "Japanese bow greeting" |
| 7 | `japanforamericans/articles/getting-around-japan-trains-jr-pass-hero` | Getting Around Japan | Shinkansen bullet train at a platform (nose shot) or Tokyo station with IC gates | "Shinkansen bullet train platform" |

## Notes
- Use landscape, high-res images. Descriptive **alt text** is added during the clean phase in travel-content-pipeline.
- Avoid identifiable individual faces in close-up where possible; crowd/wide shots are fine.
- After filling the folder in order, run from the repo root:
  ```
  node scripts/upload-batch.mjs <images-folder> import-batch-01.json
  ```
  Review the preview table, then type `y`.
