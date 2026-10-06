"""Installed-N immutable-image executor for the sealed Release suite.

This adapter is private to the selected Release Action.  It neither chooses a
Docker image from request data nor accepts a caller-defined mount, network, or
environment.  The caller already sealed the candidate; this module derives the
currently selected N image, verifies its identity labels, and runs the exact
sealed command with only the disposable suite workspace and output mounted.
"""

from __future__ import annotations

import json
import hashlib
import re
import tomllib
from dataclasses import dataclass, replace
from pathlib import Path

from release_contract import ReleaseContractError, ValidatedCandidate
from release_handoff import CURRENT_SELECTOR_RELATIVE, SealedCandidateCompilation
from release_image import CANDIDATE_LABEL, CONTEXT_LABEL, DockerExecutor, IMAGE_ID
from release_suite_limits import MAX_UNIT_TIMEOUT_SECONDS
from bootstrap_image import BootstrapImageError, read_retained_initial_framework_image
from release_suite import (
    CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE,
    COMPILED_ROOT_ENVIRONMENT_VARIABLE,
    PROJECT_ROOT_ENVIRONMENT_VARIABLE,
    REPORT_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_RELATIVE,
    SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE,
    SANDBOX_OUTPUT_PATH,
    SANDBOX_WORKSPACE_PATH,
    SuiteExecutionResult,
    _active_n_state,
    _bootstrap_prior_manifest_is_exact,
    _bootstrap_source_context_is_valid,
    require_declared_suite_command,
)


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_INSPECT_TIMEOUT_SECONDS = 30
_CLEANUP_TIMEOUT_SECONDS = 30
_CONTAINER_ID = re.compile(r"^[0-9a-f]{64}$")
_SANDBOX_TMPFS_SIZE = "2g"
_EXECUTOR_SCRATCH_RELATIVE = Path(".caprmedio_tmp")
_SUITE_LABEL = "org.caprmedio.release-suite"
_ATTEMPT_LABEL = "org.caprmedio.release-suite-attempt"
_PYTHON_CAPABILITY_GUARD = "import sys; raise SystemExit(0 if sys.version_info >= (3, 8) else 1)"
# This is deliberately an executor-owned program, not a shell fragment or a
# caller-provided command.  PID 1 is responsible for the hard deadline even
# if the host-side Docker CLI disappears before it can observe the outcome.
_DEADLINE_GUARD = r'''import math
import os
import signal
import subprocess
import sys
import time

try:
    deadline = float(sys.argv[1])
    command = sys.argv[3:]
    if (not math.isfinite(deadline) or deadline <= 0 or deadline > 7200
            or sys.argv[2] != "--" or not command):
        raise ValueError
except (IndexError, ValueError):
    raise SystemExit(125)

try:
    child = subprocess.Popen(command, start_new_session=True)
except OSError:
    raise SystemExit(125)

started = time.monotonic()
reserve = min(1.0, deadline / 2)
term_at = started + deadline - reserve
hard_at = started + deadline
while True:
    status = child.poll()
    if status is not None:
        raise SystemExit(status)
    now = time.monotonic()
    if now >= term_at:
        break
    time.sleep(min(0.05, term_at - now))

# Once TERM is issued, timeout is latched even if a cooperative child returns
# zero before hard expiry.
try:
    os.killpg(child.pid, signal.SIGTERM)
except ProcessLookupError:
    pass
except OSError:
    raise SystemExit(125)

while child.poll() is None and time.monotonic() < hard_at:
    time.sleep(min(0.05, hard_at - time.monotonic()))
if child.poll() is None:
    try:
        os.killpg(child.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    except OSError:
        raise SystemExit(125)
try:
    child.wait()
except OSError:
    raise SystemExit(125)
raise SystemExit(124)
'''
_EXPECTED_ENVIRONMENT_KEYS = frozenset({
    "PATH",
    PROJECT_ROOT_ENVIRONMENT_VARIABLE,
    REPORT_ENVIRONMENT_VARIABLE,
    COMPILED_ROOT_ENVIRONMENT_VARIABLE,
    CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_ENVIRONMENT_VARIABLE,
    SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE,
})
_BOOTSTRAP_PACKAGE_LABEL = "org.caprmedio.framework.package_manifest_sha256"
_BOOTSTRAP_CONTEXT_LABEL = "org.caprmedio.framework.source_context_sha256"


@dataclass(frozen=True)
class SelectedNImageBinding:
    image_digest: str
    executing_release: str
    source_context_sha256: str
    bootstrap: bool
    selector_sha256: str
    candidate_release: str | None
    image_path: str | None = None


def _selector_binding(root: Path, candidate: ValidatedCandidate) -> SelectedNImageBinding:
    """Read only the fully selected immutable N-image binding."""

    selector = root / CURRENT_SELECTOR_RELATIVE
    if selector.is_symlink() or not selector.is_file():
        raise ReleaseContractError("release-suite-executor-n-invalid", "selected N image binding is missing or unsafe")
    try:
        selector_bytes = selector.read_bytes()
        payload = tomllib.loads(selector_bytes.decode("utf-8"))
        selector_sha256 = hashlib.sha256(selector_bytes).hexdigest()
        release = candidate.authority.executing_release
        selected_root = ".caprmedio_runtime/framework/releases/" + release
        if isinstance(payload, dict) and "manifest_sha256" in payload:
            package_manifest = root / selected_root / "manifest.toml"
            manifest_bytes = package_manifest.read_bytes()
            bootstrap = _bootstrap_prior_manifest_is_exact(payload, manifest_bytes, release)
        else:
            bootstrap = False
        if bootstrap:
            manifest = tomllib.loads(manifest_bytes.decode("utf-8"))
            context = manifest.get("candidate_snapshot_manifest_sha256")
            if not _bootstrap_source_context_is_valid(context):
                raise ValueError("bootstrap source context is invalid")
            return SelectedNImageBinding(payload["image_digest"], release, context, True, selector_sha256, None)
        exact = {
            "schema_version": 1,
            "candidate_snapshot_manifest_sha256": candidate.authority.executing_release,
            "release": candidate.authority.executing_release,
            "candidate_release": candidate.manifest.candidate_release,
            "selected_release_root": selected_root,
            "framework_engine_root": selected_root + "/FRAMEWORK_ENGINE",
            "methodology_root": selected_root + "/METHODOLOGY",
        }
        if (not isinstance(payload, dict)
                or set(payload) != {*exact, "candidate_image_digest", "candidate_image_context_sha256"}
                or type(payload.get("schema_version")) is not int
                or any(payload.get(key) != value for key, value in exact.items())):
            raise ValueError("selector does not bind the executing release")
        image = payload.get("candidate_image_digest")
        context = payload.get("candidate_image_context_sha256")
        if (not isinstance(image, str) or IMAGE_ID.fullmatch(image) is None
                or not _bootstrap_source_context_is_valid(context)):
            raise ValueError("selector has no immutable image/context binding")
        return SelectedNImageBinding(image, release, context, False, selector_sha256, candidate.manifest.candidate_release)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        raise ReleaseContractError("release-suite-executor-n-invalid", "selected N image binding is invalid") from error


def _inspect_bound_n_image(docker: DockerExecutor, root: Path,
                           binding: SelectedNImageBinding) -> SelectedNImageBinding:
    """Verify the immutable selected-N labels and its sole image PATH."""

    if binding.bootstrap:
        try:
            retained = read_retained_initial_framework_image(
                root, binding.executing_release, binding.image_digest,
            )
        except BootstrapImageError as error:
            raise ReleaseContractError(
                "release-suite-executor-n-unproven",
                "executing N bootstrap image has no authentic retained proof",
            ) from error
        if (retained.manifest_sha256 != binding.executing_release
                or retained.source_context_sha256 != binding.source_context_sha256
                or retained.image_digest != binding.image_digest):
            raise ReleaseContractError(
                "release-suite-executor-n-unproven",
                "executing N bootstrap proof does not bind the selected image",
            )
    observed = docker.run(("docker", "image", "inspect", binding.image_digest), cwd=root, timeout_seconds=_INSPECT_TIMEOUT_SECONDS)
    if observed.timed_out:
        raise ReleaseContractError("release-suite-executor-n-unproven", "executing N image inspection timed out")
    try:
        payload = json.loads(observed.stdout)
        item = payload[0]
        labels = item["Config"]["Labels"]
        environment = item["Config"]["Env"]
        package_label = _BOOTSTRAP_PACKAGE_LABEL if binding.bootstrap else CANDIDATE_LABEL
        context_label = _BOOTSTRAP_CONTEXT_LABEL if binding.bootstrap else CONTEXT_LABEL
        context = labels[context_label]
        if (
            observed.exit_code != 0
            or not isinstance(payload, list)
            or len(payload) != 1
            or item.get("Id") != binding.image_digest
            or labels.get(package_label) != binding.executing_release
            or context != binding.source_context_sha256
            or not isinstance(environment, list)
        ):
            raise ValueError("image does not prove selected N manifest/context labels")
        if binding.bootstrap:
            environment_values: dict[str, str] = {}
            for item in environment:
                if not isinstance(item, str) or "=" not in item:
                    raise ValueError("bootstrap image environment is malformed")
                name, value = item.split("=", 1)
                if (not name or name in environment_values or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name)
                        or "\x00" in value or "\n" in value or "\r" in value):
                    raise ValueError("bootstrap image environment is unsafe")
                environment_values[name] = value
            path = environment_values.get("PATH")
        else:
            if len(environment) != 1 or not isinstance(environment[0], str) or not environment[0].startswith("PATH="):
                raise ValueError("image has undeclared environment members")
            path = environment[0].removeprefix("PATH=")
        if not path or "\x00" in path or "\n" in path or "\r" in path:
            raise ValueError("image PATH is unsafe")
        return replace(binding, image_path=path)
    except (IndexError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise ReleaseContractError("release-suite-executor-n-unproven", "executing N image labels are absent or mismatched") from error


def _safe_directory_chain(root: Path, target: Path, *, label: str) -> None:
    """Require an existing non-symlink directory at every mount ancestor."""

    if root.is_symlink() or not root.is_dir() or ".." in target.parts:
        raise ReleaseContractError("release-suite-executor-mount-unsafe", f"{label} root or path is unsafe")
    try:
        relative = target.relative_to(root)
    except ValueError as error:
        raise ReleaseContractError("release-suite-executor-mount-unsafe", f"{label} is outside the Project") from error
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink() or not cursor.is_dir():
            raise ReleaseContractError("release-suite-executor-mount-unsafe", f"{label} has a symlinked or missing ancestor")


def _attempt_mounts(root: Path, candidate_sha: str, workspace: Path, output_root: Path) -> str:
    """Accept exactly one generated attempt's workspace/output leaves."""

    evidence = root / ".caprmedio_runtime/release_suite" / candidate_sha
    _safe_directory_chain(root, evidence, label="suite evidence root")
    if workspace.name != "workspace" or output_root.name != "output" or workspace.parent != output_root.parent:
        raise ReleaseContractError("release-suite-executor-mount-unsafe", "suite mounts are not exact workspace/output leaves")
    attempt = workspace.parent
    if attempt.parent != evidence or not attempt.name.startswith("attempt-") or attempt.name == "attempt-":
        raise ReleaseContractError("release-suite-executor-mount-unsafe", "suite mounts are outside a generated attempt")
    _safe_directory_chain(root, workspace, label="suite workspace")
    _safe_directory_chain(root, output_root, label="suite output")
    return attempt.name


def _prepare_executor_scratch(workspace: Path) -> Path:
    """Reserve the sole ignored scratch mountpoint in a disposable workspace.

    Docker requires a target below a read-only bind to exist before it can be
    overmounted with tmpfs.  This creates only the fixed, empty ignored leaf;
    it never makes the source mount generally writable or accepts a caller
    selected scratch path.
    """

    scratch = workspace / _EXECUTOR_SCRATCH_RELATIVE
    try:
        if scratch.exists() or scratch.is_symlink():
            if scratch.is_symlink() or not scratch.is_dir():
                raise ValueError("scratch mountpoint is not a directory")
            if any(scratch.iterdir()):
                raise ValueError("scratch mountpoint is not empty")
        else:
            scratch.mkdir(mode=0o700)
    except (OSError, ValueError) as error:
        raise ReleaseContractError(
            "release-suite-executor-scratch-unsafe",
            "suite workspace scratch mountpoint is unsafe",
        ) from error
    return scratch


def _preflight_installed_python(docker: DockerExecutor, root: Path, image: str, python: str) -> None:
    """Prove the admitted image Python can execute the fixed guard form."""

    observed = docker.run(
        (
            "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges", "--pids-limit=128",
            "--tmpfs", f"/tmp:rw,nosuid,nodev,exec,size={_SANDBOX_TMPFS_SIZE},mode=1777",
            "--entrypoint", python, image, "-c", _PYTHON_CAPABILITY_GUARD,
        ),
        cwd=root,
        timeout_seconds=_INSPECT_TIMEOUT_SECONDS,
    )
    if observed.timed_out or observed.exit_code != 0:
        raise ReleaseContractError(
            "release-suite-executor-python-unproven",
            "installed N Python cannot execute the fixed deadline guard",
        )


def _cleanup_timed_out_container(
    docker: DockerExecutor,
    root: Path,
    cidfile: Path,
    *,
    candidate_sha: str,
    attempt_name: str,
) -> bool:
    """Remove only the exact labeled container, otherwise retain uncertainty."""

    try:
        if cidfile.is_symlink() or not cidfile.is_file() or cidfile.stat().st_size > 128:
            return False
        container_id = cidfile.read_text(encoding="ascii").strip()
        if _CONTAINER_ID.fullmatch(container_id) is None:
            return False
        inspected = docker.run(("docker", "container", "inspect", container_id), cwd=root,
                               timeout_seconds=_CLEANUP_TIMEOUT_SECONDS)
        if inspected.timed_out or inspected.exit_code != 0:
            return False
        payload = json.loads(inspected.stdout)
        item = payload[0]
        labels = item["Config"]["Labels"]
        if (
            not isinstance(payload, list)
            or len(payload) != 1
            or item.get("Id") != container_id
            or labels.get(_SUITE_LABEL) != candidate_sha
            or labels.get(_ATTEMPT_LABEL) != attempt_name
        ):
            return False
        removed = docker.run(("docker", "container", "rm", "-f", container_id), cwd=root,
                             timeout_seconds=_CLEANUP_TIMEOUT_SECONDS)
        return not removed.timed_out and removed.exit_code == 0
    except (OSError, UnicodeError, ValueError, TypeError, KeyError, IndexError, json.JSONDecodeError):
        return False


@dataclass(frozen=True)
class InstalledNSuiteDockerExecutor:
    """A closed installed-N Docker boundary derived by the Release Action."""

    root: Path
    docker: DockerExecutor
    candidate_snapshot_manifest_sha256: str
    executing_release: str
    image_digest: str
    source_context_sha256: str
    selected_n_image: SelectedNImageBinding
    image_path: str
    sealed_command: tuple[str, ...]
    sealed_working_directory: str
    compiled_root: str

    def _validate_invocation(
        self,
        command: tuple[str, ...],
        workspace: Path,
        output_root: Path,
        working_directory: str,
        environment: dict[str, str],
        timeout_seconds: float,
    ) -> None:
        _attempt_mounts(self.root, self.candidate_snapshot_manifest_sha256, workspace, output_root)
        if command != self.sealed_command or working_directory != self.sealed_working_directory:
            raise ReleaseContractError("release-suite-executor-binding-mismatch", "suite command or working directory differs from sealed selection")
        if not isinstance(timeout_seconds, (int, float)) or isinstance(timeout_seconds, bool) or not 0 < timeout_seconds <= MAX_UNIT_TIMEOUT_SECONDS:
            raise ReleaseContractError("release-suite-executor-timeout-invalid", "suite timeout is outside the governed bound")
        bindings_sha256 = environment.get(SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE)
        if not isinstance(bindings_sha256, str) or _SHA256.fullmatch(bindings_sha256) is None:
            raise ReleaseContractError("release-suite-executor-environment-untrusted", "suite source-bindings digest is invalid")
        expected = {
            "PATH": self.image_path,
            PROJECT_ROOT_ENVIRONMENT_VARIABLE: str(SANDBOX_WORKSPACE_PATH),
            REPORT_ENVIRONMENT_VARIABLE: str(SANDBOX_OUTPUT_PATH / "coverage.xml"),
            COMPILED_ROOT_ENVIRONMENT_VARIABLE: self.compiled_root,
            CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE: self.candidate_snapshot_manifest_sha256,
            SOURCE_BINDINGS_ENVIRONMENT_VARIABLE: str(SANDBOX_WORKSPACE_PATH / SOURCE_BINDINGS_RELATIVE),
            SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE: bindings_sha256,
        }
        if set(environment) != _EXPECTED_ENVIRONMENT_KEYS or environment != expected:
            raise ReleaseContractError("release-suite-executor-environment-untrusted", "suite environment differs from fixed sandbox values")
        # Reinspect immediately before execution.  A digest is immutable, but
        # this preserves the N manifest/context binding observed at admission.
        current_selection = _selector_binding(
            self.root,
            type("Candidate", (), {"authority": type("Authority", (), {
                "executing_release": self.executing_release,
            })(), "manifest": type("Manifest", (), {
                "candidate_release": self.selected_n_image.candidate_release,
            })()})(),
        )
        if replace(self.selected_n_image, image_path=None) != current_selection:
            raise ReleaseContractError("release-suite-executor-n-stale", "executing N selector changed after admission")
        if _inspect_bound_n_image(self.docker, self.root, self.selected_n_image) != self.selected_n_image:
            raise ReleaseContractError("release-suite-executor-n-stale", "executing N image labels changed after admission")

    def run(
        self,
        command: tuple[str, ...],
        *,
        workspace: Path,
        output_root: Path,
        working_directory: str,
        environment: dict[str, str],
        timeout_seconds: float,
    ) -> SuiteExecutionResult:
        self._validate_invocation(command, workspace, output_root, working_directory, environment, timeout_seconds)
        attempt_name = _attempt_mounts(self.root, self.candidate_snapshot_manifest_sha256, workspace, output_root)
        _prepare_executor_scratch(workspace)
        cidfile = output_root / "container.cid"
        if cidfile.exists() or cidfile.is_symlink():
            raise ReleaseContractError("release-suite-executor-output-unsafe", "suite output already has a container identity carrier")
        _preflight_installed_python(self.docker, self.root, self.image_digest, command[0])
        working = str(SANDBOX_WORKSPACE_PATH if working_directory == "."
                      else SANDBOX_WORKSPACE_PATH / working_directory)
        argv = (
            "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges", "--pids-limit=128",
            "--tmpfs", f"/tmp:rw,nosuid,nodev,exec,size={_SANDBOX_TMPFS_SIZE},mode=1777",
            "--tmpfs", f"{SANDBOX_WORKSPACE_PATH / _EXECUTOR_SCRATCH_RELATIVE}:rw,nosuid,nodev,exec,size={_SANDBOX_TMPFS_SIZE},mode=1777",
            "--label", f"{_SUITE_LABEL}={self.candidate_snapshot_manifest_sha256}",
            "--label", f"{_ATTEMPT_LABEL}={attempt_name}",
            "--cidfile", str(cidfile),
            "--mount", f"type=bind,src={workspace},dst={SANDBOX_WORKSPACE_PATH},readonly",
            "--mount", f"type=bind,src={output_root},dst={SANDBOX_OUTPUT_PATH}",
            "--workdir", working,
            # The inspected image Python is PID 1.  It receives only the
            # executor-owned guard, captured deadline and equality-checked
            # sealed argv; the guard never invokes a shell.
            "--entrypoint", command[0],
            "--env", f"PATH={environment['PATH']}",
            "--env", f"{PROJECT_ROOT_ENVIRONMENT_VARIABLE}={environment[PROJECT_ROOT_ENVIRONMENT_VARIABLE]}",
            "--env", f"{REPORT_ENVIRONMENT_VARIABLE}={environment[REPORT_ENVIRONMENT_VARIABLE]}",
            "--env", f"{COMPILED_ROOT_ENVIRONMENT_VARIABLE}={environment[COMPILED_ROOT_ENVIRONMENT_VARIABLE]}",
            "--env", f"{CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE}={environment[CANDIDATE_MANIFEST_ENVIRONMENT_VARIABLE]}",
            "--env", f"{SOURCE_BINDINGS_ENVIRONMENT_VARIABLE}={environment[SOURCE_BINDINGS_ENVIRONMENT_VARIABLE]}",
            "--env", f"{SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE}={environment[SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE]}",
            self.image_digest,
            "-c", _DEADLINE_GUARD, str(timeout_seconds), "--", *command,
        )
        observed = self.docker.run(argv, cwd=self.root, timeout_seconds=timeout_seconds)
        # A missing exit status is equally non-terminal: the Docker CLI may
        # have been interrupted before it could report the daemon-side state.
        # Do not let that ambiguity flow into a coverage pass.
        if observed.timed_out or observed.exit_code is None:
            cleaned = _cleanup_timed_out_container(
                self.docker,
                self.root,
                cidfile,
                candidate_sha=self.candidate_snapshot_manifest_sha256,
                attempt_name=attempt_name,
            )
            return SuiteExecutionResult(
                None,
                observed.stdout,
                observed.stderr,
                timed_out=observed.timed_out,
                left_descendants=not cleaned,
            )
        return SuiteExecutionResult(observed.exit_code, observed.stdout, observed.stderr)


def installed_n_suite_executor(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation,
    *,
    project_root: str,
    docker: DockerExecutor,
) -> InstalledNSuiteDockerExecutor:
    """Derive the only admitted executor from retained selected-Run state."""

    if not isinstance(candidate, ValidatedCandidate) or not isinstance(compilation, SealedCandidateCompilation):
        raise ReleaseContractError("release-suite-executor-handoff-untrusted", "suite executor requires typed candidate and compilation")
    root = Path(project_root).resolve(strict=True)
    if str(root) != candidate.project_root or not callable(getattr(docker, "run", None)):
        raise ReleaseContractError("release-suite-executor-unadmitted", "suite executor is not bound to the selected Project Run")
    if compilation.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256 or compilation.authority != candidate.authority:
        raise ReleaseContractError("release-suite-executor-binding-mismatch", "compiled candidate differs from selected suite candidate")
    _active_n_state(root, candidate)
    binding = _selector_binding(root, candidate)
    binding = _inspect_bound_n_image(docker, root, binding)
    if binding.image_path is None:
        raise ReleaseContractError("release-suite-executor-n-unproven", "executing N image PATH is absent")
    environment = candidate.manifest.full_suite_environment
    require_declared_suite_command(environment)
    return InstalledNSuiteDockerExecutor(
        root=root,
        docker=docker,
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        executing_release=binding.executing_release,
        image_digest=binding.image_digest,
        source_context_sha256=binding.source_context_sha256,
        selected_n_image=binding,
        image_path=binding.image_path,
        sealed_command=tuple(environment.command),
        sealed_working_directory=environment.working_directory,
        compiled_root=compilation.child_materialization_root,
    )


__all__ = ["InstalledNSuiteDockerExecutor", "SelectedNImageBinding", "installed_n_suite_executor"]
