---
atom_id: CA-R-1617
content_role: Requirement
type: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Relation Derivation Class"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Relation"
version: 2
updated_at: "2026-09-23 21:40:21 +0000"
relations:
  relates_to:
    - CA-R-1616
    - CAPRMEDIO-META-REQU-097
---
# Summary

Define Relation Derivation Class

## Claim

Relation Derivation Class **means** a classification of how a represented Realization Graph Relation is supported by source declarations, deterministic resolution, possible inference, **or** recorded observation.

it classifies the derivation evidence, **not** the Relation's validity **or** governing authority. multiple supported classes **may** apply **to** the same Relation; their evidence boundaries remain distinguishable.
