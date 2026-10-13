#!/usr/bin/env python3
"""Behavioral checks for audit-evidence.py; fictional data, no network or paid actions."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("audit-evidence.py")
EXAMPLE = SCRIPT.parent.parent / "assets" / "evidence-example.json"
spec = importlib.util.spec_from_file_location("dossier_evidence_audit", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvidenceBehavior(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dossier-evidence-test-")
        self.addCleanup(self.temp.cleanup)
        self.build = Path(self.temp.name)
        self.data = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def run_audit(self, data=None):
        (self.build / "evidence.json").write_text(json.dumps(self.data if data is None else data), encoding="utf-8")
        return module.audit_build(self.build)

    def fails_with(self, message):
        report, code = self.run_audit()
        self.assertEqual(code, 1, report)
        self.assertEqual(report["status"], "FAIL")
        self.assertIn(message, "\n".join(report["errors"]))

    def test_complete_comparison_and_sheet_pass(self):
        report, code = self.run_audit()
        self.assertEqual(code, 0, report)
        self.assertEqual(report["checked"]["critical_claims"], 3)
        self.assertIn("does not verify source truth", report["limits"])

    def test_absent_registry_never_passes(self):
        report, code = module.audit_build(self.build)
        self.assertEqual((report["status"], code), ("BLOCKED", 2))

    def test_corrupt_or_unsupported_registry_never_passes(self):
        for raw in ('{', '[]', '{"schema_version":2}', '{"schema_version":true}', '{"schema_version":1,"schema_version":1}', '{"schema_version":1,"bad":NaN}'):
            with self.subTest(raw=raw):
                (self.build / "evidence.json").write_text(raw, encoding="utf-8")
                report, code = module.audit_build(self.build)
                self.assertEqual((report["status"], code), ("BLOCKED", 2))

    def test_empty_and_incomplete_metadata_fail(self):
        self.data = {"schema_version": 1}
        self.fails_with("required")

    def test_self_published_corpus_cannot_verify_regulated_price(self):
        self.data["sources"][0]["kind"] = "corpus"
        self.fails_with("require a primary source")

    def test_publisher_policy_supports_own_policy_only(self):
        self.data["sources"].append({"id": "s-policy", "kind": "publisher_policy", "url": "https://example.invalid/refunds", "locator": "Publisher's own refund terms", "checked_at": "2026-04-15", "scope": "This publisher's refund policy only"})
        policy = deepcopy(self.data["claims"][0])
        policy.update(id="c-policy", topic="publisher_policy", sources=["s-policy"], text="The publisher accepts refund requests within seven days.", display={"sheet": "The publisher accepts refund requests within seven days."})
        policy.pop("value")
        self.data["claims"].append(policy)
        self.data["field_sheet"]["claim_ids"].append("c-policy")
        report, code = self.run_audit()
        self.assertEqual(code, 0, report)
        self.data["claims"][0]["sources"] = ["s-policy"]
        self.fails_with("require a primary source")

    def test_broken_reference_and_duplicate_ids_fail(self):
        self.data["claims"][0]["sources"] = ["missing-source"]
        self.fails_with("unknown reference")
        self.data["claims"].append(deepcopy(self.data["claims"][0]))
        self.fails_with("duplicate identifier")

    def test_published_price_cannot_hide_behind_check_current(self):
        self.data["claims"][0]["display"]["sheet"] = "Single fare: check current."
        self.fails_with("must show the actual declared amount")
        self.data["claims"][0].pop("value")
        self.fails_with("needs an actual amount")

    def test_decimal_strings_are_required_no_expressions(self):
        for bad in (3.25, True, "NaN", "Infinity", "3+0.25", "__import__('os').system('false')"):
            with self.subTest(value=bad):
                self.data["claims"][0]["value"]["amount"] = bad
                self.fails_with("finite decimal string")

    def test_future_checks_and_invalid_dates_fail(self):
        self.data["sources"][0]["checked_at"] = "2026-04-16"
        self.fails_with("after release_date")
        self.data["claims"][0]["as_of"] = "2026-02-30"
        self.fails_with("required ISO date")

    def test_expired_rate_and_overdue_recheck_fail(self):
        self.data["claims"][0]["valid_until"] = "2026-04-14"
        self.fails_with("has expired")
        self.data["claims"][0]["recheck_by"] = "2026-04-14"
        self.fails_with("recheck is overdue")

    def test_long_recheck_date_does_not_make_old_evidence_current(self):
        self.data["claims"][0]["recheck_by"] = "2029-04-15"
        self.fails_with("90-day ceiling")
        self.data["sources"][0]["checked_at"] = "2024-01-01"
        self.fails_with("has not been checked within 90 days")

    def test_incomplete_field_sheet_fails_even_when_book_has_text(self):
        self.data["field_sheet"]["claim_ids"].remove("c-single")
        self.fails_with("missing critical changeable claim c-single")
        self.data["field_sheet"]["claim_ids"].append("c-single")
        self.data["claims"][0]["display"].pop("sheet")
        self.fails_with("no canonical sheet")

    def test_claim_cannot_evade_release_checks_by_demotion(self):
        self.data["claims"][0]["critical"] = False
        self.fails_with("must be marked critical")

    def test_wrong_sum_and_changed_printed_result_fail(self):
        self.data["calculations"][0]["result"]["amount"] = "12.00"
        self.fails_with("arithmetic mismatch")
        self.data["calculations"][0]["result"]["amount"] = "13.00"
        self.data["claims"][2]["value"]["amount"] = "12.00"
        self.fails_with("published claim value/unit disagrees")

    def test_person_and_party_units_cannot_be_added(self):
        self.data["calculations"][0]["inputs"].append({"claim_id": "c-pass", "quantity": {"amount": "1", "unit": "1"}})
        self.fails_with("incompatible units")

    def test_difference_is_ordered_and_rejects_one_operand(self):
        self.data["calculations"][0].update(operation="difference", inputs=[{"claim_id": "c-single", "quantity": {"amount": "4", "unit": "journey"}}, {"claim_id": "c-pass", "quantity": {"amount": "1", "unit": "day"}}], result={"amount": "3.50", "unit": "XCU"})
        self.data["claims"][2]["value"]["amount"] = "3.50"
        self.data["claims"][2]["display"]["sheet"] = "SYNTHETIC saving in this example: XCU 3.50."
        report, code = self.run_audit()
        self.assertEqual(code, 0, report)
        self.data["calculations"][0]["inputs"].pop()
        self.fails_with("exactly two inputs")

    def test_exception_must_change_action(self):
        self.data["decisions"][0]["exceptions"][0]["action"] = self.data["decisions"][0]["action"]
        self.fails_with("alternative action")

    def test_unresolved_conflict_blocks_and_qualified_safe_text_can_pass(self):
        self.data["sources"].append(dict(self.data["sources"][0], id="s-other", url="https://example.invalid/operator/notice"))
        self.data["conflicts"] = [{"id": "conflict-1", "claim_ids": ["c-single"], "source_ids": ["s-fares", "s-other"], "status": "unresolved"}]
        self.fails_with("remains unresolved")
        claim = self.data["claims"][0]
        claim.update(status="qualified", qualification="Check the operator's current purchase screen before paying.")
        claim["display"] = {k: v + " " + claim["qualification"] for k, v in claim["display"].items()}
        self.data["conflicts"][0].update(status="resolved", resolution="The disputed assertion was narrowed to a dated fare; the instruction explicitly requires checking the purchase screen and makes no claim that conflicting pages agree.", resolved_at="2026-04-15")
        report, code = self.run_audit()
        self.assertEqual(code, 0, report)
        claim["display"]["book"] = "The price is guaranteed forever."
        self.fails_with("retain the declared qualification")

    def test_survey_needs_real_method_and_retained_observation(self):
        claim = self.data["claims"][0]
        claim.update(authority="observed", topic="other")
        self.fails_with("survey")
        self.data["sources"][0].update(kind="observation", artifact="observations.txt")
        self.data["sources"][0].pop("url")
        (self.build / "observations.txt").write_text("SYNTHETIC measurement fixture", encoding="utf-8")
        claim["survey"] = {"method": "Two observed purchases recorded on the same route", "sample": "Two fictional adult journeys", "observed_from": "2026-04-15", "observed_until": "2026-04-15"}
        # Keep the second price's independent official basis, rather than relabel all evidence as observed.
        self.data["sources"].append(dict(self.data["sources"][0], id="s-official", kind="primary", url="https://example.invalid/fares"))
        self.data["sources"][-1].pop("artifact")
        self.data["claims"][1]["sources"] = ["s-official"]
        self.data["claims"][2]["sources"] = ["s-official"]
        report, code = self.run_audit()
        self.assertEqual(code, 0, report)
        self.data["sources"][0]["artifact"] = "../outside.txt"
        self.fails_with("inside BUILD_DIR")

    def test_bad_shapes_fail_instead_of_crashing(self):
        baseline = deepcopy(self.data)
        mutations = [
            lambda d: d.update(sources=[None]),
            lambda d: d["claims"][0].update(display=["bad"]),
            lambda d: d["calculations"][0].update(inputs=None),
            lambda d: d["calculations"][0].update(operation="difference", inputs=[]),
            lambda d: d["decisions"][0].update(comparison={"basis": "same day", "options": [None, {}]}),
            lambda d: d.update(field_sheet=[]),
            lambda d: d["sources"][0].update(url="https://[invalid"),
        ]
        for mutate in mutations:
            self.data = deepcopy(baseline)
            mutate(self.data)
            with self.subTest(data=self.data):
                report, code = self.run_audit()
                self.assertEqual((report["status"], code), ("FAIL", 1), report)

    def test_cli_json_and_exit_status_match_report(self):
        self.run_audit()
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.build), "--json"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)["status"], "PASS")
        (self.build / "evidence.json").unlink()
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.build), "--json"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2, run.stderr)
        self.assertEqual(json.loads(run.stdout)["status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
