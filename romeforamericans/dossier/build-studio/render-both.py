# -*- coding: utf-8 -*-
"""render-both.py (Rome) — the Book and its Field Sheet, as two documents.

Rome paginates with render4.py rather than Paged.js, so the split is driven
through RENDER_SRC / RENDER_OUT rather than by calling a render() function.
"""
import os, subprocess, sys
import fssplit

BUILD = os.path.dirname(os.path.abspath(__file__))
doc = open(os.path.join(BUILD, 'dossier3.html'), encoding='utf-8').read()
got = fssplit.split(doc)
if not got:
    sys.exit('no field-sheet section found')
book, sheet, fsid = got
open(os.path.join(BUILD, '_book.html'), 'w', encoding='utf-8').write(book)
open(os.path.join(BUILD, '_sheet.html'), 'w', encoding='utf-8').write(sheet)
print(f"field sheet id={fsid!r}: book {len(book):,}B · sheet {len(sheet):,}B")

for src, out, label in (('_book.html', 'dossier4.pdf', 'BOOK'),
                        ('_sheet.html', 'fieldsheet.pdf', 'FIELD SHEET')):
    print(f'── {label} ──')
    env = dict(os.environ, RENDER_SRC=src, RENDER_OUT=out)
    r = subprocess.run([sys.executable, 'render4.py'], cwd=BUILD, env=env)
    if r.returncode:
        sys.exit(f'{label} failed')
