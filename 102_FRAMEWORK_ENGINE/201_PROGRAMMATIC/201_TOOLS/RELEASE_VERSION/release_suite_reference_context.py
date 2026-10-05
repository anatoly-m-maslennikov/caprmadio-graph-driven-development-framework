"""Private, read-only control-reference closure for the Release suite.

This is intentionally below the Suite Owner boundary.  It has no request,
MCP, Journal, manifest-publication, or candidate-inventory interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
import tomllib
from types import MappingProxyType
from typing import Any, Mapping, Sequence

_MCP_ROOT = Path(__file__).resolve().parents[2] / "204_MCP"
if not _MCP_ROOT.is_dir():  # pragma: no cover - immutable carrier installation failure
    raise RuntimeError("Release suite control reader carrier is unavailable")
if str(_MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(_MCP_ROOT))

from release_source_admission import (  # noqa: E402
    AUTHORITY_PIN,
    ReleaseSourceAdmissionError,
    _private_carriers,
    derive_release_private_carriers,
    derive_release_source_admission,
)
from selected_routes import PROJECT_SETTINGS_REF, canonical_json, load_selected_manifest, selected_manifest_ref  # noqa: E402


_OPERATORS_REGISTRY = PurePosixPath(".caprmedio_caprmedio/operators_registry.toml")
_BINDING_FIELDS = frozenset({
    "candidate_snapshot_manifest_sha256", "compiled_candidate_root",
    "selected_n_identity", "selected_n_image_context",
})
_SHA256 = re.compile(r"[0-9a-f]{64}")
_IDENTITY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,255}")


class ReleaseSuiteReferenceContextError(ValueError):
    """A Suite Owner cannot establish the closed control-reference context."""


@dataclass(frozen=True)
class ReferenceRow:
    source_path: str
    sha256: str
    mode: int

    def as_dict(self) -> dict[str, object]:
        return {"source_path": self.source_path, "sha256": self.sha256, "mode": self.mode}


@dataclass(frozen=True)
class ReleaseSuiteReferenceContext:
    """Captured bytes and immutable identity for one private suite attempt."""

    root: str
    trusted_binding_values: tuple[tuple[str, str], ...]
    reference_rows: tuple[ReferenceRow, ...]
    control_context_digest: str
    _verified_bytes: tuple[tuple[str, bytes], ...]

    def bindings(self) -> Mapping[str, str]:
        return MappingProxyType(dict(self.trusted_binding_values))


def _fail(message: str) -> None:
    raise ReleaseSuiteReferenceContextError(message)


def _root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseSuiteReferenceContextError("Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        _fail("Project root must be a regular directory")
    return root


def _safe_relative(value: object) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        _fail("reference path must be a non-empty canonical Project-relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or not path.parts or path.as_posix() != value or any(part in {".", ".."} for part in path.parts):
        _fail("reference path must be a non-escaping canonical Project-relative path")
    return path


def _forbid_non_control_path(value: object) -> PurePosixPath:
    """Reject path classes before a context can cause an I/O operation."""
    path = _safe_relative(value)
    parts = path.parts
    if (
        parts[0] == ".caprmedio_runtime"
        or "_journal" in parts
        or "output" in parts
        or any(part == ".env" or part.startswith(".env.") for part in parts)
    ):
        _fail("reference path is outside the private control-reference allowlist")
    return path


def _read_regular(root: Path, relative: str) -> tuple[bytes, int]:
    """Read one control carrier by descriptor, refusing every symlink race."""
    path = _forbid_non_control_path(relative)
    required = ("O_NOFOLLOW", "O_DIRECTORY")
    if any(not hasattr(os, flag) for flag in required) or not os.supports_dir_fd:
        _fail("host cannot provide no-follow descriptor traversal")
    root_fd = parent_fd = file_fd = None
    try:
        root_fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        parent_fd = root_fd
        for part in path.parts[:-1]:
            next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd)
            if parent_fd != root_fd:
                os.close(parent_fd)
            parent_fd = next_fd
        file_fd = os.open(path.parts[-1], os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
        before = os.fstat(file_fd)
        if not stat.S_ISREG(before.st_mode):
            _fail(f"reference is not a regular file: {relative}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(file_fd, 64 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(file_fd)
        if (before.st_dev, before.st_ino, before.st_mode, before.st_size, before.st_mtime_ns) != (
                after.st_dev, after.st_ino, after.st_mode, after.st_size, after.st_mtime_ns):
            _fail(f"reference changed while it was read: {relative}")
        return b"".join(chunks), before.st_mode & 0o777
    except ReleaseSuiteReferenceContextError:
        raise
    except OSError as error:
        raise ReleaseSuiteReferenceContextError(f"reference is unreadable: {relative}") from error
    finally:
        for descriptor in (file_fd, parent_fd, root_fd):
            if descriptor is not None:
                try:
                    os.close(descriptor)
                except OSError:
                    pass


def _bindings(value: Mapping[str, Any]) -> tuple[tuple[str, str], ...]:
    if not isinstance(value, Mapping) or set(value) != _BINDING_FIELDS:
        _fail("trusted binding values have an incomplete or unknown schema")
    normalized: dict[str, str] = {}
    for key in _BINDING_FIELDS:
        item = value[key]
        if not isinstance(item, str) or not item or "\n" in item or "\r" in item:
            _fail(f"trusted binding {key} must be a non-empty single-line value")
        if key == "candidate_snapshot_manifest_sha256":
            if _SHA256.fullmatch(item) is None:
                _fail("trusted candidate manifest digest must be lowercase SHA-256")
        elif key == "compiled_candidate_root":
            _safe_relative(item)
        elif _IDENTITY.fullmatch(item) is None:
            _fail(f"trusted binding {key} has an unsafe identity shape")
        normalized[key] = item
    return tuple(sorted(normalized.items()))


def _paths_from_source_paths(value: Any, paths: list[str]) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key == "source_path":
                _safe_relative(child)
                paths.append(str(child))
            else:
                _paths_from_source_paths(child, paths)
    elif isinstance(value, list):
        for child in value:
            _paths_from_source_paths(child, paths)


def _pin_paths(admission: Mapping[str, Any]) -> list[str]:
    """Use D572's existing parsed pin record; preserve occurrence validation there."""
    paths: list[str] = []
    _paths_from_source_paths(admission, paths)
    return paths


def _assert_unique_rmed_pins(admission: Mapping[str, Any]) -> None:
    """Reject a duplicate declaration where D572 defines an unordered pin list.

    Ordered Step/Action occurrences are deliberately not checked here: the
    existing D572 reader preserves repeated Action occurrences as graph data.
    """
    rows = admission.get("rmed_frontier")
    if not isinstance(rows, list):
        _fail("D572 RMED frontier is unavailable")
    paths = [row.get("source_path") for row in rows if isinstance(row, Mapping)]
    if len(paths) != len(rows) or len(paths) != len(set(paths)):
        _fail("D572 RMED frontier declares a duplicate or malformed pin")


def _control_root_from_settings(raw: bytes) -> PurePosixPath:
    try:
        parsed = tomllib.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ReleaseSuiteReferenceContextError("Project settings are invalid") from error
    paths = parsed.get("paths") if isinstance(parsed, Mapping) else None
    configured = paths.get("control_root") if isinstance(paths, Mapping) else None
    return _safe_relative(configured) if configured is not None else PurePosixPath(".caprmedio_caprmedio")


def _preflight_reader_paths(root: Path) -> tuple[dict[str, tuple[bytes, int]], tuple[str, ...]]:
    """Capture every prospective reader carrier before any delegated parser runs."""
    settings_ref = PROJECT_SETTINGS_REF.as_posix()
    settings_raw, settings_mode = _read_regular(root, settings_ref)
    manifest_ref = (_control_root_from_settings(settings_raw) / "_projection" / "selected_workflow_bindings.json").as_posix()
    manifest_raw, manifest_mode = _read_regular(root, manifest_ref)
    authority_ref = str(AUTHORITY_PIN["source_path"])
    authority_raw, authority_mode = _read_regular(root, authority_ref)
    try:
        manifest = json.loads(manifest_raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ReleaseSuiteReferenceContextError("selected manifest is unavailable for reference preflight") from error
    candidates: list[str] = [manifest_ref, _OPERATORS_REGISTRY.as_posix(), settings_ref, authority_ref]
    _paths_from_source_paths(manifest, candidates)
    freshness = manifest.get("source_freshness") if isinstance(manifest, Mapping) else None
    if isinstance(freshness, Mapping) and "selected_source_registry_ref" in freshness:
        candidates.append(freshness["selected_source_registry_ref"])
    try:
        authority_text = authority_raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ReleaseSuiteReferenceContextError("D572 is unavailable for reference preflight") from error
    if hashlib.sha256(authority_raw).hexdigest() != AUTHORITY_PIN["digest"]:
        _fail("D572 source pin is stale")
    # Parse the already descriptor-captured authority bytes before any reader
    # can reread the mutable Project.  D572 alone admits these implementation
    # paths; they remain ordinary byte-and-mode ReferenceRows in D580.
    try:
        private_carriers = _private_carriers(authority_text)
    except ReleaseSourceAdmissionError as error:
        raise ReleaseSuiteReferenceContextError("D572 private carrier declaration is invalid") from error
    candidates.extend(row["source_path"] for row in private_carriers)
    for value in re.findall(r"`([^`]+)`", authority_text):
        if value.startswith(".caprmedio_"):
            candidates.append(value)
    for candidate in candidates:
        _forbid_non_control_path(candidate)
    captured = {
        settings_ref: (settings_raw, settings_mode),
        manifest_ref: (manifest_raw, manifest_mode),
        authority_ref: (authority_raw, authority_mode),
    }
    for candidate in sorted(set(candidates)):
        if candidate not in captured:
            captured[candidate] = _read_regular(root, candidate)
    return captured, tuple(sorted(captured))


def _write_snapshot_file(root: Path, relative: str, payload: bytes, mode: int) -> None:
    target = root.joinpath(*_safe_relative(relative).parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    target.chmod(mode)


@contextmanager
def _reader_snapshot(root: Path):
    """Stage one immutable descriptor-captured reader root for existing parsers."""
    captured, paths = _preflight_reader_paths(root)
    # Retain this private 0700 disposable snapshot.  Suite evidence must not
    # become a false failure merely because a copied read-only fixture cannot
    # be removed on the host; callers receive no cleanup or retention control.
    snapshot = Path(tempfile.mkdtemp(prefix="caprmedio-release-suite-context-")).resolve(strict=True)
    try:
        snapshot.chmod(0o700)
        for relative in paths:
            payload, mode = captured[relative]
            _write_snapshot_file(snapshot, relative, payload, mode)
        yield snapshot, captured
    finally:
        # Deliberately retained for truthful diagnosis; never retry deletion.
        pass


def _closure_paths(snapshot_root: Path) -> tuple[str, ...]:
    """Derive only against the immutable reader snapshot, never mutable Project bytes."""
    manifest = load_selected_manifest(snapshot_root)
    manifest_ref = selected_manifest_ref(snapshot_root)
    admission = derive_release_source_admission(snapshot_root)
    private_carriers = derive_release_private_carriers(snapshot_root)
    freshness = manifest["source_freshness"]
    source_registry = freshness["selected_source_registry_ref"]
    _safe_relative(source_registry)
    _assert_unique_rmed_pins(admission)
    candidates = [
        manifest_ref,
        _OPERATORS_REGISTRY.as_posix(),
        PROJECT_SETTINGS_REF.as_posix(),
        str(source_registry),
        str(AUTHORITY_PIN["source_path"]),
        *_pin_paths(admission),
        *(row["source_path"] for row in private_carriers),
    ]
    # The selected manifest has already source-validated every route/admission
    # pin.  Capture their source paths too, while naturally deduplicating a
    # shared Action occurrence across the manifest and D572 closure.
    _paths_from_source_paths(manifest, candidates)
    for candidate in candidates:
        _forbid_non_control_path(candidate)
    unique = sorted(set(candidates))
    if len(unique) != len(set(unique)) or not unique:
        _fail("reference closure is empty or internally inconsistent")
    return tuple(unique)


def _preimage(bindings: tuple[tuple[str, str], ...], rows: tuple[ReferenceRow, ...]) -> dict[str, object]:
    """D580's flat, self-excluding canonical digest preimage."""
    return {
        "schema_version": 1,
        **dict(bindings),
        "reference_rows": [row.as_dict() for row in rows],
    }


def _digest(bindings: tuple[tuple[str, str], ...], rows: tuple[ReferenceRow, ...]) -> str:
    return hashlib.sha256(canonical_json(_preimage(bindings, rows)).encode("utf-8")).hexdigest()


def _validate_context_closure(context: ReleaseSuiteReferenceContext) -> tuple[Path, dict[str, ReferenceRow], dict[str, bytes]]:
    """Reject a forged or widened context before it can read or write a row."""
    if not isinstance(context, ReleaseSuiteReferenceContext):
        _fail("reference context has the wrong type")
    root = _root(context.root)
    bindings = _bindings(dict(context.trusted_binding_values))
    if bindings != context.trusted_binding_values:
        _fail("reference context binding values are not canonical")
    with _reader_snapshot(root) as (snapshot, _captured):
        expected_paths = _closure_paths(snapshot)
    rows = context.reference_rows
    if not isinstance(rows, tuple) or tuple(row.source_path for row in rows) != expected_paths:
        _fail("reference context row set differs from the private derived closure")
    if any(not isinstance(row, ReferenceRow) for row in rows):
        _fail("reference context has an untyped row")
    expected = {row.source_path: row for row in rows}
    if len(expected) != len(rows):
        _fail("reference context has duplicate rows")
    for row in rows:
        _forbid_non_control_path(row.source_path)
        if _SHA256.fullmatch(row.sha256) is None or type(row.mode) is not int or not 0 <= row.mode <= 0o777:
            _fail("reference context row is malformed")
    payloads = dict(context._verified_bytes)
    if len(payloads) != len(context._verified_bytes) or set(payloads) != set(expected):
        _fail("reference context bytes do not match its typed rows")
    if _digest(bindings, rows) != context.control_context_digest:
        _fail("reference context digest differs from its D580 preimage")
    return root, expected, payloads


def capture_context(project_root: str | Path, trusted_binding_values: Mapping[str, Any]) -> ReleaseSuiteReferenceContext:
    """Capture the exact current private closure before a read-only suite run."""
    root = _root(project_root)
    bindings = _bindings(trusted_binding_values)
    rows: list[ReferenceRow] = []
    bytes_by_path: list[tuple[str, bytes]] = []
    with _reader_snapshot(root) as (snapshot, _captured):
        for relative in _closure_paths(snapshot):
            payload, mode = _read_regular(snapshot, relative)
            rows.append(ReferenceRow(relative, hashlib.sha256(payload).hexdigest(), mode))
            bytes_by_path.append((relative, payload))
    frozen_rows = tuple(rows)
    return ReleaseSuiteReferenceContext(
        root=str(root), trusted_binding_values=bindings, reference_rows=frozen_rows,
        control_context_digest=_digest(bindings, frozen_rows), _verified_bytes=tuple(bytes_by_path),
    )


def revalidate_context(
    project_root: str | Path,
    context: ReleaseSuiteReferenceContext,
    trusted_binding_values: Mapping[str, Any],
) -> ReleaseSuiteReferenceContext:
    """Re-derive the closure; a changed Project never refreshes an attempt in place."""
    captured_root, _expected, _payloads = _validate_context_closure(context)
    root = _root(project_root)
    if root != captured_root:
        _fail("reference context belongs to another Project")
    fresh_bindings = _bindings(trusted_binding_values)
    if fresh_bindings != context.trusted_binding_values:
        _fail("trusted Suite Owner bindings changed after context capture")
    observed = capture_context(root, dict(fresh_bindings))
    if (observed.reference_rows != context.reference_rows
            or observed.control_context_digest != context.control_context_digest):
        _fail("Release suite reference context is stale")
    return context


def copy_verified_bytes(context: ReleaseSuiteReferenceContext, workspace: str | Path) -> None:
    """Copy only captured bytes into an initially writable disposable workspace."""
    _root, expected, payloads = _validate_context_closure(context)
    target_root = Path(workspace)
    if target_root.is_symlink() or not target_root.is_dir():
        _fail("reference workspace must be a regular directory")
    for relative, row in expected.items():
        payload = payloads[relative]
        if hashlib.sha256(payload).hexdigest() != row.sha256:
            _fail("reference context bytes differ from their sealed digest")
        destination = target_root
        for part in _safe_relative(relative).parts:
            destination /= part
            if destination.is_symlink():
                _fail(f"reference workspace target has a symlinked ancestor: {relative}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        cursor = target_root
        for part in _safe_relative(relative).parts[:-1]:
            cursor /= part
            if cursor.is_symlink() or not cursor.is_dir():
                _fail(f"reference workspace target parent is unsafe: {relative}")
        if destination.exists() or destination.is_symlink():
            if (
                destination.is_symlink()
                or not destination.is_file()
                or destination.read_bytes() != payload
                or destination.stat().st_mode & 0o777 != row.mode
            ):
                _fail(f"reference workspace target conflicts with sealed bytes: {relative}")
            continue
        with destination.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        destination.chmod(row.mode)


def validate_reference_rows(project_root: str | Path, reference_rows: Sequence[Mapping[str, Any]]) -> tuple[ReferenceRow, ...]:
    """Independently validate public envelope rows without private N/image data.

    The runner can use this after its read-only workspace copy to establish
    that the rows neither omit nor widen the current source-derived closure.
    """
    root = _root(project_root)
    if not isinstance(reference_rows, Sequence) or isinstance(reference_rows, (str, bytes)):
        _fail("reference rows must be an ordered array")
    rows: list[ReferenceRow] = []
    for value in reference_rows:
        if not isinstance(value, Mapping) or set(value) != {"source_path", "sha256", "mode"}:
            _fail("reference row has an incomplete or unknown schema")
        path = _forbid_non_control_path(value["source_path"])
        digest, mode = value["sha256"], value["mode"]
        if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None or type(mode) is not int or not 0 <= mode <= 0o777:
            _fail("reference row has invalid digest or mode")
        rows.append(ReferenceRow(path.as_posix(), digest, mode))
    with _reader_snapshot(root) as (snapshot, _captured):
        expected_paths = _closure_paths(snapshot)
        if tuple(row.source_path for row in rows) != expected_paths:
            _fail("reference rows differ from the private derived closure")
        for row in rows:
            payload, mode = _read_regular(snapshot, row.source_path)
            if hashlib.sha256(payload).hexdigest() != row.sha256 or mode != row.mode:
                _fail("reference row differs from current Project bytes")
    return tuple(rows)


def validate_schema2_context(envelope: Mapping[str, Any], context: ReleaseSuiteReferenceContext) -> Mapping[str, Any]:
    """Validate only D579@3's private schema-2 context additions."""
    if not isinstance(envelope, Mapping):
        _fail("schema-2 reference context has invalid inputs")
    _validate_context_closure(context)
    if envelope.get("schema_version") != 2:
        _fail("suite envelope is not schema version 2")
    rows = envelope.get("reference_rows")
    if not isinstance(rows, list) or rows != [row.as_dict() for row in context.reference_rows]:
        _fail("suite envelope reference rows differ from the sealed context")
    if envelope.get("control_context_digest") != context.control_context_digest:
        _fail("suite envelope control context digest differs from the sealed context")
    candidate = context.bindings()["candidate_snapshot_manifest_sha256"]
    if envelope.get("candidate_snapshot_manifest_sha256") != candidate:
        _fail("suite envelope candidate digest differs from the trusted context")
    return MappingProxyType(dict(envelope))


def context_preimage(context: ReleaseSuiteReferenceContext) -> Mapping[str, object]:
    """Return D580's exact self-excluding payload for suite evidence serialization."""
    _validate_context_closure(context)
    return MappingProxyType(_preimage(context.trusted_binding_values, context.reference_rows))


__all__ = [
    "ReferenceRow", "ReleaseSuiteReferenceContext", "ReleaseSuiteReferenceContextError",
    "capture_context", "context_preimage", "copy_verified_bytes", "revalidate_context", "validate_reference_rows", "validate_schema2_context",
]
