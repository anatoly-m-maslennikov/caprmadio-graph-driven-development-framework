---
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact/Revision"
version: 5
updated_at: "2026-09-30 13:09:08 +0000"
relations: {"child_of":["CA-R-1746"]}
atom_id: "CA-R-1494"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary
Record Projection dependency provenance **only** **when** required

## Scope
Projections.

## Claim
a Projection **must** record dependency provenance **only** **when** its registered job requires that information; no Projection is required **to** persist a blanket source frontier.

this conditional recording obligation does **not** remove source traceability required by `CA-R-1746-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form` **or** a more specific admitted Projection specification.

## Details
