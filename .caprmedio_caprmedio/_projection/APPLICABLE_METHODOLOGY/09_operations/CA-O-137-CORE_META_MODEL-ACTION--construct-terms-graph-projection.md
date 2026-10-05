---
atom_id: CA-O-137
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Construct Terms Graph Projection"
  depends_on: ["Action", "Term", "Governed Term", "Definition Atom", "Projection/Type: Terms Graph", "Relation Kind", "Artifact/Revision", "Journal"]
version: 2
updated_at: "2026-10-04 16:51:32 +0000"
relations:
  relates_to: [CA-R-1335, CA-R-1454, CA-R-1318, CA-R-1279, CA-M-114, CA-R-1746, CA-R-1471, CA-R-1246, CA-R-806, CA-R-1472, CA-R-1437, CA-E-382, CA-R-1720, CA-R-1728]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md
  source_atom_id: CA-O-137
  source_atom_revision: 2
  source_sha256: 6c154852b99df16961fe63c8fd869dbf86f8d75ecc950b25b189e41c3c1c5dad
  original_relations_sha256: cb6c860a6ef1c4a2b657d35221abc1ac16d6c8207c2ac974f36e9b296884ef07
---
# Summary

Construct Terms Graph Projection

## Operation

Construct Terms Graph Projection **means** the Action that constructs **or** confirms the requested derived Terms Graph from its bound current Term authority **and** admitted Relation declarations. one selected graph construction is the responsibility; vocabulary admission, source correction **and** unrelated graph generation are separate responsibilities.

### Inputs and admission

require an admitted request, explicit source selection **and** any narrower/governed-only view selection, exact current source set **and** governing Term/Relation Kind authority, representation configuration, target Projection/output destination, any existing Projection with source evidence, admitted realization/permissions **and** actual Run recording context. declared selection governs required source kinds; an upstream Projection needs its identity/Revision **and** ultimate source traceability, **not** defining authority. an explicitly empty evidenced selection differs from absent **or** unreadable selection.

### Behavior

1. resolve the actual request, source/view boundaries, admitted execution kind **and** capabilities **before** effects. retain the admitted source identities/Revisions/locations; do **not** silently substitute a different frontier **or** infer definitions from spelling, capitalization, a filename **or** shared Subject use.
2. construct all **and** only selected native Terms admitted by governing authority under CA-R-1335. for a governed-only selection, reuse CA-R-1454's complete node/internal-Relation selection **and** defining-source evidence; use CA-R-1279/CA-M-114 **only** within their actual definition/derivation domains. full Subject Paths **or** referenced path components are **not** additional definitions supplied by the referring Atom. missing **or** conflicting defining authority remains an affected limitation, never an invented Term meaning.
3. resolve each Relation's graph-qualified metadata under CA-R-1246/CA-R-806 **and** its source/derivation evidence under CA-R-1437. preserve its admitted direction, endpoint classes/context **and** cardinality. external references under CA-R-1472 remain distinguishable from native Terms; an Entity edge **or** compatible endpoint does **not** become a native Terms edge. do **not** infer an internal Relation merely from labels **or** operational classification.
4. retain exact source Claim/Artifact Revision traceability through any upstream Projection chain under CA-R-1746/CA-R-1471. apply the applicable CA-E-382 checks, including declared hierarchy/Root Term authority where relevant, **without** inventing another hierarchy **or** silently importing outside-selection parents. preserve separate fidelity, graph-validity **and** coverage outcomes; a faithful representation of a source conflict is **not** a valid graph. missing, conflicting, inaccessible, unsupported **or** stale regions/checks remain visible.
5. confirm source/definition/permission currentness **before** publishing **only** to the authorized derived-output destination. return no_op **only** **when** the existing Projection demonstrably matches the exact current selection/configuration **and** satisfies required checks. missing capability **or** stale prior output is **not** no_op. an explicitly authorized limited diagnostic output retains its incomplete/invalid state; do **not** replace an accepted complete target with an unapproved partial result.
6. retain actual output effects **and** start/terminal Action evidence, plus parent Workflow/Step references **when** applicable, in the one Journal under CA-R-1720/CA-R-1728. missing recording evidence remains a recording blocker, **not** journaled completion; recover recording separately **without** blind construction replay. no secrets **or** fictitious no-op Artifact change are recorded.

### Results and effects

- built: exact produced Projection Revision, selection/configuration/source evidence **and** actual effects/recording references, **only** **when** all required checks pass, requested coverage is complete **and** all currentness/permission/recording gates are satisfied. a failed check returns conflicting **or** failed as evidenced; an unresolved check **or** recording condition returns incomplete **or** blocked, even **when** output was produced.
- no_op: the proven unchanged current Projection **and** the same all-passed, complete-coverage/currentness/permission/recording boundary as built, with no fabricated mutation.
- incomplete, conflicting, stale **or** blocked: affected source regions/checks, actual limited output/effects **if** any **and** missing evidence/permission; no complete Projection **or** complete Run claim.
- failed **or** canceled: actual outcome, partial effects, retained prior/result evidence **and** authorized recovery boundary; no automatic repair **or** retry.

## Details

only the requested derived output **and** truthful execution evidence are effects. no defining Claim, Term meaning, Relation declaration **or** other source authority is changed. current R/M/E/D remain the graph/vocabulary/representation authority; this Action defines no Tool-specific grammar, generator, database **or** forced build schedule.
