#!/usr/bin/env python3
"""Real-PDF regression tests for audit-content.py, plus an optional browser test.

The deterministic renderer below reads a small HTML fixture and deliberately
places its seam paragraph across two PDF pages. It is a text-conservation test,
not a substitute for testing the Paged.js compositor. The latter is a separate
test and reports SKIP, never PASS, if Chromium is unavailable.
"""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('content_audit', HERE / 'audit-content.py')
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)

HTML = '''<!doctype html><html><head><title>Metadata is ignored</title></head><body>
<script>throw Error("untrusted source scripts must not run")</script>
<p hidden>Hidden 999</p><p style="display:none">Hidden 888</p>
<section>
<h1>Booking evidence</h1>
<p id="intro">Every traveller should keep the receipt.</p>
<p id="accents">Sagrada Família, Park Güell, menú del día. The oﬃce ﬁeld is non­refundable.</p>
<table><thead><tr><th>Ticket</th><th>Price</th></tr></thead><tbody>
<tr><td>Airport metro</td><td>€5.90 ◆</td></tr>
<tr><td>T-casual</td><td>NO airport metro ▲</td></tr></tbody></table>
<p id="seam">The room rate you compared when booking remains visible.</p>
<p id="last">Buy in euros, never USD. Hola and T-usual include the airport metro.</p>
</section></body></html>'''


def fixture_pdf(html_path, pdf_path, mutation=None):
    """Read the fixture's HTML strings and draw genuine selectable PDF text."""
    from lxml import html
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import simpleSplit
    font_paths = [Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
                  Path('/usr/local/share/fonts/DejaVuSans.ttf')]
    font_path = next((p for p in font_paths if p.exists()), None)
    if not font_path: raise unittest.SkipTest('DejaVu Sans is required for accent/glyph PDF fixtures.')
    pdfmetrics.registerFont(TTFont('ContentFixture', str(font_path)))
    root = html.document_fromstring(html_path.read_text(encoding='utf-8'))
    text = lambda ident: ''.join(root.get_element_by_id(ident).itertext())
    c = canvas.Canvas(str(pdf_path), pagesize=(612, 792))
    c.setFont('ContentFixture', 18)
    c.drawString(50, 720, ''.join(root.xpath('//h1')[0].itertext()))
    intro = text('intro')
    c.setFont('ContentFixture', 32)
    c.drawString(50, 655, intro[0])
    c.setFont('ContentFixture', 11)
    c.drawString(76, 655, intro[1:])
    y = 610
    for line in simpleSplit(text('accents').replace('\u00ad', ''), 'ContentFixture', 11, 500):
        c.drawString(50, y, line)
        y -= 16
    y -= 30
    for row in root.xpath('//table//tr'):
        cells = [''.join(cell.itertext()) for cell in row]
        if mutation == 'rule': cells = [cell.replace('NO airport', 'YES airport') for cell in cells]
        if mutation == 'price': cells = [cell.replace('€5.90', '') for cell in cells]
        c.drawString(50, y, cells[0]); c.drawString(300, y, cells[1]); y -= 24
    seam = text('seam')
    before, after = seam.split('compared', 1)
    # Exactly the failure class observed in the guide: the source has compared;
    # the intact PDF has com- / pared; the broken PDF loses comp and shows ared.
    c.drawString(50, 60, before + ('' if mutation == 'seam' else 'com-'))
    c.showPage(); c.setFont('ContentFixture', 11)
    c.drawString(50, 710, ('ared' if mutation == 'seam' else 'pared') + after)
    c.drawString(50, 660, text('last'))
    c.save()


class ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='dossier-content-')
        cls.dir = Path(cls.temp.name)
        cls.source = cls.dir / 'source.html'
        cls.source.write_text(HTML, encoding='utf-8')
        cls.pdf = cls.dir / 'intact.pdf'
        fixture_pdf(cls.source, cls.pdf)
        cls.critical = cls.dir / 'critical.json'
        cls.critical.write_text(json.dumps([
            {'id':'seam', 'text':'compared when booking', 'min_occurrences':1},
            {'id':'airport', 'text':'NO airport metro', 'min_occurrences':1}], ensure_ascii=False), encoding='utf-8')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_intact_accent_ligature_soft_hyphen_dropcap_table_and_wrap(self):
        report = content.audit(self.source, self.pdf, self.critical)
        self.assertEqual(report['status'], 'PASS', json.dumps(report, ensure_ascii=False, indent=2))
        self.assertEqual(report['pages'], 2)
        self.assertTrue(any(r['kind'] == 'geometric drop cap' for r in report['normalizations']))

    def test_missing_fragment_at_page_seam_fails(self):
        path = self.dir / 'broken-seam.pdf'
        fixture_pdf(self.source, path, 'seam')
        report = content.audit(self.source, path, self.critical)
        self.assertEqual(report['status'], 'FAIL', report)
        self.assertIn({'token':'compared', 'count':1}, report['missing'])
        self.assertIn({'token':'ared', 'count':1}, report['unexpected'])
        self.assertEqual(report['critical'][0]['status'], 'FAIL')
        self.assertTrue(any(e['page'] == 2 and 'ared when' in e['text'] for e in report['pdf_examples']))

    def test_changed_negation_fails(self):
        path = self.dir / 'broken-rule.pdf'
        fixture_pdf(self.source, path, 'rule')
        report = content.audit(self.source, path, self.critical)
        self.assertEqual(report['status'], 'FAIL')
        self.assertIn({'token':'no', 'count':1}, report['missing'])
        self.assertIn({'token':'yes', 'count':1}, report['unexpected'])

    def test_missing_price_fails(self):
        path = self.dir / 'broken-price.pdf'
        fixture_pdf(self.source, path, 'price')
        report = content.audit(self.source, path)
        self.assertEqual(report['status'], 'FAIL')
        self.assertIn({'token':'€', 'count':1}, report['missing'])

    def test_empty_visible_source_cannot_pass(self):
        path = self.dir / 'empty.html'
        path.write_text('<html><head></head><body><script>Only script</script><p hidden>Hidden text</p></body></html>')
        report = content.audit(path, self.pdf)
        self.assertEqual(report['status'], 'BLOCKED')
        self.assertTrue(any('No visible source text' in s for s in report['issues']))

    def test_broken_pdf_cannot_pass(self):
        path = self.dir / 'not-a-pdf.pdf'; path.write_bytes(b'not a PDF')
        self.assertEqual(content.audit(self.source, path)['status'], 'BLOCKED')

    def test_invalid_critical_contract_cannot_pass(self):
        path = self.dir / 'invalid-critical.json'
        path.write_text('[{"id":"bad","text":"compared","min_occurrences":0}]')
        self.assertEqual(content.audit(self.source, self.pdf, path)['status'], 'BLOCKED')

    def test_minimum_occurrences_checks_source_too(self):
        path = self.dir / 'twice.json'
        path.write_text('[{"id":"twice","text":"compared when booking","min_occurrences":2}]')
        report = content.audit(self.source, self.pdf, path)
        self.assertEqual(report['status'], 'FAIL')
        self.assertEqual(report['critical'][0]['source_occurrences'], 1)

    def test_static_css_uncertainty_is_recorded(self):
        path = self.dir / 'css.html'
        path.write_text(HTML.replace('</head>', '<style>.hidden {display:none}</style></head>'))
        source = content.static_source_data(path, 'Chromium unavailable in this test')
        self.assertTrue(source['issues'])
        self.assertIn('cannot validate stylesheets', source['issues'][0])

    def test_normalization_never_completes_a_missing_prefix(self):
        self.assertEqual(content._join_wraps('com-\npared', {'compared'}), 'compared')
        self.assertEqual(content._join_wraps('ared', {'compared'}), 'ared')
        self.assertEqual(content.tokens('oﬃce non\u00adrefundable menú €5.90 ◆'),
                         content.tokens('office nonrefundable menú €5.90 ◆'))

    def test_generated_toc_folio_requires_named_local_target_and_printed_number(self):
        from reportlab.pdfgen import canvas
        from pypdf import PdfReader, PdfWriter
        import fitz
        for shown, valid in [('2', True), ('3', False)]:
            raw = self.dir / f'toc-raw-{shown}.pdf'
            out = self.dir / f'toc-{shown}.pdf'
            c = canvas.Canvas(str(raw), pagesize=(612, 792))
            c.drawString(50, 700, 'Airport rule')
            c.drawString(250, 700, shown)
            c.linkRect('', 'rules', (45, 695, 270, 716), thickness=0)
            c.showPage(); c.bookmarkPage('rules')
            c.drawString(50, 700, 'Airport rule'); c.save()
            writer = PdfWriter(); writer.clone_document_from_reader(PdfReader(raw))
            writer.add_named_destination('rules', 1)
            with out.open('wb') as stream: writer.write(stream)
            with fitz.open(out) as doc:
                verified, issues = content.generated_page_refs(doc,
                    [{'href':'rules', 'label':'Airport rule'}])
                self.assertEqual(bool(verified), valid, (verified, issues))
                self.assertEqual(bool(issues), not valid)
                if valid: self.assertEqual(verified[0]['folio'], '2')

    def test_number_in_toc_label_is_not_mistaken_for_its_folio(self):
        from reportlab.pdfgen import canvas
        from pypdf import PdfReader, PdfWriter
        import fitz
        raw, out = self.dir/'toc-label-raw.pdf', self.dir/'toc-label.pdf'
        c = canvas.Canvas(str(raw), pagesize=(612, 792))
        c.drawString(50, 700, 'Decision 2')
        c.linkRect('', 'decision-two', (45, 695, 270, 716), thickness=0)
        c.showPage(); c.bookmarkPage('decision-two'); c.drawString(50, 700, 'Decision 2'); c.save()
        writer = PdfWriter(); writer.clone_document_from_reader(PdfReader(raw))
        writer.add_named_destination('decision-two', 1)
        with out.open('wb') as stream: writer.write(stream)
        with fitz.open(out) as doc:
            verified, issues = content.generated_page_refs(doc,
                [{'href':'decision-two', 'label':'Decision 2'}])
        self.assertFalse(verified)
        self.assertTrue(issues)

    def test_cli_emits_machine_readable_fail_and_code(self):
        path = self.dir / 'cli-broken.pdf'; fixture_pdf(self.source, path, 'seam')
        proc = subprocess.run([os.environ.get('CODEX_PRIMARY_RUNTIME_PYTHON', 'python3'),
            str(HERE/'audit-content.py'), str(self.source), str(path), '--json'],
            text=True, capture_output=True)
        self.assertEqual(proc.returncode, 1, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)['status'], 'FAIL')

    def test_renderer_rejects_path_escape_before_launching_browser(self):
        node = os.environ.get('CODEX_PRIMARY_RUNTIME_NODE') or shutil.which('node')
        if not node: self.skipTest('Node unavailable for renderer preflight test.')
        build = self.dir / 'unsafe-build'; build.mkdir()
        (build/'release.json').write_text(json.dumps({'documents':[
            {'id':'book', 'html':'../source.html', 'pdf':'book.pdf',
             'critical_json':'../critical.json'}]}))
        proc = subprocess.run([node, str(HERE/'render-guide.mjs'), str(build)],
                              text=True, capture_output=True)
        self.assertEqual(proc.returncode, 2)
        self.assertIn('Path escapes build directory', proc.stderr)
        self.assertFalse((build/'book.pdf').exists())

    def test_full_paged_renderer_when_chromium_available(self):
        node = os.environ.get('CODEX_PRIMARY_RUNTIME_NODE') or shutil.which('node')
        if not node: self.skipTest('Node unavailable: full Paged.js render was not tested.')
        probe = subprocess.run([node, '-e', content.SOURCE_JS, str(self.source)],
                               text=True, capture_output=True, timeout=60)
        if probe.returncode:
            self.skipTest('Chromium unavailable: full Paged.js render was not tested; real-PDF comparator tests still run.')
        build = self.dir / 'browser-build'; build.mkdir()
        docs = []
        for ident in ['book', 'sheet']:
            (build/f'{ident}.html').write_text(HTML)
            (build/f'{ident}-critical.json').write_text(self.critical.read_text())
            docs.append({'id':ident, 'html':f'{ident}.html', 'pdf':f'{ident}.pdf',
                         'critical_json':f'{ident}-critical.json'})
        (build/'release.json').write_text(json.dumps({'documents':docs}))
        proc = subprocess.run([node, str(HERE/'render-guide.mjs'), str(build)],
                               text=True, capture_output=True, timeout=180)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertTrue((build/'book.pdf').is_file())
        self.assertTrue((build/'sheet.pdf').is_file())


if __name__ == '__main__':
    unittest.main(verbosity=2)
