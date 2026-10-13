# -*- coding: utf-8 -*-
"""split-fieldsheet.py — lift the Field Sheet out of a book into its own document.

The Book holds what lasts; the Field Sheet holds what moves. Every book in the
fleet says so in its own "how to read this" — and then bound the two together,
so a reader who wants the current figures has to carry the whole book, and a
reissued sheet means reissuing the book. Japan already ships them apart
(`fieldsheet.html` -> `fieldsheet.pdf`); this does the same for the rest, from
the book's own markup so the sheet inherits its fonts, palette and furniture.

What it does, per build directory:

  · finds the field-sheet <section> by id (fs / fsheet / field-sheet) or class
  · writes `fieldsheet.html` — the book's own <head> plus that one section,
    wrapped in whatever ancestors the book's CSS keys off (.flow, .page …)
  · removes the section from `dossier3.html`
  · rewrites the contents ROW for it: the anchor becomes plain text and the
    folio cell says the sheet travels separately. Leaving the row linked would
    print a 0 — `target-counter` resolves to nothing once the target is gone,
    and the claims gate fails a book whose contents prints 0. Leaving the row
    out entirely would be worse: the book would stop telling you the sheet
    exists at all.

Usage:  python3 split-fieldsheet.py <build-dir> [--apply]
Without --apply it reports what it would do and writes nothing.
"""
import os, re, sys

FS_IDS = ('fs', 'fsheet', 'field-sheet', 'fieldsheet')


def find_section(doc):
    """(start, end, id) of the field-sheet section, or None.

    Matched on the id first and the class only as a fallback: one book classes
    several sections `fs` for the annex page-size and only one of them is the
    sheet.
    """
    for m in re.finditer(r'<section\b[^>]*>', doc):
        tag = m.group(0)
        sid = re.search(r'\bid="([^"]+)"', tag)
        cls = re.search(r'\bclass="([^"]*)"', tag)
        name = sid.group(1).lower() if sid else ''
        klass = (cls.group(1).lower().split() if cls else [])
        if name in FS_IDS or (not sid and any(k in FS_IDS for k in klass)):
            # the matching close, allowing nested sections
            depth, i = 0, m.end()
            while True:
                o = doc.find('<section', i)
                c = doc.find('</section>', i)
                if c < 0:
                    return None
                if 0 <= o < c:
                    depth += 1; i = o + 8
                elif depth:
                    depth -= 1; i = c + 10
                else:
                    return m.start(), c + 10, name or klass[0]
    return None


def wrappers(doc, pos):
    """The open tags of every element still unclosed at `pos`, in order.

    The sheet has to sit inside the same chain the book's CSS keys off — `.flow`
    sets the column width, `.page` the sheet. Rebuilding the sheet without them
    silently gives it a different measure from the book it belongs to.
    """
    open_tags = []
    for m in re.finditer(r'<(/?)(div|main|article|body)\b([^>]*)>', doc[:pos]):
        if m.group(1):
            if open_tags:
                open_tags.pop()
        elif not m.group(0).rstrip().endswith('/>'):
            open_tags.append(m.group(0))
    return [t for t in open_tags if not t.startswith('<body')]


def strip_contents_row(doc, fsid):
    """Unlink the contents row for the sheet and say where the sheet went.

    The row stays — a book that stops naming its own companion is worse than one
    whose folio is wrong — but the ANCHOR goes, because `target-counter` resolves
    to nothing once the target leaves the document and prints a 0, which the
    claims gate fails a book for.

    The FOLIO CELL has to be emptied explicitly, not just unlinked. Rome does not
    use target-counter at all (Chromium has none); render4.py writes the folios
    back by measurement and skips any row whose target it cannot resolve — so the
    row kept its original static number and the contents pointed at page 38,
    which is now somebody else's chapter. A wrong number is worse than none.
    """
    href = f'href="#{fsid}"'
    k = doc.find(href)
    if k < 0:
        return doc, 'no contents row found'

    # the enclosing row: a table row, a list item, a div.row, else the anchor
    row_start = row_end = kind = None
    for tag in ('tr', 'li'):
        o = doc.rfind(f'<{tag}', 0, k)
        c = doc.find(f'</{tag}>', k)
        if o >= 0 and c >= 0 and doc.find(f'</{tag}>', o, k) < 0:
            row_start, row_end, kind = o, c + len(tag) + 3, tag
            break
    if row_start is None:
        o = doc.rfind('<div class="row"', 0, k)
        if o >= 0 and doc.find('</div>', o, k) < 0:
            # walk to this div's own close, past the spans inside it
            depth, i2 = 0, o + 4
            while True:
                no = doc.find('<div', i2); nc = doc.find('</div>', i2)
                if nc < 0:
                    break
                if 0 <= no < nc:
                    depth += 1; i2 = no + 4
                elif depth:
                    depth -= 1; i2 = nc + 6
                else:
                    row_start, row_end, kind = o, nc + 6, 'div.row'
                    break
    if row_start is None:
        row_start = doc.rfind('<a ', 0, k)
        row_end = doc.find('</a>', k) + 4
        kind = 'a'
    row = doc[row_start:row_end]

    NOTE = '<span class="fsnote">separate sheet</span>'

    # THE FOLIO CELL FIRST, while it still holds its own <a>…</a>. Unlinking the
    # anchors beforehand turns that into a nested <span>, and the non-greedy
    # match then stops at the inner close and leaves an orphan </span> behind.
    row, n = re.subn(r'(<(?:td|span)[^>]*\bpg\b[^>]*>).*?(</(?:td|span)>)',
                     lambda m: m.group(1) + NOTE + m.group(2), row, count=1, flags=re.S)

    row = re.sub(r'<a\b[^>]*href="#%s"[^>]*>' % re.escape(fsid),
                 '<span class="fsrow">', row)
    row = row.replace('</a>', '</span>')
    if not n:
        close = row.rfind('</')
        row = row[:close] + NOTE + row[close:]
    return doc[:row_start] + row + doc[row_end:], f'{kind} row unlinked'


FSNOTE_CSS = """
/* The contents still names the Field Sheet; it just no longer points at a page
   inside this book, because the sheet is now its own document. */
.fsnote{ font-family:var(--mono,monospace); font-size:8.5px; letter-spacing:.06em;
  text-transform:uppercase; opacity:.62; white-space:nowrap; margin-left:.5em; }
.fsrow{ display:flex; align-items:baseline; width:100%; }
"""


def split(doc):
    """(book_without_the_sheet, sheet_as_a_standalone_document, fsid)."""
    found = find_section(doc)
    if not found:
        return None
    a, b, fsid = found
    section = doc[a:b]
    head = doc[:doc.index('<body')]
    chain = wrappers(doc, a)
    sheet = (head + '<body>\n' + ''.join(chain) + '\n' + section + '\n'
             + ''.join('</%s>' % re.match(r'<(\w+)', t).group(1) for t in reversed(chain))
             + '\n</body></html>\n')
    book, _note = strip_contents_row(doc[:a] + doc[b:], fsid)
    book = book.replace('</style>', FSNOTE_CSS + '</style>', 1)
    return book, sheet, fsid


if __name__ == '__main__':
    d = os.path.abspath(sys.argv[1])
    doc = open(os.path.join(d, 'dossier3.html'), encoding='utf-8').read()
    r = split(doc)
    print('no field sheet' if not r else
          f"id={r[2]!r}  book {len(r[0]):,}B  sheet {len(r[1]):,}B")
