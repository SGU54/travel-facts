# batch-16 — greeceforamericans (FINAL BATCH) 🏁

5 articles: flights-from-us-to-greece, arriving-in-athens-guide, greece-shoulder-season, best-greek-islands-for-first-timers, best-beaches-in-greece.
Status: WRITTEN. cloud=dsrkwieur, 15 images. flights uses skyscanner affiliate.

**This completes all 80 articles across 16 batches.** Content generation is done.

## Scope note (the 2 ranking articles)
best-greek-islands-for-first-timers + best-beaches-in-greece are constrained STRICTLY to the in-scope 6 (Athens + Santorini/Mykonos/Crete/Naxos/Paros). Verified 0 out-of-scope islands. Beaches article sets the Santorini=volcanic-not-sandy expectation and frames itself as "islands first-timers visit." The second gate re-checks scope.

## Next
1. SECOND GATE: paste second-gate-prompt.txt into 1-2 models (scope + correction#1 + flight/arrival facts); send findings.
2. Images: 15 per batch-16-images.md (named 01..15), then
   CLOUDINARY_FOLDER=greeceforamericans node scripts/upload-batch.mjs <folder> <path>/import-batch-16.json  (expect 15/15)
3. node scripts/articles-batch.mjs update <path>/import-batch-16.json   (draft)
4. links -> affiliates -> review -> publish.

## ⚠ Project-level follow-ups (now that writing is done)
- PUBLISH RECONCILIATION: confirm batches 2-16 are actually imported+published before the internal-link pass (inject-links needs LIVE target slugs or it 404s/skips). My import tracking only ever confirmed 1,8,9; you've reported higher live counts — worth a definitive check now.
- SITE-WIDE INTERNAL LINK PASS: best run once most/all 80 are live, so links resolve to real pages. links-map.json now has many more valid targets.
- SKILL PATCH backlog logged in state.json (scope-constraint on ranking articles; word-bounded OOS checks; keep facts.json YMYL fields fresh; second-gate findings need auditing not auto-apply; etc.)
- YMYL re-verify (batch 14 ETIAS/EES) right before publishing if time has passed.
