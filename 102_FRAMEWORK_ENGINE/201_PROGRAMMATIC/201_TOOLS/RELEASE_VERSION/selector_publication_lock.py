"""One persistent OS lock for selected Framework selector publication.

Promotion and explicit same-package image restoration share this boundary.
The Project root and Framework directory descriptors anchor ownership even if
the regular lock file or Framework directory is replaced. Process exit releases
ownership, while canonical started Action evidence still determines whether an
effect may run.
"""
from __future__ import annotations

from contextlib import contextmanager
import fcntl
import math
import os
from pathlib import Path
import stat
import time
from typing import Iterator


LOCK_RELATIVE = Path(".caprmedio_runtime/framework/selector-publication.lock")


class SelectorPublicationLockError(RuntimeError):
    """A publication lock cannot safely admit this invocation."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _recheck(chain: list[tuple[Path, os.stat_result]], parent: int,
             descriptor: int) -> None:
    for path, observed in chain:
        current = path.lstat()
        if (not stat.S_ISDIR(current.st_mode)
                or (current.st_dev, current.st_ino) != (observed.st_dev, observed.st_ino)):
            raise SelectorPublicationLockError("selector-publication-lock-unsafe", "lock ancestor changed")
    current = os.stat(LOCK_RELATIVE.name, dir_fd=parent, follow_symlinks=False)
    opened = os.fstat(descriptor)
    if (not stat.S_ISREG(current.st_mode) or current.st_nlink != 1
            or (current.st_dev, current.st_ino) != (opened.st_dev, opened.st_ino)):
        raise SelectorPublicationLockError("selector-publication-lock-unsafe", "lock carrier changed")


@contextmanager
def selector_publication_lock(project_root: Path | str, *,
                              timeout_seconds: float = 30) -> Iterator[None]:
    """Acquire anchored exclusive flocks, refusing unsafe carriers or bounded busy state."""
    if (isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float))
            or not math.isfinite(timeout_seconds) or not 0 <= timeout_seconds <= 30):
        raise SelectorPublicationLockError("selector-publication-lock-invalid", "timeout must be within [0, 30]")
    try:
        root = Path(project_root).absolute()
    except (TypeError, ValueError, OSError) as error:
        raise SelectorPublicationLockError("selector-publication-lock-invalid", "Project root is invalid") from error
    if ".." in root.parts:
        raise SelectorPublicationLockError("selector-publication-lock-unsafe", "Project root contains traversal")
    descriptors: list[int] = []
    descriptor = None
    locked_descriptors: list[int] = []
    try:
        flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
        parent = os.open(root.anchor, flags)
        descriptors.append(parent)
        chain: list[tuple[Path, os.stat_result]] = [(Path(root.anchor), os.fstat(parent))]
        current = Path(root.anchor)
        parts = [*root.parts[1:], *LOCK_RELATIVE.parent.parts]
        for index, part in enumerate(parts):
            current /= part
            if index >= len(root.parts) - 1:
                try:
                    os.mkdir(part, mode=0o700, dir_fd=parent)
                except FileExistsError:
                    pass
            parent = os.open(part, flags, dir_fd=parent)
            descriptors.append(parent)
            chain.append((current, os.fstat(parent)))
        descriptor = os.open(LOCK_RELATIVE.name,
                             os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC,
                             0o600, dir_fd=parent)
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode) or opened.st_nlink != 1:
            raise SelectorPublicationLockError("selector-publication-lock-unsafe", "lock carrier must be a regular unaliased file")
        deadline = time.monotonic() + timeout_seconds
        # Lock only the Project root, Framework directory, and regular carrier.
        # The root is stable across runtime/Framework directory replacement;
        # directory ownership also prevents replacement of the carrier from
        # producing an independently lockable inode during this context.
        project_descriptor = descriptors[len(root.parts) - 1]
        for lock_descriptor in (project_descriptor, parent, descriptor):
            while True:
                _recheck(chain, parent, descriptor)
                try:
                    fcntl.flock(lock_descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    locked_descriptors.append(lock_descriptor)
                    break
                except BlockingIOError as error:
                    if time.monotonic() >= deadline:
                        raise SelectorPublicationLockError("selector-publication-lock-busy", "selector publication is exclusively owned") from error
                    time.sleep(min(0.05, max(0, deadline - time.monotonic())))
        _recheck(chain, parent, descriptor)
    except BaseException as error:
        try:
            for lock_descriptor in reversed(locked_descriptors):
                fcntl.flock(lock_descriptor, fcntl.LOCK_UN)
        finally:
            if descriptor is not None:
                os.close(descriptor)
            for directory in reversed(descriptors):
                os.close(directory)
        if isinstance(error, OSError):
            raise SelectorPublicationLockError("selector-publication-lock-unavailable", "safe lock acquisition failed") from error
        raise
    try:
        yield
        try:
            _recheck(chain, parent, descriptor)
        except OSError as error:
            raise SelectorPublicationLockError("selector-publication-lock-unsafe", "lock carrier or ancestor disappeared") from error
    finally:
        try:
            for lock_descriptor in reversed(locked_descriptors):
                fcntl.flock(lock_descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)
            for directory in reversed(descriptors):
                os.close(directory)


__all__ = ["SelectorPublicationLockError", "selector_publication_lock"]
