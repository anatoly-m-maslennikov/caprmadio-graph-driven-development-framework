"""Synthetic contracts for the bounded proposed-reference inventory."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
import warnings
from pathlib import Path
from unittest.mock import patch


VALIDATE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VALIDATE))

from validate_atoms_workers.proposed_references import (  # noqa: E402
    ProposedReferenceError,
    inventory_proposed_references,
)


class ProposedReferenceInventoryTest(unittest.TestCase):
    def setUp(self) -> None:
        parent = Path(__file__).resolve().parents[5] / ".caprmedio_tmp"
        parent.mkdir(exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="proposed-references-", dir=parent))
        (self.root / "authority").mkdir(parents=True)
        self.structure = {"scope_units": [{"authority_path": "authority"}]}

    def tearDown(self) -> None:
        try:
            for path in sorted(self.root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
                if path.is_file() or path.is_symlink():
                    path.unlink()
                else:
                    path.rmdir()
            self.root.rmdir()
        except PermissionError:
            warnings.warn(f"Host denied temporary fixture cleanup; retained {self.root}", RuntimeWarning)

    def _carrier(
        self, relative: str, atom_id: str, *, status: str = "Active", version: int = 1,
        role: str = "Action", parent: str | None = None,
    ) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        relation = "[]" if parent is None else f"[{parent}]"
        path.write_text(
            "---\n"
            f"atom_id: {atom_id}\ncontent_role: {role}\nstatus: {status}\nversion: {version}\n"
            "relations:\n"
            f"  is_decomposition_of: {relation}\n"
            "---\n# carrier\n",
            encoding="utf-8",
        )
        return path

    def test_direct_targets_are_exact_and_projection_copy_is_excluded(self) -> None:
        source = self._carrier("authority/current.md", "CA-O-001", version=7)
        self._carrier(
            "authority/_projection/copy.md", "CA-O-001", version=99,
        )

        result = inventory_proposed_references(self.root, self.structure, ["CA-O-001"])

        self.assertEqual(1, len(result.direct_targets))
        target = result.direct_targets[0]
        self.assertEqual("CA-O-001", target.atom_id)
        self.assertEqual("Active", target.status)
        self.assertEqual(7, target.version)
        self.assertEqual("authority/current.md", target.path)
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), target.sha256)
        self.assertEqual("CA-O-001", target.metadata["atom_id"])
        self.assertEqual((), result.plan_parent_closure)

    def test_named_nonactive_archive_refuses_instead_of_satisfying_target(self) -> None:
        self._carrier("authority/archive/old.md", "CA-O-002", status="Done")

        with self.assertRaisesRegex(ProposedReferenceError, "inactive or archived"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-002"])

    def test_duplicate_active_target_and_missing_target_fail_closed(self) -> None:
        self._carrier("authority/one.md", "CA-O-003")
        self._carrier("authority/two.md", "CA-O-003")
        with self.assertRaisesRegex(ProposedReferenceError, "ambiguous"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-003"])
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-404"])

    def test_nonpositive_target_versions_fail_closed(self) -> None:
        path = self._carrier("authority/version.md", "CA-O-004", version=0)
        with self.assertRaisesRegex(ProposedReferenceError, "identity, status, or version"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-004"])
        path.unlink()
        self._carrier("authority/version.md", "CA-O-004", version=-1)
        with self.assertRaisesRegex(ProposedReferenceError, "identity, status, or version"):
            inventory_proposed_references(self.root, self.structure, ["CA-O-004"])

    def test_nested_plan_requires_actual_authenticated_parent_chain(self) -> None:
        root_parent = self._carrier(
            "authority/CA-P-ROOT--root.md", "CA-P-ROOT", role="Plan",
        )
        parent = self._carrier(
            "authority/CA-P-ROOT--root/CA-P-PARENT--parent.md",
            "CA-P-PARENT", role="Plan", parent="CA-P-ROOT",
        )
        candidate_path = "authority/CA-P-ROOT--root/CA-P-PARENT--parent/child.md"
        candidate = {
            "content_role": "Plan",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }

        result = inventory_proposed_references(
            self.root, self.structure, ["CA-P-PARENT"],
            candidate_metadata=candidate, candidate_path=candidate_path,
        )

        self.assertEqual(["CA-P-PARENT"], [item.atom_id for item in result.direct_targets])
        self.assertEqual(["CA-P-PARENT", "CA-P-ROOT"], [item.atom_id for item in result.plan_parent_closure])
        self.assertEqual(root_parent.name, Path(result.plan_parent_closure[1].path).name)
        self.assertEqual(parent.name, Path(result.plan_parent_closure[0].path).name)

    def test_nested_plan_rejects_off_frontier_lookalike_parent_directory(self) -> None:
        self._carrier(
            "authority/authoritative-parent/CA-P-PARENT--parent.md", "CA-P-PARENT", role="Plan",
        )
        candidate = {
            "content_role": "Plan",
            "relations": {"is_decomposition_of": ["CA-P-PARENT"]},
        }

        with self.assertRaisesRegex(ProposedReferenceError, "authenticated Markdown parent carrier"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-PARENT"],
                candidate_metadata=candidate,
                candidate_path="untrusted/CA-P-PARENT--parent/child.md",
            )

    def test_nested_plan_cycle_wrong_parent_path_and_changed_frontier_fail_closed(self) -> None:
        self._carrier(
            "authority/CA-P-A--a/CA-P-B--b.md", "CA-P-B", role="Plan", parent="CA-P-A",
        )
        self._carrier(
            "authority/CA-P-A--a.md", "CA-P-A", role="Plan", parent="CA-P-B",
        )
        candidate = {"content_role": "Plan", "relations": {"is_decomposition_of": ["CA-P-A"]}}
        with self.assertRaisesRegex(ProposedReferenceError, "cycle"):
            inventory_proposed_references(
                self.root, self.structure, ["CA-P-A"], candidate_metadata=candidate,
                candidate_path="authority/CA-P-A--a/child.md",
            )

        self._carrier("authority/plain.md", "CA-O-005")
        with patch("validate_atoms_workers.proposed_references.ReadContext.currentness", return_value={"state": "changed"}):
            with self.assertRaisesRegex(ProposedReferenceError, "changed"):
                inventory_proposed_references(self.root, self.structure, ["CA-O-005"])


if __name__ == "__main__":
    unittest.main()
