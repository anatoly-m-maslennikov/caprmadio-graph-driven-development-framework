---
subjects:
  governs: "development-flow"
  depends_on: []
version: 21
updated_at: "2026-10-03 02:10:09 +0400"
relations:
  child_of:
    - "CA-R-1682"
    - "CA-R-1702"
atom_id: "CA-R-1691"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Requirement — Promote active backlog candidates into Atoms

## Scope

Development Backlog candidates selected into active work.

## Claim

assigning a Development Backlog candidate **to** a current **or** future version does **not** establish governed truth. the candidate becomes active work **only** **when** the operator selects it **and** CAPRMEDIO creates **`=1`** bounded Task Atom for its action. execution **then** materializes the minimum Requirement, Method, Evaluation, Delivery, **or** future Operations Atoms needed **to** govern that work.

**`=1`** backlog line **may** produce multiple Atoms. multiple closely related backlog lines **may** produce **`=1`** Concern **or** RMED Atom **only** **when** they resolve **to** **`=1`** independently replaceable claim. Analysis, Task, Implementation, **and** Operations use their separately governed atomicity models.

the backlog entry **may** link the resulting Atoms for navigation but remains a non-authoritative planning candidate **until** release finalization removes **or** reschedules it.

## Details

a Development Backlog candidate becomes active **only** through a bounded Task Atom; specification **or** other semantic authority arises **only** from the applicable CAPRMEDIO Atoms created **or** revised during execution.
