---
subjects:
  governs: "Type"
  depends_on:
    - "Atom/Content Role"
    - "Carrier"
version: 8
updated_at: "2026-10-02 19:36:21 +0400"
relations:
  child_of:
    - "CA-R-1690"
    - "CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type"
    - "CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role"
atom_id: "CA-D-393"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-393-CORE_META_MODEL--derive-default-external-type-names.md
  source_atom_id: CA-D-393
  source_atom_revision: 8
  source_sha256: bba58abb3dc839f56d98f64bf521a06afb48a512f848916fa0b44f5ce6088201
  original_relations_sha256: c375887b69170c13f32aba865135981e98b39b9feef19c286ad30b14725760b2
---
# Summary

Derive default external Type names

## Scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.

## Details
