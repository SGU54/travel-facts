# -*- coding: utf-8 -*-
"""render-both.py — render the Book and its Field Sheet as two documents.

The split happens at RENDER time, never in the source. Only one book in the
fleet generates its dossier3.html (Barcelona, from build-html.py); editing the
generated file there would be reverted by the next build, and editing six
different generators-that-don't-exist is not a thing. Reading the source and
writing two temporary documents costs nothing and leaves every tree untouched.

Usage:  python3 render-both.py [build-dir]
Out:    dossier.pdf  (the Book, with the sheet lifted out)
        fieldsheet.pdf (the dated companion)
"""
import importlib.util, os, sys

BUILD = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BUILD)

import fssplit                                                    # noqa: E402

doc = open(os.path.join(BUILD, 'dossier3.html'), encoding='utf-8').read()
got = fssplit.split(doc)
if not got:
    sys.exit('no field-sheet section found — nothing to split')
book, sheet, fsid = got
open(os.path.join(BUILD, '_book.html'), 'w', encoding='utf-8').write(book)
open(os.path.join(BUILD, '_sheet.html'), 'w', encoding='utf-8').write(sheet)
print(f"field sheet id={fsid!r}: book {len(book):,}B · sheet {len(sheet):,}B")

# the book's own renderer, loaded without firing its bottom-of-file render()
src = open(os.path.join(BUILD, 'render-paged.py'), encoding='utf-8').read()
src = src.replace('\nif __name__ == "__main__":\n    render()\n', '\n')
spec = importlib.util.spec_from_file_location('rp', os.path.join(BUILD, 'render-paged.py'))
rp = importlib.util.module_from_spec(spec)
sys.modules['rp'] = rp
exec(compile(src, 'render-paged.py', 'exec'), rp.__dict__)

print('── BOOK ──')
rp.render('_book.html', 'dossier.pdf')
print('── FIELD SHEET ──')
rp.render('_sheet.html', 'fieldsheet.pdf')
