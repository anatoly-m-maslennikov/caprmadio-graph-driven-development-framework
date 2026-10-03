"""Batch admission may aggregate only raw, current contract evaluations."""
from pathlib import Path
import hashlib
import sys
import unittest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import batch_admission  # noqa: E402
from test_split_evaluation import (GROUPS, SOURCE_TEXT, context, part, source)  # noqa: E402
from test_subject_accounting import response as subject_response  # noqa: E402
from test_positive_observations import context5, response as contract5_part  # noqa: E402
from test_local_review import context6, part6, packet6, contract  # noqa: E402


def candidate():
    return source("mock.md", "MOCK-R-001", SOURCE_TEXT)["binding"]


def raw_parts():
    return {"mock.md": [part(group) for group in GROUPS]}


def raw_contract5_parts():
    return {"mock.md": [contract5_part(group) for group in GROUPS]}


def parts_for(binding):
    reports = [part(group) for group in GROUPS]
    for report in reports:
        report["source"] = binding
    return reports


class BatchAdmissionTests(unittest.TestCase):
    def admit(self, parts=None, candidates=None, review_context=None, **kwargs):
        return batch_admission.admit_batch(
            candidates or [candidate()], parts if parts is not None else raw_parts(),
            review_context or context(), **kwargs)

    def test_rejects_a_fresh_review_pass_that_is_not_a_contract_report(self):
        result = self.admit({"mock.md": [{"result": "passed"}] * len(GROUPS)})
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("contract_version", result["reasons"][0])

    def test_rejects_complete_inventory_that_omits_a_declared_dependency(self):
        coherence, review_context = subject_response(dependencies=("Hidden",))
        parts = [part(group) for group in GROUPS if group != "coherence"] + [coherence]
        for report in parts:
            report.update(source=coherence["source"], context_sha256=review_context.sha256)
        result = self.admit({"mock.md": parts}, candidates=[coherence["source"]],
                            review_context=review_context)
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("unaccounted declared", result["reasons"][0])

    def test_rejects_stale_current_source_and_context_bindings(self):
        stale_bytes = self.admit(current_source_texts={"mock.md": SOURCE_TEXT + "changed"})
        self.assertEqual(stale_bytes["admission"], "rejected")
        self.assertIn("current source bytes", stale_bytes["reasons"][0])

        parts = raw_parts()
        parts["mock.md"][0]["context_sha256"] = "d" * 64
        stale_context = self.admit(parts)
        self.assertEqual(stale_context["admission"], "rejected")
        self.assertIn("caller context", stale_context["reasons"][0])

    def test_rejects_stale_caller_prompt_bytes(self):
        texts = {group: group for group in GROUPS}
        bindings = {group: {"path": group + ".prompt.md",
                            "sha256": hashlib.sha256(text.encode()).hexdigest()}
                    for group, text in texts.items()}
        parts = raw_parts()
        for report in parts["mock.md"]:
            report["prompt_sha256"] = bindings[report["evaluator"]]["sha256"]
        texts["cce"] = "changed prompt bytes"
        result = self.admit(parts, prompt_bindings=bindings, prompt_texts=texts)
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("prompt bytes", result["reasons"][0])

    def test_rejects_a_missing_selected_candidate(self):
        second = source("mock-0.md", "MOCK-R-001", SOURCE_TEXT)["binding"]
        result = self.admit(candidates=[candidate(), second])
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("missing candidates", result["reasons"][0])

    def test_rejects_valid_report_bundles_swapped_between_selected_paths(self):
        first, second = candidate(), source("mock-0.md", "MOCK-R-001", SOURCE_TEXT)["binding"]
        result = self.admit({first["path"]: parts_for(second),
                             second["path"]: parts_for(first)}, candidates=[first, second])
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("does not match its selected candidate", result["reasons"][0])

    def test_freshness_map_must_cover_every_selected_candidate_exactly(self):
        first, second = candidate(), source("mock-0.md", "MOCK-R-001", SOURCE_TEXT)["binding"]
        reports = {first["path"]: parts_for(first), second["path"]: parts_for(second)}
        for supplied in ({first["path"]: SOURCE_TEXT}, {}):
            with self.subTest(supplied=supplied):
                result = self.admit(reports, candidates=[first, second], current_source_texts=supplied)
                self.assertEqual(result["admission"], "rejected")
                self.assertIn("exactly every selected candidate", result["reasons"][0])

    def test_keeps_a_valid_complete_failed_evaluation_distinct_from_rejection(self):
        parts = raw_contract5_parts()
        failure = {
            "kind": "violation", "location": "body:5:## Claim",
            "excerpt": "Atom must comply.", "reason": "Synthetic known defect.",
            "proposed_fix": "Apply the bounded correction.", "confidence": 0.99,
        }
        parts["mock.md"][0]["checks"][0].update(status="failed", findings=[failure])
        parts["mock.md"][0]["result"] = "failed"
        result = self.admit(parts, review_context=context5())
        self.assertEqual(result["admission"], "failed")
        self.assertEqual(result["summary"]["atoms"], 1)
        self.assertFalse(result["source_repair_authorized"])

    def test_accepts_only_an_exact_complete_all_passed_batch(self):
        result = self.admit(raw_contract5_parts(), review_context=context5())
        self.assertEqual(result["admission"], "accepted")
        self.assertEqual(result["summary"]["fully_passed_atoms"], 1)
        self.assertFalse(result["source_repair_authorized"])

    def test_rejects_an_unexplained_caller_pass_count(self):
        claimed = {"atoms": 1, "fully_passed_atoms": 2}
        result = self.admit(claimed_summary=claimed)
        self.assertEqual(result["admission"], "rejected")
        self.assertIn("summary", result["reasons"][0])

    def test_accepts_six_check_local_profile_without_legacy_checks(self):
        parts = {"mock.md": [part6(group) for group in contract.LOCAL_GROUPS]}
        result = self.admit(parts, review_context=context6())
        self.assertEqual(result["admission"], "accepted", result["reasons"])
        self.assertEqual(result["summary"]["review_profile"], "atom_local")
        self.assertEqual(set(result["summary"]["check_counts"]),
                         {"cce", "properties", "scope", "claim", "details", "summary"})
        self.assertEqual(result["summary"]["fully_passed_atoms"], 1)

    def test_combines_independent_local_contexts(self):
        first = candidate()
        packet = packet6()
        second_source = source("second.md", "MOCK-R-001", SOURCE_TEXT)
        packet["sources"][0] = second_source
        packet["candidate_bindings"] = [second_source["binding"]]
        second_context = contract.ReviewContext(packet)
        second_parts = [part6(group) for group in contract.LOCAL_GROUPS]
        for report in second_parts:
            report.update(source=second_source["binding"], context_sha256=second_context.sha256)
        result = self.admit(
            {"mock.md": [part6(group) for group in contract.LOCAL_GROUPS],
             "second.md": second_parts},
            candidates=[first, second_source["binding"]],
            review_context={"mock.md": context6(), "second.md": second_context})
        self.assertEqual(result["admission"], "accepted", result["reasons"])
        self.assertEqual(result["summary"]["fully_passed_atoms"], 2)
        self.assertTrue(all(row["passed"] == 2
                            for row in result["summary"]["check_counts"].values()))

    def test_retains_local_failure_and_gap_without_adding_excluded_checks(self):
        parts = [part6(group) for group in contract.LOCAL_GROUPS]
        parts[0]["checks"][0].update(status="failed", findings=[{
            "kind": "violation", "location": "body:5:## Claim", "excerpt": "must",
            "reason": "Synthetic rendering defect", "proposed_fix": "Bold must",
            "confidence": .99}])
        parts[0]["result"] = "failed"
        parts[1]["checks"][0]["status"] = "blocked"
        parts[1].update(result="blocked", coverage_gaps=[{
            "check_id": "properties", "kind": "reviewer_incomplete", "reason": "Parser not run"}])
        result = self.admit({"mock.md": parts}, review_context=context6())
        self.assertEqual(result["admission"], "failed", result["reasons"])
        summary = result["summary"]
        self.assertEqual(summary["fully_passed_atoms"], 0)
        self.assertEqual(summary["atoms_with_confirmed_findings"], 1)
        self.assertEqual(summary["atoms_with_coverage_gaps"], 1)
        self.assertEqual(summary["check_counts"]["cce"]["findings"], 1)
        self.assertEqual(summary["check_counts"]["properties"]["blocked"], 1)
        self.assertEqual(len(summary["check_counts"]), 6)

    def test_rejects_mixed_review_profiles_instead_of_merging_coverage(self):
        local = self.admit({"mock.md": [part6(group) for group in contract.LOCAL_GROUPS]},
                           review_context=context6())["summary"]
        legacy = self.admit(raw_contract5_parts(), review_context=context5())["summary"]
        with self.assertRaisesRegex(ValueError, "same review profile"):
            batch_admission._combine_summaries([local, legacy])


if __name__ == "__main__":
    unittest.main()
