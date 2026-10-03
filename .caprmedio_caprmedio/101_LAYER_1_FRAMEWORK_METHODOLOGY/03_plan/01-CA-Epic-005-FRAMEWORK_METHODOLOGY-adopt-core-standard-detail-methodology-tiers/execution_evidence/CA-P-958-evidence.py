"""Bounded Local classification evidence. No authority, runtime, or file writes.

snapshot binds the CA-P-957 result before CA-P-958; candidates and checks consume
that immutable snapshot. Authored changes are applied separately with apply_patch.
"""
from pathlib import Path
from collections import Counter
import argparse
import base64
import datetime
import hashlib
import json
import re
import runpy
import sys
import zlib

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())
TOOL = ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS'
sys.path[:0] = [str(TOOL), str(TOOL / 'COMMIT_CONTEXT')]
import commit_context_logic as canonical


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(name):
    path = HERE / name
    if not path.exists() and name == 'CA-P-958-baseline.json':
        return json.loads(zlib.decompress(base64.b64decode((HERE / (name + '.zlib.base64')).read_text())))
    return json.loads(path.read_text())


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def aliases(c):
    return {c.identity, c.filename, c.filename.removesuffix('.md')}


def graph_for(carriers, ambiguous=()):
    graph, ambiguous = {}, set(ambiguous)
    for c in carriers:
        for key in aliases(c):
            if key in ambiguous:
                continue
            if key in graph and graph[key].path != c.path:
                graph.pop(key)
                ambiguous.add(key)
            else:
                graph[key] = c
    return graph


def snapshot():
    _, _, active, _ = runpy.run_path(str(HERE / 'CA-P-957-evidence.py'))['frontier']()
    graph, registry = canonical.working_graph(ROOT), canonical.relation_registry(ROOT)
    local, protected = [], []
    for r in active:
        if r['source_scope_unit'] != 'LOCAL_CONFIGURATION':
            protected.append({k: r[k] for k in ('atom_id', 'relative_path', 'sha256', 'source_scope_unit')})
            continue
        c = canonical.carrier_from_bytes(r['relative_path'], r['bytes_utf8'].encode())
        assert c.identity == r['atom_id']
        local.append(dict(r, canonical_identity=c.identity, before_relations=c.relations,
                          baseline_diagnostics=canonical.resolve_relations(c, graph, registry)[2]))
    assert len(local) == 52 and len(protected) == 651
    return {'task': 'CA-P-958', 'basis': 'Verified current CA-P-957 mapping, without altering frozen CA-P-957 evidence',
            'records': local, 'protected_frontier': protected,
            'scope': '52 Active Local RMED; 648 Core and 3 adjacent Goals excluded',
            'limits': 'No Journal, Git mutation, settings selection, generated projection, runtime, compiler, install, folder migration, or Task lifecycle changes.'}


def candidates(batch):
    base = read('CA-P-958-baseline.json')
    decisions = read('CA-P-958-dispositions.json')['records']
    by_id = {r['atom_id']: r for r in base['records']}
    changes = []
    stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4))).strftime('%Y-%m-%d %H:%M:%S %z')
    for d in decisions:
        if d.get('batch') != batch:
            continue
        r = by_id[d['atom_id']]
        path, old = Path(r['relative_path']), r['bytes_utf8']
        assert (ROOT / path).read_bytes() == old.encode()
        archive = path.parent / 'archive' / (path.stem + '@' + str(r['version']) + '.md')
        assert not (ROOT / archive).exists(), str(archive)
        row = {'atom_id': r['atom_id'], 'operation': d['operation'],
               'before_path': path.as_posix(), 'before_version': r['version'], 'before_sha256': sha(old.encode()),
               'before_bytes_utf8': old, 'archive_path': archive.as_posix(), 'archive_sha256': sha(old.encode()),
               'before_tier': r['current_local_tier'], 'after_tier': d['tier'], 'decision': d}
        if d['operation'] == 'retire':
            changes.append(row)
            continue
        after = old
        for a, b in d.get('replacements', []):
            assert after.count(a) == 1, (r['atom_id'], a, after.count(a))
            after = after.replace(a, b)
        if d['tier'] != r['current_local_tier']:
            prefix = r['atom_id'] + '-LOCAL_CONFIGURATION-' + {'Core': 'CORE-', 'General': 'GENERAL-', 'Standard': ''}[d['tier']]
            role = {'R': 'REQUIREMENT', 'E': 'EVALUATION', 'D': 'DELIVERY', 'M': 'METHOD'}[r['content_role']]
            path = path.with_name(prefix + role + '--' + path.name.split('--', 1)[1])
        if d.get('filename'):
            path = path.with_name(d['filename'])
        after = re.sub(r'(?m)^version:.*$', 'version: ' + str(r['version'] + 1), after, count=1)
        after = re.sub(r'(?m)^updated_at:.*$', 'updated_at: "' + stamp + '"', after, count=1)
        if not re.search(r'(?m)^atom_id:', after.split('---', 2)[1]):
            after = after.replace('---\n', '---\natom_id: ' + r['atom_id'] + '\n', 1)
        c = canonical.carrier_from_bytes(path.as_posix(), after.encode())
        assert c.identity == r['canonical_identity'] and c.version == r['version'] + 1
        row.update(after_path=path.as_posix(), after_version=c.version, after_sha256=c.sha256,
                   after_bytes_utf8=after, after_relations=c.relations)
        changes.append(row)
    assert changes
    return {'task': 'CA-P-958', 'batch': batch, 'records': changes}


def patch(plan):
    lines = ['*** Begin Patch']
    for r in plan['records']:
        lines += ['*** Add File: ' + str(ROOT / r['archive_path'])]
        lines += ['+' + x for x in r['before_bytes_utf8'].splitlines()]
        if r['operation'] != 'retire' and r['after_path'] == r['before_path']:
            lines += ['*** Update File: ' + str(ROOT / r['before_path']), '@@']
            lines += ['-' + x for x in r['before_bytes_utf8'].splitlines()]
            lines += ['+' + x for x in r['after_bytes_utf8'].splitlines()]
            continue
        lines += ['*** Delete File: ' + str(ROOT / r['before_path'])]
        if r['operation'] != 'retire':
            lines += ['*** Add File: ' + str(ROOT / r['after_path'])]
            lines += ['+' + x for x in r['after_bytes_utf8'].splitlines()]
    lines += ['*** End Patch']
    return '\n'.join(lines)


def check(plans, proposed=False):
    base = read('CA-P-958-baseline.json')
    decisions = read('CA-P-958-dispositions.json')['records']
    assert len(decisions) == 52 and len({d['atom_id'] for d in decisions}) == 52
    assert {d['atom_id'] for d in decisions} == {r['atom_id'] for r in base['records']}
    by_id = {r['atom_id']: r for r in base['records']}
    changes = {r['atom_id']: r for p in plans for r in p['records']}
    assert len(changes) == sum(len(p['records']) for p in plans)
    for d in decisions:
        assert d['claim_evidence'] and d['witness'] and d['source_authority'] and d['scope_binding']
        assert d['test'] in ('S', 'F', 'G', 'absorbed', 'unresolved')
        if d['test'] == 'G':
            assert d['tier'] == 'General' and len(d['realizations']) == 2 and d['countermodel']
        if d['operation'] == 'retire':
            assert d['clause_allocation']
    protected = []
    for r in base['protected_frontier']:
        assert sha((ROOT / r['relative_path']).read_bytes()) == r['sha256'], r['relative_path']
        protected.append(r['atom_id'])
    for r in base['records']:
        delta = changes.get(r['atom_id'])
        if not delta:
            assert (ROOT / r['relative_path']).read_bytes() == r['bytes_utf8'].encode()
            continue
        assert (delta['before_path'], delta['before_version'], delta['before_sha256'], delta['before_bytes_utf8']) == (
            r['relative_path'], r['version'], r['sha256'], r['bytes_utf8'])
        if not proposed:
            assert (ROOT / delta['archive_path']).read_bytes() == r['bytes_utf8'].encode()
            if delta['operation'] == 'retire' or delta['after_path'] != delta['before_path']:
                assert not (ROOT / delta['before_path']).exists()
            if delta['operation'] != 'retire':
                assert (ROOT / delta['after_path']).read_bytes() == delta['after_bytes_utf8'].encode()
        if delta['operation'] != 'retire':
            expected = r['bytes_utf8'].split('---', 2)[2]
            for a, b in delta['decision'].get('replacements', []):
                if a in expected:
                    expected = expected.replace(a, b)
            assert expected == delta['after_bytes_utf8'].split('---', 2)[2], delta['atom_id']
            c = canonical.carrier_from_bytes(delta['after_path'], delta['after_bytes_utf8'].encode())
            assert c.identity == r['canonical_identity'] and c.version == r['version'] + 1
            assert c.sha256 == delta['after_sha256']
    actual = canonical.working_graph(ROOT)
    current = {c.path: c for c in actual.values()}
    ambiguous = {a for c in current.values() for a in aliases(c) if a not in actual}
    local_paths = {r['relative_path'] for r in base['records']} | {r.get('after_path') for r in changes.values()}
    outside = [c for c in current.values() if c.path not in local_paths]
    before_local = [canonical.carrier_from_bytes(r['relative_path'], r['bytes_utf8'].encode()) for r in base['records']]
    after_local = []
    for r in base['records']:
        delta = changes.get(r['atom_id'])
        if delta and delta['operation'] == 'retire':
            continue
        p, body = (delta['after_path'], delta['after_bytes_utf8']) if delta else (r['relative_path'], r['bytes_utf8'])
        after_local.append(canonical.carrier_from_bytes(p, body.encode()))
    before = graph_for(outside + before_local, ambiguous)
    after = graph_for(outside + after_local, ambiguous)
    registry = canonical.relation_registry(ROOT)
    touched = {a for c in before_local if c.identity in changes for a in aliases(c)}
    checked = after_local + [c for c in outside if any(
        t.removesuffix('.md') in touched or Path(t).name.removesuffix('.md') in touched
        for ts in c.relations.values() for t in ts)]
    def key(d):
        return json.dumps(dict(d, details={k: v for k, v in d.get('details', {}).items() if k != 'path'}), sort_keys=True)
    diagnostic_rows = []
    for c in checked:
        prior = next((x for x in before_local if x.identity == c.identity), c)
        ds = canonical.resolve_relations(c, after, registry)[2]
        previous = canonical.resolve_relations(prior, before, registry)[2]
        new = [d for d in ds if key(d) not in {key(d) for d in previous}]
        if ds or previous:
            diagnostic_rows.append({'atom_id': c.identity, 'path': c.path, 'diagnostics': ds,
                                    'before_diagnostics': previous, 'new_diagnostics': new})
    new_count = sum(len(r['new_diagnostics']) for r in diagnostic_rows)
    return {'task': 'CA-P-958', 'result': 'PASS' if not new_count else 'NEW_RELATION_DIAGNOSTICS',
            'proposed_overlay': proposed, 'origin_count': 52, 'mapped_change_count': len(changes),
            'exact_archive_count': len(changes) if not proposed else 0,
            'byte_unchanged_origins': 52 - len(changes), 'protected_core_count': 648,
            'protected_adjacent_goals': 3, 'active_local_count': len(after_local),
            'actual_active_tier_counts': dict(Counter(changes[c.identity]['after_tier'] if c.identity in changes else by_id[c.identity]['current_local_tier'] for c in after_local)),
            'completed_admission_count': sum(d['operation'] != 'pending' and (d['operation'] == 'unchanged' or d['atom_id'] in changes) for d in decisions),
            'pending_admission_count': sum(d['operation'] == 'pending' for d in decisions),
            'pending_ids': [d['atom_id'] for d in decisions if d['operation'] == 'pending'],
            'new_relation_diagnostic_count': new_count,
            'current_relation_diagnostic_count': sum(len(r['diagnostics']) for r in diagnostic_rows),
            'relation_records': diagnostic_rows,
            'limits': 'Exact reviewed byte maps and canonical endpoint checks; no proof of arbitrary prose, unresolved owner depth, runtime or legacy graph closure.'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('snapshot', 'candidates', 'patch', 'check'))
    ap.add_argument('--batch')
    ap.add_argument('--proposed', action='store_true')
    ap.add_argument('--plans', nargs='*', default=[])
    args = ap.parse_args()
    if args.mode == 'snapshot':
        emit(snapshot())
    elif args.mode == 'candidates':
        emit(candidates(args.batch))
    elif args.mode == 'patch':
        print(patch(read(args.plans[0])))
    else:
        emit(check([read(p) for p in args.plans], args.proposed))


if __name__ == '__main__':
    main()
