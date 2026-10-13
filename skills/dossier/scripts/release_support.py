"""Small shared contract for explicit guide outputs; no rendering or network access."""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path


class ContractError(ValueError):
    pass


def load_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ContractError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    try:
        def invalid_number(value):
            raise ContractError(f"non-finite JSON number is invalid: {value}")
        return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique,
                          parse_constant=invalid_number)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot read {path}: {exc}") from exc


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def local_path(root, value, suffix=None, must_exist=True):
    if not isinstance(value, str) or not value.strip():
        raise ContractError("an explicit relative file path is required")
    relative = Path(value)
    if relative.is_absolute():
        raise ContractError(f"absolute build path is not allowed: {value}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ContractError(f"path escapes build directory: {value}")
    if suffix and path.suffix.lower() != suffix:
        raise ContractError(f"expected {suffix} file: {value}")
    if must_exist and not path.is_file():
        raise ContractError(f"missing file: {value}")
    return path


def manifest(root):
    root = Path(root).resolve()
    obj = load_json(root / "release.json")
    if not isinstance(obj, dict) or type(obj.get("schema_version")) is not int or obj["schema_version"] != 1:
        raise ContractError("release.json requires schema_version: 1")
    for key in ("title", "edition", "release_date"):
        if not isinstance(obj.get(key), str) or not obj[key].strip():
            raise ContractError(f"release.json requires {key}")
    try:
        if date.fromisoformat(obj["release_date"]).isoformat() != obj["release_date"]:
            raise ValueError("not an ISO date")
    except ValueError as exc:
        raise ContractError("release_date must be YYYY-MM-DD") from exc
    if obj.get("purpose", "publication") not in ("publication", "proof"):
        raise ContractError("purpose must be publication or proof")
    if obj.get("evidence", "evidence.json") != "evidence.json":
        raise ContractError("the evidence contract uses evidence.json")
    documents = obj.get("documents")
    if not isinstance(documents, list) or len(documents) < 2:
        raise ContractError("declare both book and sheet in documents")
    seen, paths = set(), set()
    reserved = {root / "release.json", root / "evidence.json", root / "bindings.json"}
    reserved.add(local_path(root, obj.get("review", "review.json"), ".json", False))
    for doc in documents:
        if not isinstance(doc, dict) or doc.get("id") not in ("book", "sheet", "phone"):
            raise ContractError("document id must be book, sheet, or phone")
        identity = doc["id"]
        if identity in seen or doc.get("role", identity) != identity:
            raise ContractError(f"duplicate id or conflicting role: {identity}")
        seen.add(identity)
        for key, suffix in (("template", ".html"), ("html", ".html"), ("pdf", ".pdf")):
            path = local_path(root, doc.get(key), suffix, False)
            if path in paths or path in reserved:
                raise ContractError(f"input/output paths must be distinct: {doc.get(key)}")
            paths.add(path)
        critical = local_path(root, doc.get("critical_json", identity + "-critical.json"), ".json", False)
        if critical in paths or critical in reserved:
            raise ContractError(f"critical path overlaps another input/output: {critical.name}")
        paths.add(critical)
    if not {"book", "sheet"}.issubset(seen):
        raise ContractError("both book and sheet are required")
    return obj
