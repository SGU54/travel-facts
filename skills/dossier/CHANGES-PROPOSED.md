# dossier skill — proposed changes (whole-file copy supplied only for 0-inputs.md)

The dossier skill is 67 files and mostly sound; the 2026-10-08 merge already fixed its gate
architecture. These are the stale, contradictory or silently-wrong items found on 2026-10-14,
each with the fix. Only `references/0-inputs.md` is rewritten in full (it was entirely about
the old sandbox).

| # | file | problem | fix |
|---|---|---|---|
| 1 | `references/0-inputs.md` | asks the user to attach the corpus export and globals.css; Playwright at `/opt/pw-browsers/…`; uploads in `/mnt/user-data/uploads` | rewritten (see file) — the session exports the corpus and reads the CSS itself |
| 2 | `SKILL.md` l.158–164, `references/e-image.md` §"The sequence" step 4 | "USER hands back the files → dropped in /mnt/user-data/uploads" | the user PICKS (★, from a contact-sheet artifact); the session downloads the picked ids, names them `A07.jpg`, runs `validate-images.py`. Picking is taste; moving files is not. |
| 3 | `SKILL.md` l.69–87 "STAGE G" + `references/g-audit.md` | says `audit-release.py` is the one entry point and fails closed — true — but every shipped book is stored in a state where it is BLOCKED on 3 of 4 families (no `release.json`, no `dossier3.html`+PDF together, no `evidence.json`) | add `scripts/dossier-pack.py` (D-6) and make the handover checklist that script; state the fact in the skill: "none of the seven shipped books can be re-gated as stored" |
| 4 | `references/3b-vein-and-citability.md` (travel-empire) | `python3 /mnt/skills/user/dossier/scripts/audit-synthesis.py` | `python3 ~/.claude/skills/dossier/scripts/audit-synthesis.py` |
| 5 | `SKILL.md` "The name is a deliverable" §3 | "The dossier build does not perform the backfill — the admin does; this build just supplies the string" | the session performs it: `POST /api/guide-name-backfill` dry-run → counts → apply; gate: corpus-check `gloss` becomes exactly 1 string == the name. Also write `name`, `thesis`, hooks into `site.ts` and `site_settings` and run `fleet-gate GUIDE`. |
| 6 | `SKILL.md` l.20–32, `references/a-mine.md` | "Forged on Rome, Solved." — still the reference build; Rome's SITE is now the worst-wired (fonts dropped, 2 swamp tags, 0 body images, 0 FAQ) | one sentence: the BOOK is the reference; the site is not — run `fleet-gate --sites rome` before pointing anyone at it |
| 7 | non-negotiable #3 "The Field Sheet is dated, quarterly, emailed" | nothing emails it; no cron, no template; `common.subscribers` has 19 rows (≈8 real) and `guide_entitlements` the test buyers only | either build the quarterly send (Resend is configured on all 7 sites; `/api/guide-sheet` exists) or stop promising it on the sales page (M3 §6). ★ decision 5 in DESIGN-DECISIONS |
| 8 | gates generally | `audit-furniture` prints "50 pages, every sheet checked" ✓; `audit-page-shape` prints per-page % ✓; `audit-marks` prints counts ✓; `audit-release` prints families with no counts | add `checked N pages / N claims / N bindings` per family — the 0-gates.md contract |
| 9 | `references/f-render.md` | `render-paged.py` + Python Playwright; `SKILL.md` says Node Playwright "is not installed on this machine" | it is (barcelonaforamericans/node_modules). Keep the Python renderer as default, but the sentence is false and `audit-content.py` (which wants Node Playwright) can now run — un-BLOCK it by pointing it at that node_modules |
| 10 | `assets/brands/` | has japan, rome, thailand only; greece/barcelona/morocco/turkey shipped books without a brand file | derive and write the four missing files from their `tokens.css` (mechanical; the ★ is approval) |
