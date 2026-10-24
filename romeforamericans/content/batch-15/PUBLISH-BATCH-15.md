# Batch 15 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-15.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-15-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-15-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-15.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-15.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (all cost framed qualitatively —
zero hard prices in this batch); hero loads; renders cleanly. Then publish via admin.

## ★ Currency notes (will date — re-verify before any major refresh)
- 2026 SHORT-TERM RENTAL RULES (apartment-vs-hotel + family articles): Italy's CIN (Codice
  Identificativo Nazionale) is mandatory + displayed on legit listings; platforms must verify &
  delist non-compliant (EU reg from May 2026). The lockbox/key-box ban is REAL but NUANCED —
  Milan banned them on PUBLIC surfaces from Jan 2026, spreading, NOT yet nationwide, and Rome
  hasn't fully banned them as of mid-2026 (article states this precisely). Re-verify before refresh.
- Metro Line C reaches Colosseo (Dec 2025) — referenced in colosseum-vs-vatican.

## Re-check outcome (2 reviewers this round — Gemini skipped)
Grok clean on all 6. DeepSeek clean on 4, 2 minor precision fixes (both applied):
- apartment-vs-hotel: tightened the lockbox claim — it's a Milan PUBLIC-surface ban spreading,
  NOT a nationwide mandate, and Rome hasn't fully banned lockboxes yet (DeepSeek correctly caught
  the original wording overreached toward "universal"). Now precise.
- staying-near-termini: clarified walking distances — "the center is 15-20 min" was too generic;
  now distinguishes near (Trevi/Quirinale ~15-20) from farther (Pantheon/Navona ~20-25).
No factual errors; CIN + Line C + neighborhood facts all confirmed accurate by both reviewers.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)
  - Note: these 6 carry Booking.com slots (lodging category) — fill once that program is approved.

## Articles in this batch
1. colosseum-vs-vatican-where-to-stay (best-areas-to-stay)
2. staying-near-termini (best-areas-to-stay)
3. where-to-stay-trastevere (best-areas-to-stay)
4. hotels-with-a-view-rome (hotels-and-boutique)
5. family-friendly-stays-rome (budget-and-family)
6. apartment-vs-hotel-rome (budget-and-family)

## Done when
- [ ] 6 heroes uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
