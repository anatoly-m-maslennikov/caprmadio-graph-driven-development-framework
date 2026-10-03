#!/usr/bin/env python3
"""Design evidence only. Source reads; evidence writes only via apply_patch."""
import hashlib
import json
import re
import subprocess
import difflib
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / '.caprmedio_framework').is_dir())
INV = json.loads((HERE / 'CA-P-960-inventory.json').read_text())
RECORDS = {r['canonical_identity']: r for r in INV['records']}
DESIGNS = {}
OWNERS = {}

def before(identity):
    r = RECORDS[identity]
    return {k:r[k] for k in ('canonical_identity','version','source_path','sha256','source_owner','current_content_role','local_tier_filename_marker')}

def save(suffix, value):
    path = HERE / ('CA-P-961-' + suffix)
    content = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2) + '\n'
    rel = path.relative_to(ROOT).as_posix()
    if path.exists():
        if path.read_text()==content: return
        patch = '*** Begin Patch\n*** Update File: '+rel+'\n@@\n'+''.join('-'+x+'\n' for x in path.read_text().splitlines())+''.join('+'+x+'\n' for x in content.splitlines())+'*** End Patch\n'
    else:
        patch = '*** Begin Patch\n*** Add File: '+rel+'\n'+''.join('+'+x+'\n' for x in content.splitlines())+'*** End Patch\n'
    subprocess.run(['apply_patch'], input=patch, text=True, cwd=ROOT, check=True, capture_output=True)

def owner(identity, claim=None, source_owner=None, governs=None, dependencies=(), rationale='', role='Delivery', tier='Standard'):
    existing = RECORDS.get(identity)
    if existing:
        record = {'identity':identity,'before':before(identity),'status':'revise' if claim and claim != existing['complete_claim_body'] else 'retain','proposed_claim_body':claim or existing['complete_claim_body'],'source_owner':existing['source_owner'],'content_role':existing['current_content_role'],'local_tier':existing['local_tier_filename_marker'],'subjects_action':'retain exact existing Subjects unless the explicit proposed_subjects field supplies the narrower Carrier subject','rationale':rationale}
    else:
        assert claim and source_owner and governs
        slug = re.sub(r'[^a-z0-9]+','-',claim.splitlines()[0].lstrip('# ').lower()).strip('-')
        folder = '07_delivery' if role == 'Delivery' else '05_method'
        name = source_owner.split('_',1)[1]
        record = {'identity':identity,'status':'new_proposed_identity_not_reserved','proposed_version':1,'proposed_claim_body':claim,'source_owner':source_owner,'content_role':role,'local_tier':tier,'proposed_path':f'.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/{source_owner}/{folder}/{identity}-{name}-{role.upper()}--{slug}.md','proposed_subjects':{'governs':{'occurrent' if role == 'Method' else 'continuant':[governs]},'depends_on':{'continuant':list(dependencies)}} if dependencies else {'governs':{'occurrent' if role == 'Method' else 'continuant':[governs]}},'proposed_relations':{},'rationale':rationale}
    OWNERS[identity] = record
    return identity

def add(identity, action, allocations, proposed=None, reason='', confidence=99, status='admitted'):
    r = RECORDS[identity]
    for a in allocations:
        assert a['before_quote'] in r['complete_claim_body'], (identity,a['before_quote'])
        for target in a['owners']:
            if target in RECORDS and target not in OWNERS: owner(target, rationale='Existing authority reused for the explicitly allocated contribution; its full exact Claim is preserved in this owner record.')
    if proposed is not None:
        owner(identity, proposed, rationale=reason)
    DESIGNS[identity] = {'before':before(identity),'action':action,'admission':status,'confidence_percent':confidence,'rationale':reason,'clause_allocations':allocations,'retirement_requested':action in ('replace','dedupe'),'role_decision':('retain '+r['current_content_role'] if action not in ('replace','dedupe') else 'old identity must retire only after reference repair; surviving owners have independently specified roles'),'tier_and_scope_decision':'Preserve source owner and observed Core / General / omitted Standard tier. Claim domains and Subjects follow each exact proposed owner; no selected Settings or source-owner migration.','archive':{'required':action!='retain','path':str(Path(r['source_path']).parent / 'archive' / (Path(r['source_path']).stem+'@'+str(r['version'])+'.md')),'sha256':r['sha256'],'byte_rule':'Preserve the exact complete prior source bytes; existing identical archive is reusable, differing bytes block mutation.'},'verification_conditions':['All original clauses allocated to the exact surviving Claims below.','Refresh every source hash and proposed ID availability before implementation.','Apply and verify every required active RMED incoming-reference repair before old identity retirement.','Out-of-scope required repairs require separate Operator authorization and completion; source remains active until then.','No generated or historical mention alone blocks retirement; retain exact historical content.']}

def alloc(quote, owners, rationale):
    return {'before_quote':quote,'owners':owners,'rationale':rationale}

def whole(identity, target, reason):
    add(identity,'replace',[alloc(RECORDS[identity]['complete_claim_body'],[target],reason)],reason=reason)

def edits(identity, changes, reason):
    body = RECORDS[identity]['complete_claim_body']
    proposed = body
    allocations=[]
    for old,new,targets,why in changes:
        assert proposed.count(old)==1,(identity,old,proposed.count(old))
        proposed = proposed.replace(old,new,1)
        allocations.append(alloc(old,targets,why))
    allocations.append(alloc(body,[identity],'All original text outside the explicitly replaced spans survives byte-for-byte in the proposed retained Claim; the spans above exhaust the differences.'))
    add(identity,'split',allocations,proposed,reason)

CORE='001_CORE_META_MODEL'
LOCAL='003_LOCAL_CONFIGURATION'

owner('CA-D-378', '# Serialize Assigned Atom Identities\n\n**every** assigned Atom ID **must** begin with the registered uppercase Project identity prefix. the Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`, with Content Role Identity Letters (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Ops: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom **and** **must not** identify an Epic.\n', CORE, 'Atom/Identifier/Carrier Encoding', ('Atom/Identifier','Atom/Content Role','Project'), 'One identifier encoding contract consolidates grammar, prefix, role alphabet and Plan reservation without duplicating semantic immutable identity or Settings selection.')
for i in ['CA-R-1305','CA-R-737','CAPRMEDIO-GOV-REQU-764']: whole(i,'CA-D-378','The whole concrete identifier encoding contribution moves to one shared D owner; the old role-encoded identity cannot remain the D identity.')
owner('CA-D-379','# Serialize Epic Identifiers\n\nan Epic Identifier **must** match `<PROJECT_PREFIX>-Epic-<number>-<scope>-<summary>`.\n',CORE,'Epic/Identifier/Carrier Encoding',('Epic/Identifier',),'Epic identity grammar is distinct from D293 Directory Carrier grammar, which includes a mutable Work Sequence prefix.')
whole('CA-R-1304','CA-D-379','Reuse D293 for directory names, but retain this distinct complete Epic Identifier grammar in D379.')
owner('CA-D-353',RECORDS['CA-D-353']['complete_claim_body'].rstrip()+' **every** Epic **must** have **`=1`** Directory Carrier.\n',rationale='Consolidate Structural Entity Carrier cardinality with its stricter Epic qualification: >=1 remains for other Structural Entities and =1 remains for Epic.')
whole('CA-R-1369','CA-D-353','D353 is revised to retain the exact stricter Epic cardinality; D263 describes the inverse per-directory cardinality and is not a replacement.')
edits('CA-R-728',[('the immutable `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>` identity','the immutable identity',['CA-R-728','CA-D-378'],'Immutable identity remains R; the exact textual grammar is D378.')],'Retain the accepted Project-owned Atom identity definition; move only its concrete grammar.')
owner('CA-R-1415','# Give Every Atom Revision One Version\n\n**every** Atom Revision **must** have **`=1`** positive integer Version that increases monotonically across successive Revisions of the same Atom.\n',rationale='R165 positivity and monotonicity are consolidated into the existing Version owner; no new competing Version Requirement.')
owner('CA-R-1416','# Give Every Atom Revision One Updated At\n\n**every** Atom Revision **must** have **`=1`** unambiguous Updated At date-time.\n',rationale='R165 unambiguous date-time qualification is added to the existing Updated At owner.')
add('CA-R-165','dedupe',[alloc('**`=1`** positive monotonic `version`',['CA-R-1415','CA-D-270'],'R1415 retains cardinality, positive integer and monotonically increasing Version; D270 exclusively serializes version.'),alloc('**`=1`** unambiguous `updated_at`',['CA-R-1416','CA-D-270'],'R1416 retains cardinality and unambiguous date-time; D270 exclusively serializes updated_at.')],reason='Retire only after semantic qualifiers are present in existing R owners and all required incoming references are semantically mapped.')
edits('CA-R-1372',[('derived `updated_at`','derived Updated At',['CA-R-1372'],'The direct Operator statement identifies Journal Updated At as a derived date-time property. This spelling normalization imposes neither persistence nor non-materialization.')],'Resolved at 99 from direct Operator statement: Artifact/Revision has journals: updated_at (date + time) but derived. Preserve exactly-one derivation from latest accepted entry; no independently asserted Carrier serialization field exists here.')
owner('CA-M-275','# Format Scope Unit Names\n\n**to** write a Scope Unit Name, join nonempty uppercase letter-or-digit word tokens with single underscores.\n',CORE,'Scope Unit Name Authoring',('Scope Unit/Name',),'Global reusable naming procedure; no Carrier scope is invented. D302 and D284 continue to own filename encoding.',role='Method')
OWNERS['CA-M-275']['proposed_relations']={'method_for':['CA-R-962']}
whole('CA-R-963','CA-M-275','Resolved at 99 using R1340, M229, M235 and the Task formatting instruction: the global name-writing rule is M; concrete filename references remain D302/D284. All nonempty/uppercase/letter-or-digit/single-underscore constraints survive.')
owner('CA-D-380','# Serialize Navigational Order Numbers\n\n**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default Navigational Order Number of **every** non-Project Scope Unit **must** be rendered with **`>=2`** digits.\n',CORE,'Navigational Order Number/Carrier Encoding',('Navigational Order Number','Scope Unit'), 'Concrete decimal rendering and minimum width are distinct from Operator ownership and chronological default; D297/D299 own composition, D300 allocation.')
edits('CA-R-978',[('Operator-controlled decimal navigation label','Operator-controlled navigation label',['CA-R-978','CA-D-380'],'Operator control and Scope Unit label meaning remain R; base-ten rendering goes to D380.')],'Resolved at 99: decimal is the rendering choice for an Operator-controlled navigation label, corroborated by D297/D299/D300 Carrier composition.')
edits('CA-R-981',[(' **and** rendered with **`>=2`** digits','',['CA-D-380'],'The exact minimum two-digit default rendering moves; one-based chronology and same-parent domain remain R.')],'Keep chronological default as a Requirement; place width in existing navigation representation domain.')
owner('CA-D-381','# Serialize Work Sequence Numbers\n\n**every** Carrier rendering of a Work Sequence Number **must** use decimal digits.\n',CORE,'Work Sequence Number/Carrier Encoding',('Work Sequence Number',),'D293/D294 use the same navigation Property; decimal rendering is independent of positive ordinal and local uniqueness semantics.')
edits('CA-R-997',[('unique positive decimal ordinal','unique positive ordinal',['CA-R-997','CA-D-381'],'Local uniqueness and positive ordinal remain R; base-ten rendering moves to D381.')],'Resolved at 99 with R991/R992 and D293/D294: decimal is a concrete label encoding; positive local ordinal semantics remain unchanged.')

owner('CA-D-382','# Place Local Environment Injection Carriers\n\nFor local development, secret values **may** be injected from a repository-local `.env` File Carrier outside **every** applicable Project authority Carrier root. **every** real `.env` variant **must** be ignored by Git **and** excluded from CAPRMEDIO discovery. a tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**. mutable runtime configuration identifiers **must** receive their runtime values through the local environment Carrier.\n',CORE,'Local Environment Injection/File Carrier',('Project','Runtime Configuration'), 'One local development Carrier contract; no secret files are read and no runtime value is selected.')
env_old='For local development, secret values **may** be injected from a repository-local `.env` file outside every applicable Project authority Carrier root. **every** real `.env` variant is ignored by Git **and** is excluded from CAPRMEDIO discovery. A tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**. '
edits('CAPRMEDIO-GOV-REQU-290',[(env_old,'',['CA-D-382'],'All local environment placement, Git/discovery exclusion and dummy-example content clauses survive in D382.'),('**when** an identifier is mutable runtime configuration, its runtime value is supplied through the local environment carrier as well; ','',['CA-D-382'],'Runtime identifier injection remains explicitly owned by D382.')],'Retain the complete security prohibition, secret universe, covered surfaces, redaction, production injection behavior, identifier minimization and incident remediation. Only concrete local environment Carrier clauses move.')
owner('CA-D-383','# Serialize Interaction Reporting Mode\n\nthe Framework Instance Settings TOML Carrier **must** serialize its interaction reporting setting as `reporting_mode` **in** the `[interaction]` section, using the allowed value **and** default governed by CAPRMEDIO-GOV-REQU-294.\n',CORE,'Framework Instance Settings/Carrier/Interaction Reporting',('Framework Instance Settings','Interaction Reporting Mode'),'Reuse R294 for semantic modes and default; D383 exclusively owns the TOML field path.')
block='the Framework Instance Settings Artifact provides one framework-instance interaction reporting setting:\n\n```toml\n[interaction]\nreporting_mode = "silent" # silent | verbose\n```'
edits('CAPRMEDIO-GOV-REQU-294',[(block,'the Framework Instance Settings Artifact provides one framework-instance interaction reporting setting.', ['CAPRMEDIO-GOV-REQU-294','CA-D-383'],'Single setting ownership remains R; exact TOML [interaction].reporting_mode syntax moves to D383. Allowed values and silent default remain in R.')],'Retain silent/verbose behavior, mandatory exceptions, presentation-only boundary and single settings owner.')
owner('CA-D-384','# Serialize Git Commit Type Tokens\n\na Git Commit Type **must** use Carrier token `git_commit`; an External Git Commit Type **must** use Carrier token `external_git_commit`.\n',CORE,'Git Commit/Type/Carrier Token',('Type',),'Token map only; native SHA identity and internal/external governance routes remain R296.')
edits('CAPRMEDIO-GOV-REQU-296',[('artifact type `git_commit`','Type Git Commit',['CAPRMEDIO-GOV-REQU-296','CA-D-384'],'Type admission and internal route remain R; exact token moves to D384.'),('artifact type `external_git_commit`','Type External Git Commit',['CAPRMEDIO-GOV-REQU-296','CA-D-384'],'Type admission and external route remain R; exact token moves to D384.')],'Retain native repository-qualified SHA identity, provenance facts, and type-derived governance locus.')
owner('CA-D-385',RECORDS['CAPRMEDIO-GOV-REQU-297']['complete_claim_body'],CORE,'Architecture View/Projection Carrier',('Scope Unit','Projection'), 'Optional Projection content and linked active sources form one coherent Carrier content contract; disabled surfaces still need no placeholders.')
whole('CAPRMEDIO-GOV-REQU-297','CA-D-385','The complete optional architecture-view content and navigation-authority exclusion moves together; no unnecessary R split.')
owner('CA-D-386','# Serialize Concern Priority\n\na Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** Epic, Task, Action Policy, **and** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.\n',CORE,'Concern/Priority/Carrier Encoding',('Priority','Atom/Content Role: Concern'), 'Field/value serialization and omission contract only; comparison increments, virtual result, operator selection and precedence exceptions remain R299.')
edits('CAPRMEDIO-GOV-REQU-299',[('a Concern Atom stores **`=1`** `priority` value: `high`, `medium`, **or** `low`. **every** Epic, Task, Action Policy, **and** non-Concern Content Role Atom **must** omit `priority`. `highest` is a virtual comparison result **and** is never stored.','a Concern Atom has **`=1`** Priority value: High, Medium, **or** Low. Highest is a virtual comparison result.',['CAPRMEDIO-GOV-REQU-299','CA-D-386'],'Semantic Priority cardinality/value vocabulary and virtual highest remain R; carrier field spelling, omission and non-storage go to D386.')],'The effective comparison algorithm, selection modes/default, ambiguity/unsatisfiable-obligation stops and unrelated precedence remain exact.')
owner('CA-D-387','# Serialize Atomic Admission Strictness\n\nthe Framework Instance Settings TOML Carrier **must** encode atomic admission strictness as `creation_strictness` **in** `[artifacts]`, using the allowed values **and** default governed by CAPRMEDIO-GOV-REQU-302.\n',CORE,'Framework Instance Settings/Carrier/Atomic Admission Strictness',('Framework Instance Settings',),'Concrete TOML key only; admission criteria and promotion approval remain R302.')
edits('CAPRMEDIO-GOV-REQU-302',[(' through `artifacts.creation_strictness`','',['CA-D-387'],'The concrete TOML path moves; medium/high/default and settings ownership remain in R.')],'Preserve medium/high checks, focused-question stop, unchanged broader-scope promotion, explicit Operator acceptance and later revision/replacement gates.')
owner('CA-D-388','# Serialize Generated Data Stage Prefixes and Formats\n\nJournal input **and** generated Projection Carriers **must** use these ordered stage prefixes: canonical Journal input `src`, deterministic lossless staging Projection `stg`, consumer-ready semantic Projection `mrt`, **and** aggregated metrics Projection `biz`. `src` **must** use canonical NDJSON Journal input; `stg` **must** use TOON. these prefixes classify Journal inputs **and** generated Projections **only**. unregistered stage prefixes remain available for later governed Extension.\n',CORE,'Generated Data Stage/Carrier Encoding',('Journal','Projection'),'One shared prefix/format contract; stage dependency direction and stage semantics remain R337.')
stage_body='# Register generated-data stages\n\nthe following ordered generated-data pipeline stages **must** be registered, referenced by their Carrier prefixes governed by CA-D-388:\n\n| Stage reference | Stage meaning |\n| --- | --- |\n| `src` | Canonical Journal input; authority comes from the Journal, **not** the prefix. |\n| `stg` | Deterministic, lossless Projection of a bounded `src` frontier. |\n| `mrt` | Consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |\n| `biz` | Aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |\n\nDependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.\n'
add('CAPRMEDIO-GOV-REQU-337','split',[alloc('the following ordered vocabulary **must** be registered for generated-data pipeline stages:',['CAPRMEDIO-GOV-REQU-337','CA-D-388'],'R registers the semantic stage vocabulary; D owns its representation prefixes.'),alloc('| `src` | Canonical NDJSON Journal input; authority comes from the Journal, **not** the prefix. |',['CAPRMEDIO-GOV-REQU-337','CA-D-388'],'Journal input/authority meaning stays R; src token and NDJSON format go to D.'),alloc('| `stg` | Deterministic, lossless TOON projection of a bounded `src` frontier. |',['CAPRMEDIO-GOV-REQU-337','CA-D-388'],'Bounded deterministic lossless transformation stays R; stg token and TOON go to D.'),alloc('| `mrt` | Consumer-ready semantic Projection, including Requirement groupings by scope **and** tier **or** Mermaid relation maps. |',['CAPRMEDIO-GOV-REQU-337','CA-D-388'],'Semantic consumer purpose/examples remain R; mrt prefix goes to D.'),alloc('| `biz` | Aggregated CAPRMEDIO artifact **and** implementation metrics, including point-in-time snapshots **and** historical trends. |',['CAPRMEDIO-GOV-REQU-337','CA-D-388'],'Metrics meaning and time views remain R; biz prefix goes to D.'),alloc('Dependencies **must** move forward through `src → stg → mrt → biz`; a stage **may** depend on **any** earlier registered stage but **must not** depend on a later stage.',['CAPRMEDIO-GOV-REQU-337'],'Exact forward dependency constraints remain R; prefixes are cross-references to D388.'),alloc('These prefixes classify Journal inputs **and** generated Projections **only**. Unregistered stage prefixes remain available for later governed extension.',['CA-D-388'],'Exact Carrier domain restriction and open extension preserve in D388.')],stage_body,'Retain stage semantics and dependency topology; isolate only prefix and physical format authority.')
owner('CA-D-329',RECORDS['CA-D-329']['complete_claim_body'].rstrip()+' prose **must** be reserved for additional invalidation conditions that cannot be encoded **without** loss.\n',rationale='Existing exact proof_frontier_refs encoding receives the original lossless prose fallback qualification; no duplicate D frontier owner.')
edits('CAPRMEDIO-GOV-REQU-353',[('GOV REQU 010 defines the required `proof_frontier_refs` representation; prose is reserved for additional invalidation conditions that cannot be encoded **without** loss.','the Carrier representation follows CA-D-329.',['CA-D-329'],'Resolve noncanonical GOV REQU 010 against exact existing D329; frontier key and lossless prose fallback go to D329.')],'Retain complete governed proof binding domain: revisions, configurations, evaluators, environments and material inputs.')
owner('CA-D-389','# Serialize Analysis Type Tokens\n\nRationale **must** use Carrier token `rationale`; External Analysis Report **must** use Carrier token `external_analysis_report`.\n',CORE,'Atom/Content Role: Analysis/Type/Carrier Token',('Atom/Content Role: Analysis/Type',),'One CORE_META_MODEL Analysis Type token map; Rationale explanatory meaning and external review envelope behavior retain their R owners.')
edits('CAPRMEDIO-GOV-REQU-355',[('an `external_analysis_report` Atom','an External Analysis Report Atom',['CAPRMEDIO-GOV-REQU-355','CA-D-389'],'The required external Analysis Type remains R; concrete token moves to D389.')],'Keep provider-neutral review envelope, one internal interpretation, exclusive derivation source and owning-role materialization obligations.')
for i,did,subject,reason in [('CAPRMEDIO-GOV-REQU-362','CA-D-390','Artifact/Updated At/Carrier Encoding','The whole optional timezone setting and emitted timestamp representation is one D contract; reuse D270/D310 for the Atom/Projection field bindings and preserve this format, allowed timezone interpretations and local default.'),('CAPRMEDIO-GOV-REQU-373','CA-D-391','Project Scope Unit Graph/Projection Carrier/Authority Mode','Effective mode exposure belongs to the consuming Projection, distinct from D374 selecting Settings field encoding.'),('CAPRMEDIO-GOV-REQU-383','CA-D-392','Project Scope Unit Graph/Projection Carrier/Project Identity','Projection field exposure preserves Settings ownership and canonical/prior-name distinction; D375 is the originating Settings field, not an equivalent Projection owner.'),('CAPRMEDIO-GOV-REQU-760','CA-D-393','External Type/Carrier Token Derivation','Derivation chooses the concrete external_ serialization prefix; registered default and separately explicit non-default exceptions qualify this same token contract.')]:
    owner(did,RECORDS[i]['complete_claim_body'],CORE,subject,(),reason)
    whole(i,did,reason)
edits('CAPRMEDIO-GOV-REQU-750',[(' with Carrier token `rationale`','',['CA-D-389'],'Type admission and non-normative explanatory conclusion remain R; token moves to D389.')],'Keep internal Rationale Type admission and explanatory-only authority boundary.')
owner('CA-D-394','# Bind Convenience Symlink Carriers to One Native Source\n\na convenience symlink Carrier **must** expose the one native reusable framework source governed by project-local authority **without** creating copied authority, an additional governance owner, **or** a live authority cycle.\n',CORE,'Convenience Symlink Carrier',('Native Reusable Framework Source','Project Authority'),'The concrete symlink representation is subordinate to the R086 source-ownership and recursion boundary; no new path or symlink is selected.')
edits('CAPRMEDIO-META-REQU-086',[('convenience symlinks expose that one native source','convenience locators expose that one native source',['CAPRMEDIO-META-REQU-086','CA-D-394'],'R retains one-source recursion termination; D394 retains the concrete symlink form and no-copied-authority qualifications.')],'Preserve self-hosting governance and distinct native/project/locator owners; concrete locator representation moves.')
owner('CA-D-395','# Serialize Ambient Project Scope Paths\n\na Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.\n',CORE,'Scope Path/Carrier Encoding',('Scope Path','Project'),'Exact field spelling, omitted ambient Project and empty Project path; no list/string schema is invented.')
edits('CAPRMEDIO-META-REQU-098',[('The current project is ambient **and** never repeated **in** `scope_path`. Project scope therefore uses an empty path.','The current project is ambient.',['CAPRMEDIO-META-REQU-098','CA-D-395'],'Ambient Project semantics remain R; field omission and empty-path serialization are D395.')],'Retain ordered project-relative address and identity/form/role/governance invariance under Scope.')
add('CAPRMEDIO-META-REQU-119','retain',[alloc(RECORDS['CAPRMEDIO-META-REQU-119']['complete_claim_body'],['CAPRMEDIO-META-REQU-119','CA-D-268'],'The primary Claim explicitly unifies pre-existence, directed explanatory ownership and no subject mutation. Embedded Rationale/backlink exclusion enforces that coherent authority boundary, not an independently chosen format. D268 already represents the owned direct relation once on its owner.')],reason='Resolved at 99 from the complete primary Claim and DRY: retain the coherent General R contribution. No new D duplicates relation ownership; no tier change.')
owner('CA-D-283',RECORDS['CA-D-283']['complete_claim_body'].rstrip()+' **every** same-identity Atom Revision, including a governed Summary **or** Scope change, **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename.\n',rationale='The existing Project-owned filename owner receives exact same-ID preservation for Summary and Scope changes; D281/D282 already synchronize H1 and filename from the same Summary.')
edits('CAPRMEDIO-META-REQU-122',[('while preserving the exact assigned Atom-ID segment **in** its Carrier filename','while preserving its assigned Atom identity',['CAPRMEDIO-META-REQU-122','CA-D-283'],'Stable identity remains R; exact filename segment preservation goes to D283.'),('updates the Carrier filename **and** H1 **without** creating a successor Atom','does **not** create a successor Atom',['CAPRMEDIO-META-REQU-122','CA-D-281','CA-D-282'],'No successor for same-primary-meaning Summary change stays R; existing D281/D282 require both H1 and slug to render the current Summary.')],'Retain mutable Summary versus immutable identity, draft/accepted distinction, governed Revision, immutable recoverable history and primary-meaning successor boundary.')
edits('CAPRMEDIO-META-REQU-166',[('one unambiguous `updated_at`','one unambiguous Updated At date-time',['CAPRMEDIO-META-REQU-166','CA-D-310'],'The semantic date-time cardinality/unambiguity/latest-completed-rebuild contribution stays R; D310 is the existing updated_at field owner and retains its no-timestamp-only-currentness guard.')],'Preserve latest completed rebuild, governed generator/procedure, declared configuration, job-specific provenance and no-blanket-source-frontier requirement.')
edits('CAPRMEDIO-META-REQU-174',[('typed frontmatter relations','typed relations',['CAPRMEDIO-META-REQU-174','CA-D-268'],'Typed application endpoints and ownership remain R; existing D268 owns frontmatter serialization.')],'Retain internal/external package ownership, separate binding Atom, Extension and Scope targets and Settings-exclusive activation/revision selection.')
edits('CAPRMEDIO-META-REQU-730',[('preserve the exact Atom-ID segment **in** its Carrier filename','preserve its Atom identity',['CAPRMEDIO-META-REQU-730','CA-D-283'],'R retains identity under governed Scope change; D283 owns exact filename Atom-ID segment preservation.')],'Retain new Revision and lineage-impact review for changed Applicability; reuse shared filename owner.')
edits('CAPRMEDIO-GOV-REQU-381',[('typed frontmatter relation','typed relation',['CAPRMEDIO-GOV-REQU-381','CA-D-268'],'feature_realization remains the exact registered semantic relation with Feature/native-target endpoints; D268 owns frontmatter encoding.')],'Keep non-Scope native Realization targets and relation meaning in R; reuse direct relation D owner.')

record_policy=RECORDS['CAPRMEDIO-GOV-REQU-315']['complete_claim_body'].split('## Structured record policy\n\n',1)[1].split('\n\nLogs record',1)[0]
owner('CA-D-396','# Serialize Structured Production Log Records\n\n'+record_policy+'\n',LOCAL,'File Carrier',('Logging Policy',),'Move the exact conditional record-field universe, including UTC timestamp, without broadening where-applicable or altering logging behavior.')
owner('CA-D-406','# Serialize Governed Workflow Journal Carriers\n\nGoverned CAPRMEDIO workflow **and** local project-control Journal Carriers **must** use append-only NDJSON **in** their applicable registered authoritative places. the CAPRMEDIO Project Work Journal placement follows CA-D-328; Implementation Journal placement follows CA-D-339.\n',LOCAL,'Journal',('Work Journal','Implementation Journal'),'PENDING 98: retain full original NDJSON domain, but reconcile older blanket .caprmedio role-folder location with current differentiated placements. Operator disposition required for this literal location change.')
OWNERS['CA-D-406']['admission']='pending_operator'
old_journal='Governed CAPRMEDIO workflow **and** local project-control Journals use append-only NDJSON carriers **in** their applicable `.caprmedio` role folders; they are **not** a substitute for the production system\'s log platform.'
edits('CAPRMEDIO-GOV-REQU-315',[(record_policy,'the Carrier content of structured production log records follows CA-D-396.',['CA-D-396'],'Exact where-applicable field universe moves to D396; UTC remains limited to production logs.'),(old_journal,'Governed CAPRMEDIO workflow **and** local project-control Journals are **not** a substitute for the production system\'s log platform.',['CAPRMEDIO-GOV-REQU-315','CA-D-406','CA-D-328','CA-D-339'],'Production-platform distinction remains R; append-only NDJSON domain moves to proposed D406. Location reconciliation is explicitly pending Operator decision; no silent scope equivalence between Journal Types.')],'Retain policy coverage, severity meanings, actionable failures, bounded DEBUG, meaningful transitions, deduplicated exception reporting, sensitive-data minimization, retention/sink failure behavior, monitors and no-prose-only acceptance. Separate exact record shape from behavior; location conflict remains unadmitted.')
DESIGNS['CAPRMEDIO-GOV-REQU-315']['admission']='pending_operator'
DESIGNS['CAPRMEDIO-GOV-REQU-315']['confidence_percent']=98
DESIGNS['CAPRMEDIO-GOV-REQU-315']['operator_question']='May GOV-315 retain append-only NDJSON for all governed workflow and local-control Journals while replacing its blanket .caprmedio role-folder placement with the applicable registered Journal placements, including D328 for Work Journal and D339 for Implementation Journal?'
DESIGNS['CAPRMEDIO-GOV-REQU-315']['alternatives']=['Recommended: admit the proposed current-placement reconciliation while preserving the original NDJSON domain.','Retain the original location wording and leave the conflict unresolved; do not apply the affected extraction.']
for i,did,subject,reason in [('CAPRMEDIO-GOV-REQU-323','CA-D-397','Artifact/Type','Exact catl/maps/hubs/irec/ijrn prefix-to-Type table and Atom identity exclusion move as one representation contract.'),('CAPRMEDIO-GOV-REQU-676','CA-D-398','Atom/Revision/Frontmatter','Exact optional owning-Claim YAML contribution maps and current-selection exclusions move as one qualified Carrier contract; no selected Settings value is touched.')]:
    owner(did,RECORDS[i]['complete_claim_body'],LOCAL,subject,(),reason)
    whole(i,did,reason)
owner('CA-D-399','# Serialize Requirement Type Tokens\n\nConstraint **must** use Carrier token `constraint`; Boundary **must** use Carrier token `boundary`.\n',LOCAL,'Atom/Content Role: Requirement/Type',(),'One token map serves R293/R825/GOV761 without duplicating Constraint meaning, explicit external admission or Boundary meaning.')
owner('CA-D-400','# Serialize Evaluation Type Tokens\n\nQA Case **must** use Carrier token `qa_case`; Evaluation Control **must** use Carrier token `evaluation_control`; Evaluation Approach **must** use Carrier token `evaluation_approach`.\n',LOCAL,'Atom/Content Role: Evaluation/Type',(),'One Local Configuration Evaluation token map; distinct Type admission/meaning remains with its original R owners.')
owner('CA-D-401','# Serialize Concern Type Tokens\n\nQuestion **must** use Carrier token `question`; Problem **must** use Carrier token `problem`; Risk **must** use Carrier token `risk`; Opportunity **must** use Carrier token `opportunity`.\n',LOCAL,'Atom/Content Role: Concern/Type',(),'Concrete tokens only; canonical Question/Problem admission and added Risk/Opportunity remain R749.')
owner('CA-D-402','# Serialize Delivery Type Tokens\n\nRelease Definition **must** use Carrier token `release_definition`; Environment Definition **must** use Carrier token `environment_definition`.\n',LOCAL,'Atom/Content Role: Delivery/Type',(),'Concrete token map; semantic Type admission remains R751.')
owner('CA-D-403','# Serialize Operations Type Tokens\n\nRelease Record **must** use Carrier token `release_record`; Deployment Record **must** use Carrier token `deployment_record`; Environment State **must** use Carrier token `environment_state`; Health Record **must** use Carrier token `health_record`; Incident Record **must** use Carrier token `incident_record`.\n',LOCAL,'Atom/Content Role: Operations/Type',(),'Exact tokens verified in GOV752@11 frontmatter project_graph_state.artifacts.enabled_types; no spelling inferred from display names.')
owner('CA-D-404','# Serialize Method Type Tokens\n\nImplementation Method **must** use Carrier token `implementation_method`; Implementation Decision **must** use Carrier token `implementation_decision`; External Implementation Method **must** use Carrier token `external_implementation_method`; Method Binding **must** use Carrier token `method_binding`.\n',LOCAL,'Atom/Content Role: Method/Type',(),'One map serves four independently meaningful Method Types, preserving external exact-source and binding boundaries in R.')
token_groups={'CA-R-293':('CA-D-399',['constraint']),'CA-R-825':('CA-D-399',['boundary']),'CAPRMEDIO-GOV-REQU-761':('CA-D-399',['constraint']),'CAPRMEDIO-GOV-REQU-748':('CA-D-400',['qa_case','evaluation_control']),'CAPRMEDIO-R-793-REQUIREMENT-BSEED_GOVERNANCE':('CA-D-400',['evaluation_approach']),'CAPRMEDIO-GOV-REQU-751':('CA-D-402',['release_definition','environment_definition']),'CAPRMEDIO-GOV-REQU-754':('CA-D-404',['implementation_method']),'CAPRMEDIO-GOV-REQU-755':('CA-D-404',['implementation_decision']),'CAPRMEDIO-GOV-REQU-762':('CA-D-404',['external_implementation_method']),'CAPRMEDIO-GOV-REQU-763':('CA-D-404',['method_binding'])}
for identity,(target,tokens) in token_groups.items():
    changes=[]
    body=RECORDS[identity]['complete_claim_body']
    for token in tokens:
        old=(' **and** has Carrier token `'+token+'`') if (' **and** has Carrier token `'+token+'`') in body else (' with Carrier token `'+token+'`')
        changes.append((old,'',[target],'Exact token moves to the one shared D map; all Type meaning/admission and external/internal qualification remains R.'))
    edits(identity,changes,'Preserve the complete semantic Type meaning/admission; reuse one token map per Content Role and source-owner context. No Type, tier, default or Settings selection changes.')
edits('CAPRMEDIO-GOV-REQU-749',[(' **and** **must** use Carrier tokens `question` **and** `problem`, respectively','',['CA-D-401'],'Exact Question/Problem tokens move; CA-R-1231 admission reference remains R.'),(' with Carrier token `risk`','',['CA-D-401'],'Risk token moves; internal Type admission stays R.'),(' with Carrier token `opportunity`','',['CA-D-401'],'Opportunity token moves; internal Type admission stays R.')],'Retain Question/Problem canonical admission and additional internal Risk/Opportunity admission.')
edits('CAPRMEDIO-GOV-REQU-752',[(' with their existing lowercase Carrier tokens','',['CA-D-403'],'Exact map read from this same source Revision: ops:release_record, ops:deployment_record, ops:environment_state, ops:health_record, ops:incident_record. Concrete tokens go to D403; five internal Type admissions stay R.')],'Resolved at 99 from the source\'s own faithfully bound machine-readable contribution, not guessed naming. Frontmatter contributions continue to reflect the surviving admission; the token map is singular D authority.')
owner('CA-D-405','# Exclude Completed Work from the Development Backlog Carrier\n\nthe Development Backlog Carrier **must not** retain a completed-work section.\n',LOCAL,'Development Backlog',(),'The explicit content exclusion is separate from manifest-based release reconciliation and existing history destinations.')
edits('CAPRMEDIO-META-REQU-103',[('The Development Backlog does **not** retain a completed-work section. ','',['CA-D-405'],'The exact completed-work-section content prohibition moves; journal/projection rebuild and done/history provenance remain unchanged.')],'Retain exact manifest accounting, full versus partial delivery, rescheduling, Journal append and Projection regeneration. done/ and Git are existing provenance references, not a new Carrier mandate or authorization to write either.')

# Reuse governed objects instead of inventing unregistered representation/authoring paths.
subject_map={'CA-D-378':'Atom/Identifier','CA-D-379':'Epic/Identifier','CA-D-380':'Navigational Order Number','CA-D-381':'Work Sequence Number','CA-D-382':'File Carrier','CA-D-383':'Framework Instance Settings','CA-D-384':'Atom/Content Role: Implementation/Type','CA-D-385':'Projection','CA-D-386':'Priority','CA-D-387':'Framework Instance Settings','CA-D-388':'Generated Data Stage Prefix','CA-D-389':'Atom/Content Role: Analysis/Type','CA-D-390':'Artifact/Revision','CA-D-391':'Projection','CA-D-392':'Projection','CA-D-393':'Type','CA-D-394':'File Carrier','CA-D-395':'Scope Path','CA-M-275':'Scope Unit/Name'}
for identity,entity in subject_map.items():
    OWNERS[identity]['proposed_subjects']['governs']={'occurrent' if identity=='CA-M-275' else 'continuant':[entity]}
    OWNERS[identity]['subjects_rationale']='Reuse the governed object; Content Role identifies the contribution and Temporal Form belongs to the Atom-Subject relation. No representation or authoring dependent Entity is introduced.'
OWNERS['CA-R-1372']['proposed_claim_body']=OWNERS['CA-R-1372']['proposed_claim_body'].replace('\nevery Journal/Revision','\n**every** Journal/Revision')
OWNERS['CA-R-1415']['proposed_claim_body']='# Give Every Atom Revision One Version\n\n**every** Atom Revision **must** have **`=1`** positive integer Version that increases monotonically across successive Revisions of the same Atom.\n'
OWNERS['CAPRMEDIO-GOV-REQU-315']['proposed_subjects']={'governs':{'continuant':['Logging Policy']},'depends_on':{'continuant':['Evaluation Control','Production Evaluation Checklist']}}
OWNERS['CAPRMEDIO-GOV-REQU-315']['subjects_rationale']='The retained Claim governs Logging Policy. Reuse this existing named prerequisite from CA-M-163 and GOV315 body instead of the unrelated generic evaluation occurrence; concrete record shape is allocated to D396.'
def finish_design():
    # The root's checkpoint records the direct Operator resolution; no new approval
    # or Journal storage/migration operation is inferred from it.
    approval={'status':'approved','source':'Direct Operator response relayed by the coordinating root in this execution: continue, selecting the D328 dedicated-folder explanation.','decision':'Preserve each Journal registered D-defined placement, including D328 dedicated .caprmedio_caprmedio/work_journal/ and D339 Implementation Content Role directory. Preserve append-only NDJSON throughout the original governed workflow/local-control Journal domain.','authorization_boundary':'Disposition design only; no new storage, migration, Journal write, source-owner move or selected Settings change.'}
    d=DESIGNS['CAPRMEDIO-GOV-REQU-315']
    d.update(admission='admitted',confidence_percent=99,operator_resolution=approval)
    d.pop('operator_question',None); d.pop('alternatives',None)
    d['rationale']=d['rationale'].replace('location conflict remains unadmitted.','the direct Operator resolution preserves each registered Journal placement.')
    for a in d['clause_allocations']:
        a['rationale']=a['rationale'].replace('Location reconciliation is explicitly pending Operator decision; no silent scope equivalence between Journal Types.','The Operator approved reuse of each registered placement. D328 and D339 retain their distinct domains; D406 covers the remainder of the original NDJSON domain without duplicating their contracts.')
    o=OWNERS['CA-D-406']
    o.update(admission='admitted',operator_resolution=approval,rationale='Approved placement reconciliation. Reuse D328 and D339 unchanged for their exact Journal domains; impose the original append-only NDJSON contract only on other governed workflow/local-control Journals, at their registered places.')
    o['proposed_claim_body']='# Serialize Governed Workflow Journal Carriers\n\n**every** governed CAPRMEDIO workflow **or** local project-control Journal Carrier whose append-only NDJSON representation is **not** already governed by CA-D-328 **or** CA-D-339 **must** use append-only NDJSON **in** its applicable registered authoritative place. the CAPRMEDIO Project Work Journal follows CA-D-328; the Implementation Journal follows CA-D-339.\n'
    OWNERS['CAPRMEDIO-GOV-REQU-315']['rationale']=d['rationale']
    # These are Entity choices from the complete Claims, not mechanically copied
    # GOVERNS entries. Carrier is intentionally generic for streamed logs/symlinks.
    subjects={
      'CA-D-378':('Atom/Identifier',['Atom/Content Role','Project','Atom Collection/Type: Epic/Identifier'],'Identifier grammar requires role, Project prefix and the separate Epic identifier domain.'),
      'CA-D-379':('Atom Collection/Type: Epic/Identifier',['Atom Collection/Type: Epic','Project','Scope Unit'],'Reuse R1304 exact Epic Identifier Entity; the grammar uses Epic, Project and Scope components.'),
      'CA-M-275':('Scope Unit/Name',['Scope Unit'],'The reusable writing Method governs the existing persistent Name, so CONTINUANT is independent of the Method role.'),
      'CA-D-380':('Navigational Order Number',['Carrier','Scope Unit'],'The represented number requires a Carrier and the non-Project Scope Unit domain for minimum width.'),
      'CA-D-381':('Work Sequence Number',['Carrier'],'The ordinal is governed through its Carrier rendering; it is not its own prerequisite.'),
      'CA-D-382':('File Carrier',['Project','Project-Owned Carrier Root'],'Local environment File placement and discovery exclusions require the Project and its authority root. Runtime configuration remains a descriptive phrase, not a new Entity.'),
      'CA-D-383':('Framework Instance Settings/Authoritative Carrier/Content',['Framework Instance Settings'],'Existing Settings Carrier content is governed; the Settings supplies the reporting setting and semantic default.'),
      'CA-D-384':('Atom/Content Role: Implementation/Type',['Carrier'],'The Implementation Type map specifies Carrier tokens; native commit identity remains R296.'),
      'CA-D-385':('Projection',['Scope Unit','Atom/Claim'],'The optional view requires its Scope hierarchy and represented source Claims.'),
      'CA-D-386':('Atom/Carrier',['Atom/Content Role','Priority','Atom Collection/Type: Epic'],'One Priority storage contract requires role eligibility, semantic Priority and the additional Epic exclusion.'),
      'CA-D-387':('Framework Instance Settings/Authoritative Carrier/Content',['Framework Instance Settings'],'The Settings owns admission strictness; this contribution encodes its exact field.'),
      'CA-D-388':('Generated Data Stage Prefix',['Journal','Projection','Carrier/Format'],'Reuse the existing Prefix Entity; Journal and Projection define the limited domain and Carrier Format supplies NDJSON/TOON.'),
      'CA-D-389':('Atom/Content Role: Analysis/Type',['Carrier'],'The existing qualified Type Entity is encoded by the Carrier map.'),
      'CA-D-390':('Framework Instance Settings/Artifact Timestamp Timezone',['Framework Instance Settings','Artifact/Revision','Carrier'],'Reuse the original timestamp timezone Entity; Settings provides interpretation for emitted Revision timestamps.'),
      'CA-D-391':('Project Scope Unit Graph Projection/Authority Modes',['Framework Instance Settings','Project','Scope Unit','Authority Mode'],'Reuse original exact governed Projection property and declare each independently owned selection/domain prerequisite.'),
      'CA-D-392':('Project Scope Unit Graph Projection',['Project Settings','Project Name','Obsolete Project Name'],'The consuming Projection exposes independently owned canonical and prior Project names.'),
      'CA-D-393':('Type',['Atom/Content Role','Carrier'],'External token derivation requires the role default and its Carrier representation; Type meaning is not redefined.'),
      'CA-D-394':('Carrier',['Methodology Source','Project'],'A convenience symlink can expose files or directories; generic Carrier avoids inventing a File-only limitation. The existing native source and Project ownership remain prerequisites.'),
      'CA-D-395':('Carrier/Representation',['Project','Scope Unit'],'The existing representation Entity is narrowed in the Claim to scope_path, with ambient Project and Scope addressing as prerequisites.'),
      'CA-D-396':('Carrier',['Logging Policy'],'The structured record contract applies to log Carriers including streams; no File-only storage restriction is introduced.'),
      'CA-D-397':('Artifact/Type',['Artifact','Atom/Identifier'],'Type prefixes distinguish Artifact forms from Atom identity encoding.'),
      'CA-D-398':('Atom/Revision/Frontmatter',['Atom/Claim','Project Scope Unit Graph Projection','Project Settings','Framework Instance Settings'],'The optional YAML contribution is bounded by its owning Claim, consuming Projection and separate Settings authorities.'),
      'CA-D-399':('Atom/Content Role: Requirement/Type',['Carrier'],'Carrier representation of already admitted Requirement Types.'),
      'CA-D-400':('Atom/Content Role: Evaluation/Type',['Carrier'],'Carrier representation of already admitted Evaluation Types.'),
      'CA-D-401':('Atom/Content Role: Concern/Type',['Carrier'],'Carrier representation of already admitted Concern Types.'),
      'CA-D-402':('Atom/Content Role: Delivery/Type',['Carrier'],'Carrier representation of already admitted Delivery Types.'),
      'CA-D-403':('Atom/Content Role: Operations/Type',['Carrier'],'Carrier representation of already admitted Operations Types, read exactly from GOV752 own contribution.'),
      'CA-D-404':('Atom/Content Role: Method/Type',['Carrier'],'Carrier representation of already admitted Method Types.'),
      'CA-D-405':('Development Backlog',['Carrier'],'The Backlog is governed only for one Carrier content exclusion.'),
      'CA-D-406':('Journal/Carrier',['Journal','Work Journal','Implementation Journal','Project'],'Existing Journal Carrier Entity; exact Work/Implementation domains and Project registry bound reuse and residual format coverage.'),
    }
    for identity,(governs,deps,reason) in subjects.items():
        assert governs not in deps and len(deps)==len(set(deps))
        OWNERS[identity]['proposed_subjects']={'governs':{'continuant':[governs]},'depends_on':{'continuant':deps}}
        OWNERS[identity]['subjects_rationale']=reason+' Reviewed against CA-M-125 and CA-E-246: one governed Entity, genuine prerequisites, no duplicate Subject, no role-derived Temporal Form.'
    # Normative operators and already governed Terms in newly drafted fragments.
    OWNERS['CA-D-378']['proposed_claim_body']=OWNERS['CA-D-378']['proposed_claim_body'].replace('with Content Role Identity Letters (','the Atom Content Role Identity Letter **must** be **in** (')
    OWNERS['CA-D-378']['proposed_claim_body']=OWNERS['CA-D-378']['proposed_claim_body'].replace('`, the Atom','`. the Atom')
    OWNERS['CA-D-396']['proposed_claim_body']=OWNERS['CA-D-396']['proposed_claim_body'].replace('record includes,','record **must** include,')
    OWNERS['CA-D-393']['proposed_claim_body']=OWNERS['CA-D-393']['proposed_claim_body'].replace('Content role','Content Role')
    for o in OWNERS.values():
        if o['status']!='new_proposed_identity_not_reserved': continue
        lines=o['proposed_claim_body'].splitlines(keepends=True)
        normalized=[]
        for line in lines:
            if line.startswith('#'):
                normalized.append(line); continue
            parts=re.split(r'(`[^`]*`|\*\*.*?\*\*)',line)
            for n in range(0,len(parts),2):
                value=parts[n]
                value=re.sub(r'\b(?:A|An|The|It|Its|For|These|Unregistered|Governed)\b(?=\s)',lambda m:m.group().lower(),value)
                value=re.sub(r'(?<![\w-])(?:artifact|atom|project|scope|revision|claim|operator|carrier|projection)(?![\w-])',lambda m:m.group().title(),value)
                value=re.sub(r'(?<![\w-])(?:must not|not in|is not empty|is empty|starts with|ends with|to|means|must|may|if|then|when|otherwise|before|after|until|unless|all|every|any|none|and|or|not|without|where|only|in|contains)(?![\w-])',lambda m:'**'+m.group()+'**',value)
                parts[n]=value
            normalized.append(''.join(parts))
        o['proposed_claim_body']=''.join(normalized)
        o['rendering_review']='New Carrier/Method Claims normalize registered operators under M229/M234/D280; governed Terms reuse existing meanings; literal code tokens and headings are preserved.'
    OWNERS['CA-D-385']['proposed_claim_body']=OWNERS['CA-D-385']['proposed_claim_body'].replace('child scopes','child Scopes').replace('represented claims','represented Claims')
    OWNERS['CA-D-353']['proposed_subjects']={'governs':{'continuant':['Structural Entity']},'depends_on':{'continuant':['Directory Carrier','Atom Collection/Type: Epic']}}
    OWNERS['CA-D-353']['subjects_rationale']='The stricter Epic qualification requires the already governed Epic subtype; Structural Entity remains the single governed Entity.'
    OWNERS['CA-R-1415']['proposed_subjects']={'governs':{'continuant':['Atom/Revision/Version']},'depends_on':{'continuant':['Atom/Revision','Atom']}}
    OWNERS['CA-R-1415']['subjects_rationale']='Monotonicity compares successive Revisions of the same Atom, so Atom is a genuine added prerequisite.'
    OWNERS['CA-D-283']['proposed_subjects']={'governs':{'continuant':['Project-Owned Markdown Atom Carrier/Filename']},'depends_on':{'continuant':['Atom/Identifier','Atom/Revision','Atom/Summary','Atom/Scope']}}
    OWNERS['CA-D-283']['subjects_rationale']='Same-identity preservation through Summary or Scope change explicitly requires the Identifier, Revision, Summary and Scope Entities.'
    # Role-changing replacements keep the whole original Claim's supporting
    # relation envelope. The M replacement uses the explicitly reviewed method_for.
    for d in DESIGNS.values():
        if d['action']!='replace': continue
        targets={t for a in d['clause_allocations'] for t in a['owners']}
        if len(targets)!=1: continue
        target=next(iter(targets)); o=OWNERS[target]
        if o['status']!='new_proposed_identity_not_reserved' or target=='CA-M-275': continue
        section=re.search(r'^relations:\s*\n((?:[ \t].*(?:\n|$))*)',RECORDS[d['before']['canonical_identity']]['frontmatter_text'],re.M)
        if not section: continue
        key=None
        for line in section.group(1).splitlines():
            match=re.match(r'^  ([a-z_]+):\s*$',line)
            if match: key=match.group(1); continue
            match=re.match(r'^    -\s*(.+?)\s*$',line)
            if match and key:
                value=match.group(1).strip('"\'')
                o['proposed_relations'].setdefault(key,[])
                if value not in o['proposed_relations'][key]: o['proposed_relations'][key].append(value)
        o['outgoing_relation_review']='Preserve the replaced complete Claim supporting relation envelope; retain legacy decorated target spelling where unchanged. Canonical reference normalization is permitted only after exact target resolution, not a source-owner migration.'
    DESIGNS['CAPRMEDIO-GOV-REQU-337']['illustrative_content_review']='The retained Mermaid relation maps phrase occurs after including, alongside Requirement groupings by Scope and tier. It illustrates consumer-ready semantic Projection uses; it does not require every Carrier to use Mermaid. Preserve it in the semantic stage meaning; D388 alone governs the explicit stage prefixes and NDJSON/TOON formats.'
    DESIGNS['CA-R-1372']['action']='normalize_semantic_spelling'
    DESIGNS['CA-R-1372']['clause_allocations'].append(alloc('every Journal/Revision',['CA-R-1372'],'CCE-only normalization to **every** Journal/Revision preserves the original universal quantifier.'))
    DESIGNS['CA-R-165']['clause_allocations'].insert(0,alloc('**every** Atom Revision **must** have',['CA-R-1415','CA-R-1416'],'Both surviving semantic owners quantify every Atom Revision and retain the original obligation.'))
    DESIGNS['CA-R-165']['clause_allocations'].append(alloc(' **and** ',['CA-R-1415','CA-R-1416'],'Both properties remain simultaneously required, rather than alternatives, through the two universally applicable surviving Requirements.'))
    DESIGNS['CAPRMEDIO-GOV-REQU-302']['clause_allocations'].append(alloc(RECORDS['CAPRMEDIO-GOV-REQU-302']['complete_claim_body'].splitlines()[2],['CAPRMEDIO-GOV-REQU-302','CA-D-387'],'The complete first clause keeps the two strictness selections, Settings ownership and medium default in R302; D387 alone carries the extracted artifacts.creation_strictness field path.'))
    # Full old source remains in the audit and exact Archive; below make unchanged
    # text explicit so the old whole-body fallback cannot hide an unallocated edit.
    for identity,d in DESIGNS.items():
        original=RECORDS[identity]['complete_claim_body']
        d['original_claim_body']=original
        d['clause_allocations']=[a for a in d['clause_allocations'] if not a['rationale'].startswith('All original text outside')]
        if identity in OWNERS and OWNERS[identity]['status']=='revise':
            after=OWNERS[identity]['proposed_claim_body']
            d['retained_claim_changes']=[]
            for tag,a,b,c,e in difflib.SequenceMatcher(None,original,after,autojunk=False).get_opcodes():
                if tag=='equal':
                    d['clause_allocations'].append(alloc(original[a:b],[identity],'Exact unchanged span survives in the retained same-identity Claim.'))
                else:
                    d['retained_claim_changes'].append({'kind':tag,'before_start':a,'before_end':b,'before_text':original[a:b],'after_start':c,'after_end':e,'after_text':after[c:e]})
        for a in d['clause_allocations']:
            a['after_claims']={target:OWNERS[target]['proposed_claim_body'] for target in a['owners']}
        d['admission_boundary']='Admitted disposition design at threshold 99; implementation and retirement remain gated by this mapping and refreshed evidence.'
        d['retirement_gate']={'requires_all_mapped_repairs':True,'may_retire_before_repairs':False,'implementation_task':'CA-P-962 or CA-P-963 according to source owner; cross-owner necessary reference repairs may be completed first.'}
        d['execution_revision_handoff']='CA-P-962 must repair Local GOV761/GOV762 and GOV-EVAL-006 before affected Core extraction or retirement. CA-P-963 must refresh those sanctioned newer source Revisions, preserve their repaired references, and archive every intermediate Revision it changes. The CA-P-960 snapshot is the original evidence baseline, never an instruction to overwrite a newer sanctioned Revision.'
    # Preserve prior owner Revisions as exactly as candidate Revisions.
    for identity,o in OWNERS.items():
        if identity in RECORDS:
            r=RECORDS[identity]
            o['prior_source_text']=r['complete_source_text']
            o['proposed_version']=r['version']+(o['status']=='revise')
            o['archive']={'required':o['status']=='revise','path':str(Path(r['source_path']).parent/'archive'/(Path(r['source_path']).stem+'@'+str(r['version'])+'.md')),'sha256':r['sha256'],'byte_rule':'Exact prior source bytes, no normalization; identical existing Archive reusable, conflicting Archive blocks.'}
        o['proposed_cce_version']='cce_1'
        o['proposed_cce_form']='method' if o['content_role']=='Method' else 'serialization' if o['status']=='new_proposed_identity_not_reserved' else re.search(r'^cce_form:\s*(.+)$',RECORDS[identity]['frontmatter_text'],re.M).group(1)
        o['subject_review_status']='reviewed' if o.get('proposed_subjects') else 'retain existing Subjects for preserved primary Claim; no broad Subject normalization admitted'

finish_design()

def incoming_scan():
    identities=set(DESIGNS)|{i for i,o in OWNERS.items() if o['status']=='revise'}
    pattern='(?<![A-Za-z0-9])(?:'+'|'.join(re.escape(i) for i in sorted(identities,key=len,reverse=True))+')(?![0-9])'
    cmd=['rg','--json','--hidden','--no-ignore','--pcre2','-g','!**/.git/**','-g','!**/.env','-g','!**/.env.*','-g','!**/*.env','-g','!**/execution_evidence/**',pattern,'.']
    proc=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    if proc.returncode not in (0,1): raise RuntimeError(proc.stderr)
    refs=[]
    cache={}
    for line in proc.stdout.splitlines():
        event=json.loads(line)
        if event['type']!='match': continue
        data=event['data']; path=data['path'].get('text')
        if path is None: continue
        path=path.removeprefix('./'); text=data['lines'].get('text','').rstrip('\n'); lineno=data['line_number']
        if path not in cache:
            raw=(ROOT/path).read_bytes()
            value=raw.decode('utf-8',errors='replace')
            header=re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)',value,re.S)
            cache[path]={'sha256':hashlib.sha256(raw).hexdigest(),'text':value,'lines':value.splitlines(),'header':header.group(1) if header else None,'header_end':value[:header.end()].count('\n') if header else 0}
        f=cache[path]
        inactive=any(x in Path(path).parts for x in ('archive','draft','drafts','done','solved','goals_archive','jobs_archive'))
        generated=bool(re.search(r'00_APPLICABLE_METHODOLOGY/0[45679]_',path) or '.projection.' in path or '/.caprmedio_install/' in '/'+path or '/.caprmedio_runtime/' in '/'+path)
        role=next((x for x in Path(path).parts if x in ('04_requirement','05_method','06_evaluation','07_delivery')),None)
        rmed=bool(role and f['header'] is not None and not inactive and not generated)
        in_scope=path in {r['source_path'] for r in INV['records']}
        relation=None
        if f['header'] is not None and lineno <= f['header_end']:
            active_top=None; active_key=None
            for l in f['lines'][:lineno]:
                if re.match(r'^\w[^:]*:',l): active_top=l.split(':',1)[0]
                m=re.match(r'^  ([a-z_]+):\s*$',l)
                if m: active_key=m.group(1)
            if active_top=='relations': relation=active_key
        for match in re.finditer(pattern,text):
            identity=match.group()
            if re.match(r'^atom_id\s*:',text): continue
            if in_scope and RECORDS.get(identity,{}).get('source_path')==path: continue
            disposition=DESIGNS.get(identity)
            targets=([identity] if not disposition or not disposition['retirement_requested'] else sorted({t for a in disposition['clause_allocations'] for t in a['owners']}))
            if inactive or generated:
                classification='remaining_nonblocking_reconciliation'; rationale='Historical or generated mention: preserve history or regenerate through its separately governed process. It does not itself establish an active RMED dependency.'
            elif rmed and disposition and disposition['retirement_requested']:
                classification='required_pre_retirement_repair'; rationale='Active RMED reference to an identity proposed for retirement. Repair its semantic target before retiring that identity.'
            elif rmed:
                classification='remaining_nonblocking_reconciliation'; rationale='The referenced identity remains active with the semantic contribution preserved; inspect its consumer Claim for any separately extracted representation dependency.'
            else:
                classification='out_of_scope_followup'; rationale='Non-RMED consumer outside source mutation scope. Reconcile only under separately applicable authority; this mention alone does not block retirement.'
            excerpt=text if len(text)<=800 else text[max(0,match.start()-180):match.end()+180]
            refs.append({'reference_id':len(refs)+1,'target_before':identity,'consumer_path':path,'consumer_sha256':f['sha256'],'line':lineno,'column':match.start()+1,'before_text':excerpt,'before_text_is_excerpt':len(text)>800,'typed_relation':relation,'consumer_active_RMED':rmed,'consumer_in_mutation_scope':in_scope,'consumer_context':'historical' if inactive else 'generated_or_installed' if generated else 'active_RMED' if rmed else 'other','classification':classification,'proposed_targets':targets,'mapping_rationale':rationale,'mutation_authority':'CA-P-962 or CA-P-963 source scope' if in_scope else 'Separate Operator authorization and completion required for any out-of-scope repair','blocking_external_prerequisite':classification=='required_pre_retirement_repair' and not in_scope})
    reviews={
      ('CAPRMEDIO-GOV-REQU-302','CAPRMEDIO-GOV-REQU-294'):(['CAPRMEDIO-GOV-REQU-294'],'The admission Claim points to reporting behavior for its focused-question workflow. R294 retains silent/verbose behavior and mandatory exception reporting; the consumer does not prescribe [interaction].reporting_mode encoding. Retain this semantic relation; canonicalize the legacy decorated target while revising this already affected source.',False),
      ('CAPRMEDIO-GOV-EVAL-009','CAPRMEDIO-GOV-REQU-299'):(['CAPRMEDIO-GOV-REQU-299','CA-D-386'],'Applicable conditions 1–3 test stored priority eligibility, exact high/medium/low values, and rejection of highest/critical/deferred. Conditions 4–7 test the surviving R comparison and selection semantics. Retain R299 and add D386 to evaluation_for before extracting its Carrier clauses.',True),
      ('CA-E-427','CA-R-1304'):(['CA-D-379'],'The check requires one canonical Epic Identifier and rejects malformed identifiers; that exact grammar moves wholly from R1304 to D379. Replace this evaluation_for target only after D379 is admitted, before retiring R1304.',False),
      ('CA-E-427','CA-R-1369'):(['CA-D-353'],'The check rejects !=1 Epic Directory Carriers. D353 must first include the stricter =1 Epic qualification, then replace R1369 in evaluation_for before retiring it. D263 inverse per-directory cardinality is not interchangeable.',False),
      ('CAPRMEDIO-GOV-REQU-314','CAPRMEDIO-GOV-REQU-748'):(['CAPRMEDIO-GOV-REQU-748'],'The checklist Claim consumes the admitted Evaluation Control Type and distinguishes control meaning, realization and result. evaluation_control is its reference to that Type, not an independent encoding obligation or token validation. R748 still admits that Type; retain its semantic relates_to target. No optional D400 link is added.',False),
      ('CAPRMEDIO-GOV-REQU-762','CAPRMEDIO-GOV-REQU-760'):(['CA-D-393'],'External Implementation Method uses the default external-name derivation context. D393 retains the external_<internal_type_name> rule, role-default qualification and explicit non-default exception. Replace the entire decorated relates_to value with canonical CA-D-393 before retiring GOV760.',False),
      ('CAPRMEDIO-GOV-REQU-761','CAPRMEDIO-GOV-REQU-760'):(['CA-D-393'],'Constraint explicitly uses the non-default external-name exception and is not derived from the default rule. D393 preserves that exception. Replace the entire decorated relates_to value with canonical CA-D-393 before retiring GOV760.',False),
      ('CAPRMEDIO-GOV-EVAL-006','CAPRMEDIO-GOV-REQU-294'):(['CAPRMEDIO-GOV-REQU-294','CA-D-383'],'Conditions 1, 4, 6 and 7 load/parse Settings, test the two allowed reporting values, reject unknown keys where closed, and require deterministic settings. R294 preserves allowed behavior/values; D383 owns the extracted field path. Retain R294 and add D383 before extraction.',True),
      ('CAPRMEDIO-GOV-EVAL-006','CAPRMEDIO-GOV-REQU-302'):(['CAPRMEDIO-GOV-REQU-302','CA-D-387'],'Conditions 1, 3, 6 and 7 load/parse Settings, test medium/high admission strictness, reject unknown keys where closed, and require deterministic settings. R302 preserves allowed strictness/default; D387 owns the extracted field. Retain R302 and add D387 before extraction.',True),
      ('CAPRMEDIO-FRAMEWORK-ENGINE-REQU-561','CAPRMEDIO-GOV-REQU-337'):(['CAPRMEDIO-GOV-REQU-337'],'The complete consumer routes stage selection, validation and materialization through the governed stage vocabulary and deterministic Tools without redefining either. Retained GOV337 still registers the four stage meanings, their prefix cross-references and all forward-only dependency constraints. It points to D388 for physical formats. No consuming vocabulary clause loses its authority; the external child_of relation remains valid.',False),
      ('CA-M-163','CAPRMEDIO-GOV-REQU-315'):(['CAPRMEDIO-GOV-REQU-315'],'The complete Method expressly consumes ERROR/WARNING/INFO/DEBUG meanings and actionable, sanitized, bounded diagnostics. GOV315 retains those meanings, retention/failure behavior and the no-Journal-as-log-sink boundary. Method step 4 already delegates Carrier placement/encoding to Delivery; no new external rewrite is required.',False),
    }
    unknown=[]
    for ref in refs:
        ref['review_status']='reviewed'
        if ref['consumer_active_RMED']:
            stem=Path(ref['consumer_path']).stem
            consumer=next((i for i in sorted({key[0] for key in reviews},key=len,reverse=True) if stem==i or stem.startswith(i+'-')),None)
            review=reviews.get((consumer,ref['target_before']))
            if not review:
                unknown.append(ref['reference_id']); ref['review_status']='unresolved'; continue
            targets,reason,pre_extraction=review
            ref.update(proposed_targets=targets,mapping_rationale=reason,required_before_extraction=pre_extraction,consumer_review='Complete current consumer Claim read and interpreted against exact proposed owner Claims.')
            if pre_extraction: ref['classification']='remaining_nonblocking_reconciliation'
            ref['repair_phase']='before affected clause extraction in CA-P-962' if pre_extraction else 'before old target retirement' if ref['classification']=='required_pre_retirement_repair' else 'no blocking repair'
            if ref['typed_relation']:
                ref['proposed_relation_values']=targets
                ref['repair_instruction']='Replace the entire selected decorated relation value with the canonical target list; preserve unrelated relation values and all consumer clauses. Deduplicate and canonically order under D268.'
        else:
            ref['required_before_extraction']=False
            if ref['consumer_context']=='historical' or '/work_journal/' in ref['consumer_path']:
                ref['classification']='remaining_nonblocking_reconciliation'
                ref['mapping_rationale']='Historical content or append-only Journal provenance records the original identity/revision; retain its exact historical reference. proposed_targets records the future authority lookup, not a history rewrite.'
            elif ref['consumer_context']=='generated_or_installed':
                ref['mapping_rationale']='Generated/installed consumer is downstream of the current source frontier, not an independent active RMED authority. Rebuild/reinstall only under separately authorized work; this task preserves its current bytes.'
            else:
                ref['mapping_rationale']='Read-only inspected non-RMED mention in analysis, concern, plan, Settings provenance, implementation migration/map or report. The occurrence is not an active RMED authority dependency. Preserve now and reconcile only through the separately applicable downstream workflow; no selected Settings or Tool mutation is admitted.'
    result={'task':'CA-P-961@2','scan':'Repository-wide rg --hidden --no-ignore text scan, including ignored paths. Symlinks are not followed; .git, secret-file paths and task evidence are excluded. Source, generated, installed, historical and external consumers inspected read-only.','status':'complete' if not unknown else 'blocked_unreviewed_active_consumer','references':refs,'unreviewed_active_reference_ids':unknown,'summary':{'occurrences':len(refs),'consumers':len(cache),'active_RMED_occurrences':sum(r['consumer_active_RMED'] for r in refs),'required_pre_retirement':sum(r['classification']=='required_pre_retirement_repair' for r in refs),'required_before_extraction':sum(r.get('required_before_extraction',False) for r in refs),'external_blockers':sum(r['blocking_external_prerequisite'] for r in refs)}}
    save('incoming-references.json',result)
    print(json.dumps({'references':len(refs),'active_RMED':sum(r['consumer_active_RMED'] for r in refs),'required':sum(r['classification']=='required_pre_retirement_repair' for r in refs)}))
    return result

def output(references):
    failures=[]
    for r in INV['records']:
        path=ROOT/r['source_path']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=r['sha256']: failures.append(r['source_path'])
    candidates={r['canonical_identity'] for r in INV['records'] if r['disposition']['category'] not in ('justified_non_D_contribution','existing_D_authority')}
    coverage=[]
    for identity,d in DESIGNS.items():
        body=RECORDS[identity]['complete_claim_body']; covered=[False]*len(body)
        for a in d['clause_allocations']:
            for match in re.finditer(re.escape(a['before_quote']),body):
                covered[match.start():match.end()]=[True]*(match.end()-match.start())
        uncovered=[]; offset=0
        for line in body.splitlines(keepends=True):
            # Heading/table labels are presentation, not silently missing obligations.
            label=line.startswith('#') or bool(re.match(r'^\|[ |:-]+\|\s*$',line)) or line.strip() in ('| Prefix | Stage meaning |','| Artifact form | Type | Prefix |')
            missing=''.join(c for n,c in enumerate(line,offset) if not covered[n] and (c.isalnum() or c in '`*<>='))
            if missing and not label: uncovered.append({'line':line.rstrip(),'unallocated_characters':missing})
            offset+=len(line)
        coverage.append({'identity':identity,'all_substantive_original_text_allocated':not uncovered,'unallocated':uncovered,'allocation_count':len(d['clause_allocations']),'review':'Complete source/after Claims compared for meaning, domain, conditions and modality; exact unchanged spans and original extracted clauses recorded. This coverage check corroborates the semantic review; it is not a proof of semantic equivalence.'})
    source_root=ROOT/'.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources'
    actual={str(p.relative_to(ROOT)) for so in (CORE,LOCAL) for p in (source_root/so).rglob('*.md') if any(v in p.parts for v in ('04_requirement','05_method','06_evaluation','07_delivery')) and not any(v in p.relative_to(source_root/so).parts for v in ('archive','draft','drafts','done','solved'))}
    expected={r['source_path'] for r in INV['records']}
    new_ids=sorted(i for i,o in OWNERS.items() if o['status']=='new_proposed_identity_not_reserved')
    pat='(?<![A-Za-z0-9])(?:'+'|'.join(map(re.escape,new_ids))+')(?![0-9])'
    args=['rg','--hidden','--no-ignore','--pcre2','-n','-g','!**/.git/**','-g','!**/.env','-g','!**/.env.*','-g','!**/*.env','-g','!**/execution_evidence/**',pat,'.']
    collision_scan=subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
    if collision_scan.returncode not in (0,1): raise RuntimeError(collision_scan.stderr)
    names=subprocess.run(['rg','--files','--hidden','--no-ignore','-g','!**/.git/**','-g','!**/.env','-g','!**/.env.*','-g','!**/*.env','-g','!**/execution_evidence/**','.'],cwd=ROOT,text=True,capture_output=True,check=True).stdout.splitlines()
    filename_collisions=[p for p in names if re.search(pat,p)]
    archive_checks=[]
    for identity,o in OWNERS.items():
        if not o.get('archive',{}).get('required'): continue
        a=o['archive']; path=ROOT/a['path']; digest=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
        archive_checks.append({'identity':identity,'path':a['path'],'expected_sha256':a['sha256'],'existing_sha256':digest,'status':'must_create_exact_copy' if digest is None else 'identical_reusable' if digest==a['sha256'] else 'conflicting_archive'})
    for identity,d in DESIGNS.items():
        if identity in OWNERS or not d['archive']['required']: continue
        a=d['archive']; path=ROOT/a['path']; digest=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
        archive_checks.append({'identity':identity,'path':a['path'],'expected_sha256':a['sha256'],'existing_sha256':digest,'status':'must_create_exact_copy' if digest is None else 'identical_reusable' if digest==a['sha256'] else 'conflicting_archive'})
    subject_failures=[]
    for identity,o in OWNERS.items():
        s=o.get('proposed_subjects')
        if not s: continue
        governed=[v for vs in s['governs'].values() for v in vs]
        deps=[v for vs in s.get('depends_on',{}).values() for v in vs]
        if len(governed)!=1 or len(governed+deps)!=len(set(governed+deps)): subject_failures.append(identity)
    owners_missing=sorted({t for d in DESIGNS.values() for a in d['clause_allocations'] for t in a['owners']}-set(OWNERS))
    acceptance={
      'all_50_candidates_dispositioned':candidates==set(DESIGNS),
      'all_clauses_allocated':all(r['all_substantive_original_text_allocated'] for r in coverage),
      'all_owners_resolve':not owners_missing,
      'all_source_hashes_unchanged':not failures,
      'source_frontier_unchanged':actual==expected,
      'all_proposed_ids_globally_available':not collision_scan.stdout and not filename_collisions,
      'archive_paths_safe':not any(a['status']=='conflicting_archive' for a in archive_checks),
      'subjects_one_governed_no_duplicates':not subject_failures,
      'all_dispositions_admitted_at_99':all(d['admission']=='admitted' and d['confidence_percent']>=99 for d in DESIGNS.values()),
      'references_review_complete':references['status']=='complete',
      'no_unresolved_external_retirement_blocker':references['summary']['external_blockers']==0,
      'analysis_identity_letter_preserved':'Analysis: A' in OWNERS['CA-D-378']['proposed_claim_body'],
      'version_monotonicity_preserved':'increases monotonically across successive Revisions of the same Atom' in OWNERS['CA-R-1415']['proposed_claim_body'],
      'date_time_unambiguity_preserved':'unambiguous Updated At date-time' in OWNERS['CA-R-1416']['proposed_claim_body'],
      'stricter_epic_cardinality_preserved':'**every** Epic **must** have **`=1`** Directory Carrier' in OWNERS['CA-D-353']['proposed_claim_body'],
      'journal_resolution_approved':DESIGNS['CAPRMEDIO-GOV-REQU-315']['operator_resolution']['status']=='approved',
    }
    passed=all(acceptance.values())
    verification={'task':'CA-P-961@2','result':'PASS' if passed else 'FAIL','checks':acceptance,'clause_coverage':coverage,'source_refresh':{'count':len(expected),'sha256_mismatches':failures,'added':sorted(actual-expected),'removed':sorted(expected-actual)},'proposed_identity_availability':{'ids':new_ids,'reservation':'none; recheck immediately before admission','content_collisions':collision_scan.stdout.splitlines(),'filename_collisions':filename_collisions},'archive_checks':archive_checks,'subject_failures':subject_failures,'missing_owners':owners_missing,'reference_summary':references['summary'],'verification_limits':'Design review plus deterministic evidence checks; no source schema/compiler, Tools, install/runtime, Projection, Journal, Task lifecycle or Git workflow was run or modified.'}
    save('verification.json',verification)
    save('dispositions.json',{'task':'CA-P-961@2','status':'ready_for_source_implementation' if passed else 'verification_failed','authority_basis':['CA-R-1339@3','CA-R-1340@3','CA-R-1341@3','CA-R-1342@3','CA-M-271@2','CA-D-285@5','CA-M-125@12','CA-E-246@10','CA-M-229@5','CA-M-234@6','CA-D-280@6','CA-M-001@9','CA-M-002@12','CA-M-005@7','CA-M-006@7','CA-P-033@9'],'effective_confidence_threshold':99,'confidence_source':'Direct Operator instruction and Task value agree at 99; no Settings selection changed.','source_refresh':verification['source_refresh'],'dispositions':list(DESIGNS.values()),'authority_owners':list(OWNERS.values()),'remaining_candidates':sorted(candidates-set(DESIGNS)),'incoming_reference_evidence':'CA-P-961-incoming-references.json','verification_evidence':'CA-P-961-verification.json','implementation_order':['Refresh exact source frontier, source hashes, proposed ID availability and Archive paths.','Admit surviving authority owners and preserve all required prior Revisions exactly.','Repair the four pre-retirement and three pre-extraction incoming references in both permitted source owners; verify each intended target and consumer clause.','Only then retire replaced identities or extract affected clauses. Preserve all original semantic qualifications and source ownership.','Leave generated/installed/historical and non-RMED downstream mentions to their separately authorized processes.'],'overlap_review':['D268 remains general owned direct-relation encoding; D272 retains the distinct Task-prerequisite qualification. Neither is retired by this design.','D363 retains lowercase Project-name filename grammar; D364 retains exact root placement and exactly-one authoritative Carrier. No consolidation or Settings move is admitted.','D328 and D339 retain their original distinct Journal domains. D406 applies only to the remainder of GOV315 original NDJSON domain, avoiding duplicate Carrier contracts.'],'limitations':['Proposed identities are available but not reserved or source Atoms; refresh before implementation.','Read-only repository text scan does not follow symlinks or inspect secret files; generated/installed data remain downstream, including newly discovered ignored paths.','No source, lifecycle, Settings selection, generated projection, runtime, install, Journal or Git writes.']})
    report=f'''# CA-P-961 lossless Carrier authority disposition design

Non-authoritative evidence for CA-P-961@2. Result: **{'PASS' if passed else 'FAIL'}**. All 50 candidates have explicit dispositions at the effective threshold of 99. This completes design evidence only; the coordinating agent owns Task lifecycle disposition.

The exact current 698-source frontier and every captured SHA-256 still match CA-P-960. `{len(OWNERS)}` surviving owner records contain complete proposed Claims; `{len(new_ids)}` new identities are proposals, globally checked against repository content and filenames, and remain unreserved. Exact prior-source bytes and Archive paths/hashes are recorded for every changed or retired existing owner. No source or Archive was changed.

## Decisions retained

- R165 retires only after existing R1415 contains positive integer Version increasing monotonically across successive Revisions, R1416 contains one unambiguous Updated At date-time, and D270 remains the field encoding owner.
- R1372 stays semantic: exactly one derived Journal Revision Updated At from the latest accepted entry; no new persisted field is proposed.
- R963 becomes proposed M275 naming/formatting authority; D284/D302 keep their physical filename domains. R1369 exact-one Epic Directory Carrier qualification is added to D353 before retirement.
- The Operator approved each registered Journal placement: D328 dedicated `.caprmedio_caprmedio/work_journal/` and D339 Implementation Content Role directory remain unchanged. D406 covers only the remaining original governed workflow/local-control NDJSON domain. No new storage or migration action is authorized.
- GOV315 retains its Logging Policy and receives the matching existing Logging Policy Subject; generic evaluation is not its primary governed Entity. D396 governs generic Carrier so streamed/network production logs are not excluded. New owner Subjects reuse existing Entities, declare genuine prerequisites, and do not infer Temporal Form from Content Role.
- GOV337 preserves all stage meanings and forward-only dependency semantics. Mermaid relation maps are illustrative consumer-ready examples, not an independent mandatory format. D388 owns explicit stage prefixes and NDJSON/TOON encoding.
- GOV752 token spellings come from its exact bound source contribution. Type admission remains R; Carrier token authority is D. Source ownership and Core/General/omitted Standard tier decisions remain independent; no tier or source-owner migration is proposed.

## Incoming-reference handoff

The complete text scan includes ignored paths: {references['summary']['occurrences']:,} occurrences across {references['summary']['consumers']:,} consumers, with {references['summary']['active_RMED_occurrences']} active RMED occurrences. Every occurrence is classified; every active RMED consumer has a complete-Claim mapping rationale. There are zero external blocking repairs.

| Timing | Consumer | Required mapping |
| --- | --- | --- |
| Before retirement | CA-E-427 | R1304 → D379; R1369 → revised D353 |
| Before retirement | Local GOV761 and GOV762 | GOV760 → D393, replacing each whole decorated target value |
| Before extraction | Core GOV-EVAL-009 | Retain GOV299; add D386 for storage/omission checks |
| Before extraction | Local GOV-EVAL-006 | Retain GOV294/GOV302; add D383/D387 for parsed Settings encoding |

These repairs are in the two permitted source owners and must be verified before dependent extraction/retirement; CA-P-962 can perform the necessary cross-owner reference slice. GOV314 retains its Type-admission relation without an unnecessary optional D link. External ENGINE561 still consumes the retained stage vocabulary; CA-M-163 still consumes retained severity semantics and already delegates Carrier encoding to D. Historical/Journal records remain exact; generated/installed and other non-RMED mentions are downstream follow-ups.

**Revision handoff:** CA-P-962 must repair GOV761/GOV762 and GOV-EVAL-006 in Local Configuration before the affected Core extraction/retirement. CA-P-963 must preserve those references, refresh the sanctioned newer Revisions, and archive each intermediate Revision it changes. It must never overwrite those newer Revisions with the CA-P-960 snapshot; use that snapshot only as the original allocation evidence.

## Verification and boundary

`CA-P-961-verification.json` records source membership/hashes, complete substantive original-text allocation, owner resolution, Archive safety, global ID availability, Subject cardinality/duplicate checks, semantic qualifier guards, admission and reference-review status. Semantic review supplies the role/Scope decisions; these checks corroborate it and do not claim automated proof of equivalence.

All writes stayed under `execution_evidence/CA-P-961-*` through `apply_patch`. No source Atom, Task/lifecycle file, selected Settings, Journal, Git state, Tool/compiler/install/runtime or generated Projection was changed. Pending Epic005 R1224/R1225/R1227 Settings, R1222 placement and source-owner decisions remain excluded. This approved boundary is not a task blocker.

Reproduce from repository root with `python3 -B {str(Path(__file__).relative_to(ROOT))}`. The script refreshes only this task's evidence through `apply_patch` and fails the verification result if the source frontier, ID availability, coverage or mapping conditions no longer hold.
'''
    save('report.md',report)
    print(json.dumps({'dispositions':len(DESIGNS),'remaining':len(candidates-set(DESIGNS)),'source_mismatches':len(failures),'verification':verification['result'],'failed_checks':[k for k,v in acceptance.items() if not v]}))

if __name__=='__main__':
    output(incoming_scan())
