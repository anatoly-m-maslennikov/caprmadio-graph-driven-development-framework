---
subjects:
  governs: "semantics"
  depends_on:
    - "Atom/Content Role"
    - "Implementation"
    - "Action"
    - "Workflow"
    - "Actor"
    - "Journal/Record"
    - "Relation"
version: 26
updated_at: "2026-10-03 02:24:19 +0400"
relations:
  child_of:
    - CA-M-001
atom_id: "CA-R-1702"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1702-CORE_META_MODEL-CORE-REQUIREMENT--preserve-content-role-boundaries-through-caprmedio-loop.md
  source_atom_id: CA-R-1702
  source_atom_revision: 26
  source_sha256: 54db65547f750b8b31f107016f2eefa10ea27d44e36bd95e9abe0a4fe9bf3c96
  original_relations_sha256: 2f95e55e3d0a844c858c40eeab601ef29e88bfb9f5c8b9fd17a85ccd2af662a7
---
# Summary

Preserve content role boundaries through CAPRMEDIO loop

## Scope

transitions through the CAPRMEDIO loop across Content Roles.

## Claim

**every** transition through Concern, Analysis, Plan, Requirement, Method, Evaluation, Delivery, Implementation, **and** Operations produces **or** updates the meaning owned by the receiving Content Role **without** converting the source meaning into that role **or** implying completion of a later role.

**in** particular:

- Analysis owns findings, alternatives, explanation, **and** rationale;
- Plan states intended work **without** realizing it; decomposition relates independent Plan Atoms **without** merging their Claims;
- Requirement establishes model definitions, required properties, outcomes, **or** boundaries **without** selecting their Method;
- Method provides authorship, construction, **and** Implementation conventions, Evaluation checks correctness, **and** Delivery specifies Carrier contents **and** boundaries;
- Implementation materially realizes accepted Spec Claims **and** **may** contain procedural code, but does **not** prove Evaluation **or** operational success; **and**
- Operations owns specific reusable Action, Workflow, **and** Actor participation/authorization behavior under CA-R-1530; actual executions **and** their Journal Records carrying execution evidence **and** state changes are distinct from those definitions **and** from RMED Spec.

Relations carry meaning between roles while **every** related Artifact retains its own identity, authority, lifecycle, **and** owning role.

## Details
