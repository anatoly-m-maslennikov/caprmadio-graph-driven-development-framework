"""Execute the report admission boundary against adversarial reviewer responses."""
import copy
import unittest

from test_split_evaluation import RULE_TEXT, context, contract, gap, part, source


class StrictEvidence(unittest.TestCase):
    def test_rejects_null_blank_or_untyped_evidence(self):
        for evidence in ([None], [" "], [{}], [False]):
            response = part("cce")
            response["checks"][0]["evidence"] = evidence
            with self.subTest(evidence=evidence), self.assertRaises(ValueError):
                contract.validate_part(response, context=context())

    def test_threshold_comes_from_caller_not_response(self):
        response = part("cce")
        response["confidence_threshold"] = 0.1
        response["checks"][0].update(status="failed", findings=[{
            "kind": "violation", "location": "Claim", "excerpt": "Atom",
            "reason": "test violation", "proposed_fix": "test repair", "confidence": 0.98}])
        response["result"] = "failed"
        with self.assertRaisesRegex(ValueError, "threshold"):
            contract.validate_part(response, context=context())
        response["checks"][0]["findings"][0]["confidence"] = 0.99
        contract.validate_part(response, context=context())

    def test_unresolved_subject_mapping_cannot_hide_under_alignment(self):
        response = part("coherence")
        response["checks"][6]["status"] = "blocked"
        response.update(result="blocked", coverage_gaps=[{
            "check_id": "subjects", "reason": "Ambiguous Entity mapping"}])
        with self.assertRaisesRegex(ValueError, "gap"):
            contract.validate_part(response, context=context())

    def test_subject_quotes_and_definitions_are_source_bound(self):
        for field, bad in (("excerpt", "invented phrase"), ("definitions", [])):
            response = part("coherence")
            response["checks"][0]["subject_inventory"]["mentions"][0][field] = bad
            with self.subTest(field=field), self.assertRaises(ValueError):
                contract.validate_part(response, context=context())

    def test_ambiguous_subject_mapping_requires_its_own_gap(self):
        response = part("coherence")
        row = response["checks"][0]
        row["subject_inventory"]["mentions"][0].update(
            resolution="unresolved", entity=None, definitions=[])
        with self.assertRaises(ValueError):
            contract.validate_part(response, context=context())
        row["status"] = "blocked"
        row['subject_inventory']['complete'] = False
        response.update(result="blocked", coverage_gaps=[gap('subjects', 'Atom referent unresolved')])
        contract.validate_part(response, context=context())

    def test_inherited_obligation_prevents_false_local_omission(self):
        response = part("cce")
        row = response["checks"][0]
        resolution = {
            "id": "evidence-disposition", "state": "inherited", "local_required": False,
            "reason": "The bound profile supplies this result for the selected Type.",
            "support": [{"authority": "MOCK-R-002@1", "excerpt": "unavailable evidence blocks"}],
        }
        row["obligation_resolutions"] = [resolution]
        contract.validate_part(response, context=context())
        row.update(status="failed", findings=[{
            "kind": "omission", "obligation_id": "evidence-disposition",
            "location": "Claim", "excerpt": "absent local unavailable branch",
            "reason": "missing result", "proposed_fix": "repeat inherited result", "confidence": 1.0}])
        response["result"] = "failed"
        with self.assertRaisesRegex(ValueError, "omission"):
            contract.validate_part(response, context=context())
        resolution.update(state="missing", local_required=True)
        contract.validate_part(response, context=context())

    def test_unresolved_obligation_blocks_even_without_finding(self):
        response = part("cce")
        row = response["checks"][0]
        row["obligation_resolutions"] = [{
            "id": "result-profile", "state": "unresolved", "local_required": None,
            "reason": "Inherited applicability is unknown", "support": []}]
        with self.assertRaises(ValueError):
            contract.validate_part(response, context=context())
        row["status"] = "blocked"
        response.update(result="blocked", coverage_gaps=[gap('cce', 'Inherited applicability unknown')])
        contract.validate_part(response, context=context())

    def test_legacy_and_forged_authority_are_rejected_without_rewriting(self):
        for field, value in (("contract_version", 1), ("authority_sources", [])):
            response = part("cce")
            response[field] = value
            before = copy.deepcopy(response)
            with self.assertRaises(ValueError):
                contract.validate_part(response, context=context())
            self.assertEqual(response, before)

    def test_context_binds_threshold_and_source_bytes(self):
        for threshold in (None, True, float("nan"), float("inf"), -0.1, 1.1):
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                contract.ReviewContext({"confidence_threshold": threshold, "sources": []})
        record = source("rule.md", "MOCK-R-002", RULE_TEXT)
        record["text"] += " changed after binding"
        with self.assertRaisesRegex(ValueError, "binding"):
            contract.ReviewContext({"confidence_threshold": 0.99, "sources": [record]})

    def test_empty_inventory_cannot_support_subject_failure_or_pass(self):
        response = part("coherence")
        row = response["checks"][0]
        row["subject_inventory"]["mentions"] = []
        with self.assertRaises(ValueError):
            contract.validate_part(response, context=context())
        row.update(status="failed", findings=[{
            "kind": "violation", "location": "Markdown", "excerpt": "No Entity mentions",
            "reason": "Claim does not concern GOVERNS", "proposed_fix": "Review Claim", "confidence": 1.0}])
        response["result"] = "failed"
        with self.assertRaisesRegex(ValueError, 'resolved Entity'):
            contract.validate_part(response, context=context())

    def test_frontmatter_is_not_markdown_mention_evidence(self):
        raw = '---\nsubjects:\n  governs: Hidden Entity\n---\n# Summary\nAtom rule\n'
        candidate = source("mock.md", "MOCK-R-001", raw)
        bound_context = contract.ReviewContext({"confidence_threshold": 0.99, "sources": [
            candidate, source("rule.md", "MOCK-R-002", RULE_TEXT)]})
        response = part("coherence")
        response.update(source=candidate["binding"], context_sha256=bound_context.sha256)
        from context_builder import body_sections
        response['checks'][0]['subject_inventory']['sections_reviewed'] = body_sections(raw)
        response["checks"][0]["subject_inventory"]["mentions"][0]["excerpt"] = "Hidden Entity"
        with self.assertRaisesRegex(ValueError, "Markdown"):
            contract.validate_part(response, context=bound_context)

    def test_inherited_satisfaction_never_waives_mandatory_local_fields(self):
        response = part("properties")
        response["checks"][0]["obligation_resolutions"] = [{
            "id": "scope-heading", "state": "inherited", "local_required": True,
            "reason": "Heading exists in another Atom",
            "support": [{"authority": "MOCK-R-002@1", "excerpt": "Required Scope heading."}]}]
        with self.assertRaisesRegex(ValueError, "mandatory local"):
            contract.validate_part(response, context=context())


if __name__ == "__main__":
    unittest.main()
