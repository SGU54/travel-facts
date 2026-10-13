#!/usr/bin/env python3
"""Render a reviewable NEW-site SQL pair locally. Never connect to a database."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


RESERVED = {
    "public", "common", "information_schema", "auth", "storage", "extensions",
    "realtime", "graphql", "graphql_public", "supabase_functions",
    "supabase_migrations", "pgbouncer", "vault", "net", "cron",
}


def validate_schema(value: str) -> str:
    if not re.fullmatch(r"[a-z][a-z0-9_]{0,62}", value):
        raise ValueError("Schema must be 1–63 ASCII lowercase letters/digits/underscores, starting with a letter")
    if value in RESERVED or value.startswith(("pg_", "supabase_")):
        raise ValueError("Reserved/shared/system schema is not a new site target")
    return value


def validate_categories(raw: object) -> list[dict]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("Categories must be a nonempty JSON array")
    categories = []
    seen = set()
    for row in raw:
        if not isinstance(row, dict):
            raise ValueError("Each category must be an object")
        if set(row) - {"name", "slug", "parent_slug", "display_order"}:
            raise ValueError("Unknown category fields; use name, slug, parent_slug, display_order")
        name, slug = row.get("name"), row.get("slug")
        parent, order = row.get("parent_slug"), row.get("display_order")
        if not isinstance(name, str) or not name.strip() or "\x00" in name:
            raise ValueError("Each category needs a nonempty name without NUL")
        if not isinstance(slug, str) or not all(
            part and all(character.isalnum() for character in part)
            for part in slug.split("-")
        ):
            raise ValueError("Category slugs must use Unicode letters/numbers separated by single hyphens, without spaces or path separators")
        if slug in seen:
            raise ValueError(f"Duplicate category slug: {slug}")
        if parent is not None and (not isinstance(parent, str) or not parent):
            raise ValueError("parent_slug must be a slug or null")
        if isinstance(order, bool) or not isinstance(order, int) or not -(2**31) <= order < 2**31:
            raise ValueError("display_order must be a PostgreSQL integer")
        seen.add(slug)
        categories.append({"name": name, "slug": slug, "parent_slug": parent, "display_order": order})
    by_slug = {row["slug"]: row for row in categories}
    for row in categories:
        parent = row["parent_slug"]
        if parent is not None:
            if parent == row["slug"] or parent not in by_slug:
                raise ValueError(f"Invalid parent for {row['slug']}")
            if by_slug[parent]["parent_slug"] is not None:
                raise ValueError("This navigation contract supports two category levels; adapt it before adding more")
    return categories


def json_sql_literal(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    base = "travel_json_" + hashlib.sha256(payload.encode()).hexdigest()[:12]
    suffix = 0
    while True:
        delimiter = "$" + base + (f"_{suffix}" if suffix else "") + "$"
        if delimiter not in payload:
            return delimiter + payload + delimiter + "::jsonb"
        suffix += 1


def render(schema: str, raw: object, assets: Path) -> dict[str, str]:
    schema = validate_schema(schema)
    categories = validate_categories(raw)
    quoted_schema = '"' + schema + '"'
    result = {}
    for template, target in (("schema.sql", "0001_core.sql"), ("seed.sql", "0002_categories.sql")):
        content = (assets / template).read_text(encoding="utf-8")
        if "{{SITE_SCHEMA}}" not in content:
            raise ValueError(f"Missing schema token in {template}")
        if template == "seed.sql" and content.count("{{CATEGORY_JSON}}") != 1:
            raise ValueError("seed.sql must contain exactly one category JSON token")
        content = content.replace("{{SITE_SCHEMA}}", quoted_schema)
        # Check remaining template tokens BEFORE inserting untrusted category text.
        remainder = content.replace("{{CATEGORY_JSON}}", "")
        if re.search(r"\{\{[A-Z_]+\}\}", remainder):
            raise ValueError(f"Unresolved template token in {template}")
        content = content.replace("{{CATEGORY_JSON}}", json_sql_literal(categories))
        result[target] = "-- Rendered locally for review; NOT applied to any database.\n" + content
    return result


def write_outputs(outputs: dict[str, str], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    if any((destination / name).exists() for name in outputs):
        raise ValueError("Output already exists; use a new review directory. Existing migrations are never overwritten")
    created = []
    try:
        for name, content in outputs.items():
            with (destination / name).open("x", encoding="utf-8") as stream:
                created.append(destination / name)
                stream.write(content)
    except Exception:
        for path in created:
            path.unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--categories", type=Path, required=True, help="Approved category JSON array")
    parser.add_argument("--out-dir", type=Path, required=True, help="New local review directory")
    args = parser.parse_args()
    try:
        raw = json.loads(args.categories.read_text(encoding="utf-8"))
        outputs = render(args.schema, raw, Path(__file__).resolve().parent.parent / "assets")
        write_outputs(outputs, args.out_dir)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for name, content in outputs.items():
        print(f"REVIEW FILE {args.out_dir / name} sha256={hashlib.sha256(content.encode()).hexdigest()}")
    print("Local rendering only. Database schema, grants, RLS, and API behavior remain unverified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
