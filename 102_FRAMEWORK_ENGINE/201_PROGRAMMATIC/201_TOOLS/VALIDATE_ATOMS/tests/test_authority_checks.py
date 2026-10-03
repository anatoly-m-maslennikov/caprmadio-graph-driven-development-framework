"""Source-bound primitive checks; expected behavior comes from named authority."""

from __future__ import annotations

import copy
import hashlib
import sys
import unittest
from pathlib import Path
from typing import Any

import yaml

TOOL = Path(__file__).resolve().parents[1]
CORE = Path(__file__).resolve().parent / "fixtures/authority_checks"
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.authority import resolve_context  # noqa: E402
from validate_atoms_workers.checks import validate_carrier  # noqa: E402


def source(atom_id: str) -> dict[str, Any]:
    path = CORE / f"{atom_id}.md"
    text = path.read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    return {
        "binding": {
            "atom_id": atom_id,
            "version": metadata["version"],
            "path": str(path),
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        },
        "text": text,
        "metadata": metadata,
    }


def run_check(atom_ids: list[str], metadata: dict[str, Any], body: str = "") -> dict[str, Any]:
    return validate_carrier(metadata, body, resolve_context([source(a) for a in atom_ids]))


def outcome(result: dict[str, Any], code: str) -> dict[str, Any]:
    return next(value for value in result["outcomes"] if value["code"] == code)


class AuthorityChecksTest(unittest.TestCase):
    def test_absent_authority_cannot_execute_retired_field_check(self) -> None:
        result = validate_carrier({"cce_form": "method"}, "", resolve_context([]))
        self.assertEqual(outcome(result, "property.retired_fields")["outcome"], "not_checked")
        self.assertFalse(result["findings"])

    def test_changed_source_retains_obligations_but_does_not_execute(self) -> None:
        original = source("CA-D-478")
        context = resolve_context([original])
        changed = copy.deepcopy(original)
        changed["text"] += "\nchanged\n"
        changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode()).hexdigest()
        stale = resolve_context([changed])
        self.assertEqual(stale.required, context.required)
        self.assertGreater(stale.unsupported, context.unsupported)
        self.assertEqual(stale.required, stale.supported + stale.unsupported)
        self.assertTrue(stale.gaps)

    def test_unknown_source_retains_an_obligation(self) -> None:
        known = source("CA-D-478")
        unknown = copy.deepcopy(known)
        unknown["binding"]["atom_id"] = "EX-R-900"
        context = resolve_context([unknown])
        self.assertTrue(any("EX-R-900" in gap["reason"] for gap in context.gaps))

    def test_retired_fields_are_errors_and_not_required(self) -> None:
        clean = run_check(["CA-D-478"], {})
        bad = run_check(["CA-D-478"], {"cce_version": "cce_1", "llm_session_ids": []})
        self.assertEqual(outcome(clean, "property.retired_fields")["outcome"], "passed")
        failed = outcome(bad, "property.retired_fields")
        self.assertEqual(failed["outcome"], "failed")
        self.assertEqual(len(failed["finding_indexes"]), 2)
        self.assertTrue(all(f["code"] == "PROPERTY_RETIRED" for f in bad["findings"]))

    def test_version_and_timestamp_do_not_coerce_values(self) -> None:
        for version in (True, "1", 0, None):
            result = run_check(
                ["CA-D-270"], {"version": version, "updated_at": "2026-09-24T19:00:00Z"}
            )
            self.assertEqual(outcome(result, "frontmatter.version")["outcome"], "failed")
        for timestamp in (
            "2026-02-30T00:00:00Z",
            "2026-09-24T19:00:00",
            "2026-09-24T19:00:00+25:00",
        ):
            result = run_check(["CA-D-270"], {"version": 1, "updated_at": timestamp})
            self.assertEqual(outcome(result, "frontmatter.updated_at")["outcome"], "failed")
        for timestamp in ("2026-09-24 19:00:00 +0400", "2026-09-24T19:00:00.1-03:30"):
            result = run_check(["CA-D-270"], {"version": 1, "updated_at": timestamp})
            self.assertEqual(outcome(result, "frontmatter.updated_at")["outcome"], "passed")

    def test_subjects_and_relations_reject_wrong_shapes(self) -> None:
        result = run_check(
            ["CA-D-269", "CA-D-268"],
            {
                "subjects": {"governs": ["Atom"], "depends_on": ["Atom", "Atom"]},
                "relations": {"relates_to": []},
            },
        )
        self.assertEqual(outcome(result, "frontmatter.subjects")["outcome"], "failed")
        self.assertEqual(outcome(result, "frontmatter.relations")["outcome"], "failed")
        clean = run_check(
            ["CA-D-269", "CA-D-268"], {"subjects": {"governs": "Atom"}, "relations": {}}
        )
        self.assertEqual(outcome(clean, "frontmatter.subjects")["outcome"], "passed")
        self.assertEqual(outcome(clean, "frontmatter.relations")["outcome"], "passed")

    def test_fenced_headings_do_not_create_body_properties(self) -> None:
        valid = "# Summary\nA summary\n\n## Scope\nA scope\n\n## Claim\nA claim\n```md\n## Claim\n```\n## Details\n"
        result = run_check(["CA-D-479"], {"content_role": "Requirement"}, valid)
        self.assertEqual(outcome(result, "body.sections")["outcome"], "passed")
        invalid = run_check(
            ["CA-D-479"], {"content_role": "Requirement"}, valid + "\n## Claim\nAgain\n"
        )
        self.assertEqual(outcome(invalid, "body.sections")["outcome"], "failed")

    def test_empty_summary_is_not_filled_by_claim_content(self) -> None:
        result = run_check(
            ["CA-D-479"],
            {"content_role": "Requirement"},
            "# Summary\n\n## Claim\nA claim\n## Details\n",
        )
        self.assertEqual(outcome(result, "body.sections")["outcome"], "failed")

    def test_unclassified_expansion_cannot_be_rejected_by_core_domain(self) -> None:
        original = source("CA-R-1608")
        expansion = copy.deepcopy(original)
        expansion["binding"]["atom_id"] = "EX-R-900"
        context = resolve_context([original, expansion])
        result = validate_carrier({"content_role": "Concern", "status": "Review"}, "", context)
        self.assertEqual(outcome(result, "domain.status.concern")["outcome"], "not_checked")

    def test_concern_domain_preserves_exact_case(self) -> None:
        for value, expected in (("active", "passed"), ("Active", "failed")):
            result = run_check(["CA-R-1608"], {"content_role": "Concern", "status": value})
            self.assertEqual(outcome(result, "domain.status.concern")["outcome"], expected)

    def test_lowercase_draft_does_not_allocate_identity(self) -> None:
        result = run_check(
            ["CA-D-446", "CA-R-1608"],
            {"content_role": "Concern", "status": "draft", "atom_id": "EX-C-1"},
        )
        self.assertEqual(outcome(result, "frontmatter.atom_id")["outcome"], "failed")

    def test_plan_sections_and_priority_are_conditional(self) -> None:
        body = "# Summary\nWork\n## Objective\nDo work\n## Details\nContext\n### Definition of Done\nResult exists\n"
        result = run_check(
            ["CA-D-470", "CA-D-386"],
            {"content_role": "Plan", "type": "Plan", "priority": "high"},
            body,
        )
        self.assertEqual(outcome(result, "plan.sections")["outcome"], "passed")
        self.assertEqual(outcome(result, "concern.priority")["outcome"], "failed")

    def test_plan_role_does_not_imply_plan_type(self) -> None:
        result = run_check(["CA-D-470"], {"content_role": "Plan", "type": "Action Policy"})
        self.assertEqual(outcome(result, "plan.sections")["outcome"], "not_checked")

    def test_timestamp_value_does_not_prove_quoted_source_encoding(self) -> None:
        result = run_check(["CA-D-270"], {"version": 1, "updated_at": "2026-09-24T19:00:00Z"})
        self.assertEqual(
            outcome(result, "frontmatter.updated_at_quoting")["outcome"], "not_checked"
        )

    def test_author_string_does_not_establish_actor_resolution(self) -> None:
        result = run_check(["CA-D-274"], {"author": "Example Author"})
        self.assertEqual(outcome(result, "frontmatter.author")["outcome"], "passed")
        self.assertEqual(outcome(result, "author.resolution")["outcome"], "not_checked")
        self.assertTrue(result["gaps"])


if __name__ == "__main__":
    unittest.main()
