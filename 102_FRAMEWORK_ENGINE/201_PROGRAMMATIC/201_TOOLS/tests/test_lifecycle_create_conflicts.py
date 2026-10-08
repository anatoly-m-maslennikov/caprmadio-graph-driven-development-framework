from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "epic-resume-create"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

import sys

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from lifecycle_intents import LifecycleError, create_atom_action  # noqa: E402


class CreateAtomConflictTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = \".caprmedio_caprmedio\"\n",
            encoding="utf-8",
        )
        self.destination = (
            self.root
            / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CA-R-901--occupied.md"
        )
        self.destination.parent.mkdir(parents=True)
        self.destination.write_text(
            "---\n"
            "atom_id: CA-R-901\n"
            "content_role: Requirement\n"
            "status: Active\n"
            "version: 2\n"
            "updated_at: 2026-10-06 00:00:00 +0000\n"
            "---\n"
            "# Summary\n\n"
            "Existing occupied carrier\n",
            encoding="utf-8",
        )

    def test_occupied_destination_with_different_carrier_is_a_conflict_without_write(self) -> None:
        request = {
            "carrier": {
                "path": self.destination.relative_to(self.root).as_posix(),
                "frontmatter": "atom_id: CA-R-901\ncontent_role: Requirement\nstatus: Active",
                "content": "# Summary\n\nRequested new carrier\n",
            }
        }
        before = self.destination.read_bytes()

        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            create_atom_action(self.root, request, execute=True, authorized=True)

        self.assertEqual(before, self.destination.read_bytes())

    def test_malformed_preserved_history_reserves_identity_without_inferring_an_atom(self) -> None:
        history = self.destination.parent / "archive" / "CA-R-902--retained@1.md"
        history.parent.mkdir()
        history.write_bytes(b"retained but malformed historical bytes")
        destination = self.destination.with_name("CA-R-902--new.md")
        request = {
            "carrier": {
                "path": destination.relative_to(self.root).as_posix(),
                "frontmatter": "atom_id: CA-R-902\ncontent_role: Requirement\nstatus: Active",
                "content": "# Summary\n\nNew carrier\n",
            }
        }

        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            create_atom_action(self.root, request, execute=True, authorized=True)

        self.assertEqual(b"retained but malformed historical bytes", history.read_bytes())
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
