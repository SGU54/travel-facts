# references/build-traps.md — the render traps, already paid for

**Read at Stage F, before you debug anything.** Every entry below cost real time on a
build. None of them is caught by a gate. Check this list first when a render misbehaves.

## 1. The paginator dies with `[object ProgressEvent]`

**Cause:** Paged.js re-fetches the stylesheet over XHR to parse the `@page` rules.
Under `file://` that request is blocked by CORS, so the paginator never initialises.

**Fix: inline the CSS into the HTML.** Never `<link rel="stylesheet">` in a build you
render locally.

```python
html = html.replace('__CSSINLINE__', open('dossier.css').read())
```

Make the generator do it, not a post-step — a post-step silently stops running the day
someone regenerates the HTML.

## 2. The render hangs with no output and no error

**Cause:** `paged.polyfill.js` is missing from the **root** of the build directory (the
driver injects it with a relative `src`), or the file you downloaded is not the
polyfill at all.

**Check the size first.** A 96-byte `paged.polyfill.js` is an error page, not a
library. Fetch it from the npm registry, which is reachable:

```
curl -sL https://registry.npmjs.org/pagedjs/-/pagedjs-0.4.3.tgz -o pagedjs.tgz
tar xzf pagedjs.tgz && find package -name paged.polyfill.js -exec cp {} . \;
```

When a render hangs, verify the polyfill loads **before** optimising images or CSS.
A missing build dependency produces symptoms identical to a performance problem.

## 3. A rule appears at the top of pages that open no chapter

**Cause:** a `border-top` on an element split across pages is **redrawn on every
fragment**. The chapter separator reappears at the head of each continuation page,
with body text pressed against it. Readers describe it as *"suffocating, like there's
no space"* — and they are right, because that bar should not be there at all.

**Fix: make the separator a pseudo-element.** Pseudo-elements cannot be cloned onto
fragments.

```css
.chap{ border-top:none; box-decoration-break:slice; -webkit-box-decoration-break:slice; }
.chap::before{ content:""; display:block; height:1px; background:var(--line); margin:0 0 20px; }
```

The same applies to padding, background and box-shadow on any splittable block.

## 4. A chapter opener strands at the foot of a page

**Cause:** `break-after:avoid` is not honoured reliably. The opener gets placed, the
next block does not fit, and the title sits alone above 60% white space.

**Fix: an opener pack** — bind the opener to its body in one unbreakable block, and
**accumulate blocks until the pack carries real body**, not merely the first one:

```python
acc, end = 0, None
for j in range(open_index + 1, len(blocks)):
    if blocks[j].startswith(('<p', '<div class="ledger"', '<h2')):
        acc += words(blocks[j]); end = j
        if acc >= 55: break        # 55 words — one short lead does NOT satisfy it
```

Without the word floor, a one-sentence lead satisfies the pack and the opener strands
anyway. That regression shipped once; the floor is why it cannot again.

## 5. The feathering silently does nothing

**Cause:** `render-paged.py` skips any section without an `id`
(`if not s["id"]: continue`). A generator that emits `<section class="decision">` gets
no feathering at all, and every tail stays ragged.

**Fix: honour the contract.** Sections must be `<section class="dec chap" id="…"
data-ref="…">`, and feedable plates must be `<figure class="photo">` with an inline
height.

## 6. Chapters that each open a page leave the book half empty

**Cause:** one `break-before:page` per chapter. With 8 decisions and 6 essays that is
14 forced breaks, and every short chapter leaves a tail.

**Fix: let chapters FLOW.** Separate them with a rule and generous margin, not a page
break. This was the single largest density gain on this build: 20 pages at 56% median
fill became 16 at 89%, and the same content later carried 37 pages without padding.

## 7. Small things that look like bugs to a reader

- `str.title()` breaks apostrophes: `WON'T` → `Won'T`. Write a title-caser that
  handles apostrophes and leaves function words lowercase.
- A map figure with no height cap can push a whole page of white space. Cap it:
  `max-height:3.5in; object-fit:contain`.
- `audit-furniture` needs `--paper <hex>` for any palette that is not Rome's, or every
  page reads as "unpainted".
- Figure captions **must** be numbered `FIG. N · …`. The rhythm check looks for that
  literal string; without it a well-illustrated book counts as a text-only desert.

## 8. The method rule

A patch whose target text does not match **fails silently**. On this build a fix was
announced that had never been applied, and the defect survived another round.

**Verify the code changed before you claim the fix.** And then **rasterise the page and
look at it** — fragmentation artifacts (trap 3), stranded openers (trap 4) and
mis-keyed figures are all invisible to every gate in this skill.
