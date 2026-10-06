---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    - "Framework Instance Settings"
version: 8
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CAPRMEDIO-GOV-REQU-302
atom_id: "CA-D-387"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Delivery"
global_tier: 11
---
# Serialize Atomic Admission Strictness

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CAPRMEDIO-GOV-REQU-302.
