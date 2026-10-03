---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Admission"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
version: 17
updated_at: "2026-10-02 21:01:00 +0400"
relations:
  child_of:
    - CA-R-933
atom_id: "CA-R-951"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Require an exact dependency before a Demand

## Scope

Consumer Scope Units with an accepted Goal.

## Claim

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.

## Details
