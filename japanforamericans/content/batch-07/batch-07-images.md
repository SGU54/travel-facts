# Batch 07 — Image Manifest (japanforamericans · Things to Do + Day Trips + Temples)

13 heroes, no in-body. Download in this order (matches `import-batch-07.array.json`), prefix `1_`…`13_`, into `content/batch-07/images/`. (All files must be numbered, or the script falls back to file-date order.)

| # | slug-hero | What it should show | Search |
|---|-----------|---------------------|--------|
| 1 | best-things-to-do-in-osaka | Dotonbori neon canal at night | "Osaka Dotonbori canal neon" |
| 2 | teamlab-tokyo-guide | Immersive digital-art light room | "teamlab digital art lights" |
| 3 | best-free-things-to-do-in-japan | Free icon — Fushimi torii or a park | "Fushimi Inari torii path" |
| 4 | hakone-day-trip-guide | Lake Ashi torii + Mt Fuji / ropeway | "Hakone Lake Ashi Mt Fuji torii" |
| 5 | nara-day-trip-guide | Nara deer with Todai-ji / park | "Nara deer Todai-ji park" |
| 6 | nikko-day-trip-guide | Toshogu Shrine ornate gate / Shinkyo bridge | "Nikko Toshogu shrine" |
| 7 | senso-ji-temple-guide | Kaminarimon lantern / Nakamise | "Senso-ji Kaminarimon lantern" |
| 8 | fushimi-inari-shrine-guide | Torii gate tunnel | "Fushimi Inari torii tunnel" |
| 9 | meiji-shrine-guide | Forest torii approach / sake barrels | "Meiji Shrine torii forest" |
| 10 | temple-shrine-etiquette-japan | Purification fountain (temizuya) / torii | "shrine purification fountain temizuya" |
| 11 | kamakura-day-trip-guide | Great Buddha (Daibutsu) open-air | "Kamakura Great Buddha Daibutsu" |
| 12 | himeji-castle-day-trip-guide | White Heron castle, ideally with blossoms | "Himeji Castle white" |
| 13 | best-things-to-do-in-japan | Iconic composite — Shinkansen+Fuji or Fushimi | "Shinkansen Mt Fuji" |

(Full public_id = `japanforamericans/articles/<slug>-hero`; script derives it from the JSON.)

## Upload + import
```
node scripts/upload-batch.mjs content/batch-07/images content/batch-07/import-batch-07.array.json
```
Confirm `media folder: japanforamericans/articles` and `Sorted by numeric prefix`, then `y`. Bulk-import → expect 13 × created. **Fills the empty `temples-and-shrines` category (+4).**

## ⚠ Verification
See `VERIFY-MASTER.md` (now covers B5–B7). Most of this batch leans on the verified FINAL.json sight pools (Osaka, Hakone, Nara, Nikko, Kamakura, Himeji, Senso-ji, Fushimi Inari, Meiji), so risk is moderate — new specifics flagged there.
