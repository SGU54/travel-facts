#!/usr/bin/env python3
"""Check a dossier's declared evidence contract, never the truth of its sources.

Usage: audit-evidence.py BUILD_DIR [--json]
Exit 0: registry checks passed; 1: failed checks; 2: missing/unreadable input.
Standard library only. No network, eval, or implicit unit/currency conversions.
See references/evidence-contract.md for the version 1 contract and its limits.
"""

import argparse
from datetime import date
from decimal import Decimal, DecimalException, ROUND_HALF_UP, localcontext
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


SCHEMA_VERSION = 1
KINDS = {"primary", "secondary", "corpus", "observation", "publisher_policy"}
AUTHORITIES = {"official", "reported", "observed", "inference", "judgment"}
TOPICS = {"fare", "tax", "legal", "admission", "schedule", "geography", "other", "publisher_policy"}
PRIMARY_TOPICS = {"fare", "tax", "legal", "admission"}
FRESHNESS_DAYS = {"changeable": 90, "stable": 730}
ID = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*\Z")
DECIMAL = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?\Z")
UNIT = re.compile(r"(?:1|[A-Za-z][A-Za-z0-9_]*)(?:[*/](?:1|[A-Za-z][A-Za-z0-9_]*))*\Z")
PLACEHOLDER = re.compile(r"(?:tbd|todo|n/?a|unknown|check current|verify at source|to be confirmed|placeholder|\.\.\.|…)[ .!?]*\Z", re.I)


def normalized(text):
    return " ".join(text.split()).casefold() if isinstance(text, str) else ""


def contains_amount(text, amount):
    """Check canonical plain decimal notation (dot or comma), not prose meaning."""
    if not isinstance(text, str):
        return False
    for token in re.findall(r"(?<![\d.,])-?\d+(?:[.,]\d+)?(?!\d|[.,]\d)", text):
        if Decimal(token.replace(",", ".")) == amount:
            return True
    return False


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("non-finite JSON number: " + value)


class Auditor:
    def __init__(self, build_dir, data):
        self.build_dir = Path(build_dir).resolve()
        self.data = data
        self.errors = []
        self.counts = {}
        self.release = None
        self.source_dates = {}
        self.claim_dates = {}
        self.values = {}
        self.results = {}

    def error(self, path, message):
        self.errors.append(f"{path}: {message}")

    def text(self, obj, key, path):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip() or PLACEHOLDER.fullmatch(value.strip()):
            self.error(path + "." + key, "required non-placeholder text")
            return None
        return value.strip()

    def array(self, obj, key, path, minimum=0):
        value = obj.get(key)
        if not isinstance(value, list):
            self.error(path + "." + key, "required array")
            return []
        if len(value) < minimum:
            self.error(path + "." + key, f"requires at least {minimum} item(s)")
        return value

    def mapping(self, obj, key, path):
        value = obj.get(key)
        if not isinstance(value, dict):
            self.error(path + "." + key, "required object")
            return {}
        return value

    def day(self, obj, key, path, future=False, optional=False):
        if optional and key not in obj:
            return None
        value = obj.get(key)
        try:
            if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
                raise ValueError()
            parsed = date.fromisoformat(value)
        except ValueError:
            self.error(path + "." + key, "required ISO date YYYY-MM-DD")
            return None
        if not future and self.release and parsed > self.release:
            self.error(path + "." + key, "is after release_date")
        return parsed

    def index(self, key, minimum=0):
        result = {}
        for position, item in enumerate(self.array(self.data, key, "evidence", minimum)):
            path = f"{key}[{position}]"
            if not isinstance(item, dict):
                self.error(path, "must be an object")
                continue
            ident = item.get("id")
            if not isinstance(ident, str) or not ID.fullmatch(ident):
                self.error(path + ".id", "required stable identifier (letters, digits, dot, underscore, hyphen)")
            elif ident in result:
                self.error(path + ".id", "duplicate identifier " + ident)
            else:
                result[ident] = item
        self.counts[key] = len(result)
        return result

    def refs(self, obj, key, path, target, minimum=1):
        result = []
        seen = set()
        for position, ident in enumerate(self.array(obj, key, path, minimum)):
            where = f"{path}.{key}[{position}]"
            if not isinstance(ident, str) or ident not in target:
                self.error(where, f"unknown reference {ident!r}")
            elif ident in seen:
                self.error(where, f"duplicate reference {ident}")
            else:
                result.append(ident)
                seen.add(ident)
        return result

    def enum(self, obj, key, path, allowed):
        value = obj.get(key)
        if not isinstance(value, str) or value not in allowed:
            self.error(path + "." + key, "must be one of " + ", ".join(sorted(allowed)))
            return None
        return value

    def amount(self, obj, key, path):
        value = obj.get(key)
        if not isinstance(value, str) or len(value) > 60 or not DECIMAL.fullmatch(value):
            self.error(path + "." + key, "must be a finite decimal string, not a JSON number or expression")
            return None
        return Decimal(value)

    def measure(self, value, path):
        if not isinstance(value, dict):
            self.error(path, "requires {amount: decimal string, unit: string}")
            return None
        amount = self.amount(value, "amount", path)
        unit = value.get("unit")
        if not isinstance(unit, str) or len(unit) > 100 or not UNIT.fullmatch(unit):
            self.error(path + ".unit", "use explicit units such as EUR/person/night, journey, minute, or 1")
            return None
        dimensions = {}
        sign = 1
        for token in re.split(r"([*/])", unit):
            if token in ("*", "/"):
                sign = 1 if token == "*" else -1
            elif token != "1":
                dimensions[token] = dimensions.get(token, 0) + sign
        dimensions = {k: v for k, v in dimensions.items() if v}
        return (amount, dimensions) if amount is not None else None

    def sources_check(self, sources):
        for ident, source in sources.items():
            path = "sources." + ident
            kind = self.enum(source, "kind", path, KINDS)
            self.text(source, "locator", path)
            self.text(source, "scope", path)
            self.source_dates[ident] = self.day(source, "checked_at", path)
            url = source.get("url")
            artifact = source.get("artifact")
            if bool(url) == bool(artifact):
                self.error(path, "give exactly one url or observation artifact")
            if url:
                try:
                    parsed = urlsplit(url) if isinstance(url, str) else None
                    if not parsed or parsed.scheme not in {"https", "http"} or not parsed.hostname or parsed.username or parsed.password or any(c.isspace() for c in url):
                        raise ValueError()
                    parsed.port
                except ValueError:
                    self.error(path + ".url", "must be an HTTP(S) URL without credentials")
            if artifact:
                if kind != "observation":
                    self.error(path + ".artifact", "local artifacts are only for recorded observations; other sources need a URL")
                if not isinstance(artifact, str):
                    self.error(path + ".artifact", "must be a relative path to a retained observation file")
                else:
                    candidate = (self.build_dir / artifact).resolve()
                    if Path(artifact).is_absolute() or not candidate.is_relative_to(self.build_dir) or not candidate.is_file():
                        self.error(path + ".artifact", "must resolve to a file inside BUILD_DIR")

    def claims_check(self, claims, sources):
        for ident, claim in claims.items():
            path = "claims." + ident
            self.text(claim, "text", path)
            self.text(claim, "scope", path)
            authority = self.enum(claim, "authority", path, AUTHORITIES)
            volatility = self.enum(claim, "volatility", path, set(FRESHNESS_DAYS))
            topic = self.enum(claim, "topic", path, TOPICS)
            status = self.enum(claim, "status", path, {"verified", "qualified", "unresolved"})
            if status == "unresolved":
                self.error(path + ".status", "unresolved claim cannot be released; resolve, qualify safely, or withdraw it")
            if type(claim.get("critical")) is not bool:
                self.error(path + ".critical", "must be an explicit boolean")
            critical = claim.get("critical") is True
            source_ids = self.refs(claim, "sources", path, sources)
            source_kinds = {sources[s].get("kind") for s in source_ids if isinstance(sources[s].get("kind"), str)}
            if critical and topic in PRIMARY_TOPICS and "primary" not in source_kinds:
                self.error(path + ".sources", "critical fare, tax, legal and admission claims require a primary source")
            if authority == "official" and "primary" not in source_kinds and not (topic == "publisher_policy" and "publisher_policy" in source_kinds):
                self.error(path + ".authority", "official requires a primary source; publisher_policy only supports the publisher's own policy")
            if "publisher_policy" in source_kinds and topic != "publisher_policy" and not (source_kinds - {"publisher_policy", "corpus"}):
                self.error(path + ".sources", "the publisher's own policy cannot verify destination facts")
            as_of = self.day(claim, "as_of", path)
            recheck = self.day(claim, "recheck_by", path, future=True)
            start = self.day(claim, "valid_from", path, future=True, optional=True)
            end = self.day(claim, "valid_until", path, future=True, optional=True)
            self.claim_dates[ident] = as_of
            if start and end and start > end:
                self.error(path, "valid_from is after valid_until")
            if as_of and recheck and recheck < as_of:
                self.error(path, "recheck_by is before as_of")
            for source_id in source_ids:
                checked = self.source_dates.get(source_id)
                if as_of and checked and checked > as_of:
                    self.error(path + ".as_of", f"precedes the check of cited source {source_id}")
            if critical and self.release:
                if start and start > self.release:
                    self.error(path + ".valid_from", "claim does not yet apply at release_date")
                if end and end < self.release:
                    self.error(path + ".valid_until", "claim has expired at release_date")
                if recheck and recheck < self.release:
                    self.error(path + ".recheck_by", "recheck is overdue at release_date")
                if volatility and as_of:
                    ceiling = FRESHNESS_DAYS[volatility]
                    if (self.release - as_of).days > ceiling:
                        self.error(path + ".as_of", f"critical {volatility} claim was checked more than {ceiling} days before release")
                    if recheck and (recheck - as_of).days > ceiling:
                        self.error(path + ".recheck_by", f"exceeds the {ceiling}-day ceiling; use a shorter interval where needed")
                    for source_id in source_ids:
                        checked = self.source_dates.get(source_id)
                        if checked and (self.release - checked).days > ceiling:
                            self.error(path + ".sources", f"source {source_id} has not been checked within {ceiling} days")
            if authority in {"inference", "judgment"}:
                for i, assumption in enumerate(self.array(claim, "assumptions", path, 1)):
                    self.text({"text": assumption}, "text", f"{path}.assumptions[{i}]")
            if authority == "observed":
                survey = self.mapping(claim, "survey", path)
                self.text(survey, "method", path + ".survey")
                self.text(survey, "sample", path + ".survey")
                observed_from = self.day(survey, "observed_from", path + ".survey")
                observed_until = self.day(survey, "observed_until", path + ".survey")
                if observed_from and observed_until and observed_from > observed_until:
                    self.error(path + ".survey", "observation period is reversed")
                if observed_until and as_of and observed_until > as_of:
                    self.error(path + ".survey", "observations end after as_of")
                if "observation" not in source_kinds:
                    self.error(path + ".sources", "observed requires a retained observation source")
            display = self.mapping(claim, "display", path)
            if not display:
                self.error(path + ".display", "give at least one canonical book or sheet snippet")
            for component in display:
                if component not in {"book", "sheet"}:
                    self.error(path + ".display", "unknown component " + str(component))
                self.text(display, component, path + ".display")
            if status == "qualified":
                qualification = self.text(claim, "qualification", path)
                if qualification:
                    for component, snippet in display.items():
                        if normalized(qualification) not in normalized(snippet):
                            self.error(path + ".display." + component, "must retain the declared qualification verbatim")
            if critical and topic in {"fare", "tax"} and "value" not in claim:
                self.error(path + ".value", "a critical price or tax needs an actual amount and unit; 'check current' is not a value")
            if "value" in claim:
                value = self.measure(claim["value"], path + ".value")
                if value:
                    self.values[ident] = value
                    if topic in {"fare", "tax"} and value[0] < 0:
                        self.error(path + ".value", "a price or tax cannot be negative")
                    if critical and volatility == "changeable" and not contains_amount(display.get("sheet"), value[0]):
                        self.error(path + ".display.sheet", "must show the actual declared amount in plain decimal notation, not only 'check current'")
            if "calculation_id" in claim and authority != "inference":
                self.error(path + ".authority", "a computed claim must be labeled inference")

    def require_critical(self, ident, claims, path):
        if ident in claims and claims[ident].get("critical") is not True:
            self.error(path, f"referenced decision/sheet/calculation input {ident} must be marked critical")

    def calculations_check(self, calculations, claims):
        for ident, calc in calculations.items():
            path = "calculations." + ident
            operation = self.enum(calc, "operation", path, {"sum", "difference"})
            inputs = self.array(calc, "inputs", path, 1)
            if operation == "difference" and len(inputs) != 2:
                self.error(path + ".inputs", "difference requires exactly two inputs, in order")
            terms = []
            for i, term in enumerate(inputs):
                where = f"{path}.inputs[{i}]"
                if not isinstance(term, dict):
                    self.error(where, "must be an object")
                    continue
                ref = term.get("claim_id")
                if not isinstance(ref, str) or ref not in claims:
                    self.error(where + ".claim_id", f"unknown reference {ref!r}")
                    continue
                self.require_critical(ref, claims, where)
                if "calculation_id" in claims[ref]:
                    self.error(where + ".claim_id", "chained calculations are not supported; use source values directly")
                    continue
                value = self.values.get(ref)
                if not value:
                    self.error(where + ".claim_id", "claim needs an actual numeric value and unit")
                quantity = self.measure(term.get("quantity"), where + ".quantity")
                if quantity and quantity[0] < 0:
                    self.error(where + ".quantity", "quantity must be nonnegative; use difference for subtraction")
                if value and quantity:
                    dimensions = value[1].copy()
                    for name, power in quantity[1].items():
                        dimensions[name] = dimensions.get(name, 0) + power
                    dimensions = {k: v for k, v in dimensions.items() if v}
                    terms.append((value[0] * quantity[0], dimensions))
            expected = self.measure(calc.get("result"), path + ".result")
            if not terms or len(terms) != len(inputs) or not expected or not operation or (operation == "difference" and len(terms) != 2):
                continue
            if any(unit != terms[0][1] for _, unit in terms[1:]):
                self.error(path, "cannot add/subtract incompatible units; align person/party, time, distance and currency first")
                continue
            if expected[1] != terms[0][1]:
                self.error(path + ".result.unit", "does not match input units after quantity cancellation")
                continue
            total = sum((v for v, _ in terms), Decimal("0")) if operation == "sum" else terms[0][0] - terms[1][0]
            if "round_to" in calc:
                quantum = self.amount(calc, "round_to", path)
                if quantum is None or quantum <= 0 or quantum.normalize().as_tuple().digits != (1,):
                    self.error(path + ".round_to", "must be a positive power of ten, such as 0.01")
                    continue
                total = total.quantize(quantum.normalize(), rounding=ROUND_HALF_UP)
            if total != expected[0]:
                self.error(path + ".result.amount", f"arithmetic mismatch: declared {expected[0]}, calculated {total}")
            self.results[ident] = (total, expected[1])
        for ident, claim in claims.items():
            if "calculation_id" not in claim:
                continue
            ref = claim["calculation_id"]
            path = "claims." + ident + ".calculation_id"
            if not isinstance(ref, str) or ref not in calculations:
                self.error(path, f"unknown reference {ref!r}")
            elif ident not in self.values or ref not in self.results:
                self.error(path, "computed claim requires a value and a valid calculation")
            elif self.values[ident] != self.results[ref]:
                self.error(path, "published claim value/unit disagrees with calculated result")

    def decisions_check(self, decisions, claims, calculations):
        covered = set()
        for ident, decision in decisions.items():
            path = "decisions." + ident
            self.text(decision, "question", path)
            when = self.text(decision, "when", path)
            action = self.text(decision, "action", path)
            refs = self.refs(decision, "claim_ids", path, claims)
            covered.update(refs)
            for ref in refs:
                self.require_critical(ref, claims, path + ".claim_ids")
            for i, exception in enumerate(self.array(decision, "exceptions", path, 1)):
                where = f"{path}.exceptions[{i}]"
                if not isinstance(exception, dict):
                    self.error(where, "must be an object")
                    continue
                condition = self.text(exception, "condition", where)
                alternative = self.text(exception, "action", where)
                if condition and normalized(condition) == normalized(when):
                    self.error(where + ".condition", "must name a changed condition, not repeat the default")
                if alternative and normalized(alternative) == normalized(action):
                    self.error(where + ".action", "must give an alternative action, not repeat the default")
                for ref in self.refs(exception, "claim_ids", where, claims):
                    covered.add(ref)
                    self.require_critical(ref, claims, where + ".claim_ids")
            if "comparison" not in decision:
                continue
            comparison = self.mapping(decision, "comparison", path)
            self.text(comparison, "basis", path + ".comparison")
            results = []
            for i, option in enumerate(self.array(comparison, "options", path + ".comparison", 2)):
                where = f"{path}.comparison.options[{i}]"
                if not isinstance(option, dict):
                    self.error(where, "must be an object")
                    continue
                self.text(option, "label", where)
                ref = option.get("calculation_id")
                if not isinstance(ref, str) or ref not in calculations:
                    self.error(where + ".calculation_id", f"unknown reference {ref!r}")
                elif ref not in self.results:
                    self.error(where + ".calculation_id", "comparison requires a valid calculation")
                else:
                    results.append(self.results[ref])
                    terms = calculations[ref].get("inputs", [])
                    for term in terms if isinstance(terms, list) else []:
                        if isinstance(term, dict) and isinstance(term.get("claim_id"), str) and term["claim_id"] not in refs:
                            self.error(where, f"calculation input {term['claim_id']} is missing from decision claim_ids")
            if results and any(unit != results[0][1] for _, unit in results[1:]):
                self.error(path + ".comparison", "options use incompatible result units")
        return covered

    def sheet_check(self, claims):
        sheet = self.mapping(self.data, "field_sheet", "evidence")
        checked = self.day(sheet, "checked_at", "field_sheet")
        refs = self.refs(sheet, "claim_ids", "field_sheet", claims, 1)
        self.counts["field_sheet_claims"] = len(refs)
        if checked and self.release and (self.release - checked).days > FRESHNESS_DAYS["changeable"]:
            self.error("field_sheet.checked_at", "sheet has not been checked within 90 days of release")
        for ref in refs:
            self.require_critical(ref, claims, "field_sheet.claim_ids")
            display = claims[ref].get("display")
            if not isinstance(display, dict) or not isinstance(display.get("sheet"), str) or not display["sheet"].strip():
                self.error("field_sheet.claim_ids", f"{ref} has no canonical sheet value/status snippet")
            as_of = self.claim_dates.get(ref)
            if checked and as_of and as_of > checked:
                self.error("field_sheet.checked_at", f"precedes the check of listed claim {ref}")
        for ident, claim in claims.items():
            if claim.get("critical") is True and claim.get("volatility") == "changeable" and ident not in refs:
                self.error("field_sheet.claim_ids", f"missing critical changeable claim {ident}")
        return set(refs)

    def conflicts_check(self, conflicts, claims, sources):
        for ident, conflict in conflicts.items():
            path = "conflicts." + ident
            self.refs(conflict, "claim_ids", path, claims)
            self.refs(conflict, "source_ids", path, sources, 2)
            status = self.enum(conflict, "status", path, {"resolved", "unresolved"})
            if status != "resolved":
                self.error(path + ".status", "declared source conflict remains unresolved for publication")
            else:
                self.text(conflict, "resolution", path)
                self.day(conflict, "resolved_at", path)

    def run(self):
        self.text(self.data, "project", "evidence")
        self.release = self.day(self.data, "release_date", "evidence", future=True)
        sources = self.index("sources", 1)
        claims = self.index("claims", 1)
        decisions = self.index("decisions", 1)
        calculations = self.index("calculations")
        conflicts = self.index("conflicts")
        self.counts["critical_claims"] = sum(c.get("critical") is True for c in claims.values())
        if not self.counts["critical_claims"]:
            self.error("claims", "at least one decisive claim must be explicitly critical")
        self.sources_check(sources)
        self.claims_check(claims, sources)
        with localcontext() as ctx:
            ctx.prec = 160
            try:
                self.calculations_check(calculations, claims)
            except DecimalException as exc:
                self.error("calculations", "Decimal calculation failed: " + type(exc).__name__)
        covered = self.decisions_check(decisions, claims, calculations)
        covered.update(self.sheet_check(claims))
        for ident, claim in claims.items():
            if claim.get("critical") is True and ident not in covered:
                self.error("claims." + ident, "critical claim is not covered by any decision or Field Sheet")
        self.conflicts_check(conflicts, claims, sources)
        return {"gate": "evidence", "status": "FAIL" if self.errors else "PASS", "errors": self.errors, "checked": self.counts,
                "limits": "Checks declared provenance, dates, coverage and arithmetic only; does not verify source truth, omitted claims, editorial quality or final artifacts."}


def audit_build(build_dir):
    path = Path(build_dir) / "evidence.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object, parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise ValueError("evidence.json must contain an object")
        if type(data.get("schema_version")) is not int or data["schema_version"] != SCHEMA_VERSION:
            raise ValueError("missing or unsupported schema_version; expected integer 1")
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        return {"gate": "evidence", "status": "BLOCKED", "errors": [f"{path}: {exc}"], "checked": {}}, 2
    report = Auditor(build_dir, data).run()
    return report, 1 if report["errors"] else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)
    report, code = audit_build(args.build_dir)
    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("EVIDENCE " + report["status"])
        if report["checked"]:
            print("Checked: " + ", ".join(f"{k}={v}" for k, v in report["checked"].items()))
        for error in report["errors"]:
            print("- " + error)
        if "limits" in report:
            print(report["limits"])
    return code


if __name__ == "__main__":
    sys.exit(main())
