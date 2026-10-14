# Stage 0 — What a fresh session needs (and fetches itself)

A new session has **no context**, but on this machine it has the repos, the database and
the browser. It asks the user for ONE thing — the project name — and derives the rest.
"Attach the corpus export" and "attach globals.css" are dead text: both are a command away.

## The four inputs

| # | what | where it comes from | who |
|---|---|---|---|
| 1 | **The corpus** | `articles` table of the project's schema: `node scripts/articles-batch.mjs export > corpus.json` in the site repo, or one PostgREST call with `Accept-Profile: <schema>`, `status=eq.published`. Save as `travel-facts/<project>/dossier/corpus.json` | the session |
| 1b | **`globals.css` + `tokens.css`** | `<site>/apps/site/app/` — read from disk | the session |
| 2 | **The project name** — e.g. `romeforamericans` | the user | ★ |
| 3 | **The brand tokens** | `assets/brands/<project>.json` if it exists; else derive from the site's CSS and **confirm with the user** (4 swatches, 3 faces, one rendered page — `references/brand-tokens.md`) | derive: session · approve: ★ |
| 4 | **That project's previous build** | `travel-facts/<project>/dossier/build*/` on disk (the newest by mtime; print which) | the session |

> **A build never transfers between projects.** Rome's build dir resumes Rome and nothing
> else. Lisbon starts from Lisbon's corpus with an empty build dir.

Everything else is derived. **Do not ask the user for facts about the destination.**

## Tooling on THIS machine (replaces the sandbox paths)

- Python 3.13 at `python3`; PIL available; **no ImageMagick**. `pip install -r
  ~/.claude/skills/dossier/scripts/requirements.txt` once (lxml, pypdf).
- Playwright: `barcelonaforamericans/node_modules/playwright` (Node) — `render-paged.py`
  uses the Python Playwright; check `python3 -c "import playwright"` first and say so if
  it is missing. The path `/opt/pw-browsers/chromium_headless_shell-1194/…` from the old
  sandbox does not exist here.
- Scripts: `~/.claude/skills/dossier/scripts/` (NOT `/mnt/skills/user/dossier/`). Run
  them with the build dir as argument; run `audit-release.py` without `python3 -I` (it
  imports its sibling `release_support.py`).
- Shipped PDFs today live in `fleet-growth-review/Book-<Dest>.pdf` and under
  `travel-facts/<project>/` — not in any build dir. See D-6 below.

## The two ways a session starts

**A — new destination:** read state.json → export the corpus → Stage A mine → derive
brand tokens, render the sample, ★ approve → Stage A2 ★ thesis → Stage B.

**B — resuming:** `ls -t travel-facts/<project>/dossier/build*/dossier3.html | head -1`,
`python3 build3.py` must print `pages: N` AND bump `dossier3.html`'s mtime; re-run the
Stage F gates before believing anything the last session said.

## The opening move, in order

```
1. read travel-facts/<project>/state.json            → stage, what's live, what's written
2. export the corpus; run the Stage A counts          → viable? what shape?
   (load article-list.json swamps[] as a HYPOTHESIS; strip span.guide + its sentence
   from every cue tally)
3. brand tokens: read assets/brands/<project>.json, or derive + ★ confirm
4. THEN Stage A properly
```

## What a fresh session must NOT assume

- that the photos in a resumed build are final;
- that the previous session's page count is still true — re-run the gates;
- that the decisions transfer;
- that an external design review has been applied — check the CSS.

## The handover checklist — now a script (D-6)

```
python3 scripts/dossier-pack.py <project>      # proposed; see CHANGES-PROPOSED.md
```
It must: copy the build dir, the rendered PDF(s), `corpus.json`, `evidence.json` and
`release.json` into `travel-facts/<project>/dossier/release-<date>/`; re-run
`audit-release.py` there and print each gate's count; update state.json
(`dossier: {pages, words, pdf, released_at}`); refuse to finish with any gate BLOCKED.
No shipped book is in that state today (2026-10-14: `audit-release.py` on Japan's
`build-v2` → BLOCKED inputs, BLOCKED source-defects, BLOCKED depth; no PDF in the dir).
