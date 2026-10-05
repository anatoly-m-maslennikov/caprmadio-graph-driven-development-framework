---
subjects:
  governs: "Artifact/Activity"
  depends_on:
    - "Artifact"
    - "Artifact/Revision/Status"
version: 12
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1307"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models.md
  source_atom_id: CA-R-1307
  source_atom_revision: 12
  source_sha256: 89cf0cde999fac4e6c9697936637d05a39be30675f1f305caa9e029bd7154285
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Limit Artifact Activity to explicit Status models

## Scope

Artifacts to which explicitly defined Status models apply.

## Claim

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.

## Details
