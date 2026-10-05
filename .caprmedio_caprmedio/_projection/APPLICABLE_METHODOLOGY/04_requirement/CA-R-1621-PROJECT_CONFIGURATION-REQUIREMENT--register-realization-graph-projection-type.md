---
atom_id: CA-R-1621
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Realization Graph"
  depends_on:
    - "Implementation"
    - "Project Configuration"
    - "Projection"
    - "Spec Content Roles"
version: 4
updated_at: "2026-10-03 01:07:45 +0400"
relations:
  relates_to:
    - CA-R-1568
    - CA-R-1616
    - CA-R-1631
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1621-PROJECT_CONFIGURATION-REQUIREMENT--register-realization-graph-projection-type.md
  source_atom_id: CA-R-1621
  source_atom_revision: 4
  source_sha256: 527037c8c22355403929e48698432f9b27c3d9c2cd659aa6e15347914bec5e91
  original_relations_sha256: 695ef58c9dabb656ca3524e218df1bd9654588850a8709ccf2f2ddf9fc283635
---
# Summary

Register Realization Graph Projection Type

## Scope

the caprmedio Project Configuration registration of the `realization_graph` Projection Type.

## Claim

the caprmedio Project Configuration **must** register `realization_graph` as a specialized non-authoritative Projection Type for understanding existing Implementation **and** supporting reverse engineering into proposed RMED.

## Details

- registration uses the accepted specialized graph specification **and** the general Projection guarantees of CORE_META_MODEL; it does **not** add this Type **to** the universal Core requirements of other Projects.
- registration **and** activation remain distinct. the configured activation follows CA-R-1631; accepting this registration does **not** activate the Projection.
- the output remains a Projection under CA-R-1746. its permitted Implementation contribution under CA-R-1568 is **not** an Atom Content Role assigned **to** the Projection.
