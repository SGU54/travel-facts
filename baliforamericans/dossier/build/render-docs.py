# render-docs.py — render the compiled documents (_book.html, _sheet.html) with
# the book's own renderer, loaded without firing its bottom-of-file render().
import importlib.util, os, sys
BUILD = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, BUILD)
which = sys.argv[1:] or ['book', 'sheet']; sys.argv = sys.argv[:1]
src = open(os.path.join(BUILD, 'render-paged.py'), encoding='utf-8').read()
src = src.replace('\nif __name__ == "__main__":\n    render()\n', '\n')
spec = importlib.util.spec_from_file_location('rp', os.path.join(BUILD, 'render-paged.py'))
rp = importlib.util.module_from_spec(spec); sys.modules['rp'] = rp
exec(compile(src, 'render-paged.py', 'exec'), rp.__dict__)
if 'book' in which:
    print('── BOOK ──'); rp.render('_book.html', 'dossier.pdf')
if 'sheet' in which:
    print('── FIELD SHEET ──'); rp.render('_sheet.html', 'fieldsheet.pdf')
