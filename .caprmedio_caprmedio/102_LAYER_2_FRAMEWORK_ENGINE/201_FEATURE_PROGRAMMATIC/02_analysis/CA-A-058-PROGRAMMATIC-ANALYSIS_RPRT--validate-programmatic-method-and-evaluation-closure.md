---
subjects:
  governs:
    continuant:
      - programmatic-policy
    occurrent:
      - validation
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  derived_from:
    - CA-A-052
    - CA-A-053
    - CA-A-055
    - CA-A-056
    - CA-A-057
---
# Validate PROGRAMMATIC Method and Evaluation closure

## Scope resolution

CA-P-074 is Done. The final CA-P-075 validation set is every active Method
and Evaluation carrier at `PROGRAMMATIC` or one of its registered descendants,
excluding `archive/`, `done/`, `canceled/`, and `drafts/`. It resolves to 264
active carriers: 48 Methods and 216 Evaluations. The adjacent candidate set is
27 drafts (8 Methods and 19 Evaluations); drafts have no stable Atom-ID segment
and are not current authority in this Task.

The 27 excluded drafts retain legacy list-shaped Subjects metadata. That does
not invalidate this active-frontier closure, but each candidate must receive
the current declared temporal-form Subjects structure before promotion. This
is a bounded draft-maintenance follow-up, not an authority claim or a reason
to assign a stable identity before acceptance.

No native Implementation carrier is in scope. `AGENTIC` and `SKILLS` are out
of scope unless a direct relation from the selected active frontier requires
them; no such relation was found.

## Policy dispositions and coverage

CA-A-053's eight policy dispositions are either accepted or explicitly
deferred with a named later owner and reliance limit. There is no unresolved
disposition in the selected active frontier without an Operator acceptance and
bounded reliance condition.

The shared `PROGRAMMATIC` surface has 11 active Methods and 20 active
Evaluations. Every active Method has at least one direct active Evaluation:
48 of 48. The final active direct-relation totals are 62 `method_for`, 308
`evaluation_for`, and 88 `derived_from` occurrences. The Method/Evaluation
coverage remains shared where it is mechanism-neutral and specialized where a
Tool, App, or MCP boundary owns the behavior, as recorded in CA-A-057.

## Carrier and lineage repair

The initial validation found 191 active legacy carriers using `subject_scopes`,
144 obsolete `artifact_subtype: qa_case` fields, and 167 Evaluation carrier
names that did not use the current canonical address grammar. All 191 were
revised without changing their Claim or direct relation meaning: Subjects use
the current declared temporal-form structure, obsolete subtype metadata is
absent, and the 167 Evaluation names are canonical. Each exact predecessor was
preserved in its local `archive/` directory before its successor was written.

The precision pass found 101 additional current-carrier defects under current
BSEED authority. It removed 65 forbidden derived `atom_id` frontmatter values,
removed the unregistered `check_of` relation from 25 Evaluations (29 target
occurrences), normalized 56 legacy long CA references in 29 carriers to their
stable Atom IDs, rebound one old external Requirement filename to its current
external carrier, removed one inactive external Method target, and rebound
CA-E-217 from a Delivery target to its applicable Method CA-M-087. Each of
these 101 exact immediate predecessors is also preserved locally.

The complete mechanical repair therefore created 292 exact predecessor archive
revisions. All revised current carriers have positive incremented versions and
current timestamps. No native code, Delivery, Requirement, or BSEED carrier
was changed by this Task.

## Final validation result

The final deterministic validator parsed all 264 active carriers as YAML and
found exactly one H1 per carrier, unique canonical `CA-M` or `CA-E` identity
segments, valid carrier-derived Scope/Tier/Type, no repeated derived
classification metadata, valid declared Subjects, and no obsolete
`subject_scopes` or `artifact_subtype` field. Every allowed direct relation has
one active unambiguous target of its registered endpoint class. It found zero
invalid target, unregistered relation-key, duplicate identity, invalid subject,
forbidden `child_of` or `tier_parent`, malformed carrier, or missing direct
Method Evaluation coverage result.

The FPF active-Method closure baseline remains non-regressed inside this Task
Scope: the selected Methods have unique filename-derived identities, valid
tiers, canonical active relation targets, no authored inverse or deferred
replacement relation, and no unregistered relation key.

`SOFTWARE` is not a current Scope Unit in authority or in either Scope Unit
Graph projection. The sole current occurrence in CA-M-110 is the literal
technical-configuration table key `tool.caprmedio.framework_engine_software`,
not a Scope Unit assertion. Historical evidence mentions are likewise not
current scope authority.

## Projection currentness

Method/Evaluation carrier metadata does not contribute a Scope Unit Graph
value, so no graph projection is affected by this repair. The selected installed
`GENERATE_PROJECT_GRAPH_STATE` generator was nevertheless run with `--apply`;
it returned `changed: false` with 18 contributions, and its immediate dry run
also returned `changed: false`. Both graph projections remain non-authoritative
working-tree snapshots and contain no `SOFTWARE` Scope Unit.

The selected installed generator still has an older BSEED materialization map
than the canonical source generator. That installed-release update is outside
this Task and does not affect the PROGRAMMATIC Method/Evaluation results or
the no-`SOFTWARE` graph result recorded here.

## CA-P-081 deferred Requirement boundary

CA-P-081 handed 73 current Requirement acceptance boundaries to this workstream.
Twenty now have an active Requirement-to-Method-to-Evaluation chain:
CA-R-1071 through CA-R-1075 and CA-R-1105 through CA-R-1119. The other 53 have
no active Method/Evaluation chain: CA-R-802; CA-R-863 through CA-R-870;
CA-R-1094 through CA-R-1104; CA-R-1120; CA-R-1122 through CA-R-1125;
CA-R-1127 through CA-R-1135; and CA-R-1138 through CA-R-1156.

This is a Requirement-realization boundary, not a defect in the selected active
Method/Evaluation frontier: CA-P-075 validates the active Method/Evaluation
authority and its sufficient Method coverage, and it does not invent new
Requirement-specific Methods or Evaluations. A later Requirement-realization
Task must either establish an accepted Method/Evaluation chain for each listed
Requirement or explicitly retire or bound that Requirement.

## Decision and reopening conditions

CA-P-075 is complete. Reopen it if an active PROGRAMMATIC Method or Evaluation
changes, if a relation registry or Scope Unit authority change invalidates this
validation, if the installed generator is changed in a way that affects a
selected scope value, or if a listed CA-P-081 Requirement receives a new
Method/Evaluation realization requiring this final matrix to be recomputed.
