---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 13
updated_at: "2026-10-02 21:16:45 +0400"
relations: {}
atom_id: "CA-R-1030"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1030-CORE_META_MODEL-GENERAL--prohibit-silent-non-compatible-impact-dispositions.md
---
# Prohibit silent non-compatible Impact dispositions

## Scope

the selection of non-compatible Impact dispositions.

## Claim

TOOLING **must not** select `update_required`, `replacement_required`, **or** `uncertain` **without** an explicit governed disposition.

## Details
