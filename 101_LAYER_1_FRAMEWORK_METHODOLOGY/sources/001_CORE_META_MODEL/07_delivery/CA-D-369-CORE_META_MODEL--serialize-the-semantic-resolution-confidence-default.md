---
subjects:
  governs: "Framework Instance Settings/Confidence/Semantic Resolution Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
version: 8
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-369"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the semantic-resolution confidence default

## Scope

an explicit semantic-resolution confidence default in the Framework Instance Settings TOML Carrier.

## Claim

an explicit semantic-resolution confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.semantic_resolution_threshold_percent`.

## Details
