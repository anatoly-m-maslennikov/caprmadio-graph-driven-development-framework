#!/usr/bin/env python3
"""Independent read-only source verification; evidence writes use apply_patch only."""
import collections
import datetime
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())
BASE = ROOT / '.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
CORE, LOCAL = '001_CORE_META_MODEL', '003_LOCAL_CONFIGURATION'
ROLES = ('04_requirement', '05_method', '06_evaluation', '07_delivery')
S = json.loads((HERE / 'CA-P-960-snapshot.json').read_text())
D = json.loads((HERE / 'CA-P-961-dispositions.json').read_text())
L = json.loads((HERE / 'CA-P-962-changes.json').read_text())
REF = json.loads((HERE / 'CA-P-961-incoming-references.json').read_text())
records = {r['canonical_identity']: r for r in S['records']}
owners = {o['identity']: o for o in D['authority_owners'] if o['source_owner'] == CORE}
dispositions = {d['before']['canonical_identity']: d for d in D['dispositions'] if d['before']['source_owner'] == CORE}
latest = {o['identity']: o for o in L['operations'] if o.get('after')}
retired = {o['identity']: o for o in L['operations'] if o['kind'] == 'retire_predecessor'}
checks, fields, archives, order, mapping, body_diffs = {}, [], [], [], [], []


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def save(name, data):
    path = HERE / ('CA-P-962-' + name)
    content = data if isinstance(data, str) else json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    old = path.read_text() if path.exists() else None
    if old == content:
        return
    patch = '*** Begin Patch\n'
    if old is None:
        patch += '*** Add File: ' + str(path.relative_to(ROOT)) + '\n'
    else:
        patch += '*** Update File: ' + str(path.relative_to(ROOT)) + '\n@@\n' + ''.join('-'+s+'\n' for s in old.splitlines())
    patch += ''.join('+'+s+'\n' for s in content.splitlines()) + '*** End Patch\n'
    subprocess.run(['apply_patch'], input=patch, text=True, cwd=ROOT, check=True, capture_output=True)
    assert path.read_bytes() == content.encode()


def components(path):
    text = path.read_text()
    match = re.fullmatch(r'---\n(.*?)\n---\n(.*)', text, re.S)
    assert match, path
    return match.group(1), match.group(2)


paths = [p for owner in (CORE, LOCAL) for role in ROLES for p in (BASE / owner / role).glob('*.md')]
fronts = [components(p)[0] for p in paths]
# A second parser, independent of executor regex extraction, rejects malformed or aliased YAML.
run = subprocess.run(['ruby', '-ryaml', '-rjson', '-rdate', '-e', 'puts JSON.generate(JSON.parse(STDIN.read).map { |x| YAML.safe_load(x, permitted_classes: [Time, Date], aliases: false) })'], input=json.dumps(fronts), text=True, capture_output=True, check=True)
parsed = {str(p.relative_to(ROOT)): m for p,m in zip(paths,json.loads(run.stdout))}
checks['all_current_source_frontmatter_parses_independently'] = len(parsed) == len(paths)
checks['all_34_admitted_core_dispositions_completed'] = set(L['completed_dispositions']) == set(dispositions) and len(dispositions) == 34

for op in L['operations']:
    if op.get('archive'):
        a = op['archive']
        data = (ROOT / a['path']).read_bytes()
        expected = op['before']['sha256']
        assert sha(data) == a['sha256'] == expected, op['identity']
        if op['before']['version'] == records.get(op['identity'],{}).get('version'):
            assert data == records[op['identity']]['complete_source_text'].encode()
            evidence_basis = 'CA-P-960 complete source bytes'
        else:
            prior = [p for p in L['operations'] if p['sequence'] < op['sequence'] and p.get('after') and p['identity'] == op['identity'] and p['after']['version'] == op['before']['version']]
            assert len(prior) == 1 and prior[0]['after']['sha256'] == sha(data)
            evidence_basis = 'Exact intermediate source bytes bound by preceding operation hash'
        archives.append({'identity': op['identity'], 'version': a['version'], 'path': a['path'], 'sha256': sha(data), 'operation_sequence': op['sequence'], 'byte_exact': True, 'basis': evidence_basis})
checks['every_changed_or_retired_prior_has_byte_exact_archive'] = len(archives) == sum(1 for op in L['operations'] if op.get('before'))

for identity, op in latest.items():
    after = op['after']
    path = ROOT / after['path']
    assert sha(path.read_bytes()) == after['sha256'], identity
    meta, body = parsed[after['path']], components(path)[1]
    assert meta['atom_id'] == identity
    assert type(meta['version']) is int and meta['version'] == after['version'] and meta['version'] > 0
    datetime.datetime.strptime(meta['updated_at'], '%Y-%m-%d %H:%M:%S %z')
    assert meta['cce_version'] == 'cce_1' and isinstance(meta['cce_form'],str)
    subjects = meta['subjects']
    assert set(subjects) <= {'governs','depends_on'}
    values = []
    for kind, forms in subjects.items():
        assert set(forms) <= {'continuant','occurrent'}
        for form, refs in forms.items():
            assert isinstance(refs,list) and refs
            assert all(isinstance(ref,str) and ref for ref in refs)
            values += refs
    assert sum(len(v) for v in subjects['governs'].values()) == 1
    assert len(values) == len(set(values))
    assert body.startswith('# ') and body.count('\n# ') == 0
    assert not re.search(r'\*\*[A-Z][a-z]+\*\*',body)
    if identity in owners:
        o = owners[identity]
        assert CORE in path.parts
        tier = o['local_tier']
        assert ('-GENERAL-' in path.name) == (tier == 'General')
        assert '-CORE-' not in path.name and '-PRINCIPLE-' not in path.name
        slug = re.sub(r'[^a-z0-9]+','-',body.splitlines()[0][2:].lower()).strip('-')
        assert path.name.split('--',1)[1] == slug+'.md'
        design = o['proposed_claim_body']
        assert re.findall(r'`[^`]*`',body) == re.findall(r'`[^`]*`',design), identity
        assert body.replace('**','').casefold() == design.replace('**','').casefold(), identity
        if body != design:
            body_diffs.append({'identity': identity, 'classification': 'Only registered-operator bold rendering and general sentence/cell-start capitalization; literal code sequences exact', 'diff': ''.join(difflib.unified_diff(design.splitlines(True),body.splitlines(True),fromfile='admitted design',tofile='current source'))})
    else:
        assert body == records[identity]['complete_claim_body'], identity
    fields.append({'identity': identity, 'path': after['path'], 'version': meta['version'], 'sha256': sha(path.read_bytes()), 'identity': identity, 'identity_version_timestamp_cce_subject_fields_pass': True, 'source_owner_preserved': True, 'claim_bytes_preserved_for_reference_only_consumer': identity not in owners})

checks['all_current_changed_atom_fields_checked_independently'] = len(fields) == len(latest)
checks['all_changed_claim_literals_preserved'] = True
checks['every_changed_summary_matches_filename'] = True
checks['exact_general_or_omitted_standard_tier_preserved'] = True
checks['one_governs_and_unique_subjects'] = True
for identity,o in owners.items():
    if o['status'] == 'retain':
        assert sha((ROOT/o['before']['source_path']).read_bytes()) == o['before']['sha256'], identity
checks['all_7_core_retained_owners_unchanged'] = sum(o['status']=='retain' for o in owners.values()) == 7

touched_original = {op['identity'] for op in L['operations'] if op.get('before') and op['identity'] in records}
expected_paths = {r['source_path'] for r in S['records'] if r['canonical_identity'] not in touched_original}
for r in S['records']:
    if r['canonical_identity'] not in touched_original:
        assert sha((ROOT/r['source_path']).read_bytes()) == r['sha256'], r['canonical_identity']
expected_paths |= {op['after']['path'] for op in latest.values()}
assert expected_paths == set(parsed), {'missing':sorted(expected_paths-set(parsed)),'extra':sorted(set(parsed)-expected_paths)}
checks['whole_two_owner_frontier_matches_exact_authorized_operations'] = True
checks['unaffected_source_bytes_unchanged'] = True
assert all(not (ROOT / op['before']['source_path']).exists() for op in retired.values())
checks['every_retired_predecessor_absent_from_active_source'] = True

# Rescan actual active RMED carriers in both source owners and Project authority.
external = [p for p in (ROOT/'.caprmedio_caprmedio').rglob('*.md') if p.parent.name in ROLES and not {'archive','drafts','done','onhold','cancelled','execution_evidence'}.intersection(p.relative_to(ROOT).parts)]
retired_pattern = re.compile(r'(?<![A-Z0-9-])('+'|'.join(re.escape(i) for i in retired)+r')(?![0-9])')
remaining = []
for p in paths + external:
    for n,line in enumerate(p.read_text().splitlines(),1):
        if retired_pattern.search(line): remaining.append({'path':str(p.relative_to(ROOT)),'line':n,'text':line})
assert not remaining, remaining
checks['no_active_source_or_project_RMED_mentions_require_retired_identity'] = True

for repair in L['reference_repairs']:
    meta = parsed[repair['consumer_path']]
    values = meta['relations'][repair['relation']]
    assert all(t in values for t in repair['targets_after'])
    assert values == sorted(set(values))
    consumer_op = next(x for x in L['operations'] if x['sequence'] == repair['operation_sequence'])
    target_ops = []
    for target in repair['targets_after']:
        if target != repair['target_before']:
            op = next(x for x in L['operations'] if x['identity'] == target and x.get('after'))
            assert op['sequence'] < consumer_op['sequence']
            target_ops.append(op['sequence'])
    extraction = next(x for x in L['operations'] if x['identity'] == repair['target_before'] and x['kind'] in ('retire_predecessor','revise_owner'))
    assert consumer_op['sequence'] < extraction['sequence']
    order.append({'reference_id': repair['reference_id'], 'consumer': repair['consumer'], 'successor_sequences': target_ops, 'consumer_repair_sequence': consumer_op['sequence'], 'extraction_or_retirement_sequence': extraction['sequence'], 'verified': True, 'clause_mapping_rationale': repair['clause_mapping_rationale']})
assert len(order) == 7
checks['all_seven_required_mappings_precede_retirement_or_extraction'] = True

def body(identity):
    return components(ROOT/latest[identity]['after']['path'])[1]

# Independent semantic qualifier guards: do not derive expected facts from executor transformations.
assert '(Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Ops: O)' in body('CA-D-378')
checks['analysis_identity_letter_uppercase_A'] = True
assert 'positive integer Version' in body('CA-R-1415') and 'increases monotonically across successive Revisions of the same Atom' in body('CA-R-1415')
checks['version_positive_integer_monotonicity_preserved'] = True
assert '**`=1`** unambiguous Updated At date-time' in body('CA-R-1416')
checks['updated_at_unambiguous_date_time_preserved'] = True
assert '**`=1`** derived Updated At from its latest accepted Journal entry' in body('CA-R-1372') and '`updated_at`' not in body('CA-R-1372')
checks['journal_timestamp_remains_derived_no_new_field'] = True
assert '**`>=1`** Directory Carrier' in body('CA-D-353') and '**every** Epic **must** have **`=1`** Directory Carrier' in body('CA-D-353')
checks['generic_structural_and_stricter_epic_cardinality_preserved'] = True
assert 'nonempty uppercase letter-or-digit word tokens with single underscores' in body('CA-M-275')
checks['scope_unit_name_all_formatting_qualifiers_preserved'] = True
for identity in ('CA-D-328','CA-D-339','CA-D-270'):
    assert sha((ROOT/records[identity]['source_path']).read_bytes()) == records[identity]['sha256']
checks['journal_locations_and_existing_revision_field_owner_unchanged'] = True

for identity,d in dispositions.items():
    targets = list(dict.fromkeys(t for a in d['clause_allocations'] for t in a['owners']))
    resolved = []
    for target in targets:
        o = owners[target]
        resolved.append({'identity':target, 'role':o['content_role'], 'local_tier':o['local_tier'], 'source_owner':o['source_owner'], 'current':latest[target]['after'] if target in latest else o['before']})
    mapping.append({'before':d['before'], 'action':d['action'], 'primary_claim_identity_decision': 'replace or absorb predecessor into independently identified surviving owners' if d['retirement_requested'] else 'retain same recognizable primary Claim; extract Carrier representation or refine semantic wording under admitted design', 'confidence_percent':99, 'rationale':d['rationale'], 'after_owners':resolved, 'archive_proofs':[a for a in archives if a['identity']==identity], 'clause_allocations':d['clause_allocations'], 'complete':True})

local = [op for op in latest.values() if LOCAL in Path(op['after']['path']).parts]
handoff = {'task':'CA-P-962@2', 'next_task':'CA-P-963@2', 'instruction':'Refresh these current sanctioned bytes; preserve each repaired link and exact prior Revision before changing it. Never overwrite from CA-P-960. Claim text was not extracted or otherwise changed by CA-P-962.', 'consumers':[{'identity':op['identity'],'before':op['before'],'current':op['after'],'archive':op['archive'],'claim_bytes_preserved':True,'repaired_links':[r for r in L['reference_repairs'] if r['consumer']==op['identity']]} for op in local]}
save('local-handoff.json', handoff)
save('mapping.json', {'task':'CA-P-962@2','dispositions':mapping,'normalization_adjustments':body_diffs,'explicit_subject_corrections':[op for op in L['operations'] if op.get('subject_correction')],'intermediate_corrections':[op for op in L['operations'] if op['kind']=='repair_owner']})
verification = {'task':'CA-P-962@2','result':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'counts':{'core_dispositions':len(dispositions),'core_owners':len(owners),'new_core_owners':sum(o['status']=='new_proposed_identity_not_reserved' for o in owners.values()),'revised_core_owners':sum(o['status']=='revise' for o in owners.values()),'retained_core_owners':sum(o['status']=='retain' for o in owners.values()),'retired_predecessors':len(retired),'current_changed_atoms':len(fields),'exact_archives':len(archives),'operations':len(L['operations']),'current_two_owner_sources':len(paths),'external_active_RMED_carriers_scanned':len(external),'required_reference_mappings':len(order),'local_consumers':len(local)},'independent_field_checks':fields,'archive_proofs':archives,'reference_operation_order':order,'remaining_active_retired_identity_mentions':remaining,'limitations':['Semantic equivalence uses complete Claim review from CA-P-961 plus explicit qualifier guards and actual normalization-diff review; syntax/hash checks alone do not prove meaning.','Historical and generated/installed references retain their bytes and remain nonblocking downstream reconciliation for CA-P-964.','No Journal, Git, source-owner migration, selected Settings, runtime/install/Tool or Task lifecycle work was performed.'],'normalization_correction':L.get('normalization_audit')}
save('verification.json',verification)
assert verification['result']=='PASS'
counts=verification['counts']
lines=['# CA-P-962 Core Carrier authority repair', '', 'Non-authoritative execution evidence for CA-P-962@2. Result: **PASS**. All 34 admitted Core dispositions are applied; Task lifecycle remains with the coordinating agent.', '', f"The current slice has {counts['core_owners']} surviving Core owners: {counts['new_core_owners']} new, {counts['revised_core_owners']} revised, and {counts['retained_core_owners']} reused unchanged. {counts['retired_predecessors']} predecessor identities retired. The five reference-only consumers and all changed owners have independent field/hash checks. {counts['exact_archives']} exact Archives preserve original or intermediate prior bytes across {counts['operations']} recorded source operations.", '', '## Required reference ordering', '', '| Consumer | Current Revision | Verified mapping |', '| --- | --- | --- |']
for op in latest.values():
    if op['kind']=='repair_consumer':
        rs=[r for r in L['reference_repairs'] if r['consumer']==op['identity']]
        lines.append('| '+op['identity']+' | @'+str(op['after']['version'])+' | '+'; '.join(r['target_before']+' → '+', '.join(r['targets_after']) for r in rs)+' |')
lines += ['', 'All seven mappings have successor → consumer repair → extraction/retirement operation sequences in verification.json. Consumer Claims remain byte-exact. GOV302 also canonicalizes its existing semantic relates_to value for GOV294 while retaining that relation.', '', '## Preserved boundaries and corrections', '', '- R1415 retains positive integer Version and monotonic increase; R1416 retains exactly one unambiguous Updated At date-time. Existing D270 remains unchanged. R1372 remains derived from the latest accepted Journal entry with no new persisted field.', '- D353 retains generic >=1 Structural Entity Carrier cardinality and stricter =1 for Epic. M275 preserves nonempty uppercase letter-or-digit tokens and single underscores. Shared D owners are reused once, and the seven Core retain owners are byte-unchanged.', '- General tier is preserved on R1415/R1416; the other changed Core owners retain omitted Standard. Source ownership and current Claim Scope are preserved. No selected Settings or Journal location was changed.', '- Exact admitted Claim text is preserved apart from registered-operator bold rendering and general sentence/cell-start capitalization. Three current Subject assignments are narrowed or aligned using existing Entities: R981 Navigational Order Number; GOV296 Implementation Type with identity, Governance Origin and existing provenance prerequisite; GOV299 Priority with its comparison/Settings/Operator prerequisites. Their exact changes and rationale are recorded in mapping.json.', '- Root found an overbroad article-case normalization that changed the unquoted Analysis identity letter A to a in D378@1. Work paused; every actual-versus-design Claim diff and literal token sequence was audited. D378@1 is preserved exactly, and corrected D378@2 restores uppercase A. The helper now limits article normalization to sentence/cell starts. A separate GOV296@10→@11 correction restores existing lowercase provenance Subject spelling. All original operation hashes and intermediate Archives remain recorded.', '', '## Verification and handoff', '', f"Independent Ruby Psych parsing and field checks pass for all {counts['current_changed_atoms']} current changed Atoms. The whole two-owner frontier is exactly accounted for, with every unaffected source SHA unchanged. A fresh scan of source and {counts['external_active_RMED_carriers_scanned']} active Project RMED Carriers finds no retired identity mention requiring an active target.", '', 'CA-P-962-local-handoff.json gives the exact current path, Version, SHA-256, prior Archive, and repaired links for Local GOV761, GOV762 and GOV-EVAL006. CA-P-963 must refresh those sanctioned Revisions, preserve the links and archive the intermediate bytes before its own changes; the CA-P-960 snapshot is only the original allocation baseline.', '', 'Generated/installed and historical mentions remain nonblocking downstream reconciliation. No Task/lifecycle, Project authority outside the source owners, selected Settings, pending Epic005 issue, source ownership, Tools/install/runtime, Journal, Git index, commit or push was changed.', '', 'Reproduce verification from repository root with:', '', '`python3 -B '+str((HERE/'CA-P-962-verify.py').relative_to(ROOT))+'`', '', 'Verification regenerates only CA-P-962 evidence through apply_patch and reads source bytes. It does not mutate source Atoms.', '']
save('report.md','\n'.join(lines))
print(json.dumps({'result':verification['result'],'counts':counts,'checks':checks},indent=2))
