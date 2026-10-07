"""Read-only helpers derived from Atom carriers and saved Run evidence."""
import asyncio
import base64
import hashlib
import json
import time
import tomllib
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

from validate_atoms_workers.parsing import parse_carrier


class Query(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    query: str = ''
    limit: int = Field(default=10, ge=1, le=50)
    scope_unit: str | None = None
    include_descendants: bool = False
    availability: str | None = None
    offset: int = Field(default=0, ge=0)


class Context(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    id: str


class Observation(BaseModel):
    model_config = ConfigDict(extra='forbid', strict=True)
    run_id: str
    include_results: bool = False
    ordinal: int | None = Field(default=None, ge=0)


class Watch(Observation):
    cursor: str | None = None
    timeout_seconds: float = Field(default=0, ge=0, le=30)


class Service:
    def __init__(self, root, exposed=()):
        self.root = Path(root).resolve(strict=True)
        self.exposed = set(exposed)

    def read(self, path):
        path = Path(path)
        if not path.is_relative_to(self.root):
            raise ValueError('Path outside Project')
        for part in path.relative_to(self.root).parts:
            if part.startswith('.env') or part.endswith('.env'):
                raise ValueError('Protected path')
        current = self.root
        for part in path.relative_to(self.root).parts:
            current /= part
            if current.is_symlink():
                raise ValueError('Symlink carrier')
        if path.stat().st_size > 8 * 1024 * 1024:
            raise ValueError('Carrier exceeds read limit')
        from validate_atoms_workers.read_io import open_regular
        import os
        descriptor = open_regular(path)
        with os.fdopen(descriptor, 'rb') as stream:
            raw = stream.read(8 * 1024 * 1024 + 1)
            if len(raw) > 8 * 1024 * 1024:
                raise ValueError('Carrier exceeds read limit')
            return raw

    def _control_root(self):
        """Resolve the Project's declared control root from its one settings Carrier."""
        settings_paths = sorted(
            path for path in self.root.glob('.caprmedio_*/caprmedio_project_settings.toml')
            if path.is_file() and not path.is_symlink() and not path.parent.is_symlink()
        )
        if len(settings_paths) != 1:
            raise ValueError('Project settings carrier is missing or ambiguous')
        settings_path = settings_paths[0]
        try:
            settings = tomllib.loads(self.read(settings_path).decode())
        except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
            raise ValueError('Invalid Project settings carrier') from error
        paths = settings.get('paths', {})
        if not isinstance(paths, dict):
            raise ValueError('Invalid Project control root')
        default = settings_path.parent.relative_to(self.root).as_posix()
        value = paths.get('control_root', default)
        if not isinstance(value, str) or not value:
            raise ValueError('Invalid Project control root')
        control = Path(value)
        if control.is_absolute() or '..' in control.parts or control.as_posix() in ('', '.'):
            raise ValueError('Invalid Project control root')
        control_path = self.root / control
        resolved = control_path.resolve()
        if control_path.is_symlink() or not resolved.is_relative_to(self.root) or not resolved.is_dir():
            raise ValueError('Invalid Project control root')
        return resolved

    def _admitted_selected_route_tools(self):
        """Return synthetic discovery rows for source-admitted selected routes only.

        Selected routes intentionally have no Atom ``tool_binding``: their public
        MCP names are registered from the fail-closed canonical manifest.  Keep
        that distinction in discovery rather than treating a source carrier as
        executable.  Importing and loading the existing manifest is therefore
        the sole admission path here as well.
        """
        if not self.exposed:
            return []
        try:
            from selected_routes import load_selected_manifest
            manifest = load_selected_manifest(self.root)
        except (ImportError, OSError, ValueError):
            return []

        rows = []
        for entry in manifest.get("routes", []):
            if not isinstance(entry, dict):
                continue
            route = entry.get("route")
            workflow = entry.get("workflow")
            actions = entry.get("ordered_actions")
            if route not in self.exposed or not isinstance(workflow, dict) or not isinstance(actions, list):
                continue
            workflow_id = workflow.get("atom_id")
            action_ids = [item.get("atom_id") for item in actions if isinstance(item, dict)]
            if (not isinstance(route, str) or not isinstance(workflow_id, str) or not action_ids
                    or not all(isinstance(identity, str) for identity in action_ids)):
                continue
            rows.append({
                "name": route, "mcp_name": route, "availability": "mcp", "source_atom": workflow_id,
                "workflow_ids": [workflow_id], "action_ids": action_ids, "selected_route": True,
                "definition_manifest": {"manifest_ref": manifest["manifest_ref"],
                                        "manifest_digest": manifest["canonical_manifest_sha256"]},
                "source_freshness": manifest["source_freshness"],
                "summary": f"Selected route admitted by the current binding manifest: {route}.",
            })
        return rows

    @staticmethod
    def _selected_route_input_schema(route: str):
        """Compact contract for the generic selected-route MCP request object."""
        digest = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["operation_route", "request_id", "parameters", "parameters_digest",
                         "target_frontier", "target_frontier_digest", "effects", "effects_digest",
                         "definition_manifest", "source_freshness", "initiative"],
            "properties": {
                "operation_route": {"const": route},
                "mode": {"enum": ["preview", "execute"], "default": "preview"},
                "request_id": {"type": "string"}, "parameters": {"type": "object"},
                "parameters_digest": digest, "target_frontier": {"type": "array", "minItems": 1},
                "target_frontier_digest": digest, "effects": {"type": "array"},
                "effects_digest": digest, "definition_manifest": {"type": "object"},
                "source_freshness": {"type": "object"}, "initiative": {"type": "object"},
                "lineage": {"type": "array"}, "expected_definition_revisions": {"type": "array"},
                "proposal_receipt": {"type": "object"}, "proposal_receipt_digest": digest,
                "assigned_action_id": {"type": "string"}, "requested_runs": {"type": "array", "minItems": 1},
                "operator_authorization": {"type": "object"},
            },
            "allOf": [{"if": {"properties": {"mode": {"const": "execute"}}, "required": ["mode"]},
                       "then": {"required": ["proposal_receipt", "proposal_receipt_digest",
                                             "assigned_action_id", "requested_runs", "operator_authorization"]}}],
        }

    def catalog(self):
        control = self._control_root()
        atoms, tools, issues = {}, [], []
        started, total = time.monotonic(), 0
        def current_source(path):
            relative = path.relative_to(control).parts
            if control.name in relative or '_release_materialized' in relative:
                return False
            if any(part.lower() in ('archive', 'archived', 'draft', 'done', 'resolved', 'canceled', 'cancelled', '_journal', '_projection')
                   for part in relative):
                return False
            return ('00_APPLICABLE_METHODOLOGY' not in relative
                    or '000_APPLICABLE_MTHD_sources' in relative)
        # M318/D520 omit delivered copies before counting source candidates;
        # canonical methodology sources still participate in duplicate checks.
        candidates = (path for path in control.rglob('*.md') if current_source(path))
        for number, path in enumerate(candidates):
            if number >= 10000 or time.monotonic() - started > 60:
                issues.append('incomplete: catalog limit reached')
                break
            try:
                raw = self.read(path)
                total += len(raw)
                if total > 256 * 1024 * 1024:
                    issues.append('incomplete: total read limit reached')
                    break
                parsed = parse_carrier(raw, path)
                data = parsed.metadata
                if str(data.get('status', '')).lower() != 'active':
                    continue
                identity = data.get('atom_id')
                if not isinstance(identity, str):
                    continue
                row = {'id': identity, 'scope_unit': data.get('current_scope_unit'),
                       'type': data.get('type'), 'content_role': data.get('content_role'),
                       'source_path': str(path.relative_to(self.root)),
                       'sha256': hashlib.sha256(raw).hexdigest(), 'content': parsed.body,
                       'properties': json.loads(json.dumps(data, default=str))}
                if identity in atoms:
                    issues.append(f'ambiguous Atom ID: {identity}')
                    atoms[identity] = None
                else:
                    atoms[identity] = row
                for block in parsed.body.split('```toml')[1:]:
                    binding = tomllib.loads(block.split('```', 1)[0]).get('tool_binding')
                    if binding:
                        entry = self.root / binding['entrypoint']
                        tools.append({**binding, 'source_atom': identity,
                                      'source_path': row['source_path'],
                                      'sha256': row['sha256'], 'scope_unit': row['scope_unit'],
                                      'summary': parsed.body.split('##', 1)[0].replace('# Summary', '').strip(),
                                      'availability': ('mcp' if binding.get('mcp_name') in self.exposed
                                                       else 'source' if entry.is_file() else 'missing')})
            except (ValueError, OSError, KeyError, TypeError) as error:
                issues.append(f'{path.relative_to(self.root)}: {type(error).__name__}')
        valid = {key: value for key, value in atoms.items() if value}
        counts = {}
        for tool in tools:
            counts[tool['name']] = counts.get(tool['name'], 0) + 1
        tools = [tool for tool in tools if tool['source_atom'] in valid and counts[tool['name']] == 1]
        tools.extend(self._admitted_selected_route_tools())
        return valid, tools, issues

    def discover(self, request, operations=False):
        atoms, tools, issues = self.catalog()
        rows = list(atoms.values()) if operations else tools
        if operations:
            rows = [row for row in rows if row['content_role'] == 'Operations']
            for row in rows:
                bindings = [tool for tool in tools if row['id'] in tool.get('action_ids', []) + tool.get('workflow_ids', [])]
                row['availability'] = 'mcp' if any(tool['availability'] == 'mcp' for tool in bindings) else 'source' if bindings else 'unresolved'
                row['tools'] = [tool['name'] for tool in bindings]
                row['summary'] = row['content'].split('##', 1)[0].replace('# Summary', '').strip()
        words = request.query.lower().split()
        rows = [row for row in rows if all(word in json.dumps(row).lower() for word in words)]
        if request.scope_unit:
            structure = tomllib.loads(self.read(self._control_root() / 'project_structure.toml').decode())
            units = structure.get('scope_units', [])
            selected = {request.scope_unit}
            if not any(unit['scope_unit_name'] == request.scope_unit for unit in units):
                raise ValueError('Unknown Scope Unit')
            if request.include_descendants:
                for _ in units:
                    selected.update(unit['scope_unit_name'] for unit in units if unit.get('parent') in selected)
            rows = [row for row in rows if row.get('scope_unit', atoms.get(row.get('source_atom'), {}).get('scope_unit')) in selected]
        if request.availability:
            rows = [row for row in rows if row.get('availability') == request.availability]
        rows.sort(key=lambda row: row.get('name', row.get('id', '')))
        return {'matches': [{key: value for key, value in row.items() if key != 'content'}
                            for row in rows[request.offset:request.offset + request.limit]],
                'total': len(rows), 'next_offset': request.offset + request.limit
                if request.offset + request.limit < len(rows) else None,
                'coverage_issues': issues}

    def context(self, request):
        atoms, tools, issues = self.catalog()
        row = atoms.get(request.id)
        if row is None:
            matches = [tool for tool in tools if tool['name'] == request.id]
            if len(matches) != 1:
                raise ValueError('Unknown or ambiguous capability')
            row = matches[0]
        selected = [item for item in tools if item.get("selected_route") and request.id in {
            item["name"], item["source_atom"], *item["action_ids"]
        }]
        if selected:
            definition = dict(row)
            routes = sorted(item["name"] for item in selected)
            definition.update({"availability": "mcp", "tools": routes,
                               "definition_manifest": selected[0]["definition_manifest"],
                               "source_freshness": selected[0]["source_freshness"]})
            return {"definition": definition, "related_definitions": [],
                    "input_schema": (self._selected_route_input_schema(routes[0])
                                     if len(routes) == 1 else None),
                    "context_complete": True, "coverage_issues": issues}
        identities = set(row.get('action_ids', []) + row.get('workflow_ids', []))
        if 'source_atom' in row:
            identities.add(row['source_atom'])
        content = row.get('content', '') + json.dumps(row.get('properties', {}))
        import re
        identities.update(re.findall(r'CA-[RMEDO]-\d+', content))
        related = [atoms[identity] for identity in sorted(identities) if identity in atoms and identity != request.id]
        related.extend(item for item in atoms.values() if item['scope_unit'] == row.get('scope_unit')
                       and item['content_role'] in ('Requirement', 'Method', 'Evaluation', 'Delivery')
                       and item not in related and item['id'] != request.id)
        budget, selected = 256 * 1024, []
        used = len(json.dumps(row).encode())
        for item in related:
            size = len(json.dumps(item).encode())
            if used + size > budget:
                break
            selected.append(item)
            used += size
        models = {'DISCOVER_TOOLS': Query, 'DISCOVER_OPERATIONS': Query,
                  'GET_EXECUTION_CONTEXT': Context, 'GET_EXECUTION_STATUS': Observation,
                  'RESUME_EXECUTION_CONTEXT': Observation, 'WATCH_EXECUTION': Watch}
        return {'definition': row, 'related_definitions': selected,
                'input_schema': models[request.id].model_json_schema() if request.id in models else None,
                'context_complete': len(selected) == len(related) and used <= budget,
                'coverage_issues': issues}

    def status(self, request):
        import re
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,127}', request.run_id):
            raise ValueError('Invalid Run ID')
        path = self.root / '.caprmedio_tmp/rmed-base-revise' / request.run_id / 'progress.json'
        if not path.is_file():
            admission = self.root / '.caprmedio_install/workflow_orchestrator/runs' / request.run_id / 'request.json'
            if admission.is_file():
                import sys
                sys.path.insert(0, str(Path(__file__).resolve().parents[2] / '203_APPS/WORKFLOW_ORCHESTRATOR'))
                from backend import status as queued_status
                from contracts import Status
                result = queued_status(self.root, Status(run_id=request.run_id))
                saved = json.loads(self.read(admission))
                return result, {'request': saved['request'], 'selection': saved['selection_bindings'],
                                'criteria': saved['rule_bindings'], 'events': [], 'reports': [], 'handoffs': []}
            raise ValueError('Run not found; only RMED Atoms Base Revise backend is registered')
        state = json.loads(self.read(path))
        result = {key: state.get(key) for key in ('workflow_run_id', 'workflow_name', 'outcome',
                  'progress', 'report_path', 'recording_blockers', 'updated_at', 'coverage_gates')}
        result['operator_question'] = next((row['operator_question'] for row in
            state.get('coverage_gates', {}).values() if row.get('operator_question')), None)
        if request.include_results:
            result['results'] = state.get('reports', [])
            result['history'] = state.get('history', [])
            if request.ordinal is not None:
                if request.ordinal >= len(result['results']):
                    raise ValueError('Ordinal outside frozen selection')
                result['results'] = [result['results'][request.ordinal]]
                result['history'] = [result['history'][request.ordinal]] if result['history'] else []
        return result, state

    def resume(self, request):
        result, state = self.status(request)
        result.update({key: state.get(key) for key in ('request', 'selection', 'criteria', 'handoffs')})
        result['pending'] = state.get('progress', {}).get('states', [])
        drift = []
        for selected in state.get('selection', []):
            source = selected.get('source', {})
            try:
                digest = hashlib.sha256(self.read(self.root / source['path'])).hexdigest()
                if digest != source.get('sha256'):
                    drift.append({'atom_id': selected.get('atom_id'), 'state': 'changed'})
            except (OSError, ValueError, KeyError):
                drift.append({'atom_id': selected.get('atom_id'), 'state': 'unavailable'})
        result['source_drift'] = drift
        return result

    async def watch(self, request):
        previous = None
        if request.cursor:
            if len(request.cursor) > 4096:
                raise ValueError('Oversized cursor')
            try:
                previous = json.loads(base64.urlsafe_b64decode(request.cursor).decode())
                if previous['run_id'] != request.run_id:
                    raise ValueError('Cursor belongs to another Run')
                if not all(key in previous for key in ('position', 'fingerprint', 'prefix')):
                    raise ValueError('Incomplete cursor')
            except (ValueError, KeyError, TypeError, UnicodeError) as error:
                raise ValueError('Invalid cursor') from error
        deadline = time.monotonic() + request.timeout_seconds
        while True:
            result, state = await asyncio.to_thread(self.status, request)
            events = []
            for row in state.get('events', []):
                if not row.get('receipt'):
                    break
                events.append(row['event'])
            fingerprint = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()
            position = previous['position'] if previous else 0
            if not isinstance(position, int) or position < 0:
                raise ValueError('Invalid cursor position')
            if position > len(events):
                raise ValueError('Cursor is ahead of recorded evidence')
            prefix = hashlib.sha256(json.dumps(events[:position], sort_keys=True).encode()).hexdigest()
            if previous and previous.get('prefix') != prefix:
                raise ValueError('Recorded evidence differs from cursor')
            changed = previous is None or previous['fingerprint'] != fingerprint or position != len(events)
            terminal = result['outcome'] in ('completed', 'failed', 'interrupted')
            if changed or terminal or time.monotonic() >= deadline:
                cursor = base64.urlsafe_b64encode(json.dumps({'run_id': request.run_id,
                    'position': len(events), 'fingerprint': fingerprint,
                    'prefix': hashlib.sha256(json.dumps(events, sort_keys=True).encode()).hexdigest()}).encode()).decode()
                return {'status': result, 'notifications': events[position:], 'changed': changed,
                        'terminal': terminal, 'cursor': cursor}
            await asyncio.sleep(0.2)
