---
atom_id: CA-R-1621
content_role: Requirement
type: Requirement
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
version: 2
updated_at: "2026-09-23 21:40:21 +0000"
relations:
  relates_to:
    - CA-R-1568
    - CA-R-1616
    - CAPRMEDIO-GOV-REQU-305
    - CAPRMEDIO-META-REQU-657
---
# Summary

Register Realization Graph Projection Type

## Claim

the caprmedio Project Configuration **must** register `realization_graph` as a specialized non-authoritative Projection Type for understanding existing Implementation **and** supporting reverse engineering into proposed RMED.

- registration uses the accepted specialized graph specification **and** the general Projection guarantees of CORE_META_MODEL; it does **not** add this Type **to** the universal Core requirements of other Projects.
- registration **and** activation remain distinct. the configured activation follows CAPRMEDIO-GOV-REQU-305; accepting this registration does **not** activate the Projection.
- the output remains a Projection under CAPRMEDIO-META-REQU-657. its permitted Implementation contribution under CA-R-1568 is **not** an Atom Content Role assigned **to** the Projection.
