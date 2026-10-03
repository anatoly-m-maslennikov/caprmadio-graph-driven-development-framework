"""Read-only frontier binding and review display for CA-P-957.

This is evidence tooling, not a semantic classifier or production parser.
It never assigns a Local Tier. Human-reviewed dispositions are separate data.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frontier():
    inventory = json.loads((HERE / 'CA-P-952-methodology-tier-frontier.projection.json').read_text())
    delta = json.loads((HERE / 'CA-P-956-applied-source-delta.json').read_text())
    changed = {r['atom_id']: r for r in delta['existing']}
    mapped = {}
    added_957 = []
    index = HERE / 'CA-P-957-applied-source-delta.json'
    if index.exists():
        for name in json.loads(index.read_text())['applied_batch_mappings']:
            applied = json.loads((HERE / name).read_text())
            frozen = HERE / applied['frozen_plan']
            assert sha(frozen.read_bytes()) == applied['frozen_plan_sha256']
            for row in applied['existing']:
                mapped.setdefault(row['atom_id'], []).append(row)
            added_957.extend(applied.get('additions', []))
    active = []
    remaining = []
    for r in inventory['records']:
        change = changed.get(r['atom_id'])
        if change:
            archive = (ROOT / change['archive_path']).read_bytes()
            assert sha(archive) == change['before_sha256']
            assert archive.decode() == change['before_bytes_utf8']
            if change['operation'] == 'retire':
                continue
            path, digest, tier = change['after_path'], change['after_sha256'], change['proposed_tier']
        else:
            path, digest, tier = r['relative_path'], r['sha256'], r['current_local_tier']
        version = change['after_version'] if change else r['version']
        retired = False
        for later in mapped.get(r['atom_id'], []):
            assert not change, 'CA-P-956 source results are excluded from CA-P-957'
            assert not retired, 'a retired origin cannot be silently reactivated'
            assert (later['before_path'], later['before_sha256'], later['before_version']) == (path, digest, version)
            assert sha((ROOT / later['archive_path']).read_bytes()) == digest
            if later['operation'] == 'retire':
                path, retired = later['archive_path'], True
            else:
                path, digest, tier, version = later['after_path'], later['after_sha256'], later['after_tier'], later['after_version']
        data = (ROOT / path).read_bytes()
        assert sha(data) == digest, ('unexplained source drift', r['atom_id'], path)
        record = dict(r, relative_path=path, sha256=digest, current_local_tier=tier,
                      version=version, bytes_utf8=data.decode(), excluded_as_956_result=bool(change),
                      retired_by_957=retired)
        if mapped.get(r['atom_id']):
            record['governs_subjects'] = mapped[r['atom_id']][-1].get('after_governs_subjects', record['governs_subjects'])
        if not retired:
            active.append(record)
        if r['source_scope_unit'] == 'CORE_META_MODEL' and not change:
            remaining.append(record)
    for r in delta['additions']:
        data = (ROOT / r['new_path']).read_bytes()
        assert sha(data) == r['after_sha256']
        active.append(dict(atom_id=r['atom_id'], relative_path=r['new_path'],
                           source_scope_unit='CORE_META_MODEL', sha256=r['after_sha256'],
                           bytes_utf8=data.decode(), current_local_tier=r['new_tier'],
                           excluded_as_956_result=True))
    for r in added_957:
        path = r.get('after_path', r['new_path'])
        data = (ROOT / path).read_bytes()
        assert sha(data) == r['after_sha256']
        active.append(dict(atom_id=r['atom_id'], relative_path=path,
                           source_scope_unit='CORE_META_MODEL', sha256=r['after_sha256'],
                           bytes_utf8=data.decode(), current_local_tier=r['new_tier'],
                           version=r.get('after_version', 1), excluded_as_956_result=False,
                           content_role=r['content_role'], governs_subjects=r['governs_subjects'],
                           added_by_957=True))
    excluded = set(inventory['selection']['excluded_directory_segments_casefolded'])
    observed = set()
    for source in inventory['source_roots']:
        for p in (ROOT / source).rglob('*.md'):
            if any(x.casefold() in excluded for x in p.relative_to(ROOT / source).parts):
                continue
            if '@' in p.stem or p.name.startswith('.'):
                continue
            if not any(x in ('04_requirement', '05_method', '06_evaluation', '07_delivery') for x in p.parts):
                continue
            body = p.read_text()
            front = body.split('---', 2)[1] if body.startswith('---') else ''
            status = re.search(r'(?mi)^status: *[\"\']?([^\"\'\n]+)', front)
            if status and status.group(1).strip().casefold() != 'active':
                continue
            observed.add(p.relative_to(ROOT).as_posix())
    for p in (ROOT / inventory['adjacent_authority_root']).glob('*.md'):
        if '@' not in p.stem:
            observed.add(p.relative_to(ROOT).as_posix())
    assert observed == {r['relative_path'] for r in active}
    retirement_count = sum(row['operation'] == 'retire' for rows in mapped.values() for row in rows)
    assert len(active) == 707 - retirement_count + len(added_957)
    assert sum(r['source_scope_unit'] == 'CORE_META_MODEL' for r in active) == 652 - retirement_count + len(added_957)
    assert len(remaining) == 620
    return inventory, delta, active, remaining


def read_batch_plan(batch):
    effective = HERE / ('CA-P-957-batch-' + batch + '-effective-planned-source-delta.json')
    path = effective if effective.exists() else HERE / ('CA-P-957-batch-' + batch + '-planned-source-delta.json')
    plan = json.loads(path.read_text())
    if 'superseded_frozen_plan' in plan:
        assert sha((HERE / plan['superseded_frozen_plan']).read_bytes()) == plan['superseded_frozen_plan_sha256']
        assert sha((HERE / plan['post_checkpoint_correction']).read_bytes()) == plan['post_checkpoint_correction_sha256']
    return path, plan


def read_batch_dispositions(batch, plan):
    records = json.loads((HERE / ('CA-P-957-batch-' + batch + '-dispositions.json')).read_text())['records']
    overrides = plan.get('classification_overrides', {})
    assert set(overrides) <= {r['atom_id'] for r in records}
    return [dict(r, **overrides.get(r['atom_id'], {})) for r in records]


def bound_bytes(path, digest):
    """Read a current result or its explicitly mapped exact subsequent Archive."""
    current = ROOT / path
    if current.exists() and sha(current.read_bytes()) == digest:
        return current.read_bytes()
    index = HERE / 'CA-P-957-applied-source-delta.json'
    for name in json.loads(index.read_text())['applied_batch_mappings']:
        for row in json.loads((HERE / name).read_text())['existing']:
            if (row['before_path'], row['before_sha256']) == (path, digest):
                data = (ROOT / row['archive_path']).read_bytes()
                assert sha(data) == digest
                return data
    raise AssertionError(('unbound current or historical source', path, digest))


def ledger_batch_ids(ledger, batch):
    return {r['atom_id'] for r in ledger['records']
            if r['batch'] == batch or batch in r.get('followup_batches', [])}


def check_body_preservation(before, after, change):
    expected = before.split('---', 2)[2]
    for replacement in change.get('approved_body_replacements', []):
        assert expected.count(replacement['before']) == replacement['count']
        expected = expected.replace(replacement['before'], replacement['after'])
    assert expected == after.split('---', 2)[2]


def check_retirement_authorities(change, plan, active, applied):
    """Bind each retained owner, including fresh authorities in this exact batch."""
    survivors = change.get('successors') or [change['successor']]
    survivors += change.get('additional_surviving_authorities', [])
    additions = {r['atom_id']: r for r in plan.get('additions', [])}
    for survivor in survivors:
        fresh = additions.get(survivor['atom_id'])
        if fresh:
            assert survivor['path'] == fresh['new_path']
            assert survivor['complete_bytes_utf8'] == fresh['new_bytes_utf8']
            assert survivor['sha256'] == sha(fresh['new_bytes_utf8'].encode())
            if applied:
                assert bound_bytes(survivor['path'], survivor['sha256']).decode() == survivor['complete_bytes_utf8']
        else:
            assert bound_bytes(survivor['path'], survivor['sha256']).decode() == survivor['complete_bytes_utf8']
        if applied:
            assert any(r['atom_id'] == survivor['atom_id'] for r in active)


def check_additions(plan, active, applied=None):
    """Validate authored candidate bytes and explicit identity/tier evidence, not meaning."""
    rows = plan.get('additions', [])
    assert len({r['atom_id'] for r in rows}) == len(rows)
    results = {r['atom_id']: r for r in (applied or {}).get('additions', [])}
    if applied is not None:
        assert set(results) == {r['atom_id'] for r in rows}
    for row in rows:
        text = row['new_bytes_utf8']
        assert re.search(r'(?m)^atom_id: ' + re.escape(row['atom_id']) + r'$', text)
        assert re.search(r'(?m)^version: 1$', text)
        assert row['complete_body'] == text.split('---', 2)[2]
        assert Path(row['new_path']).name.startswith(row['atom_id'] + '-CORE_META_MODEL-')
        token = {'Core': 'CORE-', 'General': 'GENERAL-', 'Standard': ''}[row['new_tier']]
        assert '-CORE_META_MODEL-' + token + {'R': 'REQUIREMENT', 'M': 'METHOD', 'E': 'EVALUATION', 'D': 'DELIVERY'}[row['content_role']] + '--' in row['new_path']
        assert row['governs_subjects'] and row['reason']
        if row['decisive_test'] == 'G':
            assert row['new_tier'] == 'General' and len(row['preserving_realizations']) == 2 and row['countermodel']
        elif row['decisive_test'] == 'S':
            assert row['new_tier'] == 'Standard' and row['replacement_witness']
        else:
            assert row['decisive_test'] == 'F' and row['new_tier'] == 'Core' and row['negation_witness']
        if applied is None:
            assert not (ROOT / row['new_path']).exists()
            assert not any(r['atom_id'] == row['atom_id'] for r in active)
        else:
            result = results[row['atom_id']]
            assert result['new_path'] == row['new_path'] and result['after_version'] == 1
            assert result['new_tier'] == row['new_tier'] and result['content_role'] == row['content_role']
            assert result['after_sha256'] == sha(text.encode())
            assert bound_bytes(result['new_path'], result['after_sha256']).decode() == text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check-batch', help='Check a frozen pre-mutation evidence batch such as 01')
    ap.add_argument('--check-applied-batch', help='Check an explicitly mapped applied source batch such as 01')
    ap.add_argument('--check-proposed-relations', help='Run the canonical relation resolver on a complete proposed-byte batch overlay')
    ap.add_argument('--role', choices=list('RMED'))
    ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--count', type=int, default=0)
    ap.add_argument('--ids', nargs='*')
    ap.add_argument('--full', action='store_true')
    ap.add_argument('--compact', action='store_true', help='Omit repeated long paths from the review display')
    args = ap.parse_args()
    inventory, delta, active, remaining = frontier()
    if args.check_proposed_relations:
        batch = args.check_proposed_relations
        _, plan = read_batch_plan(batch)
        tool_root = ROOT / '102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS'
        sys.path[:0] = [str(tool_root), str(tool_root / 'COMMIT_CONTEXT')]
        import commit_context_logic as canonical
        base_graph = canonical.working_graph(ROOT)
        registry = canonical.relation_registry(ROOT)
        # An applied batch's old renamed paths no longer exist. Reconstruct the
        # explicit frozen before graph so existing diagnostics are not falsely
        # reported as new merely because a candidate moved. This is read-only
        # evidence reconstruction, not mutation of the working authority graph.
        if (HERE / ('CA-P-957-batch-' + batch + '-applied-source-delta.json')).exists():
            before_carriers = {c.path: c for c in base_graph.values()}
            current_ambiguous = {key for c in before_carriers.values()
                                 for key in (c.identity, c.filename, c.filename.removesuffix('.md'))
                                 if key not in base_graph}
            for row in plan['existing']:
                if row['operation'] != 'retire':
                    before_carriers.pop(row['proposed_path'], None)
            for row in plan.get('additions', []):
                before_carriers.pop(row['new_path'], None)
            for row in plan['existing']:
                prior = canonical.carrier_from_bytes(row['before_path'], row['before_bytes_utf8'].encode())
                before_carriers[prior.path] = prior
            base_graph = {}
            for prior in before_carriers.values():
                for key in (prior.identity, prior.filename, prior.filename.removesuffix('.md')):
                    if key in current_ambiguous:
                        continue
                    if key in base_graph and base_graph[key].path != prior.path:
                        base_graph.pop(key)
                        current_ambiguous.add(key)
                    else:
                        base_graph[key] = prior
        current = {c.path: c for c in base_graph.values()}
        def aliases(carrier):
            return {carrier.identity, carrier.filename, carrier.filename.removesuffix('.md')}
        # Keep already ambiguous aliases absent rather than letting a rebuild
        # accidentally select one owner, notably the preexisting R1385 collision.
        ambiguous = {key for carrier in current.values() for key in aliases(carrier) if key not in base_graph}
        removed_paths = {r['before_path'] for r in plan['existing']}
        touched_aliases = {key for p, c in current.items() if p in removed_paths for key in aliases(c)}
        overlaid = {p: c for p, c in current.items() if p not in removed_paths}
        candidates = []
        for row in plan['existing']:
            if row['operation'] == 'retire':
                continue
            carrier = canonical.carrier_from_bytes(row['proposed_path'], row['proposed_bytes_utf8'].encode())
            overlaid[carrier.path] = carrier
            candidates.append(carrier)
        for row in plan.get('additions', []):
            carrier = canonical.carrier_from_bytes(row['new_path'], row['new_bytes_utf8'].encode())
            overlaid[carrier.path] = carrier
            candidates.append(carrier)
        graph = {}
        for carrier in overlaid.values():
            for key in aliases(carrier):
                if key in ambiguous:
                    continue
                if key in graph and graph[key].path != carrier.path:
                    graph.pop(key)
                    ambiguous.add(key)
                else:
                    graph[key] = carrier
        checked = {c.path: c for c in candidates}
        for carrier in overlaid.values():
            for targets in carrier.relations.values():
                if any(t.removesuffix('.md') in touched_aliases or Path(t).name.removesuffix('.md') in touched_aliases for t in targets):
                    checked[carrier.path] = carrier
        rows = []
        candidate_predecessors = {r['proposed_path']: r['before_path'] for r in plan['existing'] if r['operation'] != 'retire'}
        def diagnostic_key(value):
            value = dict(value, details={k: v for k, v in value.get('details', {}).items() if k != 'path'})
            return json.dumps(value, sort_keys=True)
        for carrier in checked.values():
            _, sources, diagnostics = canonical.resolve_relations(carrier, graph, registry)
            prior_diagnostics = []
            predecessor_path = candidate_predecessors.get(carrier.path, carrier.path)
            if predecessor_path in current:
                _, _, prior_diagnostics = canonical.resolve_relations(current[predecessor_path], base_graph, registry)
            prior_keys = {diagnostic_key(d) for d in prior_diagnostics}
            new_diagnostics = [d for d in diagnostics if diagnostic_key(d) not in prior_keys]
            rows.append({'atom_id': carrier.identity, 'path': carrier.path, 'sha256': carrier.sha256,
                         'planned_candidate': carrier in candidates, 'source_count': len(sources), 'diagnostics': diagnostics,
                         'prior_diagnostics': prior_diagnostics, 'new_diagnostics': new_diagnostics})
        count = sum(len(r['diagnostics']) for r in rows)
        candidate_count = sum(len(r['diagnostics']) for r in rows if r['planned_candidate'])
        new_candidate_count = sum(len(r['new_diagnostics']) for r in rows if r['planned_candidate'])
        new_inbound_count = sum(len(r['new_diagnostics']) for r in rows if not r['planned_candidate'])
        outcome = 'DIAGNOSTICS' if new_candidate_count or new_inbound_count else ('PASS_WITH_EXISTING_DIAGNOSTICS' if count else 'PASS')
        print(json.dumps({'result': outcome, 'batch': batch,
                          'candidate_count': len(candidates), 'checked_count': len(rows), 'diagnostic_count': count,
                          'candidate_diagnostic_count': candidate_count, 'new_inbound_diagnostic_count': new_inbound_count,
                          'new_candidate_diagnostic_count': new_candidate_count,
                          'records': rows, 'preserved_ambiguous_alias_count': len(ambiguous),
                          'limit': 'Canonical current/proposed relation endpoint and registry checks; no production mutation, semantic tier-parent proof, or runtime validation.'}, indent=2))
        return
    if args.check_applied_batch:
        batch = args.check_applied_batch
        applied = json.loads((HERE / ('CA-P-957-batch-' + batch + '-applied-source-delta.json')).read_text())
        plan_path = HERE / applied['frozen_plan']
        assert sha(plan_path.read_bytes()) == applied['frozen_plan_sha256']
        plan = json.loads(plan_path.read_text())
        planned = {r['atom_id']: r for r in plan['existing']}
        corrections = {}
        for record in applied.get('post_checkpoint_corrections', []):
            correction_path = HERE / record['path']
            assert sha(correction_path.read_bytes()) == record['sha256']
            correction = json.loads(correction_path.read_text())
            assert correction['atom_id'] == record['atom_id']
            assert correction['before_candidate_bytes_utf8'] == planned[record['atom_id']]['proposed_bytes_utf8']
            assert correction['proposed_version'] == planned[record['atom_id']]['proposed_version']
            corrections[record['atom_id']] = correction
        dispositions = read_batch_dispositions(batch, plan)
        reviewed = {r['atom_id']: r for r in dispositions}
        lookup = {r['atom_id']: r for r in remaining}
        parse_relations = runpy.run_path(str(HERE / 'CA-P-956-source-cases.py'))['relations']
        assert {r['atom_id'] for r in applied['existing']} == set(planned)
        for result in applied['existing']:
            before = planned[result['atom_id']]
            archive = (ROOT / result['archive_path']).read_bytes()
            assert archive.decode() == before['before_bytes_utf8']
            assert sha(archive) == before['before_sha256'] == result['archive_sha256']
            if result['operation'] == 'retire':
                assert not (ROOT / before['before_path']).exists()
                check_retirement_authorities(before, plan, active, True)
                continue
            after = bound_bytes(result['after_path'], result['after_sha256'])
            correction = corrections.get(result['atom_id'])
            expected_after = correction['proposed_bytes_utf8'] if correction else before['proposed_bytes_utf8']
            assert after.decode() == expected_after
            assert archive.decode() == before['before_bytes_utf8']
            assert sha(after) == result['after_sha256']
            assert sha(archive) == before['before_sha256'] == result['archive_sha256']
            check_body_preservation(archive.decode(), after.decode(), before)
            if correction:
                expected_relations = parse_relations(archive.decode())
                for kind, removed in correction['removed_relations'].items():
                    assert set(removed) <= set(expected_relations[kind])
                    expected_relations[kind] = [t for t in expected_relations[kind] if t not in removed]
                assert parse_relations(after.decode()) == expected_relations == correction['retained_relations']
                assert sha(after) == correction['proposed_sha256']
            elif not before.get('exact_replacements'):
                assert parse_relations(after.decode()) == parse_relations(archive.decode())
            if before['before_path'] != result['after_path']:
                assert not (ROOT / before['before_path']).exists()
            assert result['after_version'] == before['before_version'] + 1
        check_additions(plan, active, applied)
        for atom_id, review in reviewed.items():
            if atom_id not in planned:
                assert bound_bytes(review['source_path'], review['source_sha256']).decode().split('---', 2)[2] == review['complete_body']
        ledger = json.loads((HERE / 'CA-P-957-master-review-ledger.json').read_text())
        assert len(ledger['records']) == 620
        assert {r['atom_id'] for r in ledger['records']} == {r['atom_id'] for r in remaining}
        assert ledger_batch_ids(ledger, batch) == {i for i, r in reviewed.items() if not r.get('cross_frontier_dependency_repair')}
        print(json.dumps({'result': 'PASS', 'batch': batch, 'applied_revisions': sum(r['operation'] == 'revise' for r in planned.values()),
                          'applied_retirements': sum(r['operation'] == 'retire' for r in planned.values()),
                          'applied_additions': len(plan.get('additions', [])),
                          'exact_prior_archives': len(planned), 'unchanged_dispositions': len(reviewed) - len(planned),
                          'remaining_origin_frontier': len(remaining), 'mapped_active': len(active),
                          'plan_sha256': sha(plan_path.read_bytes()),
                          'limit': 'Checks exact source mapping, archives, body/relations preservation and all unchanged frontier members; no installed runtime or unreviewed semantic closure.'}, indent=2))
        return
    if args.check_batch:
        batch = args.check_batch
        assert not (HERE / ('CA-P-957-batch-' + batch + '-applied-source-delta.json')).exists(), 'Batch already applied: use --check-applied-batch; frozen pre-mutation hashes are historical.'
        plan_path, plan = read_batch_plan(batch)
        dispositions = read_batch_dispositions(batch, plan)
        lookup = {r['atom_id']: r for r in remaining + active}
        reviewed = {r['atom_id']: r for r in dispositions}
        assert len(reviewed) == len(dispositions)
        assert set(reviewed) <= set(lookup)
        changes = {r['atom_id']: r for r in plan['existing']}
        assert len(changes) == len(plan['existing'])
        assert set(changes) <= set(reviewed)
        parse_relations = runpy.run_path(str(HERE / 'CA-P-956-source-cases.py'))['relations']
        def normalized(value):
            return ' '.join(value.replace('**', '').replace('`', '').split())
        for atom_id, review in reviewed.items():
            source = lookup[atom_id]
            if atom_id not in changes and (source['sha256'], source['relative_path']) != (review['source_sha256'], review['source_path']):
                historical = bound_bytes(review['source_path'], review['source_sha256']).decode()
                source = dict(source, relative_path=review['source_path'], sha256=review['source_sha256'],
                              bytes_utf8=historical, current_local_tier=review['new_tier'])
            assert review['source_path'] == source['relative_path']
            assert review['source_sha256'] == source['sha256']
            assert review['complete_body'] == source['bytes_utf8'].split('---', 2)[2]
            assert normalized(review['governing_clause_normalized']) in normalized(review['complete_body'])
            assert review['reason']
            if review['decisive_test'] == 'S':
                assert review['replacement_witness'] and review['new_tier'] == 'Standard'
            elif review['decisive_test'] == 'F':
                assert review['negation_witness'] and review['concrete_choice_test'] and review['new_tier'] == 'Core'
            elif review['decisive_test'] == 'G':
                assert len(review['preserving_realizations']) == 2 and review['countermodel'] and review['new_tier'] == 'General'
            elif review['decisive_test'] == 'lossless_allocation':
                assert changes[atom_id]['operation'] == 'retire' and review['new_tier'] is None
                assert review['allocation_evidence'] and review['successor_ids']
                assert set(review['successor_ids']) == {r['atom_id'] for r in changes[atom_id]['successors']}
            elif review['decisive_test'] == 'dependency_repair_only':
                assert review['classification_deferred_or_previously_admitted']
                assert review['new_tier'] == source['current_local_tier']
                assert source['source_scope_unit'] == 'CORE_META_MODEL'
            elif review['decisive_test'] == 'reference_binding_only':
                assert review['cross_frontier_dependency_repair']
                assert review['new_tier'] == source['current_local_tier']
                assert source['source_scope_unit'] != 'CORE_META_MODEL'
            else:
                raise AssertionError('unadmitted disposition test')
            assert parse_relations(source['bytes_utf8']) == review['direct_relations']
            assert '\n## Scope\n' not in source['bytes_utf8']
            if atom_id not in changes:
                assert source['current_local_tier'] == review['new_tier']
        for atom_id, change in changes.items():
            source = lookup[atom_id]
            before = source['bytes_utf8']
            assert change['before_bytes_utf8'] == before
            assert change['before_sha256'] == sha(before.encode())
            assert change['before_version'] == source['version']
            old = Path(source['relative_path'])
            expected_archive = old.parent / 'archive' / (old.stem + '@' + str(source['version']) + old.suffix)
            assert change['archive_path'] == expected_archive.as_posix()
            assert not (ROOT / change['archive_path']).exists()
            if change['operation'] == 'retire':
                assert change['proposed_path'] is None and change['proposed_version'] is None
                check_retirement_authorities(change, plan, active, False)
                assert change['retirement_reason']
                continue
            after = change['proposed_bytes_utf8']
            assert change['proposed_version'] == source['version'] + 1
            assert change['proposed_tier'] == reviewed[atom_id]['new_tier']
            expected_path = source['relative_path'].replace('-CORE_META_MODEL-CORE-', '-CORE_META_MODEL-').replace('-CORE_META_MODEL-GENERAL-', '-CORE_META_MODEL-')
            token = {'Core': 'CORE-', 'General': 'GENERAL-', 'Standard': ''}[change['proposed_tier']]
            expected_path = expected_path.replace('-CORE_META_MODEL-', '-CORE_META_MODEL-' + token)
            assert change['proposed_path'] == expected_path
            check_body_preservation(before, after, change)
            expected = re.sub(r'(?m)^version: [0-9]+$', 'version: ' + str(source['version'] + 1), before)
            expected = re.sub(r'(?m)^updated_at:.*$', 'updated_at: "' + plan['recorded_at'] + '"', expected)
            for replacement in change.get('exact_replacements', []):
                assert expected.count(replacement['before']) == replacement['count']
                expected = expected.replace(replacement['before'], replacement['after'])
            assert after == expected
            if not change.get('exact_replacements'):
                assert parse_relations(before) == parse_relations(after)
            if change['proposed_path'] != change['before_path']:
                assert not (ROOT / change['proposed_path']).exists()
        check_additions(plan, active)
        ledger = json.loads((HERE / 'CA-P-957-master-review-ledger.json').read_text())
        assert len(ledger['records']) == 620
        assert {r['atom_id'] for r in ledger['records']} == {r['atom_id'] for r in remaining}
        assert len({r['atom_id'] for r in ledger['records']}) == 620
        assert ledger_batch_ids(ledger, batch) == {i for i, r in reviewed.items() if not r.get('cross_frontier_dependency_repair')}
        rejected = {r['atom_id'] for r in ledger['records'] if r['batch'] == batch and r.get('admitted_unchanged') is False}
        for atom_id in rejected:
            row = next(r for r in ledger['records'] if r['atom_id'] == atom_id)
            correction = json.loads((HERE / row['post_checkpoint_disposition']).read_text())
            assert correction['atom_id'] == atom_id
            assert correction['source_sha256'] == reviewed[atom_id]['source_sha256']
            assert correction['complete_body'] == reviewed[atom_id]['complete_body']
        print(json.dumps({'post_checkpoint_rejected_admissions': sorted(rejected),
                          'admitted_unchanged': len(reviewed) - len(changes) - len(rejected)}))
        print(json.dumps({'result': 'PASS', 'batch': batch, 'reviewed': len(reviewed),
                          'planned_revisions': sum(r['operation'] == 'revise' for r in changes.values()),
                          'planned_retirements': sum(r['operation'] == 'retire' for r in changes.values()),
                          'frozen_unchanged_proposals': len(reviewed) - len(changes),
                          'frontier': 620, 'plan_sha256': sha(plan_path.read_bytes()),
                          'limit': 'Checks frozen evidence and proposed byte transformations, not unreviewed semantic claims or installed runtime.'}, indent=2))
        return
    print(json.dumps({'mapped_active': len(active), 'core_active': sum(r['source_scope_unit'] == 'CORE_META_MODEL' for r in active), 'origin_dispositions': len(remaining),
                      'active_origin_count': sum(not r.get('retired_by_957') for r in remaining),
                      'roles': {role: sum(r['content_role'] == role for r in remaining) for role in 'RMED'},
                      'frozen_952_digest': inventory['frontier_sha256']}, indent=2))
    rows = [r for r in remaining if not args.role or r['content_role'] == args.role]
    if args.ids:
        rows = [r for r in remaining if r['atom_id'] in args.ids]
    elif args.count:
        rows = rows[args.start:args.start + args.count]
    else:
        rows = []
    for r in rows:
        text = r['bytes_utf8']
        front, body = text.split('---', 2)[1:]
        print('\n' + r['atom_id'] + '@' + str(r['version']) + ' | ' + r['current_local_tier'] + ('' if args.compact else ' | ' + r['relative_path']))
        if args.full:
            print(text)
        else:
            print('GOVERNS: ' + json.dumps(r['governs_subjects'], ensure_ascii=False))
            rels = runpy.run_path(str(HERE / 'CA-P-956-source-cases.py'))['relations'](text)
            print('RELATIONS: ' + json.dumps(rels, ensure_ascii=False))
            print(body.strip())


if __name__ == '__main__':
    main()
