#!/usr/bin/env python3
"""Confined CA-P-962 executor: all mutations use apply_patch; one disposition per run."""
import argparse
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())
BASE = ROOT / '.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
CORE = '001_CORE_META_MODEL'
LOCAL = '003_LOCAL_CONFIGURATION'
DESIGN = json.loads((HERE / 'CA-P-961-dispositions.json').read_text())
SNAP = json.loads((HERE / 'CA-P-960-snapshot.json').read_text())
RECORDS = {r['canonical_identity']: r for r in SNAP['records']}
OWNERS = {o['identity']: o for o in DESIGN['authority_owners'] if o['source_owner'] == CORE}
DISPOSITIONS = {d['before']['canonical_identity']: d for d in DESIGN['dispositions'] if d['before']['source_owner'] == CORE}
REFERENCES = json.loads((HERE / 'CA-P-961-incoming-references.json').read_text())['references']
REPAIRS = [r for r in REFERENCES if r.get('consumer_in_mutation_scope') and (r['classification'] == 'required_pre_retirement_repair' or r.get('required_before_extraction'))]
SUBJECT_CORRECTIONS = {
    'CA-R-981': {'governs': {'continuant': ['Navigational Order Number']}, 'depends_on': {'continuant': ['Scope Unit']}},
    'CAPRMEDIO-GOV-REQU-296': {'governs': {'continuant': ['Atom/Content Role: Implementation/Type']}, 'depends_on': {'continuant': ['Atom/Identity', 'Governance Origin', 'provenance']}},
    'CAPRMEDIO-GOV-REQU-299': {'governs': {'continuant': ['Priority']}, 'depends_on': {'continuant': ['Atom/Content Role: Concern', 'Scope Unit', 'Framework Instance Settings', 'Operator']}},
}
LOGPATH = HERE / 'CA-P-962-changes.json'
LOG = json.loads(LOGPATH.read_text()) if LOGPATH.exists() else {'task': 'CA-P-962@2', 'operations': [], 'completed_dispositions': [], 'reference_repairs': [], 'baseline': None}


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4))).strftime('%Y-%m-%d %H:%M:%S %z')


def rel(path):
    return str(Path(path).relative_to(ROOT))


def permitted(path):
    p = Path(path).resolve()
    if p.parent == HERE and p.name.startswith('CA-P-962-'):
        return
    assert any(p.is_relative_to(BASE / owner) for owner in (CORE, LOCAL)), p
    assert p.suffix == '.md' and '.env' not in p.name, p


def patch_files(changes):
    pieces = ['*** Begin Patch\n']
    for path, content in changes:
        path = Path(path)
        permitted(path)
        old = path.read_text() if path.exists() else None
        if old == content:
            continue
        if content is None:
            assert old is not None
            pieces.append('*** Delete File: ' + rel(path) + '\n')
        elif old is None:
            assert content.endswith('\n')
            pieces.append('*** Add File: ' + rel(path) + '\n' + ''.join('+' + line + '\n' for line in content.splitlines()))
        else:
            assert content.endswith('\n') and old.endswith('\n')
            pieces.append('*** Update File: ' + rel(path) + '\n@@\n' + ''.join('-' + line + '\n' for line in old.splitlines()) + ''.join('+' + line + '\n' for line in content.splitlines()))
    if len(pieces) == 1:
        return
    pieces.append('*** End Patch\n')
    run = subprocess.run(['apply_patch'], input=''.join(pieces), text=True, cwd=ROOT, capture_output=True)
    assert run.returncode == 0, run.stdout + run.stderr
    for path, content in changes:
        if content is None:
            assert not Path(path).exists()
        else:
            assert Path(path).read_bytes() == content.encode(), path


def save_log():
    patch_files([(LOGPATH, json.dumps(LOG, ensure_ascii=False, indent=2) + '\n')])


def split(text):
    match = re.fullmatch(r'---\n(.*?)\n---\n(.*)', text, re.S)
    assert match, text[:100]
    return match.group(1), match.group(2)


def top_block(front, key):
    found = re.search(r'^' + re.escape(key) + r':[^\n]*(?:\n[ \t]+[^\n]*)*', front, re.M)
    return found.group() if found else None


def set_block(front, key, value):
    old = top_block(front, key)
    block = key + ': ' + value if '\n' not in value else key + ':\n' + value
    return front.replace(old, block, 1) if old else front + '\n' + block


def subjects_block(subjects):
    lines = []
    for relation, forms in subjects.items():
        lines.append('  ' + relation + ':')
        for form, values in forms.items():
            if not values:
                continue
            lines.append('    ' + form + ':')
            lines += ['      - ' + json.dumps(v) for v in values]
    return '\n'.join(lines)


def relations_from(front):
    block = top_block(front, 'relations') or 'relations: {}'
    result = {}
    kind = None
    for line in block.splitlines()[1:]:
        if re.fullmatch(r'  [a-z_]+:', line):
            kind = line.strip()[:-1]
            result[kind] = []
        elif line.strip().startswith('- '):
            assert kind
            result[kind].append(line.strip()[2:].strip('\"\''))
        else:
            raise AssertionError(('unsupported relation syntax', line))
    return result


def relations_block(values):
    if not values:
        return '{}'
    return '\n'.join('  ' + kind + ':\n' + '\n'.join('    - ' + json.dumps(v) for v in sorted(set(targets))) for kind, targets in values.items())


def field(front, key):
    block = top_block(front, key)
    assert block is not None
    return block.split(':', 1)[1].strip().strip('\"\'')


def normalize_body(body):
    # Presentation-only correction required by live M229/M234/D280. Literal code is protected.
    ordinary = {'An': 'an', 'A': 'a', 'The': 'the', 'Its': 'its', 'One': 'one', 'They': 'they', 'These': 'these', 'For': 'for', 'Secrets': 'secrets', 'Production': 'production', 'Email': 'email', 'Deleting': 'deleting', 'Precise': 'precise', 'Distinct': 'distinct', 'Dependencies': 'dependencies', 'Canonical': 'canonical', 'Deterministic': 'deterministic', 'Consumer-ready': 'consumer-ready', 'Aggregated': 'aggregated', 'Accept': 'accept', 'Reject': 'reject', 'Confirm': 'confirm', 'Stop': 'stop'}
    operators = ('must not', 'not in', 'is not empty', 'is empty', 'starts with', 'ends with', 'otherwise', 'without', 'before', 'unless', 'until', 'after', 'every', 'means', 'contains', 'when', 'then', 'only', 'must', 'none', 'all', 'any', 'and', 'not', 'may', 'where', 'or', 'if', 'in', 'to')
    output = []
    for line in body.splitlines():
        if line.startswith('#') or re.match(r'^\|[ -]+\|', line):
            output.append(line)
            continue
        parts = re.split(r'(`[^`]*`|\*\*.*?\*\*)', line)
        for i in range(0, len(parts), 2):
            p = parts[i]
            for old, new in ordinary.items():
                # Sentence/cell starts only: never alter a mapped identity letter such as Analysis: A.
                p = re.sub(r'(^[ \t]*|[.!?][ \t]+|\|[ \t]+)' + re.escape(old) + r'\b', lambda m: m.group(1) + new, p)
            p = re.sub(r'(?<![A-Za-z_-])(' + '|'.join(operators) + r')(?![A-Za-z_-])', lambda m: '**' + m.group().lower() + '**', p, flags=re.I)
            parts[i] = p
        output.append(''.join(parts))
    return '\n'.join(output) + '\n'


def final_path(o, body):
    source = Path(o.get('proposed_path') or o['before']['source_path'])
    prefix = source.name.split('--', 1)[0]
    slug = re.sub(r'[^a-z0-9]+', '-', body.splitlines()[0][2:].lower()).strip('-')
    return ROOT / source.parent / (prefix + '--' + slug + '.md')


def source_path(identity):
    ops = [x for x in LOG['operations'] if x.get('identity') == identity and x.get('after')]
    return ROOT / (ops[-1]['after']['path'] if ops else RECORDS[identity]['source_path'])


def exact_archive(identity, text, source):
    front, _ = split(text)
    version = int(field(front, 'version'))
    path = source.parent / 'archive' / (source.stem + '@' + str(version) + '.md')
    if path.exists():
        assert path.read_bytes() == text.encode(), ('archive collision', path)
    else:
        patch_files([(path, text)])
    assert hashlib.sha256(path.read_bytes()).hexdigest() == sha(text)
    return {'path': rel(path), 'version': version, 'sha256': sha(text), 'byte_exact': True}


def active_sources():
    return [p for owner in (CORE, LOCAL) for role in ('04_requirement','05_method','06_evaluation','07_delivery') for p in (BASE / owner / role).glob('*.md')]


def active_mentions(identity):
    pattern = re.compile(r'(?<![A-Z0-9-])' + re.escape(identity) + r'(?![0-9])')
    found = []
    for p in active_sources():
        text = p.read_text()
        front, body = split(text)
        if (top_block(front, 'atom_id') and field(front, 'atom_id') == identity) or RECORDS.get(identity, {}).get('source_path') == rel(p):
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                found.append({'path': rel(p), 'line': number, 'text': line})
    return found


def id_available(identity):
    # Scan all text and filenames, including ignored paths, without following symlinks or secret paths.
    pattern = r'(?<![A-Z0-9-])' + re.escape(identity) + r'(?![0-9])'
    args = ['rg','--hidden','--no-ignore','--pcre2','-l','-g','!**/.git/**','-g','!**/.env','-g','!**/.env.*','-g','!**/*.env','-g','!**/.DS_Store','-g','!**/execution_evidence/**',pattern,'.']
    run = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    assert run.returncode in (0,1), run.stderr
    collisions = run.stdout.splitlines()
    files = subprocess.run(['rg','--files','--hidden','--no-ignore','-g','!**/.git/**','-g','!**/.env*','-g','!**/*.env','-g','!**/.DS_Store'], cwd=ROOT, text=True, capture_output=True, check=True).stdout.splitlines()
    collisions += [p for p in files if re.search(pattern, Path(p).name) and '/execution_evidence/' not in p]
    assert not collisions, ('identity unavailable', identity, collisions)
    return {'identity': identity, 'checked_at': now(), 'global_content_and_filename_collisions': []}


def check_atom(path, expected_identity, expected_version):
    text = path.read_text()
    front, body = split(text)
    assert field(front, 'atom_id') == expected_identity
    assert int(field(front, 'version')) == expected_version and expected_version > 0
    datetime.datetime.strptime(field(front, 'updated_at'), '%Y-%m-%d %H:%M:%S %z')
    assert field(front, 'cce_version') == 'cce_1'
    sb = top_block(front, 'subjects')
    assert sb
    governed = re.search(r'  governs:\n((?:    .*(?:\n|$))*)', sb)
    assert governed and len(re.findall(r'^      - ', governed.group(), re.M)) == 1, sb
    values = re.findall(r'^      - (.+)', sb, re.M)
    assert len(values) == len(set(v.strip('\"\'') for v in values)), sb
    assert body.startswith('# ') and body.count('\n# ') == 0
    assert not re.search(r'\*\*[A-Z][a-z]+\*\*', body)
    return {'identity': expected_identity, 'path': rel(path), 'version': expected_version, 'sha256': sha(text), 'subjects_one_governs_unique': True, 'metadata_valid': True}


def owner_ready(identity):
    o = OWNERS[identity]
    if o['status'] == 'retain':
        p = ROOT / o['before']['source_path']
        assert hashlib.sha256(p.read_bytes()).hexdigest() == o['before']['sha256']
        return
    if any(x.get('identity') == identity and x['kind'] in ('new_owner','revise_owner') for x in LOG['operations']):
        return
    body = normalize_body(o['proposed_claim_body'])
    path = final_path(o, body)
    archive = None
    old = None
    availability = None
    if o['status'] == 'new_proposed_identity_not_reserved':
        availability = id_available(identity)
        front = '\n'.join(['atom_id: ' + identity, 'cce_version: ' + o['proposed_cce_version'], 'cce_form: ' + o['proposed_cce_form'], 'subjects:\n' + subjects_block(o['proposed_subjects']), 'version: 1', 'updated_at: "' + now() + '"', 'relations: ' + relations_block(o.get('proposed_relations', {}))])
        front = front.replace('relations:   ', 'relations:\n  ')
    else:
        oldpath = ROOT / o['before']['source_path']
        old = oldpath.read_text()
        assert sha(old) == o['before']['sha256'], identity
        archive = exact_archive(identity, old, oldpath)
        front, _ = split(old)
        front = set_block(front, 'version', str(o['proposed_version']))
        front = set_block(front, 'updated_at', json.dumps(now()))
        front = set_block(front, 'cce_version', o['proposed_cce_version'])
        front = set_block(front, 'cce_form', o['proposed_cce_form'])
        if o.get('proposed_subjects'):
            front = set_block(front, 'subjects', subjects_block(o['proposed_subjects']))
        if identity in SUBJECT_CORRECTIONS:
            front = set_block(front, 'subjects', subjects_block(SUBJECT_CORRECTIONS[identity]))
        if identity == 'CAPRMEDIO-GOV-REQU-302':
            relations = relations_from(front)
            relations['relates_to'] = ['CAPRMEDIO-GOV-REQU-294' if v.startswith('CAPRMEDIO-GOV-REQU-294-') else v for v in relations['relates_to']]
            front = set_block(front, 'relations', relations_block(relations))
    new = '---\n' + front + '\n---\n' + body
    changes = [(path, new)]
    if old is not None and path != oldpath:
        assert not path.exists()
        changes.append((oldpath, None))
    patch_files(changes)
    after = check_atom(path, identity, o['proposed_version'])
    LOG['operations'].append({'sequence': len(LOG['operations']) + 1, 'kind': 'new_owner' if old is None else 'revise_owner', 'identity': identity, 'at': now(), 'before': o.get('before'), 'after': after, 'archive': archive, 'id_availability': availability, 'design_body_adjusted': body != o['proposed_claim_body'], 'design_body_sha256': sha(o['proposed_claim_body']), 'actual_body_sha256': sha(body), 'claim_and_subject_review': o.get('subjects_rationale',o['rationale']), 'subject_correction': SUBJECT_CORRECTIONS.get(identity), 'subject_correction_authority': 'CA-M-125 narrowest governed Entity and actual prerequisites; existing governed objects only' if identity in SUBJECT_CORRECTIONS else None, 'local_tier': o['local_tier']})
    save_log()


def repair_consumer(path):
    refs = [r for r in REPAIRS if r['consumer_path'] == path]
    if all(r['reference_id'] in [x['reference_id'] for x in LOG['reference_repairs']] for r in refs):
        return
    for r in refs:
        for target in r['proposed_targets']:
            if target in OWNERS and target != r['target_before']:
                owner_ready(target)
    source = ROOT / path
    old = source.read_text()
    assert sha(old) == refs[0]['consumer_sha256']
    front, body = split(old)
    identity = field(front, 'atom_id')
    archive = exact_archive(identity, old, source)
    relations = relations_from(front)
    for r in refs:
        values = relations[r['typed_relation']]
        selected = [v for v in values if v == r['target_before'] or v.startswith(r['target_before'] + '-')]
        assert len(selected) == 1
        relations[r['typed_relation']] = [v for v in values if v not in selected] + r['proposed_targets']
    version = int(field(front, 'version')) + 1
    front = set_block(front, 'relations', relations_block(relations))
    front = set_block(front, 'version', str(version))
    front = set_block(front, 'updated_at', json.dumps(now()))
    # Cross-owner slice changes only direct references and Revision metadata; Claims remain exact.
    patch_files([(source, '---\n' + front + '\n---\n' + body)])
    after = check_atom(source, identity, version)
    assert split(source.read_text())[1] == body
    operation = {'sequence': len(LOG['operations']) + 1, 'kind': 'repair_consumer', 'identity': identity, 'at': now(), 'before': {'path': path, 'version': version-1, 'sha256': sha(old)}, 'after': after, 'archive': archive, 'claim_bytes_preserved': True, 'reference_ids': [r['reference_id'] for r in refs]}
    LOG['operations'].append(operation)
    for r in refs:
        assert all(t in relations[r['typed_relation']] for t in r['proposed_targets'])
        LOG['reference_repairs'].append({'reference_id': r['reference_id'], 'consumer': identity, 'consumer_path': path, 'target_before': r['target_before'], 'targets_after': r['proposed_targets'], 'relation': r['typed_relation'], 'operation_sequence': operation['sequence'], 'clause_mapping_rationale': r['mapping_rationale'], 'targets_verified_before_extraction_or_retirement': True})
    save_log()


def apply_disposition(identity):
    assert identity in DISPOSITIONS
    if identity in LOG['completed_dispositions']:
        print(identity + ' already completed')
        return
    d = DISPOSITIONS[identity]
    path = ROOT / d['before']['source_path']
    assert sha(path.read_text()) == d['before']['sha256']
    targets = list(dict.fromkeys(o for a in d['clause_allocations'] for o in a['owners']))
    for target in targets:
        if target != identity:
            owner_ready(target)
    for r in REPAIRS:
        if r['target_before'] == identity:
            repair_consumer(r['consumer_path'])
    if d['retirement_requested']:
        pending = active_mentions(identity)
        assert not pending, ('active required reference', identity, pending)
        old = path.read_text()
        archive = exact_archive(identity, old, path)
        patch_files([(path, None)])
        LOG['operations'].append({'sequence': len(LOG['operations']) + 1, 'kind': 'retire_predecessor', 'identity': identity, 'at': now(), 'before': d['before'], 'after': None, 'archive': archive, 'successors': targets, 'active_required_mentions_before_retirement': pending})
    elif identity in OWNERS:
        owner_ready(identity)
    for target in targets:
        if OWNERS[target]['status'] != 'retain':
            op = next(x for x in LOG['operations'] if x.get('identity') == target and x.get('after'))
            check_atom(ROOT / op['after']['path'], target, op['after']['version'])
    LOG['completed_dispositions'].append(identity)
    save_log()
    print(identity + ': ' + d['action'] + ' PASS → ' + ', '.join(targets))


def baseline():
    assert LOG['baseline'] is None
    mismatches = [r['source_path'] for r in SNAP['records'] if not (ROOT/r['source_path']).exists() or hashlib.sha256((ROOT/r['source_path']).read_bytes()).hexdigest() != r['sha256']]
    assert not mismatches, mismatches
    expected = {r['source_path'] for r in SNAP['records']}
    current = {rel(p) for p in active_sources()}
    assert expected == current, {'added': sorted(current-expected),'removed': sorted(expected-current)}
    ids = [id_available(i) for i,o in OWNERS.items() if o['status'] == 'new_proposed_identity_not_reserved']
    LOG['baseline'] = {'at': now(), 'source_count': len(expected), 'source_sha256_mismatches': [], 'frontier_matches': True, 'new_core_id_availability': ids, 'source_baseline': 'CA-P-960-snapshot.json'}
    save_log()
    print('Baseline PASS: all 698 exact sources; new Core IDs globally available')


def repair_normalization():
    identity = 'CA-D-378'
    source = source_path(identity)
    old = source.read_text()
    front, body = split(old)
    assert int(field(front, 'version')) == 1
    assert body.count('Analysis: a,') == 1
    fixed = body.replace('Analysis: a,', 'Analysis: A,')
    assert fixed == OWNERS[identity]['proposed_claim_body']
    archive = exact_archive(identity, old, source)
    front = set_block(front, 'version', '2')
    front = set_block(front, 'updated_at', json.dumps(now()))
    patch_files([(source, '---\n' + front + '\n---\n' + fixed)])
    after = check_atom(source, identity, 2)
    LOG['operations'].append({'sequence': len(LOG['operations'])+1, 'kind': 'repair_owner', 'identity': identity, 'at': now(), 'before': {'path': rel(source), 'version': 1, 'sha256': sha(old)}, 'after': after, 'archive': archive, 'reason': 'Root spot-check caught unquoted Analysis identity letter changed by overbroad article case normalization. Restore exact admitted uppercase A. The original operation hashes and erroneous intermediate Revision remain preserved.', 'actual_body_sha256': sha(fixed), 'design_body_sha256': sha(OWNERS[identity]['proposed_claim_body']), 'design_body_adjusted': False})
    LOG['normalization_audit'] = {'result': 'PASS_AFTER_CORRECTION', 'scope': 'Every design-versus-actual Claim diff reviewed; every inline code literal remains exact; only unintended semantic change was Analysis A to a in D378, restored in version 2.', 'prevention': 'Case substitutions now match sentence or table-cell starts only; explicit Analysis A independent guard required by final verification.'}
    save_log()
    print('CA-D-378 correction PASS: exact version 1 Archive; uppercase Analysis A restored at version 2')


def repair_subject_spelling():
    identity = 'CAPRMEDIO-GOV-REQU-296'
    source = source_path(identity)
    old = source.read_text()
    front, body = split(old)
    version = int(field(front, 'version'))
    assert version == 10 and front.count('"Provenance"') == 1
    archive = exact_archive(identity, old, source)
    front = front.replace('"Provenance"', '"provenance"')
    front = set_block(front, 'version', str(version+1))
    front = set_block(front, 'updated_at', json.dumps(now()))
    patch_files([(source, '---\n' + front + '\n---\n' + body)])
    after = check_atom(source, identity, version+1)
    LOG['operations'].append({'sequence': len(LOG['operations'])+1, 'kind': 'repair_owner', 'identity': identity, 'at': now(), 'before': {'path': rel(source), 'version': version, 'sha256': sha(old)}, 'after': after, 'archive': archive, 'reason': 'Preserve the existing general Entity reference provenance spelling; do not invent a capitalized Governed Term. Primary Claim and other Subjects remain unchanged.', 'claim_bytes_preserved': True})
    save_log()
    print('GOV296 Subject spelling PASS at version 11; intermediate version 10 archived exactly')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['baseline','apply','prepare','repair-normalization','repair-subject-spelling','list'])
    parser.add_argument('identity', nargs='?')
    args = parser.parse_args()
    if args.action == 'baseline': baseline()
    elif args.action == 'apply': apply_disposition(args.identity)
    elif args.action == 'prepare': owner_ready(args.identity)
    elif args.action == 'repair-normalization': repair_normalization()
    elif args.action == 'repair-subject-spelling': repair_subject_spelling()
    else: print('\n'.join(DISPOSITIONS))


if __name__ == '__main__':
    main()
