"""Opt-in HTTP MCP proof for the approved six-Workflow first usable cut.

Run only with a sealed immutable candidate image and either the established
Release E2E context or an explicit first-cut scratch context.  This is
evidence for the bounded cut, not a Release/promotion or all-route suite.
"""
from __future__ import annotations

import asyncio
import json
import os
from dataclasses import dataclass
from pathlib import Path
import re
import secrets
import socket
import unittest
from unittest import mock
from typing import Mapping

from first_cut_http_security import FirstCutHttpSecurityError, probe_first_cut_http_security
import test_selected_workflows_docker_e2e as selected_harness


FIRST_CUT_CASES = (
    ("W01", "create_atom"),
    ("W02", "update_atom"),
    ("W03", "replace_atom"),
    ("W04", "change_atom_status"),
    ("W09", "run_implementation_workflow"),
    ("W13", "build_applicable_methodology"),
)
_IMMUTABLE_IMAGE = re.compile(r"sha256:[0-9a-f]{64}\Z")
_REPOSITORY_TMP = selected_harness.ROOT / ".caprmedio_tmp"


@dataclass(frozen=True)
class FirstCutE2EContext:
    """The two selected-harness values safe for this development-only cut."""

    scratch_root: Path
    candidate_image_digest: str


def _narrow_context(environ: Mapping[str, str]) -> FirstCutE2EContext:
    """Validate the explicit, disposable context without changing Release grammar."""
    image = environ.get("CAPRMEDIO_FIRST_CUT_HTTP_IMAGE")
    scratch_text = environ.get("CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH")
    if not image or not scratch_text:
        raise ValueError(
            "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE and CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH are both required"
        )
    if not _IMMUTABLE_IMAGE.fullmatch(image):
        raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_IMAGE must be a lowercase sha256 immutable digest")
    scratch = Path(scratch_text)
    if not scratch.is_absolute() or scratch.is_symlink() or not scratch.is_dir():
        raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH must be an existing, non-symlink absolute directory")
    try:
        scratch_resolved = scratch.resolve(strict=True)
        repository_tmp = _REPOSITORY_TMP.resolve(strict=True)
        scratch_resolved.relative_to(repository_tmp)
    except (OSError, ValueError) as error:
        raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH must be below repository .caprmedio_tmp") from error
    if scratch_resolved == repository_tmp:
        raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH must be a child of repository .caprmedio_tmp")
    return FirstCutE2EContext(scratch_root=scratch_resolved, candidate_image_digest=image)


def _first_cut_context(environ: Mapping[str, str]) -> object:
    """Prefer a valid formal context, otherwise require the narrow explicit one."""
    if selected_harness.E2E_CONTEXT is not None:
        return selected_harness.E2E_CONTEXT
    return _narrow_context(environ)


async def _attempt_cleanup(first_failure: BaseException | None, action) -> BaseException | None:
    """Run one teardown action without hiding an earlier failure."""
    try:
        await action()
    except BaseException as error:
        return error if first_failure is None else first_failure
    return first_failure


class FirstCutCorpusTests(unittest.TestCase):
    """Synthetic guard: the opt-in harness cannot silently widen or shrink."""

    def test_exact_approved_first_cut(self) -> None:
        self.assertEqual(("W01", "W02", "W03", "W04", "W09", "W13"),
                         tuple(case for case, _route in FIRST_CUT_CASES))

    def test_narrow_context_requires_complete_immutable_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "both required"):
            _narrow_context({})
        with self.assertRaisesRegex(ValueError, "immutable digest"):
            _narrow_context({
                "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": "latest",
                "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH": str(_REPOSITORY_TMP),
            })

    def test_narrow_context_rejects_tmp_root_not_child(self) -> None:
        with self.assertRaisesRegex(ValueError, "must be a child"):
            _narrow_context({
                "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": "sha256:" + "a" * 64,
                "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH": str(_REPOSITORY_TMP),
            })

    def test_explicit_http_port_never_binds_a_host_socket(self) -> None:
        with mock.patch.object(socket, "socket", side_effect=AssertionError("socket bind must not run")):
            token, port = FirstCutHttpDockerEndToEnd._http_environment({
                "CAPRMEDIO_FIRST_CUT_HTTP_PORT": "18092",
            })
        self.assertTrue(token)
        self.assertEqual(18092, port)
        for value in ("0", "65536", "not-a-port"):
            with self.subTest(port=value), self.assertRaisesRegex(ValueError, "integer in 1..65535"):
                FirstCutHttpDockerEndToEnd._http_environment({"CAPRMEDIO_FIRST_CUT_HTTP_PORT": value})

    def test_cleanup_attempt_preserves_first_failure_and_continues(self) -> None:
        calls = []

        async def first() -> None:
            calls.append("first")
            raise RuntimeError("first cleanup failure")

        async def second() -> None:
            calls.append("second")

        failure = asyncio.run(_attempt_cleanup(None, first))
        failure = asyncio.run(_attempt_cleanup(failure, second))
        self.assertEqual(["first", "second"], calls)
        self.assertIsInstance(failure, RuntimeError)
        self.assertEqual("first cleanup failure", str(failure))

    def test_loopback_client_ignores_inherited_socks_proxy(self) -> None:
        async def check_client() -> None:
            with mock.patch.dict(os.environ, {"ALL_PROXY": "socks5://127.0.0.1:9"}):
                client = FirstCutHttpDockerEndToEnd._http_client("synthetic-token")
                try:
                    self.assertFalse(client.trust_env)
                    self.assertEqual("Bearer synthetic-token", client.headers["Authorization"])
                finally:
                    await client.aclose()

        asyncio.run(check_client())


class FirstCutHttpDockerEndToEnd(unittest.IsolatedAsyncioTestCase):
    """Exercise real Docker HTTP MCP against one disposable GoldenProject per route."""

    def setUp(self) -> None:
        self._previous_context = selected_harness.E2E_CONTEXT
        self._context_installed = False
        self._previous_http_environment = None
        if os.environ.get("CAPRMEDIO_DOCKER_E2E") != "1":
            self.skipTest("requires CAPRMEDIO_DOCKER_E2E=1")
        try:
            context = _first_cut_context(os.environ)
        except ValueError as error:
            self.fail(f"first-cut HTTP E2E input is invalid: {error}")
        selected_harness.E2E_CONTEXT = context
        self._context_installed = True
        self._assertions = selected_harness.SelectedWorkflowsDockerEndToEnd("runTest")
        self._previous_http_environment = {
            key: os.environ.get(key)
            for key in ("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", "CAPRMEDIO_MCP_HTTP_PORT")
        }

    async def asyncTearDown(self) -> None:
        if self._previous_http_environment is not None:
            for key, value in self._previous_http_environment.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
        if self._context_installed:
            selected_harness.E2E_CONTEXT = self._previous_context

    @staticmethod
    def _http_environment(environ: Mapping[str, str] | None = None) -> tuple[str, int]:
        token = secrets.token_urlsafe(32)
        environment = os.environ if environ is None else environ
        if "CAPRMEDIO_FIRST_CUT_HTTP_PORT" in environment:
            try:
                port = int(environment["CAPRMEDIO_FIRST_CUT_HTTP_PORT"])
            except ValueError as error:
                raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_PORT must be an integer in 1..65535") from error
            if not 1 <= port <= 65535:
                raise ValueError("CAPRMEDIO_FIRST_CUT_HTTP_PORT must be an integer in 1..65535")
            return token, port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        return token, port

    @staticmethod
    def _http_client(token: str):
        import httpx2

        # The admitted endpoint is explicit loopback. Never send its bearer
        # through a process-wide HTTP/SOCKS proxy inherited from the host.
        return httpx2.AsyncClient(headers={"Authorization": f"Bearer {token}"}, trust_env=False)

    async def _http_session(self, url: str, token: str):
        from mcp.client.session import ClientSession
        from mcp.client.streamable_http import streamable_http_client

        client = self._http_client(token)
        transport = streamable_http_client(url, http_client=client)
        streams = await transport.__aenter__()
        session = ClientSession(*streams)
        await session.__aenter__()
        await session.initialize()
        return client, transport, session

    @staticmethod
    async def _close_http_session(client, transport, session) -> None:
        await session.__aexit__(None, None, None)
        await transport.__aexit__(None, None, None)
        await client.aclose()

    async def _http_terminal_status(self, session, run_id: str) -> dict:
        deadline = asyncio.get_running_loop().time() + 75
        observed = {}
        while asyncio.get_running_loop().time() < deadline:
            observed = selected_harness._structured_tool_result(await session.call_tool(
                "workflow_orchestrator", {"request": {"operation": "status", "run_id": run_id}},
            ))
            if observed.get("outcome") not in {"queued", "admitted", "started", "running", "pending"}:
                return observed
            await asyncio.sleep(0.25)
        self.fail(f"HTTP selected Workflow did not reach a terminal state: {observed}")

    def _assert_http_lifecycle_status(
        self,
        status: dict,
        token: str,
        *,
        expected_states: set[str],
        expected_health: str | None,
    ) -> None:
        """Assert only the mcp-http row; compose may also report worker services."""
        rendered = json.dumps(status, sort_keys=True)
        self.assertNotIn(token, rendered, "runtime status must not render the bearer token")
        services = status.get("services")
        self.assertIsInstance(services, list, status)
        http_rows = [row for row in services if isinstance(row, dict) and row.get("Service") == "mcp-http"]
        self.assertEqual(1, len(http_rows), status)
        row = http_rows[0]
        self.assertIn(str(row.get("State", "")).lower(), expected_states, row)
        if expected_health is not None:
            self.assertEqual(expected_health, str(row.get("Health", "")).lower(), row)

    async def _cleanup_case(
        self,
        first_failure: BaseException | None,
        *,
        runtime,
        temporary,
        worker_started: bool,
        http_started: bool,
        client,
        transport,
        session,
        token: str | None,
    ) -> BaseException | None:
        """Always close HTTP, stop services, and clean fixtures in that order."""
        failure = first_failure

        async def close_session() -> None:
            await self._close_http_session(client, transport, session)

        async def stop_http() -> None:
            stopped = await asyncio.to_thread(runtime.mcp_http_stop)
            self.assertEqual("stopped", stopped.get("outcome"), stopped)
            stopped_status = await asyncio.to_thread(runtime.mcp_http_status)
            self._assert_http_lifecycle_status(
                stopped_status, token, expected_states={"stopped", "exited"}, expected_health=None,
            )

        async def stop_worker() -> None:
            await self._assertions._stop(runtime)

        async def clean_fixture() -> None:
            temporary.cleanup()

        try:
            if session is not None:
                failure = await _attempt_cleanup(failure, close_session)
        finally:
            try:
                if http_started:
                    failure = await _attempt_cleanup(failure, stop_http)
            finally:
                try:
                    if worker_started:
                        failure = await _attempt_cleanup(failure, stop_worker)
                finally:
                    failure = await _attempt_cleanup(failure, clean_fixture)
        return failure

    async def test_six_workflows_over_authenticated_http_mcp(self) -> None:
        for case_id, route in FIRST_CUT_CASES:
            with self.subTest(case=case_id):
                temporary, root, fixture = self._assertions._new_fixture(selected_harness.GoldenCase(case_id, route))
                runtime = self._assertions._runtime(root)
                worker_started = False
                http_started = False
                client = transport = session = None
                token = None
                failure = None
                try:
                    fixture.prepare()
                    worker_started = True
                    await self._assertions._start(runtime)
                    if case_id == "W01":
                        stdio_context = await self._assertions._call(
                            runtime, root, "get_execution_context", {"id": "create_atom"},
                        )
                        self.assertTrue(stdio_context.get("context_complete"), stdio_context)
                        definition = stdio_context.get("definition")
                        self.assertIsInstance(definition, dict, stdio_context)
                        self.assertEqual("create_atom", definition.get("name"), stdio_context)
                    token, port = self._http_environment()
                    os.environ["CAPRMEDIO_MCP_HTTP_SECRET_TOKEN"] = token
                    os.environ["CAPRMEDIO_MCP_HTTP_PORT"] = str(port)
                    started = await asyncio.to_thread(runtime.mcp_http_start)
                    http_started = True
                    self.assertEqual(f"http://127.0.0.1:{port}/mcp", started["url"])
                    running_status = await asyncio.to_thread(runtime.mcp_http_status)
                    self._assert_http_lifecycle_status(
                        running_status, token, expected_states={"running"}, expected_health="healthy",
                    )
                    client, transport, session = await self._http_session(started["url"], token)
                    names = {tool.name for tool in (await session.list_tools()).tools}
                    self.assertIn(route, names)
                    self.assertIn("workflow_orchestrator", names)
                    await asyncio.to_thread(
                        probe_first_cut_http_security,
                        started["url"],
                        token,
                        list_tools=lambda _url, _token: names,
                        recording_boundary=lambda: self._assertions._recording_snapshot(root),
                    )
                    request_id = f"first-cut-http-{case_id.lower()}"
                    before = fixture.snapshot()
                    preview = selected_harness._structured_tool_result(await session.call_tool(
                        route, {"request": fixture.request(request_id=request_id)},
                    ))
                    self.assertEqual("preview", preview.get("disposition"), preview)
                    self.assertEqual(before, fixture.snapshot(), "HTTP preview changed authority")
                    execute = fixture.request(
                        request_id=request_id, mode="execute",
                        receipt=preview["proposal_receipt"],
                        receipt_digest=preview["proposal_receipt_digest"],
                    )
                    admitted = selected_harness._structured_tool_result(await session.call_tool(
                        "workflow_orchestrator",
                        {"request": {"operation": "enqueue_selected", "run_id": request_id,
                                     "execution": execute}},
                    ))
                    self.assertIn(admitted.get("outcome"),
                                  {"queued", "admitted", "started", "running", "pending", "completed"}, admitted)
                    terminal = await self._http_terminal_status(session, request_id)
                    self.assertEqual("terminal", terminal.get("disposition"), terminal)
                    self.assertEqual("completed", terminal.get("outcome"), terminal)
                    selected = terminal.get("selected_result")
                    self.assertIsInstance(selected, dict, terminal)
                    graph = self._assertions._graph_result(root, request_id)
                    rows = self._assertions._assert_graph_path_and_native_results(root, fixture, request_id, graph)
                    self._assertions._assert_shared_run_journal(
                        root, request_id, self._assertions._route_binding(fixture), selected, graph,
                    )
                    self._assertions._assert_route_specific_effects(root, fixture, execute, before, rows)
                except (selected_harness.GoldenCorpusError, FirstCutHttpSecurityError) as error:
                    failure = AssertionError(str(error))
                except BaseException as error:
                    failure = error
                finally:
                    failure = await self._cleanup_case(
                        failure,
                        runtime=runtime,
                        temporary=temporary,
                        worker_started=worker_started,
                        http_started=http_started,
                        client=client,
                        transport=transport,
                        session=session,
                        token=token,
                    )
                if failure is not None:
                    raise failure


if __name__ == "__main__":
    unittest.main()
