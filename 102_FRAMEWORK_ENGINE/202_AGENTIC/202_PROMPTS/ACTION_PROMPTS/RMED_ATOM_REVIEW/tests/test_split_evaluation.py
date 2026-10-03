"""Contract tests for three independent evaluators, not a simulation of judgment."""
import copy
import hashlib
import importlib
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
contract = importlib.import_module("evaluation_contract")
GROUPS = contract.GROUPS
SOURCE_TEXT = ('---\nsubjects:\n  governs: Atom\n  depends_on: []\n---\n'
    '# Summary\nAtom rule\n## Scope\nAtoms\n## Claim\nAtom must comply.\n## Details\n')
RULE_TEXT = '---\nstatus: active\ncontent_role: Requirement\nsubjects:\n  governs: Atom\n---\n# Definition\n\nAtom means a governed statement. unavailable evidence blocks. Required Scope heading.'


def source(path, identifier, body):
    return {"binding": {"atom_id": identifier, "version": 1, "path": path,
                        "sha256": hashlib.sha256(body.encode()).hexdigest()}, "text": body}


def context(preflight=None):
    return contract.ReviewContext({"confidence_threshold": 0.99, 'preflight': preflight or {}, "sources": [
        source(path, "MOCK-R-001", SOURCE_TEXT) for path in
        ("mock.md", "mock-0.md", "mock-1.md", "mock-2.md")
    ] + [source("rule.md", "MOCK-R-002", RULE_TEXT)]})


def merge_evaluations(parts):
    return contract.merge_evaluations(parts, context=context())


def gap(check_id, reason):
    return {"check_id": check_id, "kind": "unresolved_interpretation", "reason": reason}


def part(group):
    result = {
        "contract_version": 4,
        "evaluator": group,
        "source": source("mock.md", "MOCK-R-001", SOURCE_TEXT)["binding"],
        "context_sha256": context().sha256,
        "authority_sources": [source("rule.md", "MOCK-R-002", RULE_TEXT)["binding"]],
        "checks": [{"id": check, "status": "passed", "evidence": ["Observed fixture value"],
                    "authority": ["MOCK-R-002@1"], "findings": [], "obligation_resolutions": []}
                   for check in GROUPS[group]],
        "coverage_gaps": [], "mechanical_evidence": [], "result": "passed",
    }
    if group == "coherence":
        from context_builder import body_sections
        result["checks"][0]["subject_inventory"] = {"complete": True, "sections_reviewed": body_sections(SOURCE_TEXT), "mentions": [{
            "location": "Claim", "excerpt": "Atom", "entity": "Atom", "resolution": "resolved", "resolution_basis": "meaning",
            "rationale": "Literal use of the bound Entity definition.",
            "definitions": [{"authority": "MOCK-R-002@1", "excerpt": "Atom means a governed statement."}]}]}
    return result


class SplitEvaluation(unittest.TestCase):
    def test_disjoint_complete_checks(self):
        flattened = [check for group in GROUPS.values() for check in group]
        self.assertEqual(len(flattened), 10)
        self.assertEqual(len(set(flattened)), 10)
        self.assertEqual(GROUPS["cce"], ("cce",))
        self.assertEqual(GROUPS["properties"], ("properties",))

    def test_merge_preserves_parts(self):
        parts = [part(group) for group in GROUPS]
        result = merge_evaluations(parts)
        self.assertEqual(result["result"], "passed")
        self.assertEqual(len(result["checks"]), 10)
        self.assertEqual(result["parts"], parts)
        result["parts"][0]["result"] = "changed"
        self.assertEqual(parts[0]["result"], "passed")

    def test_missing_duplicate_or_wrong_group_rejected(self):
        parts = [part(group) for group in GROUPS]
        for bad in (parts[:-1], parts + [parts[0]], [parts[0], parts[0], parts[2]]):
            with self.assertRaises(ValueError):
                merge_evaluations(bad)
        bad = copy.deepcopy(parts)
        bad[0]["checks"][0]["id"] = "properties"
        with self.assertRaises(ValueError):
            merge_evaluations(bad)

    def test_mixed_source_or_context_rejected(self):
        for field in ("source", "context_sha256"):
            parts = [part(group) for group in GROUPS]
            parts[1][field] = {"sha256": "d" * 64} if field == "source" else "d" * 64
            with self.assertRaises(ValueError):
                merge_evaluations(parts)

    def test_failed_does_not_erase_blocked(self):
        parts = [part(group) for group in GROUPS]
        parts[0]["checks"][0].update(status="failed", findings=[{
            "kind": "violation",
            "location": "Claim:1", "excerpt": "must", "reason": "not bold",
            "proposed_fix": "Render **must**", "confidence": 0.99}])
        parts[0]["result"] = "failed"
        parts[1]["checks"][0]["status"] = "blocked"
        parts[1]["coverage_gaps"] = [gap("properties", "Missing Operator registry")]
        parts[1]["result"] = "blocked"
        merged = merge_evaluations(parts)
        self.assertEqual(merged["result"], "failed")
        self.assertEqual(merged["coverage_gaps"], [gap("properties", "Missing Operator registry")])

    def test_missing_evidence_and_false_pass_rejected(self):
        for mutation in ("empty_evidence", "bad_result", "unreported_gap", "extra_check", "failed_no_finding"):
            parts = [part(group) for group in GROUPS]
            target = parts[0]
            if mutation == "empty_evidence":
                target["checks"][0]["evidence"] = []
            elif mutation == "bad_result":
                target["result"] = "failed"
            elif mutation == "unreported_gap":
                target["coverage_gaps"] = ["Unresolved authority"]
            elif mutation == "extra_check":
                target["checks"].append(copy.deepcopy(target["checks"][0]))
            else:
                target["checks"][0]["status"] = "failed"
                target["result"] = "failed"
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                merge_evaluations(parts)

    def test_cce_includes_operator_inventory(self):
        text = (HERE / "evaluate_cce.prompt.md").read_text()
        for token in ("must not", "otherwise", "before", "unless", "every", "all", "none", "not in", "starts with", "!=", ">="):
            self.assertIn(token, text)
        for phrase in ("lowercase", "bold inline-code", "Scope Unit", "Requirement", "Method", "Evaluation", "Delivery"):
            self.assertIn(phrase, text)

    def test_property_prompt_carries_schema_and_no_lookup_dependency(self):
        text = (HERE / "evaluate_properties.prompt.md").read_text()
        for field in ("atom_id", "version", "updated_at", "author", "current_scope_unit", "claim_target_scope_unit", "local_tier", "global_tier", "subjects", "relations"):
            self.assertIn("`" + field + "`", text)
        for prompt in HERE.glob("evaluate_*.prompt.md"):
            if prompt.name == "evaluate_atom.prompt.md":
                continue
            text = prompt.read_text()
            self.assertNotIn("Read the shared README", text)
            self.assertIn("inline", text)
            self.assertIn("blocked", text)

    def test_cce_requires_separate_surface_and_language_sweeps(self):
        # Prompt regression only: this does not simulate or prove model accuracy.
        text = (HERE / "evaluate_cce.prompt.md").read_text()
        for required in (
            "two separate sweeps", "raw Markdown delimiters",
            "**>=2**", "**`>=2`**", "sentence, bullet, and table-cell starts",
            "Rendering:", "Vocabulary:", "Profile:", "Understandability:",
            "Unfinished coverage blocks", "Never initialize a batch to passed",
            "Do not require a modal keyword", "assess actual dependencies",
        ):
            self.assertIn(required, text)

    def test_coherence_scans_entire_markdown(self):
        text = (HERE / "evaluate_coherence.prompt.md").read_text()
        self.assertIn("entire Markdown", text)
        self.assertIn("Summary, Scope, Claim, Details", text)
        self.assertIn("No subject_inventory", text)
        self.assertIn("independently", text)

    def test_blocked_without_available_authority_remains_visible(self):
        parts = [part(group) for group in GROUPS]
        parts[0]["checks"][0].update(status="blocked", authority=[], evidence=["Missing Term definitions"])
        parts[0].update(result="blocked", coverage_gaps=[gap("cce", "Missing Term definitions")])
        merged = merge_evaluations(parts)
        self.assertEqual(merged["result"], "blocked")
        self.assertEqual(merged["coverage_gaps"], [gap("cce", "Missing Term definitions")])

    def test_malformed_finding_is_not_accepted(self):
        parts = [part(group) for group in GROUPS]
        parts[0]["checks"][0].update(status="failed", findings=[{"reason": "unsupported"}])
        parts[0]["result"] = "failed"
        with self.assertRaises(ValueError):
            merge_evaluations(parts)

    def test_each_evaluator_baseline_has_fresh_bound_sources(self):
        import json
        manifest = json.loads((HERE / "source_bindings.json").read_text())
        sources = {entry["atom_id"] for entry in manifest["sources"]}
        self.assertEqual(set(manifest["evaluators"]), set(GROUPS))
        for group, identifiers in manifest["evaluators"].items():
            self.assertGreater(len(identifiers), 0)
            self.assertTrue(set(identifiers) <= sources)
            self.assertEqual(len(identifiers), len(set(identifiers)), group)


if __name__ == "__main__":
    unittest.main()
