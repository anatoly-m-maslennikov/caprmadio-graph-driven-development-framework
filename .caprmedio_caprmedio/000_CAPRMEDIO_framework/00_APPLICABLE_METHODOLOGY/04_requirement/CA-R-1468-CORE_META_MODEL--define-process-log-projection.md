---
subjects:
  governs: "Projection/Type: Process Log"
  depends_on:
    - "Step Run"
    - "Workflow Run"
    - "Projection"
    - "Journal"
    - "Journal/Record"
    - "Action"
    - "Workflow"
version: 6
updated_at: "2026-10-02 23:17:53 +0400"
relations: {}
atom_id: "CA-R-1468"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1468-CORE_META_MODEL--define-process-log-projection.md
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
