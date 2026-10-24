# Batch 17 — Publishing guide (THE FINAL SIX — completes all 96)

Same flow: images -> import -> review -> publish. **No internal links, no affiliates**
(both deferred to the refine pass). From the site repo root, with apps/admin/.env.local
present. Schema is rome.

## Files
- import-batch-17.json — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- batch-17-images.md — image manifest with curated Unsplash/Pexels candidate links.

## Step 1 — Images
Pick + download 6 heroes per batch-17-images.md into one folder, in order, then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-17.json
```
(is-rome-safe: choose a welcoming Rome scene, not crime/police imagery.)

## Step 2 — Import as draft (idempotent)
POST import-batch-17.json to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Facts match facts.json; no serve_live value frozen (zero hard prices — the various "%" are the
US-tipping-habit contrast or figures of speech, NOT Rome prices); hero loads; renders cleanly.

## Currency / accuracy notes
- is-rome-safe: web-verified against multiple 2026 sources — Rome safe by Euro standards,
  violent crime rare, pickpocketing the concentrated risk (Line A, 64/40, Colosseum, Trevi,
  Vatican queue, Termini), lower crime index than Paris/Barcelona, tap water safe, EU 112.
  Written deliberately proportionate (aware-not-afraid).
- Tipping: not obligatory (full wage, not US tipped-subminimum); coperto/servizio explained.

## Re-check outcome (2 reviewers — DeepSeek + Gemini; no Grok this round)
DeepSeek: clean on 5, 1 fix. Gemini: clean on 2, fixes on 4. I web-verified the factual-history
flags before applying:
- ★ TRAPIZZINO ORIGIN (Gemini, correct — web-verified): trapizzino was invented by Stefano
  Callegari in 2008 at his shop "00100" on Via Giovanni Branca in Testaccio, NOT "at the market"
  (the covered hall opened 2012). FIXED to "born in the Testaccio neighborhood (Callegari's
  creation), championed by the market's stalls."
- ★ MARKET "RELOCATED 2012" (DeepSeek, correct — web-verified): the market was REBUILT IN SITU
  on its Testaccio site (modern hall opened 2012), not moved from elsewhere. FIXED to "housed in
  a purpose-built structure since 2012 (rebuilt on its Testaccio site)."
- crime-index phrasing (Gemini): clarified "rates lower than Paris/Barcelona" -> "rates as safer
  than." APPLIED.
- tipping ~10% guide tip (Gemini): removed the percentage (self-undermining in a "drop the %
  reflex" article) -> cash gesture. APPLIED.
- Palazzo Massimo "a full hour" (Gemini called it contradiction w/ "sleeper hit"): softened to
  "a good hour or more" — light touch, not the mandated "two hours." APPLIED.
- Gemini fine-dining + DeepSeek fine-dining "notes": both self-marked "not an error / acceptable."
  No change. Correctly non-flags.

## Deferred to the REFINE PASS (NOT this batch)
- Internal links (one comprehensive pass across all 96)
- Affiliate links + disclosure
  - Note: is-rome-safe, tipping-in-italy, esquilino-termini-guide, ostiense-street-art-guide
    have NO affiliate slots; fine-dining + testaccio-food-market carry GetYourGuide slots.

## Articles in this batch
1. is-rome-safe (safety-and-scams)
2. tipping-in-italy (money-and-costs)
3. esquilino-termini-guide (monti-and-esquilino)
4. ostiense-street-art-guide (testaccio-and-ostiense)
5. fine-dining-rome (trattorias-and-dining)
6. testaccio-food-market (testaccio-and-ostiense)

## Done when
- [ ] 6 heroes picked, verified, uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin   ->   ★ THIS COMPLETES ALL 96 ARTICLES
