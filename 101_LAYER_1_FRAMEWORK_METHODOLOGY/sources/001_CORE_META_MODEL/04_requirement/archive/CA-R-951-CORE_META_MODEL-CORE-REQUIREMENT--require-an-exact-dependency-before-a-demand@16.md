---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Admission"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
version: 16
updated_at: 2026-09-06 01:45:12 +0400
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
type: "Requirement"
global_tier: 9
---
# Require an exact dependency before a Demand

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.
