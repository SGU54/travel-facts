# Batch 14 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-14.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-14-images.md` — what to download, in order, + upload command.

## Step 1 — Images
Download 6 heroes per `batch-14-images.md` into one folder, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-14.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-14.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (all prices soft); hero loads;
renders cleanly. Then publish via admin.

## ★ Currency notes (venue-specific — will date; re-verify before any major refresh)
- ROOFTOP BARS and MARKETS name specific venues, web-verified current as of mid-2026 with a
  "venues change — confirm before you go" caveat baked into each article. Re-verify the named
  venues (rooftops especially) before a future refresh, as bars open/close/rebrand.
- All prices kept soft/"check current"; market hours stated soft (food markets generally Mon-Sat
  mornings, closed Sun; Porta Portese = Sunday).

## Re-check outcome (verify-don't-vote-count in action)
Grok + Gemini clean on all 6. DeepSeek flagged 4 items:
- Tap-water wording (tourist-trap), Campo de' Fiori hours consistency + Trionfale closed-Sundays
  (markets): all ALREADY handled accurately in the written articles — no change needed.
- "Free alternatives" heading vs the paid Vittoriano lift (rooftop): already resolved in the
  article ("Free (and low-cost)... the first four are free; the Vittoriano is a cheap paid option").
- ★ DeepSeek claimed "The Vista" rooftop is "likely a fabrication" / "appears in no 2025-26
  roundups." WEB-VERIFIED FALSE: The Vista is real and current — active site (thevistarooftop.com),
  Instagram (16K, posting 2026), Tripadvisor reviews, and a 3-day-old Rome rooftop roundup naming
  it as their top pick on Via di Torre Argentina near the Pantheon. KEPT as written; DeepSeek was
  confidently wrong. Verification surfaced one real improvement: added that The Vista is book-ahead
  / membership-style, not a walk-up.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)
  - Note: roman-coffee-culture and avoid-tourist-trap-restaurants-rome have NO affiliate slots.

## Articles in this batch
1. roman-coffee-culture (coffee-gelato-aperitivo)
2. best-aperitivo-rome (coffee-gelato-aperitivo)
3. rooftop-bars-rome (coffee-gelato-aperitivo)
4. avoid-tourist-trap-restaurants-rome (roman-dishes)
5. where-to-eat-trastevere-testaccio (trattorias-and-dining)
6. best-markets-rome (roman-dishes)

## Done when
- [ ] 6 heroes uploaded to Cloudinary
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
