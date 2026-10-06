"""Runtime boundary tests; mocks never need live credentials or paid inference."""

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "docker"))

from runtime_config import control_directory  # noqa: E402
from remote_agent import RemoteAgent  # noqa: E402
from runtime import Runtime  # noqa: E402


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = APP.parents[3] / ".caprmedio_tmp/tests/docker-runtime"
        self.temporary.mkdir(parents=True, exist_ok=True)

    def test_native_and_docker_namespaces_do_not_share_a_queue(self):
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": ""}):
            self.assertEqual(control_directory(), ".caprmedio_install/workflow_orchestrator")
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "docker"}):
            self.assertEqual(control_directory(), ".caprmedio_install/workflow_orchestrator/docker")
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": "../escape"}):
            with self.assertRaises(ValueError):
                control_directory()

    def test_mock_compose_has_no_credential_input_or_published_ports(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            runtime = Runtime(Path(directory), mock=True)
            command = runtime.command("config")
            self.assertIn("--env-file", command)
            self.assertIn("/dev/null", command)
            self.assertNotIn("auth.compose.yaml", " ".join(command))
            self.assertIn("mock.compose.yaml", " ".join(command))
            self.assertNotIn("CAPRMEDIO_CODEX_AUTH_FILE", runtime.environment())

    def test_remote_adapter_bounds_and_validates_output(self):
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                pass

            def read(self, size):
                self.size = size
                return json.dumps(
                    {"report_json": "{}", "candidate_content": None, "confidence": 99.0}
                ).encode()

        response = Response()
        with patch("remote_agent.urlopen", return_value=response) as opening:
            output = RemoteAgent().execute({"bound": True}, "check", Path("."), 10)
        self.assertEqual(output["confidence"], 99.0)
        self.assertEqual(response.size, 8 * 1024 * 1024 + 1)
        self.assertEqual(opening.call_args.kwargs["timeout"], 15)
        payload = json.loads(opening.call_args.args[0].data)
        self.assertEqual(payload, {"context": {"bound": True}, "phase": "check", "timeout": 10})

    def test_routing_does_not_fall_back_when_docker_stops(self):
        from docker_bridge import invoke

        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            path = root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"transport": "docker", "project_name": "caprmedio-test"}))
            with patch("docker_bridge.subprocess.run", side_effect=OSError("unavailable")):
                with self.assertRaisesRegex(RuntimeError, "Docker runtime is unavailable"):
                    invoke(root, {"operation": "status", "run_id": "test"})

    def test_resolved_compose_enforces_service_boundaries(self):
        runtime = Runtime(APP.parents[3], mock=True)
        config = json.loads(runtime.call("--profile", "stdio", "config", "--format", "json"))
        for service in config["services"].values():
            self.assertTrue(service["read_only"])
            self.assertEqual(service["cap_drop"], ["ALL"])
            self.assertEqual(service["restart"], "no")
            self.assertFalse(service.get("ports"))
            self.assertFalse(service.get("privileged", False))
        agent = config["services"]["agent"]
        self.assertEqual(set(agent["networks"]), {"runtime"})
        self.assertTrue(all(volume["type"] == "volume" for volume in agent["volumes"]))
        self.assertNotIn("secrets", agent)
        for name in ("worker", "mcp"):
            mounts = config["services"][name]["volumes"]
            project = next(volume for volume in mounts if volume["target"] == "/project")
            self.assertEqual(project["source"], str(runtime.root))
            self.assertFalse(project.get("read_only", False))
            self.assertEqual(
                {volume["target"] for volume in mounts if volume.get("read_only")},
                {"/project/.git"},
            )
            self.assertEqual(len(mounts), 2)
            self.assertFalse(any(volume["target"].startswith("/workspace") for volume in mounts))
        ignored = (APP / "docker/Dockerfile.dockerignore").read_text()
        for value in (
            "**/.env", "**/.env.*", "**/*.env", "**/auth.json",
            "**/.caprmedio_tmp", "**/.caprmedio_install",
            "**/.caprmedio_runtime", "**/tmp",
        ):
            self.assertIn(value, ignored)

    def test_failed_start_does_not_select_docker_transport(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".caprmedio_caprmedio").mkdir()
            (root / ".git").mkdir()
            runtime = Runtime(root, mock=True)
            with patch.object(runtime, "call", side_effect=RuntimeError("not ready")):
                with self.assertRaises(RuntimeError):
                    runtime.start()
            self.assertFalse(
                (root / ".caprmedio_install/workflow_orchestrator/docker/transport.json").exists()
            )

    def test_start_only_creates_routing_after_services_are_ready(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".caprmedio_caprmedio").mkdir()
            (root / ".git").mkdir()
            runtime = Runtime(root, mock=True)
            with patch.object(runtime, "call", return_value="") as operation:
                self.assertEqual(runtime.start()["outcome"], "ready")
                self.assertEqual(runtime.start()["outcome"], "ready")
            self.assertEqual(operation.call_count, 2)
            marker = root / ".caprmedio_install/workflow_orchestrator/docker/transport.json"
            self.assertEqual(json.loads(marker.read_text())["project_name"], runtime.project)
            self.assertEqual(list(marker.parent.glob("transport-*.json")), [])
            self.assertFalse((marker.parent / "runs").exists())

    def test_mount_and_routing_symlinks_rejected_before_start(self):
        with tempfile.TemporaryDirectory(
            dir=self.temporary, ignore_cleanup_errors=True
        ) as directory:
            root = Path(directory)
            (root / ".git").mkdir()
            outside = root / "unmounted"
            outside.mkdir()
            authority = root / ".caprmedio_caprmedio"
            authority.symlink_to(outside, target_is_directory=True)
            runtime = Runtime(root, mock=True)
            with patch.object(runtime, "call") as operation:
                with self.assertRaises(ValueError):
                    runtime.start()
                operation.assert_not_called()
            authority.unlink()
            authority.mkdir()
            install = root / ".caprmedio_install"
            install.mkdir()
            (install / "workflow_orchestrator").symlink_to(outside, target_is_directory=True)
            with patch.object(runtime, "call") as operation:
                with self.assertRaises(ValueError):
                    runtime.start()
                operation.assert_not_called()

    def test_docker_sandbox_selection_does_not_change_native_policy(self):
        from agent import CodexAgent

        native = CodexAgent().command(Path("/tmp/mock"))
        isolated = CodexAgent(container_isolation=True).command(Path("/tmp/mock"))
        self.assertEqual(native[native.index("--sandbox") + 1], "read-only")
        self.assertEqual(isolated[isolated.index("--sandbox") + 1], "danger-full-access")
        self.assertIn('approval_policy="never"', isolated)
        self.assertIn("--ignore-user-config", isolated)


class AgentServiceTests(unittest.TestCase):
    def setUp(self):
        from starlette.testclient import TestClient
        import agent_service

        self.service = agent_service
        self.service.busy = False
        self.service.calls = 0
        self.client = TestClient(agent_service.app)
        self.addCleanup(self.client.close)

    def test_unknown_fields_and_phase_rejected_before_dispatch(self):
        for payload in (
            {"context": {}, "phase": "unknown", "timeout": 1},
            {"context": {}, "phase": "check", "timeout": 1, "surprise": True},
        ):
            self.assertEqual(self.client.post("/execute", json=payload).status_code, 422)
        self.assertEqual(self.service.calls, 0)

    def test_oversized_and_busy_requests_do_not_dispatch(self):
        with patch.object(self.service, "MAX_BYTES", 20):
            self.assertEqual(self.client.post("/execute", content=b"x" * 21).status_code, 413)
        self.service.busy = True
        self.assertEqual(
            self.client.post(
                "/execute", json={"context": {}, "phase": "check", "timeout": 1}
            ).status_code,
            409,
        )
        self.assertEqual(self.service.calls, 0)

    def test_invalid_output_is_not_accepted_and_errors_do_not_leak(self):
        for value in ({"confidence": 100}, RuntimeError("secret detail")):
            if isinstance(value, Exception):
                replacing = patch.object(self.service, "execute", side_effect=value)
            else:
                replacing = patch.object(self.service, "execute", return_value=value)
            with replacing:
                response = self.client.post(
                    "/execute", json={"context": {}, "phase": "check", "timeout": 1}
                )
            self.assertEqual(response.status_code, 502)
            self.assertNotIn("secret", response.text)
            self.assertFalse(self.service.busy)

    def test_missing_credentials_are_not_reported_ready(self):
        with (
            patch.dict(os.environ, {"CAPRMEDIO_AGENT_MODE": "codex"}),
            patch.object(Path, "is_file", return_value=False),
        ):
            self.assertFalse(self.client.get("/health").json()["ready"])


if __name__ == "__main__":
    unittest.main()
