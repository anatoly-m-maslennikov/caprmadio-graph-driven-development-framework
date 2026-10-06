---
subjects:
  governs: "requirement-topology"
  depends_on: []
version: 16
updated_at: "2026-10-03 01:51:15 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-030-REQUIREMENT--require-complete-authority-topology-in-strict-mode
    - "CA-R-1767"
atom_id: "CA-R-1672"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Permit terminal Implementation Methods

## Scope

terminal permission for an active Implementation Method after its local Implementation Decisions are absorbed and archived.

## Claim

`implementation_method` **must** be registered as terminal-permitted, so an active Implementation Method **may** remain childless **after** its local Implementation Decisions have been losslessly absorbed **and** archived.

## Details
