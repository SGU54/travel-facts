# Batch 08 — Image Manifest (japanforamericans · Food cluster)

13 heroes, no in-body. Download in this order (matches `import-batch-08.array.json`), prefix `1_`…`13_` (ALL must be numbered), into `content/batch-08/images/`.

| # | slug-hero | What it should show | Search |
|---|-----------|---------------------|--------|
| 1 | japanese-food-guide-first-timers | Spread of varied Japanese dishes | "Japanese food spread table" |
| 2 | how-to-order-and-eat-in-japan | Plastic food models / ticket machine | "Japanese restaurant plastic food display" |
| 3 | vegetarian-dietary-needs-japan | Veg / shojin ryori meal | "shojin ryori vegetarian Japanese" |
| 4 | ramen-types-explained | Bowl of ramen with toppings | "ramen bowl chashu egg" |
| 5 | sushi-guide-for-beginners | Nigiri sushi assortment | "nigiri sushi assortment" |
| 6 | must-try-japanese-dishes | Varied dishes — tempura/donburi | "Japanese dishes variety tempura" |
| 7 | convenience-store-food-guide | Konbini onigiri / shelves | "Japanese convenience store onigiri" |
| 8 | where-to-eat-in-tokyo | Tsukiji market food / Tokyo dining alley | "Tsukiji outer market food" |
| 9 | where-to-eat-in-kyoto | Nishiki Market or Pontocho lantern lane | "Pontocho alley Kyoto evening" |
| 10 | izakaya-guide-for-visitors | Izakaya interior / red lantern | "izakaya interior red lantern" |
| 11 | japanese-drinks-sake-beer-whisky | Sake set / highball / beer | "sake bottles cups" |
| 12 | food-tours-in-japan | Street-food grazing / market tour | "Japan street food market tour" |
| 13 | what-to-eat-in-osaka | Takoyaki / okonomiyaki on griddle | "takoyaki Osaka street food" |

(Full public_id = `japanforamericans/articles/<slug>-hero`; script derives it.)

## Upload + import
```
node scripts/upload-batch.mjs content/batch-08/images content/batch-08/import-batch-08.array.json
```
Confirm `media folder: japanforamericans/articles` and `Sorted by numeric prefix`, then `y`. Bulk-import → expect 13 × created. **Fills the empty `food-and-drink`, `what-to-eat`, and `where-to-eat` categories.**

## ⚠ Verification
See `VERIFY-MASTER.md` (now B5–B8). Food content is mostly stable general knowledge, but dietary/allergy guidance and a few specifics are flagged.
