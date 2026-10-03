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

    def catalog(self):
        settings = tomllib.loads(self.read(self.root / '.caprmedio_caprmedio/caprmedio_project_settings.toml').decode())
        control = self.root / settings.get('paths', {}).get('control_root', '.caprmedio_caprmedio')
        if '..' in control.parts or not control.is_relative_to(self.root) or control.is_symlink():
            raise ValueError('Invalid Project control root')
        atoms, tools, issues = {}, [], []
        started, total = time.monotonic(), 0
        candidates = (path for path in control.rglob('*.md') if not
                      any(part.lower() in ('archive', 'archived', 'draft', 'done', 'resolved', 'canceled', 'cancelled')
                          for part in path.relative_to(control).parts))
        for number, path in enumerate(candidates):
            if number >= 10000 or time.monotonic() - started > 60:
                issues.append('incomplete: catalog limit reached')
                break
            relative = path.relative_to(control).parts
            if '00_APPLICABLE_METHODOLOGY' in relative and '000_APPLICABLE_MTHD_sources' not in relative:
                continue
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
            structure = tomllib.loads(self.read(self.root / '.caprmedio_caprmedio/project_structure.toml').decode())
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
            raise ValueError('Run not found; only RMED Atoms Base Revise backend is registered')
        state = json.loads(self.read(path))
        result = {key: state.get(key) for key in ('workflow_run_id', 'workflow_name', 'outcome',
                  'progress', 'report_path', 'recording_blockers', 'updated_at')}
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
