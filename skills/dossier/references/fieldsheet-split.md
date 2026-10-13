# The two documents — splitting the Field Sheet out of the Book

Every book says it in its own "how to read this": **the Book holds what lasts, the Field
Sheet holds what moves.** Binding them together contradicts that on the first page — a
reader who wants the current figures has to carry the whole book, and reissuing a sheet
means reissuing the book.

So every project ships **two PDFs**:

```
<Name>.pdf              the Book        stable, ~2 years
<Name>-FieldSheet.pdf   the Field Sheet dated, reissued quarterly
<Name>-phone.pdf        the Book, set for a phone
```

---

## The split happens at RENDER time, never in the source

```
python3 render-both.py <build-dir>
  → _book.html   the book with the sheet lifted out
  → _sheet.html  the sheet as a standalone document
  → dossier.pdf + fieldsheet.pdf
```

`fssplit.py` does the surgery; `render-both.py` calls the book's own renderer twice.

**Why not edit the source?** Because some projects generate `dossier3.html` from a
Python builder, and editing the generated file there is reverted by the next build —
silently, with no trace of why the sheet came back. Reading the source and writing two
temporary documents costs nothing and leaves every tree untouched. One mechanism,
whatever the project's build style.

**Rome's renderer takes env vars** instead of a `render()` call, because `render4.py` is
a script, not a module: `RENDER_SRC=_book.html RENDER_OUT=dossier4.pdf python3 render4.py`.
With neither set it behaves exactly as before.

---

## Finding the section

Field-sheet ids are not consistent across projects: `fs`, `fsheet`, `field-sheet`,
`fieldsheet`. Match on the id first and the class only as a fallback — one project
classes several sections `fs` for the annex page size and only one of them is the sheet.

**A `front` class is a LAYOUT class, not a position.** One project's sheet carries
`class="front fieldsheet"` and is back matter like every other.

---

## The sheet inherits the book's head AND its wrapper chain

The standalone document is the book's own `<head>` (fonts, palette, `@page` furniture)
plus the one section, wrapped in **whatever ancestors the book's CSS keys off** —
`.flow` sets the column measure, `.page` the sheet. Rebuild the sheet without them and
it silently renders at a different measure from the book it belongs to.

---

## The contents row stays — but loses its anchor AND its folio

A book that stops naming its own companion is worse than one whose folio is wrong. So
the row keeps its title and prints **"separate sheet"** where the page number was.

**It must lose the anchor**, because `target-counter` resolves to nothing once the target
leaves the document and prints **0** — and the claims gate fails a book whose contents
prints 0.

**It must lose the folio TEXT too, explicitly.** Rome has no `target-counter`;
`render4.py` writes folios back by measurement and *skips any row whose target it cannot
resolve* — so the row kept its original static number and the contents pointed at page
38, which is now another chapter. **A wrong number is worse than none.**

**Order matters inside the row:** replace the folio cell FIRST, while it still holds its
own `<a>…</a>`. Unlink the anchors first and the cell becomes a nested `<span>`; the
non-greedy match then stops at the inner close and leaves an orphan `</span>`.

Four row idioms exist in the fleet and all four need handling: `<tr>`, `<li>`,
`<div class="row">`, and a `<nav>` of bare `<a>`.

---

## THE CLASS OF BUG THIS EXPOSED: tools reading the source, not the print

Three separate tools in the chain read `dossier3.html` while operating on the **split**
PDF. Each failed silently:

- **`add-nav.py`** built the outline from the unsplit source, looked for a chapter the
  printed file no longer has, and reported "19/20 resolved" with a dangling entry.
- **`render-phone.py`** set the phone edition from the unsplit source, so the phone book
  silently kept a chapter the print book had lost.
- the splitter's own dry-run, if pointed at the wrong file.

All now prefer `_book.html` when it exists, falling back to `dossier3.html` for a project
that was never split. `add-nav.py` also takes `--html <file>`.

> **The rule:** any tool that describes, navigates or re-sets a PDF must read **the
> document that was actually paginated**, not the source it came from.

---

## Prose that places the sheet "at the back"

Grep for it before you ship — `at the back`, `back of the book`, `final page`,
`overleaf`. The sheet is no longer in there.

**Check what the phrase refers to.** One project's "at the back" is its *sources ledger*,
which stays in the book. Do not touch it.

**Keep the replacement no longer than the original.** A fix 20 characters longer pushed
a reading key off page 2 onto a sheet of its own and the `book` gate caught it
(consistency 28–92 %, a near-empty tail). Reworded shorter, the book lost the page it
should have lost and nothing else moved.

---

## Order of operations for a project

```
1  render-both.py <build-dir>          book + sheet
2  add-nav.py <build-dir>              outline + links  (reads _book.html)
3  render-phone.py <build-dir>         phone edition    (reads _book.html)
4  add-nav.py <build-dir> --pdf dossier-phone.pdf --html _book.html
5  emit-manuscript.py <build-dir>
6  audit-release.py <build-dir>        all six gates
```

The sheet itself is not gated — it is one to three pages of dated tables with no
chapters, no contents and no outline, and every gate assumes a book.
