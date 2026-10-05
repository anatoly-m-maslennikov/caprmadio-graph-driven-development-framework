"""Shared persisted-resource selection for sealed Release Version inventories.

Selection is deliberately conservative: every ordinary regular file below an
admitted root is retained.  The small excluded set consists only of
well-known transient tooling state.  Secret-shaped path names are refused
while enumerating names, before a caller can read their bytes.
"""

from __future__ import annotations

import os
from pathlib import Path


_EPHEMERAL_DIRECTORIES = frozenset(
    {
        ".caprmedio_tmp",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        ".tox",
        ".nox",
        ".venv",
        ".virtualenv",
        "venv",
        "virtualenv",
        "testcache",
        ".testcache",
    }
)
_EPHEMERAL_FILE_NAMES = frozenset({".DS_Store"})
_BYTECODE_SUFFIXES = frozenset({".pyc", ".pyo"})


class ReleaseInventoryError(RuntimeError):
    """Stable refusal raised before an unsafe inventory can be consumed."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _is_secret_name(name: str) -> bool:
    return name == ".env" or name.startswith(".env.") or name.endswith(".env")


def refuse_secret_path(path: str | Path) -> None:
    """Refuse secret-shaped components without opening the named path."""

    value = Path(path)
    for component in value.parts:
        if _is_secret_name(component):
            raise ReleaseInventoryError(
                "release-inventory-secret-refused",
                f"secret-shaped path is not admitted to a release inventory: {value.as_posix()}",
            )


def _is_ephemeral_directory(name: str) -> bool:
    return name in _EPHEMERAL_DIRECTORIES


def _is_ephemeral_file(name: str) -> bool:
    return name in _EPHEMERAL_FILE_NAMES or Path(name).suffix in _BYTECODE_SUFFIXES


def persistent_regular_files(root: Path, directory: Path) -> list[Path]:
    """Return ordered persisted files below ``directory`` without reading bytes.

    ``root`` and ``directory`` are already validated by each boundary for its
    own public error type.  This helper only decides membership and refuses
    symlinks or non-regular entries that could make a sealed tree ambiguous.
    """

    try:
        directory.relative_to(root)
    except ValueError as error:
        raise ReleaseInventoryError("release-inventory-path-unsafe", "inventory root escapes project") from error
    refuse_secret_path(directory.relative_to(root))
    files: list[Path] = []
    for current, directories, names in os.walk(directory, topdown=True, followlinks=False):
        current_path = Path(current)
        retained_directories: list[str] = []
        for name in sorted(directories):
            path = current_path / name
            relative = path.relative_to(root)
            refuse_secret_path(relative)
            if _is_ephemeral_directory(name):
                continue
            if path.is_symlink():
                raise ReleaseInventoryError(
                    "release-inventory-symlink",
                    f"symlink is not admitted: {relative.as_posix()}",
                )
            if not path.is_dir():
                raise ReleaseInventoryError(
                    "release-inventory-invalid",
                    f"inventory directory is not a regular directory: {relative.as_posix()}",
                )
            retained_directories.append(name)
        directories[:] = retained_directories
        for name in sorted(names):
            path = current_path / name
            relative = path.relative_to(root)
            refuse_secret_path(relative)
            if _is_ephemeral_file(name):
                continue
            if path.is_symlink():
                raise ReleaseInventoryError(
                    "release-inventory-symlink",
                    f"symlink is not admitted: {relative.as_posix()}",
                )
            if not path.is_file():
                raise ReleaseInventoryError(
                    "release-inventory-invalid",
                    f"inventory entry is not a regular file: {relative.as_posix()}",
                )
            files.append(path)
    return sorted(files, key=lambda path: path.relative_to(directory).as_posix())


__all__ = ["ReleaseInventoryError", "persistent_regular_files", "refuse_secret_path"]
