"""Focused Unit-Gate phase admission tests over sealed package rows."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import PackageRow  # noqa: E402
from release_suite import _test_module_source_paths  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES, derive_test_phase_map_from_rows  # noqa: E402


UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_compilation.py"


def package_row(path: str, digest: str) -> PackageRow:
    return PackageRow(
        resource="FRAMEWORK_ENGINE",
        source_path=path,
        destination_path="FRAMEWORK_ENGINE/" + path.removeprefix("102_FRAMEWORK_ENGINE/"),
        sha256=digest,
        mode=0o644,
    )


class ReleaseSuitePhaseAdmissionTests(unittest.TestCase):
    """The Unit observer must consume only the sealed ``unit`` partition."""

    def rows(self) -> list[PackageRow]:
        # Deliberately unsorted: the shared projection, not fixture order,
        # defines both the phase rows and their digest.
        paths = (CANDIDATE_E2E_MODULES[1], UNIT_MODULE, CANDIDATE_E2E_MODULES[2], CANDIDATE_E2E_MODULES[0])
        return [package_row(path, f"{index + 1:064x}") for index, path in enumerate(paths)]

    def test_exact_three_e2e_rows_are_excluded_from_the_unit_module_set(self) -> None:
        rows = self.rows()
        phase_map = derive_test_phase_map_from_rows(rows)

        self.assertEqual((UNIT_MODULE,), phase_map.unit_paths)
        self.assertEqual(tuple(sorted(CANDIDATE_E2E_MODULES)), phase_map.candidate_e2e_paths)
        self.assertEqual((UNIT_MODULE,), _test_module_source_paths(rows))
        self.assertEqual(tuple(sorted(phase_map.rows)), phase_map.rows)

    def test_phase_map_digest_changes_when_one_sealed_module_digest_changes(self) -> None:
        rows = self.rows()
        original = derive_test_phase_map_from_rows(rows)
        changed = list(rows)
        changed[0] = changed[0].model_copy(update={"sha256": "f" * 64})

        self.assertNotEqual(original.sha256, derive_test_phase_map_from_rows(changed).sha256)

    def test_missing_or_duplicate_e2e_assignments_refuse_before_unit_admission(self) -> None:
        rows = self.rows()
        with self.assertRaises(ReleaseContractError) as missing:
            derive_test_phase_map_from_rows(rows[:-1])
        self.assertEqual("release-test-phase-e2e-set-invalid", missing.exception.code)

        duplicate = [*rows, rows[0].model_copy(update={"destination_path": "FRAMEWORK_ENGINE/duplicate.py"})]
        with self.assertRaises(ReleaseContractError) as repeated:
            derive_test_phase_map_from_rows(duplicate)
        self.assertEqual("release-test-phase-duplicate-module", repeated.exception.code)


if __name__ == "__main__":
    unittest.main()
