#!/usr/bin/env python3
"""Behavioral contract tests with explicitly synthetic, real-PDF book/sheet fixtures.

The review records here are test data, not editorial attestations for a real product.
No network calls; no claim that this exercises a browser/Paged.js render.
"""
import copy
from datetime import date
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from release_support import ContractError, digest, load_json, manifest


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


compiler = module("compile-guide")
release = module("audit-release")


def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fixture(root):
    """Make raw templates, compile shared evidence, and independently typeset test PDFs."""
    evidence = load_json(HERE.parent / "assets/evidence-example.json")
    write_json(root / "evidence.json", evidence)
    project = {"schema_version": 1, "title": "SYNTHETIC guide proof", "edition": "test-1",
               "release_date": evidence["release_date"], "purpose": "proof", "assets": [],
               "documents": [{"id": ident, "template": ident + "-template.html", "html": ident + ".html",
                              "pdf": ident + ".pdf", "page_size_pt": [612, 792]}
                             for ident in ("book", "sheet")]}
    write_json(root / "release.json", project)
    for identity in ("book", "sheet"):
        snippets = "".join("<p>{{claim:" + claim["id"] + "}}</p>" for claim in evidence["claims"] if identity in claim.get("display", {}))
        content = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{{title}}</title></head><body>'
                   '<h1>{{title}}</h1><p>Checked {{release-date}}. Fictional training data only.</p>'
                   + snippets + '<p><a href="{{source-url:s-fares}}">Fictional source for this proof</a></p></body></html>')
        (root / (identity + "-template.html")).write_text(content, encoding="utf-8")
    compiler.compile_documents(root)
    from lxml import html
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import simpleSplit
    font = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    if not font.exists():
        raise unittest.SkipTest("DejaVu Sans is required for real-PDF test fixtures")
    pdfmetrics.registerFont(TTFont("ReleaseFixture", str(font)))
    snapshots = {}
    for doc in project["documents"]:
        tree = html.document_fromstring((root / doc["html"]).read_text(encoding="utf-8"))
        pdf = canvas.Canvas(str(root / doc["pdf"]), pagesize=(612, 792))
        pdf.setTitle(project["title"])
        y = 725
        for element in tree.xpath("//body/h1 | //body/p"):
            text = "".join(element.itertext())
            size = 18 if element.tag == "h1" else 11
            pdf.setFont("ReleaseFixture", size)
            for line in simpleSplit(text, "ReleaseFixture", size, 490):
                pdf.drawString(60, y, line)
                y -= size * 1.5
            for link in element.xpath(".//a"):
                pdf.linkURL(link.get("href"), (60, y, 550, y + size * 1.5), relative=0)
            y -= 15
        pdf.save()
        check = release.inspect_pdf(root, doc)
        if check["status"] != "PASS":
            raise AssertionError(check)
        snapshots[doc["id"]] = check["snapshot"]
    review = release.review_template(root, project, snapshots)
    review.update(reviewer="SYNTHETIC test record; no human approval claimed", reviewed_at=date.today().isoformat())
    for entry in review["documents"].values():
        entry["pages_viewed"] = list(range(1, entry["page_count"] + 1))
        entry["checks"] = {key: "pass" for key in release.REVIEW_CHECKS}
        entry["notes"] = ["Synthetic positive control for the review contract, not publication evidence."]
    review["scenarios"] = [
        {"id": "four journeys", "result": "pass", "details": "Synthetic 4 × 3.25 = 13.00, compared with 9.50 for one day."},
        {"id": "two journeys", "result": "pass", "details": "Synthetic 2 × 3.25 = 6.50, below the 9.50 pass price."}]
    write_json(root / "review.json", review)
    return project, snapshots


class ReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home = tempfile.TemporaryDirectory(prefix="dossier-release-test-")
        cls.base = Path(cls.home.name) / "base"
        cls.base.mkdir()
        cls.project, cls.snapshots = fixture(cls.base)

    @classmethod
    def tearDownClass(cls):
        cls.home.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dossier-release-case-")
        self.root = Path(self.temp.name)
        shutil.copytree(self.base, self.root, dirs_exist_ok=True)

    def tearDown(self):
        self.temp.cleanup()

    def run_release(self, *flags):
        proc = subprocess.run([sys.executable, str(HERE / "audit-release.py"), str(self.root), *flags, "--json"], capture_output=True, text=True, timeout=180)
        return proc, json.loads(proc.stdout)

    def test_real_book_and_sheet_pass_only_as_a_synthetic_proof(self):
        proc, report = self.run_release()
        self.assertEqual(proc.returncode, 0, report)
        self.assertEqual(report["status"], "PASS")
        self.assertFalse(report["release_ready"])
        self.assertEqual({g["gate"] for g in report["gates"]}, {"evidence", "bindings", "pdf:book", "content:book", "pdf:sheet", "content:sheet", "review"})

    def test_missing_sheet_cannot_silently_audit_another_pdf(self):
        (self.root / "sheet.pdf").unlink()
        proc, report = self.run_release()
        self.assertNotEqual(proc.returncode, 0)
        self.assertFalse(report["release_ready"])
        self.assertTrue(any(g["gate"] == "pdf:sheet" and g["status"] == "BLOCKED" for g in report["gates"]))

    def test_canonical_correction_requires_recompiling_both_outputs(self):
        evidence = load_json(self.root / "evidence.json")
        claim = evidence["claims"][0]
        claim["display"]["book"] += " Keep the ticket after validation."
        claim["display"]["sheet"] += " Keep the ticket after validation."
        write_json(self.root / "evidence.json", evidence)
        with self.assertRaisesRegex(ContractError, "stale"):
            compiler.compile_documents(self.root, check=True)
        compiler.compile_documents(self.root)
        self.assertIn("Keep the ticket", (self.root / "book.html").read_text())
        self.assertIn("Keep the ticket", (self.root / "sheet.html").read_text())
        report = release.inspect_review(self.root, self.project, self.snapshots)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("evidence.json changed" in error for error in report["errors"]))

    def test_editing_generated_html_is_not_a_canonical_fix(self):
        path = self.root / "sheet.html"
        path.write_text(path.read_text().replace("XCU 3.25", "XCU 8.75"))
        with self.assertRaisesRegex(ContractError, "edited, or stale"):
            compiler.compile_documents(self.root, check=True)

    def test_untracked_local_chart_blocks_compilation(self):
        path = self.root / "book-template.html"
        path.write_text(path.read_text().replace("</body>", '<img src="chart.svg"></body>'))
        (self.root / "chart.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><text>3.25</text></svg>')
        with self.assertRaisesRegex(ContractError, "untracked local asset"):
            compiler.compile_documents(self.root)

    def test_changed_declared_chart_invalidates_the_build(self):
        path = self.root / "chart.svg"
        path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text>3.25</text></svg>')
        project = load_json(self.root / "release.json")
        project["assets"] = ["chart.svg"]
        write_json(self.root / "release.json", project)
        compiler.compile_documents(self.root)
        path.write_text(path.read_text().replace("3.25", "8.75"))
        with self.assertRaisesRegex(ContractError, "bindings.json is missing or stale"):
            compiler.compile_documents(self.root, check=True)

    def test_untracked_font_inside_declared_css_is_rejected(self):
        template = self.root / "book-template.html"
        template.write_text(template.read_text().replace("</head>", '<link rel="stylesheet" href="print.css"></head>'))
        (self.root / "print.css").write_text('@font-face{font-family:test;src:url("fonts/body.woff2")}')
        project = load_json(self.root / "release.json")
        project["assets"] = ["print.css"]
        write_json(self.root / "release.json", project)
        with self.assertRaisesRegex(ContractError, "untracked local asset"):
            compiler.compile_documents(self.root)

    def test_nan_cannot_disable_page_size_checks(self):
        path = self.root / "release.json"
        path.write_text(path.read_text().replace("612,", "NaN,"))
        with self.assertRaisesRegex(ContractError, "non-finite"):
            manifest(self.root)

    def test_bad_evidence_returns_json_blocked_instead_of_traceback(self):
        evidence = load_json(self.root / "evidence.json")
        evidence["sources"] = [None]
        write_json(self.root / "evidence.json", evidence)
        proc, report = self.run_release()
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertEqual(report["status"], "BLOCKED")

    def test_example_sources_cannot_become_a_publication(self):
        project = load_json(self.root / "release.json")
        project["purpose"] = "publication"
        write_json(self.root / "release.json", project)
        proc, report = self.run_release()
        self.assertEqual(proc.returncode, 2)
        self.assertIn("synthetic/reserved", report["gates"][0]["errors"][0])

    def test_missing_editorial_review_blocks_even_intact_pdfs(self):
        (self.root / "review.json").unlink()
        proc, report = self.run_release()
        self.assertEqual(proc.returncode, 2)
        self.assertTrue(any(g["gate"] == "review" and g["status"] == "BLOCKED" for g in report["gates"]))

    def test_prepare_review_never_marks_checks_pass(self):
        (self.root / "review.json").unlink()
        proc, report = self.run_release("--prepare-review")
        self.assertEqual(proc.returncode, 2)
        review = load_json(self.root / "review.json")
        self.assertFalse(review["reviewer"])
        self.assertEqual(review["documents"]["sheet"]["pages_viewed"], [])
        self.assertEqual(set(review["documents"]["book"]["checks"].values()), {"pending"})

    def test_pdf_change_invalidates_review(self):
        import fitz
        path = self.root / "book.pdf"
        with fitz.open(path) as pdf:
            pdf.set_metadata({**pdf.metadata, "subject": "Changed after review"})
            pdf.saveIncr()
        snapshots = copy.deepcopy(self.snapshots)
        snapshots["book"]["pdf_sha256"] = digest(path)
        report = release.inspect_review(self.root, self.project, snapshots)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("pdf_sha256" in error for error in report["errors"]))

    def test_major_issue_cannot_be_waived_as_an_accepted_release(self):
        review = load_json(self.root / "review.json")
        review["open_issues"] = [{"severity": "major", "status": "accepted", "explanation": "Important exception still wrong"}]
        write_json(self.root / "review.json", review)
        self.assertEqual(release.inspect_review(self.root, self.project, self.snapshots)["status"], "FAIL")

    def test_paths_cannot_escape_or_overwrite_a_template(self):
        for changed in ("../elsewhere.html", "book-template.html"):
            project = copy.deepcopy(self.project)
            project["documents"][0]["html"] = changed
            write_json(self.root / "release.json", project)
            with self.assertRaises(ContractError):
                manifest(self.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
