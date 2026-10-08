"""Disposable Release-host inputs for the mandatory Docker E2E harness.

This is deliberately a fixture helper, not a fourth E2E harness.  Its caller
owns the existing ``test_docker_e2e.py`` opt-in/context gate.  The helper only
materializes a source-pinned private Project, starts the fixed local
release-host worker, and builds exact MCP request carriers.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from typing import Any, Mapping


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
RELEASE_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION"
TOOLS_ROOT = RELEASE_ROOT.parent
MCP_ROOT = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
RELEASE_TESTS = RELEASE_ROOT / "tests"
BASE_REVISE_BINDINGS = ROOT / (
    "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/"
    "RMED_ATOM_REVIEW/source_bindings.json"
)
for _location in (APP, TOOLS_ROOT, RELEASE_ROOT, MCP_ROOT, RELEASE_TESTS):
    if str(_location) not in sys.path:
        sys.path.insert(0, str(_location))

from release_compilation import build_preflight_validated_candidate  # noqa: E402
from release_e2e_golden.fixture import (  # noqa: E402
    _PAYLOAD,
    SUITE_DRIVER_COMMAND,
    _copy_canonical_and_control_closure,
    _selector_bytes,
    _write_engine_seed,
    _write_new,
)
from release_handoff import CURRENT_SELECTOR_RELATIVE  # noqa: E402
from selected_routes import canonical_digest, load_selected_manifest  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from workflow_run_support import _canonical_digest  # noqa: E402
import release_host_bridge  # noqa: E402


RUN_ID = "release-recovery-host-e2e"
REQUEST_ID = "release-recovery-host-e2e-request"
_READY_TIMEOUT_SECONDS = 30.0


class ReleaseRecoveryFixtureError(RuntimeError):
    """The scoped fixture cannot establish the required real host boundary."""


def _copy_interpreter(root: Path) -> Path:
    """Expose the exact fixed host-test runtime through the disposable layout.

    The configured interpreter is a virtual-environment launcher: linking only
    its binary loses that environment's ``pyvenv.cfg`` and site-packages once
    Python resolves it beneath the disposable Project.  A read-only link to
    the current complete host-test runtime preserves the required interpreter
    identity and dependencies without copying or mutating an installed runtime.
    """
    source = ROOT / release_host_bridge.FIXED_INTERPRETER
    runtime = source.parents[1]
    if not source.exists() or not source.is_file() or not (runtime / "pyvenv.cfg").is_file():
        raise ReleaseRecoveryFixtureError("the required host-test interpreter is unavailable")
    destination_runtime = root / ".caprmedio_runtime/host-tests"
    destination_runtime.parent.mkdir(parents=True, exist_ok=True)
    if destination_runtime.exists() or destination_runtime.is_symlink():
        raise ReleaseRecoveryFixtureError("the disposable fixed interpreter path is already occupied")
    destination_runtime.symlink_to(runtime, target_is_directory=True)
    destination = root / release_host_bridge.FIXED_INTERPRETER
    if not destination.is_file():
        raise ReleaseRecoveryFixtureError("the disposable fixed interpreter link is unavailable")
    return destination


_FAULT_ENVIRONMENT = "CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT"
_POST_EFFECT_FAULT = "effect-action-once"
_BEFORE_EFFECT_ADMISSION_FAULT = "before-effect-admission-block"
_DURABLE_IN_PROGRESS_FAULT = "durable-in-progress-block"
_FAULTS = frozenset({_POST_EFFECT_FAULT, _BEFORE_EFFECT_ADMISSION_FAULT, _DURABLE_IN_PROGRESS_FAULT})
_FAULT_MARKERS = {
    _BEFORE_EFFECT_ADMISSION_FAULT: "before-effect-admission.ready",
    _DURABLE_IN_PROGRESS_FAULT: "durable-in-progress.ready",
}


def _fault_sitecustomize(directory: Path) -> None:
    """Install bounded fixture-only faults at real Release execution boundaries.

    ``effect-action-once`` preserves the existing real shared-writer OSError:
    it never fabricates a pending event.  The two barrier faults only stop the
    disposable worker: one is before the private Release Action body and the
    other is immediately after its actual durable in-progress checkpoint.
    Neither barrier manufactures a canonical event or permits continuation.
    """
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "sitecustomize.py").write_text(
        """import os
import pathlib
import time

fault = os.environ.get("CAPRMEDIO_TEST_RELEASE_RECORDING_FAULT")
root = pathlib.Path(os.environ.get("CAPRMEDIO_TEST_RELEASE_FAULT_ROOT", ""))

def _marker(name):
    if not root.is_dir():
        raise RuntimeError("fixture fault root is unavailable")
    path = root / name
    path.write_text("ready\\n", encoding="ascii")
    # The test terminates this disposable worker.  A return would admit a real
    # effect, so expiry is a deterministic test-only refusal instead.
    time.sleep(60)
    raise RuntimeError("fixture fault barrier was not terminated")

if fault == "before-effect-admission-block":
    # The selected provider imports this callable by value, so wrap its live
    # dispatch binding rather than only release_actions.execute_release_action.
    import selected_native_providers
    _real_execute = selected_native_providers.execute_release_action
    _fired = False

    def _before_admission(*args, **kwargs):
        global _fired
        if not _fired:
            _fired = True
            _marker("before-effect-admission.ready")
        return _real_execute(*args, **kwargs)

    selected_native_providers.execute_release_action = _before_admission
elif fault == "durable-in-progress-block":
    import release_actions
    _real_checkpoint = release_actions._checkpoint
    _fired = False

    def _after_durable_checkpoint(run, *, index, context, result=None):
        global _fired
        value = _real_checkpoint(run, index=index, context=context, result=result)
        if not _fired and result is None and release_actions.PHASES[index][2] == "deliver_sources":
            _fired = True
            _marker("durable-in-progress.ready")
        return value

    release_actions._checkpoint = _after_durable_checkpoint
elif fault == "effect-action-once":
    import work_journal

    _real_append = work_journal.append_sealed_events
    _fired = False

    def _append_once(root, events, **kwargs):
        global _fired
        if not _fired and len(events) == 1:
            event = events[0]
            run = event.get("run", {}) if isinstance(event, dict) else {}
            if (event.get("event") == "completed" and run.get("kind") == "action"
                    and bool(event.get("effect_refs"))):
                _fired = True
                raise OSError("fixture-only shared Journal terminal write failure")
        return _real_append(root, events, **kwargs)

    work_journal.append_sealed_events = _append_once
""",
        encoding="utf-8",
    )


def _copy_runtime_readiness_definition(root: Path) -> None:
    """Retain the unrelated CA-O-104 input required by worker readiness.

    Release execution itself is governed by its selected source closure, but
    the existing worker's production fingerprint also reads the Base Revise
    CA-O-104 source before it advertises readiness.  Copy the exact pinned
    bytes into this disposable Project rather than borrowing a real Project
    authority or weakening the ready/fingerprint check.
    """
    try:
        bindings = json.loads(BASE_REVISE_BINDINGS.read_text(encoding="utf-8"))
        definition = next(
            row for row in bindings["sources"]
            if isinstance(row, Mapping) and row.get("atom_id") == "CA-O-104"
        )
        relative = Path(definition["path"])
        expected = definition["sha256"]
    except (KeyError, OSError, StopIteration, TypeError, ValueError) as error:
        raise ReleaseRecoveryFixtureError("the current CA-O-104 readiness binding is unavailable") from error
    if (relative.is_absolute() or ".." in relative.parts or not expected
            or len(expected) != 64 or not all(character in "0123456789abcdef" for character in expected)):
        raise ReleaseRecoveryFixtureError("the current CA-O-104 readiness binding is invalid")
    source = ROOT / relative
    if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
        raise ReleaseRecoveryFixtureError("the current CA-O-104 readiness source is stale")
    destination = root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if hashlib.sha256(destination.read_bytes()).hexdigest() != expected:
        raise ReleaseRecoveryFixtureError("the copied CA-O-104 readiness source is invalid")


def _materialize_release_host_project(root: Path) -> Any:
    """Build a current disposable pre-delivery candidate without seeding effects.

    The golden fixture normally pre-seeds the derived source tree and compiled
    child so its receipt readers can inspect fixtures.  That would make the
    delivery Action a no-op here.  This bounded variant reuses its source and
    engine setup, retains the worker's CA-O-104 fingerprint input *before*
    candidate sealing, and leaves the delivery target absent for the actual
    Release Action to create.
    """
    _copy_canonical_and_control_closure(root)
    _copy_runtime_readiness_definition(root)
    _write_engine_seed(root)
    _write_new(root / CURRENT_SELECTOR_RELATIVE, _selector_bytes("N"))
    _preflight, candidate = build_preflight_validated_candidate(
        root,
        candidate_release=_PAYLOAD["candidate_release"],
        full_suite_environment={
            "runner": "local-subprocess",
            "command": list(SUITE_DRIVER_COMMAND),
            "working_directory": ".",
        },
        candidate_image_reference="mock-data-only-presealed-candidate",
    )
    return candidate


def _requested_runs(root: Path, manifest: Mapping[str, Any], run_id: str,
                    parameters: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Ask the production graph validator to produce the sealed Run plan."""
    execution = {
        "mode": "execute",
        "operation_route": "release_version",
        "definition_manifest": {
            "manifest_ref": manifest["manifest_ref"],
            "manifest_digest": manifest["canonical_manifest_sha256"],
        },
        "source_freshness": manifest["source_freshness"],
    }
    graph = SelectedExecution(root)._validate_graph(execution)
    limits = parameters.get("run_visit_limits")
    return SelectedExecution.build_requested_runs(graph, run_id, limits)


@dataclass
class ReleaseRecoveryDockerFixture:
    """One independent Release-host worker and one source-pinned Project."""

    root: Path
    interpreter: Path
    fault_import_root: Path
    candidate: Any
    worker: subprocess.Popen[bytes] | None = None

    @classmethod
    def create(cls, scratch_root: Path) -> "ReleaseRecoveryDockerFixture":
        parent = scratch_root / "docker-e2e-release-recovery"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(prefix="release-host-", dir=parent)).resolve()
        try:
            candidate = _materialize_release_host_project(root)
            (root / ".git").mkdir(exist_ok=True)
            (root / ".caprmedio_caprmedio/_journal").mkdir(exist_ok=True)
            interpreter = _copy_interpreter(root)
            fault_import_root = root / ".caprmedio_tmp/release-recovery-fault"
            _fault_sitecustomize(fault_import_root)
            return cls(root, interpreter, fault_import_root, candidate)
        except BaseException:
            shutil.rmtree(root, ignore_errors=True)
            raise

    def cleanup(self) -> None:
        self.stop_worker()
        if os.environ.get("CAPRMEDIO_KEEP_DOCKER_FIXTURES") != "1":
            shutil.rmtree(self.root, ignore_errors=True)

    def environment(self, *, fault: str | bool | None = None) -> dict[str, str]:
        environment = dict(os.environ)
        environment.pop("CAPRMEDIO_RUNTIME_NAMESPACE", None)
        environment.pop("CAPRMEDIO_AGENT_MODE", None)
        existing = environment.get("PYTHONPATH")
        environment["PYTHONPATH"] = os.pathsep.join(
            part for part in (str(self.fault_import_root), str(TOOLS_ROOT), existing) if part
        )
        if fault is True:  # preserve the existing live post-effect test call shape
            fault = _POST_EFFECT_FAULT
        elif fault is False:
            fault = None
        if fault is not None and fault not in _FAULTS:
            raise ReleaseRecoveryFixtureError(f"unsupported fixture fault: {fault}")
        environment.pop(_FAULT_ENVIRONMENT, None)
        environment.pop("CAPRMEDIO_TEST_RELEASE_FAULT_ROOT", None)
        if fault is not None:
            environment[_FAULT_ENVIRONMENT] = fault
            environment["CAPRMEDIO_TEST_RELEASE_FAULT_ROOT"] = str(self.fault_import_root)
        return environment

    def mcp_parameters(self, *, fault: str | bool | None = None):
        from mcp import StdioServerParameters

        return StdioServerParameters(
            command=str(self.interpreter),
            args=[str(MCP_ROOT / "implementation_server.py"), "--project-root", str(self.root)],
            env=self.environment(fault=fault),
            cwd=self.root,
        )

    def start_worker(self, *, fault: str | bool | None = None) -> None:
        self.stop_worker()
        if isinstance(fault, str) and fault in _FAULT_MARKERS:
            marker = self.fault_marker(fault)
            if marker.exists() or marker.is_symlink():
                marker.unlink()
        command = [str(self.interpreter), str(APP / "orchestrator.py"), "--project-root", str(self.root), "release-worker"]
        directory = self.root / ".caprmedio_install/workflow_orchestrator/release-host"
        directory.mkdir(parents=True, exist_ok=True)
        log = (directory / "worker.log").open("ab")
        try:
            self.worker = subprocess.Popen(
                command,
                cwd=self.root,
                env=self.environment(fault=fault),
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=log,
                start_new_session=True,
            )
        finally:
            log.close()
        self.wait_ready()

    def fault_marker(self, fault: str) -> Path:
        """Return the private marker for a blocking fixture fault only."""
        if fault not in _FAULT_MARKERS:
            raise ReleaseRecoveryFixtureError(f"fixture fault has no barrier marker: {fault}")
        return self.fault_import_root / _FAULT_MARKERS[fault]

    def wait_for_fault_marker(self, fault: str) -> Path:
        marker = self.fault_marker(fault)
        deadline = time.monotonic() + _READY_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            if self.worker is not None and self.worker.poll() is not None:
                raise ReleaseRecoveryFixtureError(self._worker_failure("release host stopped before fixture fault barrier"))
            if marker.is_file() and not marker.is_symlink() and marker.read_bytes() == b"ready\n":
                return marker
            time.sleep(0.1)
        raise ReleaseRecoveryFixtureError(self._worker_failure("release host did not reach fixture fault barrier"))

    def wait_ready(self) -> dict[str, Any]:
        ready = self.root / release_host_bridge.READY
        deadline = time.monotonic() + _READY_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            if self.worker is not None and self.worker.poll() is not None:
                raise ReleaseRecoveryFixtureError(self._worker_failure("release host stopped before readiness"))
            if ready.is_file():
                try:
                    available = release_host_bridge.availability(self.root)
                except (OSError, RuntimeError, ValueError):
                    time.sleep(0.1)
                    continue
                return available
            time.sleep(0.1)
        raise ReleaseRecoveryFixtureError(self._worker_failure("release host did not become ready"))

    def _worker_failure(self, reason: str) -> str:
        log = self.root / ".caprmedio_install/workflow_orchestrator/release-host/worker.log"
        output = log.read_text(encoding="utf-8", errors="replace")[-4000:] if log.is_file() else ""
        return f"{reason}: {output}"

    def stop_worker(self) -> None:
        worker = self.worker
        self.worker = None
        if worker is None or worker.poll() is not None:
            return
        try:
            os.killpg(worker.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            worker.wait(timeout=15)
        except subprocess.TimeoutExpired:
            os.killpg(worker.pid, signal.SIGKILL)
            worker.wait(timeout=15)

    def preview_request(self) -> dict[str, Any]:
        manifest = load_selected_manifest(self.root)
        source = manifest["source_freshness"]
        candidate = self.candidate.manifest.model_dump(mode="json", by_alias=True)
        parameters = {
            "operation": "apply",
            "project_root": str(self.root),
            "candidateSnapshotManifest": candidate,
            "expected_executing_release": candidate["executing_release"],
            "expected_project_structure_digest": candidate["project_structure_digest"],
            "expected_framework_settings_digest": candidate["framework_settings_digest"],
            "expected_source_frontier_digest": candidate["source_frontier_digest"],
            "run_receipt_refs": ["release-recovery-host-e2e:admission"],
        }
        target = [
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
            "CA-O-164-PROJECT_CONFIGURATION-WORKFLOW--release-a-selected-framework-version.md"
        ]
        effects = [{"type": "release_version"}]
        return {
            "operation_route": "release_version",
            "mode": "preview",
            "request_id": REQUEST_ID,
            "parameters": parameters,
            "parameters_digest": canonical_digest(parameters),
            "target_frontier": target,
            "target_frontier_digest": canonical_digest(target),
            "effects": effects,
            "effects_digest": canonical_digest(effects),
            "definition_manifest": {
                "manifest_ref": manifest["manifest_ref"],
                "manifest_digest": manifest["canonical_manifest_sha256"],
            },
            "source_freshness": source,
            "initiative": {
                "initiative_id": "CA-P-1716",
                "instruction_summary": "bounded disposable Release recovery proof",
                "initiative_ref": "fixture/release-recovery-host-e2e",
            },
        }

    def execute_request(self, preview: Mapping[str, Any]) -> dict[str, Any]:
        if preview.get("disposition") != "preview":
            raise ReleaseRecoveryFixtureError(f"Release preview was not admitted: {preview}")
        request = self.preview_request()
        manifest = load_selected_manifest(self.root)
        request.update({
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "release-recovery-host-e2e-operator",
            "requested_runs": _requested_runs(self.root, manifest, RUN_ID, request["parameters"]),
        })
        request["operator_authorization"] = {
            "authorization_ref": "fixture/release-recovery-host-e2e",
            "authorization_freshness": {
                "state": "current",
                "digest": hashlib.sha256(b"release-recovery-host-e2e").hexdigest(),
            },
            "request_id": request["request_id"],
            "operation_route": request["operation_route"],
            "proposal_receipt_digest": request["proposal_receipt_digest"],
            "parameters_digest": request["parameters_digest"],
            "target_frontier_digest": request["target_frontier_digest"],
            "effects_digest": request["effects_digest"],
            "definition_manifest": request["definition_manifest"],
            "source_freshness": request["source_freshness"],
        }
        return request

    def request_identity(self) -> str:
        """The shared selected-run identity, recomputed from retained request bytes."""
        frozen = json.loads((self.root / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID /
                             "selected_request.json").read_text(encoding="utf-8"))
        execution = frozen["request"]["execution"]
        return _canonical_digest(execution)

    def release_workflow_source(self) -> Path:
        route = next(
            entry for entry in load_selected_manifest(self.root)["routes"]
            if entry.get("route") == "release_version"
        )
        return self.root / route["workflow"]["source_path"]

    @staticmethod
    def content_digest(path: Path) -> str:
        """Hash a recorded effect's full file or directory content.

        Source delivery records a source-copy directory, not necessarily a
        single file.  Hashing its tree gives the recovery assertion a concrete
        no-replay observation without assuming a particular effect shape.
        """
        if path.is_file():
            return hashlib.sha256(path.read_bytes()).hexdigest()
        if path.is_dir():
            digest = hashlib.sha256()
            for member in sorted(path.rglob("*")):
                if member.is_file():
                    digest.update(member.relative_to(path).as_posix().encode("utf-8"))
                    digest.update(b"\\0")
                    digest.update(member.read_bytes())
                    digest.update(b"\\0")
            return digest.hexdigest()
        raise ReleaseRecoveryFixtureError(f"effect reference does not resolve to a file or directory: {path}")

    def pending_events(self) -> list[Path]:
        path = self.root / ".caprmedio_runtime/state/work_journal/pending"
        return sorted(path.glob("*.json")) if path.is_dir() else []

    def pending_event_ids(self) -> list[str]:
        """Return only the retained sealed event identities.

        A resumed Release graph may safely create a later, unrelated pending
        carrier.  Callers therefore track the original effect-bearing event
        by identity rather than treating every later carrier as a replay.
        """
        event_ids: list[str] = []
        for path in self.pending_events():
            payload = json.loads(path.read_text(encoding="utf-8"))
            event_id = payload.get("event_id")
            if not isinstance(event_id, str) or not event_id:
                raise ReleaseRecoveryFixtureError(f"invalid pending event carrier: {path}")
            event_ids.append(event_id)
        return event_ids

    def selected_result(self) -> dict[str, Any] | None:
        """Read the retained selected-run result without a second queue call.

        The actual execute and recover paths remain local-MCP requests.  This
        narrow file read avoids asking a recovering DBOS queue to synchronously
        serve a status request while it is progressing beyond the recovered
        terminal record.
        """
        path = (self.root / ".caprmedio_install/workflow_orchestrator/runs" / RUN_ID /
                "accepted.json")
        if not path.is_file():
            return None
        payload = json.loads(path.read_text(encoding="utf-8"))
        result = payload.get("result") if isinstance(payload, Mapping) else None
        if not isinstance(result, dict):
            raise ReleaseRecoveryFixtureError(f"invalid selected result carrier: {path}")
        return result

    def journal_events(self) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []
        journal = self.root / ".caprmedio_caprmedio/_journal"
        for path in sorted(journal.glob("*.ndjson")):
            events.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line)
        return events
