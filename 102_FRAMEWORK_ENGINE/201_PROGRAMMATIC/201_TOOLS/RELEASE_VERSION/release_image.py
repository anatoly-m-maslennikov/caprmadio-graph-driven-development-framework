"""Bound image phases; never select a runtime or replay an uncertain effect.

The executor is an internal dependency, not a Tool request member. Fake executor
results prove command construction only. Actual image proof requires the Docker
executor and successful immutable-ID inspection and executable canary output.
Retirement observes the separate promotion producer and retains the image
until the sealed Framework Instance Settings retention condition is bound.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import tomllib
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Literal, Protocol

from release_contract import (IMAGE_DOCKERFILE, PROJECT_SKILL_TARGET, CandidateSnapshotManifest,
                              ReleaseContractError, SealedAuthority, ValidatedCandidate, canonical_json)
from release_handoff import (COMPILER_ENTRYPOINT_RELATIVE, CURRENT_SELECTOR_RELATIVE,
                             DERIVED_SOURCE_COPY_RELATIVE, MATERIALIZED_RELATIVE,
                             SealedCandidateCompilation, _file)
from release_packaging import RUNTIME_ROOT, _complete_rows, _render_manifest, _verify_release
from release_suite import (EVIDENCE_ROOT as SUITE_ROOT, SUPPORTED_RUNNER, SuiteGateEvidence,
                           _observe_report, _safe_path, verify_bound_suite_evidence)


IMAGE_ID = re.compile(r"^sha256:[0-9a-f]{64}$")
IMAGE_ROOT = ".caprmedio_runtime/release_image"
CANDIDATE_LABEL = "org.caprmedio.candidate"
CONTEXT_LABEL = "org.caprmedio.context"
MAX_OUTPUT_BYTES = 4 * 1024 * 1024


@dataclass(frozen=True)
class DockerCommandResult:
    exit_code: int | None
    stdout: bytes
    stderr: bytes
    timed_out: bool = False


class DockerExecutor(Protocol):
    def run(self, argv: tuple[str, ...], *, cwd: Path, timeout_seconds: float) -> DockerCommandResult: ...


class DockerSubprocessExecutor:
    """Existing Docker CLI only; no shell, provisioning or socket workaround."""

    def run(self, argv: tuple[str, ...], *, cwd: Path, timeout_seconds: float) -> DockerCommandResult:
        if not argv or argv[0] != "docker" or argv[1] not in {"build", "image", "run", "container"}:
            raise ReleaseContractError("release-image-command-invalid", "unsupported internal Docker operation")
        try:
            result = subprocess.run(argv, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True,
                                    shell=False, timeout=timeout_seconds, check=False)
            return DockerCommandResult(result.returncode, result.stdout, result.stderr)
        except subprocess.TimeoutExpired as error:
            # Killing a CLI does not establish whether its daemon-side effect stopped.
            return DockerCommandResult(None, error.stdout or b"", error.stderr or b"", True)


@dataclass(frozen=True)
class ImageBuildEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["built", "failed", "incomplete", "stale", "effect_uncertain", "recording_uncertain"]
    reason: str
    candidate_image_digest: str | None
    context_root: str
    context_sha256: str
    package_manifest_sha256: str
    suite_receipt_sha256: str
    evidence_root: str
    commands_sha256: str
    execution_kind: Literal["docker-subprocess", "test-double"]
    receipt_sha256: str | None = None


@dataclass(frozen=True)
class ImageVerificationEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["verified", "failed", "incomplete", "stale", "effect_uncertain", "recording_uncertain"]
    reason: str
    candidate_image_digest: str
    build_receipt_sha256: str
    evidence_root: str
    commands_sha256: str
    execution_kind: Literal["docker-subprocess", "test-double"]
    receipt_sha256: str | None = None


@dataclass(frozen=True)
class ImageRetirementEvidence:
    candidate_snapshot_manifest_sha256: str
    outcome: Literal["retained", "pending", "stale", "recording_uncertain"]
    reason: str
    candidate_image_digest: str
    prior_image_digest: str | None
    promotion_receipt_sha256: str
    retaining_container_refs: tuple[str, ...] | None
    observed_rollback_refs: tuple[str, ...] | None
    required_rollback_refs: tuple[str, ...] | None
    evidence_root: str
    commands_sha256: str
    execution_kind: Literal["docker-subprocess", "test-double"]
    receipt_sha256: str | None = None


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree(root: Path) -> str:
    records = []
    if root.is_symlink() or not root.is_dir():
        raise ReleaseContractError("release-image-context-unsafe", "image context root is unsafe")
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not (path.is_dir() or path.is_file()):
            raise ReleaseContractError("release-image-context-unsafe", "image context contains an unsafe carrier")
        if path.is_file():
            records.append((path.relative_to(root).as_posix(), _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    return _digest(canonical_json(records))


def _freeze(root: Path) -> tuple[bytes, str | None]:
    selector = _file(root, CURRENT_SELECTOR_RELATIVE).read_bytes()
    skill = root / PROJECT_SKILL_TARGET
    for ancestor in (root / ".agents", root / ".agents/skills", skill):
        if ancestor.is_symlink():
            raise ReleaseContractError("release-image-selection-unsafe", "public Skill selection contains a symlink")
    return selector, _tree(skill) if skill.exists() else None


def _bound(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation, suite: SuiteGateEvidence) -> Path:
    return verify_bound_suite_evidence(candidate, compilation, suite)


def _post_bound(candidate, compilation, suite, root, frozen):
    _bound(candidate, compilation, suite)
    if _freeze(root) != frozen:
        raise ReleaseContractError("release-image-selection-stale", "executing N or public Skill changed during image phase")


def _attempt(root: Path, candidate_sha: str, phase: str) -> Path:
    parent = _safe_path(root, f"{IMAGE_ROOT}/{candidate_sha}/{phase}", create=True)
    return Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)


def _record(attempt: Path, evidence):
    payload = canonical_json(asdict(evidence))
    try:
        _write(attempt / "receipt.json", payload)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="image receipt recording is uncertain")
    return replace(evidence, receipt_sha256=_digest(payload))


def _command(executor, argv, root, attempt, records, timeout):
    argv = tuple(argv)
    try:
        result = executor.run(argv, cwd=root, timeout_seconds=timeout)
    except OSError as error:
        result = DockerCommandResult(None, b"", type(error).__name__.encode())
    if not isinstance(result, DockerCommandResult) or not isinstance(result.stdout, bytes) or not isinstance(result.stderr, bytes):
        raise ReleaseContractError("release-image-executor-invalid", "executor must return captured byte outputs")
    if len(result.stdout) > MAX_OUTPUT_BYTES or len(result.stderr) > MAX_OUTPUT_BYTES:
        raise ReleaseContractError("release-image-output-incomplete", "captured Docker output is too large")
    index = len(records)
    _write(attempt / f"command-{index}.stdout", result.stdout)
    _write(attempt / f"command-{index}.stderr", result.stderr)
    records.append({"argv": argv, "exit_code": result.exit_code, "timed_out": result.timed_out,
                    "stdout_sha256": _digest(result.stdout), "stderr_sha256": _digest(result.stderr)})
    return result


def _inspect(executor, image, context_sha, candidate_sha, root, attempt, records, timeout):
    result = _command(executor, ("docker", "image", "inspect", image), root, attempt, records, timeout)
    if result.timed_out:
        return False
    if result.exit_code != 0:
        return False
    try:
        inspected = json.loads(result.stdout)
        labels = inspected[0]["Config"]["Labels"]
        return len(inspected) == 1 and inspected[0]["Id"] == image and labels.get(CANDIDATE_LABEL) == candidate_sha and labels.get(CONTEXT_LABEL) == context_sha
    except (ValueError, TypeError, KeyError, IndexError):
        return False


# This producer reads image bytes and executes the image's actual MCP gateway.
# Its output is parsed strictly by verify_candidate_image, never a caller flag.
CANARY = r'''import asyncio, hashlib, json, shutil, sys, tomllib
from pathlib import Path
from mcp import Client, StdioServerParameters
def digest(value):
    return hashlib.sha256(value).hexdigest()
base = Path('/opt/caprmedio-framework')
spec = json.loads(Path('/opt/caprmedio-release-canary.json').read_bytes())
manifest_bytes = (base / 'manifest.toml').read_bytes()
assert digest(manifest_bytes) == spec['package_manifest_sha256']
manifest = tomllib.loads(manifest_bytes.decode())
assert manifest['candidate_snapshot_manifest_sha256'] == spec['candidate_snapshot_manifest_sha256']
rows = spec['package_rows']
assert manifest['files'] == rows
expected = {'manifest.toml'} | {row['destination'] for row in rows}
assert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == expected
for row in rows:
    p = base / row['destination']
    assert p.is_file() and not p.is_symlink()
    assert digest(p.read_bytes()) == row['sha256'] and p.stat().st_mode & 511 == row['mode']
for row in spec['engine_rows']:
    p = Path('/workspace') / row['path']
    assert p.is_file() and not p.is_symlink()
    assert digest(p.read_bytes()) == row['sha256'] and p.stat().st_mode & 511 == row['mode']
engine = Path('/workspace/102_FRAMEWORK_ENGINE')
assert {p.relative_to(Path('/workspace')).as_posix() for p in engine.rglob('*') if p.is_file()} == {row['path'] for row in spec['engine_rows']}
project = Path('/tmp/release-canary-project')
project.mkdir()
source = project / '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
shutil.copytree(base / 'METHODOLOGY/sources', source)
shutil.copytree(base / 'METHODOLOGY/compiled', project / '.caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY')
(project / '.caprmedio_caprmedio/project_structure.toml').write_text('[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\nauthority_path = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"\n')
async def probe():
    params = StdioServerParameters(command=sys.executable, args=['/workspace/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py', '--project-root', str(project)])
    async with Client(params, cache=None) as client:
        page = await client.list_tools()
        names = [tool.name for tool in page.tools]
        while page.next_cursor:
            page = await client.list_tools(cursor=page.next_cursor)
            names.extend(tool.name for tool in page.tools)
        assert names and len(names) == len(set(names))
        result = await client.call_tool('get_mcp_reload_status', {'request': {}})
        assert not result.is_error
        return sorted(names)
names = asyncio.run(asyncio.wait_for(probe(), 60))
print(json.dumps({'schema': 'caprmedio.release_version.image_canary.v1', 'candidate_snapshot_manifest_sha256': spec['candidate_snapshot_manifest_sha256'], 'package_manifest_sha256': digest(manifest_bytes), 'verified_files': len(rows), 'mcp_tools': names}, sort_keys=True))
'''


def _context(root, candidate, compilation, attempt):
    identity, rows, _selector = _complete_rows(root, compilation)
    package = _safe_path(root, (RUNTIME_ROOT / "releases" / identity).as_posix())
    manifest = _render_manifest(identity, rows)
    _verify_release(package, manifest, rows)
    inputs = {row.source_path: row for row in candidate.manifest.source_inventory_rows if row.resource == "IMAGE_INPUT"}
    if not {IMAGE_DOCKERFILE, "pyproject.toml", "uv.lock"} <= inputs.keys():
        raise ReleaseContractError("release-image-input-incomplete", "Dockerfile, pyproject.toml and uv.lock must all be sealed image inputs")
    context = attempt / "context"
    context.mkdir()
    _write(context / "PACKAGE/manifest.toml", manifest.encode())
    engine_rows = []
    for row in rows:
        source = package / row.destination_path
        payload = source.read_bytes()
        if _digest(payload) != row.sha256 or source.stat().st_mode & 0o777 != row.mode:
            raise ReleaseContractError("release-image-package-stale", "package changed while private context was assembled")
        _write(context / "PACKAGE" / row.destination_path, payload, row.mode)
        runtime = None
        if row.resource == "FRAMEWORK_ENGINE":
            runtime = "102_" + row.destination_path
        elif row.resource == "SKILL":
            runtime = "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/" + row.destination_path.removeprefix("SKILLS/ca/")
        if runtime:
            _write(context / runtime, payload, row.mode)
            engine_rows.append({"path": runtime, "sha256": row.sha256, "mode": row.mode})
    for source_relative, row in sorted(inputs.items()):
        source = _file(root, source_relative)
        payload = source.read_bytes()
        if _digest(payload) != row.source_sha256 or source.stat().st_mode & 0o777 != row.source_mode:
            raise ReleaseContractError("release-image-input-stale", "sealed image input changed during context assembly")
        _write(context / source_relative, payload, row.source_mode)
        if source_relative.startswith("102_FRAMEWORK_ENGINE/"):
            engine_rows.append({"path": source_relative, "sha256": row.source_sha256, "mode": row.source_mode})
    pinned = (context / IMAGE_DOCKERFILE).read_bytes()
    if _digest(pinned) != candidate.manifest.candidate_image.dockerfile_sha256:
        raise ReleaseContractError("release-image-dockerfile-stale", "pinned Dockerfile digest differs")
    _write(context / "Dockerfile", pinned + b"\nCOPY PACKAGE /opt/caprmedio-framework\nCOPY canary.py /opt/caprmedio-release-canary.py\nCOPY canary.json /opt/caprmedio-release-canary.json\n")
    _write(context / "canary.py", CANARY.encode())
    package_rows = [{"resource": row.resource, "source_path": row.source_path, "destination": row.destination_path,
                     "sha256": row.sha256, "mode": row.mode} for row in rows]
    _write(context / "canary.json", canonical_json({"candidate_snapshot_manifest_sha256": identity,
           "package_manifest_sha256": _digest(manifest.encode()), "package_rows": package_rows, "engine_rows": engine_rows}))
    return context, _digest(manifest.encode())


def build_candidate_image(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                          suite: SuiteGateEvidence, *, executor: DockerExecutor, timeout_seconds: float = 900) -> ImageBuildEvidence:
    """One admitted build attempt, retaining its exact context and output evidence."""
    if isinstance(timeout_seconds, bool) or not 0 < timeout_seconds <= 900:
        raise ReleaseContractError("release-image-timeout-invalid", "image timeout must be within (0, 900]")
    root = _bound(candidate, compilation, suite)
    frozen = _freeze(root)
    attempt = _attempt(root, candidate.manifest.sha256, "build")
    context, package_sha = _context(root, candidate, compilation, attempt)
    context_sha = _tree(context)
    records = []
    image, outcome, reason = None, "incomplete", "immutable image identity is unverified"
    try:
        _post_bound(candidate, compilation, suite, root, frozen)
        result = _command(executor, ("docker", "build", "--iidfile", str(attempt / "image.id"),
                          "--label", f"{CANDIDATE_LABEL}={candidate.manifest.sha256}",
                          "--label", f"{CONTEXT_LABEL}={context_sha}", "--file", str(context / "Dockerfile"), str(context)),
                          root, attempt, records, timeout_seconds)
        if result.timed_out:
            outcome, reason = "effect_uncertain", "Docker CLI timed out; build effect must not be replayed"
        elif result.exit_code != 0:
            outcome, reason = "failed", "candidate image build failed"
        else:
            iid = attempt / "image.id"
            value = iid.read_text().strip() if iid.is_file() and not iid.is_symlink() else ""
            if IMAGE_ID.fullmatch(value):
                image = value
                if _inspect(executor, image, context_sha, candidate.manifest.sha256, root, attempt, records, timeout_seconds):
                    outcome, reason = "built", "bound immutable image built; executable verification is still required"
        _post_bound(candidate, compilation, suite, root, frozen)
        if _tree(context) != context_sha:
            raise ReleaseContractError("release-image-context-stale", "private build context changed during execution")
    except (ValueError, OSError, RuntimeError) as error:
        outcome, reason = "stale" if isinstance(error, ReleaseContractError) and "stale" in error.code else "recording_uncertain", str(error)
    commands = canonical_json(records)
    try:
        _write(attempt / "commands.json", commands)
    except OSError:
        outcome, reason = "recording_uncertain", "captured image command recording is uncertain"
    evidence = ImageBuildEvidence(candidate.manifest.sha256, outcome, reason, image,
               context.relative_to(root).as_posix(), context_sha, package_sha, suite.receipt_sha256,
               attempt.relative_to(root).as_posix(), _digest(commands),
               "docker-subprocess" if type(executor) is DockerSubprocessExecutor else "test-double")
    return _record(attempt, evidence)


def _verify_build_artifacts(root, candidate, compilation, suite, build):
    if not isinstance(build, ImageBuildEvidence) or build.outcome != "built" or not build.receipt_sha256 or not IMAGE_ID.fullmatch(build.candidate_image_digest or ""):
        raise ReleaseContractError("release-image-build-untrusted", "verification requires a recorded immutable build")
    if build.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256 or build.suite_receipt_sha256 != suite.receipt_sha256:
        raise ReleaseContractError("release-image-build-mismatch", "build belongs to another candidate or suite")
    prefix = f"{IMAGE_ROOT}/{candidate.manifest.sha256}/build/"
    if (not build.evidence_root.startswith(prefix) or not build.evidence_root.removeprefix(prefix).startswith("attempt-")
        or "/" in build.evidence_root.removeprefix(prefix) or build.context_root != f"{build.evidence_root}/context"):
        raise ReleaseContractError("release-image-build-path-invalid", "build carrier is outside the fixed attempt root")
    attempt = _safe_path(root, build.evidence_root)
    receipt = _file(root, f"{build.evidence_root}/receipt.json").read_bytes()
    if _digest(receipt) != build.receipt_sha256 or receipt != canonical_json(asdict(replace(build, receipt_sha256=None))):
        raise ReleaseContractError("release-image-build-untrusted", "build receipt does not match retained evidence")
    commands = _file(root, f"{build.evidence_root}/commands.json").read_bytes()
    if _digest(commands) != build.commands_sha256:
        raise ReleaseContractError("release-image-build-untrusted", "build command evidence changed")
    parsed = json.loads(commands)
    context = _safe_path(root, build.context_root)
    expected_build = ["docker", "build", "--iidfile", str(attempt / "image.id"),
                      "--label", f"{CANDIDATE_LABEL}={candidate.manifest.sha256}",
                      "--label", f"{CONTEXT_LABEL}={build.context_sha256}",
                      "--file", str(context / "Dockerfile"), str(context)]
    if (not isinstance(parsed, list) or len(parsed) != 2
        or parsed[0].get("argv") != expected_build
        or parsed[1].get("argv") != ["docker", "image", "inspect", build.candidate_image_digest]
        or any(type(command.get("exit_code")) is not int or command["exit_code"] != 0 or command.get("timed_out") is not False for command in parsed)):
        raise ReleaseContractError("release-image-build-untrusted", "build did not execute the exact private-context build and immutable inspection")
    if _file(root, f"{build.evidence_root}/image.id").read_text().strip() != build.candidate_image_digest:
        raise ReleaseContractError("release-image-build-untrusted", "retained build image identity changed")
    for index, command in enumerate(parsed):
        for stream in ("stdout", "stderr"):
            if _digest(_file(root, f"{build.evidence_root}/command-{index}.{stream}").read_bytes()) != command[f"{stream}_sha256"]:
                raise ReleaseContractError("release-image-build-untrusted", "build captured output changed")
    if _tree(context) != build.context_sha256:
        raise ReleaseContractError("release-image-context-stale", "private build context no longer matches")
    inspected = json.loads(_file(root, f"{build.evidence_root}/command-1.stdout").read_bytes())
    try:
        labels = inspected[0]["Config"]["Labels"]
        valid_inspect = (len(inspected) == 1 and inspected[0]["Id"] == build.candidate_image_digest
                         and labels.get(CANDIDATE_LABEL) == candidate.manifest.sha256
                         and labels.get(CONTEXT_LABEL) == build.context_sha256)
    except (TypeError, KeyError, IndexError, AttributeError):
        valid_inspect = False
    if not valid_inspect:
        raise ReleaseContractError("release-image-build-untrusted", "retained build inspection differs from the exact immutable image")
    identity, rows = compilation.candidate_snapshot_manifest_sha256, list(compilation.package_rows)
    manifest = _render_manifest(identity, rows)
    if build.package_manifest_sha256 != _digest(manifest.encode()):
        raise ReleaseContractError("release-image-build-untrusted", "build package identity differs from the complete current package")
    _verify_release(context / "PACKAGE", manifest, rows)
    expected_paths = {"PACKAGE/manifest.toml", "Dockerfile", "canary.py", "canary.json"}
    engine_rows = []
    for row in rows:
        expected_paths.add("PACKAGE/" + row.destination_path)
        runtime = None
        if row.resource == "FRAMEWORK_ENGINE":
            runtime = "102_" + row.destination_path
        elif row.resource == "SKILL":
            runtime = "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/" + row.destination_path.removeprefix("SKILLS/ca/")
        if runtime:
            expected_paths.add(runtime)
            engine_rows.append({"path": runtime, "sha256": row.sha256, "mode": row.mode})
            path = context / runtime
            if _digest(path.read_bytes()) != row.sha256 or path.stat().st_mode & 0o777 != row.mode:
                raise ReleaseContractError("release-image-context-stale", "private Engine bytes differ from the complete package")
    for row in sorted((row for row in candidate.manifest.source_inventory_rows if row.resource == "IMAGE_INPUT"), key=lambda row: row.source_path):
        expected_paths.add(row.source_path)
        path = context / row.source_path
        if _digest(path.read_bytes()) != row.source_sha256 or path.stat().st_mode & 0o777 != row.source_mode:
            raise ReleaseContractError("release-image-context-stale", "private image input differs from its sealed source")
        if row.source_path.startswith("102_FRAMEWORK_ENGINE/"):
            engine_rows.append({"path": row.source_path, "sha256": row.source_sha256, "mode": row.source_mode})
    spec = {"candidate_snapshot_manifest_sha256": identity, "package_manifest_sha256": _digest(manifest.encode()),
            "package_rows": [{"resource": row.resource, "source_path": row.source_path, "destination": row.destination_path,
                              "sha256": row.sha256, "mode": row.mode} for row in rows], "engine_rows": engine_rows}
    dockerfile = (context / IMAGE_DOCKERFILE).read_bytes() + b"\nCOPY PACKAGE /opt/caprmedio-framework\nCOPY canary.py /opt/caprmedio-release-canary.py\nCOPY canary.json /opt/caprmedio-release-canary.json\n"
    if ((context / "canary.py").read_bytes() != CANARY.encode()
        or (context / "canary.json").read_bytes() != canonical_json(spec)
        or (context / "Dockerfile").read_bytes() != dockerfile
        or {path.relative_to(context).as_posix() for path in context.rglob("*") if path.is_file()} != expected_paths):
        raise ReleaseContractError("release-image-context-stale", "private context or fixed canary producer changed")
    return attempt


def _verify_build(root, candidate, compilation, suite, build):
    _complete_rows(root, compilation)
    return _verify_build_artifacts(root, candidate, compilation, suite, build)


def _read_suite_artifacts(root, candidate, compilation, suite):
    """Observe the original execution artifacts without consulting a selector."""
    if not isinstance(suite, SuiteGateEvidence) or not suite.passed:
        raise ReleaseContractError("release-image-suite-untrusted", "image artifacts require a successful recorded suite")
    environment = candidate.manifest.full_suite_environment
    prefix = f"{SUITE_ROOT}/{candidate.manifest.sha256}/"
    suffix = suite.evidence_root.removeprefix(prefix)
    if (suite.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or suite.runner != environment.runner or suite.runner != SUPPORTED_RUNNER
        or suite.command != tuple(environment.command) or suite.working_directory != environment.working_directory
        or type(suite.exit_code) is not int or suite.exit_code != 0
        or not suite.evidence_root.startswith(prefix) or not suffix.startswith("attempt-") or "/" in suffix):
        raise ReleaseContractError("release-image-suite-untrusted", "suite artifacts differ from the exact sealed invocation")
    attempt = _safe_path(root, suite.evidence_root)
    for name, expected in (("receipt.json", suite.receipt_sha256), ("stdout.bin", suite.stdout_sha256),
                           ("stderr.bin", suite.stderr_sha256), ("coverage.xml", suite.report_sha256)):
        payload = _file(root, f"{suite.evidence_root}/{name}").read_bytes()
        if _digest(payload) != expected or (name == "receipt.json" and payload != canonical_json(asdict(replace(suite, receipt_sha256=None)))):
            raise ReleaseContractError("release-image-suite-untrusted", "original suite receipt or captured output changed")
    tests, coverage, reason = _observe_report(attempt / "coverage.xml", compilation)
    if reason or tests != suite.executed_tests or coverage != suite.coverage:
        raise ReleaseContractError("release-image-suite-untrusted", "original suite report no longer establishes complete successful coverage")


def _artifact_inputs(candidate, compilation):
    if not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedCandidateCompilation):
        raise ReleaseContractError("release-image-handoff-untrusted", "artifact reader requires internal typed candidate and compilation")
    try:
        manifest = CandidateSnapshotManifest.model_validate(candidate.manifest.model_dump(mode="json", by_alias=True))
        authority = SealedAuthority.model_validate(candidate.authority.model_dump(mode="json"))
        sealed = SealedCandidateCompilation.model_validate(compilation.model_dump(mode="json"))
    except (ValueError, AttributeError) as error:
        raise ReleaseContractError("release-image-handoff-untrusted", "artifact inputs fail canonical typed validation") from error
    if (authority != sealed.authority or authority.expected_candidate_snapshot_manifest_sha256 != manifest.sha256
        or any(getattr(authority, field) != getattr(manifest, field) for field in (
            "executing_release", "candidate_release", "canonical_source_snapshot_digest", "project_structure_digest",
            "framework_settings_digest", "source_frontier_digest", "nested_source_recursive_sha256_before"))
        or sealed.candidate_snapshot_manifest_sha256 != manifest.sha256
        or sealed.expected_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or sealed.actual_derived_source_copy_sha256 != manifest.expected_derived_source_copy_sha256
        or sealed.expected_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or sealed.actual_compiled_output_sha256 != manifest.expected_compiled_output_sha256
        or sealed.compiler_frontier_digest != manifest.source_frontier_digest
        or sealed.compiler_entrypoint.path != COMPILER_ENTRYPOINT_RELATIVE
        or sealed.source_copy_root != DERIVED_SOURCE_COPY_RELATIVE
        or sealed.child_materialization_root != f"{MATERIALIZED_RELATIVE}/{manifest.sha256}"
        or list(sealed.package_rows) != sorted(sealed.package_rows, key=lambda row: (row.destination_path, row.source_path, row.sha256))):
        raise ReleaseContractError("release-image-handoff-untrusted", "artifact inputs identify mismatching sealed candidate facts")
    root = Path(candidate.project_root).resolve()
    if not root.is_dir():
        raise ReleaseContractError("release-image-project-missing", "artifact Project root is missing")
    return root


def verify_candidate_image(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                           suite: SuiteGateEvidence, build: ImageBuildEvidence, *, executor: DockerExecutor,
                           timeout_seconds: float = 120) -> ImageVerificationEvidence:
    """Inspect exact ID and execute fixed complete-package/MCP canary in isolation."""
    if isinstance(timeout_seconds, bool) or not 0 < timeout_seconds <= 120:
        raise ReleaseContractError("release-image-timeout-invalid", "canary timeout must be within (0, 120]")
    root = _bound(candidate, compilation, suite)
    _verify_build(root, candidate, compilation, suite, build)
    frozen = _freeze(root)
    attempt = _attempt(root, candidate.manifest.sha256, "verify")
    records = []
    outcome, reason = "incomplete", "candidate image canary evidence is incomplete"
    try:
        if _inspect(executor, build.candidate_image_digest, build.context_sha256, candidate.manifest.sha256,
                    root, attempt, records, timeout_seconds):
            result = _command(executor, ("docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                    "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
                    "--entrypoint", "python", build.candidate_image_digest, "/opt/caprmedio-release-canary.py"),
                    root, attempt, records, timeout_seconds)
            if result.timed_out:
                outcome, reason = "effect_uncertain", "Docker CLI timed out; canary cleanup/effect is uncertain"
            elif result.exit_code != 0:
                outcome, reason = "failed", "actual candidate-image canary failed"
            else:
                try:
                    report = json.loads(result.stdout)
                    exact = {"schema", "candidate_snapshot_manifest_sha256", "package_manifest_sha256", "verified_files", "mcp_tools"}
                    tools = report.get("mcp_tools")
                    if (set(report) == exact and report["schema"] == "caprmedio.release_version.image_canary.v1"
                        and report["candidate_snapshot_manifest_sha256"] == candidate.manifest.sha256
                        and report["package_manifest_sha256"] == build.package_manifest_sha256
                        and type(report["verified_files"]) is int and report["verified_files"] == len(compilation.package_rows)
                        and isinstance(tools, list) and tools and all(isinstance(tool, str) and tool for tool in tools)
                        and len(tools) == len(set(tools)) and "get_mcp_reload_status" in tools):
                        outcome, reason = "verified", "complete bound package and executable MCP canary observed"
                except (ValueError, TypeError, AttributeError):
                    pass
        _post_bound(candidate, compilation, suite, root, frozen)
        _verify_build(root, candidate, compilation, suite, build)
    except (ValueError, OSError, RuntimeError) as error:
        outcome, reason = "stale" if isinstance(error, ReleaseContractError) and "stale" in error.code else "recording_uncertain", str(error)
    commands = canonical_json(records)
    try:
        _write(attempt / "commands.json", commands)
    except OSError:
        outcome, reason = "recording_uncertain", "canary output recording is uncertain"
    evidence = ImageVerificationEvidence(candidate.manifest.sha256, outcome, reason, build.candidate_image_digest,
               build.receipt_sha256, attempt.relative_to(root).as_posix(), _digest(commands),
               "docker-subprocess" if type(executor) is DockerSubprocessExecutor else "test-double")
    return _record(attempt, evidence)


def verify_bound_image_evidence(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                                suite: SuiteGateEvidence, build: ImageBuildEvidence,
                                evidence: ImageVerificationEvidence) -> Path:
    """Reopen actual Docker evidence for the future promotion producer.

    A test double cannot create promotion evidence. This reader has no Docker
    effect and requires current sealed N before the separate promotion effect.
    """
    _bound(candidate, compilation, suite)
    return read_image_execution_artifacts(candidate, compilation, suite, build, evidence)


def read_image_execution_artifacts(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                                   suite: SuiteGateEvidence, build: ImageBuildEvidence,
                                   evidence: ImageVerificationEvidence) -> Path:
    """Read exact original execution artifacts independently of active selection.

    This is not effect admission, current source/package proof, or promotion
    authority. After selection changes, the promotion consumer must separately
    validate its admitted intent, current source/package, selector and Skill.
    This reader has no selector override flag, Docker effect or promotion import.
    """
    root = _artifact_inputs(candidate, compilation)
    if not isinstance(build, ImageBuildEvidence):
        raise ReleaseContractError("release-image-build-untrusted", "image artifacts require typed recorded build evidence")
    if (not isinstance(evidence, ImageVerificationEvidence) or evidence.outcome != "verified"
        or build.execution_kind != "docker-subprocess" or evidence.execution_kind != "docker-subprocess"
        or not evidence.receipt_sha256):
        raise ReleaseContractError("release-image-evidence-untrusted", "promotion requires recorded actual Docker execution, never a test double")
    _read_suite_artifacts(root, candidate, compilation, suite)
    try:
        _verify_build_artifacts(root, candidate, compilation, suite, build)
    except (ValueError, TypeError, KeyError, AttributeError, IndexError, OSError) as error:
        if isinstance(error, ReleaseContractError):
            raise
        raise ReleaseContractError("release-image-build-untrusted", "retained build artifacts are malformed or missing") from error
    if (evidence.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or evidence.build_receipt_sha256 != build.receipt_sha256
        or evidence.candidate_image_digest != build.candidate_image_digest):
        raise ReleaseContractError("release-image-evidence-mismatch", "image verification belongs to a different bound build")
    prefix = f"{IMAGE_ROOT}/{candidate.manifest.sha256}/verify/"
    if (not evidence.evidence_root.startswith(prefix) or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
        or "/" in evidence.evidence_root.removeprefix(prefix)):
        raise ReleaseContractError("release-image-evidence-path-invalid", "verification carrier is outside the fixed attempt root")
    attempt = _safe_path(root, evidence.evidence_root)
    receipt = _file(root, f"{evidence.evidence_root}/receipt.json").read_bytes()
    if _digest(receipt) != evidence.receipt_sha256 or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None))):
        raise ReleaseContractError("release-image-evidence-untrusted", "verification receipt changed or is caller-forged")
    payload = _file(root, f"{evidence.evidence_root}/commands.json").read_bytes()
    if _digest(payload) != evidence.commands_sha256:
        raise ReleaseContractError("release-image-evidence-untrusted", "verification command recording changed")
    commands = json.loads(payload)
    expected_run = ["docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                    "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
                    "--entrypoint", "python", build.candidate_image_digest, "/opt/caprmedio-release-canary.py"]
    if (len(commands) != 2 or commands[0]["argv"] != ["docker", "image", "inspect", build.candidate_image_digest]
        or commands[1]["argv"] != expected_run
        or any(type(command["exit_code"]) is not int or command["exit_code"] != 0 or command["timed_out"] is not False for command in commands)):
        raise ReleaseContractError("release-image-evidence-untrusted", "verification did not execute the exact immutable-ID canary")
    captured = []
    for index, command in enumerate(commands):
        for stream in ("stdout", "stderr"):
            output = _file(root, f"{evidence.evidence_root}/command-{index}.{stream}").read_bytes()
            if _digest(output) != command[f"{stream}_sha256"]:
                raise ReleaseContractError("release-image-evidence-untrusted", "recorded verification output changed")
            if stream == "stdout":
                captured.append(json.loads(output))
    inspected, report = captured
    try:
        labels = inspected[0]["Config"]["Labels"]
        valid_inspect = (len(inspected) == 1 and inspected[0]["Id"] == build.candidate_image_digest
                         and labels.get(CANDIDATE_LABEL) == candidate.manifest.sha256
                         and labels.get(CONTEXT_LABEL) == build.context_sha256)
        tools = report["mcp_tools"]
        valid_canary = (set(report) == {"schema", "candidate_snapshot_manifest_sha256", "package_manifest_sha256", "verified_files", "mcp_tools"}
                        and report["schema"] == "caprmedio.release_version.image_canary.v1"
                        and report["candidate_snapshot_manifest_sha256"] == candidate.manifest.sha256
                        and report["package_manifest_sha256"] == build.package_manifest_sha256
                        and type(report["verified_files"]) is int and report["verified_files"] == len(compilation.package_rows)
                        and isinstance(tools, list) and tools and all(isinstance(tool, str) and tool for tool in tools)
                        and len(tools) == len(set(tools)) and "get_mcp_reload_status" in tools)
    except (TypeError, KeyError, IndexError):
        valid_inspect = valid_canary = False
    if not valid_inspect or not valid_canary:
        raise ReleaseContractError("release-image-evidence-untrusted", "actual image inspection or canary is incomplete")
    return attempt


def _observed_rollback_references(root: Path, prior_image: str) -> tuple[str, ...]:
    """Read retained selector references without asserting required retention.

    Historical presence neither proves required retention nor approved expiry.
    The approved condition must classify these observations through already
    sealed Framework Instance Settings; that binding is not implemented here.
    """
    from release_promotion import PROMOTION_ROOT

    paths = [CURRENT_SELECTOR_RELATIVE]
    parent = _safe_path(root, PROMOTION_ROOT)
    for directory in sorted(parent.iterdir()):
        if directory.is_symlink() or not directory.is_dir():
            raise ReleaseContractError("release-image-rollback-unknown", "promotion retention scope contains an unsafe carrier")
        selector = directory / "prior-selector.toml"
        if selector.is_symlink() or not selector.is_file():
            raise ReleaseContractError("release-image-rollback-unknown", "promotion retention scope has an unobserved prior selector")
        paths.append(selector.relative_to(root).as_posix())
    references = []
    for relative in paths:
        try:
            parsed = tomllib.loads(_file(root, relative).read_text())
            images = {mapping[key] for mapping in (parsed, parsed.get("selection", {})) if isinstance(mapping, dict)
                      for key in ("candidate_image_digest", "image_digest") if isinstance(mapping.get(key), str)}
        except (OSError, ValueError) as error:
            raise ReleaseContractError("release-image-rollback-unknown", "rollback selector evidence cannot be safely observed") from error
        if prior_image in images:
            references.append(relative)
    return tuple(sorted(references))


def _retaining_containers(executor, prior_image, root, attempt, records, timeout) -> tuple[str, ...]:
    """Observe every stopped/running container, matching immutable Image only."""
    result = _command(executor, ("docker", "container", "ls", "--all", "--quiet", "--no-trunc"),
                      root, attempt, records, timeout)
    if result.timed_out or type(result.exit_code) is not int or result.exit_code != 0:
        raise ReleaseContractError("release-image-containers-unknown", "all-container listing is unavailable or incomplete")
    try:
        identifiers = result.stdout.decode("ascii").splitlines()
    except UnicodeDecodeError as error:
        raise ReleaseContractError("release-image-containers-unknown", "container listing has unsupported identifiers") from error
    if (len(identifiers) != len(set(identifiers)) or len(identifiers) > 10000
        or any(re.fullmatch(r"[0-9a-f]{64}", value) is None for value in identifiers)):
        raise ReleaseContractError("release-image-containers-unknown", "container listing has unsafe or partial identifiers")
    if not identifiers:
        return ()
    result = _command(executor, ("docker", "container", "inspect", *sorted(identifiers)),
                      root, attempt, records, timeout)
    if result.timed_out or type(result.exit_code) is not int or result.exit_code != 0:
        raise ReleaseContractError("release-image-containers-unknown", "some listed containers could not be inspected")
    try:
        inspected = json.loads(result.stdout)
        if (not isinstance(inspected, list) or len(inspected) != len(identifiers)
            or {item["Id"] for item in inspected} != set(identifiers)
            or any(not IMAGE_ID.fullmatch(item["Image"]) or not isinstance(item["State"]["Status"], str)
                   or not item["State"]["Status"] for item in inspected)):
            raise ValueError("partial container inspection")
        return tuple(sorted(item["Id"] for item in inspected if item["Image"] == prior_image))
    except (ValueError, TypeError, KeyError, AttributeError) as error:
        raise ReleaseContractError("release-image-containers-unknown", "container inspections have incomplete immutable image bindings") from error


def retire_prior_image(candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                       suite: SuiteGateEvidence, build: ImageBuildEvidence,
                       verification: ImageVerificationEvidence, promotion, *, executor: DockerExecutor,
                       timeout_seconds: float = 120) -> ImageRetirementEvidence:
    """Observe exact prior-image retirement safety after verified promotion.

    There are no caller image overrides or retention-success flags. The exact
    identity comes from the promotion's observed retained N selector. Missing,
    mismatched or unavailable proof yields pending; container use yields retained.
    O169 requires an approved rollback-retention condition. Until that condition
    is bound to the already sealed Framework Instance Settings, required rollback
    references remain unknown (None), even if historical selectors are observed.
    No image removal is admitted by this frontier. A future exact removal must
    consume the condition producer and use only ``docker image rm <prior-id>``.
    """
    from release_promotion import verify_bound_promotion_evidence

    if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float)) or not 0 < timeout_seconds <= 120:
        raise ReleaseContractError("release-image-timeout-invalid", "retirement timeout must be within (0, 120]")
    root = verify_bound_promotion_evidence(candidate, compilation, suite, build, verification, promotion)
    frozen = _freeze(root)
    attempt = _attempt(root, candidate.manifest.sha256, "retire")
    prior_image = promotion.prior_image_digest
    records, containers, rollback = [], None, None
    outcome, reason = "pending", "exact prior image is unknown; no alternate image is inferred"
    try:
        if prior_image is not None:
            if not IMAGE_ID.fullmatch(prior_image) or prior_image == promotion.candidate_image_digest:
                raise ReleaseContractError("release-image-prior-unknown", "prior identity is invalid or still selected as N+1")
            rollback = _observed_rollback_references(root, prior_image)
            result = _command(executor, ("docker", "image", "inspect", prior_image), root, attempt, records, timeout_seconds)
            if result.timed_out or type(result.exit_code) is not int or result.exit_code != 0:
                reason = "exact prior image is missing, unavailable or permission-denied; retained without another target"
            else:
                try:
                    inspected = json.loads(result.stdout)
                    matches = isinstance(inspected, list) and len(inspected) == 1 and inspected[0]["Id"] == prior_image
                except (ValueError, TypeError, KeyError, IndexError):
                    matches = False
                if not matches:
                    reason = "image inspection does not prove the exact prior immutable identity"
                else:
                    containers = _retaining_containers(executor, prior_image, root, attempt, records, timeout_seconds)
                    if containers:
                        outcome, reason = "retained", "exact prior image is retained by an observed running or stopped container"
                    else:
                        # Observed selectors alone cannot classify required use:
                        # the sealed settings retention binding is still absent.
                        reason = "approved rollback-retention condition is unavailable; required references are unknown and removal remains pending"
        verify_bound_promotion_evidence(candidate, compilation, suite, build, verification, promotion)
        if _freeze(root) != frozen:
            raise ReleaseContractError("release-image-retirement-stale", "selected N+1 or public Skill changed during retirement observation")
    except (ValueError, OSError, RuntimeError) as error:
        code = getattr(error, "code", "")
        outcome = "stale" if any(part in code for part in ("stale", "currentness", "selection")) else "pending"
        reason = f"retirement safety is unproven: {code or type(error).__name__}"
    commands = canonical_json(records)
    try:
        _write(attempt / "commands.json", commands)
    except OSError:
        outcome, reason = "recording_uncertain", "retirement observation recording is uncertain"
    evidence = ImageRetirementEvidence(candidate.manifest.sha256, outcome, reason, promotion.candidate_image_digest,
               prior_image, promotion.receipt_sha256, containers, rollback, None, attempt.relative_to(root).as_posix(),
               _digest(commands), "docker-subprocess" if type(executor) is DockerSubprocessExecutor else "test-double")
    return _record(attempt, evidence)


__all__ = ["DockerCommandResult", "DockerExecutor", "DockerSubprocessExecutor", "ImageBuildEvidence",
           "ImageVerificationEvidence", "ImageRetirementEvidence", "build_candidate_image", "verify_candidate_image", "verify_bound_image_evidence",
           "read_image_execution_artifacts", "retire_prior_image"]
