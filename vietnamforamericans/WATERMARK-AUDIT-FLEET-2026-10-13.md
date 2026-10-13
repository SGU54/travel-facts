# Unsplash+ watermark audit — Vietnam, Japan, Thailand

**Date:** 2026-10-13
**Checked:** 663 distinct images (every published article hero + every distinct
in-body image on three sites).

| Site | Images | Watermarked | Status |
|---|---:|---:|---|
| vietnamforamericans | 196 | **11** | all 11 replaced — see WATERMARK-AUDIT-2026-10-13.md |
| japanforamericans | 192 | 0 | clean |
| thailandforamericans | 275 | 0 | clean |

Vietnam is the only site affected. The images were sourced by hand on
unsplash.com, so it is a per-session slip rather than a systematic fault —
which matches the result: one site caught it, two did not.

---

## The method, and the two ways it was wrong first

**Four automated detectors were written and all four failed.** Three looked for
periodicity (the watermark is a repeating grid) — but photographs repeat harder
than the watermark does, so they ranked carriage windows, railings and roof
tiles above real positives; the best scored a known-watermarked image at 97
against a clean train photo at 854. The fourth built a template by averaging the
high-pass of seven known positives, on the theory that the photographs would
cancel and the watermark reinforce; it failed because the grid sits at a
different phase in every image, so the average smears. Three of seven positives
scored below the worst negative. **Do not rebuild one of these.**

**What works is looking, at 1:1 — but the crop has to be a FRACTION of the
width, not a fixed number of pixels.** Two measured facts drive that:

1. An Unsplash+ preview is **not size-capped** — a sample was served at the full
   4000×2250. Large dimensions do not mean a file is safe.
2. The watermark's **tile pitch scales with the image**, at roughly 10% of its
   width.

So a fixed 330px crop samples three tiles on an 1800px file and *less than one*
on a 5500px file. The first pass over Japan used fixed crops and therefore
under-sampled its 146 large files; they were re-checked with a 22%-of-width crop
rendered at 460px, where the glyphs are plainly legible. Validated against a
known Unsplash+ file at 4000px before use.

Also: re-cut near-white frames from their darkest mid-tone window. Light grey on
a blown sky is invisible.

## Sourcing: the guard that removes the judgement call

Unsplash's search API marks every paid preview with `plus: true` /
`premium: true` and serves it from `plus.unsplash.com` rather than
`images.unsplash.com`. Filtering on those three signals at search time rejected
40 results across Vietnam's 11 replacement searches — about a quarter of
everything returned. Picking by hand in the browser has no such guard, which is
how these got in: the badge is easy to miss and the thumbnail looks clean.

Script: `source-clean-unsplash.py` (next to this file).

## The fifth detector also failed — but it found the gap the audit had

The idea: an Unsplash+ preview might carry a file-level signature, so 2,300
unchecked files could be scanned instead of eyeballed. The 11 Vietnam positives
turned out to share a width (1800px) and a JPEG quantization table
(md5 `d14d0ba2…`) that the first few clean files did not.

**It is not a watermark detector.** Scanned across all of Vietnam's 208 local
files, that signature matches **98** of them — the 11 positives and 87 clean
ones. It identifies a *sourcing route*, not a paid preview: files downloaded by
hand from an unsplash.com photo page at the 1800px option, which is how batches
11–20 were sourced. Treating it as a detector would have been a 9:1 false
positive rate dressed up as a scan.

What it is genuinely good for is finding **which files came through the hand
route** — the only route that has ever produced a watermark here, because it is
the one with no `plus:` flag to filter on.

### What that surfaced: the paid books were never audited

Every audit so far covered *site article* images. The dossier plates — the
photographs inside the books people pay for — were not in scope. The route
fingerprint shows the hand route was used for some of them:

| Book | Plates with the hand-route fingerprint | Result |
|---|---:|---|
| japanforamericans | 8 (`A01`–`A08`) | **clean** |
| moroccoforamericans | 7 (cover, closing, desert, eating, fez-medersa, ground, medina) | **clean** |

All 15 cut at native resolution into 560×360 windows chosen for flatness and
mid-tone luminance — a plain wall, open water, a concrete platform, a bare
ochre façade, which are the surfaces where the grid is most obvious. Morocco's
`closing.jpg` is a night market with no mid-tone window at all; it was re-cut
from its brightest region and contrast-boosted ×3.2. Nothing on any of them.

## The remaining five sites — AUDITED 2026-10-13 (later)

barcelona, greece, morocco, rome, turkey. **No watermark found.**

**Scope was smaller than feared.** The "~2,300 images" estimate counted local
files, including duplicates and frames never used. The real figure is the
images the published articles actually reference: **1,151 distinct live
images** (276 / 238 / 265 / 96 / 276).

**Method — provenance first, then eyes.** Every watermark this fleet has ever
had came from ONE route: a file downloaded by hand from an unsplash.com photo
page. That route leaves a JPEG quantization-table fingerprint
(md5 `d14d0ba2…`). It is NOT a watermark detector — on Vietnam it matched 98
files of which 11 were watermarked — but it reliably answers *"did this file
come through the hand route at all?"*

Each live ORIGINAL (no `/cdn-cgi/image/` transform — a transform re-encodes and
destroys the table) was range-fetched for its header only, 16KB each, and its
DQT parsed:

| | count | result |
|---|---:|---|
| JPEG, table read | 906 | **0 hand-route** |
| PNG | 232 | Unsplash serves JPEG — these are the AI-generated fallback pipeline, not downloads |
| JPEG, table past 16KB | 13 | fingerprint inconclusive → **all 13 visually audited** |

**Then 53 images were cut at NATIVE resolution and read** — every one of the 13
inconclusive files, plus a stratified sample across all five sites, with the
crop window chosen for flatness and mid-tone luminance. That put the best
possible detection surfaces under the eye: flat skies at 5184px and 6240px, a
Sahara dune at 4496px, plain walls, open water, wet cobbles, tarmac. A grid of
faint grey text could not have hidden on any of them. Nothing.

**What this does and does not establish.** The provenance scan is COMPLETE —
all 1,151. The visual audit is a SAMPLE and cannot prove absence by itself.
The conclusion is strong because the two agree: zero files from the only route
that has ever produced a watermark here, and nothing visible in a sample
weighted toward the unknowns.

**One trap worth recording.** The first pass reported "0 hand-route hits across
1,151" and was meaningless: Python's urllib had no CA bundle, so every one of
the 1,151 fetches had failed with an SSL error and the script counted zero hits
among zero successes. It was caught only because the script also printed the
error count. **A scan that reports zero must also report how many it actually
read.**

---

## Not yet checked

(Article images on all 8 sites are now audited.)

- **199 other dossier plates** across the seven books. They do not carry the
  hand-route fingerprint, but that only means they were not downloaded that way
  *or* were re-encoded by the build pipeline, which destroys the table. The
  fingerprint can confirm the route, never rule it out.
