# This IS Rome's real source — but one revision behind the shipped book

Extracted 2026-09-25 from `dossiers-pdf/builds/rome-solved-source (1).tar.gz`
(internal timestamps 19 July 2026, 02:53–04:52 UTC).

Unlike `../build/`, this is the genuine lineage. Verified:

- its own `dossier.pdf` and `audits/` say 44pp, CLEAN
- rebuilding here reproduces that exactly — **60/60** sampled sentences
- against the shipped 47pp book, with running heads stripped and drop caps
  rejoined, prose overlap is **96% / 92%** both ways
- same cover press line (`LA TAVOLA`), same two printed uses of "the corpus"

## Why it is still not what ships

The shipped `rome-solved.pdf` was rendered 19 July at 07:52 CEST — about an hour
after this archive's last file. That final revision did three things this tree
cannot reproduce:

1. **Moved the running head into the HTML so it varies per chapter.** Here it is a
   static Chromium header template reading `Rome, Solved. | La Tavola · A Decision
   Manual` on every page; the shipped book reads `◆ Rome for Americans ◆ <page>
   CHAPTER <chapter title>`. Rebuilding from here puts a fixed press line on all
   44 pages.
2. Trimmed roughly 500 words.
3. Re-laid the book from 44pp to 47pp.

So a rebuild here would fix Rome's two "corpus" mentions at the price of a
visible furniture regression on every page. Rome has the mildest corpus problem
in the fleet, so that trade is not worth taking — **leave the shipped 47pp book
alone** unless the 19 July 07:52 source turns up.

## Local changes

`render3.js` had `/home/claude/build/rome-solved` and a pinned
`/opt/pw-browsers/chromium-1194/...` hardcoded; both replaced with `__dirname`
and playwright's own browser resolution. `node_modules` is a symlink to
barcelonaforamericans' so `require('playwright')` resolves.
