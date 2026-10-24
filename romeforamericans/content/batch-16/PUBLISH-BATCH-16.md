# Batch 16 — Publishing guide (6 articles)

Same flow: images → import → review → publish. **No internal links, no affiliates**
(both deferred to end of project). From the site repo root, with `apps/admin/.env.local`
present. Schema is `rome`.

## Files
- `import-batch-16.json` — 6 articles, cleaned HTML, categories, excerpts, hero IDs.
- `batch-16-images.md` — TEST image manifest WITH curated candidate links per article
  (Unsplash/Pexels/Wikimedia photo-pages + gallery-pages to pick from).

## Step 1 — Images (TEST RUN — option 1)
For each article, open the candidate links in `batch-16-images.md`, pick one hero, download
into one folder IN ORDER. These are pages to choose from, not guaranteed direct-download
URLs — verify each: live, >=1600px landscape, license OK (Unsplash/Pexels free commercial;
Wikimedia check the specific licence), no recognizable faces / brand signage. Then:
```
node scripts/upload-batch.mjs <images-folder> import-batch-16.json
```

## Step 2 — Import as draft (idempotent)
POST `import-batch-16.json` to the admin import API. Lands as draft.

## Step 3 — Review against the quality gate, then publish
Per article: facts match facts.json; no serve_live value frozen (zero hard prices in this
batch — only "15-20%" describing the US tipping habit being contrasted); hero loads; renders
cleanly. Then publish via admin.

## ★ Currency notes (2026 calendar — will date; re-verify before any major refresh)
- ★ EASTER 2026 = SUNDAY APRIL 5 (Palm Sun Mar 29, Good Fri Apr 3). Verified across many
  sources. Both the March and April sections of rome-month-by-month reflect this.
- Natale di Roma Apr 21 (festivities Apr 17-21) — NOT a public holiday, transport/shops normal.
- Ferragosto Aug 15 — locals leave, some closures, Vatican Museums closed Aug 14-15
  (reflected in both month-by-month and rome-in-summer).
- Sts Peter & Paul Jun 29 (city holiday); Liberation Day Apr 25; Festa della Repubblica Jun 2;
  Labor Day May 1; European Heritage Days mid-late Sept.
- ★ 2025 JUBILEE IS OVER — 2026 crowds subside vs the Holy Year, but Rome still busy.
- Trevi basin free after 10pm; Pantheon timed-entry; Metro Line C reaches Colosseo.

## Re-check outcome (★ verify-don't-vote-count — a real catch)
3 reviewers; DISAGREED on Easter, so I web-verified rather than vote-counting:
- ★ EASTER DATE: my draft said "late March" (WRONG). DeepSeek said April 5 (RIGHT). Gemini
  said March 29 (WRONG — that's Palm Sunday). Grok rubber-stamped my wrong "late March" (MISS).
  Web-verified across ~12 sources: Easter 2026 = APRIL 5. FIXED both the March and April
  sections. This is exactly why we verify every flag instead of counting votes.
- Natale di Roma "not a public holiday" + Ferragosto "Vatican Museums closed Aug 14-15":
  both correct (DeepSeek + Gemini), APPLIED.
- Gemini's "frozen price" flags ("couple hundred euros" fine, "couple of euros" Trevi,
  "~EUR14 Leonardo Express"): ALL HALLUCINATED — grep-confirmed none of those strings exist
  in Batch 16 (zero euro figures). REJECTED (same cross-batch hallucination as Batches 10/14).
- Gemini's pickpocket "alarmism" flag: REJECTED — DeepSeek judged the warnings proportionate;
  it's a single tied-to-the-rush mention, not repetitive. Trimming would weaken useful advice.

## Deferred to end of project (NOT this batch)
- Internal links (one comprehensive pass at the end)
- Affiliate links + disclosure (one pass once programs approved)
  - Note: rome-month-by-month + mistakes-americans-make-in-rome have NO affiliate slots.

## Articles in this batch
1. rome-with-kids-itinerary (rome-in-1-3-days)
2. rainy-day-rome-itinerary (rome-in-1-3-days)
3. rome-month-by-month (when-to-go)
4. rome-in-summer (when-to-go)
5. evening-walk-centro-storico (centro-storico)
6. mistakes-americans-make-in-rome (safety-and-scams)

## Done when
- [ ] 6 heroes picked, verified, uploaded to R2
- [ ] 6 imported as draft
- [ ] Each reviewed against the quality gate
- [ ] Published via admin
