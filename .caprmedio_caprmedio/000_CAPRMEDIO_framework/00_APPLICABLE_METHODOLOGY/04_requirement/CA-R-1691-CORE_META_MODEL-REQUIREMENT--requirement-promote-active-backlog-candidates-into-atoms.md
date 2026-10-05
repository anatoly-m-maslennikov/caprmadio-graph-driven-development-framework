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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1691-CORE_META_MODEL-REQUIREMENT--requirement-promote-active-backlog-candidates-into-atoms.md
  source_atom_id: CA-R-1691
  source_atom_revision: 21
  source_sha256: 4fc85bd5eb791489fef2e8df76020d75cb851f6d074fc87a8adf565b4844d561
  original_relations_sha256: e993fdf9eb607df60577f31e29a8ec9b4a45c5634135598de949b7c4c4432a61
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
