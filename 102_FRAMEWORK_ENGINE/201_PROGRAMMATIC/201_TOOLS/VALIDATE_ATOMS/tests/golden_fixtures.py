"""Filesystem setup and independent fingerprints for golden command tests."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from typing import Any
import warnings

HERE = Path(__file__).resolve().parent
TEMP_PARENT = HERE.parents[4] / ".caprmedio_tmp"


@contextmanager
def isolated_directory() -> Iterator[str]:
    # Cleanup is a harness operation, separate from validator read-only checks.
    root = Path(tempfile.mkdtemp(prefix="validate-atoms-e2e-", dir=TEMP_PARENT)).resolve()
    try:
        yield str(root)
    finally:
        if root.parent != TEMP_PARENT.resolve() or not root.name.startswith("validate-atoms-e2e-"):
            raise AssertionError("refusing cleanup outside the harness temporary directory")
        try:
            for path in sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True):
                if path.is_symlink() or path.is_file():
                    path.unlink()
                else:
                    path.rmdir()
            root.rmdir()
        except PermissionError:
            warnings.warn(f"Host denied temporary fixture cleanup; retained {root}", RuntimeWarning)


def no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)


def fixture_path(relative: str) -> Path:
    path = HERE / relative
    if not isinstance(relative, str) or Path(relative).is_absolute():
        raise AssertionError(f"not a relative test path: {relative!r}")
    if not path.resolve().is_relative_to(HERE):
        raise AssertionError(f"test path escapes tests/: {relative!r}")
    return path


def fingerprint(root: Path) -> dict[str, tuple[str, int] | tuple[str, int, str]]:
    """Include every directory/file/link and mode; never follow a fixture link."""
    result: dict[str, tuple[str, int] | tuple[str, int, str]] = {}
    for path in sorted(root.rglob("*")):
        name = str(path.relative_to(root))
        mode = path.lstat().st_mode
        if path.is_symlink():
            result[name] = ("link", mode, os.readlink(path))
        elif path.is_file():
            result[name] = ("file", mode, hashlib.sha256(path.read_bytes()).hexdigest())
        else:
            result[name] = ("directory", mode)
    return result


def copy_fixtures(relative_paths: list[str], root: Path) -> None:
    for relative in relative_paths:
        source = fixture_path(relative)
        destination = root / source.relative_to(HERE / "fixtures")
        if source.is_dir():
            shutil.copytree(source, destination, dirs_exist_ok=True, symlinks=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination, follow_symlinks=False)
