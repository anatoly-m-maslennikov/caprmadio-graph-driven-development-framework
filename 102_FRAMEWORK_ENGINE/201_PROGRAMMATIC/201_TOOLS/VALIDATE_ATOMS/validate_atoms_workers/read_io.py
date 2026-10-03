"""Bound all reads, reject protected paths, and fingerprint actual inputs."""

from dataclasses import dataclass, field
import hashlib
import os
from pathlib import Path
import stat
import time
from typing import Any


class ReadFailure(OSError):
    pass


class LimitReached(RuntimeError):
    def __init__(self, limit: str) -> None:
        super().__init__(limit)
        self.limit = limit


def protected(path: Path) -> bool:
    return any(
        part == ".env"
        or part.startswith(".env.")
        or part.endswith(".env")
        or part in {".ssh", ".aws", ".gnupg"}
        for part in path.parts
    )


def open_regular(path: Path, *, directory: bool = False) -> int:
    """Open every path component with O_NOFOLLOW to close symlink TOCTOU gaps."""
    descriptor = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parts[1:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
        return os.open(path.name, flags | (os.O_DIRECTORY if directory else 0), dir_fd=descriptor)
    finally:
        os.close(descriptor)


@dataclass
class ReadContext:
    roots: list[str]
    limits: dict[str, int]
    started: float = field(default_factory=time.monotonic)
    bytes_read: int = 0
    fingerprints: dict[str, str] = field(default_factory=dict)
    sizes: dict[str, int] = field(default_factory=dict)
    inventories: dict[str, tuple[str, ...]] = field(default_factory=dict)
    candidates: set[str] = field(default_factory=set)

    def checkpoint(self) -> None:
        if time.monotonic() - self.started >= self.limits["timeout_seconds"]:
            raise LimitReached("timeout_seconds")

    def allowed(self, path: Path) -> Path:
        self.checkpoint()
        normalized = Path(os.path.abspath(path))
        if protected(normalized):
            raise ReadFailure("Protected path.")
        if not any(normalized.is_relative_to(Path(root)) for root in self.roots):
            raise ReadFailure("Path is outside allowed_read_roots.")
        # Treat even in-bound symlinks as unsupported rather than guess identities.
        if normalized.resolve() != normalized:
            raise ReadFailure("Symlink paths are not admitted.")
        return normalized

    def read(self, path: Path, *, remember: bool = True) -> bytes:
        path = self.allowed(path)
        with os.fdopen(open_regular(path), "rb") as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode):
                raise ReadFailure("Input is not a regular file.")
            self.check_size(info.st_size)
            raw = stream.read(info.st_size)
            self.bytes_read += len(raw)
            self.checkpoint()
            after = os.fstat(stream.fileno())
            fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")
            if any(getattr(after, field) != getattr(info, field) for field in fields):
                raise ReadFailure("Input changed during read.")
        if remember:
            self.fingerprints.setdefault(str(path), hashlib.sha256(raw).hexdigest())
            self.sizes[str(path)] = len(raw)
        return raw

    def check_size(self, size: int) -> None:
        if size > self.limits["max_file_bytes"]:
            raise LimitReached("max_file_bytes")
        if self.bytes_read + size > self.limits["max_total_read_bytes"]:
            raise LimitReached("max_total_read_bytes")

    def inventory(self, root: Path, *, remember: bool = True) -> list[Path]:
        root = self.allowed(root)
        pending = [root]
        found: list[Path] = []
        while pending:
            path = pending.pop()
            self.checkpoint()
            if path.is_symlink():
                found.append(path)  # Report without following or reading.
            elif path.is_dir():
                self.allowed(path)
                descriptor = open_regular(path, directory=True)
                try:
                    with os.scandir(descriptor) as entries:
                        for entry in entries:
                            self.checkpoint()
                            if entry.name != ".DS_Store":
                                pending.append(path / entry.name)
                            if len(pending) > 1_000_000:
                                raise ReadFailure("Directory traversal exceeds host ceiling.")
                finally:
                    os.close(descriptor)
            elif path.suffix.lower() == ".md" or protected(path):
                found.append(path)
            if len(found) > self.limits["max_candidates"]:
                raise LimitReached("max_candidates")
        names = tuple(sorted(str(path) for path in found))
        if remember:
            self.inventories[str(root)] = names
        return [Path(name) for name in names]

    def discover(self, roots: list[str]) -> list[Path]:
        found = set()
        for root in sorted(roots):
            found.update(self.inventory(Path(root)))
            if len(found) > self.limits["max_candidates"]:
                raise LimitReached("max_candidates")
        return sorted(found)

    def currentness(self) -> dict[str, Any]:
        affected: list[dict[str, str]] = []
        for name, digest in sorted(self.fingerprints.items()):
            try:
                current = hashlib.sha256(self.read(Path(name), remember=False)).hexdigest()
            except OSError:
                current = ""
            if current != digest:
                affected.append({"path": name, "sha256": digest})
        for root, members in sorted(self.inventories.items()):
            try:
                names = tuple(str(path) for path in self.inventory(Path(root), remember=False))
            except OSError:
                names = ()
            if names != members:
                affected.append({"path": root})
        return {"state": "changed" if affected else "unchanged", "affected_inputs": affected}
