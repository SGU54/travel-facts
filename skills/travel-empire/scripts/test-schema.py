#!/usr/bin/env python3
"""Offline SQL rendering safety checks; does not execute PostgreSQL or prove RLS."""

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("render_schema", ROOT / "scripts/render-schema.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
BASE = [{"name": "Plan", "slug": "plan", "parent_slug": None, "display_order": 1}]


class SchemaRenderingTests(unittest.TestCase):
    def test_reserved_and_injected_targets_are_rejected(self):
        for schema in ("public", "common", "auth", "pg_catalog", "supabase_storage",
                       'japan"; DROP SCHEMA common;--', "Japan", "a" * 64, ""):
            with self.subTest(schema=schema), self.assertRaises(ValueError):
                MODULE.render(schema, BASE, ROOT / "assets")

    def test_valid_target_is_qualified_and_does_not_overwrite_live_schema(self):
        rendered = MODULE.render("test_city_us", BASE, ROOT / "assets")
        schema = rendered["0001_core.sql"]
        self.assertIn('CREATE SCHEMA "test_city_us";', schema)
        self.assertNotIn("IF NOT EXISTS", schema)
        self.assertNotIn("{{SITE_SCHEMA}}", schema)
        self.assertIn("status = 'published'", schema)
        self.assertIn("articles ENABLE ROW LEVEL SECURITY", schema)

    def test_dangerous_names_remain_json_data(self):
        name = "D'Art; DROP TABLE common.facts; \\ ' {{SITE_SCHEMA}}"
        rows = [{**BASE[0], "name": name}]
        rendered = MODULE.render("test_city", rows, ROOT / "assets")["0002_categories.sql"]
        match = re.search(r"payload jsonb := (\$travel_json_[a-z0-9_]+\$)(.*?)\1::jsonb;", rendered, re.S)
        self.assertIsNotNone(match)
        self.assertEqual(json.loads(match.group(2)), rows)

    def test_empty_duplicate_and_broken_taxonomies_fail(self):
        examples = [[], BASE + BASE, [{**BASE[0], "parent_slug": "missing"}],
                    [{**BASE[0], "display_order": True}],
                    [{**BASE[0], "slug": "a/b"}],
                    [{**BASE[0], "parent_slug": "plan"}],
                    [{**BASE[0], "name": ""}]]
        for rows in examples:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                MODULE.render("test_city", rows, ROOT / "assets")

    def test_deep_tree_requires_navigation_change(self):
        rows = BASE + [
            {"name": "Entry", "slug": "entry", "parent_slug": "plan", "display_order": 1},
            {"name": "Visa", "slug": "visa", "parent_slug": "entry", "display_order": 1},
        ]
        with self.assertRaises(ValueError):
            MODULE.render("test_city", rows, ROOT / "assets")

    def test_multilingual_slugs_are_preserved_as_category_data(self):
        rows = [
            {"name": "Voyage", "slug": "café-à-paris", "parent_slug": None, "display_order": 1},
            {"name": "السفر", "slug": "السفر-٢٠٢٦", "parent_slug": "café-à-paris", "display_order": 1},
            {"name": "旅行", "slug": "東京-旅行-2026", "parent_slug": "café-à-paris", "display_order": 2},
        ]
        rendered = MODULE.render("test_city", rows, ROOT / "assets")["0002_categories.sql"]
        match = re.search(r"payload jsonb := (\$travel_json_[a-z0-9_]+\$)(.*?)\1::jsonb;", rendered, re.S)
        self.assertIsNotNone(match)
        self.assertEqual(json.loads(match.group(2)), rows)

    def test_multilingual_slugs_still_reject_unsafe_path_characters(self):
        for slug in ("東京/旅行", "../東京", "東京 旅行", "café\\paris", "-café", "café-", "東京--旅行", "東京_旅行"):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                MODULE.render("test_city", [{**BASE[0], "slug": slug}], ROOT / "assets")

    def test_missing_template_token_is_an_error(self):
        with tempfile.TemporaryDirectory() as temporary:
            assets = Path(temporary)
            (assets / "schema.sql").write_text("SELECT 1;")
            with self.assertRaises(ValueError):
                MODULE.render("test_city", BASE, assets)

    def test_cli_writes_review_files_and_refuses_replacement(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            categories = folder / "categories.json"
            categories.write_text(json.dumps(BASE))
            destination = folder / "review"
            command = [sys.executable, str(ROOT / "scripts/render-schema.py"),
                       "--schema", "test_city", "--categories", str(categories),
                       "--out-dir", str(destination)]
            first = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertIn("remain unverified", first.stdout)
            before = {p.name: p.read_bytes() for p in destination.iterdir()}
            second = subprocess.run(command, text=True, capture_output=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(before, {p.name: p.read_bytes() for p in destination.iterdir()})


if __name__ == "__main__":
    unittest.main()
