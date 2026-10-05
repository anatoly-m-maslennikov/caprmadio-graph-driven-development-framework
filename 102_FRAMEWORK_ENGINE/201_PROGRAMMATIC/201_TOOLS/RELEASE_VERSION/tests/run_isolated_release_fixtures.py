#!/usr/bin/env python3
"""Prepare and optionally run Release fixtures in an isolated Linux container.

The default action creates a retained, source-current snapshot only.  Docker
is never contacted unless the caller explicitly supplies ``--run``.  A run
first proves that the immutable image's dependency inputs and installed
dependencies match the snapshot, then binds that snapshot read-only at
``/workspace``.  It never mounts a Docker socket or the working checkout.

This is fixture evidence only.  It does not build, install, select, promote,
or retire a CAPRMEDIO release image.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Sequence


TEST_ROOT = Path(__file__).resolve().parent
RELEASE_ROOT = TEST_ROOT.parent
TOOLS_ROOT = RELEASE_ROOT.parent
for _path in (TOOLS_ROOT, RELEASE_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from release_inventory import ReleaseInventoryError, persistent_regular_files, refuse_secret_path  # noqa: E402


ENGINE_ROOT = Path("102_FRAMEWORK_ENGINE")
SNAPSHOT_FILE = ".caprmedio_isolated_release_fixture_snapshot.json"
IMAGE_IDENTIFIER = re.compile(r"^sha256:[0-9a-f]{64}$")
RELEASE_FIXTURE_WORKDIR = "/workspace/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
RETAINED_RUNNER = "../tests/retained_fixture_runner.py"
DEPENDENCY_GROUPS = ("rmed-workflow-mcp", "workflow-orchestrator", "validate-atoms")
DEPENDENCY_MODULES = {
    "pydantic": "pydantic",
    "PyYAML": "yaml",
    "mcp": "mcp",
    "jsonschema": "jsonschema",
    "dbos": "dbos",
}


class FixtureIsolationError(RuntimeError):
    """One safe fixture-isolation precondition was not met."""


@dataclass(frozen=True)
class SnapshotRecord:
    path: str
    mode: int
    sha256: str


@dataclass(frozen=True)
class SealedFixtureSnapshot:
    path: str
    source_digest: str
    records: tuple[SnapshotRecord, ...]
    dependency_requirements: dict[str, str]


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_json(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _refuse_secret(relative: str | Path) -> None:
    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise FixtureIsolationError(f"{error.code}: {error}") from error


def _regular_file(project: Path, relative: Path) -> Path:
    _refuse_secret(relative)
    path = project / relative
    if path.is_symlink() or not path.is_file():
        raise FixtureIsolationError(f"snapshot input is not a regular file: {relative.as_posix()}")
    try:
        path.resolve(strict=True).relative_to(project)
    except ValueError as error:
        raise FixtureIsolationError(f"snapshot input escapes Project: {relative.as_posix()}") from error
    return path


def _record(project: Path, path: Path) -> SnapshotRecord:
    try:
        relative = path.relative_to(project)
    except ValueError as error:
        raise FixtureIsolationError("snapshot input is outside the Project") from error
    _refuse_secret(relative)
    if path.is_symlink() or not path.is_file():
        raise FixtureIsolationError(f"snapshot input is not a regular file: {relative.as_posix()}")
    payload = path.read_bytes()
    return SnapshotRecord(relative.as_posix(), stat.S_IMODE(path.stat().st_mode), _sha256(payload))


def _dependency_requirements(pyproject: bytes) -> dict[str, str]:
    try:
        document = tomllib.loads(pyproject.decode("utf-8"))
        groups = document["dependency-groups"]
    except (KeyError, TypeError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise FixtureIsolationError("pyproject.toml has no valid dependency groups") from error
    if not isinstance(groups, dict):
        raise FixtureIsolationError("pyproject dependency groups are invalid")
    requirements: dict[str, str] = {}
    for group in DEPENDENCY_GROUPS:
        values = groups.get(group)
        if not isinstance(values, list):
            raise FixtureIsolationError(f"missing dependency group: {group}")
        for value in values:
            if not isinstance(value, str):
                raise FixtureIsolationError(f"invalid dependency in group: {group}")
            match = re.fullmatch(r"([A-Za-z0-9_-]+)(.*)", value)
            if match is None:
                raise FixtureIsolationError(f"invalid dependency requirement: {value}")
            name, specifier = match.groups()
            if name not in DEPENDENCY_MODULES:
                continue
            if name in requirements and requirements[name] != specifier:
                raise FixtureIsolationError(f"conflicting fixture dependency requirement: {name}")
            requirements[name] = specifier
    if set(requirements) != set(DEPENDENCY_MODULES):
        missing = sorted(set(DEPENDENCY_MODULES) - set(requirements))
        raise FixtureIsolationError(f"fixture dependency requirements are incomplete: {', '.join(missing)}")
    return dict(sorted(requirements.items()))


def _collect_records(project: Path) -> tuple[tuple[SnapshotRecord, ...], dict[str, str]]:
    inputs = [_regular_file(project, Path("pyproject.toml")), _regular_file(project, Path("uv.lock"))]
    engine = project / ENGINE_ROOT
    if engine.is_symlink() or not engine.is_dir():
        raise FixtureIsolationError("Framework Engine source directory is absent or unsafe")
    try:
        engine_files = persistent_regular_files(project, engine)
    except ReleaseInventoryError as error:
        raise FixtureIsolationError(f"{error.code}: {error}") from error
    records = tuple(sorted((_record(project, path) for path in [*inputs, *engine_files]), key=lambda record: record.path))
    if len({record.path for record in records}) != len(records):
        raise FixtureIsolationError("snapshot source records are duplicated")
    pyproject = (project / "pyproject.toml").read_bytes()
    return records, _dependency_requirements(pyproject)


def _source_digest(records: Sequence[SnapshotRecord]) -> str:
    return _sha256(_canonical_json([asdict(record) for record in records]))


def _copy_record(project: Path, snapshot: Path, record: SnapshotRecord) -> None:
    relative = Path(record.path)
    source = _regular_file(project, relative)
    actual = _record(project, source)
    if actual != record:
        raise FixtureIsolationError(f"source changed while preparing snapshot: {record.path}")
    target = snapshot / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target, follow_symlinks=False)
    os.chmod(target, record.mode)
    observed = _record(snapshot, target)
    if observed != record:
        raise FixtureIsolationError(f"snapshot copy does not match source: {record.path}")


def prepare_snapshot(project: Path, snapshot_parent: Path) -> SealedFixtureSnapshot:
    """Copy a complete secret-checked Engine fixture snapshot without Docker."""

    project = project.resolve(strict=True)
    snapshot_parent = snapshot_parent.resolve(strict=True)
    if snapshot_parent.is_symlink() or not snapshot_parent.is_dir():
        raise FixtureIsolationError("snapshot parent is absent or unsafe")
    records, dependencies = _collect_records(project)
    digest = _source_digest(records)
    snapshot = Path(tempfile.mkdtemp(prefix=f"caprmedio-release-fixtures-{digest[:12]}-", dir=snapshot_parent))
    os.chmod(snapshot, 0o755)
    for record in records:
        _copy_record(project, snapshot, record)
    copied_records, copied_dependencies = _collect_records(snapshot)
    if copied_records != records or copied_dependencies != dependencies or _source_digest(copied_records) != digest:
        raise FixtureIsolationError("sealed snapshot does not exactly match current source")
    sealed = SealedFixtureSnapshot(str(snapshot), digest, records, dependencies)
    (snapshot / SNAPSHOT_FILE).write_bytes(_canonical_json({
        "source_digest": sealed.source_digest,
        "records": [asdict(record) for record in sealed.records],
        "dependency_requirements": sealed.dependency_requirements,
    }))
    return sealed


def _parse_version(value: str) -> tuple[int, ...]:
    match = re.fullmatch(r"(\d+(?:\.\d+)*)", value)
    if match is None:
        raise FixtureIsolationError(f"unsupported installed dependency version: {value}")
    parts = tuple(int(part) for part in match.group(1).split("."))
    while len(parts) > 1 and parts[-1] == 0:
        parts = parts[:-1]
    return parts


def _matches_requirement(version: str, requirement: str) -> bool:
    observed = _parse_version(version)
    pieces = requirement.split(",")
    if not pieces or any(not piece for piece in pieces):
        raise FixtureIsolationError(f"unsupported dependency requirement: {requirement}")
    clauses: list[tuple[str, str]] = []
    for piece in pieces:
        match = re.fullmatch(r"(==|>=|<=|>|<)(\d+(?:\.\d+)*)", piece)
        if match is None:
            raise FixtureIsolationError(f"unsupported dependency requirement: {requirement}")
        clauses.append(match.groups())
    for operator, required_text in clauses:
        required = _parse_version(required_text)
        if not {
            "==": observed == required,
            ">=": observed >= required,
            "<=": observed <= required,
            ">": observed > required,
            "<": observed < required,
        }[operator]:
            return False
    return True


def _require_image_identifier(image: str) -> None:
    """Reject tags and partial digests before any Docker invocation."""

    if IMAGE_IDENTIFIER.fullmatch(image) is None:
        raise FixtureIsolationError("image must be a full sha256:<64 lowercase hex> Docker image ID")


def _docker_json(argv: Sequence[str]) -> dict[str, Any]:
    result = subprocess.run(tuple(argv), check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise FixtureIsolationError(f"Docker preflight failed: {result.stderr.strip() or result.stdout.strip()}")
    try:
        document = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise FixtureIsolationError("Docker preflight did not return JSON") from error
    if not isinstance(document, dict):
        raise FixtureIsolationError("Docker preflight JSON is invalid")
    return document


def verify_image_compatibility(image: str, snapshot: SealedFixtureSnapshot) -> dict[str, Any]:
    """Require base dependency inputs and imports to match before source binding."""

    _require_image_identifier(image)
    code = """
import hashlib, importlib, importlib.metadata, json
paths = ('/workspace/pyproject.toml', '/workspace/uv.lock')
dependencies = {'pydantic': 'pydantic', 'PyYAML': 'yaml', 'mcp': 'mcp', 'jsonschema': 'jsonschema', 'dbos': 'dbos'}
for module in dependencies.values():
    importlib.import_module(module)
print(json.dumps({
    'inputs': {path.rsplit('/', 1)[-1]: hashlib.sha256(open(path, 'rb').read()).hexdigest() for path in paths},
    'versions': {distribution: importlib.metadata.version(distribution) for distribution in dependencies},
}, sort_keys=True))
"""
    document = _docker_json((
        "docker", "run", "--rm", "--network", "none", "--read-only",
        "--tmpfs", "/tmp:rw,nosuid,nodev,mode=1777,size=64m",
        "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
        "--pids-limit", "64", "--memory", "256m", "--entrypoint", "/opt/venv/bin/python",
        image, "-c", code,
    ))
    expected_inputs = {
        "pyproject.toml": next(record.sha256 for record in snapshot.records if record.path == "pyproject.toml"),
        "uv.lock": next(record.sha256 for record in snapshot.records if record.path == "uv.lock"),
    }
    if document.get("inputs") != expected_inputs:
        raise FixtureIsolationError("immutable image dependency inputs differ from the sealed source snapshot")
    versions = document.get("versions")
    if not isinstance(versions, dict):
        raise FixtureIsolationError("immutable image did not report dependency versions")
    for distribution, requirement in snapshot.dependency_requirements.items():
        version = versions.get(distribution)
        if not isinstance(version, str) or not _matches_requirement(version, requirement):
            raise FixtureIsolationError(f"immutable image dependency does not satisfy source requirement: {distribution}{requirement}")
    return document


def run_isolated_fixtures(image: str, snapshot: SealedFixtureSnapshot, tests: Sequence[str]) -> int:
    """Run selected unchanged unittest fixtures with a read-only source bind."""

    verify_image_compatibility(image, snapshot)
    if not tests:
        raise FixtureIsolationError("at least one selected unittest target is required for --run")
    command = (
        "docker", "run", "--rm", "--network", "none", "--read-only",
        "--tmpfs", "/tmp:rw,nosuid,nodev,mode=1777,size=1g",
        "--tmpfs", "/home/caprmedio:rw,nosuid,nodev,mode=0700,size=32m",
        "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
        "--pids-limit", "256", "--memory", "2g", "--cpus", "2",
        "--user", "1000:1000",
        "--mount", f"type=bind,source={snapshot.path},target=/workspace,readonly",
        "--workdir", RELEASE_FIXTURE_WORKDIR,
        "--env", "HOME=/home/caprmedio",
        "--env", "PYTHONNOUSERSITE=1",
        "--env", "PYTHONDONTWRITEBYTECODE=1",
        "--env", f"PYTHONPATH={RELEASE_FIXTURE_WORKDIR}/tests:{RELEASE_FIXTURE_WORKDIR}",
        "--entrypoint", "/opt/venv/bin/python", image,
        RETAINED_RUNNER, *tests,
    )
    return subprocess.run(command, check=False).returncode


def _arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare a sealed source snapshot for isolated Release fixtures.")
    parser.add_argument("--image", required=True, help="full immutable local Docker image ID, sha256:<64 lowercase hex>")
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[5])
    parser.add_argument("--snapshot-parent", type=Path, default=Path("/private/tmp"))
    parser.add_argument("--run", action="store_true", help="after snapshot preparation, run selected fixtures in Docker")
    parser.add_argument("--test", action="append", default=[], help="dotted unittest target; repeat for multiple targets")
    options = parser.parse_args(argv)
    if IMAGE_IDENTIFIER.fullmatch(options.image) is None:
        parser.error("--image must be a full sha256:<64 lowercase hex> Docker image ID")
    if options.run and not options.test:
        parser.error("--run requires at least one --test")
    return options


def main(argv: Sequence[str] | None = None) -> int:
    options = _arguments(argv)
    try:
        snapshot = prepare_snapshot(options.project_root, options.snapshot_parent)
        print(_canonical_json({
            "snapshot_path": snapshot.path,
            "source_digest": snapshot.source_digest,
            "records": len(snapshot.records),
            "docker_invoked": options.run,
        }).decode("utf-8"))
        return run_isolated_fixtures(options.image, snapshot, options.test) if options.run else 0
    except FixtureIsolationError as error:
        print(f"isolated-release-fixtures: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
