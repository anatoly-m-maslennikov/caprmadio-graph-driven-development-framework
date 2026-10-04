---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal/Filename"
  depends_on:
    - "Operator"
    - "Project/Scope Unit"
    - "Project"
    - "Project Name"
version: 15
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-292"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL--serialize-external-project-goal-filenames.md
---
# Summary

Serialize External Project Goal Filenames

## Scope

external Project Goal filenames.

## Claim

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.

the `<PROJECT_SCOPE>` component **must** be the exact registered Project Name.

## Details
