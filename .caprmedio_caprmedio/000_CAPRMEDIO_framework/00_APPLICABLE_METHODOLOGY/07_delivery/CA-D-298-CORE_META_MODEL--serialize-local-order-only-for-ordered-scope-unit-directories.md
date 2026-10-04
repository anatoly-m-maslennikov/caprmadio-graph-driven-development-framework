---
subjects:
  governs: "Directory Carrier/Name"
  depends_on:
    - "Scope Unit/Type: Ordered"
    - "Scope Unit/Type: Unordered"
    - "Scope Unit/Label"
    - "Local Order"
version: 11
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-298"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-298-CORE_META_MODEL--serialize-local-order-only-for-ordered-scope-unit-directories.md
---
# Summary

Serialize Local Order Only for Ordered Scope Unit Directories

## Scope

Scope Unit authority Directory Carrier Names that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
