---
subjects:
  governs: "Framework Instance Settings/Confidence/Necessary Information Threshold/Carrier"
  depends_on:
    - "Framework Instance Settings"
    - "Confidence Threshold"
    - "Carrier"
version: 9
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-368"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the necessary-information confidence default

## Scope

an explicit necessary-information confidence default in the Framework Instance Settings TOML Carrier.

## Claim

an explicit necessary-information confidence default **in** the Framework Instance Settings TOML Carrier **must** use the integer-percentage field `confidence.necessary_information_threshold_percent`.

## Details
