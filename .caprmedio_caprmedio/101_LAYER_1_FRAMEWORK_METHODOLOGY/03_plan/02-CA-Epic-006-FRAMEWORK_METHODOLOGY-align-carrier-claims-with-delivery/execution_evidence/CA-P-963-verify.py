#!/usr/bin/env python3
"""Independent YAML and lossless-disposition checks; write only CA-P-963 evidence."""
import datetime
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('carrier_963', HERE/'CA-P-963-execute.py')
x = importlib.util.module_from_spec(spec)
spec.loader.exec_module(x)
u, ROOT, LOCAL, CORE = x.u, x.ROOT, x.LOCAL, x.CORE
L, OWNERS, DISPOSITIONS = x.LOG, x.OWNERS, x.DISPOSITIONS
baseline = {r['identity']:r for r in L['baseline']['sources']}
latest = {op['identity']:op['after'] for op in L['operations'] if op.get('after')}
retired = {op['identity']:op for op in L['operations'] if op['kind']=='retire_predecessor'}
checks, archives, field_checks, mappings, order = {}, [], [], [], []
assert set(L['completed_dispositions']) == set(DISPOSITIONS) and len(DISPOSITIONS)==16
checks['all_16_local_dispositions_applied'] = True

paths = u.active_sources()
fronts = [u.split(p.read_text())[0] for p in paths]
run = subprocess.run(['ruby','-ryaml','-rjson','-rdate','-e','puts JSON.generate(JSON.parse(STDIN.read).map { |x| YAML.safe_load(x, permitted_classes: [Time, Date], aliases: false) })'],input=json.dumps(fronts),text=True,capture_output=True,check=True)
parsed = {u.rel(p):meta for p,meta in zip(paths,json.loads(run.stdout))}
checks['all_current_frontmatter_parses_independently'] = len(parsed)==len(paths)

expected = dict(baseline)
for op in L['operations']:
    if op.get('before'):
        assert op['before']==baseline[op['identity']]
        a = op['archive']
        data = (ROOT/a['path']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==a['sha256']==op['before']['sha256']
        original = next((r for r in x.SNAP['records'] if r['canonical_identity']==op['identity']),None)
        if original and original['version']==op['before']['version']:
            assert data == original['complete_source_text'].encode()
        else:
            handoff = next(c for c in x.HANDOFF['consumers'] if c['identity']==op['identity'])
            assert a['sha256']==handoff['current']['sha256'] and a['version']==handoff['current']['version']
        archives.append({'identity':op['identity'],**a,'basis':'Exact pre-963 source bytes verified against the bound baseline; original960 or sanctioned962 handoff Revision'})
    if op.get('after'):
        expected[op['identity']]=op['after']
    else:
        del expected[op['identity']]
        assert not (ROOT/op['before']['path']).exists()
assert x.manifest()==sorted(expected.values(),key=lambda r:r['path'])
assert len(archives)==16 and len(paths)==714
assert all(before==expected[i] for i,before in baseline.items() if i not in latest and i not in retired)
checks['exact_whole_frontier_and_unaffected_bytes'] = True
checks['all_16_prior_revisions_byte_exact'] = True
checks['both_predecessors_retired_after_successor_establishment'] = len(retired)==2

def body(identity):
    return u.split((ROOT/(latest.get(identity) or baseline[identity])['path']).read_text())[1]

for identity,after in latest.items():
    path=ROOT/after['path']
    meta=parsed[after['path']]
    o=OWNERS[identity]
    assert x.check_atom(path,identity,after['version'])==after
    assert LOCAL in path.parts and path.parent.name==('07_delivery' if o['content_role']=='Delivery' else '04_requirement')
    assert '-CORE-' not in path.name and '-GENERAL-' not in path.name and '-PRINCIPLE-' not in path.name
    assert type(meta['version']) is int and meta['version']>0
    datetime.datetime.strptime(meta['updated_at'],'%Y-%m-%d %H:%M:%S %z')
    assert meta['cce_version']=='cce_1' and meta['cce_form']==o['proposed_cce_form']
    subjects=meta['subjects']
    assert set(subjects)<= {'governs','depends_on'}
    values=[]
    for kind,forms in subjects.items():
        assert set(forms)<={'continuant','occurrent'}
        for form,refs in forms.items():
            assert isinstance(refs,list) and refs and all(isinstance(r,str) and r for r in refs)
            values+=refs
    assert sum(len(v) for v in subjects['governs'].values())==1 and len(values)==len(set(values))
    if o.get('proposed_subjects'):
        assert subjects==o['proposed_subjects']
    if o['status']=='new_proposed_identity_not_reserved':
        assert meta['atom_id']==identity and re.fullmatch(r'CA-D-(39[6-9]|40[0-6])',identity)
        assert meta['relations']==o.get('proposed_relations',{}) or {k:sorted(v) for k,v in meta['relations'].items()}=={k:sorted(v) for k,v in o.get('proposed_relations',{}).items()}
    else:
        op=next(op for op in L['operations'] if op['identity']==identity)
        prior=u.split((ROOT/op['archive']['path']).read_text())[0]
        current=u.split(path.read_text())[0]
        allowed=['version','updated_at']+(['subjects'] if o.get('proposed_subjects') else [])
        for key in allowed:
            prior=prior.replace(u.top_block(prior,key),'')
            current=current.replace(u.top_block(current,key),'')
        assert current==prior,identity
    actual,design=body(identity),o['proposed_claim_body']
    assert re.findall(r'`[^`]*`',actual)==re.findall(r'`[^`]*`',design)
    # Independently allow only the exact sentence/cell-start case changes reviewed before execution.
    plain=design.replace('**','')
    replacements=[]
    if identity=='CAPRMEDIO-GOV-REQU-315':
        replacements=[('The policy','the policy'),('| An operation','| an operation'),('| A material','| a material'),('\nAn `ERROR`','\nan `ERROR`'),('\nProduction','\nproduction'),('. An exception','. an exception'),('. A production','. a production'),('. A component','. a component')]
    elif identity=='CAPRMEDIO-META-REQU-103':
        replacements=[('. A candidate','. a candidate')]
    for old,new in replacements:
        assert old in plain
        plain=plain.replace(old,new)
    assert actual.replace('**','')==plain,identity
    assert path.name.split('--',1)[1]==re.sub(r'[^a-z0-9]+','-',actual.splitlines()[0][2:].lower()).strip('-')+'.md'
    field_checks.append({**after,'source_owner_role_tier_identity_version_cce_subjects_and_summary_pass':True,'admitted_claim_literal_case_exact':True,'unrelated_metadata_and_contributions_exact':o['status']!='new_proposed_identity_not_reserved'})
checks['all_25_changed_atoms_have_independent_fields_and_claim_checks'] = len(field_checks)==25
checks['all_type_admission_contributions_and_unrelated_metadata_preserved'] = True
checks['one_governs_exact_admitted_subjects_standard_tier_and_source_owner'] = True

for i,o in OWNERS.items():
    if i not in latest:
        assert hashlib.sha256((ROOT/baseline[i]['path']).read_bytes()).hexdigest()==baseline[i]['sha256']
checks['shared_D328_and_Core_D339_reused_unchanged'] = True
for c in x.HANDOFF['consumers']:
    current=latest.get(c['identity']) or baseline[c['identity']]
    for repair in c['repaired_links']:
        values=parsed[current['path']]['relations'][repair['relation']]
        assert all(t in values for t in repair['targets_after'])
        for target in repair['targets_after']:
            assert target in expected
    if c['identity']=='CAPRMEDIO-GOV-EVAL-006':
        assert current['sha256']==c['current']['sha256']
checks['all_sanctioned962_links_preserved_and_resolve'] = True

for identity in retired:
    assert not x.active_mentions(identity)
for sequence in L['disposition_sequences']:
    extraction=sequence['extraction_or_retirement_sequence']
    for successor in sequence['successors_verified_before_extraction_or_retirement']:
        operation=next((o for o in L['operations'] if o['identity']==successor['identity'] and o.get('after')),None)
        assert not operation or operation['sequence']<extraction
    order.append({**sequence,'verified':True})
checks['all_successors_precede_extraction_or_retirement_no_active_required_retired_mentions'] = len(order)==16
assert 'whose append-only NDJSON representation is **not** already governed by CA-D-328 **or** CA-D-339' in body('CA-D-406')
assert 'in** its applicable registered authoritative place' in body('CA-D-406')
assert 'role folders' not in body('CAPRMEDIO-GOV-REQU-315') and '.caprmedio_caprmedio/work_journal/' in body('CA-D-328')
assert 'under its Implementation Content Role directory as append-only NDJSON segments' in body('CA-D-339')
assert 'where** applicable' in body('CA-D-396') and 'UTC timestamp' in body('CA-D-396')
assert all(t in body('CA-D-398') for t in ('optional machine-readable contribution','faithfully represents','current Operator-selected Project identity','Framework Instance Settings','`project_settings`'))
checks['journal_domain_logging_scope_and_configuration_exclusions_preserved'] = True
assert x.index_sha()==x.INDEX_SHA
checks['git_index_unchanged'] = True

for identity,d in DISPOSITIONS.items():
    targets=list(dict.fromkeys(i for a in d['clause_allocations'] for i in a['owners']))
    mappings.append({'identity':identity,'original_design_before':d['before'],'execution_before':baseline[identity],'action':d['action'],'confidence_percent':99,'rationale':d['rationale'],'primary_claim_identity_decision':'successor replaces carrier-only predecessor' if d['retirement_requested'] else 'retain recognizable semantic primary Claim and extract Carrier specification','after_owners':[{'identity':i,'source_owner':OWNERS[i]['source_owner'],'content_role':OWNERS[i]['content_role'],'local_tier':OWNERS[i]['local_tier'],'current':latest.get(i) or baseline[i]} for i in targets],'clause_allocations':[{k:a[k] for k in ('before_quote','owners','rationale')} for a in d['clause_allocations']],'archive_proofs':[a for a in archives if a['identity']==identity],'complete':True})

counts={'local_dispositions':16,'new_local_delivery_owners':11,'revised_local_owners':14,'retired_local_predecessors':2,'reused_local_owners':1,'reused_core_owners':1,'current_changed_atoms':25,'exact_archives':16,'operations':len(L['operations']),'current_sources':len(paths),'current_core_sources':sum(CORE in p.parts for p in paths),'current_local_sources':sum(LOCAL in p.parts for p in paths)}
verification={'task':'CA-P-963@2','result':'PASS','checks':checks,'counts':counts,'independent_field_checks':field_checks,'archive_proofs':archives,'disposition_operation_order':order,'limitations':['Semantic allocation follows approved961 complete Claims; independent syntax/hash/literal and qualifier checks support but do not prove semantic equivalence.','Generated/installed and historical mentions remain nonblocking downstream reconciliation. No runtime or Projection rebuild is claimed.']}
handoff={'task':'CA-P-963@2','next_task':'CA-P-964','result':'PASS','counts':counts,'retired_identity_successors':{i:op['successors'] for i,op in retired.items()},'new_delivery_owners':[after for i,after in latest.items() if OWNERS[i]['status']=='new_proposed_identity_not_reserved'],'local962_consumers_current':[latest.get(c['identity']) or baseline[c['identity']] for c in x.HANDOFF['consumers']],'required_reference_repairs_remaining':[],'nonblocking_reconciliation':'GOV314 retains its Type-admission reference to R748. Historical, generated, installed and non-RMED mentions retain exact bytes; refer to CA-P-961 incoming-reference classification. Comprehensive reconciliation belongs to964.','boundary':'Root owns lifecycle. No Settings selection/default or source-owner migration, Journal, external Project authority, Tool/compiler/install/runtime, Projection rebuild, Git index/commit/push mutation.'}
lines=['# CA-P-963 Local Configuration Carrier authority repair','','Non-authoritative execution evidence for CA-P-963@2. Result: **PASS**. All 16 admitted Local dispositions are applied; Task lifecycle remains with the coordinating root.','','11 new Local Delivery owners, 14 revised Local semantic owners and two retired Carrier-only predecessors are recorded across 27 source operations. All 16 exact prior Archives were verified, including GOV761@12 and GOV762@9 from the sanctioned CA-P-962 handoff. The resulting frontier is 714 active sources: Core 655 unchanged and Local 59.','','| Predecessor | Disposition | Surviving owners |','| --- | --- | --- |']
for m in mappings:
    lines.append('| '+m['identity']+' | '+m['action']+' | '+', '.join(a['identity'] for a in m['after_owners'])+' |')
lines+=['','The Delivery successors were established and verified before each extraction or retirement. No additional active RMED reference repair was required for either retired Local identity; a fresh source and Project RMED scan confirms no active required mention remains. GOV314 continues to consume retained R748 Type admission.','','D328 keeps its dedicated Work Journal placement and Core D339 keeps Implementation Content Role placement, both byte-unchanged. D406 covers only the residual governed workflow/local-control NDJSON domain at its registered authoritative place. Production logging retains every approved behavioral qualification; D396 governs generic Carrier, preserving streamed/network logs and where-applicable fields.','','Type meanings, internal/external admission, allowed variation and all existing machine-readable contribution maps remain intact. GOV761@13 and GOV762@10 retain CA-D-393; GOV-EVAL006@17 remains byte-unchanged with CA-D-383/CA-D-387 links. Existing filename-derived and explicit legacy identities remain unchanged; new D396–406 use role-coded identities, exact admitted Subjects and omitted Standard tier.','','Independent Ruby Psych parsing, exact metadata/contribution preservation, complete admitted Claim comparison, literal/case checks, 16 Archive receipts and 16 ordering checks pass. The four reviewed rendering diffs affect only registered-operator bolding and actual sentence/cell-start capitalization. Git index SHA remains '+x.INDEX_SHA+'.','','No Settings selections/defaults, source ownership, pending Epic005 decisions, external Project authority, Journal, Tool/compiler/install/runtime, Projection rebuild, Git index, commit or push was changed. Downstream nonblocking reconciliation is recorded in CA-P-963-handoff.json.','','Reproduce verification with `python3 -B '+u.rel(HERE/'CA-P-963-verify.py')+'`. The verifier only writes CA-P-963 evidence through apply_patch.','']
outputs={'verification.json':verification,'mapping.json':{'task':'CA-P-963@2','dispositions':mappings},'handoff.json':handoff,'report.md':'\n'.join(lines)}
u.patch_files([(HERE/('CA-P-963-'+name),data if isinstance(data,str) else json.dumps(data,ensure_ascii=False,indent=2)+'\n') for name,data in outputs.items()])
print(json.dumps({'result':'PASS','counts':counts,'checks':checks},indent=2))
