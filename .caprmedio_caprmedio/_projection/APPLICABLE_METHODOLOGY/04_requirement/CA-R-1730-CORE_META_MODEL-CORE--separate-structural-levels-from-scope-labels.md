---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Structural Level"
    - "Structural Parent Relation"
    - "Scope Unit/Label"
    - "Operator"
    - "Project Structure"
version: 19
updated_at: "2026-10-03 02:39:08 +0400"
relations:
  child_of:
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
    - CA-R-1776
atom_id: "CA-R-1730"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1730-CORE_META_MODEL-CORE--separate-structural-levels-from-scope-labels.md
  source_atom_id: CA-R-1730
  source_atom_revision: 19
  source_sha256: 6c4009bc43c8046065bd5a87cae55a3ed0ccb17af98c27a0d3371689a9f8cc3a
  original_relations_sha256: 02c44ffab5879f586ba20d0b697b30c3f316b274fe3e1c202318d46502c49370
---
# Summary

Separate structural levels from scope labels

## Scope

Structural Levels **and** Scope Unit Labels.

## Claim

Structural Level **must** follow declared Scope Unit parentage; a retained level number **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's Structural Level, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.

## Details
