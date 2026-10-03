"""Regression corpus for supported context-bound checks, not semantic review."""

import hashlib
import json
from pathlib import Path
import sys
import unittest
from typing import Any

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import Obligation, resolve_context  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.check_context_extended import ADAPTERS  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402


def sources() -> list[dict[str, Any]]:
    entries = json.loads((TOOL / "validate_atoms_workers/context_authority.json").read_text())[
        "sources"
    ]
    result = []
    for identifier, row in entries.items():
        path = TOOL / "tests/fixtures/context_authority" / (identifier + ".md")
        text = path.read_text()
        assert hashlib.sha256(text.encode()).hexdigest() == row["sha256"]
        result.append(
            dict(
                binding=dict(
                    atom_id=identifier, path=str(path), version=row["version"], sha256=row["sha256"]
                ),
                text=text,
                metadata=parse_carrier(text.encode(), path).metadata,
            )
        )
    return result


def check(code: str, metadata: dict[str, Any], **inputs: Any) -> Check:
    inputs.setdefault("reference_complete", True)
    value = Check(
        Obligation(code, [], True, "fixture"),
        resolve_context([]),
        dict(sources=sources(), **inputs),
    )
    ADAPTERS[code](metadata, "", value)
    return value


class ContextChecks(unittest.TestCase):
    def test_retry_accepts_zero_and_rejects_negative_boolean(self) -> None:
        for value, errors in ((0, 0), (3, 0), (-1, 1), (True, 1), ("3", 1)):
            result = check(
                "plan.retry_domain",
                dict(content_role="Plan", type="Plan", implementation_retry_limit=value),
            )
            self.assertEqual(len(result.findings), errors)
            self.assertFalse(result.gaps)

    def test_retry_absence_does_not_insert_default(self) -> None:
        metadata = dict(content_role="Plan", type="Plan")
        result = check("plan.retry_domain", metadata)
        self.assertFalse(result.findings + result.gaps)
        self.assertNotIn("implementation_retry_limit", metadata)

    def test_confidence_local_override_zero_is_present(self) -> None:
        result = check(
            "plan.override_selection",
            dict(content_role="Plan", type="Plan", autonomous_confidence_threshold=0),
        )
        self.assertFalse(result.findings + result.gaps)

    def test_invalid_confidence_does_not_fall_through(self) -> None:
        for value in (-1, 101, True, "95"):
            result = check(
                "plan.override_selection",
                dict(content_role="Plan", type="Plan", autonomous_confidence_threshold=value),
            )
            self.assertTrue(result.findings)

    def test_confidence_walks_explicit_plan_relations_not_folders(self) -> None:
        parent = dict(
            atom_id="P-2",
            version=2,
            status="Active",
            content_role="Plan",
            type="Plan",
            autonomous_confidence_threshold=98,
        )
        result = check(
            "plan.override_selection",
            dict(
                atom_id="P-1",
                content_role="Plan",
                type="Plan",
                relations={"is_decomposition_of": ["P-2"]},
            ),
            references=[dict(metadata=parent, path=Path("/references/parent.md"))],
        )
        self.assertFalse(result.findings + result.gaps)

    def test_ambiguous_parent_is_not_selected_by_highest_version(self) -> None:
        parents = [
            dict(
                metadata=dict(
                    atom_id="P-2",
                    version=version,
                    status="Active",
                    content_role="Plan",
                    type="Plan",
                    autonomous_confidence_threshold=98,
                )
            )
            for version in (1, 2)
        ]
        result = check(
            "plan.override_selection",
            dict(content_role="Plan", type="Plan", relations={"is_decomposition_of": ["P-2"]}),
            references=parents,
        )
        self.assertTrue(result.gaps)

    def test_missing_settings_context_is_not_success(self) -> None:
        result = check("plan.override_selection", dict(content_role="Plan", type="Plan"))
        self.assertTrue(result.gaps)

    def test_projection_without_runtime_is_not_success(self) -> None:
        result = check("projection.fidelity", {"projection": {"source_carrier_path": "source.md"}})
        self.assertTrue(result.gaps)

    def test_nonprojection_is_not_applicable(self) -> None:
        result = check("projection.fidelity", {})
        self.assertFalse(result.applicable)
        self.assertFalse(result.findings + result.gaps)

    def test_incomplete_references_cannot_certify_parent_override(self) -> None:
        result = check(
            "plan.override_selection",
            dict(content_role="Plan", type="Plan", relations={"is_decomposition_of": ["P-2"]}),
            reference_complete=False,
            references=[
                dict(
                    metadata=dict(
                        atom_id="P-2",
                        content_role="Plan",
                        type="Plan",
                        autonomous_confidence_threshold=98,
                    )
                )
            ],
        )
        self.assertTrue(result.gaps)

    def test_cycle_without_override_is_detected(self) -> None:
        child = dict(
            atom_id="P-1",
            content_role="Plan",
            type="Plan",
            relations={"is_decomposition_of": ["P-2"]},
        )
        parent = dict(
            atom_id="P-2",
            content_role="Plan",
            type="Plan",
            relations={"is_decomposition_of": ["P-1"]},
        )
        result = check(
            "plan.override_selection",
            child,
            references=[dict(metadata=child), dict(metadata=parent)],
        )
        self.assertTrue(any(item["code"] == "RELATION_CYCLE" for item in result.findings))

    def test_changed_support_source_never_runs_retry_predicate(self) -> None:
        rows = sources()
        next(row for row in rows if row["binding"]["atom_id"] == "CA-R-1488")["text"] += "changed"
        value = Check(
            Obligation("plan.retry_domain", [], True, "fixture"),
            resolve_context([]),
            dict(sources=rows),
        )
        ADAPTERS["plan.retry_domain"](
            dict(content_role="Plan", type="Plan", implementation_retry_limit=-1), "", value
        )
        self.assertTrue(value.gaps)
        self.assertFalse(value.findings)


if __name__ == "__main__":
    unittest.main()
