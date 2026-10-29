# -*- coding: utf-8 -*-
"""lock-pdf.py <pdf> [<pdf>…] — the reader may read, print and copy text; nobody may change,
reorder or delete pages without the owner password (kept in _pdf-owner-password.txt, never in a package)."""
import sys, os, secrets, pymupdf
here = os.path.dirname(os.path.abspath(__file__)); pw_file = os.path.join(here, '_pdf-owner-password.txt')
if not os.path.exists(pw_file): open(pw_file, 'w').write(secrets.token_urlsafe(18))
owner = open(pw_file).read().strip()
perm = pymupdf.PDF_PERM_PRINT | pymupdf.PDF_PERM_PRINT_HQ | pymupdf.PDF_PERM_COPY | pymupdf.PDF_PERM_ACCESSIBILITY
for p in sys.argv[1:]:
    d = pymupdf.open(p); tmp = p + '.locked'
    d.save(tmp, encryption=pymupdf.PDF_ENCRYPT_AES_256, owner_pw=owner, user_pw='', permissions=perm, garbage=3, deflate=True); d.close()
    os.replace(tmp, p); print('locked', p, '(read/print/copy only)')
