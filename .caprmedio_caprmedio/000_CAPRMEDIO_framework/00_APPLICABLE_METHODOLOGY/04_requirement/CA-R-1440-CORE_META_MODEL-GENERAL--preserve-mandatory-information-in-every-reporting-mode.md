---
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode/mandatory information"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Operator"
version: 7
updated_at: "2026-10-02 22:59:46 +0400"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-R-1420"
atom_id: "CA-R-1440"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1440-CORE_META_MODEL-GENERAL--preserve-mandatory-information-in-every-reporting-mode.md
---
# Summary

Preserve mandatory information in every reporting mode

## Scope

mandatory information reported by **every** interaction reporting mode.

## Claim

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.

## Details
