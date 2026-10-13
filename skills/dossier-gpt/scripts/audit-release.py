#!/usr/bin/env python3
"""Audit explicit book + Field Sheet artifacts. No skipped gate is a pass.

Usage: python3 audit-release.py BUILD_DIR [--prepare-review] [--json]
The review template is pending, never automatically approved. Exit 0 PASS, 1 FAIL,
2 BLOCKED. A proof can pass checks but is never declared ready for publication.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from release_support import ContractError, digest, load_json, local_path, manifest

HERE = Path(__file__).resolve().parent
REVIEW_CHECKS = ("facts", "decisions", "consistency", "visual", "navigation")


def gate_script(name, *arguments):
    try:
        proc = subprocess.run([sys.executable, str(HERE / name), *map(str, arguments), "--json"],
                              capture_output=True, text=True, timeout=180)
        result = json.loads(proc.stdout)
        if not isinstance(result, dict):
            raise ValueError("gate output is not an object")
        result["command_exit_code"] = proc.returncode
        if proc.returncode != 0 and result.get("status") == "PASS":
            result["status"] = "BLOCKED"
            result.setdefault("errors", []).append("gate reported PASS with a nonzero exit code")
        if proc.returncode == 0 and result.get("status") != "PASS":
            result.setdefault("errors", []).append("gate did not report PASS")
        return result
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        return {"gate": name, "status": "BLOCKED", "errors": [str(exc)]}


def inspect_pdf(root, doc):
    result = {"gate": f"pdf:{doc['id']}", "status": "PASS", "errors": [], "warnings": []}
    try:
        import fitz
        pdf_path = local_path(root, doc["pdf"], ".pdf")
        with fitz.open(pdf_path) as pdf:
            if pdf.needs_pass or not len(pdf):
                raise ContractError("PDF is encrypted or contains no pages")
            if not (pdf.metadata or {}).get("title", "").strip():
                result["errors"].append("PDF title metadata is missing")
            expected_size = doc.get("page_size_pt")
            if expected_size is not None and (not isinstance(expected_size, list) or
                    len(expected_size) != 2 or any(type(n) not in (int, float) or not math.isfinite(n) or n <= 0 for n in expected_size)):
                raise ContractError("page_size_pt must be [positive width, positive height]")
            page_texts, external, small = [], 0, []
            for index, page in enumerate(pdf, 1):
                if expected_size and any(abs(a - b) > 1 for a, b in zip((page.rect.width, page.rect.height), expected_size)):
                    result["errors"].append(f"page {index}: size differs from declared page_size_pt")
                page_texts.append(page.get_text())
                for block in page.get_text("dict").get("blocks", []):
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            text = span.get("text", "").strip()
                            if not text:
                                continue
                            x0, y0, x1, y1 = span["bbox"]
                            if not all(math.isfinite(v) for v in (x0, y0, x1, y1)) or x0 < -1 or y0 < -1 or x1 > page.rect.width + 1 or y1 > page.rect.height + 1:
                                result["errors"].append(f"page {index}: text extends beyond the page: {text[:90]!r}")
                            if span.get("size", 0) < 8.9:
                                small.append({"page": index, "pt": round(span.get("size", 0), 2), "text": text[:70]})
                for link in page.get_links():
                    if link.get("kind") == fitz.LINK_GOTO:
                        target = link.get("page", -1)
                        if not isinstance(target, int) or target < 0 or target >= len(pdf):
                            result["errors"].append(f"page {index}: unresolved internal link")
                    if link.get("kind") == fitz.LINK_URI:
                        uri = link.get("uri", "")
                        parsed = urlsplit(uri)
                        if parsed.scheme in ("https", "http") and parsed.netloc:
                            external += 1
                        elif parsed.scheme != "mailto":
                            result["errors"].append(f"page {index}: malformed external link {uri!r}")
            if not "".join(page_texts).strip():
                result["errors"].append("PDF contains no extractable text")
            if not external:
                result["errors"].append("no clickable external source/update links in this PDF")
            toc = pdf.get_toc()
            if doc["id"] in ("book", "phone") and len(pdf) > 4 and not toc:
                result["errors"].append("book longer than four pages has no PDF bookmarks")
            for _, label, target in toc:
                if target < 1 or target > len(pdf):
                    result["errors"].append(f"bookmark {label!r} has an invalid page")
            if small:
                result["warnings"].append({"message": "Text below 9pt: confirm it is secondary furniture, not essential content.", "spans": small[:40], "total": len(small)})
            result["checked"] = {"pages": len(pdf), "external_links": external, "bookmarks": len(toc)}
            result["snapshot"] = {"pdf_sha256": digest(pdf_path), "html_sha256": digest(local_path(root, doc["html"], ".html")), "page_count": len(pdf)}
    except (ImportError, OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        result["status"] = "BLOCKED"
        result["errors"].append(str(exc))
    if result["errors"] and result["status"] != "BLOCKED":
        result["status"] = "FAIL"
    return result


def review_template(root, release, snapshots):
    return {"schema_version": 1, "reviewer": "", "reviewed_at": "",
            "release_sha256": digest(root / "release.json"),
            "evidence_sha256": digest(root / "evidence.json"),
            "bindings_sha256": digest(root / "bindings.json"),
            "documents": {identity: {**snapshot, "pages_viewed": [],
                          "checks": {name: "pending" for name in REVIEW_CHECKS}, "notes": []}
                          for identity, snapshot in snapshots.items()},
            "scenarios": [], "open_issues": []}


def inspect_review(root, release, snapshots):
    result = {"gate": "review", "status": "PASS", "errors": []}
    try:
        review = load_json(local_path(root, release.get("review", "review.json"), ".json"))
        if not isinstance(review, dict) or review.get("schema_version") != 1:
            raise ContractError("review.json requires schema_version: 1")
        reviewer = review.get("reviewer")
        if not isinstance(reviewer, str) or not reviewer.strip() or reviewer.lower() in ("pending", "tbd", "unknown"):
            result["errors"].append("identify the actual reviewer")
        try:
            checked = date.fromisoformat(review.get("reviewed_at", ""))
            if checked < date.fromisoformat(release["release_date"]) or checked > date.today():
                raise ValueError("review date precedes release or is in the future")
        except (ValueError, TypeError):
            result["errors"].append("reviewed_at must be the actual YYYY-MM-DD review date, at/after release")
        for field, path in (("release_sha256", "release.json"), ("evidence_sha256", "evidence.json"), ("bindings_sha256", "bindings.json")):
            if review.get(field) != digest(root / path):
                result["errors"].append(f"review is stale: {path} changed")
        entries = review.get("documents", {})
        if not isinstance(entries, dict) or set(entries) != set(snapshots):
            raise ContractError("review must cover exactly the declared documents")
        for identity, snapshot in snapshots.items():
            entry = entries[identity]
            if not isinstance(entry, dict):
                raise ContractError(f"invalid review entry for {identity}")
            for field, value in snapshot.items():
                if entry.get(field) != value:
                    result["errors"].append(f"{identity}: review is stale ({field})")
            pages = entry.get("pages_viewed")
            if not isinstance(pages, list) or any(type(n) is not int for n in pages) or sorted(pages) != list(range(1, snapshot["page_count"] + 1)):
                result["errors"].append(f"{identity}: record every page actually viewed once")
            checks = entry.get("checks", {})
            if not isinstance(checks, dict) or any(checks.get(name) != "pass" for name in REVIEW_CHECKS):
                result["errors"].append(f"{identity}: editorial/visual/navigation checks remain incomplete")
            notes = entry.get("notes")
            if not isinstance(notes, list) or not notes or not all(isinstance(n, str) and n.strip() for n in notes):
                result["errors"].append(f"{identity}: add concrete observations from the review")
        scenarios = review.get("scenarios")
        if not isinstance(scenarios, list) or len(scenarios) < 2:
            result["errors"].append("test the principal traveler and a materially different scenario")
        else:
            ids = set()
            for scenario in scenarios:
                if not isinstance(scenario, dict) or not all(isinstance(scenario.get(k), str) and scenario[k].strip() for k in ("id", "details")) or scenario.get("result") != "pass":
                    result["errors"].append("each scenario needs an id, concrete details, and a passing result")
                    continue
                if scenario["id"] in ids:
                    result["errors"].append("scenario IDs must be distinct")
                ids.add(scenario["id"])
        issues = review.get("open_issues")
        if not isinstance(issues, list):
            result["errors"].append("open_issues must be an explicit array")
        else:
            for issue in issues:
                if not isinstance(issue, dict) or issue.get("severity") != "minor" or issue.get("status") != "accepted" or not isinstance(issue.get("explanation"), str) or not issue["explanation"].strip():
                    result["errors"].append("unresolved issue: only an explicitly accepted, explained minor issue may remain")
    except (ContractError, OSError, KeyError, TypeError) as exc:
        result["status"] = "BLOCKED"
        result["errors"].append(str(exc))
    if result["errors"] and result["status"] != "BLOCKED":
        result["status"] = "FAIL"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("--prepare-review", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.build_dir.resolve()
    gates = []
    try:
        release = manifest(root)
        purpose = release.get("purpose", "publication")
        evidence = load_json(local_path(root, "evidence.json", ".json"))
        if not isinstance(evidence, dict) or not isinstance(evidence.get("sources"), list) or not all(isinstance(s, dict) for s in evidence["sources"]):
            raise ContractError("evidence.json must be an object with a sources array of objects")
        if purpose == "publication":
            for source in evidence.get("sources", []):
                url = source.get("url", "")
                if not isinstance(url, str):
                    raise ContractError("a source URL must be a string")
                host = (urlsplit(url).hostname or "").lower()
                if host.endswith((".invalid", ".test", ".example")) or host in ("example.com", "example.org", "example.net", "localhost"):
                    raise ContractError("synthetic/reserved source URL in a publication; replace with actual verified evidence")
        gates.append(gate_script("audit-evidence.py", root))
        gates.append(gate_script("compile-guide.py", root, "--check"))
        snapshots = {}
        for doc in release["documents"]:
            structure = inspect_pdf(root, doc)
            gates.append(structure)
            if "snapshot" in structure:
                snapshots[doc["id"]] = structure["snapshot"]
            critical = local_path(root, doc.get("critical_json", doc["id"] + "-critical.json"), ".json")
            result = gate_script("audit-content.py", local_path(root, doc["html"], ".html"), local_path(root, doc["pdf"], ".pdf"), "--critical-json", critical)
            result["gate"] = "content:" + doc["id"]
            gates.append(result)
        if args.prepare_review:
            if len(snapshots) != len(release["documents"]):
                raise ContractError("cannot prepare review until every final PDF/HTML pair exists")
            destination = local_path(root, release.get("review", "review.json"), ".json", False)
            if destination.exists():
                raise ContractError("review file already exists; preserve observations and refresh only after inspecting changed artifacts")
            destination.write_text(json.dumps(review_template(root, release, snapshots), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            gates.append({"gate": "review", "status": "BLOCKED", "errors": ["pending review template created; inspect the artifacts and complete it honestly"]})
        else:
            if len(snapshots) != len(release["documents"]):
                gates.append({"gate": "review", "status": "BLOCKED", "errors": ["final document snapshots unavailable"]})
            else:
                gates.append(inspect_review(root, release, snapshots))
    except (ContractError, OSError, ValueError, TypeError, KeyError) as exc:
        purpose = "unknown"
        gates.append({"gate": "inputs", "status": "BLOCKED", "errors": [str(exc)]})
    status = "BLOCKED" if any(g.get("status") not in ("PASS", "FAIL") for g in gates) else ("FAIL" if any(g.get("status") == "FAIL" for g in gates) else "PASS")
    report = {"gate": "release", "status": status, "purpose": purpose,
              "release_ready": status == "PASS" and purpose == "publication", "gates": gates,
              "limits": "Checks validate recorded evidence, build consistency, and review completion; they do not independently prove factual truth or market value."}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for gate in gates:
            print(f"{gate.get('status', 'BLOCKED'):8} {gate.get('gate', 'unknown')}")
            for error in gate.get("errors", [])[:12]:
                print("  " + str(error))
            for warning in gate.get("warnings", [])[:4]:
                print("  REVIEW: " + str(warning))
        print("\n" + ("PROOF CHECKS PASS — not a publication approval" if status == "PASS" and purpose == "proof" else f"RELEASE {status}"))
        print(report["limits"])
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[status]


if __name__ == "__main__":
    sys.exit(main())
