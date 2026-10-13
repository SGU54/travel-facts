# This tree does NOT build the shipped *Rome, Solved.*

Extracted 2026-09-25 from `dossiers-pdf/builds/rome-solved-source.tar.gz`.
It builds and renders cleanly, **but it is a different, earlier manuscript.**

Measured against the shipped `livres/rome-solved.pdf`:

| | shipped | this tree |
|---|---|---|
| pages | 47 | 50 |
| words | 14,878 | 12,903 |
| cover press line | `LA TAVOLA · A DECISION MANUAL` | `ROMEFORAMERICANS.COM · A DECISION MANUAL · FIRST EDITION` |
| prints "the corpus" | 2× | 0× |

**Sentence overlap is zero in both directions** — 0 of 60 sampled shipped
sentences appear here, and 0 of 40 sampled sentences here appear in the shipped
book. Not a trimmed edition: a different text. (A character-bag similarity of
86% is misleading; it ignores word order.)

It is also factually stale. It prints *"ETIAS logged as not yet required, launch
signalled late 2026"* — the window the EU withdrew, and which we corrected across
the fleet in September 2026. Rebuilding from here would put that back in print.

So: **do not render this over the shipped book.** The real source for the 47pp
edition is still missing. What is here is genuinely useful — the fonts, the ten
photographs, and the module layout — if that later source ever has to be
reconstructed.

`render.py` was patched for portability: it indexed `[-1]` into a glob of a Linux
container path and raised IndexError at import on any other machine.
