#!/usr/bin/env python3
"""add-nav.py — give a finished dossier PDF the two things it shipped without:
a bookmark outline, and clickable external links.

Why: all six PDFs in livres-2026-09-26 had ZERO bookmarks, and Morocco and
Thailand had zero link annotations of any kind. A 45-57pp reference book with no
outline is one a reader cannot navigate, and the books send readers to their own
/sources ledger and to official sites in text that was not clickable.

Bookmarks come from the contents section's own anchors resolved against the PDF's
named destinations, so an outline entry can never point somewhere the contents
page does not — they are generated from the same hrefs Paged.js already resolved.

Run:  python3 add-nav.py <build-dir> [--out FILE]
Reads <build-dir>/dossier3.html and <build-dir>/dossier.pdf; rewrites the PDF.
"""
import os, re, sys, subprocess, html as _html

# The TLDs the fleet actually cites. Rome names six official sources and five of
# them are .it or .va, so without those the book's most useful links — the
# Vatican ticket office, the Colosseum, the transport authority — stayed text.
# .es and .cat added for Barcelona: a Catalan destination's official sources
# (the transport authority, the city's own tax pages) live on both.
URL_RE = re.compile(
    r'\b(?:[a-z0-9-]+\.)+(?:com|org|net|gr|gov|it|va|eu|es|cat|co\.uk)(?:/[A-Za-z0-9._~:/?#\[\]@!$&\'()*+,;=%-]*)?',
    re.I)
# text that looks like a domain but is not a site we want to send a reader to
SKIP = re.compile(r'^(e\.g|i\.e|etc|vs)\.', re.I)


def read(p):
    return open(p, encoding='utf-8').read()


def toc_entries(doc):
    """(title, anchor-id, part-or-None) in reading order, from the contents section.

    The five books write their contents three different ways — a <table> of <tr>,
    a <ul> whose title sits in span.t OUTSIDE the anchor (Turkey), and an <ol>
    whose title is the anchor text (Japan) — so the row is located first and the
    title taken from whichever of the two places actually carries it.
    """
    best, n_best = None, 0
    for m in re.finditer(r'<section\b[^>]*>', doc):
        start = m.start()
        depth, i = 0, start
        while i < len(doc):
            o = doc.find('<section', i + 1)
            c = doc.find('</section>', i + 1)
            if c == -1:
                break
            if o != -1 and o < c:
                depth += 1; i = o
            elif depth:
                depth -= 1; i = c
            else:
                break
        body = doc[start:c]
        n = len(re.findall(r'href="#', body))
        if n > n_best:
            best, n_best = body, n
    if not best:
        return []
    out, part = [], None
    # A fourth contents idiom: Barcelona writes a <nav class="toc"> of bare <a>
    # elements — the anchor IS the row, with no <tr> or <li> around it. The row
    # matcher found nothing, so the book was handed an outline of zero bookmarks
    # while the script still reported success. Where there are no table or list
    # rows at all, take each anchor as its own row.
    rows = list(re.finditer(r'<(tr|li)\b[^>]*>(.*?)</\1>', best, re.S))
    if not rows:
        rows = list(re.finditer(r'(?P<t>)(?P<c><a href="#[^"]+"[^>]*>.*?</a>)', best, re.S))
    for row in rows:
        tag, cell = row.group(1), row.group(2)
        if 'class="part"' in row.group(0) and 'href="#' not in cell:
            part = _text(cell) or part
            continue
        a = re.search(r'<a href="#([^"]+)"[^>]*>(.*?)</a>', cell, re.S)
        if not a:
            continue
        title = _text(a.group(2))
        if not title:                                     # Turkey: title outside the <a>
            t = re.search(r'<span class="t">(.*?)</span>', cell, re.S)
            title = _text(t.group(1)) if t else ''
        if title:
            out.append((title, a.group(1), part))
    # de-duplicate: most books emit one anchor for the title and one for the folio
    seen, uniq = set(), []
    for t, i, p in out:
        if i in seen:
            continue
        seen.add(i); uniq.append((t, i, p))
    return uniq


def _text(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = _html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def word_boxes(pdf):
    """Every word with its page and box, from pdftotext -bbox-layout."""
    xml = subprocess.run(['pdftotext', '-bbox-layout', pdf, '-'],
                         capture_output=True, text=True, check=True).stdout
    pages = []
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        w, h, body = float(pm.group(1)), float(pm.group(2)), pm.group(3)
        words = []
        for wm in re.finditer(
                r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
                body, re.S):
            words.append((float(wm.group(1)), float(wm.group(2)), float(wm.group(3)),
                          float(wm.group(4)), _html.unescape(wm.group(5))))
        pages.append((w, h, words))
    return pages


def main():
    build = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
    # --pdf lets the phone edition, which is paginated from the same source and so
    # carries the same anchors, get the same outline as the print book.
    pdf = os.path.join(build, sys.argv[sys.argv.index('--pdf') + 1]
                       if '--pdf' in sys.argv else 'dossier.pdf')
    out = pdf
    if '--out' in sys.argv:
        out = sys.argv[sys.argv.index('--out') + 1]
    import pypdf
    from pypdf.annotations import Link
    doc = read(os.path.join(build, 'dossier3.html'))
    r = pypdf.PdfReader(pdf)
    w = pypdf.PdfWriter(clone_from=pdf)

    # ---- where does each named destination land? -------------------------------
    dest_page = {}
    for name, d in (r.named_destinations or {}).items():
        try:
            dest_page[name.lstrip('/')] = r.get_destination_page_number(d)
        except Exception:
            pass
    if not dest_page:            # fall back to the link annotations themselves
        for pi, pg in enumerate(r.pages):
            for a in (pg.get('/Annots') or []):
                o = a.get_object()
                if o.get('/Subtype') == '/Link' and o.get('/Dest'):
                    dest_page.setdefault(str(o['/Dest']).lstrip('/'), None)

    # ---- bookmarks -------------------------------------------------------------
    entries = toc_entries(doc)
    made, parents, skipped = 0, {}, []
    for title, aid, part in entries:
        pi = dest_page.get(aid)
        if pi is None:
            skipped.append(aid); continue
        par = None
        if part:
            if part not in parents:
                parents[part] = w.add_outline_item(part, pi, bold=True)
            par = parents[part]
        w.add_outline_item(title, pi, parent=par)
        made += 1

    # ---- external links --------------------------------------------------------
    added = 0
    try:
        pages = word_boxes(pdf)
    except Exception as e:
        pages = []; print(f"  ! bbox pass unavailable ({e})")
    for pi, (pw, ph, words) in enumerate(pages):
        if pi >= len(w.pages):
            break
        mw, mh = w.pages[pi].mediabox.width, w.pages[pi].mediabox.height
        sx, sy = float(mw) / pw, float(mh) / ph
        for (x0, y0, x1, y1, txt) in words:
            t = txt.strip().strip('.,;:)(“”"’')
            if not URL_RE.fullmatch(t) or SKIP.match(t):
                continue
            # A wrapped domain leaves a tail fragment as its own word box —
            # "greeceforamerican-/s.com" produced a link to https://s.com. Any real
            # host here has a first label of at least three characters.
            if len(t.split('/')[0].split('.')[0]) < 3:
                continue
            host, _, path = t.partition('/')
            uri = t if t.startswith('http') else 'https://' + host.lower() + (('/' + path) if path else '')
            # pdftotext y grows downward; PDF user space grows upward
            rect = (x0 * sx, float(mh) - y1 * sy, x1 * sx, float(mh) - y0 * sy)
            w.add_annotation(page_number=pi, annotation=Link(rect=rect, url=uri))
            added += 1

    with open(out, 'wb') as f:
        w.write(f)
    name = os.path.basename(os.path.dirname(build)) or build
    print(f"  bookmarks: {made}/{len(entries)} ({len(parents)} groups)"
          f"   external links: +{added}")
    if skipped:
        print(f"  ! no destination for: {', '.join(skipped[:6])}")
    return 0 if made else 1


if __name__ == '__main__':
    sys.exit(main())
