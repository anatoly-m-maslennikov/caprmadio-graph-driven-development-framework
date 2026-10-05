"""Initialize the first installed CAPRMEDIO Framework Runtime.

This is intentionally *not* a Release Version helper.  Release Version
requires an already selected N and publishes N+1 only after its full gate.
This module admits the single bootstrap case where the Framework runtime and
the project-local ``ca`` Skill do not yet exist.

The caller supplies a direct-Action Journal boundary, independent of selected
Workflow routing.  ``begin_action`` records and reopens canonical started
evidence before an effect; ``finish_action`` is the only terminal writer used
here.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol

from release_contract import PROJECT_SKILL_TARGET, ReleaseContractError, canonical_json
from release_handoff import CURRENT_SELECTOR_RELATIVE, PackageRow as ReleasePackageRow
from release_image import DockerCommandResult, DockerExecutor, IMAGE_ID
from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path
from release_packaging import (MANIFEST_NAME, RUNTIME_ROOT, ReleasePackagingError, _render_manifest,
                               _verify_release)


RELEASES_RELATIVE = RUNTIME_ROOT / "releases"
SELECTOR_RELATIVE = Path(CURRENT_SELECTOR_RELATIVE)
INITIALIZATION_EVIDENCE_RELATIVE = Path(".caprmedio_runtime/framework_initialization")
ENGINE_RELATIVE = Path("102_FRAMEWORK_ENGINE")
SKILL_SOURCE_RELATIVE = ENGINE_RELATIVE / "202_AGENTIC/205_SKILLS/ca"
METHODOLOGY_SOURCES_RELATIVE = Path(
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources"
)
METHODOLOGY_COMPILED_RELATIVE = Path(
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
)
OBSOLETE_METHODOLOGY_COMPILED_RELATIVE = Path(
    ".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY"
)
PACKAGE_NAME = "caprmedio-framework"
PACKAGE_IMAGE_LABEL = "org.caprmedio.framework.package_manifest_sha256"
SOURCE_CONTEXT_IMAGE_LABEL = "org.caprmedio.framework.source_context_sha256"
_HOOK_CONFIG_NAMES = frozenset(
    {
        ".huskyrc",
        ".pre-commit-config.yaml",
        ".pre-commit-config.yml",
        "husky.config.cjs",
        "husky.config.js",
        "husky.config.mjs",
        "lefthook.yaml",
        "lefthook.yml",
    }
)


class FrameworkInitializationError(ReleaseContractError):
    """A stable refusal or incomplete state from first-installation only."""

    def __init__(self, code: str, message: str, *, effect_refs: tuple[str, ...] = ()) -> None:
        super().__init__(code, message)
        self.effect_refs = effect_refs


INITIALIZATION_ACTION_ID = "FRAMEWORK_INITIALIZATION"


class DirectActionJournal(Protocol):
    """Minimal injected Journal boundary for an explicit, unselected Action.

    This deliberately has no selected-workflow registry, route, or RunTracker
    dependency.  Its implementation is the sole canonical Journal writer.
    """

    def begin_action(
        self,
        *,
        action_id: str,
        requested_run_id: str,
        intent: Mapping[str, Any],
    ) -> Mapping[str, Any]: ...

    def record_effects(self, run_id: str, *, result_ref: str, effect_refs: list[str]) -> None: ...

    def finish_action(
        self,
        run_id: str,
        *,
        outcome: str,
        result_ref: str,
        effect_refs: list[str],
        report_ref: str | None = None,
    ) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class PackageRow:
    resource: str
    source_path: str
    destination_path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class InitializationPlan:
    """A read-only package plan bound to the observed current source bytes."""

    root: Path
    rows: tuple[PackageRow, ...]
    release: str
    source_context_sha256: str
    manifest_bytes: bytes
    manifest_sha256: str


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _root(project_root: Path | str) -> Path:
    root = Path(project_root).resolve()
    if not root.is_dir() or root.is_symlink():
        raise FrameworkInitializationError("initial-project-invalid", "project root must be a regular directory")
    return root


def _relative(root: Path, path: Path, *, label: str) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise FrameworkInitializationError("initial-path-unsafe", f"{label} escapes the project root") from error


def _safe_path(root: Path, relative: Path, *, create: bool = False) -> Path:
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise FrameworkInitializationError("initial-path-unsafe", "runtime path is unsafe")
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise FrameworkInitializationError("initial-path-unsafe", f"runtime path contains a symlink: {relative.as_posix()}")
        if cursor.exists() and not cursor.is_dir() and cursor != root / relative:
            raise FrameworkInitializationError("initial-path-unsafe", f"runtime path has a non-directory parent: {relative.as_posix()}")
        if create and not cursor.exists():
            cursor.mkdir()
    return cursor


def _safe_file(root: Path, relative: Path, *, code: str) -> Path:
    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise FrameworkInitializationError(error.code, str(error)) from error
    path = root / relative
    for parent in (path, *path.parents):
        if parent == root.parent:
            break
        if parent.is_symlink():
            raise FrameworkInitializationError("initial-path-unsafe", f"source path contains a symlink: {relative.as_posix()}")
        if parent == root:
            break
    if not path.is_file() or path.is_symlink():
        raise FrameworkInitializationError(code, f"required regular file is absent: {relative.as_posix()}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise FrameworkInitializationError("initial-path-unsafe", f"source escapes project: {relative.as_posix()}") from error
    return path


def _regular_files(root: Path, relative: Path, *, code: str) -> list[Path]:
    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise FrameworkInitializationError(error.code, str(error)) from error
    folder = root / relative
    if folder.is_symlink() or not folder.is_dir():
        raise FrameworkInitializationError(code, f"required regular directory is absent: {relative.as_posix()}")
    try:
        files = persistent_regular_files(root, folder)
    except ReleaseInventoryError as error:
        raise FrameworkInitializationError(error.code, str(error)) from error
    if not files:
        raise FrameworkInitializationError(code, f"required directory is empty: {relative.as_posix()}")
    return files


def _assert_empty_boundary(root: Path) -> None:
    selector = root / SELECTOR_RELATIVE
    releases = root / RELEASES_RELATIVE
    # Validate every ancestor, including `.agents`, before a later mkdir can
    # traverse a symlink outside the project root.
    skill_parent = _safe_path(root, Path(PROJECT_SKILL_TARGET).parent, create=False)
    skill = skill_parent / Path(PROJECT_SKILL_TARGET).name
    if os.path.lexists(selector):
        raise FrameworkInitializationError("initial-runtime-not-empty", "first installation requires no current Framework selector")
    if os.path.lexists(releases):
        if releases.is_symlink() or not releases.is_dir():
            raise FrameworkInitializationError("initial-runtime-not-empty", "Framework releases boundary is not empty")
        if any(releases.iterdir()):
            raise FrameworkInitializationError("initial-runtime-not-empty", "first installation requires no retained Framework release")
    if os.path.lexists(skill):
        if skill.is_symlink() or not skill.is_dir():
            raise FrameworkInitializationError("initial-skill-not-empty", "project-local ca Skill boundary is not empty")
        if any(skill.iterdir()):
            raise FrameworkInitializationError("initial-skill-not-empty", "first installation requires no project-local ca Skill")


def _assert_hook_free(skill_root: Path, files: list[Path]) -> None:
    for file in files:
        relative = file.relative_to(skill_root)
        if "hooks" in relative.parts or relative.name in _HOOK_CONFIG_NAMES:
            raise FrameworkInitializationError("initial-skill-hook-forbidden", "initial ca Skill payload contains a hook carrier")


def _obsolete_compiled_copy_exists(root: Path) -> bool:
    """Whether the retired standalone compiled copy could mask a missing role tree."""

    obsolete = root / OBSOLETE_METHODOLOGY_COMPILED_RELATIVE
    if obsolete.is_symlink():
        return True
    if not obsolete.is_dir():
        return False
    try:
        return bool(persistent_regular_files(root, obsolete))
    except ReleaseInventoryError as error:
        raise FrameworkInitializationError(error.code, str(error)) from error


def _compiled_methodology_files(root: Path) -> list[Path]:
    """Read only canonical compiled role folders, never the embedded sources.

    Applicable Methodology has one canonical directory.  Its
    ``000_APPLICABLE_MTHD_sources`` child is separately carried below
    ``METHODOLOGY/sources``; it must not be duplicated in the compiled
    package inventory.
    """

    compiled_root = root / METHODOLOGY_COMPILED_RELATIVE
    if compiled_root.is_symlink() or not compiled_root.is_dir():
        if _obsolete_compiled_copy_exists(root):
            raise FrameworkInitializationError(
                "initial-methodology-compiled-obsolete",
                "only the retired standalone Applicable Methodology copy is available",
            )
        raise FrameworkInitializationError(
            "initial-methodology-compiled-missing",
            "canonical compiled Applicable Methodology directory is absent",
        )

    files: list[Path] = []
    for child in sorted(compiled_root.iterdir(), key=lambda path: path.name):
        if child.name == METHODOLOGY_SOURCES_RELATIVE.name:
            # This directory is intentionally inventoried once through its
            # canonical source root above.
            continue
        if child.name == ".DS_Store":
            continue
        relative = _relative(root, child, label="compiled Methodology role folder")
        if child.is_symlink() or not child.is_dir():
            raise FrameworkInitializationError(
                "initial-methodology-compiled-invalid",
                f"canonical compiled Methodology carrier is not a role folder: {relative}",
            )
        files.extend(_regular_files(root, Path(relative), code="initial-methodology-compiled-missing"))
    if files:
        return files
    if _obsolete_compiled_copy_exists(root):
        raise FrameworkInitializationError(
            "initial-methodology-compiled-obsolete",
            "only the retired standalone Applicable Methodology copy is available",
        )
    raise FrameworkInitializationError(
        "initial-methodology-compiled-missing",
        "canonical Applicable Methodology has no compiled role carriers",
    )


def _package_rows(root: Path) -> tuple[PackageRow, ...]:
    engine_files = _regular_files(root, ENGINE_RELATIVE, code="initial-engine-missing")
    source_files = _regular_files(root, METHODOLOGY_SOURCES_RELATIVE, code="initial-methodology-sources-missing")
    compiled_files = _compiled_methodology_files(root)
    skill_files = _regular_files(root, SKILL_SOURCE_RELATIVE, code="initial-skill-source-missing")
    _assert_hook_free(root / SKILL_SOURCE_RELATIVE, skill_files)

    rows: list[PackageRow] = []
    for path in engine_files:
        if path.is_relative_to(root / SKILL_SOURCE_RELATIVE):
            continue
        relative = path.relative_to(root)
        rows.append(PackageRow("FRAMEWORK_ENGINE", relative.as_posix(), f"FRAMEWORK_ENGINE/{path.relative_to(root / ENGINE_RELATIVE).as_posix()}", _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    for path in source_files:
        relative = path.relative_to(root)
        rows.append(PackageRow("METHODOLOGY", relative.as_posix(), f"METHODOLOGY/sources/{path.relative_to(root / METHODOLOGY_SOURCES_RELATIVE).as_posix()}", _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    for path in compiled_files:
        relative = path.relative_to(root)
        rows.append(PackageRow("METHODOLOGY", relative.as_posix(), f"METHODOLOGY/compiled/{path.relative_to(root / METHODOLOGY_COMPILED_RELATIVE).as_posix()}", _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    for path in skill_files:
        relative = path.relative_to(root)
        rows.append(PackageRow("SKILL", relative.as_posix(), f"SKILLS/ca/{path.relative_to(root / SKILL_SOURCE_RELATIVE).as_posix()}", _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    if not rows:
        raise FrameworkInitializationError("initial-package-incomplete", "initial package inventory is empty")
    destinations = [row.destination_path for row in rows]
    if len(destinations) != len(set(destinations)):
        raise FrameworkInitializationError("initial-package-duplicate", "initial package has duplicate destinations")
    if not any(row.destination_path.startswith("FRAMEWORK_ENGINE/") for row in rows):
        raise FrameworkInitializationError("initial-package-incomplete", "initial package lacks Framework Engine")
    if not any(row.destination_path.startswith("METHODOLOGY/sources/") for row in rows) or not any(row.destination_path.startswith("METHODOLOGY/compiled/") for row in rows):
        raise FrameworkInitializationError("initial-package-incomplete", "initial package lacks complete Methodology")
    required_skill = {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"}
    if not required_skill.issubset(destinations):
        raise FrameworkInitializationError("initial-package-incomplete", "initial package lacks the complete ca control payload")
    return tuple(sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256)))


def _source_context_sha256(rows: tuple[PackageRow, ...]) -> str:
    """Seal exactly the source frontier named by D575.

    Destination paths intentionally do not participate: the source-context is
    the ordered set of source carrier bytes and modes.  The package manifest
    separately binds each source to its delivered destination.
    """

    records = [
        (row.source_path, row.sha256, row.mode)
        for row in sorted(rows, key=lambda row: row.source_path)
    ]
    return _digest(canonical_json(records))


def _release_rows(rows: tuple[PackageRow, ...]) -> list[ReleasePackageRow]:
    """Use the established package-carrier schema without invoking Release Version.

    Initial installation is not a candidate, promotion, or N-to-N+1 action.
    It does, however, emit the same complete PackageRow carrier shape so
    existing read-only runtime/package verifiers can reopen the first N.
    """

    return [
        ReleasePackageRow(
            resource=row.resource,
            source_path=row.source_path,
            destination_path=row.destination_path,
            sha256=row.sha256,
            mode=row.mode,
        )
        for row in rows
    ]


def _manifest(rows: tuple[PackageRow, ...]) -> tuple[bytes, str, str]:
    """Render the package manifest and its two distinct immutable identities."""

    source_context_sha256 = _source_context_sha256(rows)
    # The shared manifest field names a sealed source snapshot.  For the
    # bootstrap package it is exactly the D575 source-context digest, not a
    # Release Version candidate and never a requested/selected workflow ID.
    payload = _render_manifest(source_context_sha256, _release_rows(rows)).encode("utf-8")
    return payload, _digest(payload), source_context_sha256


def _plan_sources(root: Path) -> InitializationPlan:
    """Read and seal source bytes without inspecting runtime publication state."""

    rows = _package_rows(root)
    manifest_bytes, manifest_sha256, source_context_sha256 = _manifest(rows)
    # The content-addressed package directory is addressed by the actual
    # manifest bytes, not by a separately named release or a caller value.
    return InitializationPlan(root, rows, manifest_sha256, source_context_sha256, manifest_bytes, manifest_sha256)


def plan_initial_framework_installation(project_root: Path | str) -> InitializationPlan:
    """Read and seal the only admissible first-install package without writes."""

    root = _root(project_root)
    _assert_empty_boundary(root)
    return _plan_sources(root)


def _validate_image_digest(image_digest: str) -> None:
    if not isinstance(image_digest, str) or not IMAGE_ID.fullmatch(image_digest):
        raise FrameworkInitializationError("initial-image-invalid", "initial runtime requires an immutable image digest")


def _verify_image(executor: DockerExecutor, root: Path, image_digest: str, plan: InitializationPlan) -> None:
    _validate_image_digest(image_digest)
    try:
        observed = executor.run(("docker", "image", "inspect", image_digest), cwd=root, timeout_seconds=60)
    except OSError as error:
        raise FrameworkInitializationError("initial-image-unavailable", "initial image inspection failed") from error
    if not isinstance(observed, DockerCommandResult) or observed.timed_out or observed.exit_code != 0:
        raise FrameworkInitializationError("initial-image-unavailable", "initial image inspection is unavailable")
    try:
        payload = json.loads(observed.stdout)
        inspected = payload[0]
        labels = inspected["Config"]["Labels"]
    except (IndexError, KeyError, TypeError, ValueError) as error:
        raise FrameworkInitializationError("image-package-binding-invalid", "image inspection has no sealed package binding") from error
    if len(payload) != 1 or inspected.get("Id") != image_digest or not isinstance(labels, Mapping):
        raise FrameworkInitializationError("image-package-binding-invalid", "image identity differs from the requested immutable digest")
    if labels.get(PACKAGE_IMAGE_LABEL) != plan.manifest_sha256:
        raise FrameworkInitializationError("image-package-binding-invalid", "image does not bind the exact initial package manifest")
    if labels.get(SOURCE_CONTEXT_IMAGE_LABEL) != plan.source_context_sha256:
        raise FrameworkInitializationError("image-source-context-binding-invalid", "image does not bind the sealed initial source context")


def _atomic_file(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    except BaseException:
        if temporary.exists():
            temporary.unlink()
        raise


def _copy_and_verify(root: Path, source_relative: str, destination: Path, row: PackageRow) -> None:
    source = _safe_file(root, Path(source_relative), code="initial-source-stale")
    payload = source.read_bytes()
    if _digest(payload) != row.sha256 or source.stat().st_mode & 0o777 != row.mode:
        raise FrameworkInitializationError("initial-source-stale", f"source changed after package planning: {source_relative}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as target:
        target.write(payload)
        target.flush()
        os.fsync(target.fileno())
    destination.chmod(row.mode)


def _stage_package(plan: InitializationPlan) -> Path:
    root = plan.root
    releases = _safe_path(root, RELEASES_RELATIVE, create=True)
    if releases.is_symlink() or not releases.is_dir():
        raise FrameworkInitializationError("initial-runtime-not-empty", "Framework release parent is unsafe")
    target = releases / plan.release
    if os.path.lexists(target):
        raise FrameworkInitializationError("initial-runtime-not-empty", "initial package target already exists")
    try:
        staging = Path(tempfile.mkdtemp(prefix=f".initial-{plan.release[:12]}-", dir=releases))
    except OSError as error:
        raise FrameworkInitializationError("initial-package-staging-failed", "initial package staging could not begin") from error
    try:
        for row in plan.rows:
            _copy_and_verify(root, row.source_path, staging / row.destination_path, row)
        _atomic_file(staging / MANIFEST_NAME, plan.manifest_bytes)
        _verify_package(plan, staging)
        try:
            os.replace(staging, target)
        except OSError as error:
            raise FrameworkInitializationError(
                "initial-package-publication-failed",
                "initial package publication could not complete",
                effect_refs=(_relative(root, staging, label="package staging"),),
            ) from error
        directory = os.open(releases, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
        _verify_package(plan, target)
        return target
    except FrameworkInitializationError:
        raise
    except OSError as error:
        raise FrameworkInitializationError(
            "initial-package-publication-failed",
            "initial package staging or verification could not complete",
            effect_refs=(_relative(root, staging, label="package staging"),),
        ) from error
    except BaseException:
        # Retain a failed staging carrier for truthful recovery inspection.
        raise


def _verify_package(plan: InitializationPlan, folder: Path) -> None:
    manifest = folder / MANIFEST_NAME
    if manifest.is_symlink() or not manifest.is_file() or manifest.read_bytes() != plan.manifest_bytes:
        raise FrameworkInitializationError("initial-package-invalid", "initial package manifest differs from the sealed plan")
    if _digest(plan.manifest_bytes) != plan.manifest_sha256:
        raise FrameworkInitializationError("initial-package-invalid", "initial package manifest digest differs from the sealed plan")
    try:
        decoded = tomllib.loads(plan.manifest_bytes.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise FrameworkInitializationError("initial-package-invalid", "initial package manifest is not valid TOML") from error
    expected_records = [
        {
            "resource": row.resource,
            "source_path": row.source_path,
            "destination": row.destination_path,
            "sha256": row.sha256,
            "mode": row.mode,
        }
        for row in _release_rows(plan.rows)
    ]
    if (
        set(decoded) != {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
        or decoded.get("schema_version") != 2
        or decoded.get("package") != PACKAGE_NAME
        or decoded.get("candidate_snapshot_manifest_sha256") != plan.source_context_sha256
        or decoded.get("files") != expected_records
    ):
        raise FrameworkInitializationError("initial-package-invalid", "initial package manifest fields differ from the sealed plan")
    try:
        _verify_release(folder, plan.manifest_bytes.decode("utf-8"), _release_rows(plan.rows))
    except ReleasePackagingError as error:
        raise FrameworkInitializationError("initial-package-invalid", "initial package is not readable by the shared package verifier") from error
    expected = {MANIFEST_NAME, *(row.destination_path for row in plan.rows)}
    actual = {path.relative_to(folder).as_posix() for path in folder.rglob("*") if path.is_file()}
    if actual != expected:
        raise FrameworkInitializationError("initial-package-incomplete", "initial package inventory differs from the sealed plan")
    for row in plan.rows:
        target = folder / row.destination_path
        if target.is_symlink() or not target.is_file() or _digest(target.read_bytes()) != row.sha256 or target.stat().st_mode & 0o777 != row.mode:
            raise FrameworkInitializationError("initial-package-invalid", f"initial package member differs: {row.destination_path}")


def _selector(plan: InitializationPlan, image_digest: str) -> bytes:
    release_root = f"{RELEASES_RELATIVE.as_posix()}/{plan.release}"
    values = {
        "schema_version": 1,
        "manifest_sha256": plan.manifest_sha256,
        "release": plan.release,
        "selected_release_root": release_root,
        "framework_engine_root": release_root + "/FRAMEWORK_ENGINE",
        "methodology_root": release_root + "/METHODOLOGY",
        "image_digest": image_digest,
    }
    lines = [f"{key} = {json.dumps(value)}" for key, value in values.items()]
    return ("\n".join(lines) + "\n").encode("utf-8")


def _publish_skill(plan: InitializationPlan, package: Path) -> Path:
    root = plan.root
    # Reopen the complete ancestor chain immediately before staging/copying.
    # `_assert_empty_boundary` made the same check before package work, but a
    # filesystem race must not turn `.agents` into an escape route meanwhile.
    parent = _safe_path(root, Path(PROJECT_SKILL_TARGET).parent, create=True)
    target = parent / Path(PROJECT_SKILL_TARGET).name
    if os.path.lexists(target):
        if target.is_symlink() or not target.is_dir() or any(target.iterdir()):
            raise FrameworkInitializationError("initial-skill-not-empty", "project-local ca Skill changed before publication")
    try:
        staging = Path(tempfile.mkdtemp(prefix=".ca-initial-", dir=parent))
        source = package / "SKILLS/ca"
        for path in sorted(source.rglob("*")):
            relative = path.relative_to(source)
            output = staging / relative
            if path.is_dir():
                output.mkdir(exist_ok=True)
            elif path.is_file() and not path.is_symlink():
                output.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, output)
                output.chmod(path.stat().st_mode & 0o777)
            else:
                raise FrameworkInitializationError("initial-skill-invalid", "sealed Skill has an unsafe carrier")
        expected = {path.relative_to(source).as_posix(): path.read_bytes() for path in source.rglob("*") if path.is_file()}
        actual = {path.relative_to(staging).as_posix(): path.read_bytes() for path in staging.rglob("*") if path.is_file()}
        if actual != expected:
            raise FrameworkInitializationError("initial-skill-invalid", "staged project Skill differs from the sealed package")
        try:
            os.replace(staging, target)
        except OSError as error:
            raise FrameworkInitializationError(
                "initial-skill-publication-failed",
                "project-local ca Skill publication could not complete",
                effect_refs=(_relative(root, staging, label="Skill staging"),),
            ) from error
        directory = os.open(parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
        return target
    except FrameworkInitializationError:
        raise
    except OSError as error:
        staging_ref = ()
        if "staging" in locals() and staging.exists():
            staging_ref = (_relative(root, staging, label="Skill staging"),)
        raise FrameworkInitializationError(
            "initial-skill-publication-failed",
            "project-local ca Skill staging or publication could not complete",
            effect_refs=staging_ref,
        ) from error
    except BaseException:
        # Retain staged bytes for recovery inspection; never retry blindly.
        raise


def _write_result(root: Path, release: str, payload: Mapping[str, Any]) -> str:
    relative = INITIALIZATION_EVIDENCE_RELATIVE / release / "result.json"
    try:
        _atomic_file(root / relative, canonical_json(dict(payload)))
    except OSError as error:
        raise FrameworkInitializationError("initial-result-recording-unavailable", "initial installation result carrier could not be written") from error
    return relative.as_posix()


def _journal_start(
    journal: DirectActionJournal,
    requested_run_id: str,
    plan: InitializationPlan,
    image_digest: str,
) -> str:
    if not isinstance(requested_run_id, str) or not requested_run_id:
        raise FrameworkInitializationError("initial-run-invalid", "requested Action Run ID is required")
    intent = {
        "action_id": INITIALIZATION_ACTION_ID,
        "kind": "first_framework_runtime_installation",
        "manifest_sha256": plan.manifest_sha256,
        "source_context_sha256": plan.source_context_sha256,
        "image_digest": image_digest,
    }
    try:
        started = journal.begin_action(
            action_id=INITIALIZATION_ACTION_ID,
            requested_run_id=requested_run_id,
            intent=intent,
        )
        run_id = started.get("run_id") if isinstance(started, Mapping) else None
    except Exception as error:
        # A direct Action Journal can refuse a repeated or recoverable intent.
        # Preserve that stable refusal rather than relabelling it as an
        # infrastructure outage: callers must not treat it as permission to
        # replay a possibly effected installation.
        code = getattr(error, "code", None)
        if isinstance(code, str) and code.startswith("direct-action-"):
            raise FrameworkInitializationError(code, str(error)) from error
        raise FrameworkInitializationError("initial-journal-start-unavailable", "canonical started Action evidence is unavailable") from error
    if not isinstance(run_id, str) or not run_id or started.get("disposition") != "started":
        raise FrameworkInitializationError("initial-journal-start-unavailable", "canonical started Action evidence has no Run ID")
    return run_id


def _terminalize(
    journal: DirectActionJournal,
    run_id: str,
    *,
    outcome: str,
    result_ref: str,
    effect_refs: list[str],
) -> Mapping[str, Any]:
    try:
        journal.record_effects(run_id, result_ref=result_ref, effect_refs=effect_refs)
        terminal = journal.finish_action(run_id, outcome=outcome, result_ref=result_ref, effect_refs=effect_refs)
    except Exception as error:
        raise FrameworkInitializationError("initial-journal-terminal-unavailable", "canonical terminal Action evidence is unavailable") from error
    if not isinstance(terminal, Mapping):
        raise FrameworkInitializationError("initial-journal-terminal-unavailable", "canonical terminal Action evidence is invalid")
    return terminal


def initialize_framework_runtime(
    project_root: Path | str,
    *,
    journal: DirectActionJournal,
    requested_run_id: str,
    image_digest: str,
    image_executor: DockerExecutor,
) -> dict[str, Any]:
    """Perform one explicit first install with shared Run evidence.

    A completed return is possible only when the package, selector, exact
    project Skill, immutable image and canonical terminal Action receipt all
    agree.  If canonical terminal recording is unavailable after publication,
    the real published carriers remain in place and the result is explicitly
    ``recording_pending``; the Action never rolls back or replays an
    uncertain effect.
    """

    root = _root(project_root)
    package: Path | None = None
    selector_published = False
    skill_published = False
    # Seal source identity first, write canonical started evidence for exactly
    # that identity, then admit the empty publication boundary before effects.
    plan = _plan_sources(root)
    _validate_image_digest(image_digest)
    run_id = _journal_start(journal, requested_run_id, plan, image_digest)
    try:
        _assert_empty_boundary(root)
        _verify_image(image_executor, root, image_digest, plan)
        package = _stage_package(plan)
        _verify_package(plan, package)
        # Source bytes must remain exactly the planned source frontier before
        # any active selector or public Skill is published.
        if _package_rows(root) != plan.rows:
            raise FrameworkInitializationError("initial-source-stale", "source changed after sealed package staging")
        _publish_skill(plan, package)
        skill_published = True
        # The public Skill must be complete before the selector makes this
        # package active.  The selector is deliberately the final activation
        # point; separate directory publications are not one transaction.
        try:
            _atomic_file(root / SELECTOR_RELATIVE, _selector(plan, image_digest))
        except OSError as error:
            raise FrameworkInitializationError(
                "initial-selector-publication-failed",
                "initial Framework selector publication could not complete",
            ) from error
        selector_published = True
        result_ref = _write_result(
            root,
            plan.release,
            {
                # The package is published, but it is not a completed
                # installation until the sole Journal writer produces its
                # terminal receipt.
                "state": "published_pending_terminal",
                "release": plan.release,
                "manifest_sha256": plan.manifest_sha256,
                "image_digest": image_digest,
                "release_root": _relative(root, package, label="release root"),
            },
        )
        effect_refs = [_relative(root, package, label="release root"), SELECTOR_RELATIVE.as_posix(), PROJECT_SKILL_TARGET, result_ref]
        terminal = _terminalize(journal, run_id, outcome="completed", result_ref=result_ref, effect_refs=effect_refs)
        if terminal.get("disposition") != "terminal" or terminal.get("outcome") != "completed":
            return {
                "state": "recording_pending",
                "reason": "canonical-terminal-evidence-pending",
                "release": plan.release,
                "manifest_sha256": plan.manifest_sha256,
                "result_ref": result_ref,
                "terminal": dict(terminal),
            }
        return {
            "state": "installed",
            "release": plan.release,
            "manifest_sha256": plan.manifest_sha256,
            "image_digest": image_digest,
            "release_root": _relative(root, package, label="release root"),
            "result_ref": result_ref,
            "terminal": dict(terminal),
        }
    except FrameworkInitializationError as error:
        effects: list[str] = list(error.effect_refs)
        if package is not None:
            effects.append(_relative(root, package, label="release root"))
        if selector_published:
            effects.append(SELECTOR_RELATIVE.as_posix())
        if skill_published:
            effects.append(PROJECT_SKILL_TARGET)
        if error.code in {"initial-journal-terminal-unavailable", "initial-result-recording-unavailable"}:
            # Publication has already happened.  Its exact outcome is no
            # longer safe to replay or compensate until the sole Journal
            # writer records it, so retain carriers and report that fact.
            return {
                "state": "recording_pending",
                "reason": error.code,
                "release": plan.release,
                "manifest_sha256": plan.manifest_sha256,
                "effect_refs": effects,
                "terminal": None,
            }
        state = "partial" if effects or package is not None or selector_published or skill_published else "blocked"
        try:
            result_ref = _write_result(root, plan.release, {"state": state, "reason": error.code, "message": str(error)})
            effects.append(result_ref)
            terminal = _terminalize(
                journal,
                run_id,
                outcome="partial" if state == "partial" else "failed",
                result_ref=result_ref,
                effect_refs=effects,
            )
            if terminal.get("disposition") != "terminal":
                state = "recording_pending"
            return {"state": state, "reason": error.code, "result_ref": result_ref, "terminal": dict(terminal)}
        except FrameworkInitializationError:
            return {"state": "recording_pending", "reason": error.code, "terminal": None}


__all__ = [
    "FrameworkInitializationError",
    "InitializationPlan",
    "INITIALIZATION_ACTION_ID",
    "DirectActionJournal",
    "PACKAGE_IMAGE_LABEL",
    "SOURCE_CONTEXT_IMAGE_LABEL",
    "initialize_framework_runtime",
    "plan_initial_framework_installation",
]
