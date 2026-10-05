---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    - "Local Order"
    - "Scope Unit/Type: Ordered"
version: 12
updated_at: "2026-10-02 21:52:05 +0400"
relations: {}
atom_id: "CA-R-1293"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1293-CORE_META_MODEL-CORE--prohibit-demands-to-later-ordered-siblings.md
  source_atom_id: CA-R-1293
  source_atom_revision: 12
  source_sha256: ca33e5cabef7bc7a7cc9071db16177c338c871dc0570f4d79b0b745031844006
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Prohibit Demands to Later Ordered Siblings

## Scope

Demand Atoms owned by Ordered Scope Units.

## Claim

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.

## Details
