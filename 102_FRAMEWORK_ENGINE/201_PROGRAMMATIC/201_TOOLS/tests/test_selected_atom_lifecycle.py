from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

import sys

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from lifecycle_intents import (  # noqa: E402
    LifecycleError,
    carrier_descriptor,
    change_status_atom_action,
    create_atom_action,
    replace_atom_action,
    update_atom_action,
)
from atom_operations import ToolError  # noqa: E402


class SelectedAtomLifecycleTest(unittest.TestCase):
    """Golden single-target lifecycle cases for the CA-D-527 route payload."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.requirements = self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement"
        self.requirements.mkdir(parents=True)
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n", encoding="utf-8"
        )
        self.target = self._atom("CA-R-100", "target", "Stable summary")
        self.successor_one = self._atom("CA-R-101", "first-successor", "First successor")
        self.successor_two = self._atom("CA-R-102", "second-successor", "Second successor")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _atom(
        self,
        atom_id: str,
        slug: str,
        summary: str,
        *,
        status: str = "Active",
        version: int = 1,
        relations: str = "relations: {}",
        include_type: bool = False,
    ) -> Path:
        path = self.requirements / f"{atom_id}--{slug}.md"
        payload = (
            "---\n"
            + f"atom_id: {atom_id}\n"
            + "content_role: Requirement\n"
            + ("type: Requirement\n" if include_type else "")
            + f"status: {status}\n"
            + f"version: {version}\n"
            + "updated_at: 2026-01-01 00:00:00 +0000\n"
            + f"{relations}\n"
            + "---\n"
            + "# Summary\n\n"
            + f"{summary}\n\n"
            + "## Scope\n\n"
            + "Fixture scope.\n\n"
            + "## Claim\n\n"
            + "Fixture claim.\n"
        )
        path.write_text(payload, encoding="utf-8")
        return path

    @staticmethod
    def _model() -> dict[str, object]:
        return {
            "model_ref": "fixture://requirement-statuses",
            "model_revision": "7",
            "content_role": "Requirement",
            "statuses": ["Active", "Reviewed", "Archived"],
            "transitions": {"Active": ["Reviewed", "Archived"], "Reviewed": ["Active", "Archived"]},
            "archive_status": "Archived",
        }

    def _carrier(self, atom_id: str, slug: str, summary: str) -> dict[str, str]:
        path = self.requirements / f"{atom_id}--{slug}.md"
        return {
            "path": path.relative_to(self.root).as_posix(),
            "frontmatter": f"atom_id: {atom_id}\ncontent_role: Requirement\nstatus: Active",
            "content": f"# Summary\n\n{summary}\n\n## Scope\n\nFixture.\n",
        }

    @staticmethod
    def _proposal(path: Path, *, summary: str, body_suffix: str = "") -> dict[str, str]:
        text = path.read_text(encoding="utf-8")
        frontmatter, content = text[4:].split("\n---\n", 1)
        current_summary = content.split("# Summary\n\n", 1)[1].split("\n\n", 1)[0]
        return {
            "frontmatter": frontmatter,
            "content": content.replace(current_summary, summary, 1) + body_suffix,
        }

    def test_authorized_create_uses_a_complete_carrier_and_duplicate_is_no_effect(self) -> None:
        path = self.requirements / "CA-R-103--created.md"
        carrier = self._carrier("CA-R-103", "created", "Created summary")

        result = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)

        self.assertEqual(result["operation"], "create")
        self.assertEqual(result["effects"][0]["state"], "changed")
        self.assertEqual(carrier_descriptor(self.root, "CA-R-103")["version"], 1)
        before = path.read_bytes()
        duplicate = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        self.assertEqual(duplicate["outcome"], "duplicate")
        self.assertEqual(path.read_bytes(), before)

        missing_identity = dict(carrier)
        missing_identity["path"] = (self.requirements / "CA-R-104--missing-id.md").relative_to(self.root).as_posix()
        missing_identity["frontmatter"] = "content_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-required"):
            create_atom_action(self.root, {"carrier": missing_identity}, execute=True, authorized=True)
        mismatch = dict(carrier)
        mismatch["path"] = (self.requirements / "CA-R-105--mismatch.md").relative_to(self.root).as_posix()
        mismatch["frontmatter"] = "atom_id: CA-R-106\ncontent_role: Requirement\nstatus: Active"
        with self.assertRaisesRegex(LifecycleError, "atom-frontmatter-id-mismatch"):
            create_atom_action(self.root, {"carrier": mismatch}, execute=True, authorized=True)

    def test_changed_summary_is_a_terminal_non_effect_replace_handoff(self) -> None:
        before = self.target.read_bytes()
        result = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Changed summary"),
                "change_class": "semantic_revision",
                "successors": [self._carrier("CA-R-105", "replacement", "Changed summary")],
            },
            execute=True,
            authorized=True,
        )

        self.assertEqual(result["outcome"], "replace_handoff")
        self.assertEqual(result["effects"][0]["state"], "unchanged")
        self.assertEqual(result["replace_handoff"]["predecessor"]["atom_id"], "CA-R-100")
        self.assertEqual(result["replace_handoff"]["successors"][0]["frontmatter"].splitlines()[0], "atom_id: CA-R-105")
        self.assertEqual(self.target.read_bytes(), before)

    def test_update_honors_identity_revision_class_and_true_noop(self) -> None:
        carrier_only = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nCarrier note.\n"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(carrier_only["observed"]["version"], 1)
        self.assertEqual(carrier_only["effects"][0]["state"], "changed")

        semantic = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary", body_suffix="\nSemantic detail.\n"),
                "change_class": "semantic_revision",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(semantic["observed"]["version"], 2)
        prior_revision = self.root / semantic["history"]["prior_revision"]["path"]
        self.assertTrue(prior_revision.exists())
        self.assertEqual(semantic["history"]["prior_revision"]["version"], 1)

        before = self.target.read_bytes()
        noop = update_atom_action(
            self.root,
            {
                "target": carrier_descriptor(self.root, "CA-R-100"),
                "proposed": self._proposal(self.target, summary="Stable summary"),
                "change_class": "carrier_only",
            },
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")
        self.assertEqual(self.target.read_bytes(), before)

    def test_replace_publishes_supplied_successors_then_archives_one_predecessor(self) -> None:
        first = self._carrier("CA-R-105", "first-replacement", "First replacement")
        second = self._carrier("CA-R-106", "second-replacement", "Second replacement")
        result = replace_atom_action(
            self.root,
            {
                "predecessor": carrier_descriptor(self.root, "CA-R-100"),
                "successors": [first, second],
                "status_model": self._model(),
            },
            execute=True,
            authorized=True,
        )

        predecessor = result["predecessor"]
        self.assertEqual(result["outcome"], "applied")
        self.assertEqual(len(result["successors"]), 2)
        self.assertFalse(self.target.exists())
        self.assertTrue((self.root / first["path"]).exists())
        self.assertTrue((self.root / second["path"]).exists())
        archived = self.root / predecessor["path"]
        self.assertTrue(archived.exists())
        self.assertIn("@1", archived.name)
        self.assertIn("status: Archived", archived.read_text(encoding="utf-8"))

    def test_model_specific_status_noop_and_archive_relation_diagnostics(self) -> None:
        self.target.write_text(
            self.target.read_text(encoding="utf-8").replace("relations: {}", "relations:\n  depends_on: [CA-R-101]"),
            encoding="utf-8",
        )
        self._atom("CA-R-104", "inbound", "Inbound", relations="relations:\n  depends_on: [CA-R-100]")
        self.assertNotIn("type:", self.target.read_text(encoding="utf-8"))

        reviewed = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Reviewed", "status_model": self._model()},
            execute=True,
            authorized=True,
        )
        self.assertEqual(reviewed["observed"]["status"], "Reviewed")
        reviewed_path = self.root / reviewed["observed"]["path"]
        self.assertEqual(reviewed_path.parent.name, "reviewed")
        self.assertFalse(self.target.exists())
        noop = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Reviewed", "status_model": self._model()},
            execute=True,
            authorized=True,
        )
        self.assertEqual(noop["outcome"], "no-op")

        promoted = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Active", "status_model": self._model()},
            execute=True,
            authorized=True,
        )
        self.assertEqual(promoted["observed"]["status"], "Active")
        self.assertTrue(self.target.exists())

        archived = change_status_atom_action(
            self.root,
            {"target": carrier_descriptor(self.root, "CA-R-100"), "status": "Archived", "status_model": self._model()},
            execute=True,
            authorized=True,
        )
        self.assertEqual(archived["outcome"], "applied")
        self.assertEqual({item["direction"] for item in archived["broken_references"]}, {"inbound", "outgoing"})
        self.assertEqual(archived["repair_handoff"]["operation"], "repair_relations")
        self.assertTrue(self.successor_one.exists())

    def test_replace_reports_partial_when_successor_or_archive_publication_fails(self) -> None:
        first = self._carrier("CA-R-105", "first-partial", "First partial")
        second = self._carrier("CA-R-106", "second-partial", "Second partial")
        original_create = __import__("lifecycle_intents").create_atom_revision
        calls = 0

        def fail_second(*args: object, **kwargs: object) -> object:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise ToolError("injected-successor-failure", "second successor failed")
            return original_create(*args, **kwargs)

        with patch("lifecycle_intents.create_atom_revision", side_effect=fail_second):
            partial = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [first, second], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial["outcome"], "partial")
        self.assertTrue((self.root / first["path"]).exists())
        self.assertFalse((self.root / second["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial["unknown_remainder"][0]["phase"], "publish_successor")

        archive_failure = self._carrier("CA-R-107", "archive-partial", "Archive partial")
        with patch("lifecycle_intents.archive_atom_revision", side_effect=ToolError("injected-archive-failure", "archive failed")):
            partial_archive = replace_atom_action(
                self.root,
                {"predecessor": carrier_descriptor(self.root, "CA-R-100"), "successors": [archive_failure], "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(partial_archive["outcome"], "partial")
        self.assertTrue((self.root / archive_failure["path"]).exists())
        self.assertTrue(self.target.exists())
        self.assertEqual(partial_archive["unknown_remainder"][0]["phase"], "archive_predecessor")

    def test_stale_and_multi_target_requests_stop_before_an_effect(self) -> None:
        descriptor = carrier_descriptor(self.root, "CA-R-100")
        descriptor["digest"] = hashlib.sha256(b"stale").hexdigest()
        before = self.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "stale-carrier"):
            update_atom_action(
                self.root,
                {"target": descriptor, "proposed": self._proposal(self.target, summary="Stable summary"), "change_class": "carrier_only"},
                execute=True,
                authorized=True,
            )
        with self.assertRaisesRegex(LifecycleError, "one-target-required"):
            change_status_atom_action(
                self.root,
                {"target": [carrier_descriptor(self.root, "CA-R-100")], "status": "Reviewed", "status_model": self._model()},
                execute=True,
                authorized=True,
            )
        self.assertEqual(self.target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
