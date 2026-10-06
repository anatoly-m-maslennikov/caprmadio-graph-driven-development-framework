"""Private first-N Framework image production and proof reopening.

This carrier is intentionally separate from :mod:`release_image`: the latter
requires an existing selected N and a Release Version candidate.  Bootstrap
has neither.  It may retain a sealed build context and Docker observations,
but it never publishes a runtime package, project Skill, or selector.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import time
import tomllib
from datetime import datetime, timezone
from dataclasses import asdict, dataclass, replace
from pathlib import Path, PurePosixPath
from typing import Literal, Protocol

from release_contract import IMAGE_DOCKERFILE, ReleaseContractError, canonical_json
from release_contract import REQUIRED_ENGINE_SOURCE_PREFIXES
from release_handoff import PackageRow
from release_image import DockerCommandResult, DockerExecutor, DockerSubprocessExecutor, IMAGE_ID
from release_inventory import ReleaseInventoryError, refuse_secret_path
from release_packaging import REQUIRED_SKILL_FILES, RUNTIME_ROOT, ReleasePackagingError, _render_manifest, _verify_release


BOOTSTRAP_IMAGE_RELATIVE = Path(".caprmedio_runtime/framework/bootstrap-image-evidence")
PACKAGE_IMAGE_LABEL = "org.caprmedio.framework.package_manifest_sha256"
SOURCE_CONTEXT_IMAGE_LABEL = "org.caprmedio.framework.source_context_sha256"
_DEPENDENCY_INPUTS = (IMAGE_DOCKERFILE, "pyproject.toml", "uv.lock")
_ENGINE_COPY = b"COPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_MAX_OUTPUT_BYTES = 4 * 1024 * 1024


class BootstrapImageError(ReleaseContractError):
    """A first-N image build or its retained proof is unavailable."""


@dataclass(frozen=True)
class BootstrapImageEvidence:
    """The sole private image-proof carrier accepted by the initializer."""

    manifest_sha256: str
    source_context_sha256: str
    outcome: Literal["verified", "failed", "incomplete", "stale", "effect_uncertain", "recording_uncertain"]
    reason: str
    image_digest: str | None
    context_sha256: str
    evidence_root: str
    commands_sha256: str
    execution_kind: Literal["docker-subprocess", "test-double"]
    started_at: str
    finished_at: str
    bootstrap_proof_key: str = ""
    proof_root: str = ""
    context_root: str = ""
    receipt_sha256: str | None = None

    @property
    def package_manifest_sha256(self) -> str:
        """Compatibility spelling for the initializer's package identity."""
        return self.manifest_sha256


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _error(code: str, message: str) -> BootstrapImageError:
    return BootstrapImageError(code, message)


def _root(plan: object) -> Path:
    value = getattr(plan, "root", None)
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise _error("bootstrap-image-plan-invalid", "initial package plan has no regular Project root") from error
    if root.is_symlink() or not root.is_dir():
        raise _error("bootstrap-image-plan-invalid", "initial package plan root is unsafe")
    return root


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise _error("bootstrap-image-plan-invalid", f"initial package plan {label} is invalid")
    return value


def _relative(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise _error("bootstrap-image-plan-invalid", f"{label} must be a normalized relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value or any(part in {"", ".", ".."} for part in path.parts):
        raise _error("bootstrap-image-plan-invalid", f"{label} must be a normalized relative path")
    return value


def _plan(plan: object) -> tuple[Path, tuple[object, ...], str, str, bytes]:
    root = _root(plan)
    rows = getattr(plan, "rows", None)
    manifest_sha256 = _sha(getattr(plan, "manifest_sha256", None), "manifest digest")
    source_context_sha256 = _sha(getattr(plan, "source_context_sha256", None), "source-context digest")
    manifest_bytes = getattr(plan, "manifest_bytes", None)
    if not isinstance(rows, tuple) or not rows or not isinstance(manifest_bytes, bytes):
        raise _error("bootstrap-image-plan-invalid", "initial package plan is incomplete")
    if _digest(manifest_bytes) != manifest_sha256:
        raise _error("bootstrap-image-plan-invalid", "initial package manifest bytes differ from its digest")
    destinations: set[str] = set()
    for row in rows:
        source = _relative(getattr(row, "source_path", None), "plan source path")
        destination = _relative(getattr(row, "destination_path", None), "plan destination path")
        _sha(getattr(row, "sha256", None), "row digest")
        mode = getattr(row, "mode", None)
        if type(mode) is not int or not 0 <= mode <= 0o777 or source in destinations or destination in destinations:
            raise _error("bootstrap-image-plan-invalid", "initial package rows are malformed or duplicate")
        destinations.add(source)
        destinations.add(destination)
    return root, rows, manifest_sha256, source_context_sha256, manifest_bytes


def _safe_file(root: Path, relative: str, *, code: str) -> Path:
    try:
        refuse_secret_path(relative)
    except ReleaseInventoryError as error:
        raise _error(error.code, str(error)) from error
    path = root.joinpath(*PurePosixPath(relative).parts)
    cursor = root
    for part in PurePosixPath(relative).parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise _error("bootstrap-image-path-unsafe", f"input path is symlinked: {relative}")
    if path.is_symlink() or not path.is_file():
        raise _error(code, f"required regular input is absent: {relative}")
    try:
        path.resolve(strict=True).relative_to(root)
    except ValueError as error:
        raise _error("bootstrap-image-path-unsafe", f"input path escapes Project: {relative}") from error
    return path


def _read_exact(root: Path, relative: str, sha256: str, mode: int, *, code: str) -> bytes:
    path = _safe_file(root, relative, code=code)
    payload = path.read_bytes()
    if _digest(payload) != sha256 or path.stat().st_mode & 0o777 != mode:
        raise _error(code, f"sealed input changed: {relative}")
    return payload


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)


def _write_or_verify(path: Path, payload: bytes, mode: int) -> None:
    """Permit only an identical overlap between the package and Docker roots."""
    if path.exists():
        if (path.is_symlink() or not path.is_file() or path.read_bytes() != payload
                or path.stat().st_mode & 0o777 != mode):
            raise _error("bootstrap-image-context-invalid", "sealed image-context paths conflict")
        return
    _write(path, payload, mode)


def _tree_digest(root: Path) -> str:
    records: list[tuple[str, str, int]] = []
    if root.is_symlink() or not root.is_dir():
        raise _error("bootstrap-image-context-invalid", "private image context is unsafe")
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not (path.is_file() or path.is_dir()):
            raise _error("bootstrap-image-context-invalid", "private image context contains an unsafe carrier")
        if path.is_file():
            records.append((path.relative_to(root).as_posix(), _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    return _digest(canonical_json(records))


def _input_rows(root: Path) -> tuple[tuple[str, bytes, int], ...]:
    rows: list[tuple[str, bytes, int]] = []
    for relative in _DEPENDENCY_INPUTS:
        path = _safe_file(root, relative, code="bootstrap-image-input-missing")
        payload = path.read_bytes()
        rows.append((relative, payload, path.stat().st_mode & 0o777))
    if _ENGINE_COPY not in rows[0][1]:
        raise _error("bootstrap-image-input-invalid", "fixed Dockerfile does not copy the sealed Engine mirror")
    # The three paths are a closed source contract even when a deliberately
    # minimal fixed Dockerfile does not consume the dependency pair yet.
    # They remain copied and sealed in the private context, never discovered
    # from a caller-controlled Dockerfile instruction.
    return tuple(rows)


def _assert_plan_current(plan: object) -> None:
    root, rows, manifest_sha256, _source_context, manifest_bytes = _plan(plan)
    for row in rows:
        _read_exact(root, row.source_path, row.sha256, row.mode, code="bootstrap-image-source-stale")
    # The two values are repeated deliberately: this makes an altered frozen
    # plan fail before Docker receives any context path.
    if _digest(manifest_bytes) != manifest_sha256:
        raise _error("bootstrap-image-source-stale", "initial package manifest changed")
    _input_rows(root)


def _canary() -> bytes:
    """Fixed complete-package and MCP readiness canary; no host credentials."""
    return b'''import asyncio, hashlib, json, sys, tomllib\nfrom pathlib import Path\nfrom mcp import Client, StdioServerParameters\ndef digest(v): return hashlib.sha256(v).hexdigest()\nbase = Path('/opt/caprmedio-framework')\nspec = json.loads(Path('/opt/caprmedio-bootstrap-canary.json').read_bytes())\nmanifest_bytes = (base / 'manifest.toml').read_bytes()\nassert digest(manifest_bytes) == spec['manifest_sha256']\nmanifest = tomllib.loads(manifest_bytes.decode())\nassert manifest['candidate_snapshot_manifest_sha256'] == spec['source_context_sha256']\nassert manifest['files'] == spec['package_rows']\nexpected = {'manifest.toml'} | {row['destination'] for row in spec['package_rows']}\nassert {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} == expected\nfor row in spec['package_rows']:\n p = base / row['destination']; assert p.is_file() and not p.is_symlink()\n assert digest(p.read_bytes()) == row['sha256'] and p.stat().st_mode & 511 == row['mode']\nasync def probe():\n project = Path('/tmp/bootstrap-canary-project'); project.mkdir()\n source = project / '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'\n source.parent.mkdir(parents=True); (source.parent / '003_PROJECT_CONFIGURATION').mkdir()\n for row in spec['package_rows']:\n  if row['destination'].startswith('METHODOLOGY/sources/'):\n   out = source / row['destination'].removeprefix('METHODOLOGY/sources/'); out.parent.mkdir(parents=True, exist_ok=True); out.write_bytes((base / row['destination']).read_bytes())\n params = StdioServerParameters(command=sys.executable, args=['/opt/caprmedio-framework/FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py', '--project-root', str(project)])\n async with Client(params, cache=None) as client:\n  page = await client.list_tools(); names = [tool.name for tool in page.tools]\n  while page.next_cursor:\n   page = await client.list_tools(cursor=page.next_cursor); names.extend(tool.name for tool in page.tools)\n  result = await client.call_tool('get_mcp_reload_status', {'request': {}})\n  assert names and len(names) == len(set(names)) and not result.is_error\n  return sorted(names)\nnames = asyncio.run(asyncio.wait_for(probe(), 60))\nprint(json.dumps({'schema':'caprmedio.bootstrap_image_canary.v1','manifest_sha256':spec['manifest_sha256'],'source_context_sha256':spec['source_context_sha256'],'verified_files':len(spec['package_rows']),'mcp_tools':names}, sort_keys=True))\n'''


def _context(plan: object, attempt: Path) -> tuple[Path, str]:
    root, rows, manifest_sha256, source_context_sha256, manifest_bytes = _plan(plan)
    _assert_plan_current(plan)
    context = attempt / "context"
    context.mkdir()
    _write(context / "PACKAGE/manifest.toml", manifest_bytes)
    package_rows: list[dict[str, object]] = []
    for row in rows:
        payload = _read_exact(root, row.source_path, row.sha256, row.mode, code="bootstrap-image-source-stale")
        _write(context / "PACKAGE" / row.destination_path, payload, row.mode)
        # The fixed repository Dockerfile copies the Engine tree from the
        # context root.  Package destinations are deliberately different, so
        # mirror only already sealed Engine rows at their declared source
        # paths; this does not discover or admit another host input.
        if row.resource == "FRAMEWORK_ENGINE":
            _write(context / row.source_path, payload, row.mode)
        package_rows.append({"resource": row.resource, "source_path": row.source_path,
                             "destination": row.destination_path, "sha256": row.sha256, "mode": row.mode})
    for relative, payload, mode in _input_rows(root):
        _write_or_verify(context / relative, payload, mode)
    dockerfile = (context / IMAGE_DOCKERFILE).read_bytes()
    _write(context / "Dockerfile", dockerfile + b"\nCOPY --chown=${RUNTIME_UID}:${RUNTIME_GID} PACKAGE /opt/caprmedio-framework\nCOPY bootstrap-canary.py /opt/caprmedio-bootstrap-canary.py\nCOPY bootstrap-canary.json /opt/caprmedio-bootstrap-canary.json\n")
    _write(context / "bootstrap-canary.py", _canary())
    _write(context / "bootstrap-canary.json", canonical_json({
        "manifest_sha256": manifest_sha256,
        "source_context_sha256": source_context_sha256,
        "package_rows": package_rows,
    }))
    _assert_plan_current(plan)
    return context, _tree_digest(context)


def _command(executor: DockerExecutor, name: str, argv: tuple[str, ...], root: Path, attempt: Path,
             records: list[dict[str, object]], timeout_seconds: float) -> DockerCommandResult:
    started_at_ns = time.time_ns()
    try:
        result = executor.run(argv, cwd=root, timeout_seconds=timeout_seconds)
    except OSError as error:
        result = DockerCommandResult(None, b"", type(error).__name__.encode(), False)
    if not isinstance(result, DockerCommandResult) or not isinstance(result.stdout, bytes) or not isinstance(result.stderr, bytes):
        raise _error("bootstrap-image-executor-invalid", "executor must return captured byte outputs")
    if len(result.stdout) > _MAX_OUTPUT_BYTES or len(result.stderr) > _MAX_OUTPUT_BYTES:
        raise _error("bootstrap-image-output-invalid", "captured Docker output is too large")
    if name not in {"build", "inspect", "canary"} or any(record.get("phase") == name for record in records):
        raise _error("bootstrap-image-command-invalid", "bootstrap image command order is invalid")
    _write(attempt / "commands" / name / "stdout", result.stdout)
    _write(attempt / "commands" / name / "stderr", result.stderr)
    records.append({"phase": name, "argv": list(argv), "exit_code": result.exit_code, "timed_out": result.timed_out,
                    "started_at_ns": started_at_ns, "finished_at_ns": time.time_ns(),
                    "stdout_path": f"commands/{name}/stdout", "stderr_path": f"commands/{name}/stderr",
                    "stdout_sha256": _digest(result.stdout), "stderr_sha256": _digest(result.stderr)})
    return result


def _inspect(executor: DockerExecutor, image_digest: str, plan: object, root: Path, attempt: Path,
             records: list[dict[str, object]], timeout_seconds: float) -> bool:
    result = _command(executor, "inspect", ("docker", "image", "inspect", image_digest), root, attempt, records, timeout_seconds)
    if result.timed_out or result.exit_code != 0:
        return False
    _root, _rows, manifest_sha256, source_context_sha256, _bytes = _plan(plan)
    try:
        payload = json.loads(result.stdout)
        inspected = payload[0]
        labels = inspected["Config"]["Labels"]
        return (len(payload) == 1 and inspected.get("Id") == image_digest and isinstance(labels, dict)
                and labels.get(PACKAGE_IMAGE_LABEL) == manifest_sha256
                and labels.get(SOURCE_CONTEXT_IMAGE_LABEL) == source_context_sha256)
    except (IndexError, KeyError, TypeError, ValueError):
        return False


def _fresh_inspect(executor: DockerExecutor, image_digest: str, plan: object, root: Path) -> bool:
    """Observe an image again without appending to immutable proof carriers."""
    try:
        result = executor.run(("docker", "image", "inspect", image_digest), cwd=root, timeout_seconds=60)
    except OSError:
        return False
    if (not isinstance(result, DockerCommandResult) or result.timed_out or result.exit_code != 0
            or not isinstance(result.stdout, bytes) or not isinstance(result.stderr, bytes)
            or len(result.stdout) > _MAX_OUTPUT_BYTES or len(result.stderr) > _MAX_OUTPUT_BYTES):
        return False
    _root, _rows, manifest_sha256, source_context_sha256, _bytes = _plan(plan)
    try:
        payload = json.loads(result.stdout)
        inspected = payload[0]
        labels = inspected["Config"]["Labels"]
        return (len(payload) == 1 and inspected.get("Id") == image_digest and isinstance(labels, dict)
                and labels.get(PACKAGE_IMAGE_LABEL) == manifest_sha256
                and labels.get(SOURCE_CONTEXT_IMAGE_LABEL) == source_context_sha256)
    except (IndexError, KeyError, TypeError, ValueError):
        return False


def _toml(evidence: BootstrapImageEvidence) -> bytes:
    value = asdict(replace(evidence, receipt_sha256=None))
    lines = ["schema_version = 1"]
    for key in ("manifest_sha256", "source_context_sha256", "outcome", "reason", "image_digest", "context_sha256",
                "evidence_root", "commands_sha256", "execution_kind", "started_at", "finished_at",
                "bootstrap_proof_key", "proof_root", "context_root"):
        item = value[key]
        if item is None:
            lines.append(f"{key} = false")
        else:
            lines.append(f"{key} = {json.dumps(item, ensure_ascii=False)}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _record(attempt: Path, evidence: BootstrapImageEvidence) -> BootstrapImageEvidence:
    try:
        payload = _toml(evidence)
        _write(attempt / "evidence.toml", payload)
        descriptor = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return replace(evidence, receipt_sha256=_digest(payload))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="bootstrap image evidence recording is uncertain")


def _canary_valid(report: object, *, manifest_sha256: str, source_context_sha256: str,
                  row_count: int, image_digest: str, actual_executor: bool) -> bool:
    if not isinstance(report, dict):
        return False
    # A test double can exercise the complete parser and command boundary, but
    # its resulting evidence remains explicitly ``test-double`` and therefore
    # cannot be treated as actual first-N authorization by the initializer.
    required = {"schema", "manifest_sha256", "source_context_sha256", "verified_files", "mcp_tools"}
    if set(report) not in (required, required | {"image_digest"}):
        return False
    return (
        ("image_digest" not in report or report["image_digest"] == image_digest)
        and report["schema"] == "caprmedio.bootstrap_image_canary.v1"
        and report["manifest_sha256"] == manifest_sha256
        and report["source_context_sha256"] == source_context_sha256
        and type(report["verified_files"]) is int and report["verified_files"] == row_count
        and isinstance(report["mcp_tools"], list) and report["mcp_tools"]
        and len(report["mcp_tools"]) == len(set(report["mcp_tools"]))
        and "get_mcp_reload_status" in report["mcp_tools"]
    )


def _proof_key(root: Path, manifest_sha256: str, image_digest: str) -> Path:
    if IMAGE_ID.fullmatch(image_digest) is None:
        raise _error("bootstrap-image-digest-invalid", "image digest must be an immutable SHA-256 ID")
    key = _digest(canonical_json([manifest_sha256, image_digest]))
    return root / BOOTSTRAP_IMAGE_RELATIVE / key


def _materialize_canonical_proof(root: Path, attempt: Path, evidence: BootstrapImageEvidence) -> BootstrapImageEvidence:
    """Copy sealed retained bytes to their content-addressed proof directory.

    Some supported hosts deny directory rename, so this never relies on it.
    The source is retained, the destination is created once, and every copied
    carrier is re-digested before the canonical evidence is written.
    """
    if evidence.image_digest is None:
        return replace(evidence, outcome="recording_uncertain", reason="bootstrap image proof has no immutable image ID")
    proof = _proof_key(root, evidence.manifest_sha256, evidence.image_digest)
    try:
        proof.mkdir(parents=True, exist_ok=False)
        for name in ("context", "commands"):
            shutil.copytree(attempt / name, proof / name, copy_function=shutil.copy2)
        shutil.copy2(attempt / "commands.json", proof / "commands.json")
        proof_root = proof.relative_to(root).as_posix()
        copied = replace(
            evidence,
            evidence_root=proof_root,
            bootstrap_proof_key=proof.name,
            proof_root=proof_root,
            context_root=f"{proof_root}/context",
            receipt_sha256=None,
        )
        if (_tree_digest(proof / "context") != evidence.context_sha256
                or _digest((proof / "commands.json").read_bytes()) != evidence.commands_sha256):
            raise OSError("copied bootstrap proof differs from retained attempt")
        copied = _record(proof, copied)
        if copied.outcome == "recording_uncertain":
            return copied
        descriptor = os.open(proof, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        return copied
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="canonical bootstrap proof recording is uncertain")


def produce_initial_framework_image(plan: object, *, executor: DockerExecutor,
                                    timeout_seconds: float = 900) -> BootstrapImageEvidence:
    """Build, inspect, and canary one first-N image without publication effects."""
    if isinstance(timeout_seconds, bool) or not 0 < timeout_seconds <= 900:
        raise _error("bootstrap-image-timeout-invalid", "build timeout must be within (0, 900]")
    root, _rows, manifest_sha256, source_context_sha256, _bytes = _plan(plan)
    started_at = _timestamp()
    try:
        _assert_plan_current(plan)
    except BootstrapImageError as error:
        return BootstrapImageEvidence(
            manifest_sha256, source_context_sha256, "stale", str(error), None, "0" * 64,
            "", _digest(b"[]"), "docker-subprocess" if type(executor) is DockerSubprocessExecutor else "test-double",
            started_at, _timestamp(),
        )
    parent = root / BOOTSTRAP_IMAGE_RELATIVE
    parent.mkdir(parents=True, exist_ok=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    context, context_sha256 = _context(plan, attempt)
    records: list[dict[str, object]] = []
    image: str | None = None
    outcome: Literal["verified", "failed", "incomplete", "stale", "effect_uncertain", "recording_uncertain"] = "incomplete"
    reason = "immutable bootstrap image identity is unverified"
    try:
        _assert_plan_current(plan)
        result = _command(executor, "build", ("docker", "build", "--iidfile", str(attempt / "image.id"),
            "--label", f"{PACKAGE_IMAGE_LABEL}={manifest_sha256}",
            "--label", f"{SOURCE_CONTEXT_IMAGE_LABEL}={source_context_sha256}",
            "--file", str(context / "Dockerfile"), str(context)), root, attempt, records, timeout_seconds)
        if result.timed_out:
            outcome, reason = "effect_uncertain", "Docker build timed out; its effect must not be replayed"
        elif result.exit_code != 0:
            outcome, reason = "failed", "bootstrap image build failed"
        else:
            candidate = (attempt / "image.id").read_text().strip() if (attempt / "image.id").is_file() else ""
            if IMAGE_ID.fullmatch(candidate) and _inspect(executor, candidate, plan, root, attempt, records, timeout_seconds):
                image = candidate
                canary = _command(executor, "canary", ("docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                    "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
                    "--entrypoint", "python", candidate, "/opt/caprmedio-bootstrap-canary.py"), root, attempt, records, 120)
                if canary.timed_out:
                    outcome, reason = "effect_uncertain", "bootstrap image canary timed out"
                elif canary.exit_code != 0:
                    outcome, reason = "failed", "bootstrap image canary failed"
                else:
                    report = json.loads(canary.stdout)
                    if _canary_valid(report, manifest_sha256=manifest_sha256,
                                     source_context_sha256=source_context_sha256,
                                     row_count=len(getattr(plan, "rows")), image_digest=candidate,
                                     actual_executor=type(executor) is DockerSubprocessExecutor):
                        outcome, reason = "verified", "complete initial package and fixed MCP canary observed"
        _assert_plan_current(plan)
        if _tree_digest(context) != context_sha256:
            raise _error("bootstrap-image-context-stale", "private bootstrap context changed during Docker execution")
    except (OSError, ValueError, RuntimeError, BootstrapImageError) as error:
        outcome = "stale" if isinstance(error, BootstrapImageError) and "stale" in error.code else "recording_uncertain"
        reason = str(error)
    commands = canonical_json(records)
    try:
        _write(attempt / "commands.json", commands)
    except OSError:
        outcome, reason = "recording_uncertain", "bootstrap image command recording is uncertain"
    evidence = BootstrapImageEvidence(manifest_sha256, source_context_sha256, outcome, reason, image, context_sha256,
                                      attempt.relative_to(root).as_posix(), _digest(commands),
                                      "docker-subprocess" if type(executor) is DockerSubprocessExecutor else "test-double",
                                      started_at, _timestamp())
    evidence = _record(attempt, evidence)
    if evidence.outcome == "verified":
        evidence = _materialize_canonical_proof(root, attempt, evidence)
    return evidence


def _load_evidence(plan: object, image_digest: str) -> tuple[Path, BootstrapImageEvidence]:
    root, _rows, manifest_sha256, source_context_sha256, _bytes = _plan(plan)
    return _load_evidence_for_identity(root, manifest_sha256, source_context_sha256, image_digest)


def _load_evidence_for_identity(root: Path, manifest_sha256: str, source_context_sha256: str,
                                image_digest: str) -> tuple[Path, BootstrapImageEvidence]:
    """Read the canonical proof addressed by an already verified package."""

    proof = _proof_key(root, manifest_sha256, image_digest)
    if proof.is_symlink() or not proof.is_dir():
        raise _error("bootstrap-image-proof-missing", "canonical bootstrap image proof is absent")
    evidence_path = proof / "evidence.toml"
    if evidence_path.is_symlink() or not evidence_path.is_file():
        raise _error("bootstrap-image-proof-missing", "canonical bootstrap image evidence is absent")
    try:
        payload = evidence_path.read_bytes()
        parsed = tomllib.loads(payload.decode("utf-8"))
        expected = {"schema_version", "manifest_sha256", "source_context_sha256", "outcome", "reason", "image_digest",
                    "context_sha256", "evidence_root", "commands_sha256", "execution_kind", "started_at", "finished_at",
                    "bootstrap_proof_key", "proof_root", "context_root"}
        if set(parsed) != expected or parsed["schema_version"] != 1:
            raise ValueError("unsupported evidence schema")
        evidence = BootstrapImageEvidence(**{key: parsed[key] for key in expected if key != "schema_version"})
        if payload != _toml(evidence):
            raise ValueError("evidence is not canonical")
        evidence = replace(evidence, receipt_sha256=_digest(payload))
    except (TypeError, ValueError, tomllib.TOMLDecodeError, UnicodeDecodeError) as error:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap image proof is malformed") from error
    if (evidence.outcome != "verified"
            or evidence.manifest_sha256 != manifest_sha256 or evidence.source_context_sha256 != source_context_sha256
            or evidence.image_digest != image_digest or evidence.evidence_root != proof.relative_to(root).as_posix()
            or evidence.bootstrap_proof_key != proof.name or evidence.proof_root != proof.relative_to(root).as_posix()
            or evidence.context_root != f"{proof.relative_to(root).as_posix()}/context"):
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap image proof does not bind this plan and digest")
    return proof, evidence


def _verify_retained_commands(proof: Path, evidence: BootstrapImageEvidence) -> list[dict[str, object]]:
    commands = proof / "commands.json"
    if commands.is_symlink() or not commands.is_file() or _digest(commands.read_bytes()) != evidence.commands_sha256:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command receipt changed")
    try:
        records = json.loads(commands.read_bytes())
    except (UnicodeDecodeError, ValueError) as error:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command receipt is invalid") from error
    if not isinstance(records, list) or [record.get("phase") if isinstance(record, dict) else None for record in records] != ["build", "inspect", "canary"]:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command receipt is incomplete")
    for record in records:
        if not isinstance(record, dict) or set(record) != {"phase", "argv", "exit_code", "timed_out", "started_at_ns", "finished_at_ns", "stdout_path", "stderr_path", "stdout_sha256", "stderr_sha256"}:
            raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command receipt has an unsupported shape")
        for stream in ("stdout", "stderr"):
            if record[f"{stream}_path"] != f"commands/{record['phase']}/{stream}":
                raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command output path is invalid")
            path = proof / record[f"{stream}_path"]
            digest = record[f"{stream}_sha256"]
            if (path.is_symlink() or not path.is_file() or not isinstance(digest, str)
                    or _SHA256.fullmatch(digest) is None or _digest(path.read_bytes()) != digest):
                raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command output changed")
    if any(type(record["started_at_ns"]) is not int or type(record["finished_at_ns"]) is not int
           or record["started_at_ns"] > record["finished_at_ns"] for record in records):
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command times are invalid")
    if any(type(record["exit_code"]) is not int or record["exit_code"] != 0
           or type(record["timed_out"]) is not bool or record["timed_out"]
           for record in records):
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap command receipt is not successful")
    build, inspect, canary = (record["argv"] for record in records)
    expected_labels = {
        f"{PACKAGE_IMAGE_LABEL}={evidence.manifest_sha256}",
        f"{SOURCE_CONTEXT_IMAGE_LABEL}={evidence.source_context_sha256}",
    }
    if (not all(isinstance(value, str) for value in build)
            or len(build) != 11 or build[:3] != ["docker", "build", "--iidfile"]
            or build[4] != "--label" or build[6] != "--label" or {build[5], build[7]} != expected_labels
            or build[8] != "--file" or not build[9].endswith("/Dockerfile")
            or not build[3].endswith("/image.id") or build[9].removesuffix("/Dockerfile") != build[10]):
        raise _error("bootstrap-image-proof-invalid", "retained build argv is not the fixed bootstrap vector")
    if inspect != ["docker", "image", "inspect", evidence.image_digest]:
        raise _error("bootstrap-image-proof-invalid", "retained image inspection argv is not bound to the immutable ID")
    expected_canary = ["docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
                       "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs",
                       "/tmp:rw,nosuid,nodev,size=128m", "--entrypoint", "python", evidence.image_digest,
                       "/opt/caprmedio-bootstrap-canary.py"]
    if canary != expected_canary:
        raise _error("bootstrap-image-proof-invalid", "retained MCP canary argv is not bound to the immutable ID")
    return records


def _retained_initial_package(root: Path, executing_release: str) -> tuple[Path, tuple[PackageRow, ...], bytes, str]:
    """Read a first-N package without consulting the subsequently edited host source."""

    if not isinstance(executing_release, str) or _SHA256.fullmatch(executing_release) is None:
        raise _error("bootstrap-image-package-invalid", "retained bootstrap release identity is invalid")
    package_relative = f"{RUNTIME_ROOT.as_posix()}/releases/{executing_release}"
    manifest_path = _safe_file(root, f"{package_relative}/manifest.toml", code="bootstrap-image-package-missing")
    try:
        manifest_bytes = manifest_path.read_bytes()
        manifest_text = manifest_bytes.decode("utf-8")
        manifest = tomllib.loads(manifest_text)
        if (
            _digest(manifest_bytes) != executing_release
            or set(manifest) != {"schema_version", "candidate_snapshot_manifest_sha256", "package", "files"}
            or manifest["schema_version"] != 2
            or manifest["package"] != "caprmedio-framework"
            or not isinstance(manifest["candidate_snapshot_manifest_sha256"], str)
            or _SHA256.fullmatch(manifest["candidate_snapshot_manifest_sha256"]) is None
            or not isinstance(manifest["files"], list)
        ):
            raise ValueError("retained bootstrap manifest is invalid")
        rows = tuple(PackageRow.model_validate({
            "resource": row["resource"],
            "source_path": row["source_path"],
            "destination_path": row["destination"],
            "sha256": row["sha256"],
            "mode": row["mode"],
        }) for row in manifest["files"])
        source_context_sha256 = manifest["candidate_snapshot_manifest_sha256"]
        expected_context = _digest(canonical_json([
            (row.source_path, row.sha256, row.mode)
            for row in sorted(rows, key=lambda item: item.source_path)
        ]))
        destinations = {row.destination_path for row in rows}
        resources = {row.resource for row in rows}
        if (
            not rows
            or list(rows) != sorted(rows, key=lambda item: (item.destination_path, item.source_path, item.sha256))
            or len(destinations) != len(rows)
            or expected_context != source_context_sha256
            or resources != {"FRAMEWORK_ENGINE", "METHODOLOGY", "SKILL"}
            or not any(row.destination_path.startswith("METHODOLOGY/sources/") for row in rows)
            or not any(row.destination_path.startswith("METHODOLOGY/compiled/") for row in rows)
            or not REQUIRED_SKILL_FILES <= destinations
            or any(
                not any(row.source_path.startswith(prefix) for row in rows if row.resource == "FRAMEWORK_ENGINE")
                for prefix in REQUIRED_ENGINE_SOURCE_PREFIXES
            )
        ):
            raise ValueError("retained bootstrap package is incomplete")
        package = root / package_relative
        _verify_release(package, _render_manifest(source_context_sha256, rows), rows)
    except (KeyError, OSError, TypeError, ValueError, tomllib.TOMLDecodeError, ReleasePackagingError) as error:
        raise _error("bootstrap-image-package-invalid", "retained bootstrap package is not exact") from error
    return package, rows, manifest_bytes, source_context_sha256


def _verify_retained_package_context(proof: Path, manifest_bytes: bytes, rows: tuple[PackageRow, ...]) -> None:
    """Tie the retained build context and canary input to the retained package bytes."""

    package = proof / "context" / "PACKAGE"
    try:
        if package.is_symlink() or not package.is_dir() or (package / "manifest.toml").read_bytes() != manifest_bytes:
            raise ValueError("retained package context does not match the package manifest")
        expected = {"manifest.toml", *(row.destination_path for row in rows)}
        actual = {
            item.relative_to(package).as_posix()
            for item in package.rglob("*")
            if item.is_file()
        }
        if actual != expected:
            raise ValueError("retained package context inventory differs")
        for row in rows:
            _read_exact(package, row.destination_path, row.sha256, row.mode, code="bootstrap-image-proof-invalid")
        canary = proof / "context" / "bootstrap-canary.json"
        expected_canary = canonical_json({
            "manifest_sha256": _digest(manifest_bytes),
            "source_context_sha256": _source_context(rows),
            "package_rows": [
                {"resource": row.resource, "source_path": row.source_path,
                 "destination": row.destination_path, "sha256": row.sha256, "mode": row.mode}
                for row in rows
            ],
        })
        if canary.is_symlink() or not canary.is_file() or canary.read_bytes() != expected_canary:
            raise ValueError("retained canary input differs from the package")
        program = proof / "context" / "bootstrap-canary.py"
        if program.is_symlink() or not program.is_file() or program.read_bytes() != _canary():
            raise ValueError("retained canary program differs from the fixed probe")
    except (OSError, ValueError, BootstrapImageError) as error:
        raise _error("bootstrap-image-proof-invalid", "retained bootstrap package context is invalid") from error


def _source_context(rows: tuple[PackageRow, ...]) -> str:
    return _digest(canonical_json([
        (row.source_path, row.sha256, row.mode)
        for row in sorted(rows, key=lambda item: item.source_path)
    ]))


def read_retained_initial_framework_image(project_root: Path | str, executing_release: str,
                                          image_digest: str) -> BootstrapImageEvidence:
    """Authenticate a first-N image from retained package/proof bytes only.

    This is deliberately a reader, not an initializer revalidation: a later
    N+1 source frontier is expected to differ from the first installed N.
    """

    try:
        root = Path(project_root).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise _error("bootstrap-image-package-invalid", "Project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise _error("bootstrap-image-package-invalid", "Project root is unsafe")
    package, rows, manifest_bytes, source_context_sha256 = _retained_initial_package(root, executing_release)
    del package
    proof, evidence = _load_evidence_for_identity(root, executing_release, source_context_sha256, image_digest)
    if evidence.execution_kind != "docker-subprocess":
        raise _error("bootstrap-image-proof-invalid", "retained bootstrap proof was not produced by DockerSubprocessExecutor")
    records = _verify_retained_commands(proof, evidence)
    if _tree_digest(proof / "context") != evidence.context_sha256:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap proof bytes changed")
    _verify_retained_package_context(proof, manifest_bytes, rows)
    try:
        report = json.loads((proof / records[2]["stdout_path"]).read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, TypeError, ValueError) as error:
        raise _error("bootstrap-image-proof-invalid", "retained bootstrap canary report is invalid") from error
    if not _canary_valid(report, manifest_sha256=executing_release,
                         source_context_sha256=source_context_sha256,
                         row_count=len(rows), image_digest=image_digest, actual_executor=True):
        raise _error("bootstrap-image-proof-invalid", "retained bootstrap canary report is not bound to the package")
    return evidence


def revalidate_initial_framework_image(plan: object, image_digest: str, *, executor: DockerExecutor) -> BootstrapImageEvidence:
    """Reopen only the derived proof path, then perform a fresh immutable inspect."""
    _assert_plan_current(plan)
    root, _rows, _manifest, _source_context, _bytes = _plan(plan)
    proof, evidence = _load_evidence(plan, image_digest)
    context = proof / "context"
    _verify_retained_commands(proof, evidence)
    if _tree_digest(context) != evidence.context_sha256:
        raise _error("bootstrap-image-proof-invalid", "canonical bootstrap proof bytes changed")
    if not _fresh_inspect(executor, image_digest, plan, root):
        raise _error("bootstrap-image-proof-stale", "fresh image inspection no longer proves the sealed bootstrap image")
    _assert_plan_current(plan)
    return evidence


__all__ = [
    "BOOTSTRAP_IMAGE_RELATIVE", "BootstrapImageError", "BootstrapImageEvidence",
    "produce_initial_framework_image", "read_retained_initial_framework_image", "revalidate_initial_framework_image",
]
