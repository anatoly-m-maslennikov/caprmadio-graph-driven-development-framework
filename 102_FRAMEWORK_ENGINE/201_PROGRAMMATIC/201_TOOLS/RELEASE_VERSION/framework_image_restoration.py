"""Guarded restoration of one missing selected bootstrap image.

This boundary is deliberately narrower than both first installation and a
Release Version promotion.  It consumes only an already-selected first-N
package and its historical bootstrap proof.  The retained-image producer owns
the disposable Docker context; this module owns the one-way admission,
selector binding, private recovery carriers, and Journal result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tomllib
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import bootstrap_image as _bootstrap_image
from bootstrap_image import (
    BootstrapImageError,
    BootstrapImageEvidence,
    produce_retained_framework_image,
    read_retained_initial_framework_image,
)
from framework_initialization import (
    PACKAGE_IMAGE_LABEL,
    SOURCE_CONTEXT_IMAGE_LABEL,
    DirectActionJournal,
    _atomic_file,
)
from release_contract import PROJECT_SKILL_TARGET, ReleaseContractError, canonical_json
from release_handoff import CURRENT_SELECTOR_RELATIVE
from release_image import DockerCommandResult, DockerExecutor, DockerSubprocessExecutor, IMAGE_ID
from selector_publication_lock import SelectorPublicationLockError, selector_publication_lock


RESTORATION_ACTION_ID = "FRAMEWORK_IMAGE_RESTORATION"
RESTORATION_KIND = "retained_selected_framework_image_restoration"
RESTORATION_ROOT = Path(".caprmedio_runtime/framework_image_restoration")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_SELECTOR_FIELDS = (
    "schema_version",
    "manifest_sha256",
    "release",
    "selected_release_root",
    "framework_engine_root",
    "methodology_root",
    "image_digest",
)
_MAX_DOCKER_OUTPUT_BYTES = 4 * 1024 * 1024


class FrameworkImageRestorationError(ReleaseContractError):
    """A stable restoration refusal before or after a guarded effect."""


@dataclass(frozen=True)
class _FrozenRestoration:
    root: Path
    selector: bytes
    selector_sha256: str
    release: str
    old_image_digest: str
    original: BootstrapImageEvidence
    package_inventory_sha256: str
    skill_inventory_sha256: str
    intent: dict[str, str]
    intent_sha256: str
    private_root: Path


@dataclass(frozen=True)
class _Terminalization:
    """The Journal's observable terminal state, never a synthetic receipt."""

    terminal: Mapping[str, Any] | None
    pending_event_id: str | None
    error_code: str | None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _stable_effect_refs(values: list[str]) -> list[str]:
    """Keep effect evidence ordered, unique, and safe for Journal v5."""
    normalized: list[str] = []
    for value in values:
        if not isinstance(value, str) or not value:
            raise _error("framework-image-restoration-effects-invalid", "effect evidence reference is invalid")
        if value not in normalized:
            normalized.append(value)
    return normalized


def _package_context_records(records: list[list[object]]) -> list[list[object]]:
    """Compare the retained package context without inventing manifest mode proof.

    The package manifest's bytes are authenticated by its digest, but the
    bootstrap proof intentionally records the copied manifest at its context
    creation mode.  Every other file and all directory modes remain exact.
    """
    normalized: list[list[object]] = []
    for record in records:
        if len(record) == 4 and record[:2] == ["file", "manifest.toml"]:
            normalized.append(record[:3])
        else:
            normalized.append(record)
    return normalized


def _direct_action_types() -> tuple[type[Any], type[Exception]]:
    """Load the existing Journal Session when this carrier is invoked as a script."""
    module = _direct_action_module()
    return module.DirectActionSession, module.DirectActionJournalError


def _direct_action_module() -> Any:
    """Load the sibling direct-Action boundary and its shared Journal reader."""
    import sys

    release_root = str(Path(__file__).resolve().parent)
    tools_root = str(Path(__file__).resolve().parent.parent)
    for directory in (release_root, tools_root):
        if directory not in sys.path:
            sys.path.insert(0, directory)
    import direct_action_session

    return direct_action_session


def _work_journal_module() -> Any:
    import sys

    tools_root = str(Path(__file__).resolve().parent.parent)
    if tools_root not in sys.path:
        sys.path.insert(0, tools_root)
    import work_journal

    return work_journal


def _error(code: str, message: str) -> FrameworkImageRestorationError:
    return FrameworkImageRestorationError(code, message)


def _root(project_root: Path | str) -> Path:
    try:
        root = Path(project_root).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise _error("framework-image-restoration-root-invalid", "Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise _error("framework-image-restoration-root-invalid", "Project root is unsafe")
    return root


def _regular_file(root: Path, relative: Path, *, code: str) -> Path:
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise _error(code, "required Project carrier path is unsafe")
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink():
            raise _error(code, "required Project carrier has a symlinked ancestor")
    if not path.is_file() or path.is_symlink():
        raise _error(code, "required Project carrier is unavailable")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error(code, "required Project carrier escapes Project") from error
    return path


def _inventory(root: Path, *, code: str) -> tuple[list[list[object]], str]:
    """Freeze the whole regular tree, including empty-directory structure."""
    if root.is_symlink() or not root.is_dir():
        raise _error(code, "frozen inventory root is unavailable or unsafe")
    records: list[list[object]] = []
    try:
        for item in sorted(root.rglob("*"), key=lambda path: path.relative_to(root).as_posix()):
            relative = item.relative_to(root).as_posix()
            if item.is_symlink():
                raise _error(code, "frozen inventory contains a symlink")
            # Finder metadata is not package, Skill, or proof content.  Only
            # a regular file is ignored: a same-named link, directory, or
            # special carrier remains an unsafe inventory input.
            if item.name == ".DS_Store" and item.is_file():
                continue
            mode = item.stat().st_mode & 0o777
            if item.is_dir():
                records.append(["directory", relative, mode])
            elif item.is_file():
                records.append(["file", relative, _digest(item.read_bytes()), mode])
            else:
                raise _error(code, "frozen inventory contains a special carrier")
    except FrameworkImageRestorationError:
        raise
    except OSError as error:
        raise _error(code, "frozen inventory cannot be read") from error
    return records, _digest(canonical_json(records))


def _closed_bootstrap_selector(payload: bytes) -> dict[str, object]:
    try:
        selector = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise _error("framework-image-restoration-selector-invalid", "selected Framework selector is not valid TOML") from error
    if not isinstance(selector, dict) or tuple(selector) != _SELECTOR_FIELDS:
        raise _error("framework-image-restoration-selector-invalid", "selected Framework selector is not the closed bootstrap shape")
    if selector.get("schema_version") != 1:
        raise _error("framework-image-restoration-selector-invalid", "selected Framework selector has an unsupported schema")
    release = selector.get("release")
    manifest = selector.get("manifest_sha256")
    image = selector.get("image_digest")
    if (not isinstance(release, str) or _SHA256.fullmatch(release) is None
            or manifest != release or not isinstance(image, str) or IMAGE_ID.fullmatch(image) is None):
        raise _error("framework-image-restoration-selector-invalid", "selected Framework selector identity is invalid")
    release_root = f".caprmedio_runtime/framework/releases/{release}"
    if selector.get("selected_release_root") != release_root:
        raise _error("framework-image-restoration-selector-invalid", "selected Framework package root differs from bootstrap shape")
    if selector.get("framework_engine_root") != release_root + "/FRAMEWORK_ENGINE":
        raise _error("framework-image-restoration-selector-invalid", "selected Framework engine root differs from bootstrap shape")
    if selector.get("methodology_root") != release_root + "/METHODOLOGY":
        raise _error("framework-image-restoration-selector-invalid", "selected Framework Methodology root differs from bootstrap shape")
    return selector


def _private_directory(root: Path, intent_sha256: str) -> Path:
    """Create only the content-addressed private observation directory."""
    if _SHA256.fullmatch(intent_sha256) is None:
        raise _error("framework-image-restoration-intent-invalid", "restoration intent digest is invalid")
    directory = root
    try:
        for part in (*RESTORATION_ROOT.parts, intent_sha256):
            directory = directory / part
            if directory.is_symlink():
                raise _error("framework-image-restoration-evidence-unsafe", "private restoration path is symlinked")
            if directory.exists():
                if not directory.is_dir():
                    raise _error("framework-image-restoration-evidence-unsafe", "private restoration path is not a directory")
            else:
                directory.mkdir(mode=0o700)
    except FrameworkImageRestorationError:
        raise
    except OSError as error:
        raise _error("framework-image-restoration-evidence-unavailable", "private restoration evidence cannot be created") from error
    return directory


def _retry_attempt_directory(frozen: _FrozenRestoration, *, requested_run_id: str,
                             retry_of_terminal_event_id: str,
                             prior_result_ref: str,
                             prior_terminal_event_digest: str) -> Path:
    """Open one immutable, per-request retry carrier below the sealed intent.

    The parent intent carrier is historical evidence.  A retry may read it but
    must never add a replacement result or mutate bytes that describe the
    original partial Run.
    """
    if not isinstance(requested_run_id, str) or not requested_run_id:
        raise _error("framework-image-restoration-run-invalid", "requested Action Run ID is required")
    if not isinstance(retry_of_terminal_event_id, str) or not retry_of_terminal_event_id:
        raise _error("framework-image-restoration-retry-invalid", "retry requires one exact terminal event ID")
    if _SHA256.fullmatch(prior_terminal_event_digest) is None:
        raise _error("framework-image-restoration-retry-invalid", "retry terminal evidence digest is invalid")
    run_digest = _digest(requested_run_id.encode("utf-8"))
    attempts_root = frozen.private_root / "attempts"
    attempt_root = attempts_root / run_digest
    try:
        for directory in (attempts_root, attempt_root):
            if directory.is_symlink():
                raise _error("framework-image-restoration-evidence-unsafe", "retry restoration path is symlinked")
            if directory.exists():
                if not directory.is_dir():
                    raise _error("framework-image-restoration-evidence-unsafe", "retry restoration path is not a directory")
            else:
                directory.mkdir(mode=0o700)
    except FrameworkImageRestorationError:
        raise
    except OSError as error:
        raise _error("framework-image-restoration-evidence-unavailable", "retry restoration evidence cannot be created") from error
    _write_once(
        attempt_root / "retry.json",
        canonical_json({
            "schema": "caprmedio.framework_image_restoration.retry.v1",
            "intent_sha256": frozen.intent_sha256,
            "requested_run_id": requested_run_id,
            "retry_of_terminal_event_id": retry_of_terminal_event_id,
            "retry_of_terminal_event_digest": prior_terminal_event_digest,
            "retry_of_result_ref": prior_result_ref,
        }),
    )
    return attempt_root


def _write_once(path: Path, payload: bytes) -> None:
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != payload:
            raise _error("framework-image-restoration-evidence-conflict", "private restoration evidence conflicts with frozen bytes")
        return
    try:
        with path.open("xb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except OSError as error:
        raise _error("framework-image-restoration-evidence-unavailable", "private restoration evidence cannot be retained") from error


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise _error("framework-image-restoration-evidence-unsafe", "private restoration carrier escapes Project") from error


def _result_ref(root: Path, private_root: Path) -> str:
    return _relative(root, private_root / "result.json")


def _existing_result(root: Path, private_root: Path) -> dict[str, Any] | None:
    path = private_root / "result.json"
    if not path.exists() and not path.is_symlink():
        return None
    if path.is_symlink() or not path.is_file():
        raise _error("framework-image-restoration-evidence-unsafe", "private restoration result is unsafe")
    try:
        result = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, ValueError) as error:
        raise _error("framework-image-restoration-evidence-invalid", "private restoration result is unreadable") from error
    if not isinstance(result, dict):
        raise _error("framework-image-restoration-evidence-invalid", "private restoration result has an unsupported shape")
    return result


def _intent_from_bytes(payload: bytes) -> dict[str, str]:
    """Reopen the closed eight-field restoration intent without invention."""
    try:
        value = json.loads(payload)
    except (UnicodeDecodeError, ValueError) as error:
        raise _error("framework-image-restoration-evidence-invalid", "restoration intent is unreadable") from error
    expected = {
        "action_id", "kind", "manifest_sha256", "source_context_sha256",
        "selected_selector_sha256", "old_image_digest", "retained_proof_receipt_sha256",
        "retained_context_sha256",
    }
    if (not isinstance(value, dict) or set(value) != expected
            or value.get("action_id") != RESTORATION_ACTION_ID or value.get("kind") != RESTORATION_KIND):
        raise _error("framework-image-restoration-evidence-invalid", "restoration intent has an unsupported shape")
    for field in expected - {"action_id", "kind", "old_image_digest"}:
        if not isinstance(value.get(field), str) or _SHA256.fullmatch(value[field]) is None:
            raise _error("framework-image-restoration-evidence-invalid", "restoration intent digest is invalid")
    if not isinstance(value.get("old_image_digest"), str) or IMAGE_ID.fullmatch(value["old_image_digest"]) is None:
        raise _error("framework-image-restoration-evidence-invalid", "restoration intent image digest is invalid")
    if payload != canonical_json(value):
        raise _error("framework-image-restoration-evidence-invalid", "restoration intent is not canonical")
    return {key: str(value[key]) for key in expected}


def _private_result_for_selector(root: Path, expected_selector_sha256: str) -> tuple[Path, dict[str, str], dict[str, Any]] | None:
    """Find only a prior result whose sealed intent names this exact selector."""
    if not isinstance(expected_selector_sha256, str) or _SHA256.fullmatch(expected_selector_sha256) is None:
        raise _error("framework-image-restoration-selector-digest-invalid", "expected selector SHA-256 is invalid")
    parent = root / RESTORATION_ROOT
    if not parent.exists():
        return None
    if parent.is_symlink() or not parent.is_dir():
        raise _error("framework-image-restoration-evidence-unsafe", "private restoration root is unsafe")
    found: tuple[Path, dict[str, str], dict[str, Any]] | None = None
    try:
        children = sorted(parent.iterdir(), key=lambda path: path.name)
    except OSError as error:
        raise _error("framework-image-restoration-evidence-unavailable", "private restoration root cannot be read") from error
    for private_root in children:
        if private_root.name == ".DS_Store" and not private_root.is_symlink() and private_root.is_file():
            continue
        if private_root.is_symlink() or not private_root.is_dir():
            raise _error("framework-image-restoration-evidence-unsafe", "private restoration root contains an unsafe carrier")
        if _SHA256.fullmatch(private_root.name) is None:
            raise _error("framework-image-restoration-evidence-invalid", "private restoration identity is invalid")
        intent_path = private_root / "intent.json"
        if intent_path.is_symlink() or not intent_path.is_file():
            raise _error("framework-image-restoration-evidence-invalid", "private restoration intent is unavailable")
        intent = _intent_from_bytes(intent_path.read_bytes())
        if _digest(canonical_json(intent)) != private_root.name:
            raise _error("framework-image-restoration-evidence-invalid", "private restoration identity does not bind its intent")
        if intent["selected_selector_sha256"] != expected_selector_sha256:
            continue
        result = _existing_result(root, private_root)
        if result is None:
            continue
        candidate = (private_root, intent, result)
        if found is not None:
            raise _error("framework-image-restoration-evidence-conflict", "multiple closed results bind one selector intent")
        found = candidate
    return found


def _freeze(root: Path, expected_selector_sha256: str) -> _FrozenRestoration:
    if not isinstance(expected_selector_sha256, str) or _SHA256.fullmatch(expected_selector_sha256) is None:
        raise _error("framework-image-restoration-selector-digest-invalid", "expected selector SHA-256 is invalid")
    selector_path = _regular_file(root, Path(CURRENT_SELECTOR_RELATIVE), code="framework-image-restoration-selector-missing")
    selector = selector_path.read_bytes()
    selector_sha256 = _digest(selector)
    if selector_sha256 != expected_selector_sha256:
        raise _error("framework-image-restoration-selector-stale", "selected Framework selector differs from the caller's exact digest")
    parsed = _closed_bootstrap_selector(selector)
    release = str(parsed["release"])
    old_image_digest = str(parsed["image_digest"])
    try:
        original = read_retained_initial_framework_image(root, release, old_image_digest)
    except BootstrapImageError as error:
        raise _error(error.code, str(error)) from error
    if (original.manifest_sha256 != release or original.source_context_sha256 == ""
            or original.image_digest != old_image_digest or original.receipt_sha256 is None
            or _SHA256.fullmatch(original.receipt_sha256) is None or _SHA256.fullmatch(original.context_sha256) is None):
        raise _error("framework-image-restoration-proof-invalid", "retained bootstrap proof is not a complete selected binding")
    package = root / ".caprmedio_runtime/framework/releases" / release
    package_records, package_inventory_sha256 = _inventory(package, code="framework-image-restoration-package-invalid")
    del package_records
    package_skill = package / "SKILLS/ca"
    package_skill_records, _package_skill_sha256 = _inventory(package_skill, code="framework-image-restoration-package-invalid")
    public_skill_records, skill_inventory_sha256 = _inventory(
        root / PROJECT_SKILL_TARGET, code="framework-image-restoration-skill-invalid"
    )
    if package_skill_records != public_skill_records:
        raise _error("framework-image-restoration-skill-stale", "public ca Skill differs from the selected retained package")
    intent = {
        "action_id": RESTORATION_ACTION_ID,
        "kind": RESTORATION_KIND,
        "manifest_sha256": original.manifest_sha256,
        "source_context_sha256": original.source_context_sha256,
        "selected_selector_sha256": selector_sha256,
        "old_image_digest": old_image_digest,
        "retained_proof_receipt_sha256": original.receipt_sha256,
        "retained_context_sha256": original.context_sha256,
    }
    intent_sha256 = _digest(canonical_json(intent))
    private_root = _private_directory(root, intent_sha256)
    _write_once(private_root / "intent.json", canonical_json(intent))
    _write_once(private_root / "prior-selector.toml", selector)
    return _FrozenRestoration(root, selector, selector_sha256, release, old_image_digest, original,
                              package_inventory_sha256, skill_inventory_sha256, intent, intent_sha256, private_root)


def _recheck(frozen: _FrozenRestoration, *, expected_selector: bytes) -> None:
    selector = _regular_file(frozen.root, Path(CURRENT_SELECTOR_RELATIVE), code="framework-image-restoration-selector-stale").read_bytes()
    if selector != expected_selector:
        raise _error("framework-image-restoration-selector-stale", "selected Framework selector changed during restoration")
    parsed = _closed_bootstrap_selector(selector)
    if parsed["release"] != frozen.release:
        raise _error("framework-image-restoration-selector-stale", "selected Framework release changed during restoration")
    package = frozen.root / ".caprmedio_runtime/framework/releases" / frozen.release
    _records, package_sha256 = _inventory(package, code="framework-image-restoration-package-stale")
    _records, skill_sha256 = _inventory(frozen.root / PROJECT_SKILL_TARGET, code="framework-image-restoration-skill-stale")
    if package_sha256 != frozen.package_inventory_sha256 or skill_sha256 != frozen.skill_inventory_sha256:
        raise _error("framework-image-restoration-input-stale", "retained package or public Skill changed during restoration")
    try:
        reopened = read_retained_initial_framework_image(frozen.root, frozen.release, frozen.old_image_digest)
    except BootstrapImageError as error:
        raise _error(error.code, str(error)) from error
    if reopened != frozen.original:
        raise _error("framework-image-restoration-proof-stale", "original retained bootstrap proof changed during restoration")


def _validate_executor(executor: DockerExecutor) -> DockerSubprocessExecutor:
    if type(executor) is not DockerSubprocessExecutor:
        raise _error("framework-image-restoration-executor-untrusted", "restoration requires DockerSubprocessExecutor")
    return executor


def _observe_selected_image(executor: DockerSubprocessExecutor, frozen: _FrozenRestoration) -> str:
    """Return ``absent`` or ``present`` only for an unambiguous daemon response."""
    try:
        result = executor.run(("docker", "image", "inspect", frozen.old_image_digest), cwd=frozen.root, timeout_seconds=60)
    except OSError as error:
        raise _error("framework-image-restoration-daemon-unavailable", "Docker daemon observation is unavailable") from error
    if (not isinstance(result, DockerCommandResult) or not isinstance(result.stdout, bytes)
            or not isinstance(result.stderr, bytes) or len(result.stdout) > _MAX_DOCKER_OUTPUT_BYTES
            or len(result.stderr) > _MAX_DOCKER_OUTPUT_BYTES):
        raise _error("framework-image-restoration-daemon-invalid", "Docker daemon observation is incomplete")
    if result.timed_out:
        raise _error("framework-image-restoration-daemon-uncertain", "Docker image observation timed out")
    if result.exit_code != 0:
        # A permission error, bad transport, or generic non-zero status is not
        # evidence of absence.  Docker's missing-image response is explicit.
        if b"no such image" in result.stderr.lower() or b"no such image" in result.stdout.lower():
            return "absent"
        raise _error("framework-image-restoration-daemon-unavailable", "Docker did not establish selected image absence")
    try:
        inspected = json.loads(result.stdout)
        values = inspected[0]
        labels = values["Config"]["Labels"]
        valid = (
            len(inspected) == 1
            and values.get("Id") == frozen.old_image_digest
            and isinstance(labels, dict)
            and labels.get(PACKAGE_IMAGE_LABEL) == frozen.release
            and labels.get(SOURCE_CONTEXT_IMAGE_LABEL) == frozen.original.source_context_sha256
        )
    except (IndexError, KeyError, TypeError, ValueError):
        valid = False
    if not valid:
        raise _error("framework-image-restoration-image-invalid", "present selected image does not match the retained package proof")
    return "present"


def _begin(journal: DirectActionJournal, requested_run_id: str, intent: Mapping[str, str]) -> str:
    if not isinstance(requested_run_id, str) or not requested_run_id:
        raise _error("framework-image-restoration-run-invalid", "requested Action Run ID is required")
    try:
        started = journal.begin_action(action_id=RESTORATION_ACTION_ID, requested_run_id=requested_run_id, intent=intent)
    except Exception as error:
        code = getattr(error, "code", "framework-image-restoration-journal-start-unavailable")
        if isinstance(code, str) and code.startswith("direct-action-"):
            raise _error(code, str(error)) from error
        raise _error("framework-image-restoration-journal-start-unavailable", "canonical started Action evidence is unavailable") from error
    run_id = started.get("run_id") if isinstance(started, Mapping) else None
    if not isinstance(run_id, str) or not run_id or started.get("disposition") != "started":
        raise _error("framework-image-restoration-journal-start-unavailable", "canonical started Action evidence did not reopen")
    return run_id


def _write_result(frozen: _FrozenRestoration, payload: Mapping[str, Any], *, result_root: Path | None = None) -> str:
    """Seal one result without replacing an earlier terminal observation."""
    root = result_root or frozen.private_root
    target = root / "result.json"
    try:
        _write_once(target, canonical_json(dict(payload)))
    except FrameworkImageRestorationError:
        raise
    except OSError as error:
        raise _error("framework-image-restoration-result-recording-unavailable", "restoration result cannot be retained") from error
    return _result_ref(frozen.root, root)


def _pending_event_id_from_session(journal: DirectActionJournal, *, run_id: str,
                                   result_ref: str) -> str | None:
    """Extract the exact event retained by DirectActionSession after append loss."""
    pending = getattr(journal, "pending", None)
    if not isinstance(pending, Mapping):
        return None
    matches: list[str] = []
    for event_id, observed in pending.items():
        if not isinstance(event_id, str) or not isinstance(observed, Mapping):
            continue
        event = observed.get("event")
        if not isinstance(event, Mapping):
            continue
        if (event.get("action_id") == RESTORATION_ACTION_ID
                and event.get("result_ref") == result_ref
                and event.get("run", {}).get("run_id") == run_id):
            matches.append(event_id)
    if len(matches) == 1:
        return matches[0]
    return None


def _terminalize(journal: DirectActionJournal, run_id: str, *, outcome: str, result_ref: str,
                 effect_refs: list[str]) -> _Terminalization:
    effect_refs = _stable_effect_refs(effect_refs)
    try:
        journal.record_effects(run_id, result_ref=result_ref, effect_refs=effect_refs)
        terminal = journal.finish_action(run_id, outcome=outcome, result_ref=result_ref, effect_refs=effect_refs)
    except Exception as error:
        return _Terminalization(
            None,
            _pending_event_id_from_session(journal, run_id=run_id, result_ref=result_ref),
            getattr(error, "code", "framework-image-restoration-journal-terminal-unavailable"),
        )
    if not isinstance(terminal, Mapping):
        return _Terminalization(None, None, "framework-image-restoration-journal-terminal-invalid")
    pending_event_id = terminal.get("pending_event_id")
    if not isinstance(pending_event_id, str):
        pending_event_id = terminal.get("event_id") if terminal.get("disposition") == "pending" else None
    return _Terminalization(dict(terminal), pending_event_id, None)


def _store_pending_reference(result_root: Path, *, event_id: str, result_ref: str,
                             run_id: str) -> None:
    if not event_id.startswith("direct-action:"):
        raise _error("framework-image-restoration-pending-invalid", "pending Journal event ID is not a direct Action event")
    _write_once(
        result_root / "pending-terminal.json",
        canonical_json({"event_id": event_id, "result_ref": result_ref, "run_id": run_id}),
    )


def _pending_reply(result_root: Path, settlement: _Terminalization, *, result_ref: str,
                   run_id: str) -> dict[str, Any]:
    """Expose actual terminal-recording loss and its sole recovery identity."""
    response: dict[str, Any] = {
        "state": "recording_pending",
        "reason": settlement.error_code or "framework-image-restoration-journal-terminal-unavailable",
        "result_ref": result_ref,
        "run_id": run_id,
        "terminal": dict(settlement.terminal) if settlement.terminal is not None else None,
    }
    if settlement.pending_event_id is not None:
        try:
            _store_pending_reference(result_root, event_id=settlement.pending_event_id,
                                     result_ref=result_ref, run_id=run_id)
        except FrameworkImageRestorationError as error:
            response["reason"] = error.code
        else:
            response["pending_event_id"] = settlement.pending_event_id
    return response


def _terminal_confirmed(settlement: _Terminalization, outcome: str) -> bool:
    return (
        settlement.terminal is not None
        and settlement.terminal.get("disposition") == "terminal"
        and settlement.terminal.get("outcome") == outcome
    )


def _proof_fields(evidence: BootstrapImageEvidence,
                  canonical_evidence: BootstrapImageEvidence | None = None) -> dict[str, Any]:
    fields = {
        "attempt_evidence_root": evidence.evidence_root,
        "attempt_commands_sha256": evidence.commands_sha256,
        "attempt_receipt_sha256": evidence.receipt_sha256,
        "attempt_execution_kind": evidence.execution_kind,
        "canonical_proof_key": evidence.bootstrap_proof_key,
        "canonical_proof_root": evidence.proof_root,
        "canonical_context_root": evidence.context_root,
    }
    if canonical_evidence is not None:
        fields["canonical_proof_receipt_sha256"] = canonical_evidence.receipt_sha256
    return fields


def _verified_produced_evidence(frozen: _FrozenRestoration, evidence: BootstrapImageEvidence) -> BootstrapImageEvidence:
    if (evidence.outcome != "verified" or evidence.execution_kind != "docker-subprocess"
            or evidence.manifest_sha256 != frozen.release
            or evidence.source_context_sha256 != frozen.original.source_context_sha256
            or evidence.context_sha256 != frozen.original.context_sha256
            or not isinstance(evidence.image_digest, str) or IMAGE_ID.fullmatch(evidence.image_digest) is None
            or evidence.receipt_sha256 is None or _SHA256.fullmatch(evidence.receipt_sha256) is None):
        raise _error("framework-image-restoration-build-invalid", "fresh retained-package image evidence is incomplete")
    try:
        applicable = read_retained_initial_framework_image(frozen.root, frozen.release, evidence.image_digest)
    except BootstrapImageError as error:
        raise _error(error.code, str(error)) from error
    # Same-ID producer evidence must describe the fresh attempt, while this
    # reader deliberately reopens the historical proof that remains canonical.
    if evidence.image_digest == frozen.old_image_digest:
        if evidence.evidence_root == frozen.original.evidence_root or applicable != frozen.original:
            raise _error("framework-image-restoration-attempt-invalid", "same-ID build did not retain distinct fresh attempt evidence")
    elif applicable.image_digest != evidence.image_digest:
        raise _error("framework-image-restoration-proof-invalid", "new canonical proof does not bind the observed image")
    return applicable


def _replacement_selector(frozen: _FrozenRestoration, new_image_digest: str) -> bytes:
    if new_image_digest == frozen.old_image_digest:
        return frozen.selector
    old = frozen.old_image_digest.encode("ascii")
    if frozen.selector.count(old) != 1:
        raise _error("framework-image-restoration-selector-invalid", "bootstrap selector does not contain exactly one image binding")
    replacement = frozen.selector.replace(old, new_image_digest.encode("ascii"), 1)
    parsed = _closed_bootstrap_selector(replacement)
    if parsed["image_digest"] != new_image_digest:
        raise _error("framework-image-restoration-selector-invalid", "replacement selector is not an exact image-only change")
    return replacement


def _result_payload(frozen: _FrozenRestoration, *, state: str, reason: str, requested_run_id: str,
                    run_id: str | None, observed_image_digest: str | None,
                    observed_selector: bytes, publication: str, evidence: BootstrapImageEvidence | None,
                    effect_refs: list[str], canonical_evidence: BootstrapImageEvidence | None = None,
                    retry_of_terminal_event_id: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema": "caprmedio.framework_image_restoration.result.v1",
        "intent_sha256": frozen.intent_sha256,
        "requested_run_id": requested_run_id,
        "run_id": run_id,
        "state": state,
        "reason": reason,
        "old_image_digest": frozen.old_image_digest,
        "observed_image_digest": observed_image_digest,
        "prior_selector_sha256": frozen.selector_sha256,
        "observed_selector_sha256": _digest(observed_selector),
        "publication": publication,
        "effect_refs": effect_refs,
    }
    if evidence is not None:
        payload.update(_proof_fields(evidence, canonical_evidence))
    if retry_of_terminal_event_id is not None:
        payload["retry_of_terminal_event_id"] = retry_of_terminal_event_id
    return payload


def _return_recorded(root: Path, private_root: Path, intent: Mapping[str, str], result: Mapping[str, Any],
                     *, requested_run_id: str) -> dict[str, Any]:
    """Return a recovery-only observation without redispatching effects."""
    state = result.get("state")
    if (not isinstance(state, str) or result.get("requested_run_id") != requested_run_id
            or result.get("intent_sha256") != _digest(canonical_json(dict(intent)))):
        raise _error("framework-image-restoration-evidence-invalid", "private restoration result has no closed state")
    response: dict[str, Any] = {
        "state": "recovery_required",
        "reason": "framework-image-restoration-existing-result",
        "prior_result": dict(result),
    }
    pending_event_id = _pending_id_for_result(root, private_root, result)
    if pending_event_id is not None:
        response["pending_event_id"] = pending_event_id
    return response


def _result_roots(root: Path, result_ref: str, *, code: str) -> tuple[Path, Path]:
    """Resolve either the legacy result or one immutable retry-run result."""
    relative = Path(result_ref)
    prefix = RESTORATION_ROOT.parts
    if relative.is_absolute() or ".." in relative.parts or tuple(relative.parts[:len(prefix)]) != prefix:
        raise _error(code, "terminal event result is outside restoration evidence")
    tail = relative.parts[len(prefix):]
    if (len(tail) == 2 and _SHA256.fullmatch(tail[0]) is not None and tail[1] == "result.json"):
        intent_root = root / Path(*prefix) / tail[0]
        result_root = intent_root
    elif (len(tail) == 4 and _SHA256.fullmatch(tail[0]) is not None and tail[1] == "attempts"
          and _SHA256.fullmatch(tail[2]) is not None and tail[3] == "result.json"):
        intent_root = root / Path(*prefix) / tail[0]
        result_root = intent_root / "attempts" / tail[2]
    else:
        raise _error(code, "terminal event result is outside restoration evidence")
    current = root
    for part in relative.parts[:-1]:
        current = current / part
        if current.is_symlink() or not current.is_dir():
            raise _error(code, "terminal event evidence path is unsafe")
    return intent_root, result_root


def _terminal_effect_refs_for_result(root: Path, result_root: Path, result: Mapping[str, Any], *, code: str) -> list[str]:
    """Derive only the producer's exact terminal effect set from a result."""
    raw = result.get("effect_refs")
    if not isinstance(raw, list) or any(not isinstance(value, str) or not value for value in raw):
        raise _error(code, "restoration result effect references are invalid")
    refs = [str(value) for value in raw]
    state = result.get("state")
    publication = result.get("publication")
    if state == "no_op":
        # Older no-op result bytes named the selector despite no selector
        # effect; Journal v5 correctly records the normalized empty set.
        if refs in ([], [CURRENT_SELECTOR_RELATIVE]):
            return []
        raise _error(code, "no-op result has unsupported effect evidence")
    if state == "partial":
        attempt = result.get("attempt_evidence_root")
        if attempt is None:
            if publication == "unpublished" and refs == []:
                return []
            raise _error(code, "partial result has unsupported effect evidence")
        if not isinstance(attempt, str) or publication not in {"unpublished", "unchanged", "replaced", "uncertain"}:
            raise _error(code, "partial result has unsupported effect evidence")
        expected = [attempt]
        if publication == "replaced":
            expected.append(CURRENT_SELECTOR_RELATIVE)
        if refs != expected:
            raise _error(code, "partial result has unsupported effect evidence")
        return expected
    if state != "restored":
        raise _error(code, "restoration result has unsupported terminal state")
    attempt = result.get("attempt_evidence_root")
    canonical = result.get("canonical_proof_root")
    if not isinstance(attempt, str) or not isinstance(canonical, str) or publication not in {"unchanged", "replaced"}:
        raise _error(code, "restored result has unsupported effect evidence")
    expected_tail = [CURRENT_SELECTOR_RELATIVE]
    if publication == "replaced":
        expected_tail.append(_relative(root, result_root / "replacement-selector.toml"))
    expected = _stable_effect_refs([attempt, canonical, *expected_tail])
    if refs == expected:
        return expected
    if attempt != canonical:
        raise _error(code, "restored result has unsupported effect evidence")
    # One old producer shape retained the canonical proof alias twice.  The
    # historical test-double path can have inserted that same alias once more;
    # both remain one exact proof alias and no unrelated reference is admitted.
    proof_prefix = refs[:-len(expected_tail)]
    if (len(proof_prefix) not in {2, 3}
            or any(value != attempt for value in proof_prefix)
            or refs[-len(expected_tail):] != expected_tail):
        raise _error(code, "restored result has unsupported duplicate effect evidence")
    return expected


def _owned_result_event(root: Path, event: Mapping[str, Any], *, code: str) -> tuple[Path, Path, dict[str, str], dict[str, Any]]:
    """Bind one sealed Journal terminal to its immutable restoration result."""
    result_ref = event.get("result_ref")
    if not isinstance(result_ref, str):
        raise _error(code, "terminal event has no restoration result")
    intent_root, result_root = _result_roots(root, result_ref, code=code)
    result = _existing_result(root, result_root)
    if result is None:
        raise _error(code, "terminal event result carrier is absent")
    intent_path = intent_root / "intent.json"
    if intent_path.is_symlink() or not intent_path.is_file():
        raise _error(code, "terminal event intent carrier is absent")
    intent = _intent_from_bytes(intent_path.read_bytes())
    intent_sha256 = _digest(canonical_json(intent))
    run = event.get("run")
    run_id = run.get("run_id") if isinstance(run, Mapping) else None
    states = {
        "restored": ("completed", "completed"),
        "no_op": ("completed", "no_op"),
        "partial": ("failed", "partial"),
    }
    effect_refs = _terminal_effect_refs_for_result(root, result_root, result, code=code)
    event_effect_refs = event.get("effect_refs")
    expected_event_effect_refs = ([] if result.get("state") == "no_op" else [*effect_refs, result_ref])
    if result.get("state") == "restored":
        effect_refs_match = event_effect_refs in (effect_refs, [*effect_refs, result_ref])
    else:
        effect_refs_match = event_effect_refs == expected_event_effect_refs
    if (
        intent_root.name != intent_sha256
        or result.get("intent_sha256") != intent_sha256
        or result.get("run_id") != run_id
        or not isinstance(result.get("requested_run_id"), str)
        or result.get("state") not in states
        or (event.get("event"), event.get("outcome")) != states[result["state"]]
        or not effect_refs_match
    ):
        raise _error(code, "terminal event does not bind the exact retained restoration result")
    if result_root != intent_root:
        retry_path = result_root / "retry.json"
        try:
            retry = json.loads(retry_path.read_bytes())
        except (OSError, UnicodeDecodeError, ValueError) as error:
            raise _error(code, "retry-run evidence is unreadable") from error
        if (
            retry_path.is_symlink()
            or not isinstance(retry, dict)
            or set(retry) != {
                "schema", "intent_sha256", "requested_run_id", "retry_of_terminal_event_id",
                "retry_of_terminal_event_digest", "retry_of_result_ref",
            }
            or retry.get("schema") != "caprmedio.framework_image_restoration.retry.v1"
            or retry.get("intent_sha256") != intent_sha256
            or retry.get("requested_run_id") != result.get("requested_run_id")
            or retry.get("retry_of_terminal_event_id") != result.get("retry_of_terminal_event_id")
            or not isinstance(retry.get("retry_of_terminal_event_digest"), str)
            or _SHA256.fullmatch(retry["retry_of_terminal_event_digest"]) is None
            or canonical_json(retry) != retry_path.read_bytes()
        ):
            raise _error(code, "retry-run evidence does not bind the retained result")
    return intent_root, result_root, intent, result


def _owned_pending_event(root: Path, event_id: str) -> tuple[Path, Path, dict[str, str], dict[str, Any]]:
    """Reopen one pending terminal event and prove it belongs to this Action result."""
    work_journal = _work_journal_module()

    if not isinstance(event_id, str) or not event_id.startswith("direct-action:"):
        raise _error("framework-image-restoration-pending-invalid", "pending event ID is not a direct Action event")
    try:
        pending, event, _context, _path = work_journal._read_pending_event(root, event_id)
    except work_journal.WorkJournalError as error:
        raise _error("framework-image-restoration-pending-invalid", str(error)) from error
    if (event.get("event_id") != event_id or event.get("action_id") != RESTORATION_ACTION_ID
            or event.get("event") not in {"completed", "failed", "abandoned"}
            or not isinstance(event.get("result_ref"), str)
            or pending.get("result_ref") != event.get("result_ref")
            or pending.get("effect_refs") != event.get("effect_refs")):
        raise _error("framework-image-restoration-pending-invalid", "pending event is not a restoration terminal record")
    return _owned_result_event(root, event, code="framework-image-restoration-pending-invalid")


def _owned_canonical_terminal(root: Path, event_id: str) -> tuple[Path, Path, dict[str, str], dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Reopen one appended terminal event; pending or started records never retry."""
    if not isinstance(event_id, str) or not event_id.startswith("direct-action:"):
        raise _error("framework-image-restoration-retry-invalid", "retry terminal event ID is not a direct Action event")
    direct_action = _direct_action_module()
    try:
        reopened = direct_action._reopen_event(root, event_id)
    except direct_action.DirectActionJournalError as error:
        raise _error("framework-image-restoration-retry-invalid", str(error)) from error
    if reopened is None:
        raise _error("framework-image-restoration-retry-invalid", "retry terminal event is not canonically appended")
    event, receipt = reopened
    session = event.get("llm_session")
    run = event.get("run")
    if (
        event.get("event_id") != event_id
        or event.get("action_id") != RESTORATION_ACTION_ID
        or event.get("event") not in {"completed", "failed", "abandoned"}
        or not isinstance(session, Mapping)
        or session.get("app") != direct_action.DIRECT_ACTION_APP
        or not isinstance(run, Mapping)
        or run.get("kind") != "action"
        or not isinstance(run.get("run_id"), str)
    ):
        raise _error("framework-image-restoration-retry-invalid", "retry event is not a canonical restoration terminal")
    intent_root, result_root, intent, result = _owned_result_event(
        root, event, code="framework-image-restoration-retry-invalid",
    )
    return intent_root, result_root, intent, result, dict(event), dict(receipt)


def _pending_id_for_result(root: Path, result_root: Path, result: Mapping[str, Any]) -> str | None:
    """Reopen the retained terminal reference, never infer an event ID."""
    reference = result_root / "pending-terminal.json"
    if not reference.exists() and not reference.is_symlink():
        return None
    if reference.is_symlink() or not reference.is_file():
        raise _error("framework-image-restoration-evidence-unsafe", "pending terminal reference is unsafe")
    try:
        value = json.loads(reference.read_bytes())
    except (OSError, UnicodeDecodeError, ValueError) as error:
        raise _error("framework-image-restoration-evidence-invalid", "pending terminal reference is unreadable") from error
    if (not isinstance(value, dict) or set(value) != {"event_id", "result_ref", "run_id"}
            or value.get("result_ref") != _result_ref(root, result_root)
            or value.get("run_id") != result.get("run_id")
            or not isinstance(value.get("event_id"), str)
            or canonical_json(value) != reference.read_bytes()):
        raise _error("framework-image-restoration-evidence-invalid", "pending terminal reference is not canonical")
    _owned_pending_event(root, value["event_id"])
    return value["event_id"]


def _retry_attempt_for_terminal(frozen: _FrozenRestoration, *, requested_run_id: str,
                                retry_of_terminal_event_id: str) -> Path:
    """Admit a deliberate retry of one completed-but-partial restoration only."""
    intent_root, _prior_result_root, prior_intent, prior_result, event, _receipt = _owned_canonical_terminal(
        frozen.root, retry_of_terminal_event_id,
    )
    del intent_root
    if (
        prior_intent != frozen.intent
        or prior_result.get("state") != "partial"
        or event.get("event") != "failed"
        or event.get("outcome") != "partial"
        or prior_result.get("publication") not in {"unchanged", "unpublished"}
        or prior_result.get("prior_selector_sha256") != frozen.selector_sha256
        or prior_result.get("observed_selector_sha256") != frozen.selector_sha256
        or prior_result.get("requested_run_id") == requested_run_id
    ):
        raise _error(
            "framework-image-restoration-retry-ineligible",
            "retry requires a different requested Run and one unpublished or unchanged-selector canonical partial result",
        )
    event_digest = event.get("event_digest")
    if not isinstance(event_digest, str) or _SHA256.fullmatch(event_digest) is None:
        raise _error("framework-image-restoration-retry-invalid", "retry terminal event digest is invalid")
    attempts_root = frozen.private_root / "attempts"
    if attempts_root.exists() or attempts_root.is_symlink():
        if attempts_root.is_symlink() or not attempts_root.is_dir():
            raise _error("framework-image-restoration-evidence-unsafe", "retry restoration root is unsafe")
        try:
            attempts = sorted(attempts_root.iterdir(), key=lambda path: path.name)
        except OSError as error:
            raise _error("framework-image-restoration-evidence-unavailable", "retry restoration root cannot be read") from error
        for attempt in attempts:
            if attempt.name == ".DS_Store" and not attempt.is_symlink() and attempt.is_file():
                continue
            if attempt.is_symlink() or not attempt.is_dir() or _SHA256.fullmatch(attempt.name) is None:
                raise _error("framework-image-restoration-evidence-invalid", "retry restoration root contains an unsafe carrier")
            retry_path = attempt / "retry.json"
            try:
                retry = json.loads(retry_path.read_bytes())
            except (OSError, UnicodeDecodeError, ValueError) as error:
                raise _error("framework-image-restoration-evidence-invalid", "retry evidence is unreadable") from error
            if retry_path.is_symlink() or not isinstance(retry, dict) or canonical_json(retry) != retry_path.read_bytes():
                raise _error("framework-image-restoration-evidence-invalid", "retry evidence is not canonical")
            if (retry.get("retry_of_terminal_event_id") == retry_of_terminal_event_id
                    and retry.get("requested_run_id") != requested_run_id):
                raise _error(
                    "framework-image-restoration-retry-ineligible",
                    "the referenced partial terminal already has a different retry Run",
                )
    return _retry_attempt_directory(
        frozen,
        requested_run_id=requested_run_id,
        retry_of_terminal_event_id=retry_of_terminal_event_id,
        prior_result_ref=str(event["result_ref"]),
        prior_terminal_event_digest=event_digest,
    )


def recover_framework_image_journal(
    project_root: Path | str,
    *,
    journal: DirectActionJournal,
    pending_event_id: str,
) -> dict[str, Any]:
    """Append only one already-sealed pending terminal restoration event.

    This is intentionally not a retry of :func:`restore_framework_image`:
    it opens no Docker transport, does not read the selector for publication,
    and cannot create a new Action event or replacement result.
    """
    try:
        root = _root(project_root)
        _intent_root, result_root, _intent, result = _owned_pending_event(root, pending_event_id)
    except FrameworkImageRestorationError as error:
        return {"state": "recovery_required", "reason": error.code}
    DirectActionSession, DirectActionJournalError = _direct_action_types()

    if not isinstance(journal, DirectActionSession):
        return {"state": "recovery_required", "reason": "framework-image-restoration-recovery-session-required",
                "pending_event_id": pending_event_id}
    try:
        recovered = journal.recover_pending(pending_event_id)
    except DirectActionJournalError as error:
        return {"state": "recovery_required", "reason": error.code, "pending_event_id": pending_event_id}
    if (not isinstance(recovered, Mapping) or recovered.get("disposition") != "recovered"
            or recovered.get("event_id") != pending_event_id):
        return {"state": "recovery_required", "reason": "framework-image-restoration-recovery-unconfirmed",
                "pending_event_id": pending_event_id}
    return {
        "state": "recovered",
        "pending_event_id": pending_event_id,
        "result_ref": _result_ref(root, result_root),
        "prior_result": result,
        "recovery": dict(recovered),
    }


def _observe_retained_result_image(executor: DockerSubprocessExecutor, root: Path, *, image_digest: str,
                                   manifest_sha256: str, source_context_sha256: str) -> None:
    """Reinspect a retained result's selected image without building or running it."""
    try:
        observed = executor.run(("docker", "image", "inspect", image_digest), cwd=root, timeout_seconds=60)
    except OSError as error:
        raise _error("framework-image-restoration-terminal-image-unavailable", "Docker image inspection is unavailable") from error
    if (not isinstance(observed, DockerCommandResult) or not isinstance(observed.stdout, bytes)
            or not isinstance(observed.stderr, bytes) or len(observed.stdout) > _MAX_DOCKER_OUTPUT_BYTES
            or len(observed.stderr) > _MAX_DOCKER_OUTPUT_BYTES or observed.timed_out or observed.exit_code != 0):
        raise _error("framework-image-restoration-terminal-image-invalid", "selected image could not be freshly authenticated")
    try:
        values = json.loads(observed.stdout)
        image = values[0]
        labels = image["Config"]["Labels"]
        valid = (
            len(values) == 1
            and image.get("Id") == image_digest
            and isinstance(labels, dict)
            and labels.get(PACKAGE_IMAGE_LABEL) == manifest_sha256
            and labels.get(SOURCE_CONTEXT_IMAGE_LABEL) == source_context_sha256
        )
    except (IndexError, KeyError, TypeError, ValueError):
        valid = False
    if not valid:
        raise _error("framework-image-restoration-terminal-image-invalid", "selected image differs from retained proof bindings")


def _authenticate_result_attempt(root: Path, result: Mapping[str, Any], proof: BootstrapImageEvidence) -> None:
    """Authenticate the result's attempt reference before it becomes an effect ref."""
    attempt_ref = result.get("attempt_evidence_root")
    if not isinstance(attempt_ref, str) or not attempt_ref:
        raise _error("framework-image-restoration-terminal-proof-invalid", "successful result has no retained attempt evidence")
    if attempt_ref == proof.evidence_root:
        if (
            result.get("attempt_commands_sha256") != proof.commands_sha256
            or result.get("attempt_receipt_sha256") != proof.receipt_sha256
            or result.get("attempt_execution_kind") != "docker-subprocess"
        ):
            raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt fields differ from canonical proof")
        return
    relative = Path(attempt_ref)
    proof_parent = Path(proof.evidence_root).parent
    if (
        relative.is_absolute() or ".." in relative.parts or relative.as_posix() != attempt_ref
        or tuple(relative.parts[:-1]) != proof_parent.parts or not relative.name.startswith("attempt-")
    ):
        raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt reference is not retained bootstrap evidence")
    attempt = root / relative
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink() or not cursor.is_dir():
            raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt evidence path is unsafe")
    evidence_path = attempt / "evidence.toml"
    if evidence_path.is_symlink() or not evidence_path.is_file():
        raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt evidence is absent")
    try:
        payload = evidence_path.read_bytes()
        parsed = tomllib.loads(payload.decode("utf-8"))
        expected = {
            "schema_version", "manifest_sha256", "source_context_sha256", "outcome", "reason", "image_digest",
            "context_sha256", "evidence_root", "commands_sha256", "execution_kind", "started_at", "finished_at",
            "bootstrap_proof_key", "proof_root", "context_root",
        }
        if set(parsed) != expected or parsed.get("schema_version") != 1:
            raise ValueError("attempt evidence schema")
        evidence = BootstrapImageEvidence(**{key: parsed[key] for key in expected if key != "schema_version"})
        if payload != _bootstrap_image._toml(evidence):
            raise ValueError("attempt evidence canonical bytes")
        receipt_sha256 = _digest(payload)
        _bootstrap_image._verify_retained_commands(attempt, evidence)
        context = attempt / "context"
        if _bootstrap_image._tree_digest(context) != evidence.context_sha256:
            raise ValueError("attempt context digest")
    except (OSError, UnicodeDecodeError, ValueError, tomllib.TOMLDecodeError, BootstrapImageError) as error:
        raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt evidence is not authentic") from error
    if (
        evidence.outcome != "verified"
        or evidence.execution_kind != "docker-subprocess"
        or evidence.manifest_sha256 != proof.manifest_sha256
        or evidence.source_context_sha256 != proof.source_context_sha256
        or evidence.image_digest != proof.image_digest
        or evidence.context_sha256 != proof.context_sha256
        or evidence.evidence_root != attempt_ref
        or evidence.bootstrap_proof_key != proof.bootstrap_proof_key
        or evidence.proof_root != proof.proof_root
        or evidence.context_root != proof.context_root
        or result.get("attempt_commands_sha256") != evidence.commands_sha256
        or result.get("attempt_receipt_sha256") != receipt_sha256
        or result.get("attempt_execution_kind") != evidence.execution_kind
    ):
        raise _error("framework-image-restoration-terminal-proof-invalid", "successful result attempt evidence does not bind the canonical proof")


def _retained_result_for_terminal(root: Path, result_ref: str,
                                  executor: DockerSubprocessExecutor) -> tuple[Path, Path, dict[str, str], dict[str, Any], list[str]]:
    """Authenticate an already-observed successful result for Journal-only repair."""
    intent_root, result_root = _result_roots(root, result_ref, code="framework-image-restoration-terminal-invalid")
    result = _existing_result(root, result_root)
    if result is None:
        raise _error("framework-image-restoration-terminal-invalid", "retained restoration result is absent")
    intent_path = intent_root / "intent.json"
    if intent_path.is_symlink() or not intent_path.is_file():
        raise _error("framework-image-restoration-terminal-invalid", "retained restoration intent is absent")
    intent = _intent_from_bytes(intent_path.read_bytes())
    intent_sha256 = _digest(canonical_json(intent))
    requested_run_id = result.get("requested_run_id")
    run_id = result.get("run_id")
    observed_image_digest = result.get("observed_image_digest")
    observed_selector_sha256 = result.get("observed_selector_sha256")
    if (
        intent_root.name != intent_sha256
        or result.get("intent_sha256") != intent_sha256
        or result.get("state") != "restored"
        or not isinstance(requested_run_id, str)
        or not isinstance(run_id, str)
        or not isinstance(observed_image_digest, str)
        or IMAGE_ID.fullmatch(observed_image_digest) is None
        or not isinstance(observed_selector_sha256, str)
        or _SHA256.fullmatch(observed_selector_sha256) is None
        or result.get("old_image_digest") != intent["old_image_digest"]
        or result.get("prior_selector_sha256") != intent["selected_selector_sha256"]
    ):
        raise _error("framework-image-restoration-terminal-invalid", "retained restoration result is not a closed successful Action result")
    prior_selector_path = intent_root / "prior-selector.toml"
    if prior_selector_path.is_symlink() or not prior_selector_path.is_file():
        raise _error("framework-image-restoration-terminal-invalid", "sealed prior selector is absent")
    prior_selector = prior_selector_path.read_bytes()
    prior = _closed_bootstrap_selector(prior_selector)
    if (
        _digest(prior_selector) != intent["selected_selector_sha256"]
        or prior["release"] != intent["manifest_sha256"]
        or prior["image_digest"] != intent["old_image_digest"]
    ):
        raise _error("framework-image-restoration-terminal-invalid", "sealed prior selector does not bind the closed restoration intent")
    try:
        old_proof = read_retained_initial_framework_image(
            root, intent["manifest_sha256"], intent["old_image_digest"],
        )
    except BootstrapImageError as error:
        raise _error(error.code, str(error)) from error
    if (
        old_proof.manifest_sha256 != intent["manifest_sha256"]
        or old_proof.source_context_sha256 != intent["source_context_sha256"]
        or old_proof.receipt_sha256 != intent["retained_proof_receipt_sha256"]
        or old_proof.context_sha256 != intent["retained_context_sha256"]
    ):
        raise _error("framework-image-restoration-terminal-proof-invalid", "sealed original proof no longer binds the closed restoration intent")
    selector = _regular_file(root, Path(CURRENT_SELECTOR_RELATIVE), code="framework-image-restoration-selector-missing").read_bytes()
    selector_sha256 = _digest(selector)
    parsed = _closed_bootstrap_selector(selector)
    if (selector_sha256 != observed_selector_sha256
            or parsed["release"] != intent["manifest_sha256"]
            or parsed["image_digest"] != observed_image_digest):
        raise _error("framework-image-restoration-terminal-input-stale", "current selector differs from the retained successful result")
    if observed_image_digest == intent["old_image_digest"]:
        expected_selector = prior_selector
    else:
        old_image = intent["old_image_digest"].encode("ascii")
        if prior_selector.count(old_image) != 1:
            raise _error("framework-image-restoration-terminal-invalid", "sealed prior selector has no exact image binding")
        expected_selector = prior_selector.replace(old_image, observed_image_digest.encode("ascii"), 1)
    if selector != expected_selector:
        raise _error("framework-image-restoration-terminal-input-stale", "current selector is not the exact sealed image-only replacement")
    publication = result.get("publication")
    expected_publication = "unchanged" if observed_selector_sha256 == intent["selected_selector_sha256"] else "replaced"
    if publication != expected_publication:
        raise _error("framework-image-restoration-terminal-invalid", "retained restoration publication result is inconsistent")
    package = root / ".caprmedio_runtime/framework/releases" / intent["manifest_sha256"]
    package_skill = package / "SKILLS/ca"
    package_records, _package_digest = _inventory(package, code="framework-image-restoration-terminal-package-invalid")
    package_skill_records, _package_skill_digest = _inventory(
        package_skill, code="framework-image-restoration-terminal-package-invalid"
    )
    public_skill_records, _public_skill_digest = _inventory(
        root / PROJECT_SKILL_TARGET, code="framework-image-restoration-terminal-skill-invalid"
    )
    try:
        proof = read_retained_initial_framework_image(root, intent["manifest_sha256"], observed_image_digest)
    except BootstrapImageError as error:
        raise _error(error.code, str(error)) from error
    if (
        proof.outcome != "verified"
        or proof.execution_kind != "docker-subprocess"
        or proof.manifest_sha256 != intent["manifest_sha256"]
        or proof.source_context_sha256 != intent["source_context_sha256"]
        or proof.image_digest != observed_image_digest
        or proof.receipt_sha256 is None
        or result.get("canonical_proof_key") != proof.bootstrap_proof_key
        or result.get("canonical_proof_root") != proof.proof_root
        or result.get("canonical_context_root") != proof.context_root
        or result.get("canonical_proof_receipt_sha256") != proof.receipt_sha256
    ):
        raise _error("framework-image-restoration-terminal-proof-invalid", "retained successful result proof is not current and authentic")
    proof_package_records, _proof_package_digest = _inventory(
        root / proof.context_root / "PACKAGE", code="framework-image-restoration-terminal-proof-invalid"
    )
    proof_skill_records, _proof_skill_digest = _inventory(
        root / proof.context_root / "PACKAGE/SKILLS/ca", code="framework-image-restoration-terminal-proof-invalid"
    )
    if _package_context_records(package_records) != _package_context_records(proof_package_records):
        raise _error("framework-image-restoration-terminal-package-stale", "selected retained package differs from authenticated proof context")
    if package_skill_records != proof_skill_records or public_skill_records != proof_skill_records:
        raise _error("framework-image-restoration-terminal-skill-stale", "public ca Skill differs from authenticated retained proof context")
    if publication == "replaced":
        replacement = _regular_file(
            root, Path(_relative(root, result_root / "replacement-selector.toml")),
            code="framework-image-restoration-terminal-invalid",
        ).read_bytes()
        if replacement != selector:
            raise _error("framework-image-restoration-terminal-input-stale", "retained replacement selector differs from current selection")
    _authenticate_result_attempt(root, result, proof)
    effect_refs = _terminal_effect_refs_for_result(
        root, result_root, result, code="framework-image-restoration-terminal-invalid",
    )
    _observe_retained_result_image(
        executor, root, image_digest=observed_image_digest,
        manifest_sha256=intent["manifest_sha256"], source_context_sha256=intent["source_context_sha256"],
    )
    return intent_root, result_root, intent, result, effect_refs


def recover_framework_image_terminal(
    project_root: Path | str,
    *,
    journal: DirectActionJournal,
    result_ref: str,
    image_executor: DockerExecutor,
) -> dict[str, Any]:
    """Record one already-observed successful restoration; never rebuild or publish.

    The result's bytes and original started Run are immutable.  This recovery
    only authenticates present state, reopens that exact started Run through
    the direct-Action Session, and writes its one missing terminal event.
    """
    try:
        root = _root(project_root)
        executor = _validate_executor(image_executor)
        with selector_publication_lock(root):
            _intent_root, result_root, intent, result, effect_refs = _retained_result_for_terminal(
                root, result_ref, executor,
            )
            DirectActionSession, DirectActionJournalError = _direct_action_types()
            if not isinstance(journal, DirectActionSession):
                return {"state": "recovery_required", "reason": "framework-image-restoration-recovery-session-required"}
            reopen = getattr(journal, "reopen_restoration_for_recording", None)
            if not callable(reopen):
                return {"state": "recovery_required", "reason": "framework-image-restoration-recovery-admission-unavailable"}
            try:
                reopened = reopen(requested_run_id=result["requested_run_id"], intent=intent)
            except DirectActionJournalError as error:
                return {"state": "recovery_required", "reason": error.code}
            run_id = reopened.get("run_id") if isinstance(reopened, Mapping) else None
            if (not isinstance(run_id, str) or run_id != result["run_id"]
                    or reopened.get("disposition") != "recording_only"):
                return {"state": "recovery_required", "reason": "framework-image-restoration-recovery-unconfirmed"}
            terminal = _terminalize(
                journal, run_id, outcome="completed", result_ref=_result_ref(root, result_root),
                effect_refs=effect_refs,
            )
            if not _terminal_confirmed(terminal, "completed"):
                return _pending_reply(result_root, terminal, result_ref=_result_ref(root, result_root), run_id=run_id)
            return {
                "state": "restored",
                "result_ref": _result_ref(root, result_root),
                "run_id": run_id,
                "terminal": dict(terminal.terminal),
                "recording_recovered": True,
            }
    except (FrameworkImageRestorationError, SelectorPublicationLockError) as error:
        return {"state": "recovery_required", "reason": getattr(error, "code", "framework-image-restoration-publication-lock-unavailable")}


def restore_framework_image(
    project_root: Path | str,
    *,
    journal: DirectActionJournal,
    requested_run_id: str,
    expected_selector_sha256: str,
    image_executor: DockerExecutor,
    retry_of_terminal_event_id: str | None = None,
) -> dict[str, Any]:
    """Restore one absent retained bootstrap image without changing N's package.

    This function intentionally has no caller-provided context, commands,
    digest replacement, or selector shape.  A previously retained result for
    the same closed intent is inspection-only; it never becomes permission to
    rebuild or republish, except for one explicit retry of a sealed partial
    terminal that still proves the selector was unchanged.
    """
    try:
        root = _root(project_root)
        if retry_of_terminal_event_id is None:
            prior = _private_result_for_selector(root, expected_selector_sha256)
            if prior is not None:
                private_root, intent, result = prior
                return _return_recorded(root, private_root, intent, result, requested_run_id=requested_run_id)
        elif not isinstance(retry_of_terminal_event_id, str) or not retry_of_terminal_event_id:
            raise _error("framework-image-restoration-retry-invalid", "retry terminal event ID must be a non-empty string")
        executor = _validate_executor(image_executor)
        frozen = _freeze(root, expected_selector_sha256)
        if retry_of_terminal_event_id is None:
            result_root = frozen.private_root
            prior = _existing_result(root, result_root)
            if prior is not None:
                return _return_recorded(root, result_root, frozen.intent, prior, requested_run_id=requested_run_id)
        else:
            result_root = _retry_attempt_for_terminal(
                frozen,
                requested_run_id=requested_run_id,
                retry_of_terminal_event_id=retry_of_terminal_event_id,
            )
            prior = _existing_result(root, result_root)
            if prior is not None:
                return _return_recorded(root, result_root, frozen.intent, prior, requested_run_id=requested_run_id)
        # Do not let a known-busy publisher become a post-build surprise.
        # This is only an availability observation; the actual publication
        # still takes and holds the same lock around its final rechecks.
        with selector_publication_lock(root):
            pass
        daemon_state = _observe_selected_image(executor, frozen)
    except (FrameworkImageRestorationError, SelectorPublicationLockError) as error:
        return {"state": "blocked", "reason": getattr(error, "code", "framework-image-restoration-publication-lock-unavailable")}

    try:
        run_id = _begin(journal, requested_run_id, frozen.intent)
    except FrameworkImageRestorationError as error:
        return {"state": "recovery_required" if error.code.startswith("direct-action-") else "blocked", "reason": error.code}

    def restoration_payload(**values: Any) -> dict[str, Any]:
        return _result_payload(
            frozen,
            retry_of_terminal_event_id=retry_of_terminal_event_id,
            **values,
        )

    def record_result(payload: Mapping[str, Any]) -> str:
        return _write_result(frozen, payload, result_root=result_root)

    if daemon_state == "present":
        try:
            _recheck(frozen, expected_selector=frozen.selector)
            payload = restoration_payload(
                state="no_op", reason="selected image is already present and freshly inspected",
                requested_run_id=requested_run_id, run_id=run_id, observed_image_digest=frozen.old_image_digest,
                observed_selector=frozen.selector, publication="unchanged", evidence=None,
                effect_refs=[],
            )
            result_ref = record_result(payload)
        except FrameworkImageRestorationError as error:
            return {"state": "partial", "reason": error.code, "run_id": run_id}
        terminal = _terminalize(journal, run_id, outcome="no_op", result_ref=result_ref, effect_refs=[])
        if not _terminal_confirmed(terminal, "no_op"):
            return _pending_reply(result_root, terminal, result_ref=result_ref, run_id=run_id)
        return {"state": "no_op", "result_ref": result_ref, "run_id": run_id, "terminal": dict(terminal.terminal)}

    try:
        evidence = produce_retained_framework_image(
            root, frozen.release, frozen.old_image_digest, executor=executor, timeout_seconds=900
        )
    except BootstrapImageError as error:
        payload = restoration_payload(
            state="partial", reason=error.code, requested_run_id=requested_run_id, run_id=run_id,
            observed_image_digest=None, observed_selector=frozen.selector, publication="unpublished",
            evidence=None, effect_refs=[],
        )
        try:
            result_ref = record_result(payload)
        except FrameworkImageRestorationError as recording_error:
            return {"state": "recording_pending", "reason": recording_error.code, "run_id": run_id}
        terminal = _terminalize(journal, run_id, outcome="partial", result_ref=result_ref, effect_refs=[result_ref])
        if not _terminal_confirmed(terminal, "partial"):
            return _pending_reply(result_root, terminal, result_ref=result_ref, run_id=run_id)
        return {"state": "partial", "reason": error.code, "result_ref": result_ref, "run_id": run_id, "terminal": dict(terminal.terminal)}
    if evidence.outcome == "effect_uncertain":
        payload = restoration_payload(
            state="effect_uncertain", reason=evidence.reason, requested_run_id=requested_run_id,
            run_id=run_id, observed_image_digest=evidence.image_digest, observed_selector=frozen.selector,
            publication="unpublished", evidence=evidence, effect_refs=[evidence.evidence_root],
        )
        try:
            result_ref = record_result(payload)
        except FrameworkImageRestorationError:
            result_ref = None
        return {"state": "effect_uncertain", "reason": evidence.reason, "result_ref": result_ref, "run_id": run_id}
    if evidence.outcome != "verified":
        state = "recording_pending" if evidence.outcome == "recording_uncertain" else "partial"
        payload = restoration_payload(
            state=state, reason=evidence.reason, requested_run_id=requested_run_id, run_id=run_id,
            observed_image_digest=evidence.image_digest, observed_selector=frozen.selector,
            publication="unpublished", evidence=evidence, effect_refs=[evidence.evidence_root],
        )
        try:
            result_ref = record_result(payload)
        except FrameworkImageRestorationError as error:
            return {"state": "recording_pending", "reason": error.code, "run_id": run_id}
        if state == "recording_pending":
            return {"state": state, "reason": evidence.reason, "result_ref": result_ref, "run_id": run_id}
        terminal = _terminalize(journal, run_id, outcome="partial", result_ref=result_ref,
                                effect_refs=[evidence.evidence_root, result_ref])
        if not _terminal_confirmed(terminal, "partial"):
            return _pending_reply(result_root, terminal, result_ref=result_ref, run_id=run_id)
        return {"state": "partial", "reason": evidence.reason, "result_ref": result_ref, "run_id": run_id, "terminal": dict(terminal.terminal)}

    try:
        applicable = _verified_produced_evidence(frozen, evidence)
        replacement = _replacement_selector(frozen, str(evidence.image_digest))
        with selector_publication_lock(root):
            _recheck(frozen, expected_selector=frozen.selector)
            if replacement != frozen.selector:
                _write_once(result_root / "replacement-selector.toml", replacement)
                _atomic_file(root / CURRENT_SELECTOR_RELATIVE, replacement)
            _recheck(frozen, expected_selector=replacement)
            reopened = read_retained_initial_framework_image(root, frozen.release, str(evidence.image_digest))
            if reopened != applicable:
                raise _error("framework-image-restoration-proof-stale", "applicable canonical proof changed after publication")
    except (FrameworkImageRestorationError, BootstrapImageError, SelectorPublicationLockError) as error:
        code = getattr(error, "code", "framework-image-restoration-publication-failed")
        try:
            observed_selector = _regular_file(
                root, Path(CURRENT_SELECTOR_RELATIVE), code="framework-image-restoration-selector-missing"
            ).read_bytes()
        except FrameworkImageRestorationError:
            observed_selector = frozen.selector
        publication = (
            "replaced" if replacement != frozen.selector and observed_selector == replacement
            else "unchanged" if observed_selector == frozen.selector else "uncertain"
        )
        effect_refs = [evidence.evidence_root]
        if publication == "replaced":
            effect_refs.append(CURRENT_SELECTOR_RELATIVE)
        payload = restoration_payload(
            state="partial", reason=str(code), requested_run_id=requested_run_id, run_id=run_id,
            observed_image_digest=evidence.image_digest, observed_selector=observed_selector,
            publication=publication, evidence=evidence, effect_refs=effect_refs,
        )
        try:
            result_ref = record_result(payload)
        except FrameworkImageRestorationError as recording_error:
            return {"state": "recording_pending", "reason": recording_error.code, "run_id": run_id}
        terminal = _terminalize(journal, run_id, outcome="partial", result_ref=result_ref,
                                effect_refs=[*effect_refs, result_ref])
        if not _terminal_confirmed(terminal, "partial"):
            return _pending_reply(result_root, terminal, result_ref=result_ref, run_id=run_id)
        return {"state": "partial", "reason": code, "result_ref": result_ref, "run_id": run_id, "terminal": dict(terminal.terminal)}

    observed_selector = replacement
    publication = "unchanged" if replacement == frozen.selector else "replaced"
    effect_refs = _stable_effect_refs([evidence.evidence_root, applicable.evidence_root, CURRENT_SELECTOR_RELATIVE])
    if replacement != frozen.selector:
        effect_refs.append(_relative(root, result_root / "replacement-selector.toml"))
    payload = restoration_payload(
        state="restored", reason="retained-package image and canonical proof were freshly verified",
        requested_run_id=requested_run_id, run_id=run_id, observed_image_digest=evidence.image_digest,
        observed_selector=observed_selector, publication=publication, evidence=evidence, effect_refs=effect_refs,
        canonical_evidence=applicable,
    )
    try:
        result_ref = record_result(payload)
    except FrameworkImageRestorationError as error:
        return {"state": "recording_pending", "reason": error.code, "run_id": run_id}
    terminal = _terminalize(journal, run_id, outcome="completed", result_ref=result_ref,
                            effect_refs=[*effect_refs, result_ref])
    if not _terminal_confirmed(terminal, "completed"):
        return _pending_reply(result_root, terminal, result_ref=result_ref, run_id=run_id)
    return {
        "state": "restored", "image_digest": evidence.image_digest, "result_ref": result_ref,
        "run_id": run_id, "terminal": dict(terminal.terminal),
    }


def _main(argv: list[str] | None = None) -> int:
    """Native boundary: preview is default; effects need all explicit inputs."""
    parser = argparse.ArgumentParser(description="Restore a selected retained bootstrap image")
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--run", dest="requested_run_id")
    parser.add_argument("--operator")
    parser.add_argument("--authorization-ref")
    parser.add_argument("--expected-selector-sha256")
    parser.add_argument("--author", default="anatoly-m")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--recover-pending-event")
    parser.add_argument("--record-retained-result")
    parser.add_argument("--retry-of-terminal-event")
    args = parser.parse_args(argv)
    if not args.execute:
        print(json.dumps({"state": "preview", "reason": "pass --execute with explicit restoration inputs, or one exact pending event ID for recovery"}, sort_keys=True))
        return 0
    DirectActionSession, _DirectActionJournalError = _direct_action_types()

    if args.recover_pending_event is not None:
        if not all((args.operator, args.authorization_ref)):
            parser.error("--execute --recover-pending-event requires --operator and --authorization-ref")
        if any((args.requested_run_id, args.expected_selector_sha256, args.retry_of_terminal_event,
                args.record_retained_result)):
            parser.error("--recover-pending-event is recovery-only and cannot include restoration execution inputs")
        root = _root(args.project_root)
        with DirectActionSession(
            root, author=args.author,
            operator_authorization={"operator": args.operator, "authorization_ref": args.authorization_ref},
            action_id=RESTORATION_ACTION_ID,
        ) as journal:
            result = recover_framework_image_journal(
                root, journal=journal, pending_event_id=args.recover_pending_event,
            )
        print(json.dumps(result, sort_keys=True))
        return 0 if result.get("state") == "recovered" else 1
    if args.record_retained_result is not None:
        if not all((args.operator, args.authorization_ref)):
            parser.error("--execute --record-retained-result requires --operator and --authorization-ref")
        if any((args.requested_run_id, args.expected_selector_sha256, args.retry_of_terminal_event)):
            parser.error("--record-retained-result is terminal-recording-only and cannot include restoration execution inputs")
        root = _root(args.project_root)
        with DirectActionSession(
            root, author=args.author,
            operator_authorization={"operator": args.operator, "authorization_ref": args.authorization_ref},
            action_id=RESTORATION_ACTION_ID,
        ) as journal:
            result = recover_framework_image_terminal(
                root, journal=journal, result_ref=args.record_retained_result,
                image_executor=DockerSubprocessExecutor(),
            )
        print(json.dumps(result, sort_keys=True))
        return 0 if result.get("state") == "restored" else 1
    if not all((args.requested_run_id, args.operator, args.authorization_ref, args.expected_selector_sha256)):
        parser.error("--execute requires --run, --operator, --authorization-ref, and --expected-selector-sha256")

    root = _root(args.project_root)
    with DirectActionSession(
        root, author=args.author,
        operator_authorization={"operator": args.operator, "authorization_ref": args.authorization_ref},
        action_id=RESTORATION_ACTION_ID,
    ) as journal:
        result = restore_framework_image(
            root, journal=journal, requested_run_id=args.requested_run_id,
            expected_selector_sha256=args.expected_selector_sha256, image_executor=DockerSubprocessExecutor(),
            retry_of_terminal_event_id=args.retry_of_terminal_event,
        )
    print(json.dumps(result, sort_keys=True))
    return 0 if result.get("state") in {"restored", "no_op"} else 1


if __name__ == "__main__":
    raise SystemExit(_main())


__all__ = [
    "FrameworkImageRestorationError", "RESTORATION_ACTION_ID",
    "recover_framework_image_journal", "recover_framework_image_terminal", "restore_framework_image",
]
