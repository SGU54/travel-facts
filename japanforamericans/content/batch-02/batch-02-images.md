# Batch 02 — Image Manifest (japanforamericans · Tokyo cluster)

Same flow as batch 1. One hero per article, no in-body images. Download in this order (matches `import-batch-02.array.json`), prefix filenames `1_`…`4_` to force order, drop in `content/batch-02/images/`.

| # | public_id | Article | What it should show | Suggested search |
|---|-----------|---------|---------------------|------------------|
| 1 | `japanforamericans/articles/where-to-stay-in-tokyo-hero` | Where to Stay in Tokyo | Tokyo neighborhood at night — Shinjuku neon streets or a lit-up skyline with hotels | "Shinjuku Tokyo street night neon" |
| 2 | `japanforamericans/articles/best-things-to-do-in-tokyo-hero` | Best Things to Do in Tokyo | Iconic Tokyo composite feel — Senso-ji temple gate, or Shibuya Crossing crowd | "Senso-ji temple Asakusa" / "Shibuya Crossing crowd" |
| 3 | `japanforamericans/articles/best-day-trips-from-tokyo-hero` | Best Day Trips from Tokyo | Mt Fuji over Hakone / Lake Ashi, or Kamakura Great Buddha | "Mt Fuji Hakone Lake Ashi" / "Kamakura Great Buddha" |
| 4 | `japanforamericans/articles/tokyo-airport-transfers-hero` | Airport to Central Tokyo | Narita Express or Keisei Skyliner train at platform, or a Tokyo station scene | "Narita Express train platform" / "Keisei Skyliner" |

## Upload
From the repo root, with the corrected script:
```
node scripts/upload-batch.mjs content/batch-02/images content/batch-02/import-batch-02.array.json
```
The script auto-detects `japanforamericans` from the import file — confirm the preview line reads `Cloudinary folder: japanforamericans/articles`, then type `y`.

## Then
Bulk-import `import-batch-02.array.json` in the admin. All 4 categories already match the live schema, so expect 4 × "created" with working heroes — no remap needed.
