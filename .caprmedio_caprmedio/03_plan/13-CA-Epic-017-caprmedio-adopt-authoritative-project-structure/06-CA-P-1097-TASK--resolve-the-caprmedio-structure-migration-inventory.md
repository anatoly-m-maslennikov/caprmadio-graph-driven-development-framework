---
atom_id: CA-P-1097
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Artifact"
    - "Atom"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
version: 2
updated_at: "2026-09-15 00:24:00 +0000"
relations:
  depends_on:
    - CA-P-1096
---
# Resolve the caprmedio structure migration inventory

the Assignee **must** resolve a complete evidence-backed inventory **and** disposition map for the caprmedio structural migration.

## Scope

the caprmedio Project; current Scope Unit declarations, recognized unit folders, Project-owned structural/Goal/path Atoms, affected methodology sources, relevant Settings, the existing structural Projection, **and** direct consumers, restricted **to** the proposed Project Structure migration.

## Definition of Done

the Task is **not** Done **if** (a current Scope Unit **or** affected source/consumer is omitted **or** a stale Projection is copied as authority **or** a concrete binding lacks provenance **or** an unresolved structural conflict is silently selected **or** a destructive/retirement action lacks an exact disposition).

## Details

read live inputs afresh. the current `.caprmedio_caprmedio/project_scope_unit_graph.projection.toml` has historical source paths **and** is a discovery aid, **not** authority. include methodology Scope Units now inside the Project, even where their physical Carrier layout differs from the logical tree; do **not** recreate retired BSEED units. distinguish genuine Scope Units from Content Role, status, Epic, runtime, administrative, **and** ordinary Implementation folders. units lacking Active Goals remain visible.

map every admitted unit to Name, parent, Type, Label, Level, Local Order **when** applicable, navigation number, authority/Implementation Folder bindings, **and** explicit mode override **when** present. distinguish explicit overrides from effective defaults. inventory Project Atoms such as CA-R-844/975 **and** CAPRMEDIO-REQU-031/705/706/707/709/712/775, Goal references, concrete D bindings, Settings compatibility copies, filesystem-discovery Tools, **and** consumers of the current Projection/old IDs.

produce per-source keep/revise/replace/retire dispositions, conflict resolutions grounded **in** Project Principles, exact source revisions, consumer coverage, change sequencing, **and** recovery evidence. proposals below 99% confidence require Operator decisions. this is inventory/disposition work **only**; do **not** change authority, folders, Settings, Tools, **or** other Plans.

execute **only** after the direct prerequisite is Done **when** one is declared. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. preserve unrelated working-tree changes **and** historical records. creating this Task authorizes no execution by itself.

inventory checkpoint (incomplete; Task remains Active): 52 unit Carrier candidates with direct active RMEDO sources were found, excluding the root Project **and** Applicable Methodology's projected copies; INSTALLED_EXTENSIONS also remains evidenced by its current Goal despite having no active local RMEDO. the legacy structural Projection omits unnumbered Tool/App units **and** is **not** promoted as authority. 34 existing Tool/App units lack declared Navigational Order Numbers **in** the active Engine authority checked:

- `ADOPT_RECONCILE`
- `APPEND_CHANGE_RECORDS`
- `ATOM_ARCHIVE`
- `ATOM_CREATE`
- `ATOM_MOVE`
- `ATOM_PROMOTE`
- `ATOM_READ`
- `ATOM_SEARCH`
- `ATOM_UPDATE`
- `ATOM_UPGRADE`
- `BULK_CHANGE`
- `CLOSE_ATOM`
- `COMMIT_CHANGE_SET`
- `COMMIT_CONTEXT`
- `COMMIT_TRIGGER`
- `COMPILE_APPLICABLE_METHODOLOGY`
- `DERIVE_CCE_CANONICAL_SIGNATURES`
- `DERIVE_SCOPE_CANONICAL_SIGNATURES`
- `DETECT_CLAIM_VALUE_SET_CANDIDATES`
- `GENERATE_ENTITY_GRAPH`
- `GENERATE_PROJECT_GRAPH_STATE`
- `GRAPH_CHECK`
- `IMPLEMENTATION_INVENTORY`
- `INSTALL_TOOLS`
- `MIGRATE_ATOM_IDENTITY`
- `PROJECTION_REBUILD`
- `REBIND_ATOM_RELATIONS`
- `REPLACE_ATOM`
- `RETRIEVE_APPLICABLE_METHODOLOGY`
- `START_BACKGROUND_SERVICES`
- `TARGET_SET`
- `AGENT_HOST_PLUGINS`
- `CODEX_PLUGIN`
- `GRAPH_APP`

the chronological default cannot be reconstructed confidently from the inspected source declarations; filesystem timestamps **and** surviving Atom update timestamps do **not** prove unit creation order. Operator decision pending: assign initial navigation numbers alphabetically within **every** affected parent, preserving existing numbered-unit values **and** current Carrier paths. no numbers were assigned, no candidate manifest was created, **and** no structural Projection was generated. the remaining source/consumer disposition inventory **and** ambiguity checks are still required **before** this Task can be Done.
