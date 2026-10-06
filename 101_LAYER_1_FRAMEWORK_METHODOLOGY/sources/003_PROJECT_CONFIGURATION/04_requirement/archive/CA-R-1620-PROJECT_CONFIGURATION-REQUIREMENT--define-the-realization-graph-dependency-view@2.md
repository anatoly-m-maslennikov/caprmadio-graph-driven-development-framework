---
atom_id: CA-R-1620
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
    - "Entity"
    - "Projection"
    - "Relation"
version: 2
updated_at: "2026-09-23 21:40:21 +0000"
relations:
  relates_to:
    - CA-R-1246
    - CA-R-1494
    - CA-R-1616
    - CAPRMEDIO-META-REQU-657
---
# Summary

Define the Realization Graph dependency view

## Claim

the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- the view **must** derive from the same source-backed graph facts **without** another independently maintained dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a second universal view.
