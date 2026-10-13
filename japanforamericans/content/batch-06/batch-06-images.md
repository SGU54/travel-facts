# Batch 06 — Image Manifest (japanforamericans · Tokyo + Kyoto pages & neighborhoods)

12 heroes, no in-body. Download in this order (matches `import-batch-06.array.json`), prefix `1_`…`12_`, into `content/batch-06/images/`.

| # | public_id (slug-hero) | What it should show | Search |
|---|------------------------|---------------------|--------|
| 1 | tokyo-travel-guide-first-timers | Tokyo skyline / cityscape overview | "Tokyo skyline daytime" |
| 2 | 3-days-in-tokyo-itinerary | Iconic Tokyo montage feel — Shibuya or skyline | "Shibuya Tokyo street day" |
| 3 | tokyo-with-kids-family-guide | Family-friendly Tokyo — colorful, teamLab-ish or park | "family Tokyo colorful attraction" |
| 4 | tokyo-nightlife-evening-districts | Neon nightlife — Shinjuku / Golden Gai at night | "Shinjuku neon night bars" |
| 5 | kyoto-travel-guide-first-timers | Kyoto overview — pagoda / temple with hills | "Kyoto temple cityscape" |
| 6 | 2-days-in-kyoto-itinerary | Higashiyama street or Kiyomizu-dera | "Kiyomizu-dera Kyoto" |
| 7 | kyoto-temples-which-to-prioritize | Fushimi Inari torii or Kinkaku-ji | "Kinkaku-ji golden pavilion" |
| 8 | shinjuku-area-guide | Shinjuku skyscrapers / station area | "Shinjuku skyscrapers Tokyo" |
| 9 | shibuya-harajuku-area-guide | Shibuya Crossing or Takeshita Street | "Shibuya Crossing crowd" |
| 10 | asakusa-old-tokyo-area-guide | Senso-ji Kaminarimon gate / Nakamise | "Senso-ji Kaminarimon Asakusa" |
| 11 | gion-higashiyama-area-guide | Gion wooden street / Hanamikoji at dusk | "Gion Hanamikoji Kyoto evening" |
| 12 | arashiyama-area-guide | Arashiyama bamboo grove | "Arashiyama bamboo grove" |

(Full public_id = `japanforamericans/articles/<slug>-hero` — the script derives it from the JSON.)

## Upload + import
```
node scripts/upload-batch.mjs content/batch-06/images content/batch-06/import-batch-06.array.json
```
Confirm folder `japanforamericans/articles`, `y`, then bulk-import. All categories valid → expect 12 × created. **This batch fills the empty `tokyo` (+4) and `kyoto` (+3) landing pages** you screenshotted.

## ⚠ Verification
See `VERIFY-MASTER.md` (cumulative). Batch 6 is lower-risk than batch 5 — mostly sight/neighborhood facts already corroborated by FINAL.json's Tokyo/Kyoto pools — but a few new specifics are flagged there.
