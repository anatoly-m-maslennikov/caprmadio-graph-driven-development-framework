"""Deliver the complete bound Methodology source tree to its fixed derived root.

No compiler, selector, canonical source, Projection, or Journal is modified.
An owned predecessor is retained beside the delivery for repair or rollback.
"""

from __future__ import annotations

import os
import tempfile
import tomllib
from pathlib import Path

from bootstrap_image import BootstrapImageError, _retained_initial_package
from release_contract import ReleaseContractError, ValidatedCandidate
from release_handoff import (
    CANONICAL_SOURCE_RELATIVE,
    CURRENT_SELECTOR_RELATIVE,
    DERIVED_SOURCE_COPY_RELATIVE,
    PROJECT_STRUCTURE_RELATIVE,
    PackageRow,
    SealedSourceCopy,
    _revalidate,
    tree_sha256,
    validate_source_copy,
)
from release_inventory import ReleaseInventoryError, persistent_regular_files
from release_packaging import (
    MANIFEST_NAME,
    RUNTIME_ROOT,
    ReleasePackagingError,
    _candidate_sha256,
    _render_manifest,
    _verify_release,
)
from release_suite import _bootstrap_prior_manifest_is_exact


class ReleaseDeliveryError(ReleaseContractError):
    """Refusal with retained project-relative recovery carriers, if any."""

    def __init__(self, code: str, message: str, *, recovery_paths: tuple[str, ...] = ()) -> None:
        self.recovery_paths = recovery_paths
        super().__init__(code, message)


def _safe_path(root: Path, relative: str) -> Path:
    cursor = root
    for part in Path(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"symlink component is not admitted: {relative}")
        if os.path.lexists(cursor) and cursor != root / relative and not cursor.is_dir():
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"non-directory ancestor: {relative}")
    return cursor


def _snapshot(folder: Path) -> dict[str, tuple[bool, int, bytes]]:
    """Read all files, directories, empty directories and observed modes."""

    if folder.is_symlink() or not folder.is_dir():
        raise ReleaseDeliveryError("release-copy-collision", "delivery tree is not a regular directory")
    records = {"": (True, folder.stat().st_mode & 0o777, b"")}
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder).as_posix()
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"unsafe source or delivery carrier: {relative}")
        records[relative] = (path.is_dir(), path.stat().st_mode & 0o777, b"" if path.is_dir() else path.read_bytes())
    return records


def _write_snapshot(folder: Path, records: dict[str, tuple[bool, int, bytes]]) -> None:
    for relative, (directory, mode, payload) in records.items():
        target = folder / relative
        if directory:
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(payload)
            target.chmod(mode)
    # Apply directory modes only once all children have been written.
    for relative in sorted(records, key=lambda item: len(Path(item).parts), reverse=True):
        directory, mode, _payload = records[relative]
        if directory:
            (folder / relative).chmod(mode)


def _persistent_file_snapshot(root: Path, folder: Path) -> dict[str, tuple[int, bytes]]:
    """Read persisted predecessor bytes/modes using the sealed inventory rules."""

    try:
        return {
            path.relative_to(folder).as_posix(): (path.stat().st_mode & 0o777, path.read_bytes())
            for path in persistent_regular_files(root, folder)
        }
    except ReleaseInventoryError as error:
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor inventory is unsafe") from error


def _admit(candidate: ValidatedCandidate) -> ValidatedCandidate:
    if not isinstance(candidate, ValidatedCandidate):
        raise ReleaseDeliveryError("release-candidate-untrusted", "delivery requires a typed locally validated candidate")
    root = Path(candidate.project_root)
    for relative in (CANONICAL_SOURCE_RELATIVE, CURRENT_SELECTOR_RELATIVE, PROJECT_STRUCTURE_RELATIVE,
                     *(row.source_path for row in candidate.manifest.source_inventory_rows)):
        _safe_path(root, relative)
    current = _revalidate(candidate)
    if current.manifest.expected_derived_source_copy_sha256 != current.authority.canonical_source_snapshot_digest:
        raise ReleaseDeliveryError("release-copy-digest-mismatch", "complete source-copy expectation differs from canonical bytes")
    return current


def _prove_predecessor(root: Path, candidate: ValidatedCandidate, destination: Path) -> None:
    """Admit replacement only from an exact, complete retained executing N."""

    executing = candidate.authority.executing_release
    relative = (RUNTIME_ROOT / "releases" / executing).as_posix()
    retained = _safe_path(root, relative)
    manifest_path = _safe_path(root, f"{relative}/{MANIFEST_NAME}")
    selector_path = _safe_path(root, CURRENT_SELECTOR_RELATIVE)
    try:
        if not manifest_path.is_file() or not selector_path.is_file():
            raise ValueError("retained executing package manifest is absent")
        manifest_bytes = manifest_path.read_bytes()
        text = manifest_bytes.decode("utf-8")
        manifest = tomllib.loads(text)
        selector = tomllib.loads(selector_path.read_text(encoding="utf-8"))
        bootstrap = (
            isinstance(selector, dict)
            and _bootstrap_prior_manifest_is_exact(selector, manifest_bytes, executing)
        )
        if bootstrap:
            # First-install N identifies its release by the exact manifest
            # digest and its rows by the immutable source-context digest.
            # Reuse the canonical retained-package reader; the selector
            # binding above keeps this exception closed to that bootstrap N.
            retained, bootstrap_rows, _manifest, identity = _retained_initial_package(root, executing)
            rows = list(bootstrap_rows)
        else:
            if set(manifest) != {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}:
                raise ValueError("retained package manifest has unexpected members")
            identity = _candidate_sha256(manifest["candidate_snapshot_manifest_sha256"])
            if manifest["schema_version"] != 2 or manifest["package"] != "caprmedio-framework" or identity != executing:
                raise ValueError("retained package does not identify executing N")
            rows = []
            for row in manifest["files"]:
                if set(row) != {"resource", "source_path", "destination", "sha256", "mode"}:
                    raise ValueError("retained package row has unexpected members")
                rows.append(PackageRow.model_validate({**{key: value for key, value in row.items() if key != "destination"},
                                                      "destination_path": row["destination"]}))
        if len({row.destination_path for row in rows}) != len(rows):
            raise ValueError("retained package destinations collide")
        if not {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"} <= {row.resource for row in rows}:
            raise ValueError("retained executing package is incomplete")
        if not {"SKILLS/ca/SKILL.md", "SKILLS/ca/agents/openai.yaml"} <= {row.destination_path for row in rows}:
            raise ValueError("retained executing package lacks required Skill files")
        if rows != sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256)):
            raise ValueError("retained package rows are not ordered")
        _verify_release(retained, text if bootstrap else _render_manifest(identity, rows), rows)
        source_rows = [row for row in rows if row.destination_path.startswith("METHODOLOGY/sources/")]
        if not source_rows:
            raise ValueError("retained package lacks Methodology sources")
        for row in source_rows:
            suffix = row.destination_path.removeprefix("METHODOLOGY/sources/")
            if row.resource != "METHODOLOGY" or row.source_path != f"{CANONICAL_SOURCE_RELATIVE}/{suffix}":
                raise ValueError("retained source row does not bind canonical Methodology")
        predecessor = _persistent_file_snapshot(root, retained / "METHODOLOGY/sources")
    except (BootstrapImageError, OSError, UnicodeDecodeError, ValueError, KeyError, TypeError, ReleasePackagingError) as error:
        raise ReleaseDeliveryError("release-copy-ownership-unproven", "cannot prove complete retained executing-N ownership") from error
    if _persistent_file_snapshot(root, destination) != predecessor:
        raise ReleaseDeliveryError("release-copy-predecessor-mismatch", "existing delivery is partial, changed, or contains unowned files")
    # Empty directories have no package byte rows. Retain the whole old tree,
    # including these directories, rather than deleting an unproven carrier.


def deliver_release_sources(candidate: ValidatedCandidate) -> SealedSourceCopy:
    """Copy fixed canonical source bytes/modes and return actual D567 proof.

    Different deliveries require complete executing-package predecessor proof.
    Failures preserve any staging/predecessor trees and expose recovery paths.
    """

    current = _admit(candidate)
    root = Path(current.project_root)
    source = _safe_path(root, CANONICAL_SOURCE_RELATIVE)
    destination = _safe_path(root, DERIVED_SOURCE_COPY_RELATIVE)
    records = _snapshot(source)
    existing = os.path.lexists(destination)
    if existing:
        actual = _snapshot(destination)
        if actual == records:
            return validate_source_copy(_admit(current))
        _prove_predecessor(root, current, destination)
    parent = destination.parent
    if not parent.exists():
        parent.mkdir()
    staging = Path(tempfile.mkdtemp(prefix=f".release-sources-{current.manifest.sha256[:12]}-", dir=parent))
    predecessor: Path | None = None
    try:
        _write_snapshot(staging, records)
        if _snapshot(staging) != records or tree_sha256(root, staging) != current.manifest.expected_derived_source_copy_sha256:
            raise ReleaseDeliveryError("release-copy-digest-mismatch", "staged full source bytes or modes differ")
        _admit(current)
        if _snapshot(source) != records:
            raise ReleaseDeliveryError("release-currentness-stale", "canonical source tree changed during delivery")
        _safe_path(root, DERIVED_SOURCE_COPY_RELATIVE)
        if existing:
            _prove_predecessor(root, current, destination)
            predecessor = Path(tempfile.mkdtemp(prefix=".release-sources-prior-", dir=parent))
            predecessor.rmdir()  # Only the just-created empty reservation.
            destination.rename(predecessor)
        elif os.path.lexists(destination):
            raise ReleaseDeliveryError("release-copy-collision", "delivery target appeared while staging")
        staging.rename(destination)
        result = validate_source_copy(_admit(current))
        if _snapshot(destination) != records or _snapshot(source) != records:
            raise ReleaseDeliveryError("release-copy-digest-mismatch", "completed delivery bytes or modes changed")
        return result
    except Exception as error:
        # Restore N's derived tree if publication failed before a new target
        # existed. Never replace a target that another actor created.
        if predecessor is not None and predecessor.exists() and not os.path.lexists(destination):
            try:
                predecessor.rename(destination)
            except OSError:
                pass
        recovery = tuple(path.relative_to(root).as_posix() for path in (staging, predecessor, destination)
                         if path is not None and os.path.lexists(path))
        code = error.code if isinstance(error, ReleaseContractError) else "release-copy-failed"
        raise ReleaseDeliveryError(code, f"source delivery did not complete; retained recovery carriers: {recovery}",
                                   recovery_paths=recovery) from error


__all__ = ["ReleaseDeliveryError", "deliver_release_sources"]
