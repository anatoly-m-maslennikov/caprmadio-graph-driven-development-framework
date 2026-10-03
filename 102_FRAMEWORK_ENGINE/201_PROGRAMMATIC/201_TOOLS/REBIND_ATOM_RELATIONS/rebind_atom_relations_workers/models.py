"""Typed CA-R-1049 and CA-M-156 relation-rebinding input and state."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


class RebindError(RuntimeError):
    """One stable, machine-readable failure from REBIND_ATOM_RELATIONS."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


@dataclass(frozen=True)
class Request:
    """One complete, source-specific relation rebind request."""

    source_path: str
    expected_sha256: str
    expected_version: int
    updated_at: str
    rewrite_map: dict[str, dict[str, str]]
    removal_map: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class State:
    """Observed source and registered active-target facts for one request."""

    root: Path
    source: Path
    source_relative: str
    source_bytes: bytes
    active_target_ids: frozenset[str]


@dataclass(frozen=True)
class Plan:
    """One sealed in-place Atom update prepared by CA-M-156."""

    output: bytes
    receipt: dict[str, object]
