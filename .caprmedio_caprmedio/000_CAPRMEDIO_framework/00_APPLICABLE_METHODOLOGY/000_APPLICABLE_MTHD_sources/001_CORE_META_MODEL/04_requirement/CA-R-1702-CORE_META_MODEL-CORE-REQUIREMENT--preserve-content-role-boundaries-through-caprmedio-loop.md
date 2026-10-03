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
