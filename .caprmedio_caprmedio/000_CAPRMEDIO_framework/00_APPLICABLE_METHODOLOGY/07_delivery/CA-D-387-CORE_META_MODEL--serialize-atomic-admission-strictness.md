---
subjects:
  governs: "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    - "Framework Instance Settings"
version: 9
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CA-R-1630
atom_id: "CA-D-387"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-387-CORE_META_MODEL--serialize-atomic-admission-strictness.md
---
# Summary

Serialize Atomic Admission Strictness

## Scope

an explicit atomic admission strictness selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CA-R-1630.

## Details
