---
subjects:
  governs: "Work Sequence Number"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Work Sequence Number"
    - "Hub Atom"
version: 17
updated_at: "2026-10-02 21:09:50 +0400"
relations:
  child_of:
    - CA-R-991
    - CA-R-992
atom_id: "CA-R-997"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-997-CORE_META_MODEL-REQUIREMENT--validate-work-sequence-numbers.md
---
# Summary

Validate Work Sequence Numbers

## Scope

supplied Work Sequence Numbers for direct Plans decomposing the same Hub or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among direct Plans decomposing the same Hub **or** sharing the same top-level Plan container.

## Details
