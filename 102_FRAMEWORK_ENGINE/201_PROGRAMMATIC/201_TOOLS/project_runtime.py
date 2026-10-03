"""Shared CAPRMEDIO runtime and temporary-path boundaries."""

from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path


RUNTIME_DIRECTORY = Path(".caprmedio_runtime")
TEMPORARY_DIRECTORY = Path(".caprmedio_tmp")
OWNER = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")


class TemporaryBoundaryError(RuntimeError):
    """A disposable Carrier cannot be placed in the required Project Temporary State."""


def repository_root(reference: Path | str) -> Path:
    """Resolve the nearest Git repository containing ``reference``."""

    candidate = Path(reference).expanduser().resolve()
    if not candidate.is_dir():
        candidate = candidate.parent
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise TemporaryBoundaryError(f"cannot resolve Project root from {candidate}")


def owned_temporary_root(repository: Path | str, owner: str) -> Path:
    """Create and return one component-owned temporary directory."""

    if not OWNER.fullmatch(owner):
        raise TemporaryBoundaryError(f"invalid temporary-state owner: {owner}")
    root = repository_root(repository)
    directory = root / TEMPORARY_DIRECTORY / owner
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def atomic_tempfile(
    destination: Path,
    owner: str,
    *,
    repository: Path | str | None = None,
    prefix: str | None = None,
    suffix: str = "",
) -> tuple[int, str]:
    """Allocate an atomic-write intermediate only below Project Temporary State."""

    root = repository_root(repository if repository is not None else destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    directory = owned_temporary_root(root, owner) / "atomic"
    directory.mkdir(parents=True, exist_ok=True)
    if os.stat(directory).st_dev != os.stat(destination.parent).st_dev:
        raise TemporaryBoundaryError(
            f"temporary state and destination are on different filesystems: {directory} -> {destination}"
        )
    return tempfile.mkstemp(
        prefix=prefix or f".{destination.name}.",
        suffix=suffix,
        dir=directory,
    )


__all__ = [
    "RUNTIME_DIRECTORY",
    "TEMPORARY_DIRECTORY",
    "TemporaryBoundaryError",
    "atomic_tempfile",
    "owned_temporary_root",
    "repository_root",
]
