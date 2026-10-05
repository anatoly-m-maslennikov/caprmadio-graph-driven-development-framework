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
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-387-CORE_META_MODEL--serialize-atomic-admission-strictness.md
  source_atom_id: CA-D-387
  source_atom_revision: 9
  source_sha256: bf5cc85740830e28421b31913823bcdcff18c4a5ee7b47590c4b39d0a3137083
  original_relations_sha256: 4f8fca2057373dee7e1934385c6ad655c38a428a7dc3d670e9844c9f996ddbfb
---
# Summary

Serialize Atomic Admission Strictness

## Scope

an explicit atomic admission strictness selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit atomic admission strictness selection **in** the Framework Instance Settings TOML Carrier **must** use `creation_strictness` **in** `[artifacts]`, using the allowed values governed by CA-R-1630.

## Details
