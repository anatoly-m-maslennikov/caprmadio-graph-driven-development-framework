---
subjects:
  governs: "Subject Expression"
  depends_on:
    - "IS_ALLOWED_VALUE_OF"
    - "Property"
version: 13
updated_at: "2026-10-02 21:35:09 +0400"
relations: {}
atom_id: "CA-R-1245"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1245-CORE_META_MODEL-REQUIREMENT--qualify-allowed-values-with-colon.md
---
# Summary

Qualify Allowed Values with Colon

## Scope

IS_ALLOWED_VALUE_OF relations in a Subject Expression.

## Claim

**in** a Subject Expression, `:` **must** express **only** one IS_ALLOWED_VALUE_OF relation from the following value **to** the immediately preceding Property occurrence.

## Details
