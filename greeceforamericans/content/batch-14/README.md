# batch-14 — greeceforamericans (visas/entry + money + when-to-go) — GATED

Second gate complete. grok: clean. deepseek: 5 findings, audited below.

## Gate audit (Claude reviewed each deepseek finding, did NOT auto-apply)
1. visa article ETIAS fee €7→€20 — **REJECTED**. €7 is web-verified-current (June 2026, official EU). facts.json's €20 was STALE. Kept €7; updated facts.json to €7 with a dated verify-live note instead.
2. entry article "a small fee" → state amount — **ACCEPTED** (using verified €7, not deepseek's €20). Added with caveat.
3. money article ATM advice placement — **DECLINED** (misread). The avoid-Euronet + euros-not-dollars guidance already has two dedicated prominent H2 sections near the top.
4. daily-budget no frozen prices — confirmed clean.
5. best-time-to-visit — confirmed clean.

## ⚠ YMYL — re-verify before publishing
ETIAS (not yet required, ~€7, late 2026) and EES (live since Oct 2025) change. Re-check europa.eu + travel.state.gov right before publish.

## Next
1. Images: 15 per batch-14-images.md (named 01..15), then
   MEDIA_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-14.json  (expect 15/15)
2. node scripts/articles-batch.mjs update <path>/import-batch-14.json   (draft)
3. links -> affiliates -> review -> publish.
