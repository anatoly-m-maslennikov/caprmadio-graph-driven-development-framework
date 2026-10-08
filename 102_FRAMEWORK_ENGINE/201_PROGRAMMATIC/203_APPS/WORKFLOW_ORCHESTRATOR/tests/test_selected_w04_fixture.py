"""Focused admission coverage for the disposable W04 status carriers."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path
import unittest


TESTS = Path(__file__).resolve().parent
PROGRAMMATIC = TESTS.parents[2]
TOOLS = PROGRAMMATIC / "201_TOOLS"
for location in (TESTS, TOOLS, TOOLS / "VALIDATE_ATOMS"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from lifecycle_intents import change_status_atom_action
from authoritative_status_models import resolve_status_model
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject, STATUS_DOMAINS


class SelectedW04FixtureTests(unittest.TestCase):
    def _fixture(self) -> GoldenProject:
        repository = TESTS.parents[4]
        scratch = repository / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        root = Path(tempfile.mkdtemp(prefix="caprmedio-w04-", dir=scratch))
        self.addCleanup(FixtureLease(root).cleanup)
        fixture = GoldenProject(repository, root, GoldenCase("W04", "change_atom_status"))
        fixture.prepare()
        return fixture

    def test_status_carriers_are_complete_under_declared_parent_scope(self) -> None:
        fixture = self._fixture()
        types = {
            "Requirement": None,
            "Method": None,
            "Evaluation": "Evaluation Approach",
            "Delivery": None,
            "Plan": "Plan",
            "Concern": "Question",
            "Operations": "Action",
            "Analysis": "Analysis Report",
        }
        sections = {
            "Requirement": ("Scope", "Claim", "Details"),
            "Method": ("Scope", "Claim", "Details"),
            "Evaluation": ("Scope", "Claim", "Details"),
            "Delivery": ("Scope", "Claim", "Details"),
            "Plan": ("Objective", "Details", "Definition of Done"),
            "Concern": ("Concern", "Evidences", "Blast radius"),
            "Operations": ("Operation", "Details"),
            "Analysis": ("Question", "Scope", "Approach", "Results", "TLDR"),
        }

        for number, (role, letter, directory, _source, statuses) in enumerate(STATUS_DOMAINS, start=8000):
            path = fixture.status_atom(role, statuses[-1], number=number)
            relative = path.relative_to(fixture.root / ".caprmedio_caprmedio")
            self.assertEqual(relative.parts[:2], ("PARENT", directory))
            carrier = path.read_text(encoding="utf-8")
            self.assertIn(f"atom_id: CA-{letter}-{number}", carrier)
            self.assertIn("current_scope_unit: PARENT", carrier)
            self.assertIn("claim_target_scope_unit: PARENT", carrier)
            self.assertIn("local_tier: Standard", carrier)
            self.assertIn("global_tier: 5", carrier)
            self.assertIn("author: golden-operator", carrier)
            self.assertIn("subjects:\n  governs: Atom/Test\n  depends_on: []", carrier)
            self.assertIn("# Summary", carrier)
            if types[role] is None:
                self.assertNotIn("type:", carrier)
            else:
                self.assertIn(f"type: {types[role]}", carrier)
            for heading in sections[role]:
                marker = "### Definition of Done" if heading == "Definition of Done" else f"## {heading}"
                self.assertIn(marker, carrier)
            model = resolve_status_model(
                fixture.root,
                {"content_role": role, "type": types[role]},
                statuses[-1],
            )
            self.assertEqual(model["statuses"], list(statuses))

        draft = fixture.status_atom("Requirement", "Draft", draft=True)
        draft_carrier = draft.read_text(encoding="utf-8")
        self.assertNotIn("atom_id:", draft_carrier)
        self.assertNotRegex(draft.name, r"CA-R-\d+")

    def test_archived_requirement_moves_to_active_through_native_admission(self) -> None:
        fixture = self._fixture()
        source = fixture.status_atom("Requirement", "Archived", number=8100)
        outcome = change_status_atom_action(
            fixture.root,
            {"target": fixture._descriptor(source.relative_to(fixture.root).as_posix()), "status": "Active"},
            execute=True,
            authorized=True,
        )
        self.assertEqual(outcome["outcome"], "applied")
        self.assertEqual(outcome["prior_status"], "Archived")

    def test_resolved_concern_moves_to_lowercase_active_under_parent_scope(self) -> None:
        fixture = self._fixture()
        source = fixture.status_atom("Concern", "resolved", number=8200)
        outcome = change_status_atom_action(
            fixture.root,
            {"target": fixture._descriptor(source.relative_to(fixture.root).as_posix()), "status": "active"},
            execute=True,
            authorized=True,
        )
        self.assertEqual("applied", outcome["outcome"])
        observed = outcome["observed"]
        self.assertEqual("active", observed["status"])
        self.assertEqual(
            ".caprmedio_caprmedio/PARENT/01_concern/CA-C-8200--docker-status.md",
            observed["path"],
        )

    def test_every_source_admitted_status_has_a_native_transition(self) -> None:
        fixture = self._fixture()
        number = 8300
        for role, _letter, _directory, source_id, statuses in STATUS_DOMAINS:
            for requested in statuses:
                with self.subTest(role=role, requested_status=requested):
                    current = next(
                        status for status in statuses
                        if status != requested and status.casefold() != "draft"
                    )
                    source = fixture.status_atom(role, current, number=number)
                    number += 1
                    outcome = change_status_atom_action(
                        fixture.root,
                        {"target": fixture._descriptor(source.relative_to(fixture.root).as_posix()), "status": requested},
                        execute=True,
                        authorized=True,
                    )
                    self.assertEqual("applied", outcome["outcome"])
                    model = outcome["status_model"]
                    self.assertEqual(list(statuses), model["statuses"])
                    self.assertEqual(requested, model["requested_status"])
                    self.assertEqual(source_id, model["model_sources"][0]["atom_id"])
                    self.assertEqual(requested, outcome["observed"]["status"])


if __name__ == "__main__":
    unittest.main()
