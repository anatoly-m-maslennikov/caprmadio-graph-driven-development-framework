"""Explicit process generations; no watcher, workflow dispatch or automatic replay."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Literal

from jsonschema import Draft202012Validator
from mcp import Client, StdioServerParameters, types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.stdio import stdio_server
from pydantic import BaseModel, ConfigDict


class ReloadRequest(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    operation: Literal['reload']
    request_id: str | None = None


CONTROL = types.Tool(name='reload_mcp_implementation',
    description='Explicitly reload MCP implementation; state-changing, no Workflow dispatch.',
    annotations=types.ToolAnnotations(read_only_hint=False, destructive_hint=False,
                                      idempotent_hint=True, open_world_hint=False),
    input_schema={'type': 'object', 'properties': {'request': ReloadRequest.model_json_schema()},
                  'required': ['request'], 'additionalProperties': False})

STATUS = types.Tool(name='get_mcp_reload_status',
    description='Read current MCP generations and in-flight counts; no reload or writes.',
    annotations=types.ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                      idempotent_hint=True, open_world_hint=False),
    input_schema={'type': 'object', 'properties': {'request': {
        'type': 'object', 'properties': {}, 'additionalProperties': False}},
        'required': ['request'], 'additionalProperties': False})


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def result(value, error=False):
    return types.CallToolResult(content=[types.TextContent(type='text', text=json.dumps(value))],
                                structured_content=value, is_error=error)


GENERATION_READY_TIMEOUT_SECONDS = 20
_STARTUP_TELEMETRY_ENV = 'CAPRMEDIO_STARTUP_TELEMETRY'
_STARTUP_PHASES = frozenset({
    'initial_fingerprint', 'reload_fingerprint', 'fingerprint_verify',
    'child_handshake', 'list_tools', 'generation_ready', 'schema_validation',
})


def _startup_telemetry_enabled():
    """Keep bounded startup timing diagnostics opt-in and transport-safe."""
    return os.environ.get(_STARTUP_TELEMETRY_ENV) == '1'


def _startup_timing(enabled, phase, started, outcome='completed'):
    """Emit fixed phase timing only; never put diagnostic data on MCP stdout."""
    if enabled and phase in _STARTUP_PHASES:
        elapsed_ms = max(0, round((time.monotonic() - started) * 1000))
        print(f'caprmedio_mcp_startup phase={phase} outcome={outcome} elapsed_ms={elapsed_ms}',
              file=sys.stderr, flush=True)


class Generation:
    def __init__(self, params, fingerprint):
        self.params, self.fingerprint = params, fingerprint
        self.client, self.tools, self.in_flight = None, [], 0
        self.retired_at = None
        self.stop = asyncio.Event()
        self.ready = asyncio.get_running_loop().create_future()
        self.startup_telemetry = _startup_telemetry_enabled()
        self.task = asyncio.create_task(self.run())

    async def run(self):
        phase = 'child_handshake'
        started = time.monotonic()
        try:
            # This is a known local implementation subprocess.  Its cold
            # import can exceed the client's fixed ten-second auto-discover
            # probe, whereas the gateway already owns a bounded readiness
            # deadline.  Negotiate the stable legacy handshake directly.
            async with Client(self.params, cache=None, mode='legacy',
                              read_timeout_seconds=GENERATION_READY_TIMEOUT_SECONDS) as client:
                _startup_timing(self.startup_telemetry, phase, started)
                self.client = client
                phase, started = 'list_tools', time.monotonic()
                page = await client.list_tools()
                self.tools = list(page.tools)
                while page.next_cursor:
                    page = await client.list_tools(cursor=page.next_cursor)
                    self.tools.extend(page.tools)
                _startup_timing(self.startup_telemetry, phase, started)
                self.ready.set_result(None)
                await self.stop.wait()
        except BaseException as error:
            if not self.ready.done():
                _startup_timing(self.startup_telemetry, phase, started, 'failed')
                self.ready.set_exception(error)

    async def close(self):
        self.stop.set()
        try:
            await asyncio.wait_for(asyncio.shield(self.task), 5)
        except (TimeoutError, asyncio.CancelledError):
            self.task.cancel()
            await asyncio.gather(self.task, return_exceptions=True)
            if asyncio.current_task().cancelling():
                raise


class Gateway:
    def __init__(self, root, implementation=None):
        self.root = Path(root).resolve(strict=True)
        self.implementation = Path(implementation or Path(__file__).with_name('implementation_server.py'))
        self.active, self.generations = None, []
        self.reload_lock, self.receipts = asyncio.Lock(), {}
        self.storage = self.root / '.caprmedio_install/mcp_hot_reload'

    def _fingerprint_with_timing(self, phase):
        started = time.monotonic()
        try:
            value = self.fingerprint()
        except BaseException:
            _startup_timing(_startup_telemetry_enabled(), phase, started, 'failed')
            raise
        _startup_timing(_startup_telemetry_enabled(), phase, started)
        return value

    def fingerprint(self):
        files = [self.implementation]
        if self.implementation.name == 'implementation_server.py':
            files = [p for p in self.implementation.parent.parent.rglob('*.py')
                     if p.name not in ('server.py', 'hot_reload.py')
                     and not any(part in ('tests', '__pycache__', '.venv', 'venv') for part in p.parts)]
        return digest([(str(p), hashlib.sha256(p.read_bytes()).hexdigest()) for p in sorted(files)])

    async def prepare(self, fingerprint):
        environment = self.child_environment()
        generation = Generation(StdioServerParameters(command=sys.executable,
            args=['-B', '-X', f'pycache_prefix={self.storage / "bytecode" / fingerprint}',
                  str(self.implementation), '--project-root', str(self.root)],
            env=environment), fingerprint)
        phase = 'generation_ready'
        started = time.monotonic()
        try:
            await asyncio.wait_for(asyncio.shield(generation.ready),
                                   GENERATION_READY_TIMEOUT_SECONDS)
            _startup_timing(_startup_telemetry_enabled(), phase, started)
            phase, started = 'schema_validation', time.monotonic()
            names = [t.name for t in generation.tools]
            if len(set(names)) != len(names) or {CONTROL.name, STATUS.name}.intersection(names):
                raise ValueError('Duplicate or reserved Tool name')
            for tool in generation.tools:
                if not re.fullmatch(r'[A-Za-z0-9_.-]{1,128}', tool.name):
                    raise ValueError('Invalid Tool name')
                Draft202012Validator.check_schema(tool.input_schema)
                if tool.output_schema is not None:
                    Draft202012Validator.check_schema(tool.output_schema)
            _startup_timing(_startup_telemetry_enabled(), phase, started)
            phase, started = 'fingerprint_verify', time.monotonic()
            if self._fingerprint_with_timing('fingerprint_verify') != fingerprint:
                raise ValueError('Implementation changed during preparation')
        except BaseException:
            if phase != 'fingerprint_verify':
                _startup_timing(_startup_telemetry_enabled(), phase, started, 'failed')
            await generation.close()
            raise
        generation.registry = digest([t.model_dump(mode='json', by_alias=True) for t in generation.tools])
        self.generations.append(generation)
        return generation

    @staticmethod
    def child_environment():
        """Pass only runtime essentials; transport credentials never reach tools."""
        allowed = {'PATH', 'TMPDIR', 'TEMP', 'TMP', 'LANG', 'TZ', 'CAPRMEDIO_RUNTIME_NAMESPACE'}
        return {key: value for key, value in os.environ.items()
                if key in allowed or key.startswith('LC_')}

    def status(self):
        return {'active_generation': self.active.fingerprint if self.active else None,
                'client_refresh_status': 'unconfirmed',
                'generations': [{'generation': g.fingerprint, 'in_flight': g.in_flight,
                                 'serving': g is self.active,
                                 'process_available': not g.task.done(),
                                 'drain_limit_reached': g.retired_at is not None
                                 and g.in_flight > 0 and time.monotonic() - g.retired_at >= 60}
                                for g in self.generations]}

    def persist(self, request_id, value):
        if self.storage.is_symlink() or self.storage.parent.is_symlink():
            raise ValueError('Symlink checkpoint directory')
        self.storage.mkdir(parents=True, exist_ok=True)
        path = self.storage / f'{request_id}.json'
        temporary = self.storage / f'{request_id}.pending'
        with temporary.open('x') as stream:
            json.dump(value, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)

    async def publish(self, old, fingerprint, context, value):
        candidate = await self.prepare(fingerprint)
        self.active = candidate
        old.retired_at = time.monotonic()
        changed = old.registry != candidate.registry
        value.update(outcome='reloaded', active_generation=fingerprint,
                     implementation_fingerprint=fingerprint,
                     registry_fingerprint=candidate.registry, registry_changed=changed)
        if changed:
            capabilities = self.server.get_capabilities(
                NotificationOptions(tools_changed=True), protocol_version=context.session.protocol_version)
            if capabilities.tools and capabilities.tools.list_changed:
                try:
                    await context.session.send_tool_list_changed()
                    value['notification_status'] = 'sent'
                except Exception:
                    value['notification_status'] = 'failed'
        if old.in_flight == 0:
            try:
                await old.close()
            except Exception:
                value['diagnostics'].append('Retired generation cleanup failed')

    async def reload(self, request, context):
        if not request.request_id or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', request.request_id):
            raise ValueError('reload requires a safe request_id')
        async with self.reload_lock:
            if request.request_id in self.receipts:
                return self.receipts[request.request_id]
            old = self.active
            value = {'request_id': request.request_id, 'previous_generation': old.fingerprint,
                     'active_generation': old.fingerprint, 'implementation_fingerprint': old.fingerprint,
                     'registry_fingerprint': old.registry, 'registry_changed': False,
                     'notification_status': 'unsupported', 'client_refresh_status': 'unconfirmed',
                     'diagnostics': [], 'outcome': 'unchanged'}
            try:
                fingerprint = self._fingerprint_with_timing('reload_fingerprint')
                if fingerprint != old.fingerprint:
                    await self.publish(old, fingerprint, context, value)
            except Exception as error:
                value.update(outcome='failed', diagnostics=[f'{type(error).__name__}: candidate rejected'])
            self.receipts[request.request_id] = value
            try:
                self.persist(request.request_id, value)
            except (OSError, ValueError):
                value['diagnostics'].append('Receipt persistence failed')
            return value

    async def control(self, context, arguments):
        try:
            if set(arguments) != {'request'}:
                raise ValueError('Expected only request')
            request = ReloadRequest.model_validate(arguments['request'])
            value = await self.reload(request, context)
            return result(value, value.get('outcome') in ('failed', 'rejected'))
        except ValueError as error:
            return result({'outcome': 'rejected', 'diagnostics': [str(error)]}, True)

    async def call(self, context, params):
        if params.name == STATUS.name:
            if params.arguments != {'request': {}}:
                return result({'outcome': 'rejected', 'diagnostics': ['Expected an empty request']}, True)
            return result(self.status())
        if params.name == CONTROL.name:
            return await self.control(context, params.arguments or {})
        generation = self.active
        generation.in_flight += 1
        try:
            if params.name not in {t.name for t in generation.tools}:
                return result({'outcome': 'rejected', 'diagnostics': ['Unknown Tool']}, True)
            return await generation.client.call_tool(params.name, params.arguments)
        except Exception:
            return result({'outcome': 'uncertain', 'generation': generation.fingerprint,
                           'diagnostics': ['Implementation call failed; no automatic replay']}, True)
        finally:
            generation.in_flight -= 1
            if generation is not self.active and generation.in_flight == 0:
                await generation.close()

    async def serve(self):
        await self.initialize()
        try:
            async with stdio_server() as streams:
                await self.build_server().run(*streams, self.server.create_initialization_options(
                    notification_options=NotificationOptions(tools_changed=True)))
        finally:
            await self.close()

    async def initialize(self):
        if self.active is None:
            self.active = await self.prepare(self._fingerprint_with_timing('initial_fingerprint'))

    async def close(self):
        closing = [asyncio.create_task(generation.close()) for generation in self.generations]
        if not closing:
            return
        done, pending = await asyncio.wait(closing, timeout=6)
        for task in pending:
            task.cancel()
        await asyncio.gather(*done, *pending, return_exceptions=True)

    def build_server(self):

        async def list_tools(context, params):
            return types.ListToolsResult(tools=[CONTROL, STATUS, *self.active.tools])

        server = Server('CAPRMEDIO', version='0.2.0', on_list_tools=list_tools,
                        on_call_tool=self.call)
        self.server = server
        return server
