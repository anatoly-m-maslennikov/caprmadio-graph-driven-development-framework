"""Pure sealed-inventory phase-map coverage."""

from __future__ import annotations

import hashlib
import sys
import unittest
from types import SimpleNamespace
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_test_phases import (  # noqa: E402
    CANDIDATE_E2E_MODULES,
    derive_test_phase_map,
)


def _candidate(rows: list[dict[str, object]]) -> object:
    return SimpleNamespace(manifest=SimpleNamespace(source_inventory_rows=rows))


def _row(path: str, digest: str) -> dict[str, object]:
    return {"resource": "FRAMEWORK_ENGINE", "source_path": path, "source_sha256": digest,
            "destination_path": f"FRAMEWORK_ENGINE/{path.removeprefix('102_FRAMEWORK_ENGINE/')}", "source_mode": 0o644}


class ReleaseTestPhaseMapTests(unittest.TestCase):
    def test_projects_all_sealed_test_modules_once_with_exact_three_candidate_e2e(self) -> None:
        paths = [
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/tests/test_release_actions.py",
            *CANDIDATE_E2E_MODULES,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/fixture_test_helper.py",
        ]
        rows = [_row(path, hashlib.sha256(path.encode()).hexdigest()) for path in paths]
        phase_map = derive_test_phase_map(_candidate(rows))

        expected = tuple(sorted((path, hashlib.sha256(path.encode()).hexdigest(),
                                 "candidate_e2e" if path in CANDIDATE_E2E_MODULES else "unit")
                                for path in paths if Path(path).name.startswith("test_")))
        self.assertEqual(phase_map.rows, expected)
        self.assertEqual(phase_map.candidate_e2e_paths, tuple(sorted(CANDIDATE_E2E_MODULES)))
        self.assertEqual(phase_map.unit_paths, (paths[0],))
        self.assertEqual(phase_map.sha256, hashlib.sha256(canonical_json(list(expected))).hexdigest())

    def test_refuses_duplicate_or_missing_declared_candidate_e2e(self) -> None:
        rows = [_row(path, hashlib.sha256(path.encode()).hexdigest()) for path in CANDIDATE_E2E_MODULES]
        rows.append(dict(rows[0]))
        with self.assertRaises(ReleaseContractError) as duplicate:
            derive_test_phase_map(_candidate(rows))
        self.assertEqual(duplicate.exception.code, "release-test-phase-duplicate-module")

        with self.assertRaises(ReleaseContractError) as missing:
            derive_test_phase_map(_candidate(rows[1:3]))
        self.assertEqual(missing.exception.code, "release-test-phase-e2e-set-invalid")

    def test_refuses_invalid_sealed_test_hash(self) -> None:
        rows = [_row(path, "x" * 64) for path in CANDIDATE_E2E_MODULES]
        with self.assertRaises(ReleaseContractError) as rejected:
            derive_test_phase_map(_candidate(rows))
        self.assertEqual(rejected.exception.code, "release-test-phase-row-invalid")
