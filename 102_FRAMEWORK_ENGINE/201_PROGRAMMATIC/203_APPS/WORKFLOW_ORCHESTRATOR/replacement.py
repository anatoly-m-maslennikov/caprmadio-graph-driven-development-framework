"""Opt-in Atom replacement with reserved identity and recoverable, non-clobbering effects."""
from contextlib import contextmanager
from datetime import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from zoneinfo import ZoneInfo

import yaml
from validate_atoms_workers.parsing import parse_carrier
from work_journal import append_sealed_events, validate_sealed_event, with_event_digest


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def render(parsed, **properties):
    metadata = {**parsed.metadata, **properties}
    return ('---\n' + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
            + '---\n' + parsed.body.lstrip('\n')).encode()


class Replacement:
    def __init__(self, engine, run_id, ordinal):
        self.engine, self.store = engine, engine.store
        self.run_id, self.ordinal = run_id, ordinal
        self.plan_path = engine.run_directory(run_id) / f'{ordinal}-fix/replacement.json'

    @contextmanager
    def lock(self):
        path = self.store.path('.caprmedio_install/workflow_orchestrator/atom-identity.lock')
        path.parent.mkdir(parents=True, exist_ok=True)
        with os.fdopen(os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600), 'r+') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(stream, fcntl.LOCK_UN)

    def next_id(self, predecessor):
        match = re.fullmatch(r'([A-Za-z][A-Za-z0-9_-]*-[RMED]-)(\d+)', predecessor)
        if not match:
            raise ValueError('Unsupported carried Atom ID sequence')
        prefix = match[1]
        pattern = re.compile(r'(?<![A-Za-z0-9_-])' + re.escape(prefix) + r'(\d+)(?!\d)')
        greatest = int(match[2])

        def include(text):
            nonlocal greatest
            greatest = max([greatest, *(int(row) for row in pattern.findall(text))])

        # Historical names and references are collision evidence, not a source
        # from which an Atom's carried identity is inferred.
        excluded = {'.git', '.caprmedio_tmp', '.caprmedio_install', 'tmp',
                    '.venv', 'venv', 'node_modules', '__pycache__'}
        for directory, children, filenames in os.walk(self.store.root, followlinks=False):
            children[:] = [name for name in children if name not in excluded
                           and not (Path(directory) / name).is_symlink()]
            for name in filenames:
                if not name.endswith('.md'):
                    continue
                path = Path(directory) / name
                if path.is_symlink():
                    continue
                if path.stat().st_size > self.store.max_file_bytes:
                    raise ValueError('Identity allocation cannot cover an oversized Markdown Carrier')
                include(name)
                include(path.read_text(errors='replace'))
        history = subprocess.run(['git', 'log', '--all', '--format=', '--name-only'],
                                 cwd=self.store.root, capture_output=True, text=True, check=False)
        if history.returncode == 0:
            include(history.stdout)
        elif (self.store.root / '.git').exists():
            raise ValueError('Cannot verify historical identity allocation')
        reservations = self.store.path('.caprmedio_install/workflow_orchestrator/runs')
        for path in reservations.glob('*/[0-9]*-fix/replacement.json'):
            if path.is_symlink():
                raise ValueError('Unsafe identity reservation')
            include(json.loads(path.read_text())['successor_atom_id'])
        return prefix + str(greatest + 1)

    def result(self, path, raw, version):
        return {'state': 'present', 'filename': path.name, 'version': version,
                'path': path.relative_to(self.store.root).as_posix(), 'sha256': digest(raw)}

    def plan(self, value, request, new_summary):
        context = value['context']
        source = self.store.path(context['source']['path'])
        before = context['source_content'].encode()
        if not source.is_file() or source.read_bytes() != before:
            raise ValueError('Source changed before replacement admission')
        previous = parse_carrier(before, source)
        proposed = parse_carrier(value['candidate_content'].encode(), source)
        predecessor = context['atom_id']
        successor_id = self.next_id(predecessor)
        version = previous.metadata.get('version')
        if type(version) is not int or version < 1:
            raise ValueError('Replacement needs the predecessor Version')
        now = datetime.now(ZoneInfo('Asia/Tbilisi')).isoformat()
        archived_raw = render(previous, status='Archived', updated_at=now)
        successor_raw = render(proposed, atom_id=successor_id, version=1,
                               author=request.author, updated_at=now)
        slug = re.sub(r'[^a-z0-9]+', '-', new_summary.lower()).strip('-')
        if not slug:
            raise ValueError('Replacement Summary has no usable filename')
        # The successor's carried Properties, not the old filename, determine
        # its canonical optional tokens.
        tokens = [successor_id]
        def token(value):
            return re.sub(r'[^A-Z0-9_]+', '_', str(value).upper()).strip('_')
        metadata = proposed.metadata
        if metadata.get('current_scope_unit'):
            tokens.append(token(metadata['current_scope_unit']))
        if metadata.get('local_tier') not in (None, 'Standard'):
            tokens.append(token(metadata['local_tier']))
        if metadata.get('type'):
            tokens.append(token(metadata['type']))
        if metadata.get('claim_target_scope_unit') not in (None, metadata.get('current_scope_unit')):
            tokens.append(token(metadata['claim_target_scope_unit']))
        head = '-'.join(tokens)
        successor = source.with_name(head + '--' + slug + '.md')
        archive = source.parent / 'archive' / f'{source.stem}@{version}.md'
        for target in (archive, successor):
            self.store.path(target.relative_to(self.store.root).as_posix())
            if target.exists():
                raise ValueError('Replacement destination already exists')
        state = self.store.load(self.run_id)
        base = {'schema_version': 3, 'author': state['author'], 'occurred_at': now,
                'llm_session': state['session'], 'subject_kind': 'file',
                'action_id': f'{self.run_id}:replacement:{self.ordinal}',
                'structural_scope': previous.metadata.get('current_scope_unit', request.scope)}
        git = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=self.store.root,
                             capture_output=True, text=True, check=False)
        recovery = with_event_digest({**base, 'event_id': base['action_id'] + ':before',
            'event': 'recovered', 'kind': 'governed_project_state',
            'result': self.result(source, before, version),
            'recovery_evidence': {'git': {'base_commit': git.stdout.strip()} if git.returncode == 0
                else {'repository_state': 'not_a_git_repository'},
                'carrier': {'filename': source.name}}})
        archived = self.result(archive, archived_raw, version)
        new = self.result(successor, successor_raw, 1)
        events = [recovery, with_event_digest({**base,
            'event_id': base['action_id'] + ':archive', 'event': 'completed',
            'kind': 'governed_project_change', 'action_type': 'MOVE+UPDATE', 'sources': [],
            'previous_result_event': recovery['event_id'], 'result': archived,
            'predecessor_atom_id': predecessor, 'successor_atom_ids': [successor_id]}),
            with_event_digest({**base, 'event_id': base['action_id'] + ':successor',
                'event': 'completed', 'kind': 'governed_project_change',
                'action_type': 'ADD', 'sources': [], 'result': new})]
        for event in events:
            validate_sealed_event(event)
        plan = {'predecessor_atom_id': predecessor, 'successor_atom_id': successor_id,
                'before': context['source'], 'archived': archived, 'successor': new,
                'archive_content': archived_raw.decode(), 'successor_content': successor_raw.decode(),
                'candidate_sha256': digest(value['candidate_content'].encode()),
                'events': events, 'journal_receipts': []}
        self.engine.save(self.plan_path, plan)  # Identity reserved before effects.
        return plan

    def publish(self, path, raw):
        if path.exists():
            if path.is_symlink() or path.read_bytes() != raw:
                raise ValueError('Replacement destination changed; reconcile before retry')
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        # A fully written temporary Carrier is published without overwriting any
        # competing destination. Readers never observe half a Markdown file.
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.replacement-', delete=False) as stream:
            temporary = Path(stream.name)
            try:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
                os.link(temporary, path)
            finally:
                temporary.unlink(missing_ok=True)

    def append(self, plan, events):
        receipts = append_sealed_events(self.store.root, events,
            author=events[0]['author'], local_date=events[0]['occurred_at'][:10], timezone='Asia/Tbilisi')
        saved = {row['event_id']: row for row in plan['journal_receipts']}
        saved.update({row['event_id']: row for row in receipts})
        plan['journal_receipts'] = list(saved.values())
        self.engine.save(self.plan_path, plan)

    def apply(self, value, request, new_summary):
        with self.lock():
            if self.plan_path.is_symlink():
                raise ValueError('Unsafe replacement plan')
            plan = json.loads(self.plan_path.read_text()) if self.plan_path.exists() else self.plan(value, request, new_summary)
            if plan['candidate_sha256'] != digest(value['candidate_content'].encode()) or plan['before'] != value['context']['source']:
                raise ValueError('Saved replacement binds a different proposal')
            before = self.store.path(plan['before']['path'])
            if before.exists() and digest(before.read_bytes()) != plan['before']['sha256']:
                raise ValueError('Source changed before replacement effects')
            archive, successor = self.store.path(plan['archived']['path']), self.store.path(plan['successor']['path'])
            if not before.exists() and not (archive.is_file() and successor.is_file()):
                raise ValueError('Incomplete replacement with missing predecessor; reconcile first')
            self.append(plan, plan['events'][:1])
            self.publish(archive, plan['archive_content'].encode())
            self.publish(successor, plan['successor_content'].encode())
            if before.exists():
                if digest(before.read_bytes()) != plan['before']['sha256']:
                    raise ValueError('Source changed during replacement; preserve all Carriers')
                before.unlink()
            self.append(plan, plan['events'][1:])
            return {key: plan[key] for key in ('predecessor_atom_id', 'successor_atom_id',
                    'before', 'archived', 'successor', 'journal_receipts')}
