"""Focused coverage for the finite graph-authority refresh closure."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch


TESTS = Path(__file__).resolve().parent
TOOL = TESTS.parent
PROJECT = TOOL.parents[3]
sys.path.insert(0, str(TOOL))

from validate_atoms_workers.graph_authority_refresh import (  # noqa: E402
    APPROVED_GRAPH_AUTHORITY_IDS,
    refresh_entries,
    verify_entries,
)


GRAPH_AUTHORITY = TOOL / "validate_atoms_workers" / "graph_authority.json"


class GraphAuthorityRefreshTests(unittest.TestCase):
    @staticmethod
    def _entries() -> dict[str, object]:
        return {
            atom_id: {
                "version": 1,
                "sha256": "0" * 64,
                "source_path": "stale/" + atom_id + ".md",
            }
            for atom_id in APPROVED_GRAPH_AUTHORITY_IDS
        }

    def test_committed_authority_is_the_exact_current_finite_closure(self) -> None:
        entries = json.loads(GRAPH_AUTHORITY.read_text(encoding="utf-8"))["sources"]
        before = copy.deepcopy(entries)

        self.assertEqual(refresh_entries(PROJECT, entries), entries)
        verify_entries(PROJECT, entries)
        self.assertEqual(
            {key: entries[key] for key in entries if key not in APPROVED_GRAPH_AUTHORITY_IDS},
            {key: before[key] for key in before if key not in APPROVED_GRAPH_AUTHORITY_IDS},
        )

    def test_stale_pin_is_refused(self) -> None:
        entries = json.loads(GRAPH_AUTHORITY.read_text(encoding="utf-8"))["sources"]
        entries["CA-D-268"]["sha256"] = "0" * 64

        with self.assertRaisesRegex(ValueError, "graph authority source is stale: CA-D-268"):
            verify_entries(PROJECT, entries)

    def test_missing_active_source_is_refused(self) -> None:
        with patch(
            "validate_atoms_workers.graph_authority_refresh._source_roots", return_value=()
        ):
            with self.assertRaisesRegex(ValueError, "active source is absent: CA-D-268"):
                refresh_entries(PROJECT, self._entries())

    def test_ambiguous_active_source_is_refused(self) -> None:
        source_root = Mock()
        source_root.glob.return_value = [Path("first.md"), Path("second.md")]
        parsed = SimpleNamespace(
            metadata={"atom_id": "CA-D-268", "status": "Active", "version": 1}
        )
        with (
            patch(
                "validate_atoms_workers.graph_authority_refresh._source_roots",
                return_value=(source_root,),
            ),
            patch(
                "validate_atoms_workers.graph_authority_refresh.parse_carrier", return_value=parsed
            ),
            patch.object(Path, "is_symlink", return_value=False),
            patch.object(Path, "is_file", return_value=True),
            patch.object(Path, "read_bytes", return_value=b"fixture"),
        ):
            with self.assertRaisesRegex(ValueError, "active source is ambiguous: CA-D-268"):
                refresh_entries(PROJECT, self._entries())


if __name__ == "__main__":
    unittest.main()
