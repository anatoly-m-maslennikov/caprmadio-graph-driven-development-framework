"""Read-only proof that canonical compiled Methodology matches its source frontier.

This verifier deliberately does not invoke the compiler request adapter: it
replays the compiler's deterministic projection function in memory and proves
the already-present canonical role tree byte-for-byte.
"""

from __future__ import annotations

import hashlib
import importlib.util
import os
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

from release_contract import ReleaseContractError


COMPILER_ENTRYPOINT_RELATIVE = Path(
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/"
    "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
)
_COMPILER_PATH = Path(__file__).resolve().parents[1] / "COMPILE_APPLICABLE_METHODOLOGY" / "compile_applicable_methodology.py"
_SPEC = importlib.util.spec_from_file_location("_framework_currentness_compiler", _COMPILER_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - installation failure
    raise RuntimeError("Framework compiler currentness cannot load Methodology compiler")
_COMPILER = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _COMPILER
_SPEC.loader.exec_module(_COMPILER)


@dataclass(frozen=True)
class CanonicalCompilerCurrentness:
    """Sealed, read-only observation of the canonical compiled Methodology."""

    compiled_root: str
    source_root: str
    compiler_entrypoint: str
    compiler_entrypoint_sha256: str
    source_frontier_digest: str
    output_tree_digest: str
    output_plan_sha256: str
    source_snapshot: tuple[tuple[str, str], ...]


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _root(value: Path | str) -> Path:
    root = Path(value).resolve()
    if root.is_symlink() or not root.is_dir():
        raise _error("initial-project-invalid", "project root must be a regular directory")
    return root


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("initial-compiler-currentness-invalid", "compiled Methodology path escapes project root") from error


def _compiler_identity(root: Path) -> tuple[str, str]:
    declared = root / COMPILER_ENTRYPOINT_RELATIVE
    if declared.is_symlink() or not declared.is_file():
        raise _error("initial-compiler-entrypoint-missing", "canonical Methodology compiler entrypoint is missing")
    executing = _COMPILER_PATH.resolve()
    try:
        declared_bytes = declared.read_bytes()
        executing_bytes = executing.read_bytes()
    except OSError as error:
        raise _error("initial-compiler-entrypoint-missing", "canonical Methodology compiler entrypoint is unreadable") from error
    if declared_bytes != executing_bytes:
        raise _error("initial-compiler-identity-mismatch", "declared compiler bytes differ from the verifier compiler")
    return COMPILER_ENTRYPOINT_RELATIVE.as_posix(), _digest(executing_bytes)


def _safe_relative(value: object, *, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise _error("initial-compiler-control-invalid", f"{label} is missing")
    relative = Path(value)
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise _error("initial-compiler-control-invalid", f"{label} is unsafe")
    return relative


def _regular_ancestors(root: Path, relative: Path, *, label: str) -> Path:
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink() or (cursor.exists() and not cursor.is_dir()):
            raise _error("initial-compiler-control-unsafe", f"{label} has an unsafe ancestor")
    return cursor


def _regular_file(root: Path, relative: Path, *, label: str, required: bool) -> Path | None:
    path = root / relative
    _regular_ancestors(root, relative.parent, label=label)
    if not path.exists() and not path.is_symlink():
        if required:
            raise _error("initial-compiler-control-missing", f"{label} is missing")
        return None
    if path.is_symlink() or not path.is_file():
        raise _error("initial-compiler-control-unsafe", f"{label} must be a regular file")
    return path


def _preflight_control_carriers(root: Path) -> tuple[Path, Path | None]:
    """Validate every carrier used to resolve compiler places before compiler reads it."""

    settings_relative = Path(_COMPILER.SETTINGS_PATH)
    settings = _regular_file(root, settings_relative, label="Project Settings Carrier", required=True)
    assert settings is not None
    try:
        payload = tomllib.loads(settings.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("initial-compiler-control-invalid", "Project Settings Carrier is not valid TOML") from error
    raw_control = payload.get("paths", {}).get("control_root") if isinstance(payload.get("paths"), dict) else None
    control = _safe_relative(raw_control, label="configured control root")
    _regular_ancestors(root, control, label="configured control root")
    control_root = root / control
    if control_root.is_symlink() or not control_root.is_dir():
        raise _error("initial-compiler-control-unsafe", "configured control root is not a regular directory")
    structure = _regular_file(root, control / "project_structure.toml", label="Project Structure Carrier", required=False)
    return control, structure


def _preflight_framework_settings(root: Path, places: object) -> None:
    source = _safe_relative(places.source.as_posix(), label="configured Methodology source root")
    _regular_ancestors(root, source, label="configured Methodology source root")
    source_root = root / source
    if source_root.is_symlink() or not source_root.is_dir():
        raise _error("initial-compiler-control-unsafe", "configured Methodology source root is unsafe")
    for relative in _COMPILER.SETTINGS_FILENAMES:
        _regular_file(root, source / relative, label="Framework Settings Carrier", required=False)


def _expected_output(root: Path, places: object, candidates: list[object]) -> dict[str, bytes]:
    expected: dict[str, bytes] = {}
    output_root = root / places.output
    for candidate in candidates:
        source = root / candidate.source_path
        target_parent = output_root / candidate.role_directory
        relative_source = Path(os.path.relpath(source, start=target_parent)).as_posix()
        target = target_parent / candidate.basename
        relative_target = _relative(root, target)
        if relative_target in expected:
            raise _error("initial-compiler-output-collision", "canonical compiler output has duplicate target paths")
        try:
            expected[relative_target] = _COMPILER.projection_bytes(source.read_bytes(), relative_source, candidate)
        except _COMPILER.CompileError as error:
            raise _error("initial-compiler-currentness-invalid", str(error)) from error
    return expected


def _actual_output(root: Path, places: object) -> dict[str, bytes]:
    output_root = root / places.output
    actual: dict[str, bytes] = {}
    for _, role_directory in _COMPILER.ROLES:
        role_root = output_root / role_directory
        if role_root.is_symlink() or not role_root.is_dir():
            raise _error("initial-compiler-output-missing", "canonical compiled Methodology role directory is missing")
        for path in sorted(role_root.rglob("*")):
            if path.name == ".DS_Store" and path.is_file() and not path.is_symlink():
                continue
            if path.is_dir() and not path.is_symlink():
                continue
            if path.is_symlink() or not path.is_file() or path.suffix != ".md":
                raise _error("initial-compiler-output-invalid", "canonical compiled Methodology has an unsafe carrier")
            # ``stage_outputs`` creates regular projection carriers with the
            # repository's canonical non-executable file mode.  A mode drift
            # is not represented by the compiler tree digest, so reject it
            # explicitly rather than letting a later package inventory merely
            # inherit the altered permission.
            if path.stat().st_mode & 0o777 != 0o644:
                raise _error("initial-compiler-output-mode-mismatch", "canonical compiled Methodology carrier mode differs from compiler output")
            actual[_relative(root, path)] = path.read_bytes()
    return actual


def _tree_digest(records: dict[str, bytes]) -> str:
    payload = [
        {"path": path, "sha256": _digest(contents)}
        for path, contents in sorted(records.items())
    ]
    return _digest(_COMPILER.canonical_json(payload))


def verify_canonical_compiler_currentness(project_root: Path | str) -> CanonicalCompilerCurrentness:
    """Prove the existing canonical compiled tree is the current deterministic output.

    Conflict-free source state is mandatory.  A frontier with any conflict has
    no uniquely determined selected output absent separately governed approval
    evidence, so this verifier refuses rather than guessing.
    """

    root = _root(project_root)
    _preflight_control_carriers(root)
    entrypoint, entrypoint_sha256 = _compiler_identity(root)
    try:
        places = _COMPILER.methodology_paths(root)
        _preflight_framework_settings(root, places)
        report, selected, snapshot = _COMPILER.compile_report(root, places)
    except _COMPILER.CompileError as error:
        raise _error("initial-compiler-currentness-invalid", str(error)) from error
    if report.get("conflict_count") != 0 or report.get("unresolved_conflict_count") != 0 or report.get("can_apply") is not True:
        raise _error("initial-compiler-conflict-unresolved", "canonical compiled Methodology requires a complete conflict-free source frontier")
    if not _COMPILER.source_snapshot_is_current(root, snapshot, places):
        raise _error("initial-compiler-source-stale", "Methodology source frontier changed before compiled-output verification")
    expected = _expected_output(root, places, selected)
    try:
        _COMPILER.validate_existing_output_ownership(root / places.output)
        actual = _actual_output(root, places)
    except _COMPILER.CompileError as error:
        raise _error("initial-compiler-output-invalid", str(error)) from error
    if set(actual) != set(expected):
        raise _error("initial-compiler-output-pathset-mismatch", "canonical compiled Methodology path set differs from deterministic output")
    for path, payload in expected.items():
        if actual[path] != payload:
            raise _error("initial-compiler-output-bytes-mismatch", f"canonical compiled Methodology differs: {path}")
    expected_digest = _tree_digest(expected)
    try:
        actual_digest = _COMPILER.generated_tree_digest(root, places)
    except _COMPILER.CompileError as error:
        raise _error("initial-compiler-output-invalid", str(error)) from error
    if actual_digest != expected_digest:
        raise _error("initial-compiler-output-digest-mismatch", "canonical compiled Methodology digest differs from deterministic output")
    if not _COMPILER.source_snapshot_is_current(root, snapshot, places):
        raise _error("initial-compiler-source-stale", "Methodology source frontier changed during compiled-output verification")
    return CanonicalCompilerCurrentness(
        compiled_root=places.output.as_posix(),
        source_root=places.source.as_posix(),
        compiler_entrypoint=entrypoint,
        compiler_entrypoint_sha256=entrypoint_sha256,
        source_frontier_digest=str(report["source_frontier_digest"]),
        output_tree_digest=actual_digest,
        output_plan_sha256=_digest(_COMPILER.canonical_json(report["output_plan"])),
        source_snapshot=tuple(sorted(snapshot.items())),
    )
