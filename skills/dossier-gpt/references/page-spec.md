# Page specification

This is the source contract for the paged HTML build. Start with
`assets/print-base.css`, copy its contents into a `<style>` in each template, and
adapt the brand tokens and page size. Inlining CSS avoids local stylesheet fetch
problems in Paged.js. Keep image/font files local and list them in release.json assets.

## Minimal document

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{title}} — {{edition}}</title>
  <style>/* Insert the complete base CSS, then project overrides. */</style>
</head>
<body>
  <header class="cover">
    <p class="kicker">A practical decision manual</p>
    <h1 class="book-title">{{title}}</h1>
    <p>Edition {{edition}} · Checked {{release-date}}</p>
  </header>
  <main>
    <section class="chapter" id="arrival">
      <h1 class="chapter-title">Choose your arrival ticket</h1>
      <p>{{claim:arrival-rule}}</p>
      <p class="source-note"><a href="{{source-url:operator}}">Operator: ticket conditions</a></p>
    </section>
  </main>
</body>
</html>
```

Use actual claim/source IDs from evidence.json. This is structure, not destination content.
A separate sheet template has `<main class="field-sheet">`, its full check date,
the necessary current values, and explicit sources. It uses the same canonical claims.

## Geometry and pagination

Use real `@page` margins and margin boxes. Paint the resulting page/sheet background,
including continuation pages. A full-bleed cover uses a named page with no margin;
its body text still needs a deliberate inset. Never clip essential text to get a fit.

The body is one flow with semantic sections. Start a chapter on a new page only when
it improves reading; do not force every short section onto its own page. Bind headings
to their first lines, keep short verdicts together, and allow long tables to span pages
with repeated headers. A block taller than a page must be redesigned or made splittable.

The CSS starts at 15px body type (11.25pt), 13px table type (9.75pt), and 12px notes
(9pt). The PDF's measured result is authoritative. Scaling a figure scales its labels;
choose the viewBox, final width, label wrapping, and type size together.

## Renderer boundary

The source HTML contains no Paged.js script. `render-guide.mjs` injects the bundled
polyfill, waits for fonts and images, paginates, then prints. It must not shorten,
remove, or rewrite prose to improve page fill. Source and PDF are checked afterwards.

A valid page count does not establish text preservation. Use audit-content for each
document and inspect all final pages. Links, bookmarks, metadata, and source notes are
part of the final artifact; recheck after any postprocessing.

The optional older compositors require their own `section.dec` and `data-ref`
conventions. Those are implementation details of that renderer, not content rules for
all guides. Do not mix two pagination systems or manually pre-split ordinary body pages.
