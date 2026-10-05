"""Child-only Release Methodology rendering from the existing compiler primitives."""

from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import sys
import tempfile
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Mapping

from release_contract import CandidateBuildRequest, ReleaseContractError, ValidatedCandidate, canonical_json
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE,
    COMPILER_ENTRYPOINT_RELATIVE,
    DERIVED_SOURCE_COPY_RELATIVE,
    MATERIALIZED_RELATIVE,
    CompilerEntrypoint,
    CompilerSuccessEvidence,
    SealedCandidateCompilation,
    build_validated_candidate,
    seal_candidate_compilation,
    tree_sha256,
    validate_source_copy,
)


CHILD_MANIFEST_NAME = "_release_manifest.json"
CHILD_MANIFEST_SCHEMA = "caprmedio.release_version.child_materialization.v1"
PLACEHOLDER_COMPONENT = "p" * 64
_COMPILER_PATH = Path(__file__).resolve().parents[1] / "COMPILE_APPLICABLE_METHODOLOGY" / "compile_applicable_methodology.py"
EXECUTING_COMPILER_PATH = _COMPILER_PATH.resolve()
_SPEC = importlib.util.spec_from_file_location("_release_version_compiler", _COMPILER_PATH)
if _SPEC is None or _SPEC.loader is None:  # pragma: no cover - installation failure
    raise RuntimeError("Release compiler cannot load the selected Methodology compiler")
_COMPILER = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _COMPILER
_SPEC.loader.exec_module(_COMPILER)


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _root(value: Path | str) -> Path:
    root = Path(value).resolve()
    if not root.is_dir():
        raise _error("release-project-missing", "release project root is missing")
    return root


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("release-path-unsafe", "release compiler path escapes project") from error


def _compiler_entrypoint(root: Path) -> CompilerEntrypoint:
    path = root / COMPILER_ENTRYPOINT_RELATIVE
    if path.is_symlink() or not path.is_file():
        raise _error("release-compiler-entrypoint-missing", "selected compiler entrypoint is missing")
    declared_bytes = path.read_bytes()
    executing_bytes = EXECUTING_COMPILER_PATH.read_bytes()
    if declared_bytes != executing_bytes:
        raise _error(
            "release-compiler-identity-mismatch",
            "declared compiler bytes do not match the compiler module executing this render",
        )
    return CompilerEntrypoint(path=COMPILER_ENTRYPOINT_RELATIVE, sha256=_digest(executing_bytes))


def _mkdir_safe(root: Path, relative: str) -> Path:
    """Create one descendant while refusing every existing symlink component."""

    current = root
    for component in Path(relative).parts:
        current = current / component
        if os.path.lexists(current):
            if current.is_symlink() or not current.is_dir():
                raise _error("release-materialization-path-unsafe", "child materialization has an unsafe existing path component")
        else:
            current.mkdir()
    return current


def _child_tree_digest(files: Mapping[str, bytes]) -> str:
    digest = hashlib.sha256()
    for relative, data in sorted(files.items()):
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def _child_manifest_bytes(
    *, candidate_release: str, compiler: CompilerEntrypoint, canonical_source_digest: str,
    frontier_digest: str, derived_copy_digest: str, nested_digest: str,
    output_files: Mapping[str, bytes],
) -> bytes:
    rows = [{"path": path, "sha256": _digest(data)} for path, data in sorted(output_files.items())]
    return canonical_json(
        {
            "schema": CHILD_MANIFEST_SCHEMA,
            "candidate_release": candidate_release,
            "compiler_entrypoint_path": compiler.path,
            "compiler_entrypoint_sha256": compiler.sha256,
            "canonical_source_snapshot_digest": canonical_source_digest,
            "compiler_frontier_digest": frontier_digest,
            "actual_derived_source_copy_sha256": derived_copy_digest,
            "nested_source_recursive_sha256_before": nested_digest,
            "nested_source_recursive_sha256_after": nested_digest,
            "output_rows": rows,
        }
    )


def _render_outputs(
    root: Path, candidates: list[Any], source_root: Path, child_root: Path, *, content_root: Path | None = None,
) -> dict[str, bytes]:
    outputs: dict[str, bytes] = {}
    for candidate in candidates:
        source = root / candidate.source_path
        if not source.is_relative_to(source_root):
            raise _error("release-compiler-source-invalid", f"selected source is outside admitted root: {candidate.source_path}")
        source_bytes_path = source if content_root is None else content_root / source.relative_to(source_root)
        if not source_bytes_path.is_file() or source_bytes_path.is_symlink():
            raise _error("release-compiler-source-invalid", f"selected source bytes are missing: {candidate.source_path}")
        target = child_root / candidate.role_directory / candidate.basename
        relative_source = Path(os.path.relpath(source, start=target.parent)).as_posix()
        rendered = _COMPILER.projection_bytes(source_bytes_path.read_bytes(), relative_source, candidate)
        child_relative = target.relative_to(child_root).as_posix()
        if child_relative == CHILD_MANIFEST_NAME or child_relative in outputs:
            raise _error("release-compiler-output-invalid", "selected compiler output has an unsafe collision")
        outputs[child_relative] = rendered
    if not outputs:
        raise _error("release-compiler-output-empty", "selected compiler rendered no child output")
    return outputs


def _report(root: Path, source_relative: str, output_relative: str) -> tuple[dict[str, Any], list[Any]]:
    canonical = _COMPILER.methodology_paths(root)
    places = _COMPILER.MethodologyPaths(
        source=Path(source_relative), output=Path(output_relative),
        structure_sha256=canonical.structure_sha256, control_root=canonical.control_root,
    )
    report, selected, _snapshot = _COMPILER.compile_report(root, places)
    if not report.get("can_apply"):
        raise _error("release-compiler-blocked", "selected compiler report has diagnostics or unresolved conflicts")
    return report, selected


def _canonical_frontier_from_copied_candidates(candidates: list[Any]) -> str:
    """Map copied-source paths back to their canonical counterparts for D566."""

    copied_root = Path(DERIVED_SOURCE_COPY_RELATIVE)
    canonical_root = Path(CANONICAL_SOURCE_RELATIVE)
    mapped: list[Any] = []
    for candidate in candidates:
        source = Path(candidate.source_path)
        try:
            canonical_source = canonical_root / source.relative_to(copied_root)
        except ValueError as error:
            raise _error("release-copied-frontier-invalid", "compiler selected a source outside the admitted copy") from error
        mapped.append(replace(candidate, source_path=canonical_source.as_posix()))
    return _COMPILER.frontier_digest(mapped)


@dataclass(frozen=True)
class ReleaseCompilationPreflight:
    candidate_release: str
    expected_derived_source_copy_sha256: str
    expected_compiled_output_sha256: str
    compiler_entrypoint: CompilerEntrypoint
    canonical_source_snapshot_digest: str
    compiler_frontier_digest: str
    nested_source_recursive_sha256_before: str
    output_files: dict[str, bytes]
    child_manifest_bytes: bytes


def preflight_release_compilation(project_root: Path | str, *, candidate_release: str) -> ReleaseCompilationPreflight:
    """Predict complete child bytes before D566 sealing, without writes."""

    root = _root(project_root)
    source_root = root / CANONICAL_SOURCE_RELATIVE
    if source_root.is_symlink() or not source_root.is_dir():
        raise _error("release-source-missing", "canonical Methodology source root is missing")
    placeholder_root = root / MATERIALIZED_RELATIVE / PLACEHOLDER_COMPONENT
    report, selected = _report(root, CANONICAL_SOURCE_RELATIVE, _relative(root, placeholder_root))
    source_digest = tree_sha256(root, source_root)
    copied_root = root / DERIVED_SOURCE_COPY_RELATIVE
    transformed: list[Any] = []
    for candidate in selected:
        source = root / candidate.source_path
        relative = source.relative_to(source_root)
        transformed.append(replace(candidate, source_path=(Path(DERIVED_SOURCE_COPY_RELATIVE) / relative).as_posix()))
    output_files = _render_outputs(root, transformed, copied_root, placeholder_root, content_root=source_root)
    actual_root = root / MATERIALIZED_RELATIVE / ("a" * 64)
    actual_files = _render_outputs(root, transformed, copied_root, actual_root, content_root=source_root)
    if output_files != actual_files:
        raise _error("release-placeholder-unstable", "candidate child component changes projected output bytes")
    compiler = _compiler_entrypoint(root)
    manifest = _child_manifest_bytes(
        candidate_release=candidate_release,
        compiler=compiler,
        canonical_source_digest=source_digest,
        frontier_digest=str(report["source_frontier_digest"]),
        derived_copy_digest=source_digest,
        nested_digest=source_digest,
        output_files=output_files,
    )
    full_tree = {**output_files, CHILD_MANIFEST_NAME: manifest}
    return ReleaseCompilationPreflight(
        candidate_release=candidate_release,
        expected_derived_source_copy_sha256=source_digest,
        expected_compiled_output_sha256=_child_tree_digest(full_tree),
        compiler_entrypoint=compiler,
        canonical_source_snapshot_digest=source_digest,
        compiler_frontier_digest=str(report["source_frontier_digest"]),
        nested_source_recursive_sha256_before=source_digest,
        output_files=output_files,
        child_manifest_bytes=manifest,
    )


def build_preflight_validated_candidate(
    project_root: Path | str, *, candidate_release: str, full_suite_environment: Mapping[str, Any],
    candidate_image_reference: str,
) -> tuple[ReleaseCompilationPreflight, ValidatedCandidate]:
    """Use predicted local hashes as D566 expectations, never caller hash values."""

    preflight = preflight_release_compilation(project_root, candidate_release=candidate_release)
    request = CandidateBuildRequest.model_validate(
        {
            "candidate_release": candidate_release,
            "expected_derived_source_copy_sha256": preflight.expected_derived_source_copy_sha256,
            "expected_compiled_output_sha256": preflight.expected_compiled_output_sha256,
            "full_suite_environment": full_suite_environment,
            "candidate_image_reference": candidate_image_reference,
        }
    )
    candidate = build_validated_candidate(
        project_root,
        request,
        observed_source_frontier_digest=preflight.compiler_frontier_digest,
    )
    if candidate.manifest.canonical_source_snapshot_digest != preflight.canonical_source_snapshot_digest:
        raise _error("release-currentness-stale", "preflight source snapshot changed before candidate sealing")
    return preflight, candidate


def render_release_candidate(
    candidate: ValidatedCandidate, preflight: ReleaseCompilationPreflight,
) -> SealedCandidateCompilation:
    """Render the admitted copied source only into its sealed child root."""

    if not isinstance(candidate, ValidatedCandidate) or not isinstance(preflight, ReleaseCompilationPreflight):
        raise _error("release-compilation-untrusted", "renderer requires internal candidate and preflight objects")
    if candidate.intent.candidate_release != preflight.candidate_release:
        raise _error("release-preflight-mismatch", "preflight and candidate release differ")
    if candidate.manifest.expected_compiled_output_sha256 != preflight.expected_compiled_output_sha256:
        raise _error("release-preflight-mismatch", "candidate output expectation differs from preflight")
    current_preflight = preflight_release_compilation(candidate.project_root, candidate_release=candidate.intent.candidate_release)
    if current_preflight != preflight:
        raise _error("release-currentness-stale", "canonical compiler report or predicted child output changed")
    source_copy = validate_source_copy(candidate)
    root = _root(candidate.project_root)
    canonical_before = tree_sha256(root, CANONICAL_SOURCE_RELATIVE)
    if canonical_before != candidate.authority.nested_source_recursive_sha256_before:
        raise _error("release-currentness-stale", "canonical nested source changed before child render")
    child_relative = f"{MATERIALIZED_RELATIVE}/{candidate.manifest.sha256}"
    child_root = root / child_relative
    if child_root.exists() or child_root.is_symlink():
        raise _error("release-child-collision", "sealed child materialization root already exists")
    report, selected = _report(root, DERIVED_SOURCE_COPY_RELATIVE, child_relative)
    if _canonical_frontier_from_copied_candidates(selected) != candidate.manifest.source_frontier_digest:
        raise _error("release-copied-frontier-mismatch", "copied compiler selection does not map to sealed canonical frontier")
    rendered = _render_outputs(root, selected, root / DERIVED_SOURCE_COPY_RELATIVE, child_root)
    if rendered != preflight.output_files:
        raise _error("release-render-mismatch", "copied-source render differs from preflight projection bytes")
    manifest = _child_manifest_bytes(
        candidate_release=candidate.manifest.candidate_release,
        compiler=preflight.compiler_entrypoint,
        canonical_source_digest=candidate.manifest.canonical_source_snapshot_digest,
        frontier_digest=preflight.compiler_frontier_digest,
        derived_copy_digest=source_copy.actual_derived_source_copy_sha256,
        nested_digest=canonical_before,
        output_files=rendered,
    )
    if manifest != preflight.child_manifest_bytes:
        raise _error("release-render-mismatch", "child manifest differs from preflight canonical bytes")
    staged_parent = _mkdir_safe(root, MATERIALIZED_RELATIVE)
    staging = Path(tempfile.mkdtemp(prefix=".release-render-", dir=staged_parent))
    try:
        for relative, data in rendered.items():
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (staging / CHILD_MANIFEST_NAME).write_bytes(manifest)
        observed = tree_sha256(root, staging)
        if observed != preflight.expected_compiled_output_sha256:
            raise _error("release-render-mismatch", "staged child tree differs from preflight digest")
        os.replace(staging, child_root)
        canonical_after = tree_sha256(root, CANONICAL_SOURCE_RELATIVE)
        if canonical_after != canonical_before:
            raise _error("release-canonical-source-mutated", "child renderer changed canonical source")
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    evidence = CompilerSuccessEvidence(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        outcome="completed",
        compiler_entrypoint=preflight.compiler_entrypoint,
        compiler_frontier_digest=preflight.compiler_frontier_digest,
        child_materialization_root=child_relative,
        actual_compiled_output_sha256=preflight.expected_compiled_output_sha256,
    )
    return seal_candidate_compilation(source_copy, evidence)


__all__ = [
    "CHILD_MANIFEST_NAME",
    "CHILD_MANIFEST_SCHEMA",
    "ReleaseCompilationPreflight",
    "build_preflight_validated_candidate",
    "preflight_release_compilation",
    "render_release_candidate",
]
