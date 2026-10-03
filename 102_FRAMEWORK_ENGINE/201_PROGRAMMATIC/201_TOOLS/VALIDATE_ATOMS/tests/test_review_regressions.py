"""Failure evidence from independent review of the integrated implementation."""

from pathlib import Path
import sys
import tempfile
import os
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from validate_atoms_workers.authority import resolve_context  # noqa: E402
from validate_atoms_workers.assessment import apply_checks  # noqa: E402
from validate_atoms_workers.contracts import empty_report  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from validate_atoms_workers.projection import verify_projection  # noqa: E402
from validate_atoms_workers.read_io import ReadContext  # noqa: E402
from validate_atoms_workers.selection import matching_selectors, filter_candidate  # noqa: E402
from validate_atoms_workers.settings import CEILINGS  # noqa: E402


class ReviewRegressions(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(
            tempfile.mkdtemp(dir=HERE.parents[4] / ".caprmedio_tmp", prefix="validator-review-")
        )
        self.reader = ReadContext([str(self.root)], dict(CEILINGS))

    def test_context_gaps_are_not_mutated_between_carriers(self) -> None:
        context = resolve_context([])
        report = empty_report()
        report["coverage"]["gaps"].extend(context.gaps)
        for name in ("a.md", "b.md"):
            path = self.root / name
            parsed = parse_carrier(b"---\nversion: 1\n---\n# Summary\n", path)
            apply_checks(path, parsed, context, self.reader, report)
        self.assertTrue(all(gap["path"] is None for gap in context.gaps))
        targets = {gap["path"] for gap in report["coverage"]["gaps"]}
        self.assertIn(str(self.root / "a.md"), targets)
        self.assertIn(str(self.root / "b.md"), targets)

    def test_projection_never_removes_body_block(self) -> None:
        source = self.root / "source.md"
        raw = b"---\nprojection: {source_carrier_path: source.md}\n---\n# Summary\n"
        source.write_bytes(raw)
        bad = raw + b"projection:\n  body_text: removed\n"
        with self.assertRaises(ValueError):
            verify_projection(
                parse_carrier(bad, self.root / "copy.md"), self.root / "copy.md", self.reader, {}
            )

    def test_identity_selectors_do_not_coerce_boolean_versions(self) -> None:
        matches = matching_selectors(
            "/a.md", {"atom_id": "A", "version": True}, [{"atom_id": "A", "version": 1}]
        )
        self.assertEqual(matches, [])

    def test_tier_selection_does_not_coerce_floats(self) -> None:
        state, _ = filter_candidate(
            {"global_tier": 1.0}, {"global_tiers": [1], "atoms": [{"atom_id": "A"}]}, None, {}
        )
        self.assertEqual(state, "unresolved")

    def test_access_time_change_is_not_a_content_change(self) -> None:
        path = self.root / "a.md"
        path.write_text("same")
        real_fstat = os.fstat
        counter = 0

        def access_time_only(descriptor: int) -> SimpleNamespace:
            nonlocal counter
            counter += 1
            value = real_fstat(descriptor)
            fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns", "st_mode")
            data = {field: getattr(value, field) for field in fields}
            return SimpleNamespace(**data, st_atime=counter)

        with patch("validate_atoms_workers.read_io.os.fstat", side_effect=access_time_only):
            self.assertEqual(self.reader.read(path), b"same")

    def test_inventory_uses_directory_descriptors(self) -> None:
        (self.root / "a.md").write_text("x")
        real_scandir = os.scandir
        used: list[object] = []

        def checked_scandir(value: int) -> object:
            used.append(value)
            return real_scandir(value)

        with patch("validate_atoms_workers.read_io.os.scandir", side_effect=checked_scandir):
            self.reader.inventory(self.root)
        self.assertTrue(used)
        self.assertTrue(all(type(value) is int for value in used))


if __name__ == "__main__":
    unittest.main()
