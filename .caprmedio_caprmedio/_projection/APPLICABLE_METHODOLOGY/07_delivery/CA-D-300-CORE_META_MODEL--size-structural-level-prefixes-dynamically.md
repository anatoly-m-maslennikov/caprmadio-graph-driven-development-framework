---
subjects:
  governs: "Directory Carrier/Numeric Prefix"
  depends_on:
    - "Scope Unit"
    - "Structural Level"
    - "Navigational Order Number"
version: 14
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-300"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-300-CORE_META_MODEL--size-structural-level-prefixes-dynamically.md
  source_atom_id: CA-D-300
  source_atom_revision: 14
  source_sha256: c70f6b177a74db94c3905cc2386bcf2bed99557d421aa974404fae91c7669819
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Size Structural Level Prefixes Dynamically

## Scope

Project-internal numeric Scope Unit Directory Carrier prefixes that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal numeric Scope Unit Directory Carrier prefix **must** concatenate these components **without** a separator:

- the Structural Level, using the decimal digit count of the greatest current Project Structural Level as its width.
- the Navigational Order Number, using the decimal rendering governed by CA-D-380-CORE_META_MODEL-DELIVERY--serialize-navigational-order-numbers.

the total prefix width is the sum of those component widths, **not** a fixed limit on the Navigational Order Number. decoding consumes the Structural Level width first **and** treats the remaining digits as the Navigational Order Number. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
