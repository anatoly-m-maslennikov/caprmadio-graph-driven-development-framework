"""Project boundary tests independent of Git and ambient checkout state."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from project_runtime import TemporaryBoundaryError, repository_root


class ProjectRuntimeBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        self.reference = self.root / "delivered" / "nested"
        self.reference.mkdir(parents=True)

    def marker(self, name):
        path = self.control / name
        path.write_text("# authoritative fixture carrier\n")
        return path

    def test_gitless_project_requires_both_authoritative_carriers(self):
        self.marker("caprmedio_project_settings.toml")
        with self.assertRaises(TemporaryBoundaryError):
            repository_root(self.reference)
        self.marker("project_structure.toml")
        self.assertEqual(repository_root(self.reference), self.root)

    def test_runtime_or_scratch_folder_does_not_identify_a_project(self):
        (self.root / ".caprmedio_runtime").mkdir()
        (self.root / ".caprmedio_tmp").mkdir()
        with self.assertRaises(TemporaryBoundaryError):
            repository_root(self.reference)

    def test_symlinked_control_or_carrier_is_not_a_project_marker(self):
        self.marker("caprmedio_project_settings.toml")
        target = self.root / "structure.toml"
        target.write_text("# fixture\n")
        (self.control / "project_structure.toml").symlink_to(target)
        with self.assertRaises(TemporaryBoundaryError):
            repository_root(self.reference)

    def test_checkout_marker_remains_supported(self):
        (self.root / ".git").mkdir()
        self.assertEqual(repository_root(self.reference), self.root)
