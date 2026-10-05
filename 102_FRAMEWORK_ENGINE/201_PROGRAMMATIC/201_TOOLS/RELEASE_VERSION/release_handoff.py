"""Locally observed, effect-free D567 candidate handoffs.

The functions here only read bytes, TOML, and modes. They never copy, compile,
stage, select a runtime, install a Skill, invoke Docker, or record a Journal
event.
"""

from __future__ import annotations

import hashlib
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, Mapping

from pydantic import Field, field_validator, model_validator

from release_contract import (
    IMAGE_DOCKERFILE,
    PROJECT_SKILL_TARGET,
    CandidateBuildRequest,
    CandidateImageReference,
    CandidateSnapshotManifest,
    ReleaseContractError,
    SealedAuthority,
    SourceInventoryRow,
    StrictModel,
    ValidatedCandidate,
    _safe_relative,
    candidate_snapshot_manifest_sha256,
    canonical_json,
    encode_candidate_manifest,
)
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path


CANONICAL_SOURCE_RELATIVE = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources"
)
PROJECT_STRUCTURE_RELATIVE = ".caprmedio_caprmedio/project_structure.toml"
FRAMEWORK_SETTINGS_RELATIVE = f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml"
CURRENT_SELECTOR_RELATIVE = ".caprmedio_runtime/framework/current.toml"
DERIVED_SOURCE_COPY_RELATIVE = "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
MATERIALIZED_RELATIVE = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized"
ENGINE_ROOT_RELATIVE = "102_FRAMEWORK_ENGINE"
SKILL_ROOT_RELATIVE = "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca"
COMPILER_ENTRYPOINT_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py"
_PINNED_IMAGE_DEPENDENCY_COPY = b"COPY pyproject.toml uv.lock ./"
_PINNED_IMAGE_DEPENDENCY_INPUTS = ("pyproject.toml", "uv.lock")


def _error(code: str, message: str) -> ReleaseContractError:
    return ReleaseContractError(code, message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _root(value: Path | str) -> Path:
    root = Path(value).resolve()
    if not root.is_dir():
        raise _error("release-project-missing", f"project root is not a directory: {root}")
    return root


def _relative(root: Path, path: Path, *, label: str) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("release-path-unsafe", f"{label} escapes project root") from error


def _file(root: Path, relative: str, *, code: str = "release-input-missing") -> Path:
    safe = _safe_relative(relative, "relative")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    path = root / safe
    if path.is_symlink() or not path.is_file():
        raise _error(code, f"required regular file is absent: {safe}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("release-path-unsafe", f"required file escapes project: {safe}") from error
    return path


def _directory(root: Path, relative: str, *, code: str = "release-input-missing") -> Path:
    safe = _safe_relative(relative, "relative")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    path = root / safe
    if path.is_symlink() or not path.is_dir():
        raise _error(code, f"required directory is absent: {safe}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("release-path-unsafe", f"required directory escapes project: {safe}") from error
    return path


def _regular_files(root: Path, directory: Path, *, code: str = "release-input-invalid") -> list[Path]:
    try:
        files = persistent_regular_files(root, directory)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    if not files:
        raise _error(code, f"required inventory is empty: {_relative(root, directory, label='directory')}")
    return files


def tree_sha256(root: Path | str, directory: Path | str) -> str:
    """Digest the ordered relative-path and byte sequence below one directory."""

    project = _root(root)
    folder = Path(directory)
    if not folder.is_absolute():
        folder = project / folder
    folder = _directory(project, _relative(project, folder, label="tree root"))
    digest = hashlib.sha256()
    for path in _regular_files(project, folder):
        relative = path.relative_to(folder).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        contents = path.read_bytes()
        digest.update(len(contents).to_bytes(8, "big"))
        digest.update(contents)
    return digest.hexdigest()


def _selector_release(root: Path) -> str:
    selector = _file(root, CURRENT_SELECTOR_RELATIVE, code="release-selection-missing")
    try:
        payload = tomllib.loads(selector.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("release-selection-invalid", "current framework selector is not valid TOML") from error
    values: list[str] = []
    for mapping in (payload, payload.get("selection") if isinstance(payload.get("selection"), dict) else {}):
        for key in ("executing_release", "selected_release", "release"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(value)
        for key in ("selected_release_root", "release_root"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(Path(value).name)
    unique = set(values)
    if len(unique) != 1:
        raise _error("release-selection-ambiguous", "current framework selector must name exactly one executing release")
    return unique.pop()


def _inventory_row(root: Path, path: Path, resource: str, destination: str) -> SourceInventoryRow:
    relative = _relative(root, path, label="inventory source")
    return SourceInventoryRow(
        resource=resource,
        source_path=relative,
        source_sha256=_sha256_bytes(path.read_bytes()),
        source_mode=path.stat().st_mode & 0o777,
        destination_path=destination,
    )


def _image_input_paths(root: Path, dockerfile: Path) -> list[Path]:
    """Observe the fixed dependency inputs declared by the pinned Dockerfile.

    This is intentionally not a general Dockerfile parser.  The known
    repository build instruction has exactly two root dependency inputs; when
    that instruction is present, both are required before the candidate can be
    sealed.
    """

    paths = [dockerfile]
    if _PINNED_IMAGE_DEPENDENCY_COPY in dockerfile.read_bytes():
        paths.extend(
            _file(root, relative, code="release-image-input-missing")
            for relative in _PINNED_IMAGE_DEPENDENCY_INPUTS
        )
    return paths


def _observed_inventory(root: Path) -> tuple[list[SourceInventoryRow], CandidateImageReference]:
    source_root = _directory(root, CANONICAL_SOURCE_RELATIVE)
    engine_root = _directory(root, ENGINE_ROOT_RELATIVE)
    skill_root = _directory(root, SKILL_ROOT_RELATIVE)
    dockerfile = _file(root, IMAGE_DOCKERFILE)
    rows: list[SourceInventoryRow] = []
    for path in _regular_files(root, source_root):
        rows.append(_inventory_row(root, path, "METHODOLOGY", f"METHODOLOGY/sources/{path.relative_to(source_root).as_posix()}"))
    for path in _regular_files(root, engine_root):
        if path == dockerfile or path.is_relative_to(skill_root):
            continue
        rows.append(_inventory_row(root, path, "FRAMEWORK_ENGINE", f"FRAMEWORK_ENGINE/{path.relative_to(engine_root).as_posix()}"))
    for path in _regular_files(root, skill_root):
        rows.append(_inventory_row(root, path, "SKILL", f"SKILLS/ca/{path.relative_to(skill_root).as_posix()}"))
    for image_input in _image_input_paths(root, dockerfile):
        if image_input == dockerfile:
            destination = f"IMAGE_INPUT/{dockerfile.relative_to(engine_root).as_posix()}"
        else:
            destination = f"IMAGE_INPUT/{image_input.relative_to(root).as_posix()}"
        rows.append(_inventory_row(root, image_input, "IMAGE_INPUT", destination))
    if not any(row.resource == "FRAMEWORK_ENGINE" for row in rows):
        raise _error("release-inventory-incomplete", "Framework Engine inventory is empty")
    image = CandidateImageReference(
        dockerfile_path=IMAGE_DOCKERFILE,
        dockerfile_sha256=_sha256_bytes(dockerfile.read_bytes()),
        candidate_image_reference="pending-local-observation",
    )
    return rows, image


def build_validated_candidate(
    project_root: Path | str,
    request: CandidateBuildRequest | Mapping[str, Any],
    *,
    observed_source_frontier_digest: str | None = None,
) -> ValidatedCandidate:
    """Observe local N/currentness and construct one pre-compiler candidate.v2."""

    root = _root(project_root)
    intent = request if isinstance(request, CandidateBuildRequest) else CandidateBuildRequest.model_validate(request)
    source_root = _directory(root, CANONICAL_SOURCE_RELATIVE)
    structure = _file(root, PROJECT_STRUCTURE_RELATIVE)
    settings = _file(root, FRAMEWORK_SETTINGS_RELATIVE)
    executing_release = _selector_release(root)
    if executing_release == intent.candidate_release:
        raise _error("release-currentness-invalid", "candidate release is already the locally selected release")
    rows, image = _observed_inventory(root)
    image = image.model_copy(update={"candidate_image_reference": intent.candidate_image_reference})
    snapshot_digest = tree_sha256(root, source_root)
    frontier_digest = observed_source_frontier_digest or snapshot_digest
    manifest = encode_candidate_manifest(
        {
            "executing_release": executing_release,
            "candidate_release": intent.candidate_release,
            "canonical_source_snapshot_ref": CANONICAL_SOURCE_RELATIVE,
            "canonical_source_snapshot_digest": snapshot_digest,
            "project_structure_digest": _sha256_bytes(structure.read_bytes()),
            "framework_settings_digest": _sha256_bytes(settings.read_bytes()),
            "source_frontier_digest": frontier_digest,
            "nested_source_recursive_sha256_before": snapshot_digest,
            "expected_derived_source_copy_sha256": intent.expected_derived_source_copy_sha256,
            "expected_compiled_output_sha256": intent.expected_compiled_output_sha256,
            "full_suite_environment": intent.full_suite_environment.model_dump(mode="json"),
            "skill_target": PROJECT_SKILL_TARGET,
            "candidate_image": image.model_dump(mode="json"),
            "source_inventory_rows": [row.model_dump(mode="json") for row in rows],
        }
    )
    authority = SealedAuthority(
        executing_release=executing_release,
        candidate_release=intent.candidate_release,
        canonical_source_snapshot_digest=snapshot_digest,
        project_structure_digest=_sha256_bytes(structure.read_bytes()),
        framework_settings_digest=_sha256_bytes(settings.read_bytes()),
        source_frontier_digest=frontier_digest,
        nested_source_recursive_sha256_before=snapshot_digest,
        expected_candidate_snapshot_manifest_sha256=manifest.sha256,
    )
    return ValidatedCandidate(str(root), manifest, authority, intent)


def _revalidate(candidate: ValidatedCandidate) -> ValidatedCandidate:
    if not isinstance(candidate, ValidatedCandidate):
        raise _error("release-candidate-untrusted", "pre-compiler handoff must be a locally validated candidate")
    observed = build_validated_candidate(
        candidate.project_root,
        candidate.intent,
        observed_source_frontier_digest=candidate.authority.source_frontier_digest,
    )
    if observed.authority != candidate.authority or observed.manifest != candidate.manifest:
        raise _error("release-currentness-stale", "locally observed selection or sealed candidate inputs changed")
    if candidate.manifest.sha256 != candidate_snapshot_manifest_sha256(candidate.manifest):
        raise _error("candidate-manifest-unsealed", "candidate manifest checksum no longer validates")
    return observed


@dataclass(frozen=True)
class SealedSourceCopy:
    candidate: ValidatedCandidate
    source_copy_root: str
    actual_derived_source_copy_sha256: str


def validate_source_copy(candidate: ValidatedCandidate, source_copy_root: Path | str | None = None) -> SealedSourceCopy:
    """Validate a completed derived copy before compiler or package admission."""

    current = _revalidate(candidate)
    root = _root(current.project_root)
    expected = root / DERIVED_SOURCE_COPY_RELATIVE
    supplied = expected if source_copy_root is None else Path(source_copy_root)
    if not supplied.is_absolute():
        supplied = root / supplied
    if supplied.resolve(strict=False) != expected.resolve(strict=False):
        raise _error("release-copy-root-invalid", "derived source copy root is not the D561 delivery root")
    copy_root = _directory(root, DERIVED_SOURCE_COPY_RELATIVE, code="release-copy-missing")
    actual = tree_sha256(root, copy_root)
    if actual != current.manifest.expected_derived_source_copy_sha256:
        raise _error("release-copy-digest-mismatch", "complete derived source copy does not match the sealed expectation")
    return SealedSourceCopy(current, DERIVED_SOURCE_COPY_RELATIVE, actual)


class CompilerEntrypoint(StrictModel):
    path: str
    sha256: str = Field(pattern="^[0-9a-f]{64}$")

    @field_validator("path")
    @classmethod
    def bounded_path(cls, value: str) -> str:
        return _safe_relative(value, "compiler entrypoint")


class CompilerSuccessEvidence(StrictModel):
    """Typed compiler result supplied by the future compiler adapter, never a mapping."""

    candidate_snapshot_manifest_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    outcome: str
    compiler_entrypoint: CompilerEntrypoint
    compiler_frontier_digest: str = Field(pattern="^[0-9a-f]{64}$")
    child_materialization_root: str
    actual_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")

    @field_validator("child_materialization_root")
    @classmethod
    def bounded_root(cls, value: str) -> str:
        return _safe_relative(value, "child_materialization_root")

    @model_validator(mode="after")
    def completed_only(self) -> "CompilerSuccessEvidence":
        if self.outcome != "completed":
            raise ValueError("compiler evidence must report completed")
        return self


class PackageRow(StrictModel):
    resource: Literal["FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"]
    source_path: str
    destination_path: str
    sha256: str = Field(pattern="^[0-9a-f]{64}$")
    mode: int = Field(ge=0, le=0o777)

    @field_validator("source_path", "destination_path")
    @classmethod
    def bounded_path(cls, value: str, info: Any) -> str:
        return _safe_relative(value, info.field_name)

    @model_validator(mode="after")
    def destination_matches_resource(self) -> "PackageRow":
        prefixes = {
            "FRAMEWORK_ENGINE": "FRAMEWORK_ENGINE/",
            "METHODOLOGY": "METHODOLOGY/",
            "SKILL": "SKILLS/ca/",
        }
        if not self.destination_path.startswith(prefixes[self.resource]):
            raise ValueError("package destination is outside its resource root")
        return self


class SealedCandidateCompilation(StrictModel):
    candidate_snapshot_manifest_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    authority: SealedAuthority
    source_copy_root: str
    expected_derived_source_copy_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    actual_derived_source_copy_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    compiler_entrypoint: CompilerEntrypoint
    compiler_frontier_digest: str = Field(pattern="^[0-9a-f]{64}$")
    expected_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    actual_compiled_output_sha256: str = Field(pattern="^[0-9a-f]{64}$")
    child_materialization_root: str
    package_rows: list[PackageRow] = Field(min_length=1)

    @field_validator("source_copy_root", "child_materialization_root")
    @classmethod
    def bounded_roots(cls, value: str, info: Any) -> str:
        return _safe_relative(value, info.field_name)

    @model_validator(mode="after")
    def complete_package_rows(self) -> "SealedCandidateCompilation":
        destinations = [row.destination_path for row in self.package_rows]
        if len(destinations) != len(set(destinations)):
            raise ValueError("package handoff has destination collisions")
        resources = {row.resource for row in self.package_rows}
        if not {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"} <= resources:
            raise ValueError("package handoff is not a complete Framework package")
        if not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= set(destinations):
            raise ValueError("package handoff lacks required ca Skill files")
        return self


def _package_rows(candidate: ValidatedCandidate, materialized_root: Path) -> list[PackageRow]:
    root = _root(candidate.project_root)
    rows: list[PackageRow] = []
    for inventory in candidate.manifest.source_inventory_rows:
        if inventory.resource == "IMAGE_INPUT":
            continue
        path = _file(root, inventory.source_path, code="release-current-input-missing")
        actual_sha = _sha256_bytes(path.read_bytes())
        actual_mode = path.stat().st_mode & 0o777
        if actual_sha != inventory.source_sha256 or actual_mode != inventory.source_mode:
            raise _error("release-currentness-stale", f"source inventory changed: {inventory.source_path}")
        rows.append(PackageRow(resource=inventory.resource, source_path=inventory.source_path, destination_path=inventory.destination_path, sha256=actual_sha, mode=actual_mode))
    for path in _regular_files(root, materialized_root, code="release-compiler-output-invalid"):
        rows.append(
            PackageRow(
                resource="METHODOLOGY",
                source_path=_relative(root, path, label="compiled output"),
                destination_path=f"METHODOLOGY/compiled/{path.relative_to(materialized_root).as_posix()}",
                sha256=_sha256_bytes(path.read_bytes()),
                mode=path.stat().st_mode & 0o777,
            )
        )
    return sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256))


def seal_candidate_compilation(
    source_copy: SealedSourceCopy,
    compiler_evidence: CompilerSuccessEvidence | None = None,
    materialization_root: Path | str | None = None,
) -> SealedCandidateCompilation:
    """Read and seal post-compiler evidence; compilation itself is not invoked."""

    if not isinstance(source_copy, SealedSourceCopy):
        raise _error("release-copy-untrusted", "source copy must be a locally validated sealed source copy")
    candidate = _revalidate(source_copy.candidate)
    root = _root(candidate.project_root)
    copy_root = _directory(root, source_copy.source_copy_root, code="release-copy-missing")
    actual_copy = tree_sha256(root, copy_root)
    if actual_copy != source_copy.actual_derived_source_copy_sha256 or actual_copy != candidate.manifest.expected_derived_source_copy_sha256:
        raise _error("release-copy-digest-mismatch", "source copy is stale, partial, or mismatched")
    expected_materialized = root / MATERIALIZED_RELATIVE / candidate.manifest.sha256
    supplied = expected_materialized if materialization_root is None else Path(materialization_root)
    if not supplied.is_absolute():
        supplied = root / supplied
    if supplied.resolve(strict=False) != expected_materialized.resolve(strict=False):
        raise _error("release-materialization-root-invalid", "compiler output is outside the sealed child materialization root")
    materialized = _directory(root, _relative(root, expected_materialized, label="materialization root"), code="release-compiler-output-missing")
    actual_output = tree_sha256(root, materialized)
    if actual_output != candidate.manifest.expected_compiled_output_sha256:
        raise _error("release-compiler-output-mismatch", "compiler output does not match the sealed expectation")
    compiler = _file(root, COMPILER_ENTRYPOINT_RELATIVE, code="release-compiler-entrypoint-missing")
    observed_entrypoint = CompilerEntrypoint(path=COMPILER_ENTRYPOINT_RELATIVE, sha256=_sha256_bytes(compiler.read_bytes()))
    if not isinstance(compiler_evidence, CompilerSuccessEvidence):
        raise _error("release-compiler-evidence-untrusted", "compiler success evidence must be a typed internal result")
    if compiler_evidence.outcome != "completed":
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not report a completed invocation")
    if compiler_evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence identifies a different candidate")
    if compiler_evidence.compiler_entrypoint != observed_entrypoint:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not match the locally observed compiler")
    if compiler_evidence.compiler_frontier_digest != candidate.authority.source_frontier_digest:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence has a stale frontier")
    if compiler_evidence.child_materialization_root != _relative(root, materialized, label="materialization root"):
        raise _error("release-compiler-evidence-mismatch", "compiler evidence names a different materialization root")
    if compiler_evidence.actual_compiled_output_sha256 != actual_output:
        raise _error("release-compiler-evidence-mismatch", "compiler evidence does not match materialized bytes")
    return SealedCandidateCompilation(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        authority=candidate.authority,
        source_copy_root=source_copy.source_copy_root,
        expected_derived_source_copy_sha256=candidate.manifest.expected_derived_source_copy_sha256,
        actual_derived_source_copy_sha256=actual_copy,
        compiler_entrypoint=observed_entrypoint,
        compiler_frontier_digest=candidate.authority.source_frontier_digest,
        expected_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
        actual_compiled_output_sha256=actual_output,
        child_materialization_root=_relative(root, materialized, label="materialization root"),
        package_rows=_package_rows(candidate, materialized),
    )


__all__ = [
    "CANONICAL_SOURCE_RELATIVE",
    "COMPILER_ENTRYPOINT_RELATIVE",
    "CURRENT_SELECTOR_RELATIVE",
    "DERIVED_SOURCE_COPY_RELATIVE",
    "MATERIALIZED_RELATIVE",
    "CompilerEntrypoint",
    "CompilerSuccessEvidence",
    "PackageRow",
    "SealedCandidateCompilation",
    "SealedSourceCopy",
    "build_validated_candidate",
    "seal_candidate_compilation",
    "tree_sha256",
    "validate_source_copy",
]
