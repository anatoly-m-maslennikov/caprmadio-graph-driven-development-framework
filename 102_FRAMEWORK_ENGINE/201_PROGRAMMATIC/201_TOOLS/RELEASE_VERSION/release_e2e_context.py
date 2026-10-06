"""Closed environment adapter for the private candidate Docker E2E driver.

The E2E driver is intentionally not a general test runner.  Its parent writes
one canonical context document into a per-attempt scratch directory, passes
only that document's path and the candidate immutable image identity through
the environment, and supplies the fixed argv from ``release_e2e_bindings``.
Keeping this parsing boundary here makes the executable driver testable without
letting a caller select a workspace, image, or command.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Mapping


CONTEXT_ENVIRONMENT_VARIABLE = "CAPRMEDIO_RELEASE_E2E_CONTEXT"
CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE = "CAPRMEDIO_CANDIDATE_IMAGE_DIGEST"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_IMAGE_ID = re.compile(r"^sha256:[0-9a-f]{64}$")
_MAX_CONTEXT_BYTES = 256 * 1024
_FIXED_HARNESS_SOURCES = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py",
)
_DOCKER_OPTINS = (("CAPRMEDIO_DOCKER_E2E", "1"),)


class ReleaseE2EContextError(ValueError):
    """A deterministic refusal of an unsealed E2E driver environment."""


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ReleaseE2EContextError("context JSON has a duplicate key")
        result[key] = value
    return result


def _require_sha256(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ReleaseE2EContextError(f"{label} must be a lowercase SHA-256")
    return value


def _require_image(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _IMAGE_ID.fullmatch(value) is None:
        raise ReleaseE2EContextError(f"{label} must be an immutable image ID")
    return value


def _relative(value: object, *, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\\" in value:
        raise ReleaseE2EContextError(f"{label} must be a normalized relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts) or path.as_posix() != value:
        raise ReleaseE2EContextError(f"{label} must be a normalized relative path")
    return value


def _absolute_directory(value: object, *, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\x00" in value:
        raise ReleaseE2EContextError(f"{label} must be an absolute directory")
    path = Path(value)
    if not path.is_absolute() or not path.is_dir():
        raise ReleaseE2EContextError(f"{label} must name one existing non-symlink directory")
    cursor = path
    while cursor != cursor.parent:
        if cursor.is_symlink():
            raise ReleaseE2EContextError(f"{label} must name one existing non-symlink directory")
        cursor = cursor.parent
    return str(path.resolve())


def _strict_child(child: str, parent: str, *, label: str) -> None:
    """Require a dedicated descendant instead of accepting its authority root."""

    try:
        relative = Path(child).relative_to(Path(parent))
    except ValueError as error:
        raise ReleaseE2EContextError(f"{label} is outside its sealed parent") from error
    if relative == Path("."):
        raise ReleaseE2EContextError(f"{label} must be a strict child of its sealed parent")


@dataclass(frozen=True)
class ReleaseE2EHarness:
    """One exact driver phase, retained in the context for driver admission."""

    source_path: str
    start_directory: str
    pattern: str
    junit_path: str
    context_optins: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class ReleaseE2EContext:
    """The complete closed context available to ``run_release_e2e.py``."""

    source_root: str
    scratch_root: str
    report_root: str
    candidate_snapshot_manifest_sha256: str
    candidate_image_digest: str
    grammar_sha256: str
    phase_map_sha256: str
    fixed_harnesses: tuple[ReleaseE2EHarness, ...]
    phase_bindings: tuple[str, ...]

    @property
    def image_id(self) -> str:
        """An explicit immutable-image alias for small driver adapters."""

        return self.candidate_image_digest

    @property
    def harnesses(self) -> tuple[ReleaseE2EHarness, ...]:
        return self.fixed_harnesses


def _parse_harnesses(value: object, *, report_root: Path, candidate_image: str) -> tuple[ReleaseE2EHarness, ...]:
    if not isinstance(value, list) or len(value) != 3:
        raise ReleaseE2EContextError("context must contain exactly three fixed harnesses")
    parsed: list[ReleaseE2EHarness] = []
    seen: set[tuple[str, str]] = set()
    for index, item in enumerate(value):
        if not isinstance(item, dict) or set(item) != {
            "source_path", "start_directory", "pattern", "junit_path", "context_optins",
        }:
            raise ReleaseE2EContextError("harness context has an unsupported shape")
        source_path = _relative(item["source_path"], label=f"harness {index} source_path")
        start_directory = _relative(item["start_directory"], label=f"harness {index} start_directory")
        pattern = item["pattern"]
        if not isinstance(pattern, str) or not pattern.startswith("test_") or "/" in pattern or "\\" in pattern:
            raise ReleaseE2EContextError("harness pattern is invalid")
        junit_raw = item["junit_path"]
        if not isinstance(junit_raw, str) or not junit_raw or "\x00" in junit_raw:
            raise ReleaseE2EContextError("harness JUnit path is invalid")
        junit_path = Path(junit_raw)
        if not junit_path.is_absolute():
            raise ReleaseE2EContextError("harness JUnit path must be absolute")
        try:
            junit_path.resolve(strict=False).relative_to(report_root)
        except ValueError as error:
            raise ReleaseE2EContextError("harness JUnit path is outside the sealed report root") from error
        if junit_path.name != f"{pattern}.xml":
            raise ReleaseE2EContextError("harness JUnit filename does not bind its pattern")
        optins = item["context_optins"]
        if not isinstance(optins, dict) or any(
            not isinstance(key, str) or not isinstance(item_value, str)
            for key, item_value in optins.items()
        ):
            raise ReleaseE2EContextError("harness opt-ins are invalid")
        observed_optins = tuple(sorted(optins.items()))
        expected_optins = (
            _DOCKER_OPTINS if source_path != _FIXED_HARNESS_SOURCES[2] else (
                ("CAPRMEDIO_DOCKER_QUERY_E2E", "1"),
                ("CAPRMEDIO_DOCKER_QUERY_IMAGE", candidate_image),
                ("CAPRMEDIO_IMAGE", candidate_image),
            )
        )
        if observed_optins != expected_optins:
            raise ReleaseE2EContextError("harness opt-ins do not match fixed image-bound admission")
        identity = (source_path, pattern)
        if identity in seen:
            raise ReleaseE2EContextError("harness context repeats a phase")
        seen.add(identity)
        parsed.append(ReleaseE2EHarness(
            source_path, start_directory, pattern, str(junit_path.resolve(strict=False)),
            observed_optins,
        ))
    if tuple(harness.source_path for harness in parsed) != _FIXED_HARNESS_SOURCES:
        raise ReleaseE2EContextError("context harness set is not the three fixed E2E sources")
    return tuple(parsed)


def load_release_e2e_context(environment=None) -> ReleaseE2EContext:
    """Load the only two driver inputs from a supplied environment mapping.

    ``environment`` is deliberately a small test seam.  Production passes no
    value, making the two declared E2E environment variables the sole ambient
    inputs.  The context itself must be canonical bytes in a regular file.
    """

    values: Mapping[str, str] = os.environ if environment is None else environment
    if not isinstance(values, Mapping):
        raise ReleaseE2EContextError("environment must be a mapping")
    context_name = values.get(CONTEXT_ENVIRONMENT_VARIABLE)
    expected_image = values.get(CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE)
    if not isinstance(context_name, str) or not context_name or "\x00" in context_name:
        raise ReleaseE2EContextError("missing sealed E2E context path")
    expected_image = _require_image(expected_image, label=CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE)
    context_path = Path(context_name)
    if not context_path.is_absolute() or context_path.is_symlink() or not context_path.is_file():
        raise ReleaseE2EContextError("sealed E2E context must be one regular absolute file")
    if context_path.stat().st_size > _MAX_CONTEXT_BYTES:
        raise ReleaseE2EContextError("sealed E2E context is too large")
    payload = context_path.read_bytes()
    try:
        raw = json.loads(payload.decode("utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, ReleaseE2EContextError) as error:
        raise ReleaseE2EContextError("sealed E2E context is not canonical JSON") from error
    if not isinstance(raw, dict) or _canonical_json(raw) != payload:
        raise ReleaseE2EContextError("sealed E2E context is not canonical JSON")
    required = {
        "schema_version", "source_root", "scratch_root", "report_root",
        "candidate_snapshot_manifest_sha256", "candidate_image_digest",
        "grammar_sha256", "phase_map_sha256", "fixed_harnesses", "phase_bindings",
    }
    if set(raw) != required or raw.get("schema_version") != 1:
        raise ReleaseE2EContextError("sealed E2E context has an unsupported schema")
    source_root = _absolute_directory(raw["source_root"], label="source_root")
    scratch_root = _absolute_directory(raw["scratch_root"], label="scratch_root")
    report_root = _absolute_directory(raw["report_root"], label="report_root")
    _strict_child(scratch_root, source_root, label="scratch_root")
    _strict_child(report_root, scratch_root, label="report_root")
    try:
        context_path.resolve(strict=True).relative_to(Path(scratch_root))
    except ValueError as error:
        raise ReleaseE2EContextError("sealed E2E context is outside the executor-owned scratch root") from error
    candidate_image = _require_image(raw["candidate_image_digest"], label="candidate_image_digest")
    if candidate_image != expected_image:
        raise ReleaseE2EContextError("candidate image environment differs from sealed context")
    fixed_harnesses = _parse_harnesses(
        raw["fixed_harnesses"], report_root=Path(report_root), candidate_image=candidate_image,
    )
    phase_bindings = raw["phase_bindings"]
    if (not isinstance(phase_bindings, list) or len(phase_bindings) != 4
            or any(not isinstance(value, str) or not value for value in phase_bindings)
            or len(set(phase_bindings)) != len(phase_bindings)):
        raise ReleaseE2EContextError("sealed E2E phase bindings are invalid")
    expected_bindings = ("image-inspect", *(harness.pattern for harness in fixed_harnesses))
    if tuple(phase_bindings) != expected_bindings:
        raise ReleaseE2EContextError("sealed E2E phase bindings do not match fixed harnesses")
    return ReleaseE2EContext(
        source_root=source_root,
        scratch_root=scratch_root,
        report_root=report_root,
        candidate_snapshot_manifest_sha256=_require_sha256(
            raw["candidate_snapshot_manifest_sha256"], label="candidate_snapshot_manifest_sha256",
        ),
        candidate_image_digest=candidate_image,
        grammar_sha256=_require_sha256(raw["grammar_sha256"], label="grammar_sha256"),
        phase_map_sha256=_require_sha256(raw["phase_map_sha256"], label="phase_map_sha256"),
        fixed_harnesses=fixed_harnesses,
        phase_bindings=tuple(phase_bindings),
    )


def context_sha256(context: ReleaseE2EContext) -> str:
    """Return a diagnostic-only digest of the fixed typed driver context."""

    return hashlib.sha256(_canonical_json({
        "source_root": context.source_root,
        "scratch_root": context.scratch_root,
        "report_root": context.report_root,
        "candidate_snapshot_manifest_sha256": context.candidate_snapshot_manifest_sha256,
        "candidate_image_digest": context.candidate_image_digest,
        "grammar_sha256": context.grammar_sha256,
        "phase_map_sha256": context.phase_map_sha256,
        "fixed_harnesses": [
            {
                "source_path": harness.source_path,
                "start_directory": harness.start_directory,
                "pattern": harness.pattern,
                "junit_path": harness.junit_path,
                "context_optins": dict(harness.context_optins),
            }
            for harness in context.fixed_harnesses
        ],
        "phase_bindings": list(context.phase_bindings),
    })).hexdigest()


__all__ = [
    "CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE",
    "CONTEXT_ENVIRONMENT_VARIABLE",
    "ReleaseE2EContext",
    "ReleaseE2EContextError",
    "ReleaseE2EHarness",
    "context_sha256",
    "load_release_e2e_context",
]
