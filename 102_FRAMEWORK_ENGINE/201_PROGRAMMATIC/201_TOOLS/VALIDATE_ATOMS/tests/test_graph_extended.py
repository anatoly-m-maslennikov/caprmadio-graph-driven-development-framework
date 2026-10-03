"""Graph adapter regressions from the current, pinned source contracts."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import unittest
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import AuthorityContext, Obligation, Record  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.check_graph_extended import ADAPTERS  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402


@lru_cache(maxsize=1)
def authorities() -> list[Record]:
    manifest = json.loads((TOOL / "validate_atoms_workers/graph_authority.json").read_text())
    result = []
    for atom_id, pin in manifest["sources"].items():
        path = TOOL / "tests/fixtures/extended_authority" / (atom_id + ".md")
        text = path.read_text()
        if hashlib.sha256(text.encode()).hexdigest() != pin["sha256"]:
            raise AssertionError("Authority fixture no longer matches its reviewed pin: " + atom_id)
        result.append(
            {
                "binding": {
                    "atom_id": atom_id,
                    "version": pin["version"],
                    "sha256": hashlib.sha256(text.encode()).hexdigest(),
                    "path": str(path),
                },
                "text": text,
                "metadata": yaml.safe_load(text.split("---", 2)[1]),
            }
        )
    return result


def atom(
    atom_id: str = "X-P-1", role: str = "Plan", status: str = "Active", **extra: Any
) -> Record:
    return {
        "atom_id": atom_id,
        "version": 1,
        "content_role": role,
        "type": "Plan" if role == "Plan" else "Requirement",
        "status": status,
        "current_scope_unit": "EXAMPLE",
        **extra,
    }


def reference(metadata: Record, path: str | None = None) -> Record:
    return {"metadata": metadata, "path": Path(path or "/inventory/" + metadata["atom_id"] + ".md")}


def check(
    code: str,
    metadata: Record,
    refs: list[Record] | tuple[()] = (),
    *,
    complete: bool = True,
    sources: list[Record] | None = None,
    path: str = "/inventory/source.md",
) -> Check:
    context = AuthorityContext(
        [],
        0,
        0,
        0,
        [],
        (),
        {"domain.status.plan": ("Active", "Backlog", "Done", "Canceled", "Archived")},
        False,
    )
    item = Check(Obligation(code, [], True, "fixture"), context)
    item.inputs = {
        "sources": authorities() if sources is None else sources,
        "references": list(refs),
        "reference_complete": complete,
        "path": Path(path),
    }
    ADAPTERS[code](metadata, "", item)
    return item


class GraphExtendedTests(unittest.TestCase):
    def test_unbound_sort_algorithm_is_a_gap_in_both_orders(self) -> None:
        for targets in (["X-R-2", "X-R-1"], ["X-R-1", "X-R-2"]):
            with self.subTest(targets=targets):
                result = check(
                    "relations.resolution",
                    atom("X-M-1", "Method", relations={"method_for": targets}),
                    [reference(atom(target, "Requirement")) for target in targets],
                )
                self.assertFalse(result.findings)
                self.assertTrue(any("ordering" in gap["reason"] for gap in result.gaps))

    def test_method_target_resolves_with_exact_role(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            [reference(atom("X-R-1", "Requirement"))],
        )
        self.assertFalse(result.findings + result.gaps)

    def test_ordering_gap_does_not_hide_wrong_target_role(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1", "X-E-1"]}),
            [reference(atom("X-R-1", "Requirement")), reference(atom("X-E-1", "Evaluation"))],
        )
        self.assertTrue(any("ordering" in gap["reason"] for gap in result.gaps))
        self.assertTrue(any("inadmissible Content Role" in row["reason"] for row in result.findings))

    def test_duplicate_targets_remain_a_defect_not_an_ordering_gap(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1", "X-R-1"]}),
            [reference(atom("X-R-1", "Requirement"))],
        )
        self.assertTrue(any("unique" in row["reason"] for row in result.findings))
        self.assertFalse(result.gaps)

    def test_method_target_wrong_role_fails(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-E-1"]}),
            [reference(atom("X-E-1", "Evaluation"))],
        )
        self.assertTrue(result.findings)
        self.assertFalse(result.gaps)

    def test_active_rmed_relation_to_inactive_rmed_fails(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            [reference(atom("X-R-1", "Requirement", "Archived"))],
        )
        self.assertTrue(any("Active" in d["reason"] for d in result.findings))

    def test_archived_rmed_owner_does_not_impose_active_target(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", "Archived", relations={"method_for": ["X-R-1"]}),
            [reference(atom("X-R-1", "Requirement", "Archived"))],
        )
        self.assertFalse(result.findings + result.gaps)

    def test_missing_and_ambiguous_target_stay_gaps(self) -> None:
        metadata = atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]})
        self.assertTrue(check("relations.resolution", metadata).gaps)
        refs = [
            reference(atom("X-R-1", "Requirement"), "/inventory/a.md"),
            reference(atom("X-R-1", "Requirement", version=2), "/inventory/b.md"),
        ]
        result = check("relations.resolution", metadata, refs)
        self.assertTrue(result.gaps)
        self.assertFalse(result.findings)

    def test_incomplete_inventory_cannot_prove_unique_reference(self) -> None:
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            [reference(atom("X-R-1", "Requirement"))],
            complete=False,
        )
        self.assertTrue(result.gaps)

    def test_reference_without_revision_identity_remains_unresolved(self) -> None:
        target = atom("X-R-1", "Requirement")
        target.pop("version")
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            [reference(target)],
        )
        self.assertTrue(result.gaps)
        self.assertFalse(result.findings)

    def test_active_rmed_target_selection_retains_archived_history(self) -> None:
        metadata = atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]})
        refs = [
            reference(atom("X-R-1", "Requirement", "Archived", version=1), "/inventory/old.md"),
            reference(atom("X-R-1", "Requirement", "Active", version=2), "/inventory/current.md"),
        ]
        result = check("relations.resolution", metadata, refs)
        self.assertFalse(result.findings + result.gaps)

    def test_two_active_rmed_revisions_remain_ambiguous(self) -> None:
        metadata = atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]})
        refs = [
            reference(atom("X-R-1", "Requirement", version=1), "/inventory/first.md"),
            reference(atom("X-R-1", "Requirement", version=2), "/inventory/second.md"),
        ]
        self.assertTrue(check("relations.resolution", metadata, refs).gaps)

    def test_faithful_projection_is_not_another_target_identity(self) -> None:
        target = atom("X-R-1", "Requirement")
        raw = "---\n" + yaml.safe_dump(target, sort_keys=False) + "---\n# Summary\nTarget\n"
        projection = raw.replace(
            "---\n", "---\nprojection:\n  source_carrier_path: original.md\n", 1
        )
        refs: list[Record] = []
        for name, text in (("original.md", raw), ("copy.md", projection)):
            path = Path("/inventory") / name
            parsed = parse_carrier(text.encode(), path)
            refs.append({"path": path, "metadata": parsed.metadata, "parsed": parsed})
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            refs,
        )
        self.assertFalse(result.findings + result.gaps)
        refs[-1]["parsed"] = parse_carrier((projection + "changed\n").encode(), refs[-1]["path"])
        changed = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-1"]}),
            refs,
        )
        self.assertTrue(changed.gaps)

    def test_unreviewed_relation_kind_is_not_assumed_valid(self) -> None:
        result = check(
            "relations.resolution",
            atom(relations={"invented": ["X-P-2"]}),
            [reference(atom("X-P-2"))],
        )
        self.assertTrue(result.gaps)

    def test_inverse_is_rejected_and_unbound_direct_order_is_a_gap(self) -> None:
        inverse = check(
            "relations.resolution",
            atom(relations={"required_by": ["X-P-2"]}),
            [reference(atom("X-P-2"))],
        )
        self.assertTrue(inverse.findings)
        direct = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-R-2", "X-R-1"]}),
            [reference(atom("X-R-1", "Requirement")), reference(atom("X-R-2", "Requirement"))],
        )
        self.assertFalse(direct.findings)
        self.assertTrue(any("ordering" in d["reason"] for d in direct.gaps))

    def test_changed_dependency_pin_does_not_execute_its_rule(self) -> None:
        sources = copy.deepcopy(authorities())
        dependency = next(s for s in sources if s["binding"]["atom_id"] == "CA-R-1017")
        dependency["text"] += "\nchanged\n"
        result = check(
            "relations.resolution",
            atom("X-M-1", "Method", relations={"method_for": ["X-E-1"]}),
            [reference(atom("X-E-1", "Evaluation"))],
            sources=sources,
        )
        self.assertTrue(result.gaps)
        self.assertFalse(result.findings)

    def test_subject_full_path_resolves_from_governed_declarations(self) -> None:
        refs = [
            reference(atom("X-R-1", "Requirement", subjects={"governs": "Widget/Color"})),
            reference(atom("X-R-2", "Requirement", subjects={"governs": "Widget/Color"})),
        ]
        result = check("subjects.resolution", atom(subjects={"governs": "Widget/Color"}), refs)
        self.assertFalse(result.findings + result.gaps)

    def test_subject_dependency_mention_does_not_declare_entity(self) -> None:
        refs = [
            reference(
                atom(
                    "X-R-1",
                    "Requirement",
                    subjects={"governs": "Widget", "depends_on": ["Widget/Color"]},
                )
            )
        ]
        result = check("subjects.resolution", atom(subjects={"governs": "Widget/Color"}), refs)
        self.assertTrue(result.gaps)

    def test_subject_term_suffix_does_not_resolve_qualified_occurrence(self) -> None:
        refs = [reference(atom("X-R-1", "Requirement", subjects={"governs": "Color"}))]
        self.assertTrue(
            check("subjects.resolution", atom(subjects={"governs": "Widget/Color"}), refs).gaps
        )

    def test_modern_subject_encoding_needs_no_migration_evidence(self) -> None:
        result = check(
            "subjects.migration", atom(subjects={"governs": "Widget", "depends_on": ["Color"]})
        )
        self.assertFalse(result.findings + result.gaps)

    def test_legacy_encoding_retains_explicit_migration_gap(self) -> None:
        result = check("subjects.migration", atom(subjects={"governs": {"continuant": ["Widget"]}}))
        self.assertTrue(result.gaps)
        self.assertFalse(result.findings)

    def test_non_plan_does_not_receive_plan_graph_obligation(self) -> None:
        result = check("plan.blocking_resolution", atom("X-R-1", "Requirement"))
        self.assertFalse(result.applicable)
        self.assertFalse(result.findings + result.gaps)

    def test_plan_blocking_accepts_pending_and_historical_endpoints(self) -> None:
        for status in ("Backlog", "Done", "Canceled", "Archived"):
            result = check(
                "plan.blocking_resolution",
                atom(relations={"blocks": ["X-P-2"]}),
                [reference(atom("X-P-2", status=status))],
            )
            self.assertFalse(result.findings + result.gaps, status)

    def test_plan_target_wrong_role_and_status_are_findings(self) -> None:
        for target in (atom("X-P-2", "Requirement"), atom("X-P-2", status="Planned")):
            result = check(
                "plan.blocking_resolution",
                atom(relations={"blocks": ["X-P-2"]}),
                [reference(target)],
            )
            self.assertTrue(result.findings)

    def test_plan_decomposition_distinctness_and_single_target(self) -> None:
        self.assertTrue(
            check(
                "plan.decomposition_resolution", atom(relations={"is_decomposition_of": ["X-P-1"]})
            ).findings
        )
        result = check(
            "plan.decomposition_resolution",
            atom(relations={"is_decomposition_of": ["X-P-2", "X-P-3"]}),
            [reference(atom("X-P-2")), reference(atom("X-P-3"))],
        )
        self.assertTrue(result.findings)

    def test_plan_decomposition_cycle_is_rejected(self) -> None:
        result = check(
            "plan.decomposition_resolution",
            atom(relations={"is_decomposition_of": ["X-P-2"]}),
            [reference(atom("X-P-2", relations={"is_decomposition_of": ["X-P-1"]}))],
        )
        self.assertTrue(any("cycle" in d["reason"] for d in result.findings))

    def test_combined_completion_cycle_is_rejected(self) -> None:
        result = check(
            "plan.blocking_resolution",
            atom(relations={"blocks": ["X-P-2"]}),
            [reference(atom("X-P-2", relations={"is_decomposition_of": ["X-P-1"]}))],
        )
        self.assertTrue(any("cycle" in d["reason"] for d in result.findings))

    def test_missing_graph_node_cannot_prove_acyclicity(self) -> None:
        result = check(
            "plan.decomposition_resolution",
            atom(relations={"is_decomposition_of": ["X-P-2"]}),
            [reference(atom("X-P-2", relations={"is_decomposition_of": ["X-P-3"]}))],
        )
        self.assertTrue(result.gaps)

    def test_plan_directory_parent_must_match_declared_parent(self) -> None:
        parent = reference(atom("X-P-2"), "/inventory/hub.md")
        wrong = reference(atom("X-P-3"), "/inventory/other.md")
        result = check(
            "plan.decomposition_resolution",
            atom(relations={"is_decomposition_of": ["X-P-3"]}),
            [parent, wrong],
            path="/inventory/hub/001_backlog/child.md",
        )
        self.assertTrue(any("placement" in d["reason"] for d in result.findings))


if __name__ == "__main__":
    unittest.main()
