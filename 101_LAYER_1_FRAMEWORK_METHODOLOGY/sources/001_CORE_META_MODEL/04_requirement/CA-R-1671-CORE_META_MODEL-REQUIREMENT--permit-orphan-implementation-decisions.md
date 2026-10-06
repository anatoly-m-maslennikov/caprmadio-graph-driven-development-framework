---
subjects:
  governs: "requirement-topology"
  depends_on: []
version: 16
updated_at: "2026-10-03 01:51:15 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness
    - "CA-R-1767"
atom_id: "CA-R-1671"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Permit orphan Implementation Decisions

## Scope

orphan permission for an active Implementation Decision in strict authority mode.

## Claim

`implementation_decision` **must** be registered as orphan-permitted, so an active Implementation Decision **may** have no parent Implementation Method even **in** strict authority mode.

## Details
