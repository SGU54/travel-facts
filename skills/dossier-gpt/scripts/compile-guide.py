#!/usr/bin/env python3
"""Compile explicit book/sheet templates from canonical evidence; fail on stale bindings.

Usage: python3 compile-guide.py BUILD_DIR [--check] [--json]
No network calls. This validates binding integrity, not factual truth.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from release_support import ContractError, digest, load_json, local_path, manifest

TOKEN = re.compile(r"\{\{\s*([a-z-]+)(?::([A-Za-z0-9_.-]+))?\s*\}\}")


class AssetReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag == "base":
            raise ContractError("a base URL is not allowed in a portable print template")
        if tag in ("iframe", "object", "embed"):
            raise ContractError(f"{tag} content must be converted to a local static asset before printing")
        if "srcset" in attrs:
            raise ContractError("select one local image src for a reproducible print template; srcset is unsupported")
        if tag in ("img", "script", "source", "video", "audio"):
            if attrs.get("src"):
                self.references.append(attrs["src"])
            if attrs.get("poster"):
                self.references.append(attrs["poster"])
        if tag == "link" and attrs.get("href"):
            self.references.append(attrs["href"])
        if tag in ("image", "use"):
            target = attrs.get("href") or attrs.get("xlink:href")
            if target:
                self.references.append(target)

    handle_startendtag = handle_starttag


def validate_assets(root, pending, declared):
    """Reject untracked dependencies; a changed chart must invalidate the review too."""
    known = {local_path(root, value): value for value in declared}
    visited = set()

    def inspect(text, origin):
        refs = []
        if origin.suffix.lower() in (".html", ".svg"):
            parser = AssetReferences()
            parser.feed(text)
            refs.extend(parser.references)
        refs.extend(match[1].strip() for match in re.findall(r"url\(\s*(['\"]?)(.*?)\1\s*\)", text, re.I))
        refs.extend(re.findall(r"@import\s+['\"]([^'\"]+)['\"]", text, re.I))
        for reference in refs:
            if reference.startswith(("#", "data:")):
                continue
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                raise ContractError(f"{origin.name}: external asset {reference!r}; store it locally and declare it")
            path = (origin.parent / unquote(url.path)).resolve()
            if not path.is_relative_to(root):
                raise ContractError(f"asset escapes build directory: {reference}")
            if path not in known:
                raise ContractError(f"untracked local asset: {path.relative_to(root)}; add it to release.json assets")
            if path not in visited and path.suffix.lower() in (".css", ".svg"):
                visited.add(path)
                inspect(path.read_text(encoding="utf-8"), path)
    for path, content in pending:
        if path.suffix.lower() == ".html":
            inspect(content, path)


def keyed(items, label):
    result = {}
    if not isinstance(items, list):
        raise ContractError(f"evidence {label} must be an array")
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ContractError(f"invalid evidence {label} entry")
        if item["id"] in result:
            raise ContractError(f"duplicate {label} id: {item['id']}")
        result[item["id"]] = item
    return result


def compile_documents(root, check=False):
    release = manifest(root)
    evidence_path = local_path(root, "evidence.json", ".json")
    evidence = load_json(evidence_path)
    if not isinstance(evidence, dict) or evidence.get("schema_version") != 1:
        raise ContractError("evidence.json requires schema_version: 1")
    if evidence.get("release_date") != release["release_date"]:
        raise ContractError("book and evidence release dates disagree")
    claims = keyed(evidence.get("claims"), "claims")
    sources = keyed(evidence.get("sources"), "sources")
    for key, claim in claims.items():
        if not isinstance(claim.get("display", {}), dict):
            raise ContractError(f"claim {key}: display must be an object")
    records, pending = {}, []
    for doc in release["documents"]:
        identity = doc["id"]
        component = "book" if identity == "phone" else identity
        template = local_path(root, doc["template"], ".html")
        output = local_path(root, doc["html"], ".html", False)
        critical_path = local_path(root, doc.get("critical_json", identity + "-critical.json"), ".json", False)
        used = {}

        def replace(match):
            kind, key = match.groups()
            if kind == "claim" and key in claims:
                value = claims[key].get("display", {}).get(component)
                if not isinstance(value, str) or not value.strip():
                    raise ContractError(f"{identity}: {key} has no {component} display text")
                used[key] = used.get(key, 0) + 1
            elif kind in ("source-url", "source-label") and key in sources:
                source = sources[key]
                value = source.get("url") if kind == "source-url" else source.get("label", key)
                if not isinstance(value, str) or not value:
                    raise ContractError(f"{identity}: {key} has no {kind}")
            elif kind in ("title", "edition", "release-date") and key is None:
                value = release[kind.replace("-", "_")]
            else:
                raise ContractError(f"unknown template token: {match.group(0)}")
            return html.escape(value, quote=True)

        raw = template.read_text(encoding="utf-8")
        content = TOKEN.sub(replace, raw)
        if "{{" in content:
            raise ContractError(f"{identity}: unresolved or malformed template token")
        critical = []
        for key, claim in claims.items():
            value = claim.get("display", {}).get(component)
            if claim.get("critical") is True and value:
                if key not in used:
                    raise ContractError(f"{identity}: critical claim {key} is not bound in its template")
                critical.append({"id": key, "text": value, "min_occurrences": used[key]})
        if not critical:
            raise ContractError(f"{identity}: no critical content is declared")
        critical_text = json.dumps(critical, ensure_ascii=False, indent=2) + "\n"
        if check:
            if not output.is_file() or output.read_text(encoding="utf-8") != content:
                raise ContractError(f"{identity}: generated HTML is missing, edited, or stale; recompile")
            if not critical_path.is_file() or critical_path.read_text(encoding="utf-8") != critical_text:
                raise ContractError(f"{identity}: critical content record is missing or stale; recompile")
        pending.extend(((output, content), (critical_path, critical_text)))
        records[identity] = {"template": doc["template"], "template_sha256": digest(template),
                             "html": doc["html"], "claims": used}
    assets = release.get("assets", [])
    if not isinstance(assets, list) or not all(isinstance(item, str) for item in assets):
        raise ContractError("release assets must be a list of relative file paths")
    asset_hashes = {item: digest(local_path(root, item)) for item in assets}
    validate_assets(root, pending, assets)
    # Validate every document and asset before writing any output.
    if not check:
        for path, content in pending:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    for identity, record in records.items():
        record["html_sha256"] = digest(local_path(root, record["html"], ".html"))
    bindings = {"schema_version": 1, "release_sha256": digest(root / "release.json"),
                "evidence_sha256": digest(evidence_path), "assets_sha256": asset_hashes,
                "documents": records}
    path = root / "bindings.json"
    if check:
        if load_json(path) != bindings:
            raise ContractError("bindings.json is missing or stale; recompile")
    else:
        path.write_text(json.dumps(bindings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"gate": "bindings", "status": "PASS", "documents": records,
            "note": "Canonical bindings match; semantic consistency still needs editorial review."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = compile_documents(args.build_dir.resolve(), args.check)
        code = 0
    except (ContractError, OSError, UnicodeError, TypeError) as exc:
        result = {"gate": "bindings", "status": "BLOCKED", "errors": [str(exc)]}
        code = 2
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else
          f"{result['status']} bindings: " + ("; ".join(result.get("errors", [])) or result["note"]))
    return code


if __name__ == "__main__":
    sys.exit(main())
