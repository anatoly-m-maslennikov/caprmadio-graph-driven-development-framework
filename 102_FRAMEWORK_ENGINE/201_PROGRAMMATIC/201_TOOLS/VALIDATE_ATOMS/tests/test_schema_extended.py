"""Behavioral cases for source-bound structural schema checks, not Claim semantics."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path
from typing import Any

import yaml

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_fields import _common  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.check_schema_extended import ADAPTERS  # noqa: E402


def sources() -> list[dict[str, Any]]:
    entries = {}
    directories = {}
    for name in ("registry.json", "schema_authority.json"):
        group = json.loads((TOOL / "validate_atoms_workers" / name).read_text())["sources"]
        entries.update(group)
        directories.update(
            {
                atom_id: "schema_authority"
                if name == "schema_authority.json"
                else "authority_checks"
                for atom_id in group
            }
        )
    result = []
    for atom_id, entry in entries.items():
        path = TOOL / "tests/fixtures" / directories[atom_id] / (atom_id + ".md")
        text = path.read_text()
        result.append(
            {
                "binding": {
                    "atom_id": atom_id,
                    "version": entry["version"],
                    "path": str(path),
                    "sha256": hashlib.sha256(text.encode()).hexdigest(),
                },
                "text": text,
                "metadata": yaml.safe_load(text.split("---", 2)[1]),
            }
        )
    return result


BODY = "# Summary\nDo work\n\n## Scope\nThe selected work.\n\n## Claim\nProduce the declared result.\n## Details\n"
PLAN_BODY = (
    BODY.replace("## Scope\nThe selected work.\n\n", "").replace("## Claim", "## Objective") + "\n### Definition of Done\nThe result exists.\n"
)


def run(
    code: str,
    metadata: dict[str, Any],
    body: str = BODY,
    *,
    source_rows: list[dict[str, Any]] | None = None,
    raw: str | None = None,
    with_inputs: bool = True,
) -> Check:
    if code == "body.additional_properties" and "content_role" not in metadata:
        metadata = dict(metadata, content_role="Requirement")
    rows = sources() if source_rows is None else source_rows
    context = AuthorityContext([r["binding"] for r in rows], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation(code, [], True, "structural adapter"), context)
    if with_inputs:
        path = Path("/bounded/mock.md")
        text = raw or "---\n" + yaml.safe_dump(metadata) + "---\n" + body
        check.inputs = {
            "path": path,
            "parsed": parse_carrier(text.encode(), path),
            "sources": rows,
            "references": [],
            "reference_complete": True,
            "structure": None,
            "request": {},
        }
    ADAPTERS[code](metadata, body, check)
    return check


def common(metadata: dict[str, Any]) -> Check:
    context = AuthorityContext([], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation("frontmatter.common_encoding", [], True, "test"), context)
    _common(metadata, BODY, check)
    return check


class SchemaExtendedTest(unittest.TestCase):
    def assert_clean(self, check: Check) -> None:
        self.assertEqual(check.findings, [])
        self.assertEqual(check.gaps, [])

    def test_fixture_digests_match_reviewed_authority(self) -> None:
        entries = {}
        for name in ("registry.json", "schema_authority.json"):
            entries.update(
                json.loads((TOOL / "validate_atoms_workers" / name).read_text())["sources"]
            )
        for row in sources():
            with self.subTest(atom_id=row["binding"]["atom_id"]):
                self.assertEqual(
                    row["binding"]["sha256"], entries[row["binding"]["atom_id"]]["sha256"]
                )

    def test_updated_at_accepts_single_and_double_quotes(self) -> None:
        for quote in ('"', "'"):
            with self.subTest(quote=quote):
                raw = f"---\nupdated_at: {quote}2026-09-25 12:00:00 +0000{quote}\n---\n" + BODY
                self.assert_clean(run("frontmatter.updated_at_quoting", {}, raw=raw))

    def test_updated_at_rejects_plain_even_when_yaml_decodes_string(self) -> None:
        raw = "---\nupdated_at: 2026-09-25 12:00:00 +0000\n---\n" + BODY
        self.assertTrue(run("frontmatter.updated_at_quoting", {}, raw=raw).findings)

    def test_updated_at_block_scalar_is_not_quoted(self) -> None:
        raw = "---\nupdated_at: |-\n  2026-09-25T12:00:00Z\n---\n" + BODY
        self.assertTrue(run("frontmatter.updated_at_quoting", {}, raw=raw).findings)

    def test_quoting_needs_raw_carrier_and_missing_value_fails(self) -> None:
        self.assertTrue(run("frontmatter.updated_at_quoting", {}, with_inputs=False).gaps)
        self.assertTrue(run("frontmatter.updated_at_quoting", {}).findings)

    def test_common_property_names_are_admitted(self) -> None:
        self.assert_clean(
            run(
                "property.admission",
                {
                    "atom_id": "EX-R-1",
                    "content_role": "Requirement",
                    "type": "Requirement",
                    "current_scope_unit": "EX",
                    "claim_target_scope_unit": "EX",
                    "local_tier": "Core",
                    "global_tier": 0,
                    "version": 1,
                    "updated_at": "2026-09-25T00:00:00Z",
                    "author": "Example",
                    "status": "Active",
                    "subjects": {"governs": "Atom"},
                    "relations": {},
                },
            )
        )

    def test_unknown_property_without_declaration_fails(self) -> None:
        self.assertTrue(
            run(
                "property.admission",
                {"content_role": "Plan", "type": "Plan", "invented_schema_flag": True},
            ).findings
        )

    def test_explicitly_forbidden_fields_do_not_become_schema_gaps(self) -> None:
        for field in ("summary", "claim", "identifier", "operators", "cce_form"):
            with self.subTest(field=field):
                self.assertTrue(run("property.admission", {field: "wrong"}).findings)

    def test_known_conditional_fields_reject_wrong_roles(self) -> None:
        for field in ("assignee", "autonomous_confidence_threshold", "implementation_retry_limit"):
            with self.subTest(field=field):
                self.assertTrue(
                    run(
                        "property.admission",
                        {"content_role": "Requirement", "type": "Requirement", field: 1},
                    ).findings
                )
        self.assertTrue(
            run(
                "property.admission", {"content_role": "Plan", "type": "Plan", "priority": "high"}
            ).findings
        )

    def test_plan_override_and_concern_priority_admission(self) -> None:
        self.assert_clean(
            run(
                "property.admission",
                {
                    "content_role": "Plan",
                    "type": "Plan",
                    "assignee": "Example",
                    "autonomous_confidence_threshold": 0,
                    "implementation_retry_limit": 0,
                },
            )
        )
        self.assert_clean(
            run(
                "property.admission",
                {"content_role": "Concern", "type": "Question", "priority": "high"},
            )
        )

    def test_nested_unknown_keys_are_rejected(self) -> None:
        self.assertTrue(
            run("property.admission", {"subjects": {"governs": "Atom", "extra": 1}}).findings
        )
        self.assertTrue(
            run(
                "property.admission", {"projection": {"source_carrier_path": "a.md", "extra": 1}}
            ).findings
        )

    def test_unresolved_field_declaration_is_gap_not_permission(self) -> None:
        rows = sources()
        rows.append(
            {
                "binding": {
                    "atom_id": "EX-D-1",
                    "version": 1,
                    "path": "/mock/ex.md",
                    "sha256": "unreviewed",
                },
                "metadata": {"subjects": {"governs": "Atom/Carrier"}},
                "text": "---\nversion: 1\n---\nClaim: use `custom_field` as a carrier field.",
            }
        )
        checked = run("property.admission", {"custom_field": "x"}, source_rows=rows)
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_opaque_extension_prevents_unknown_field_rejection(self) -> None:
        rows = sources()
        rows.append(
            {
                "binding": {
                    "atom_id": "EX-D-1",
                    "version": 1,
                    "path": "/mock/ex.md",
                    "sha256": "unreviewed",
                },
                "metadata": {},
                "text": "---\nversion: 1\n---\nThe external schema determines additional Properties.",
            }
        )
        checked = run("property.admission", {"custom_field": "x"}, source_rows=rows)
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_incomplete_inventory_prevents_unknown_field_rejection(self) -> None:
        rows = [row for row in sources() if row["binding"]["atom_id"] != "CA-D-470"]
        checked = run("property.admission", {"custom_field": "x"}, source_rows=rows)
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_opaque_extension_prevents_unknown_body_property_rejection(self) -> None:
        rows = sources()
        rows.append(
            {
                "binding": {
                    "atom_id": "EX-D-1",
                    "version": 1,
                    "path": "/mock/ex.md",
                    "sha256": "unreviewed",
                },
                "metadata": {},
                "text": "---\nversion: 1\n---\nThe external schema determines additional Properties.",
            }
        )
        checked = run(
            "body.additional_properties",
            {},
            BODY + "\n## Extension Property\nX\n",
            source_rows=rows,
        )
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_schema_sources_must_be_exact_and_runtime_inputs_present(self) -> None:
        rows = sources()
        for row in rows:
            if row["binding"]["atom_id"] == "CA-D-276":
                row["text"] += "\nchanged\n"
        self.assertTrue(run("property.admission", {}, source_rows=rows).gaps)
        self.assertTrue(run("property.admission", {}, with_inputs=False).gaps)

    def test_body_properties_cannot_be_frontmatter_copies(self) -> None:
        for field in ("summary", "claim", "definition_of_done", "details"):
            with self.subTest(field=field):
                checked = run(
                    "property.single_location",
                    {"content_role": "Plan", "type": "Plan", field: "duplicate"},
                    PLAN_BODY,
                )
                self.assertTrue(checked.findings)
        self.assert_clean(
            run("property.single_location", {"content_role": "Plan", "type": "Plan"}, PLAN_BODY)
        )

    def test_property_copy_is_invalid_even_without_canonical_body_value(self) -> None:
        self.assertTrue(run("property.single_location", {"summary": "wrong location"}, "").findings)

    def test_known_frontmatter_property_cannot_become_body_property(self) -> None:
        checked = run(
            "property.single_location", {"status": "Active"}, BODY + "\n## Status\nActive\n"
        )
        self.assertTrue(checked.findings)

    def test_extra_body_property_rejected_but_supporting_heading_allowed(self) -> None:
        self.assertTrue(run("body.additional_properties", {}, BODY + "\n## Surprise\nX\n").findings)
        self.assert_clean(run("body.additional_properties", {}, BODY + "\n### Evidence\nX\n"))

    def test_plan_body_properties_use_exact_order_and_cardinality(self) -> None:
        meta = {"content_role": "Plan", "type": "Plan"}
        self.assert_clean(run("body.additional_properties", meta, PLAN_BODY))
        self.assertTrue(
            run(
                "body.additional_properties",
                meta,
                BODY + "\n## Details\nX\n## Definition of Done\nY\n",
            ).findings
        )
        self.assertTrue(
            run("body.additional_properties", meta, PLAN_BODY + "\n## Details\nAgain\n").findings
        )

    def test_registered_property_cannot_be_ambiguously_nested(self) -> None:
        self.assertTrue(
            run(
                "body.additional_properties",
                {"content_role": "Plan", "type": "Plan"},
                BODY + "\n### Definition of Done\nX\n",
            ).findings
        )

    def test_fenced_markers_are_not_property_boundaries(self) -> None:
        self.assert_clean(
            run("body.additional_properties", {}, BODY + "\n```md\n## Surprise\n```\n")
        )

    def test_additional_body_schema_missing_or_changed_is_gap(self) -> None:
        rows = [r for r in sources() if r["binding"]["atom_id"] != "CA-D-470"]
        self.assertTrue(
            run(
                "body.additional_properties",
                {"content_role": "Plan", "type": "Plan"},
                PLAN_BODY,
                source_rows=rows,
            ).gaps
        )

    def test_model_domain_rejects_unknown_content_role(self) -> None:
        self.assertTrue(run("model.domains", {"content_role": "Invented", "type": "Plan"}).findings)

    def test_role_qualified_type_values_and_project_expansion(self) -> None:
        for role, kind in (
            ("Concern", "Problem"),
            ("Analysis", "Analysis Report"),
            ("Plan", "Plan"),
            ("Plan", "Action Policy"),
            ("Operations", "Action"),
        ):
            with self.subTest(role=role, kind=kind):
                self.assert_clean(run("model.domains", {"content_role": role, "type": kind}))

    def test_ordinary_rmd_type_is_optional_but_specialized_values_remain_checked(self) -> None:
        for role in ("Requirement", "Method", "Delivery"):
            with self.subTest(role=role):
                self.assert_clean(run("model.domains", {"content_role": role}))
        self.assert_clean(run("model.domains", {"content_role": "Requirement", "type": "Boundary"}))
        self.assert_clean(run("model.domains", {"content_role": "Requirement", "type": "Goal"}))
        self.assert_clean(run("model.domains", {"content_role": "Requirement", "type": "Demand"}))
        self.assert_clean(
            run("model.domains", {"content_role": "Method", "type": "Implementation Method"})
        )
        self.assert_clean(
            run("model.domains", {"content_role": "Delivery", "type": "Release Definition"})
        )

    def test_ordinary_type_omission_is_source_bound_and_common_encoding_stays_strict(self) -> None:
        base = {
            "content_role": "Requirement",
            "current_scope_unit": "EX",
            "local_tier": "Core",
            "global_tier": 0,
        }
        self.assert_clean(common(base))
        self.assertTrue(common({**base, "content_role": "Plan"}).findings)
        for value in (None, "", ["Requirement"]):
            with self.subTest(value=value):
                self.assertTrue(common({**base, "type": value}).findings)

        rows = [row for row in sources() if row["binding"]["atom_id"] != "CA-R-1700"]
        missing = run("model.domains", {"content_role": "Requirement"}, source_rows=rows)
        self.assertFalse(missing.findings)
        self.assertTrue(missing.gaps)

    def test_ordinary_rmd_rejects_invalid_or_redundant_type_values(self) -> None:
        for role, value in (
            ("Requirement", None),
            ("Method", ""),
            ("Delivery", ["Delivery"]),
            ("Requirement", "Requirement"),
            ("Method", "Method"),
            ("Delivery", "Delivery"),
        ):
            with self.subTest(role=role, value=value):
                self.assertTrue(run("model.domains", {"content_role": role, "type": value}).findings)

    def test_nonordinary_roles_still_require_an_admitted_type(self) -> None:
        for role in ("Plan", "Evaluation", "Operations"):
            with self.subTest(role=role):
                self.assertTrue(run("model.domains", {"content_role": role}).findings)

    def test_known_type_in_wrong_role_fails(self) -> None:
        self.assertTrue(run("model.domains", {"content_role": "Plan", "type": "Question"}).findings)

    def test_unreviewed_type_extension_causes_gap(self) -> None:
        rows = sources()
        rows.append(
            {
                "binding": {
                    "atom_id": "EX-R-1",
                    "version": 1,
                    "path": "/mock/ex.md",
                    "sha256": "unreviewed",
                },
                "metadata": {"subjects": {"governs": "Atom/Content Role: Plan/Type"}},
                "text": "---\nversion: 1\n---\nCustom Plan is an admitted Type.",
            }
        )
        checked = run(
            "model.domains", {"content_role": "Plan", "type": "Custom Plan"}, source_rows=rows
        )
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_changed_type_contribution_never_grants_membership(self) -> None:
        rows = sources()
        for row in rows:
            if row["binding"]["atom_id"] == "CA-R-1666":
                row["text"] += "\nchanged\n"
        checked = run(
            "model.domains", {"content_role": "Plan", "type": "Action Policy"}, source_rows=rows
        )
        self.assertFalse(checked.findings)
        self.assertTrue(checked.gaps)

    def test_unrelated_unknown_source_does_not_disable_known_domain_error(self) -> None:
        rows = sources()
        rows.append(
            {
                "binding": {
                    "atom_id": "EX-R-1",
                    "version": 1,
                    "path": "/mock/ex.md",
                    "sha256": "unreviewed",
                },
                "metadata": {"subjects": {"governs": "Realization Graph"}},
                "text": "---\nversion: 1\n---\nDefine graph representation.",
            }
        )
        checked = run(
            "model.domains", {"content_role": "Plan", "type": "Question"}, source_rows=rows
        )
        self.assertTrue(checked.findings)

    def test_evaluation_mechanism_labels_are_explicitly_invalid_types(self) -> None:
        for kind in ("Evaluation", "Test"):
            self.assertTrue(
                run("model.domains", {"content_role": "Evaluation", "type": kind}).findings
            )

    def test_missing_type_model_is_a_gap(self) -> None:
        self.assertTrue(
            run("model.domains", {"content_role": "Implementation", "type": "Code"}).gaps
        )

    def test_plan_model_is_structural_and_label_does_not_change_it(self) -> None:
        self.assert_clean(
            run("plan.model", {"content_role": "Plan", "type": "Plan", "label": "Epic"}, PLAN_BODY)
        )
        self.assertTrue(
            run(
                "plan.model",
                {"content_role": "Plan", "type": "Plan"},
                PLAN_BODY + "\n## Objective\nA second value\n",
            ).findings
        )
        self.assertTrue(
            run(
                "plan.model",
                {"content_role": "Plan", "type": "Plan"},
                "# Summary\nX\n## Claim\n\n## Definition of Done\nY\n",
            ).findings
        )

    def test_plan_model_does_not_misapply_to_registered_action_policy(self) -> None:
        checked = run("plan.model", {"content_role": "Plan", "type": "Action Policy"})
        self.assertFalse(checked.applicable)
        self.assert_clean(checked)

    def test_unknown_plan_type_is_a_gap_and_other_roles_not_applicable(self) -> None:
        self.assertTrue(run("plan.model", {"content_role": "Plan", "type": "Custom"}).gaps)
        checked = run("plan.model", {"content_role": "Requirement", "type": "Requirement"})
        self.assertFalse(checked.applicable)

    def test_plan_type_collection_is_invalid_not_an_adapter_error(self) -> None:
        self.assertTrue(run("plan.model", {"content_role": "Plan", "type": ["Plan"]}).findings)


if __name__ == "__main__":
    unittest.main()
