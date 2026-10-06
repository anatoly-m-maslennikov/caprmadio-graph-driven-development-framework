"""Pure phase projection for the sealed candidate test-module inventory."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Iterable, Literal

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


def _row_value(row: object, name: str) -> object:
    if isinstance(row, dict):
        return row.get(name)
    return getattr(row, name, None)


def derive_test_phase_map_from_rows(rows: Iterable[object]) -> ReleaseTestPhaseMap:
    """Classify sealed test rows supplied by either inventory or package bindings.

    Candidate inventory rows call their digest ``source_sha256`` whereas the
    schema-2 package envelope calls the same sealed value ``sha256``.  This
    projection deliberately accepts only those two already-attested carriers;
    it never discovers modules from the filesystem.
    """

    modules: dict[str, str] = {}
    try:
        iterator = iter(rows)
    except TypeError as error:
        raise _error("release-test-phase-inventory-invalid", "sealed test rows are not iterable") from error
    for row in iterator:
        path = _row_value(row, "source_path")
        digest = _row_value(row, "sha256")
        if digest is None:
            digest = _row_value(row, "source_sha256")
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


def derive_test_phase_map(candidate: ValidatedCandidate) -> ReleaseTestPhaseMap:
    """Classify only sealed candidate-inventory rows; never discover files."""

    manifest = getattr(candidate, "manifest", None)
    inventory = getattr(manifest, "source_inventory_rows", None)
    if not isinstance(inventory, list):
        raise _error("release-test-phase-inventory-invalid", "candidate has no sealed source inventory rows")
    return derive_test_phase_map_from_rows(inventory)


__all__ = [
    "CANDIDATE_E2E_MODULES",
    "ReleaseTestPhaseMap",
    "derive_test_phase_map",
    "derive_test_phase_map_from_rows",
]
