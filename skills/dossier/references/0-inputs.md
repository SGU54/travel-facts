# Stage 0 — What a fresh chat needs

A new session has **no context**. Ask for these four things up front; don't start without 1 and 2.

## The four inputs

| # | what | where it comes from | required? |
|---|---|---|---|
| 1 | **The corpus export** — `export-articles-YYYY-MM-DD.json` | the site's admin → export | **yes** — it's the only content source |
| 1b | **`globals.css`** — the file itself, not the repo | `apps/site/app/globals.css` | **yes for a new project** — the only source of the brand's hue family + intent |
| 2 | **The project name** — e.g. `romeforamericans` | the user | **yes** |
| 3 | **The brand tokens** | `assets/brands/<project>.json` if it exists; else derive from the site's `globals.css` and **confirm with the user** — see `references/brand-tokens.md` | **yes** |
| 4 | **That project's previous build** — `<project>-dossier-build.tar.gz` | a prior session **of the same project** | only when resuming |

> **A build never transfers between projects.** Rome's tarball resumes Rome and nothing else —
> its decisions, coordinates, palette and prose are Rome's. Lisbon starts from Lisbon's corpus
> with an empty build dir. **The skill is what transfers; the build is one project's output.**
> Copying Rome's `content.py` to seed Lisbon produces a Rome book with the nouns swapped,
> which is the exact failure this whole product exists to avoid.

Everything else is derived. **Do not ask the user for facts about the destination** — that's
what the corpus is for, and inventing them breaks non-negotiable #1.

## The two ways a session starts

**A — new destination** (the common case):
```
user: "build the dossier for greeceforamericans"  + attaches export-articles-*.json
                                                  + attaches globals.css
you:  1. Stage A — mine the corpus, is it viable, what shape?
      2. Stage 0b — DERIVE the brand tokens from the site's globals.css,
         show the user 4 swatches + 3 faces + one sample page, get approval,
         write assets/brands/greeceforamericans.json      ← see references/brand-tokens.md
      3. THEN Stage B
```
There is no registry of brand tokens — not in `common.sites`, not in a state.json. A project
that has never shipped a dossier **has no tokens until this session makes them**. Nothing from
any other project is reused: empty build dir, own corpus, own decisions, own palette.

**B — resuming one project**:
```
user: "resume the Rome dossier"  + attaches rome-dossier-build.tar.gz
you:  untar → build → check dossier3.html's mtime → re-run the Stage F gates → continue
```
Never assume the last session's page count, photos, or "final" status still hold.

## The opening move, in order

```
1. read state.json for the project           → stage, what's live, what's written
2. load the corpus, run the Stage A counts   → is this viable, and what shape?
   (if the project's article-list.json has a `swamps` array, load it too — it is the
   site's HYPOTHESIS of the terrain, to reconcile against the mine, never to obey;
   exclude guide-span glosses from every cue tally — see SKILL.md "The name is a
   deliverable")
3. brand tokens: read assets/brands/<project>.json, or derive + CONFIRM
4. THEN start Stage A properly
```

## If resuming from a tarball

```bash
tar xzf <project>-dossier-build.tar.gz && cd <project>-build
python3 build3.py            # must print "pages: N" AND update dossier3.html's mtime
ls -la dossier3.html         # ← check the mtime. See bug #2.
```

The build is **portable**: `BUILD = os.path.dirname(os.path.abspath(__file__))`. It runs from
wherever it's unpacked. If a fresh session hardcodes absolute paths back in, that's a
regression.

To render you also need Playwright's chromium at
`/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell` — check it exists
before promising a PDF.

## What a fresh chat must NOT assume

- **That the photos in a resumed build are final.** They're usually test images. Confirm
  before shipping; re-emit the brief (Stage E) if the user wants real ones.
- **That the previous session's page count is still true.** Re-run the gates (Stage F).
- **That the decisions transfer.** "Roma Pass or not" has no Lisbon analogue. Every project
  mines its own from its own corpus.
- **That an external design review has been applied.** Check the CSS, not the conversation.

## The handover checklist (end of any session)

```
□ tarball the build dir (source only — no .bak, no dead build.py/build2.py)
□ the PDF, re-gated
□ state.json updated with: stage, page count, word count, what's pending
□ any un-filled image slots named explicitly
```
