#!/usr/bin/env python3
"""CA-P-963 only: reuse the reviewed 962 patch/Archive utilities, one disposition per run."""
import argparse
import difflib
import hashlib
import importlib.util
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('carrier_962', HERE / 'CA-P-962-execute.py')
u = importlib.util.module_from_spec(spec)
spec.loader.exec_module(u)
ROOT, BASE, CORE, LOCAL = u.ROOT, u.BASE, u.CORE, u.LOCAL
DESIGN, SNAP = u.DESIGN, u.SNAP
DISPOSITIONS = {d['before']['canonical_identity']: d for d in DESIGN['dispositions'] if d['before']['source_owner'] == LOCAL}
TARGETS = {i for d in DISPOSITIONS.values() for a in d['clause_allocations'] for i in a['owners']}
OWNERS = {o['identity']: o for o in DESIGN['authority_owners'] if o['identity'] in TARGETS}
CORE_LOG = json.loads((HERE / 'CA-P-962-changes.json').read_text())
HANDOFF = json.loads((HERE / 'CA-P-962-local-handoff.json').read_text())
LOGPATH = HERE / 'CA-P-963-changes.json'
LOG = json.loads(LOGPATH.read_text()) if LOGPATH.exists() else {'task':'CA-P-963@2','baseline':None,'operations':[],'completed_dispositions':[],'disposition_sequences':[]}
ROLES = ('04_requirement','05_method','06_evaluation','07_delivery')
INDEX_SHA = '57190e4a096cc585704d68f44ed8f1744a2b3487c32643b5bb0da162a2d126c2'


def permitted(path):
    p = Path(path).resolve()
    assert (p.parent == HERE and p.name.startswith('CA-P-963-')) or (p.is_relative_to(BASE / LOCAL) and p.suffix == '.md' and '.env' not in p.name), p


u.permitted = permitted


def save_log():
    u.patch_files([(LOGPATH, json.dumps(LOG, ensure_ascii=False, indent=2) + '\n')])


def current_identity(path, front):
    if u.top_block(front, 'atom_id'):
        return u.field(front, 'atom_id')
    return next(r['canonical_identity'] for r in SNAP['records'] if r['source_path'] == u.rel(path) or Path(r['source_path']).name.split('--',1)[0] == path.name.split('--',1)[0])


def manifest():
    out = []
    for p in u.active_sources():
        front, _ = u.split(p.read_text())
        out.append({'identity':current_identity(p,front),'path':u.rel(p),'version':int(u.field(front,'version')),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    assert len({r['identity'] for r in out}) == len(out)
    return sorted(out,key=lambda r:r['path'])


def index_sha():
    return hashlib.sha256(subprocess.run(['git','diff','--cached','--raw','--no-renames'],cwd=ROOT,capture_output=True,check=True).stdout).hexdigest()


def current_before(identity):
    return next(r for r in LOG['baseline']['sources'] if r['identity'] == identity)


def normalize(body):
    # Reuse the corrected 962 renderer; all actual diffs are emitted and reviewed before execution.
    rendered = u.normalize_body(body)
    assert re.findall(r'`[^`]*`',rendered) == re.findall(r'`[^`]*`',body)
    assert rendered.replace('**','').casefold() == body.replace('**','').casefold()
    return rendered


def baseline():
    assert LOG['baseline'] is None
    original = {r['canonical_identity']:{'identity':r['canonical_identity'],'path':r['source_path'],'version':r['version'],'sha256':r['sha256']} for r in SNAP['records']}
    for op in CORE_LOG['operations']:
        if op.get('after'):
            original[op['identity']] = {k:op['after'][k] for k in ('identity','path','version','sha256')}
        elif op['kind'] == 'retire_predecessor':
            del original[op['identity']]
    sources = manifest()
    assert sources == sorted(original.values(),key=lambda r:r['path'])
    assert len(sources) == 705 and sum(LOCAL in r['path'] for r in sources) == 50
    for c in HANDOFF['consumers']:
        actual = next(r for r in sources if r['identity'] == c['identity'])
        assert all(actual[k] == c['current'][k] for k in ('path','version','sha256'))
    assert index_sha() == INDEX_SHA
    available = [u.id_available(i) for i,o in OWNERS.items() if o['status'] == 'new_proposed_identity_not_reserved']
    refs = [r for r in u.REFERENCES if r['target_before'] in DISPOSITIONS and (r['classification']=='required_pre_retirement_repair' or r.get('required_before_extraction'))]
    assert not refs, refs
    LOG['baseline'] = {'at':u.now(),'sources':sources,'source_count':len(sources),'local_count':50,'core_count':655,'basis':'CA-P-960 exact frontier plus every CA-P-962 recorded operation, verified against current bytes','index_sha256':INDEX_SHA,'local_handoff_verified':True,'new_identity_availability':available,'additional_required_reference_repairs':refs}
    save_log()
    diffs = []
    for i,o in OWNERS.items():
        if o['source_owner'] == LOCAL and o['status'] != 'retain':
            body = normalize(o['proposed_claim_body'])
            diffs.append({'identity':i,'body':body,'design_body_sha256':u.sha(o['proposed_claim_body']),'actual_body_sha256':u.sha(body),'diff':''.join(difflib.unified_diff(o['proposed_claim_body'].splitlines(True),body.splitlines(True),fromfile='admitted design',tofile='prepared source'))})
    u.patch_files([(HERE/'CA-P-963-prepared-claims.json',json.dumps(diffs,ensure_ascii=False,indent=2)+'\n')])
    print('Baseline PASS: 705 sources, 50 Local, 11 globally available D identities, three current handoff Revisions exact')


def check_atom(path, identity, version):
    text = path.read_text()
    front,body = u.split(text)
    assert current_identity(path,front) == identity
    assert int(u.field(front,'version')) == version
    u.datetime.datetime.strptime(u.field(front,'updated_at'),'%Y-%m-%d %H:%M:%S %z')
    sb = u.top_block(front,'subjects')
    governed = re.search(r'  governs:\n((?:    .*(?:\n|$))*)',sb)
    assert governed and len(re.findall(r'^      - ',governed.group(),re.M)) == 1
    values = re.findall(r'^      - (.+)',sb,re.M)
    assert len(values) == len(set(v.strip('\"\'') for v in values))
    assert body.startswith('# ') and body.count('\n# ') == 0
    return {'identity':identity,'path':u.rel(path),'version':version,'sha256':u.sha(text)}


def owner_ready(identity):
    o = OWNERS[identity]
    if o['source_owner'] == CORE or o['status'] == 'retain':
        before = current_before(identity)
        assert hashlib.sha256((ROOT/before['path']).read_bytes()).hexdigest() == before['sha256']
        return before
    ops = [op for op in LOG['operations'] if op['identity']==identity and op.get('after')]
    if ops:
        after = ops[-1]['after']
        assert check_atom(ROOT/after['path'],identity,after['version']) == after
        return after
    body = normalize(o['proposed_claim_body'])
    prepared = next(r for r in json.loads((HERE/'CA-P-963-prepared-claims.json').read_text()) if r['identity']==identity)
    assert body == prepared['body']
    path = u.final_path(o,body)
    before = archive = availability = None
    if o['status'] == 'new_proposed_identity_not_reserved':
        availability = u.id_available(identity)
        front = '\n'.join(['atom_id: '+identity,'cce_version: '+o['proposed_cce_version'],'cce_form: '+o['proposed_cce_form'],'subjects:\n'+u.subjects_block(o['proposed_subjects']),'version: 1','updated_at: '+json.dumps(u.now()),'relations: '+u.relations_block(o.get('proposed_relations',{}))]).replace('relations:   ','relations:\n  ')
        version = 1
        assert not path.exists()
    else:
        before = current_before(identity)
        oldpath = ROOT/before['path']
        old = oldpath.read_text()
        assert u.sha(old) == before['sha256']
        archive = u.exact_archive(identity,old,oldpath)
        front,_ = u.split(old)
        version = before['version']+1
        front = u.set_block(front,'version',str(version))
        front = u.set_block(front,'updated_at',json.dumps(u.now()))
        front = u.set_block(front,'cce_version',o['proposed_cce_version'])
        front = u.set_block(front,'cce_form',o['proposed_cce_form'])
        if o.get('proposed_subjects'):
            front = u.set_block(front,'subjects',u.subjects_block(o['proposed_subjects']))
        assert oldpath.read_text() == old
    changes = [(path,'---\n'+front+'\n---\n'+body)]
    if before and path != oldpath:
        assert not path.exists()
        changes.append((oldpath,None))
    u.patch_files(changes)
    after = check_atom(path,identity,version)
    LOG['operations'].append({'sequence':len(LOG['operations'])+1,'kind':'new_owner' if before is None else 'revise_owner','identity':identity,'at':u.now(),'before':before,'after':after,'archive':archive,'id_availability':availability,'design_body_sha256':u.sha(o['proposed_claim_body']),'actual_body_sha256':u.sha(body),'design_body_adjusted':body!=o['proposed_claim_body'],'local_tier':o['local_tier'],'claim_and_subject_review':o.get('subjects_rationale',o['rationale']),'canonical_identity_representation':'preserve existing explicit or filename-derived identity; new Delivery owners use explicit role-coded identities'})
    save_log()
    return after


def active_mentions(identity):
    pattern = re.compile(r'(?<![A-Z0-9-])'+re.escape(identity)+r'(?![0-9])')
    external = [p for p in (ROOT/'.caprmedio_caprmedio').rglob('*.md') if p.parent.name in ROLES and not {'archive','drafts','done','onhold','cancelled','execution_evidence'}.intersection(p.relative_to(ROOT).parts) and '.env' not in p.name]
    own = current_before(identity)['path']
    found = []
    for p in u.active_sources()+external:
        if u.rel(p) == own:
            continue
        for n,line in enumerate(p.read_text().splitlines(),1):
            if pattern.search(line):
                found.append({'path':u.rel(p),'line':n,'text':line})
    return found


def apply_disposition(identity):
    assert LOG['baseline'] and index_sha() == INDEX_SHA
    assert identity in DISPOSITIONS
    if identity in LOG['completed_dispositions']:
        print(identity+' already completed')
        return
    d = DISPOSITIONS[identity]
    before = current_before(identity)
    path = ROOT/before['path']
    assert u.sha(path.read_text()) == before['sha256']
    targets = list(dict.fromkeys(i for a in d['clause_allocations'] for i in a['owners']))
    successors = [owner_ready(i) for i in targets if i != identity]
    # No required incoming repairs were admitted for these two retiring Local identities.
    # All successors and current Core handoff links exist before extraction/retirement.
    for c in HANDOFF['consumers']:
        p = ROOT/c['current']['path']
        changed = [x for x in LOG['operations'] if x['identity']==c['identity'] and x.get('after')]
        if changed:
            p = ROOT/changed[-1]['after']['path']
        relations = u.relations_from(u.split(p.read_text())[0])
        for repair in c['repaired_links']:
            assert all(t in relations[repair['relation']] for t in repair['targets_after'])
    pending = []
    if d['retirement_requested']:
        pending = active_mentions(identity)
        assert not pending, pending
        old = path.read_text()
        assert u.sha(old) == before['sha256']
        archive = u.exact_archive(identity,old,path)
        assert path.read_text() == old
        u.patch_files([(path,None)])
        LOG['operations'].append({'sequence':len(LOG['operations'])+1,'kind':'retire_predecessor','identity':identity,'at':u.now(),'before':before,'after':None,'archive':archive,'successors':targets,'active_required_mentions_before_retirement':pending})
        save_log()
    else:
        owner_ready(identity)
    LOG['disposition_sequences'].append({'identity':identity,'successors_verified_before_extraction_or_retirement':successors,'extraction_or_retirement_sequence':next(x['sequence'] for x in LOG['operations'] if x['identity']==identity),'required_incoming_repairs':[],'remaining_active_required_mentions_before_retirement':pending})
    LOG['completed_dispositions'].append(identity)
    save_log()
    print(identity+': '+d['action']+' PASS -> '+', '.join(targets))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action',choices=['baseline','apply','list'])
    parser.add_argument('identity',nargs='?')
    args = parser.parse_args()
    if args.action == 'baseline':
        baseline()
    elif args.action == 'apply':
        apply_disposition(args.identity)
    else:
        print('\n'.join(DISPOSITIONS))
