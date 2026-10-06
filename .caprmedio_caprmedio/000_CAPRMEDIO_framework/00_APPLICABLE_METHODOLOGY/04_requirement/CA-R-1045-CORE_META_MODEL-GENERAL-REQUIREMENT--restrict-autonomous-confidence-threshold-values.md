---
subjects:
  governs: "Autonomous Confidence Threshold"
version: 12
updated_at: "2026-10-02 21:26:39 +0400"
relations:
  child_of:
    - CA-R-1044
atom_id: "CA-R-1045"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1045-CORE_META_MODEL-GENERAL-REQUIREMENT--restrict-autonomous-confidence-threshold-values.md
  source_atom_id: CA-R-1045
  source_atom_revision: 12
  source_sha256: 37e8c0609ebf108d53b1e5bb586abaec260d182c2e51809a5c3fd66783497dab
  original_relations_sha256: 13ef81b108b3d3354205ae5e098e777de42cc6f66b1abab73cc7116e0774cfd6
---
# Summary

Restrict Autonomous Confidence Threshold values

## Scope

Autonomous Confidence Threshold values.

## Claim

**every** Autonomous Confidence Threshold **must** be an integer percentage **`>=0`** **and** **`<=100`**. resolve its effective value from the applicable source under CA-M-271; the methodology **must not** restrict that value **to** a closed list of preferred percentages.

## Details
