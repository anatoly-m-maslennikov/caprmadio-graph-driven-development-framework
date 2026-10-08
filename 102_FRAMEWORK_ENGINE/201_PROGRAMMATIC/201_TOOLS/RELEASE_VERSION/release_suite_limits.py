"""Resolve the sealed, private Unit deadline from captured settings bytes."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
import tomllib

from release_contract import ReleaseContractError, canonical_json
from release_suite_reference_context import ReleaseSuiteReferenceContext, _UNIT_DEADLINE_SETTINGS


MAX_UNIT_TIMEOUT_SECONDS = 7200
_DEFAULT_UNIT_TIMEOUT_SECONDS = 3600


@dataclass(frozen=True)
class FrozenUnitDeadline:
    """Resolved Unit deadline and its exact private diagnostic snapshot."""

    timeout_seconds: float
    configured_timeout_seconds: float
    maximum_timeout_seconds: float
    snapshot: bytes
    snapshot_sha256: str


def _invalid(message: str) -> None:
    raise ReleaseContractError("release-suite-deadline-invalid", message)


def _timeout(value: object, *, label: str) -> float:
    if type(value) not in {int, float}:
        _invalid(f"Unit deadline {label} is not finite and positive")
    try:
        result = float(value)
    except OverflowError:
        _invalid(f"Unit deadline {label} is not finite and positive")
    if not math.isfinite(result) or result <= 0:
        _invalid(f"Unit deadline {label} is not finite and positive")
    if result > MAX_UNIT_TIMEOUT_SECONDS:
        _invalid(f"Unit deadline {label} exceeds the governed maximum")
    return result


def _document(payload: bytes, *, label: str) -> dict[str, object]:
    try:
        value = tomllib.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ReleaseContractError("release-suite-deadline-invalid", f"Unit deadline {label} settings are invalid TOML") from error
    if not isinstance(value, dict):
        _invalid(f"Unit deadline {label} settings are malformed")
    return value


def _table(document: dict[str, object], *, label: str, required: bool) -> dict[str, object]:
    value = document.get("release_suite")
    if value is None and not required:
        return {}
    allowed = {"unit_timeout_seconds"}
    if not isinstance(value, dict) or (set(value) != allowed if required else not set(value).issubset(allowed)):
        _invalid(f"Unit deadline {label} settings have an unsupported shape")
    return value


def resolve_unit_deadline(
    context: ReleaseSuiteReferenceContext,
    *,
    fixture_timeout_seconds: float | None = None,
) -> FrozenUnitDeadline:
    """Use only context-captured source bytes; fixture input may only shorten."""

    if not isinstance(context, ReleaseSuiteReferenceContext):
        _invalid("Unit deadline requires a typed reference context")
    captured = dict(context._verified_bytes)
    if len(captured) != len(context._verified_bytes) or not set(_UNIT_DEADLINE_SETTINGS).issubset(captured):
        _invalid("Unit deadline settings were not captured by the private context")
    default_path, instance_path = _UNIT_DEADLINE_SETTINGS
    default_raw, instance_raw = captured[default_path], captured[instance_path]
    default_table = _table(_document(default_raw, label="default",), label="default", required=True)
    instance_table = _table(_document(instance_raw, label="instance"), label="instance", required=False)
    default_timeout = _timeout(default_table["unit_timeout_seconds"], label="default")
    if default_timeout != _DEFAULT_UNIT_TIMEOUT_SECONDS:
        _invalid("Unit deadline default differs from the governed canonical value")
    configured = _timeout(instance_table.get("unit_timeout_seconds", default_timeout), label="configured")
    effective = configured
    if fixture_timeout_seconds is not None:
        fixture = _timeout(fixture_timeout_seconds, label="fixture")
        if fixture > configured:
            _invalid("Unit deadline fixture value may only shorten the configured value")
        effective = fixture
    snapshot = canonical_json({
        "schema_version": 1,
        "default_source_path": default_path,
        "default_source_sha256": hashlib.sha256(default_raw).hexdigest(),
        "instance_source_path": instance_path,
        "instance_source_sha256": hashlib.sha256(instance_raw).hexdigest(),
        "control_context_digest": context.control_context_digest,
        "configured_unit_timeout_seconds": configured,
        "effective_unit_timeout_seconds": effective,
    })
    return FrozenUnitDeadline(
        effective, configured, float(MAX_UNIT_TIMEOUT_SECONDS), snapshot,
        hashlib.sha256(snapshot).hexdigest(),
    )


__all__ = ["FrozenUnitDeadline", "MAX_UNIT_TIMEOUT_SECONDS", "resolve_unit_deadline"]
