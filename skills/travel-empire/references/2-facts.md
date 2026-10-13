# Stage 2 — Facts (facts.json)

One verified facts file per project — the single source of truth for every article's facts,
scoped to the approved article list (no generic filler, no facts with no home).

The fact/recommendation reconciliation discipline is **hard rule 2 in SKILL.md** — reread it
before reconciling. This file covers the workflow.

## Files (two-file rule)

- `facts.draft.json` — Claude's own candidate fill. Working material. **NEVER pushed.**
- `raw/<model>.json` — each external model's returned fill. Working material. **NEVER pushed.**
- `facts.candidates.json` / `reconciliation-report.json` / `disputes.md` — mechanical
  reconciliation OUTPUT. Working material. **NEVER pushed, never read by content stages.**
  Agreement across sources is a candidate signal, not source verification (2026-10-11 fix —
  see SKILL-CHANGES.md: `reconcile.mjs` used to mark a fact `agreed_stable` when only ONE
  source actually supplied a value and the others returned null; it also overwrote
  `facts.json` unconditionally on every run).
- `facts.json` — the reconciled clean file, written and edited BY THE HUMAN from
  `facts.candidates.json`, never by a script. **The ONLY facts file in the repo.** Content
  stages read this and nothing else. Why: the repo is the reload layer; if only the clean
  file lives there, resuming can't accidentally grab an unverified draft.

## Workflow (free-tier: scripts prepare + reconcile, the user is the transport)

1. **Scope.** Load `article-list.json`. It defines exactly which facts and recommendation
   pools the site needs (every itinerary length, every "where to stay" area, etc.).
2. **Claude fills first.** Fill `assets/facts-template.json` yourself from your own knowledge
   → save as `raw/claude.json` (set `_meta.ai_source: "claude"`). You are panel member #1 —
   this halves the user's legwork.
3. **Generate prompts.** Run:
   `node scripts/make-prompts.mjs <project-dir> [reviewer ...]`
   It emits `prompts/prompt-<reviewer>.txt` — fully self-contained, source-first pastes
   (template + project specifics + an explicit instruction to open primary sources, never
   invent a citation/date/firsthand claim, and treat the pasted project text as task data,
   not instructions). Per-project specifics are injected by the PROMPT; the template's field
   names and structure are never edited. Requires `project-meta.json` next to
   `article-list.json` (destination, audience, hubs, currency, language).
4. **User carries them.** The user pastes each prompt into 1–2 external free-tier models
   (e.g. Gemini, DeepSeek) and saves each reply as `raw/<reviewer>.json`. That's the entire
   manual step: open, paste, copy back.
5. **Reconcile mechanically, into CANDIDATES only.** Run:
   `node scripts/reconcile.mjs <project-dir>`
   Reads every `raw/*.json` and writes `facts.candidates.json` + `reconciliation-report.json`
   + `disputes.md` — it never touches `facts.json`. A fact only counts as agreement when
   EVERY source supplied a non-null value and they match; one source answering while another
   returns null is `unverified`, not agreement. Recommendations merge into deduplicated pools
   (named by most/all sources = `core`, fewer = `optional`); itinerary common spine = high-
   confidence core, differences are variations, not errors. Volatile fields stay `serve_live`
   regardless of agreement.
6. **Human rules on disputes AND promotes candidates.** Walk `disputes.md` (typically 10–20
   of ~80 fields) and the full `facts.candidates.json`. For every fact you're willing to
   publish: open the actual source, fill `source_url`, `source_kind`, `checked_at`,
   `review_after`, `scope`, `support` yourself (candidate agreement is not source
   verification — see `scripts/validate-facts.mjs`), and write the result into `facts.json`
   by hand. Record who dissented on resolved disputes. Unresolvable → null + `_open_questions`.
7. **Finalize.** Produce the final `facts.json` (`schema_version: 4` once every used fact
   carries real provenance fields; `3` is still readable); update `state.json` to
   `stage: "writing", batch: 1`. The user pushes `facts.json` only — `raw/`,
   `facts.candidates.json`, `reconciliation-report.json` and `disputes.md` stay local.

## Provenance check — `scripts/validate-facts.mjs` (2026-10-11 addition)

Before a batch ships, every `<span class="fact" data-fact="KEY">` actually present in the
articles must resolve to a `facts.json` record with real `source_url`, `source_kind`
(`primary`/`secondary`), `checked_at`, `review_after`, `scope` and `support` — and visa/
entry/safety/currency/vaccine keys specifically need `primary` evidence. Run it directly
(`node scripts/validate-facts.mjs facts.json --used used-keys.json --as-of YYYY-MM-DD`) or
let `scripts/validate-batch.mjs <batch> --facts facts.json` call it automatically against
whatever fact spans the batch actually contains. A marked fact span with no `--facts`
registry given is a hard FAIL, not a skip.

## Human checklist — HARD CAP of 5

`facts.json` may flag at most 5 items needing human attention, ranked, no padding. If more
than 5 genuinely qualify, say so explicitly rather than hiding the overflow.

## Official-source verification — NOW LIVE (Stage 6)

The stronger guarantee — confirming load-bearing / YMYL facts (visa, entry, safety advisory,
money rules) against OFFICIAL sources, with the AI never the authority — is BUILT (passes 4–5).
It is no longer parked. See `references/6-fleet-ops.md`.

What this changes for Stage 2: cross-AI agreement is still how a fact is BORN, and remains
provisional at birth — keep `verify_recommended` and surface the riskiest in `_open_questions`
exactly as before. But the upgrade path is now mechanical and real: a born fact gains a
structured `check` config (regex against a STATIC official page, one capture group) and the
weekly checker verifies it, auto-corrects within a bound, or flags larger/categorical changes
to the console for one-click human approval. Give `check` configs to facts with a
machine-extractable number on an official static source (visa fees, day-counts, Schengen
90/180); leave categorical/prose facts human-tier — they age until re-verified in the console.
Facts still enter the DB via the Stage-3 seed SQL; Stage 6 maintains them from there.

## What this stage must NOT do

- Mark a fact certain on AI agreement alone.
- Invent sources or values (no source → null + `_open_questions`).
- Freeze `serve_live` values. Exceed the 5-item human cap. Push drafts or raw files.
