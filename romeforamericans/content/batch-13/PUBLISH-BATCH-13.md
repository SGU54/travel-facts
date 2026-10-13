# Batch 13 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-13.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-13-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-13-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-13.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-13.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen; hero loads; renders cleanly.
Then publish via admin.

## ★ Currency notes (will date — re-verify before any major refresh)
- **Metro Line C now reaches COLOSSEO** (San Giovanni→Colosseo extension opened Dec 16, 2025;
  interchanges Line B at Colosseo, Line A at San Giovanni). Extension to Piazza Venezia is years
  off (~2030). Verified vs Wikipedia + current transit sources. If a future refresh predates a
  further extension, update the metro article.
- **Leonardo Express ~€14** one-way (verified unchanged 2026), stated "check current."
- **Airport taxi fixed fares** to the center: kept SOFT (sources now vary, ~€48-55 FCO / ~€30-40
  Ciampino) — left as "check the current set rate."
- **Contactless tap-to-pay** at metro gates is live (ATAC).

## Re-check outcome
Grok + DeepSeek + Gemini ALL clean on all 6 — unanimous, no flags. All three independently
confirmed the Line C→Colosseo extension and Leonardo Express details. No changes needed.
(Independent grep re-audit also confirmed: only the stable €14 fare appears, always "check current.")

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)
  - Note: rome-metro-guide and rome-buses-trams-guide have NO affiliate slots by design (pure info).

## Articles in this batch
1. fiumicino-vs-ciampino (arrival-and-airports)
2. leonardo-express-fiumicino-trains (arrival-and-airports)
3. rome-metro-guide (metro-bus-tram)
4. rome-buses-trams-guide (metro-bus-tram)
5. renting-a-car-in-rome (taxis-and-transfers)
6. florence-high-speed-train (day-trips)

## Done when
- [ ] 6 heroes uploaded to Cloudinary
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
