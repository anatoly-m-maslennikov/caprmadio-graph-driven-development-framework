---
subjects:
  governs: "Artifact/Revision/Status"
  depends_on:
    - "Action"
    - "Workflow"
    - "Step"
version: 14
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-R-1312"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1312-CORE_META_MODEL-CORE--separate-governed-transitions-from-status-values.md
  source_atom_id: CA-R-1312
  source_atom_revision: 14
  source_sha256: a125b9d20d08aeb1e96bcae739a56b73ade837a764b9688967a7458af4743ba7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Separate Governed Transitions from Status Values

## Scope
Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

## Claim
an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
