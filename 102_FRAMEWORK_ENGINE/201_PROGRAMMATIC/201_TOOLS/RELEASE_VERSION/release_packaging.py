"""Non-active staging of one locally sealed, complete Framework package.

This adapter accepts only the post-copy/post-compiler handoff from
``release_handoff``. It does not select a runtime, expose a public Skill, run
gates, build an image, or record a Journal event.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import tomllib
from pathlib import Path
from typing import Iterable

from release_contract import IMAGE_DOCKERFILE, REQUIRED_ENGINE_SOURCE_PREFIXES
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE,
    COMPILER_ENTRYPOINT_RELATIVE,
    CURRENT_SELECTOR_RELATIVE,
    DERIVED_SOURCE_COPY_RELATIVE,
    FRAMEWORK_SETTINGS_RELATIVE,
    MATERIALIZED_RELATIVE,
    PackageRow,
    SealedCandidateCompilation,
    tree_sha256,
)


RUNTIME_ROOT = Path(".caprmedio_runtime/framework")
MANIFEST_NAME = "manifest.toml"
SHA256_LENGTH = 64
SKILL_ROOT = Path("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca")
REQUIRED_SKILL_FILES = frozenset({"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"})


class ReleasePackagingError(RuntimeError):
    """Stable refusal from the retained-package staging boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _safe_relative(value: object, field: str) -> Path:
    if not isinstance(value, str) or not value:
        raise ReleasePackagingError("package-path-invalid", f"{field} must be a non-empty relative path")
    path = Path(value)
    if path.is_absolute() or path == Path(".") or any(part in {"", ".", ".."} for part in path.parts):
        raise ReleasePackagingError("package-path-unsafe", f"{field} is unsafe")
    return path


def _candidate_sha256(value: object) -> str:
    if not isinstance(value, str) or len(value) != SHA256_LENGTH or value != value.lower():
        raise ReleasePackagingError("candidate-manifest-unsealed", "candidate snapshot identity is invalid")
    try:
        int(value, 16)
    except ValueError as error:
        raise ReleasePackagingError("candidate-manifest-unsealed", "candidate snapshot identity is invalid") from error
    return value


def _regular_file(root: Path, relative: str | Path, *, code: str = "package-source-missing") -> Path:
    safe = _safe_relative(relative.as_posix() if isinstance(relative, Path) else relative, "source path")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise ReleasePackagingError(error.code, str(error)) from error
    cursor = root
    for component in safe.parts:
        cursor = cursor / component
        if cursor.is_symlink():
            raise ReleasePackagingError("package-source-symlink", f"source is a symlink: {safe.as_posix()}")
    if not cursor.is_file():
        raise ReleasePackagingError(code, f"required regular file is absent: {safe.as_posix()}")
    try:
        cursor.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise ReleasePackagingError("package-path-unsafe", f"source escapes project: {safe.as_posix()}") from error
    return cursor


def _regular_directory(root: Path, relative: str | Path, *, code: str = "package-source-missing") -> Path:
    safe = _safe_relative(relative.as_posix() if isinstance(relative, Path) else relative, "directory path")
    try:
        refuse_secret_path(safe)
    except ReleaseInventoryError as error:
        raise ReleasePackagingError(error.code, str(error)) from error
    path = root / safe
    if path.is_symlink() or not path.is_dir():
        raise ReleasePackagingError(code, f"required directory is absent: {safe.as_posix()}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise ReleasePackagingError("package-path-unsafe", f"directory escapes project: {safe.as_posix()}") from error
    return path


def _regular_files(root: Path, relative: str | Path) -> set[str]:
    directory = _regular_directory(root, relative)
    try:
        files = {path.relative_to(root).as_posix() for path in persistent_regular_files(root, directory)}
    except ReleaseInventoryError as error:
        raise ReleasePackagingError(error.code, str(error)) from error
    if not files:
        raise ReleasePackagingError("package-incomplete", f"source inventory is empty: {Path(relative).as_posix()}")
    return files


def _current_release(root: Path) -> tuple[str, bytes]:
    selector = _regular_file(root, CURRENT_SELECTOR_RELATIVE, code="release-selection-missing")
    payload = selector.read_bytes()
    try:
        parsed = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ReleasePackagingError("release-selection-invalid", "current selector is not valid TOML") from error
    values: list[str] = []
    nested = parsed.get("selection")
    for mapping in (parsed, nested if isinstance(nested, dict) else {}):
        for key in ("executing_release", "selected_release", "release"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(value)
        for key in ("selected_release_root", "release_root"):
            value = mapping.get(key)
            if isinstance(value, str) and value:
                values.append(Path(value).name)
    if len(set(values)) != 1:
        raise ReleasePackagingError("release-selection-ambiguous", "current selector must name exactly one release")
    return values[0], payload


def _tree_digest(root: Path, relative: str) -> str:
    try:
        return tree_sha256(root, relative)
    except Exception as error:  # shared D567 tree algorithm
        raise ReleasePackagingError("package-source-invalid", f"cannot observe sealed tree: {relative}") from error


def _require_runtime_parents(root: Path, *, create: bool) -> Path:
    cursor = root
    for part in RUNTIME_ROOT.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ReleasePackagingError("runtime-parent-symlink", f"runtime parent is a symlink: {cursor.relative_to(root).as_posix()}")
        if cursor.exists() and not cursor.is_dir():
            raise ReleasePackagingError("runtime-parent-invalid", f"runtime parent is not a directory: {cursor.relative_to(root).as_posix()}")
        if create and not cursor.exists():
            cursor.mkdir()
        if cursor.exists():
            try:
                cursor.resolve(strict=True).relative_to(root)
            except ValueError as error:
                raise ReleasePackagingError("runtime-parent-escape", "runtime parent escapes project root") from error
    return cursor


def _destination_for(row: PackageRow, candidate: str) -> None:
    source = Path(row.source_path)
    destination = Path(row.destination_path)
    if row.resource == "FRAMEWORK_ENGINE":
        try:
            suffix = source.relative_to("102_FRAMEWORK_ENGINE")
        except ValueError as error:
            raise ReleasePackagingError("package-source-invalid", "Engine source is outside Framework Engine") from error
        if destination != Path("FRAMEWORK_ENGINE") / suffix:
            raise ReleasePackagingError("package-destination-invalid", "Engine destination does not preserve source suffix")
    elif row.resource == "SKILL":
        try:
            suffix = source.relative_to(SKILL_ROOT)
        except ValueError as error:
            raise ReleasePackagingError("package-source-invalid", "Skill source is outside canonical ca Skill") from error
        if destination != Path("SKILLS/ca") / suffix:
            raise ReleasePackagingError("package-destination-invalid", "Skill destination does not preserve source suffix")
    elif row.resource == "METHODOLOGY":
        canonical = Path(CANONICAL_SOURCE_RELATIVE)
        materialized = Path(MATERIALIZED_RELATIVE) / candidate
        if source.is_relative_to(canonical):
            if destination != Path("METHODOLOGY/sources") / source.relative_to(canonical):
                raise ReleasePackagingError("package-destination-invalid", "Methodology source destination is invalid")
        elif source.is_relative_to(materialized):
            if destination != Path("METHODOLOGY/compiled") / source.relative_to(materialized):
                raise ReleasePackagingError("package-destination-invalid", "compiled Methodology destination is invalid")
        else:
            raise ReleasePackagingError("package-source-invalid", "Methodology source is outside sealed source or materialization roots")
    else:
        raise ReleasePackagingError("package-resource-invalid", "package row has an unknown resource")


def _read_row(root: Path, row: PackageRow) -> Path:
    if not isinstance(row, PackageRow):
        raise ReleasePackagingError("sealed-compilation-untrusted", "package rows must be typed local observations")
    source = _regular_file(root, row.source_path)
    actual_digest = _sha256(source.read_bytes())
    actual_mode = source.stat().st_mode & 0o777
    if actual_digest != row.sha256:
        raise ReleasePackagingError("package-source-digest-mismatch", f"source bytes changed: {row.source_path}")
    if actual_mode != row.mode:
        raise ReleasePackagingError("package-source-mode-mismatch", f"source mode changed: {row.source_path}")
    return source


def _complete_rows(root: Path, compilation: SealedCandidateCompilation) -> tuple[str, list[PackageRow], bytes]:
    if not isinstance(compilation, SealedCandidateCompilation):
        raise ReleasePackagingError("sealed-compilation-untrusted", "staging requires a locally sealed candidate compilation")
    candidate = _candidate_sha256(compilation.candidate_snapshot_manifest_sha256)
    authority = compilation.authority
    if candidate != authority.expected_candidate_snapshot_manifest_sha256:
        raise ReleasePackagingError("candidate-manifest-unsealed", "typed handoff is not bound to its canonical candidate identity")
    if compilation.source_copy_root != DERIVED_SOURCE_COPY_RELATIVE:
        raise ReleasePackagingError("release-copy-root-invalid", "handoff source copy root is not the D561 delivery root")
    if compilation.child_materialization_root != f"{MATERIALIZED_RELATIVE}/{candidate}":
        raise ReleasePackagingError("release-materialization-root-invalid", "handoff output is outside its candidate child root")
    if compilation.expected_derived_source_copy_sha256 != compilation.actual_derived_source_copy_sha256:
        raise ReleasePackagingError("release-copy-digest-mismatch", "handoff does not bind an actual accepted source copy")
    if compilation.expected_compiled_output_sha256 != compilation.actual_compiled_output_sha256:
        raise ReleasePackagingError("release-compiler-output-mismatch", "handoff does not bind accepted compiler output")

    selected, selector_before = _current_release(root)
    if selected != authority.executing_release:
        raise ReleasePackagingError("release-currentness-stale", "current selector differs from the sealed executing release")
    canonical_digest = _tree_digest(root, CANONICAL_SOURCE_RELATIVE)
    if canonical_digest != authority.canonical_source_snapshot_digest or canonical_digest != authority.nested_source_recursive_sha256_before:
        raise ReleasePackagingError("release-currentness-stale", "canonical Methodology frontier changed after sealing")
    structure = _regular_file(root, ".caprmedio_caprmedio/project_structure.toml")
    settings = _regular_file(root, FRAMEWORK_SETTINGS_RELATIVE)
    if _sha256(structure.read_bytes()) != authority.project_structure_digest or _sha256(settings.read_bytes()) != authority.framework_settings_digest:
        raise ReleasePackagingError("release-currentness-stale", "Project Structure or Framework Settings changed after sealing")
    if _tree_digest(root, compilation.source_copy_root) != compilation.actual_derived_source_copy_sha256:
        raise ReleasePackagingError("release-copy-digest-mismatch", "derived source copy no longer matches the sealed handoff")
    if _tree_digest(root, compilation.child_materialization_root) != compilation.actual_compiled_output_sha256:
        raise ReleasePackagingError("release-compiler-output-mismatch", "materialized compiler output no longer matches the sealed handoff")
    if compilation.compiler_entrypoint.path != COMPILER_ENTRYPOINT_RELATIVE:
        raise ReleasePackagingError("release-compiler-entrypoint-invalid", "handoff names a different compiler entrypoint")
    compiler = _regular_file(root, compilation.compiler_entrypoint.path)
    if (
        _sha256(compiler.read_bytes()) != compilation.compiler_entrypoint.sha256
        or compilation.compiler_frontier_digest != authority.source_frontier_digest
    ):
        raise ReleasePackagingError("release-currentness-stale", "compiler or compiler frontier changed after sealing")

    rows = list(compilation.package_rows)
    if not rows or rows != sorted(rows, key=lambda item: (item.destination_path, item.source_path, item.sha256)):
        raise ReleasePackagingError("package-rows-invalid", "typed package rows must be non-empty and destination ordered")
    destinations = [row.destination_path for row in rows]
    if len(destinations) != len(set(destinations)):
        raise ReleasePackagingError("package-destination-duplicate", "typed package rows contain duplicate destinations")
    for row in rows:
        _destination_for(row, candidate)
        _read_row(root, row)

    source_rows = {row.source_path for row in rows if row.resource == "METHODOLOGY" and row.destination_path.startswith("METHODOLOGY/sources/")}
    compiled_rows = {row.source_path for row in rows if row.resource == "METHODOLOGY" and row.destination_path.startswith("METHODOLOGY/compiled/")}
    engine_rows = {row.source_path for row in rows if row.resource == "FRAMEWORK_ENGINE"}
    skill_rows = {row.source_path for row in rows if row.resource == "SKILL"}
    engine_actual = _regular_files(root, "102_FRAMEWORK_ENGINE")
    engine_actual.discard(IMAGE_DOCKERFILE)
    engine_actual = {path for path in engine_actual if not Path(path).is_relative_to(SKILL_ROOT)}
    if engine_rows != engine_actual or any(not any(path.startswith(prefix) for path in engine_rows) for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES):
        raise ReleasePackagingError("package-incomplete", "typed handoff does not cover the complete Framework Engine")
    if source_rows != _regular_files(root, CANONICAL_SOURCE_RELATIVE):
        raise ReleasePackagingError("package-incomplete", "typed handoff does not cover the complete Methodology source delivery")
    if compiled_rows != _regular_files(root, compilation.child_materialization_root):
        raise ReleasePackagingError("package-incomplete", "typed handoff does not cover the complete compiler materialization")
    if skill_rows != _regular_files(root, SKILL_ROOT) or not REQUIRED_SKILL_FILES.issubset(destinations):
        raise ReleasePackagingError("package-incomplete", "typed handoff does not cover the complete ca Skill payload")
    return candidate, rows, selector_before


def _render_manifest(candidate: str, rows: Iterable[PackageRow]) -> str:
    lines = ["schema_version = 2", f"candidate_snapshot_manifest_sha256 = {_quoted(candidate)}", "package = \"caprmedio-framework\"", ""]
    for row in rows:
        lines.extend(["[[files]]", f"resource = {_quoted(row.resource)}", f"source_path = {_quoted(row.source_path)}", f"destination = {_quoted(row.destination_path)}", f"sha256 = {_quoted(row.sha256)}", f"mode = {row.mode}", ""])
    return "\n".join(lines)


def _verify_release(release_root: Path, manifest: str, rows: Iterable[PackageRow]) -> None:
    expected_rows = list(rows)
    manifest_path = release_root / MANIFEST_NAME
    if release_root.is_symlink() or not release_root.is_dir() or manifest_path.is_symlink() or not manifest_path.is_file():
        raise ReleasePackagingError("release-collision", f"existing release is invalid: {release_root.name}")
    if manifest_path.read_text(encoding="utf-8") != manifest:
        raise ReleasePackagingError("release-collision", f"existing release manifest differs: {release_root.name}")
    expected_paths = {MANIFEST_NAME, *(row.destination_path for row in expected_rows)}
    actual_paths: set[str] = set()
    for carrier in release_root.rglob("*"):
        relative = carrier.relative_to(release_root).as_posix()
        if carrier.is_symlink() or (not carrier.is_dir() and not carrier.is_file()):
            raise ReleasePackagingError("release-collision", f"existing release contains unsafe carrier: {relative}")
        if carrier.is_file():
            actual_paths.add(relative)
    if actual_paths != expected_paths:
        raise ReleasePackagingError("release-collision", f"existing release inventory differs: {release_root.name}")
    for row in expected_rows:
        target = release_root / row.destination_path
        if not target.is_file() or target.is_symlink() or _sha256(target.read_bytes()) != row.sha256 or target.stat().st_mode & 0o777 != row.mode:
            raise ReleasePackagingError("release-collision", f"existing release file differs: {row.destination_path}")


def _copy_release(root: Path, staging: Path, rows: Iterable[PackageRow], manifest: str) -> None:
    for row in rows:
        source = _read_row(root, row)  # D567: reread bytes and observed mode immediately before copy.
        target = staging / row.destination_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        target.chmod(row.mode)
    (staging / MANIFEST_NAME).write_text(manifest, encoding="utf-8", newline="\n")
    _verify_release(staging, manifest, rows)


def stage_framework_package(project_root: Path | str, sealed_compilation: SealedCandidateCompilation) -> dict[str, object]:
    """Stage one retained package from a sealed D567 post-compiler handoff."""

    root = Path(project_root).resolve()
    if not root.is_dir():
        raise ReleasePackagingError("repository-not-found", f"cannot resolve repository: {root}")
    _require_runtime_parents(root, create=False)
    candidate, rows, selector_before = _complete_rows(root, sealed_compilation)
    framework_root = _require_runtime_parents(root, create=True)
    releases_root = framework_root / "releases"
    if releases_root.is_symlink():
        raise ReleasePackagingError("runtime-parent-symlink", "release directory is a symlink")
    releases_root.mkdir(exist_ok=True)
    if not releases_root.is_dir():
        raise ReleasePackagingError("runtime-parent-invalid", "release directory is not a directory")
    release_root = releases_root / candidate
    manifest = _render_manifest(candidate, rows)

    if release_root.exists() or release_root.is_symlink():
        _verify_release(release_root, manifest, rows)
        if _current_release(root)[1] != selector_before:
            raise ReleasePackagingError("release-selection-changed", "N changed while retained package was being verified")
        return {"staged": False, "verified": True, "candidate_snapshot_manifest_sha256": candidate, "release_root": release_root.relative_to(root).as_posix(), "file_count": len(rows)}

    staging = Path(tempfile.mkdtemp(prefix=f".staging-{candidate[:12]}-", dir=releases_root))
    try:
        _copy_release(root, staging, rows, manifest)
        try:
            os.replace(staging, release_root)
        except FileExistsError:
            _verify_release(release_root, manifest, rows)
            staged = False
        else:
            staged = True
        _verify_release(release_root, manifest, rows)
        if _current_release(root)[1] != selector_before:
            raise ReleasePackagingError("release-selection-changed", "N changed while retained package was being staged")
        return {"staged": staged, "verified": True, "candidate_snapshot_manifest_sha256": candidate, "release_root": release_root.relative_to(root).as_posix(), "file_count": len(rows)}
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
