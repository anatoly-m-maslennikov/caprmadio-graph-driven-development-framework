---
atom_id: CA-O-134
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Construct Entities Graph Projection"
  depends_on: ["Action", "Entity", "Property", "Projection/Type: Entities Graph", "Project Structure", "Relation Kind", "Artifact/Revision", "Journal"]
version: 2
updated_at: "2026-10-04 16:51:32 +0000"
relations:
  relates_to: [CA-R-1438, CA-R-1456, CA-R-1746, CA-R-1471, CA-R-1246, CA-R-806, CA-R-1472, CA-R-1437, CA-R-1483, CA-D-440, CA-E-449, CA-R-1720, CA-R-1728]
---
# Summary

Construct Entities Graph Projection

## Operation

Construct Entities Graph Projection **means** the Action that constructs **or** confirms the requested derived Entities Graph from its bound current authoritative Entity declarations, Properties **and** admitted source facts. one selected graph construction is the responsibility; source correction, graph-model admission **and** unrelated graph generation are separate responsibilities.

### Inputs and admission

require an admitted request, explicit source selection **and** any narrower display selection, the exact current source set **and** governing source/Relation Kind authority, representation configuration, target Projection/output destination, any existing Projection with source evidence, admitted realization/permissions **and** actual Run recording context. the source set identifies all required source kinds **and** their coverage, including the authoritative Project Structure under CA-R-1483/CA-D-440 **when** declared Scope Unit facts are selected. upstream Projections need their own identity/Revision **and** ultimate source traceability, **not** independent authority. an explicitly empty evidenced selection differs from an absent **or** unreadable selection.

### Behavior

1. resolve the actual request, source/display boundaries, admitted execution kind **and** capabilities **before** effects. retain source identities, Revisions **and** exact source locations **without** silently substituting current files for the admitted frontier. do **not** infer Scope Units from folders **or** convert native declarations into invented Atoms.
2. construct all **and** only selected native Entity identities, their selected authoritative Property facts **and** admitted Relations under CA-R-1438/CA-R-1456 **and** the actual governing source declarations. declared Project Structure facts retain their non-Atom source identity/Revision; observed materialization remains separately traced, never declaration authority. preserve existing canonical/bearer-qualified identities; multiple views **or** governing Claims do **not** create duplicate identities.
3. resolve each Relation's graph-qualified metadata under CA-R-1246/CA-R-806. preserve admitted direction, qualified endpoints, context **and** cardinality; use CA-R-1472 for external references, keeping them distinguishable from native members. source **and** admitted derived Relation traceability follows CA-R-1437. no foreign-kind edge, fabricated Property value **or** inferred identity fills a gap.
4. retain exact source Claim/Artifact Revision evidence for admission **and** represented facts under CA-R-1746/CA-R-1471, including any upstream chain. apply the applicable CA-E-449 checks to the requested scope **and** preserve separate fidelity, graph-validity **and** coverage outcomes. missing, conflicting, inaccessible, unsupported **or** stale regions remain explicitly identified; an unperformed **or** unresolved check is **not** a pass.
5. confirm source/definition/permission currentness **before** publishing. publish **only** to the authorized derived-output destination. return no_op **only** **when** an existing Projection demonstrably matches the exact current selection/configuration **and** satisfies all required checks; a missing capability **or** stale prior output is **not** no_op. an explicitly authorized limited diagnostic output retains its actual incomplete/invalid state; do **not** replace an accepted complete target with an unapproved partial result.
6. retain actual output effects **and** start/terminal Action evidence, plus parent Workflow/Step references **when** applicable, in the one Journal under CA-R-1720/CA-R-1728. missing recording evidence remains a recording blocker, **not** journaled completion; recover recording separately **without** blind construction replay. do **not** expose secrets **or** invent a no-op Artifact change.

### Results and effects

- built: exact produced Projection Revision, selection/configuration/source evidence **and** actual effects/recording references, **only** **when** all required checks pass, requested coverage is complete **and** all currentness/permission/recording gates are satisfied. a failed check returns conflicting **or** failed as evidenced; an unresolved check **or** recording condition returns incomplete **or** blocked, even **when** output was produced.
- no_op: the proven unchanged current Projection **and** the same all-passed, complete-coverage/currentness/permission/recording boundary as built, with no fabricated mutation.
- incomplete, conflicting, stale **or** blocked: affected source regions/checks, actual limited output/effects **if** any, **and** the missing evidence/permission; no complete Projection **or** complete Run claim.
- failed **or** canceled: actual outcome, partial effects, retained prior/result evidence **and** the authorized recovery boundary; no automatic repair **or** retry.

## Details

only the requested derived output **and** its truthful execution evidence are effects. no governing source, Project Structure, Entity identity **or** Relation authority is changed. current R/M/E/D remain the graph/model/representation authority; this Action does **not** duplicate their definitions **or** mandate a particular generator, parser, language, database **or** build schedule.
