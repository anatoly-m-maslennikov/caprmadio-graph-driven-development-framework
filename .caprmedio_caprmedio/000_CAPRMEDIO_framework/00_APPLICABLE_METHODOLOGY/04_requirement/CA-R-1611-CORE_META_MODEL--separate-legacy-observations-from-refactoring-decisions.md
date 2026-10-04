---
atom_id: CA-R-1611
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation"
  depends_on:
    - "Analysis"
    - "Atom/Claim"
    - "Evaluation"
    - "Evidence"
    - "Projection"
version: 4
updated_at: "2026-10-03 00:55:03 +0400"
relations:
  relates_to:
    - CA-R-1470
    - CA-R-1687
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1611-CORE_META_MODEL--separate-legacy-observations-from-refactoring-decisions.md
---
# Summary

Separate legacy observations from refactoring decisions

## Scope

Reverse-engineering results, including observed Implementation facts and proposed decisions about the intended refactored result.

## Claim

reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.

- behavior **or** constraints proposed for preservation **must** be identified as proposed decisions.
- behavior **or** constraints proposed for change **must** be identified as proposed decisions.
- unresolved behavior, missing evidence, **and** uncertain interpretations **must** remain explicit.

an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. supporting evidence **must** remain recoverable **without** a proposed disposition **or** uncertainty being presented as an observed fact.

## Details
