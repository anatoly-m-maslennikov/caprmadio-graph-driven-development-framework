#!/usr/bin/env python3
"""Non-authoritative, read-only source audit; writes only CA-P-960 evidence via apply_patch.

No source, settings, archive, journal, Git, runtime, or generated methodology writes.
Classification is supplied by complete-Claim human/agent review, never keyword inference.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())
SOURCES = ROOT / '.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
OWNERS = ('001_CORE_META_MODEL', '003_LOCAL_CONFIGURATION')
ROLES = {'04_requirement': 'Requirement', '05_method': 'Method', '06_evaluation': 'Evaluation', '07_delivery': 'Delivery'}
INACTIVE = {'archive', 'draft', 'drafts', 'done', 'solved'}
CATEGORIES = {'N': 'justified_non_D_contribution', 'C': 'carrier_specification_outside_D', 'X': 'mixed_role_carrier_claim', 'D': 'existing_D_authority', 'U': 'unresolved_classification'}

def scalar(header, key):
    match = re.search(r'^' + re.escape(key) + r':\s*(.+)$', header, re.M)
    if not match:
        return None
    value = match.group(1).strip().strip('"\'')
    return int(value) if key == 'version' and value.isdigit() else value

def record(path):
    data = path.read_bytes()
    text = data.decode('utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    if not match:
        raise ValueError(f'Missing frontmatter: {path}')
    header, body = match.group(1), text[match.end():]
    explicit = scalar(header, 'atom_id')
    inferred = re.match(r'^([A-Z][A-Z0-9_]*(?:-[A-Z][A-Z0-9_]*)*-\d+)(?=-|\.md$)', path.name)
    if not explicit and not inferred:
        raise ValueError(f'Unresolved identity: {path}')
    identity = explicit or inferred.group(1)
    role_dir = next(x for x in path.parts if x in ROLES)
    return {
        'source_path': str(path.relative_to(ROOT)),
        'canonical_identity': identity,
        'identity_basis': 'explicit_atom_id' if explicit else 'stable_filename_identifier_prefix',
        'explicit_atom_id': explicit,
        'version': scalar(header, 'version'),
        'sha256': hashlib.sha256(data).hexdigest(),
        'byte_count': len(data),
        'source_owner': next(x for x in path.parts if x in OWNERS),
        'current_content_role': ROLES[role_dir],
        'local_tier_filename_marker': next((v.title() for v in ('CORE', 'GENERAL', 'STANDARD') if f'-{v}-' in path.name), 'Standard (unmarked; CA-D-285)'),
        'frontmatter_text': header,
        'complete_claim_body': body,
        'complete_source_text': text,
    }

def membership():
    active, excluded = [], []
    for owner in OWNERS:
        for path in sorted((SOURCES / owner).rglob('*.md')):
            relative = path.relative_to(SOURCES / owner)
            role = next((p for p in relative.parts if p in ROLES), None)
            inactive = next((p for p in relative.parts if p in INACTIVE), None)
            if role and not inactive:
                active.append(path)
            else:
                excluded.append({'source_path': str(path.relative_to(ROOT)), 'reason': f'inactive lifecycle placement: {inactive}' if inactive else 'outside RMED directories'})
    return active, excluded

def load(name):
    return json.loads((HERE / ('CA-P-960-' + name + '.json')).read_text())

def save(name, data):
    path = HERE / ('CA-P-960-' + name + '.json')
    content = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    # All evidence changes use apply_patch. The target is confined to this Task's prefix.
    rel = str(path.relative_to(ROOT))
    if path.exists():
        previous = path.read_text()
        patch = '*** Begin Patch\n*** Update File: ' + rel + '\n@@\n' + ''.join('-' + s + '\n' for s in previous.splitlines()) + ''.join('+' + s + '\n' for s in content.splitlines()) + '*** End Patch\n'
    else:
        patch = '*** Begin Patch\n*** Add File: ' + rel + '\n' + ''.join('+' + s + '\n' for s in content.splitlines()) + '*** End Patch\n'
    subprocess.run(['apply_patch'], input=patch, text=True, cwd=ROOT, check=True, capture_output=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('snapshot', 'metadata', 'show', 'build', 'verify', 'summary'))
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int, default=698)
    args = parser.parse_args()
    if args.command == 'snapshot':
        if (HERE / 'CA-P-960-snapshot.json').exists():
            raise SystemExit('Snapshot exists; do not overwrite reviewed baseline.')
        paths, excluded = membership()
        records = [record(path) for path in paths]
        save('snapshot', {'task': 'CA-P-960@2', 'scope': list(OWNERS), 'source_count': len(records), 'records': records, 'excluded': excluded})
        print(json.dumps({'source_count': len(records), 'roles': Counter(r['current_content_role'] for r in records), 'owners': Counter(r['source_owner'] for r in records), 'excluded_count': len(excluded)}))
    elif args.command == 'metadata':
        snapshot = load('snapshot')
        for item in snapshot['records']:
            live = record(ROOT / item['source_path'])
            if live['sha256'] != item['sha256']:
                raise ValueError('Source changed; metadata refresh must not replace reviewed bytes.')
            item['local_tier_filename_marker'] = live['local_tier_filename_marker']
        save('snapshot', snapshot)
        print('Corrected filename-tier interpretation only; captured source bytes and digests preserved.')
    elif args.command == 'show':
        for index, item in enumerate(load('snapshot')['records'][args.start:args.end], args.start):
            print(f"\n[{index}] {item['canonical_identity']}@{item['version']} {item['source_path'].split('/')[-1]}")
            print(item['complete_claim_body'].replace('**', ''))
    elif args.command == 'build':
        snapshot = load('snapshot')
        decisions = load('reviews')
        by_id = {}
        for row in decisions:
            identity, code, rationale = row[:3]
            if identity in by_id or code not in CATEGORIES or not rationale:
                raise ValueError(f'Invalid or duplicate review: {row}')
            by_id[identity] = {'category': CATEGORIES[code], 'rationale': rationale, 'confidence_percent': row[3] if len(row) > 3 else 99, 'related_authority_or_overlap': row[4] if len(row) > 4 else []}
        records = snapshot['records']
        identities = [r['canonical_identity'] for r in records]
        if len(identities) != len(set(identities)):
            raise ValueError('Duplicate source identity')
        if set(identities) != set(by_id):
            raise ValueError(f"Review membership mismatch. Missing: {sorted(set(identities)-set(by_id))}; extra: {sorted(set(by_id)-set(identities))}")
        for item in records:
            item['disposition'] = by_id[item['canonical_identity']]
            item['complete_claim_review'] = {'reviewed': True, 'evidence_field': 'complete_claim_body', 'reviewed_sha256': item['sha256'], 'method': 'Every complete body read from immutable source snapshot; emphasis delimiters removed for display only. Per-identity semantic rationale entered separately; no keyword-generated dispositions.'}
        snapshot['records'] = records
        snapshot['counts'] = dict(Counter(r['disposition']['category'] for r in records))
        snapshot['authority_basis'] = ['CA-R-1339@3', 'CA-R-1340@3', 'CA-R-1341@3', 'CA-R-1342@3', 'current Project Principles, especially CA-M-001@9, CA-M-002@12, CA-M-006@7, CA-P-033@9']
        snapshot['admission_note'] = 'Audit classification is evidence for CA-P-961, not approved source disposition. Items below confidence 99 remain unresolved; no source changes authorized by this inventory.'
        save('inventory', snapshot)
        print(json.dumps(snapshot['counts']))
    elif args.command == 'verify':
        inventory = load('inventory')
        paths, excluded = membership()
        current = {r['source_path']: r for r in map(record, paths)}
        stored = {r['source_path']: r for r in inventory['records']}
        failures = []
        if set(current) != set(stored):
            failures.append({'membership_added': sorted(set(current)-set(stored)), 'membership_missing': sorted(set(stored)-set(current))})
        for path, item in stored.items():
            live = current.get(path)
            if live is None:
                continue
            for field in ('canonical_identity', 'version', 'source_path', 'sha256'):
                if item.get(field) in (None, ''):
                    failures.append({'path': path, 'missing_independent_field': field})
                if item.get(field) != live.get(field):
                    failures.append({'path': path, 'changed_independent_field': field})
            for field in ('complete_source_text', 'complete_claim_body', 'frontmatter_text', 'current_content_role'):
                if item.get(field) != live.get(field):
                    failures.append({'path': path, 'changed_evidence_field': field})
            if hashlib.sha256(item['complete_source_text'].encode()).hexdigest() != item['sha256']:
                failures.append({'path': path, 'invalid_captured_source_digest': True})
            review = item.get('complete_claim_review', {})
            if not review.get('reviewed') or review.get('reviewed_sha256') != item['sha256'] or not item.get('disposition', {}).get('rationale'):
                failures.append({'path': path, 'missing_or_stale_review': True})
        identities = [r['canonical_identity'] for r in stored.values()]
        if len(identities) != len(set(identities)):
            failures.append({'duplicate_identity': True})
        for owner in ('CA-D-270', 'CA-D-310'):
            matches = [r for r in stored.values() if r['canonical_identity'] == owner]
            if len(matches) != 1 or matches[0]['disposition']['category'] != 'existing_D_authority':
                failures.append({'existing_D_owner_missing': owner})
        result = {'task': 'CA-P-960@2', 'result': 'PASS' if not failures else 'FAIL', 'source_count': len(current), 'reviewed_count': len(stored), 'source_bytes_preserved': sum(r['byte_count'] for r in stored.values()), 'independent_fields_checked': ['canonical_identity', 'version', 'source_path', 'sha256'], 'complete_evidence_compared': True, 'all_source_hashes_preserved': not any('changed_independent_field' in f and f['changed_independent_field'] == 'sha256' for f in failures), 'review_count_by_category': dict(Counter(r['disposition']['category'] for r in stored.values())), 'below_threshold_questions': [r['canonical_identity'] for r in stored.values() if r['disposition']['confidence_percent'] < 99], 'failures': failures}
        save('verification', result)
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if not failures else 1)
    elif args.command == 'summary':
        inventory = load('inventory')
        for r in inventory['records']:
            d = r['disposition']
            if d['category'] not in ('justified_non_D_contribution', 'existing_D_authority') or d['confidence_percent'] < 99:
                print(json.dumps({'id': r['canonical_identity'], 'version': r['version'], **d}))

if __name__ == '__main__':
    main()
