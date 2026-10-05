"""Pure phase projection for the sealed candidate test-module inventory."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Literal

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json


Phase = Literal["unit", "candidate_e2e"]
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
CANDIDATE_E2E_MODULES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py",
)


@dataclass(frozen=True)
class ReleaseTestPhaseMap:
    """Exact phase classification of all sealed ``test_*.py`` source rows."""

    rows: tuple[tuple[str, str, Phase], ...]
    sha256: str
    unit_paths: tuple[str, ...]
    candidate_e2e_paths: tuple[str, ...]


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _is_test_module(path: object) -> bool:
    return isinstance(path, str) and PurePosixPath(path).name.startswith("test_") and path.endswith(".py")


def derive_test_phase_map(candidate: ValidatedCandidate) -> ReleaseTestPhaseMap:
    """Classify only sealed test-module rows; never discover from the filesystem."""

    manifest = getattr(candidate, "manifest", None)
    inventory = getattr(manifest, "source_inventory_rows", None)
    if not isinstance(inventory, list):
        raise _error("release-test-phase-inventory-invalid", "candidate has no sealed source inventory rows")

    modules: dict[str, str] = {}
    for row in inventory:
        path = getattr(row, "source_path", None)
        if isinstance(row, dict):
            path = row.get("source_path")
            digest = row.get("source_sha256")
        else:
            digest = getattr(row, "source_sha256", None)
        if not _is_test_module(path):
            continue
        if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
            raise _error("release-test-phase-row-invalid", "sealed test module has an invalid source digest")
        if path in modules:
            raise _error("release-test-phase-duplicate-module", "sealed test module appears more than once")
        modules[path] = digest

    present_e2e = set(modules).intersection(CANDIDATE_E2E_MODULES)
    if present_e2e != set(CANDIDATE_E2E_MODULES):
        raise _error("release-test-phase-e2e-set-invalid", "sealed inventory lacks the exact declared candidate E2E harness set")

    rows: tuple[tuple[str, str, Phase], ...] = tuple(
        (path, digest, "candidate_e2e" if path in CANDIDATE_E2E_MODULES else "unit")
        for path, digest in sorted(modules.items())
    )
    unit_paths = tuple(path for path, _, phase in rows if phase == "unit")
    candidate_e2e_paths = tuple(path for path, _, phase in rows if phase == "candidate_e2e")
    return ReleaseTestPhaseMap(
        rows=rows,
        sha256=hashlib.sha256(canonical_json(list(rows))).hexdigest(),
        unit_paths=unit_paths,
        candidate_e2e_paths=candidate_e2e_paths,
    )


__all__ = ["CANDIDATE_E2E_MODULES", "ReleaseTestPhaseMap", "derive_test_phase_map"]
