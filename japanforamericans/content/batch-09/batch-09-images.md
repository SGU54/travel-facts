# Batch 09 — Image Manifest (japanforamericans · Transport + Connectivity)

13 heroes, no in-body. Download in this order (matches `import-batch-09.array.json`), prefix `1_`…`13_` (ALL numbered), into `content/batch-09/images/`.

| # | slug-hero | What it should show | Search |
|---|-----------|---------------------|--------|
| 1 | japan-esim-sim-guide | Phone showing SIM/eSIM / Japan map data | "smartphone eSIM travel Japan" |
| 2 | pocket-wifi-vs-esim-japan | Pocket WiFi device / phone connectivity | "pocket wifi device travel" |
| 3 | suica-pasmo-ic-card-guide | IC card tapped at ticket gate | "Suica IC card ticket gate tap" |
| 4 | tokyo-subway-explained | Tokyo subway train / network map | "Tokyo subway train platform" |
| 5 | navigating-japanese-train-stations | Busy station concourse with signage | "Tokyo station concourse signs" |
| 6 | japan-rail-pass-worth-it | Shinkansen at platform / JR Pass | "Shinkansen platform Japan Rail" |
| 7 | how-to-ride-the-shinkansen | Bullet train nose at platform | "Shinkansen nose platform" |
| 8 | renting-a-car-in-japan | Car on a scenic rural Japan road | "driving rural Japan road" |
| 9 | japanese-immigration-what-to-expect | Airport immigration / arrivals hall | "Japan airport arrivals immigration" |
| 10 | visit-japan-web-how-to-use | Phone QR code at airport kiosk | "airport QR code kiosk scan" |
| 11 | kansai-airport-to-kyoto-osaka | Kansai airport / Haruka train | "Kansai airport train Haruka" |
| 12 | narita-vs-haneda-which-airport | Tokyo airport exterior / N'EX train | "Narita Express train Tokyo" |
| 13 | passport-requirements-for-japan | US passport (Japan arrival context) | "US passport travel" |

(Full public_id = `japanforamericans/articles/<slug>-hero`; script derives it.)

## Upload + import
```
node scripts/upload-batch.mjs content/batch-09/images content/batch-09/import-batch-09.array.json
```
Confirm `media folder: japanforamericans/articles` + `Sorted by numeric prefix`, `y`, bulk-import → expect 13 × created. **Fills the empty `connectivity` and `local-transit-ic-cards` categories.**

## ⚠ Verification
See `VERIFY-MASTER.md` (now B5–B9). The SIM/eSIM articles NAME providers (Airalo, Ubigi, Holafly, Sakura Mobile, Mobal, IIJmio) and the JR Pass / Haruka / airport details — all flagged HIGH because plans, prices, and pass rules change.
