---
atom_id: CA-R-1616
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Atom/Revision"
    - "Entity"
    - "Implementation"
    - "Journal"
    - "Projection"
    - "Relation"
version: 4
updated_at: "2026-10-03 00:55:03 +0400"
relations:
  relates_to:
    - CA-R-1470
    - CA-R-1493
    - CA-R-1494
    - CA-R-1568
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1616-PROJECT_CONFIGURATION-REQUIREMENT--define-realization-graph.md
  source_atom_id: CA-R-1616
  source_atom_revision: 4
  source_sha256: 536018ba696ebe238eecba5e03bc9a37da3efcc801f7c57e436a68800d805cc0
  original_relations_sha256: 1ef18b4680635e48eb29c93ae8f0179007f8563080857fa6273edea405820955
---
# Summary

Define Realization Graph

## Scope

Realization Graphs derived from a declared selection of existing Implementation sources and available evidence.

## Claim

Realization Graph **means** a non-authoritative Projection of Entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.

- the Projection **must** retain source traceability under CA-R-1746 **and** generation identity under CA-R-1493, using **only** the source kinds selected for the job; legacy Implementation need **not** have pre-existing RMED **or** Journal records.
- missing evidence **and** uncertain interpretations **must** be reported. observed structure **or** behavior does **not** establish intended Requirements, a passed Evaluation, **or** completeness outside the checked selection.
- the Artifact kind remains Projection, including **when** delivered as an Implementation output under CA-R-1568. views derive from its source-backed facts **without** creating another source of truth.

## Details
