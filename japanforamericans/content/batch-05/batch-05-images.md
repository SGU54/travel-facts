# Batch 05 — Image Manifest (japanforamericans · Stay + Ryokan/Onsen)

8 heroes, no in-body. Download in this order (matches `import-batch-05.array.json`), prefix `1_`…`8_`, into `content/batch-05/images/`.

| # | public_id | What it should show | Search |
|---|-----------|---------------------|--------|
| 1 | `japanforamericans/articles/japan-accommodation-types-explained-hero` | Split feel: tatami ryokan room / modern hotel | "Japanese ryokan tatami room" |
| 2 | `japanforamericans/articles/best-areas-to-stay-in-japan-hero` | Tokyo or Kyoto hotel-district streetscape | "Tokyo hotel district street" |
| 3 | `japanforamericans/articles/booking-hotels-in-japan-hero` (NOTE: public_id is `booking-hotels-in-japan-tips-hero`) | Compact Japanese business hotel room | "Japanese business hotel room" |
| 4 | `japanforamericans/articles/what-is-a-ryokan-hero` | Tatami room with futon / low table, yukata | "ryokan room futon tatami" |
| 5 | `japanforamericans/articles/onsen-etiquette-for-foreigners-hero` | Outdoor onsen bath, steam, scenic (no people / tasteful) | "outdoor onsen rotenburo steam" |
| 6 | `japanforamericans/articles/best-onsen-towns-near-tokyo-kyoto-hero` | Onsen town — Kinosaki canal w/ yukata strollers, or Hakone | "Kinosaki onsen town canal" |
| 7 | `japanforamericans/articles/tattoos-and-onsen-hero` | Private onsen bath (kashikiri) — tasteful, scenic | "private onsen bath wood" |
| 8 | `japanforamericans/articles/where-to-stay-in-osaka-hero` | Dotonbori neon at night, or Umeda skyline | "Osaka Dotonbori neon night" |

⚠ Filename note: the 3rd article's public_id is `booking-hotels-in-japan-tips-hero` (with `-tips`). The script reads it from the JSON, so just keep image #3 in the 3rd slot — no action needed.

## Upload + import
```
node scripts/upload-batch.mjs content/batch-05/images content/batch-05/import-batch-05.array.json
```
Confirm folder `japanforamericans/articles`, `y`, then bulk-import `import-batch-05.array.json`. All categories valid → expect 8 × created.

## ⚠ Before publishing: read `batch-05-verify.md` — these are written from general knowledge, not FINAL.json.
