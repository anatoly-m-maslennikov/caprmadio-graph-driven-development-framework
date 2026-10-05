---
subjects:
  governs: "Confidence Threshold/source"
  depends_on:
    - "Confidence Threshold"
    - "Operator"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Hub Atom"
    - "Property"
    - "Framework Instance Settings"
version: 9
updated_at: "2026-10-02 22:59:46 +0400"
relations:
  child_of:
    - "CA-R-1427"
atom_id: "CA-R-1428"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1428-CORE_META_MODEL-GENERAL--permit-confidence-threshold-defaults-and-overrides.md
  source_atom_id: CA-R-1428
  source_atom_revision: 9
  source_sha256: 8bf145b5175d143954ac403bb11247fc8d2a74168881ed607260b1fb66c2c075
  original_relations_sha256: b9ddd5f70b093dcd4d45ab17e845ea6ec539b7ffb12ebf514ff45f075ec5936d
---
# Summary

Permit confidence-threshold defaults and overrides

## Scope

the source of a Confidence Threshold value.

## Claim

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Hub chain follows `IS_DECOMPOSITION_OF`, **not** Label spelling.

## Details
