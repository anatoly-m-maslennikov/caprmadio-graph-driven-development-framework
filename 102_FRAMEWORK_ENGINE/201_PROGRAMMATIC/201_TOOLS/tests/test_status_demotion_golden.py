"""Focused native proof for model-admitted identified-to-Draft demotion."""
from __future__ import annotations

from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

from atom_operations import atom_from_path, frontmatter_scalar  # noqa: E402
from lifecycle_intents import LifecycleError  # noqa: E402
import test_model_driven_status_lifecycle as model_fixture  # noqa: E402


class StatusDemotionGoldenTest(unittest.TestCase):
    """Reuse only the disposable, real-source fixture from the native corpus."""

    def setUp(self) -> None:
        model_fixture.ModelDrivenStatusLifecycleTest.setUpClass()
        self.fixture = model_fixture.ModelDrivenStatusLifecycleTest("run")
        self.fixture.setUp()

    def tearDown(self) -> None:
        self.fixture.tearDown()

    def test_analysis_done_to_draft_preserves_history_and_meaning(self) -> None:
        path = self.fixture.atom("Analysis", "Done")
        before = atom_from_path(self.fixture.root, path)

        result = self.fixture.execute(self.fixture.request(path, "Draft"))

        destination = self.fixture.root / result["observed"]["path"]
        self.assertEqual("CA-A--golden.md", destination.name)
        self.assertFalse(path.exists())
        self.assertEqual(before.content, atom_from_path(self.fixture.root, destination).content)
        self.assertEqual(3, result["observed"]["version"])
        self.assertIsNone(result["observed"]["atom_id"])
        self.assertIsNone(frontmatter_scalar(atom_from_path(self.fixture.root, destination).frontmatter, "atom_id"))
        history = self.fixture.root / result["history"]["prior_revision"]["path"]
        self.assertTrue(history.exists())
        self.assertEqual(before.atom_id, atom_from_path(self.fixture.root, history).atom_id)

    def test_full_canonical_filename_removes_only_assigned_number(self) -> None:
        path = self.fixture.atom("Requirement", "Active", number=1309)
        canonical = path.with_name("CA-R-1309-CORE_META_MODEL-GENERAL--golden.md")
        path.rename(canonical)
        before = atom_from_path(self.fixture.root, canonical)

        result = self.fixture.execute(self.fixture.request(canonical, "Draft"))

        destination = self.fixture.root / result["observed"]["path"]
        self.assertEqual("CA-R--CORE_META_MODEL-GENERAL--golden.md", destination.name)
        self.assertEqual(before.content, atom_from_path(self.fixture.root, destination).content)
        self.assertEqual(3, result["observed"]["version"])
        self.assertIsNone(result["observed"]["atom_id"])

    def test_archived_carrier_cannot_be_demoted_or_create_history(self) -> None:
        path = self.fixture.atom("Requirement", "Active")
        archived = self.fixture.execute(self.fixture.request(path, "Archived"))
        archived_path = self.fixture.root / archived["observed"]["path"]
        self.assertEqual("archived", atom_from_path(self.fixture.root, archived_path).lifecycle)
        before = self.fixture.snapshot()

        with self.assertRaisesRegex(LifecycleError, "atom-not-current"):
            self.fixture.execute(self.fixture.request(archived_path, "Draft"))

        self.assertEqual(before, self.fixture.snapshot())

    def test_concern_resolved_to_lowercase_draft_is_a_demotion(self) -> None:
        path = self.fixture.atom("Concern", "resolved")
        before = atom_from_path(self.fixture.root, path)

        result = self.fixture.execute(self.fixture.request(path, "draft"))

        destination = self.fixture.root / result["observed"]["path"]
        self.assertEqual("CA-C--golden.md", destination.name)
        self.assertEqual(before.content, atom_from_path(self.fixture.root, destination).content)
        self.assertIsNone(result["observed"]["atom_id"])


if __name__ == "__main__":
    unittest.main()
