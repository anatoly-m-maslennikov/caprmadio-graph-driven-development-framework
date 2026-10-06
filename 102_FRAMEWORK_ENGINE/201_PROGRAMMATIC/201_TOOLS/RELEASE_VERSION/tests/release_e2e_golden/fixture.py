"""Presealed, non-publishing golden data for the private Release E2E tests.

This module deliberately builds only a disposable Project-shaped scratch tree.
It does not call a renderer, package staging, Docker, Git, publication, or
cleanup.  The receipts are labelled mock data, while their readers are the
real source-bound Release readers; this keeps negative receipt/source mutation
tests meaningful without asserting a production image or promotion happened.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import hashlib
import json
import os
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


RELEASE_ROOT = Path(__file__).resolve().parents[2]
REPOSITORY_ROOT = RELEASE_ROOT.parents[3]
MCP_ROOT = REPOSITORY_ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
for _path in (RELEASE_ROOT, MCP_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from release_compilation import build_preflight_validated_candidate  # noqa: E402
from release_contract import ValidatedCandidate, canonical_json  # noqa: E402
from release_handoff import (  # noqa: E402
    CANONICAL_SOURCE_RELATIVE,
    COMPILER_ENTRYPOINT_RELATIVE,
    CURRENT_SELECTOR_RELATIVE,
    DERIVED_SOURCE_COPY_RELATIVE,
    MATERIALIZED_RELATIVE,
    CompilerSuccessEvidence,
    SealedCandidateCompilation,
    seal_candidate_compilation,
    validate_source_copy,
)
from release_image import (  # noqa: E402
    CANDIDATE_LABEL,
    CONTEXT_LABEL,
    IMAGE_ROOT,
    ImageBuildEvidence,
    ImageVerificationEvidence,
    _context as materialize_image_context,
    _tree as image_tree,
    verify_bound_image_evidence,
)
from release_packaging import RUNTIME_ROOT, _render_manifest  # noqa: E402
from release_suite import (  # noqa: E402
    COMPILED_PROBE_TEST_MODULE,
    EVIDENCE_ROOT,
    MODULE_RULES_RELATIVE,
    REQUIRED_COVERAGE,
    SUITE_DRIVER_COMMAND,
    SuiteGateEvidence,
    _active_n_state,
    _context_receipt,
    _source_bindings_bytes,
    verify_bound_suite_evidence,
)
from release_suite_reference_context import capture_context  # noqa: E402
from release_test_phases import derive_test_phase_map_from_rows  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402


_PAYLOAD = json.loads((Path(__file__).with_name("payloads.json")).read_bytes())
MOCK_DATA_LABEL = _PAYLOAD["fixture_kind"]
CANDIDATE_IMAGE_DIGEST = _PAYLOAD["candidate_image_digest"]
# Kept only for old static imports.  The authoritative fixture identity is
# ``fixture.candidate.manifest.sha256`` and is rebuilt from sealed local bytes.
CANDIDATE_MANIFEST_SHA256 = _PAYLOAD["candidate_snapshot_manifest_sha256"]
HARNESS_BASENAMES = tuple(_PAYLOAD["harnesses"])
HARNESS_PATHS = tuple(_PAYLOAD["harness_paths"])
UNIT_MODULE = _PAYLOAD["unit_module"]


@dataclass(frozen=True)
class SnapshotEntry:
    """A complete byte-and-mode manifest for one scratch-tree observation."""

    path: str
    sha256: str
    mode: int


@dataclass(frozen=True)
class GoldenE2EFixture:
    """Typed, presealed fixture objects plus before/after byte snapshots."""

    root: Path
    candidate: ValidatedCandidate
    compilation: SealedCandidateCompilation
    unit_suite: SuiteGateEvidence
    image_build: ImageBuildEvidence
    image: ImageVerificationEvidence
    before_snapshot: tuple[SnapshotEntry, ...]
    after_snapshot: tuple[SnapshotEntry, ...]
    fixture_kind: str = MOCK_DATA_LABEL

    @property
    def before(self) -> tuple[SnapshotEntry, ...]:
        return self.before_snapshot

    @property
    def after(self) -> tuple[SnapshotEntry, ...]:
        return self.after_snapshot

    def verify_receipts(self) -> Path:
        """Run the real, read-only suite and image receipt readers."""

        verify_bound_suite_evidence(self.candidate, self.compilation, self.unit_suite)
        return verify_bound_image_evidence(
            self.candidate, self.compilation, self.unit_suite, self.image_build, self.image,
        )


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write_new(path: Path, payload: bytes, mode: int = 0o644) -> None:
    """Create exactly one regular file; fixture setup never overwrites bytes."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)


def _copy_exact(root: Path, relative: str, source: Path | None = None) -> None:
    source = source or REPOSITORY_ROOT / relative
    if source.is_symlink() or not source.is_file():
        raise RuntimeError(f"fixture source is not a regular file: {relative}")
    target = root / relative
    payload, mode = source.read_bytes(), source.stat().st_mode & 0o777
    if target.exists():
        if target.is_symlink() or not target.is_file() or target.read_bytes() != payload or target.stat().st_mode & 0o777 != mode:
            raise RuntimeError(f"fixture source conflicts with retained bytes: {relative}")
        return
    _write_new(target, payload, mode)


def _retained_source(relative: str, expected_digest: str | None) -> Path:
    """Choose current bytes, or an already-retained predecessor archive by hash."""

    source = REPOSITORY_ROOT / relative
    if source.is_file() and not source.is_symlink() and (expected_digest is None or _digest(source.read_bytes()) == expected_digest):
        return source
    archive = source.parent / "archive"
    if archive.is_dir() and not archive.is_symlink():
        for candidate in sorted(archive.rglob("*")):
            if candidate.is_file() and not candidate.is_symlink() and _digest(candidate.read_bytes()) == expected_digest:
                return candidate
    raise RuntimeError(f"fixture has no retained byte carrier for pinned source: {relative}")


def _copy_canonical_and_control_closure(root: Path) -> None:
    """Copy current source/controls before preflight, preserving their modes."""

    # Reuse the bounded full-suite closure: it retains D580's exactly declared
    # two Prompt binding carriers and each carrier's explicit source pins.
    copy_control_closure(REPOSITORY_ROOT, root)
    for relative in (
        f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
        f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
    ):
        _copy_exact(root, relative, _retained_source(relative, None))
    # The compiler governs three structural layers even where this tiny
    # fixture intentionally carries no installed-extension source atom.
    for layer in ("001_CORE_META_MODEL", "002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION"):
        (root / CANONICAL_SOURCE_RELATIVE / layer).mkdir(parents=True, exist_ok=True)


def _write_engine_seed(root: Path) -> None:
    """Seed just the complete package carriers needed by the typed gates."""

    content = {
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py": b"# mock fixture tool\n",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py": b"# mock fixture app\n",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py": b"# mock fixture mcp\n",
        "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md": b"# mock fixture prompt\n",
        "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md": b"# mock fixture ca skill\n",
        "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml": b"name: mock-ca\n",
        "pyproject.toml": b"[project]\nname = 'release-e2e-golden'\nversion = '0'\n",
        "uv.lock": b"version = 1\n",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile": b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n",
    }
    for relative, payload in content.items():
        _write_new(root / relative, payload)
    _write_new(root / UNIT_MODULE, b"def test_mock_fixture() -> None:\n    assert True\n")
    for relative in HARNESS_PATHS:
        # D572 admits the actual harness bytes.  Only their retained command
        # observations are synthetic; no harness execution occurs here.
        _copy_exact(root, relative)
    for relative in (
        COMPILER_ENTRYPOINT_RELATIVE,
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_suite.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_e2e_bindings.json",
    ):
        _copy_exact(root, relative)


def _module_rules() -> bytes:
    probes = {
        UNIT_MODULE: [
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml",
        ],
    }
    rows = []
    for module in sorted(probes):
        row: dict[str, object] = {"test_module_source_path": module, "source_paths": sorted(probes[module])}
        if module == COMPILED_PROBE_TEST_MODULE:
            row["compiled_candidate_probe"] = True
        rows.append(row)
    return canonical_json({"schema_version": 1, "module_probes": rows})


def _seed_derived_and_compilation(root: Path) -> tuple[ValidatedCandidate, SealedCandidateCompilation]:
    """Use preflight bytes plus normal creates; never call the renderer."""

    preflight, candidate = build_preflight_validated_candidate(
        root,
        candidate_release=_PAYLOAD["candidate_release"],
        full_suite_environment={
            "runner": "local-subprocess", "command": list(SUITE_DRIVER_COMMAND), "working_directory": ".",
        },
        candidate_image_reference="mock-data-only-presealed-candidate",
    )
    canonical = root / CANONICAL_SOURCE_RELATIVE
    for source in sorted(canonical.rglob("*")):
        if source.is_file() and not source.is_symlink():
            relative = source.relative_to(canonical).as_posix()
            _write_new(root / DERIVED_SOURCE_COPY_RELATIVE / relative, source.read_bytes(), source.stat().st_mode & 0o777)
    materialized = root / MATERIALIZED_RELATIVE / candidate.manifest.sha256
    for relative, payload in preflight.output_files.items():
        _write_new(materialized / relative, payload)
    _write_new(materialized / "_release_manifest.json", preflight.child_manifest_bytes)
    source_copy = validate_source_copy(candidate)
    evidence = CompilerSuccessEvidence(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        outcome="completed",
        compiler_entrypoint=preflight.compiler_entrypoint,
        compiler_frontier_digest=preflight.compiler_frontier_digest,
        child_materialization_root=materialized.relative_to(root).as_posix(),
        actual_compiled_output_sha256=preflight.expected_compiled_output_sha256,
    )
    return candidate, seal_candidate_compilation(source_copy, evidence)


def _selector_bytes(release: str) -> bytes:
    return f'release = "{release}"\n'.encode()


def _seed_active_n(root: Path, candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> None:
    """Retain N and candidate byte carriers without calling the staging producer."""

    for identity in (candidate.authority.executing_release, candidate.manifest.sha256):
        package = root / RUNTIME_ROOT / "releases" / identity
        for row in compilation.package_rows:
            source = root / row.source_path
            _write_new(package / row.destination_path, source.read_bytes(), row.mode)
            if identity == candidate.authority.executing_release and row.resource == "SKILL":
                public = root / ".agents/skills/ca" / row.destination_path.removeprefix("SKILLS/ca/")
                _write_new(public, source.read_bytes(), row.mode)
        _write_new(package / "manifest.toml", _render_manifest(identity, compilation.package_rows).encode())
    selector_path = root / ".caprmedio_runtime/framework/current.toml"
    if not selector_path.is_file() or selector_path.read_bytes() != _selector_bytes(candidate.authority.executing_release):
        raise RuntimeError("fixture selector must be presealed before candidate construction")


def _coverage_report(root: Path, candidate: ValidatedCandidate, compilation: SealedCandidateCompilation,
                     context, phase_map_sha256: str) -> bytes:
    bindings_sha = _digest(_source_bindings_bytes(
        root, candidate.manifest.sha256, compilation.package_rows, compilation.child_materialization_root, context,
    ))
    rows = {row.source_path: row for row in compilation.package_rows}
    compiled = sorted(
        row.source_path for row in compilation.package_rows
        if row.resource == "METHODOLOGY" and row.source_path.startswith(compilation.child_materialization_root + "/")
    )[0]
    rules = json.loads(_module_rules())
    bindings = {row["test_module_source_path"]: tuple(row["source_paths"]) for row in rules["module_probes"]}
    report = ET.Element("testsuite", {
        "tests": str(len(bindings)), "failures": "0", "errors": "0", "skipped": "0",
        "caprmedio.phase": "unit",
        "caprmedio.phase_map_sha256": phase_map_sha256,
        "caprmedio.control_context_digest": context.control_context_digest,
    })
    for index, module in enumerate(sorted(bindings)):
        case = ET.SubElement(report, "testcase", {"classname": module, "name": f"mock-case-{index}"})
        properties = ET.SubElement(case, "properties")
        ET.SubElement(properties, "property", {"name": "caprmedio.test_id", "value": f"mock-case-{index}"})
        ET.SubElement(properties, "property", {"name": "caprmedio.source_bindings_sha256", "value": bindings_sha})
        sources = (module, *bindings[module], *((compiled,) if module == UNIT_MODULE else ()))
        for source_path in sources:
            row = rows[source_path]
            ET.SubElement(properties, "property", {
                "name": "caprmedio.source_probe",
                "value": canonical_json({"source_path": source_path, "sha256": row.sha256}).decode(),
            })
    return ET.tostring(report, encoding="utf-8")


def _seed_suite(root: Path, candidate: ValidatedCandidate, compilation: SealedCandidateCompilation) -> SuiteGateEvidence:
    bindings = {
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "compiled_candidate_root": compilation.child_materialization_root,
        "selected_n_identity": candidate.authority.executing_release,
        "selected_n_image_context": _PAYLOAD["selected_n_image_context"],
    }
    context = capture_context(root, bindings)
    attempt = root / EVIDENCE_ROOT / candidate.manifest.sha256 / "attempt-mock-data"
    attempt.mkdir(parents=True)
    stdout, stderr = b"MOCK DATA ONLY: sealed Unit Gate receipt\n", b""
    phase_map = derive_test_phase_map_from_rows(compilation.package_rows)
    report = _coverage_report(root, candidate, compilation, context, phase_map.sha256)
    executed_tests = len(list(ET.fromstring(report).iter("testcase")))
    _write_new(attempt / "context.json", _context_receipt(context))
    _write_new(attempt / "stdout.bin", stdout)
    _write_new(attempt / "stderr.bin", stderr)
    _write_new(attempt / "coverage.xml", report)
    selector_sha, package_sha, skill_sha = _active_n_state(root, candidate)
    bare = SuiteGateEvidence(
        candidate.manifest.sha256, "passed", f"{MOCK_DATA_LABEL}: Unit Gate fixture receipt",
        "local-subprocess", tuple(SUITE_DRIVER_COMMAND), ".", 0, executed_tests, tuple(sorted(REQUIRED_COVERAGE)),
        attempt.relative_to(root).as_posix(), _digest(stdout), _digest(stderr), _digest(report),
        selector_sha, package_sha, skill_sha, None, 0.0, context.control_context_digest, phase_map.sha256,
    )
    receipt = canonical_json(asdict(bare))
    _write_new(attempt / "receipt.json", receipt)
    return replace(bare, receipt_sha256=_digest(receipt))


def _command_record(argv: list[str], stdout: bytes, stderr: bytes = b"") -> dict[str, object]:
    return {"argv": argv, "exit_code": 0, "timed_out": False, "stdout_sha256": _digest(stdout), "stderr_sha256": _digest(stderr)}


def _inspect_payload(candidate: ValidatedCandidate, context_sha: str) -> bytes:
    return canonical_json([{"Id": CANDIDATE_IMAGE_DIGEST, "Config": {"Labels": {
        CANDIDATE_LABEL: candidate.manifest.sha256, CONTEXT_LABEL: context_sha,
    }}}])


def _seed_image(
    root: Path, candidate: ValidatedCandidate, compilation: SealedCandidateCompilation, suite: SuiteGateEvidence,
) -> tuple[ImageBuildEvidence, ImageVerificationEvidence]:
    """Materialize deterministic context and mock receipts; no Docker call occurs."""

    build_attempt = root / IMAGE_ROOT / candidate.manifest.sha256 / "build" / "attempt-mock-data"
    build_attempt.mkdir(parents=True)
    context, package_sha = materialize_image_context(root, candidate, compilation, build_attempt)
    context_sha = image_tree(context)
    build_stdout, inspect = b"MOCK DATA ONLY: docker build was not invoked\n", _inspect_payload(candidate, context_sha)
    build_commands = [
        _command_record([
            "docker", "build", "--iidfile", str(build_attempt / "image.id"), "--label",
            f"{CANDIDATE_LABEL}={candidate.manifest.sha256}", "--label", f"{CONTEXT_LABEL}={context_sha}",
            "--file", str(context / "Dockerfile"), str(context),
        ], build_stdout),
        _command_record(["docker", "image", "inspect", CANDIDATE_IMAGE_DIGEST], inspect),
    ]
    for index, command in enumerate(((build_stdout, b""), (inspect, b""))):
        _write_new(build_attempt / f"command-{index}.stdout", command[0])
        _write_new(build_attempt / f"command-{index}.stderr", command[1])
    _write_new(build_attempt / "image.id", (CANDIDATE_IMAGE_DIGEST + "\n").encode())
    build_commands_bytes = canonical_json(build_commands)
    _write_new(build_attempt / "commands.json", build_commands_bytes)
    bare_build = ImageBuildEvidence(
        candidate.manifest.sha256, "built", f"{MOCK_DATA_LABEL}: no Docker build was invoked", CANDIDATE_IMAGE_DIGEST,
        context.relative_to(root).as_posix(), context_sha, package_sha, suite.receipt_sha256,
        build_attempt.relative_to(root).as_posix(), _digest(build_commands_bytes), "docker-subprocess", None,
    )
    build_receipt = canonical_json(asdict(bare_build))
    _write_new(build_attempt / "receipt.json", build_receipt)
    build = replace(bare_build, receipt_sha256=_digest(build_receipt))

    verify_attempt = root / IMAGE_ROOT / candidate.manifest.sha256 / "verify" / "attempt-mock-data"
    verify_attempt.mkdir(parents=True)
    canary = canonical_json({
        "schema": "caprmedio.release_version.image_canary.v1",
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "package_manifest_sha256": package_sha,
        "verified_files": len(compilation.package_rows),
        "mcp_tools": ["get_mcp_reload_status", "query_artifact"],
    })
    run = [
        "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
        "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m", "--entrypoint", "python",
        CANDIDATE_IMAGE_DIGEST, "/opt/caprmedio-release-canary.py",
    ]
    verify_commands = [
        _command_record(["docker", "image", "inspect", CANDIDATE_IMAGE_DIGEST], inspect),
        _command_record(run, canary),
    ]
    for index, command in enumerate(((inspect, b""), (canary, b""))):
        _write_new(verify_attempt / f"command-{index}.stdout", command[0])
        _write_new(verify_attempt / f"command-{index}.stderr", command[1])
    verify_commands_bytes = canonical_json(verify_commands)
    _write_new(verify_attempt / "commands.json", verify_commands_bytes)
    bare_verify = ImageVerificationEvidence(
        candidate.manifest.sha256, "verified", f"{MOCK_DATA_LABEL}: no Docker canary was invoked", CANDIDATE_IMAGE_DIGEST,
        build.receipt_sha256, verify_attempt.relative_to(root).as_posix(), _digest(verify_commands_bytes), "docker-subprocess", None,
    )
    verify_receipt = canonical_json(asdict(bare_verify))
    _write_new(verify_attempt / "receipt.json", verify_receipt)
    return build, replace(bare_verify, receipt_sha256=_digest(verify_receipt))


def _snapshot(root: Path) -> tuple[SnapshotEntry, ...]:
    entries = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink():
            entries.append(SnapshotEntry(path.relative_to(root).as_posix(), _digest(path.read_bytes()), path.stat().st_mode & 0o777))
    return tuple(entries)


def materialize(root: Path | str) -> GoldenE2EFixture:
    """Create a fresh fixture tree by normal creates only, then validate it."""

    root = Path(root).resolve()
    if root.exists() and (root.is_symlink() or not root.is_dir() or any(root.iterdir())):
        raise ValueError("golden fixture root must be an empty regular directory")
    root.mkdir(parents=True, exist_ok=True)
    _copy_canonical_and_control_closure(root)
    _write_engine_seed(root)
    _write_new(root / MODULE_RULES_RELATIVE, _module_rules())
    _write_new(root / CURRENT_SELECTOR_RELATIVE, _selector_bytes("N"))
    candidate, compilation = _seed_derived_and_compilation(root)
    _seed_active_n(root, candidate, compilation)
    before = _snapshot(root)
    suite = _seed_suite(root, candidate, compilation)
    build, image = _seed_image(root, candidate, compilation, suite)
    fixture = GoldenE2EFixture(root, candidate, compilation, suite, build, image, before, _snapshot(root))
    fixture.verify_receipts()
    return fixture


def build_fixture(root: Path | str) -> GoldenE2EFixture:
    """Compatibility alias for callers that name factories as builders."""

    return materialize(root)


__all__ = [
    "CANDIDATE_IMAGE_DIGEST", "CANDIDATE_MANIFEST_SHA256", "GoldenE2EFixture", "HARNESS_BASENAMES",
    "HARNESS_PATHS", "MOCK_DATA_LABEL", "SnapshotEntry", "UNIT_MODULE", "build_fixture", "materialize",
]
