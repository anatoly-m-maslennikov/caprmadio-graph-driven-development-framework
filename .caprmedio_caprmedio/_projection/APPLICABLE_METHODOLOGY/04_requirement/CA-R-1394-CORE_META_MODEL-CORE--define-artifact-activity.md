---
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
    - "Property"
    - "Artifact/Activity: Active"
    - "Artifact/Activity: Inactive"
version: 10
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-R-1394"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1394-CORE_META_MODEL-CORE--define-artifact-activity.md
  source_atom_id: CA-R-1394
  source_atom_revision: 10
  source_sha256: 528cdcbdcdfbb450b6b263b2c7cf3f7debfd56d225a553cb9553223c7569253b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Define Artifact Activity

## Scope
Artifact Activity derived from an Artifact's current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models, including absence of an applicable Status model.

## Claim

the Artifact Property Activity **means** the derived Property that classifies an Artifact as Active **or** Inactive from its current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models. absence of an applicable Status model **means** absence of Activity, **not** Activity Inactive.

## Details
