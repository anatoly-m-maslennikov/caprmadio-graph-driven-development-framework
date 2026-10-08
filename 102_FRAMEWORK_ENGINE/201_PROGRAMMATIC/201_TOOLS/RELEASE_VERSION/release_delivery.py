"""Deliver the complete bound Methodology source tree to its fixed derived root.

No compiler, selector, canonical source, Projection, or Journal is modified.
An owned predecessor is retained beside the delivery for repair or rollback.
"""

from __future__ import annotations

import os
import stat
import tempfile
import tomllib
from dataclasses import dataclass
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
from release_inventory import _is_ephemeral_file, ReleaseInventoryError, persistent_regular_files, refuse_secret_path
from release_packaging import (
    MANIFEST_NAME,
    RUNTIME_ROOT,
    ReleasePackagingError,
    _candidate_sha256,
    _render_manifest,
    _verify_release,
)
from release_predecessor import verify_recorded_source_predecessor
from release_suite import _bootstrap_prior_manifest_is_exact


class ReleaseDeliveryError(ReleaseContractError):
    """Refusal with retained project-relative recovery carriers, if any."""

    def __init__(self, code: str, message: str, *, recovery_paths: tuple[str, ...] = ()) -> None:
        self.recovery_paths = recovery_paths
        super().__init__(code, message)


@dataclass
class _PredecessorReservation:
    """A retained private wrapper and its one permitted predecessor child."""

    parent: Path
    wrapper: Path
    backup: Path
    target_name: str
    parent_identity: tuple[int, int] | None = None
    wrapper_identity: tuple[int, int] | None = None
    backup_identity: tuple[int, int] | None = None


def _safe_path(root: Path, relative: str) -> Path:
    cursor = root
    for part in Path(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"symlink component is not admitted: {relative}")
        if os.path.lexists(cursor) and cursor != root / relative and not cursor.is_dir():
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"non-directory ancestor: {relative}")
    return cursor


def _nofollow_directory_identity(path: Path, *, label: str) -> tuple[int, int]:
    """Return a directory's nofollow identity, refusing substituted carriers."""

    try:
        observed = os.stat(path, follow_symlinks=False)
    except OSError as error:
        raise ReleaseDeliveryError("release-copy-path-unsafe", f"{label} is unavailable") from error
    if not stat.S_ISDIR(observed.st_mode):
        raise ReleaseDeliveryError("release-copy-path-unsafe", f"{label} is not a regular directory")
    return observed.st_dev, observed.st_ino


def _validate_reservation(
    reservation: _PredecessorReservation,
    *,
    require_absent_backup: bool = False,
    require_owned_backup: bool = False,
) -> None:
    """Confirm that a private reservation still names exactly its own child."""

    wrapper = reservation.wrapper
    backup = reservation.backup
    if (
        wrapper.parent != reservation.parent
        or wrapper != reservation.parent / wrapper.name
        or not wrapper.name.startswith(".release-sources-prior-private-")
        or backup.parent != wrapper
        or backup != wrapper / reservation.target_name
        or backup.name != reservation.target_name
    ):
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor reservation path changed")
    if reservation.parent_identity is None or reservation.wrapper_identity is None:
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor reservation was not bound")
    if _nofollow_directory_identity(reservation.parent, label="predecessor reservation parent") != reservation.parent_identity:
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor reservation parent changed")
    if _nofollow_directory_identity(wrapper, label="predecessor reservation") != reservation.wrapper_identity:
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor reservation changed")
    if require_absent_backup and os.path.lexists(backup):
        raise ReleaseDeliveryError("release-copy-collision", "predecessor backup child is not absent")
    if require_owned_backup:
        if reservation.backup_identity is None:
            raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor backup was not recorded")
        if _nofollow_directory_identity(backup, label="predecessor backup") != reservation.backup_identity:
            raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor backup changed")


def _reserve_predecessor(parent: Path, destination: Path) -> _PredecessorReservation:
    """Reserve a retained wrapper; the old tree may move only into its child."""

    wrapper = Path(tempfile.mkdtemp(prefix=".release-sources-prior-private-", dir=parent))
    # Return the carrier before any observation can refuse it.  A caller can
    # then expose this retained wrapper (and any hostile child) for recovery.
    return _PredecessorReservation(
        parent=parent,
        wrapper=wrapper,
        backup=wrapper / destination.name,
        target_name=destination.name,
    )


def _bind_reservation_identity(reservation: _PredecessorReservation) -> None:
    """Bind a returned private wrapper before it can receive the old tree."""

    reservation.parent_identity = _nofollow_directory_identity(
        reservation.parent, label="predecessor reservation parent",
    )
    reservation.wrapper_identity = _nofollow_directory_identity(
        reservation.wrapper, label="predecessor reservation",
    )
    _validate_reservation(reservation, require_absent_backup=True)


def _record_predecessor_backup(
    reservation: _PredecessorReservation,
    expected_identity: tuple[int, int],
) -> None:
    """Record the actual old tree immediately after its atomic move."""

    _validate_reservation(reservation)
    if _nofollow_directory_identity(reservation.backup, label="predecessor backup") != expected_identity:
        raise ReleaseDeliveryError("release-copy-path-unsafe", "predecessor backup does not match the proven old tree")
    reservation.backup_identity = expected_identity


def _snapshot(folder: Path) -> dict[str, tuple[bool, int, bytes]]:
    """Read all files, directories, empty directories and observed modes."""

    if folder.is_symlink() or not folder.is_dir():
        raise ReleaseDeliveryError("release-copy-collision", "delivery tree is not a regular directory")
    records = {"": (True, folder.stat().st_mode & 0o777, b"")}
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder).as_posix()
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise ReleaseDeliveryError("release-copy-path-unsafe", f"unsafe source or delivery carrier: {relative}")
        try:
            # Check every component before a metadata exclusion: a secret
            # name remains forbidden even when its regular-file suffix is
            # otherwise ephemeral (for example ``.env.pyc``).
            refuse_secret_path(relative)
        except ReleaseInventoryError as error:
            raise ReleaseDeliveryError("release-copy-path-unsafe", "secret-shaped source or delivery carrier is not admitted") from error
        # Persistent source-copy identity deliberately excludes Finder
        # metadata and bytecode.  Unsafe carriers were refused above; retain
        # every directory and every non-ephemeral regular file exactly.
        if path.is_file() and _is_ephemeral_file(path.name):
            continue
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


def _prove_owned_predecessor(root: Path, candidate: ValidatedCandidate, destination: Path) -> None:
    """Accept either the retained N package or the one recorded old delivery."""

    try:
        _prove_predecessor(root, candidate, destination)
    except ReleaseDeliveryError as error:
        if error.code != "release-copy-predecessor-mismatch":
            raise
        if not verify_recorded_source_predecessor(root, candidate.authority.executing_release, destination):
            raise error


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
        _prove_owned_predecessor(root, current, destination)
    parent = destination.parent
    if not parent.exists():
        parent.mkdir()
    staging = Path(tempfile.mkdtemp(prefix=f".release-sources-{current.manifest.sha256[:12]}-", dir=parent))
    reservation: _PredecessorReservation | None = None
    try:
        _write_snapshot(staging, records)
        if _snapshot(staging) != records or tree_sha256(root, staging) != current.manifest.expected_derived_source_copy_sha256:
            raise ReleaseDeliveryError("release-copy-digest-mismatch", "staged full source bytes or modes differ")
        _admit(current)
        if _snapshot(source) != records:
            raise ReleaseDeliveryError("release-currentness-stale", "canonical source tree changed during delivery")
        _safe_path(root, DERIVED_SOURCE_COPY_RELATIVE)
        if existing:
            # Retain the private wrapper for recovery.  Only its still-absent
            # fixed child may receive the owned old delivery; do not remove
            # and reuse the wrapper itself as a rename target.
            reservation = _reserve_predecessor(parent, destination)
            _bind_reservation_identity(reservation)
            predecessor_identity = _nofollow_directory_identity(destination, label="owned predecessor")
            _prove_owned_predecessor(root, current, destination)
            if _nofollow_directory_identity(destination, label="owned predecessor") != predecessor_identity:
                raise ReleaseDeliveryError("release-copy-predecessor-mismatch", "owned predecessor changed during delivery")
            _validate_reservation(reservation, require_absent_backup=True)
            destination.rename(reservation.backup)
            _record_predecessor_backup(reservation, predecessor_identity)
        elif os.path.lexists(destination):
            raise ReleaseDeliveryError("release-copy-collision", "delivery target appeared while staging")
        staging.rename(destination)
        result = validate_source_copy(_admit(current))
        if _snapshot(destination) != records or _snapshot(source) != records:
            raise ReleaseDeliveryError("release-copy-digest-mismatch", "completed delivery bytes or modes changed")
        return result
    except Exception as error:
        # Restore N's derived tree only from the exact child that received it
        # and only while no other target exists.  The empty private wrapper is
        # retained and is never itself a source-delivery candidate.
        if (
            reservation is not None
            and reservation.backup_identity is not None
            and not os.path.lexists(destination)
        ):
            try:
                _validate_reservation(reservation, require_owned_backup=True)
                reservation.backup.rename(destination)
            except (OSError, ReleaseDeliveryError):
                pass
        recovery = tuple(
            path.relative_to(root).as_posix()
            for path in (
                staging,
                None if reservation is None else reservation.wrapper,
                None if reservation is None else reservation.backup,
                destination,
            )
            if path is not None and os.path.lexists(path)
        )
        code = error.code if isinstance(error, ReleaseContractError) else "release-copy-failed"
        raise ReleaseDeliveryError(code, f"source delivery did not complete; retained recovery carriers: {recovery}",
                                   recovery_paths=recovery) from error


__all__ = ["ReleaseDeliveryError", "deliver_release_sources"]
