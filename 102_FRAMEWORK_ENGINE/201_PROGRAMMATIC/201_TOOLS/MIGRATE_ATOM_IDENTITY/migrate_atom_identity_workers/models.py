"""Typed request state for the CA-R-1048 identity-migration Doer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


class MigrationError(RuntimeError):
    """One stable, machine-readable identity-migration failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


@dataclass(frozen=True)
class Request:
    """One sealed carrier migration approved before the Tool runs."""

    source_path: str
    destination_path: str
    expected_sha256: str
    expected_version: int
    approved_old_identity: str | None
    new_atom_id: str
    classification: str
    source_filename: str
    destination_prefix: tuple[str, ...]
    summary: str
    frontmatter_removals: tuple[str, ...]
    frontmatter_updates: dict[str, Any]
    relation_rewrite_map: dict[str, dict[str, str]]
    relation_removal_map: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class State:
    """Observed filesystem facts; collection belongs outside the pure manager."""

    root: Path
    source: Path
    destination: Path
    source_relative: str
    destination_relative: str
    source_bytes: bytes
    source_role: str
    destination_role: str
    new_identity_collisions: tuple[str, ...]
    old_identity_collisions: tuple[str, ...]


@dataclass(frozen=True)
class Plan:
    """A fully validated, single-carrier mutation prepared by CA-M-155."""

    output: bytes
    receipt: dict[str, Any]
