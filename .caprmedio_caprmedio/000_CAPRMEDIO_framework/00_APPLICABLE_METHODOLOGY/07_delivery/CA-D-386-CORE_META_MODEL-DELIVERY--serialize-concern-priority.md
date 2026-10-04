---
subjects:
  governs: "Atom/Carrier"
  depends_on:
    - "Atom/Content Role"
    - "Priority"
    - "Atom/Content Role: Plan/Type: Plan"
version: 8
updated_at: "2026-10-01 21:24:33 +0400"
relations: {}
atom_id: "CA-D-386"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-386-CORE_META_MODEL-DELIVERY--serialize-concern-priority.md
---
# Summary

Serialize Concern Priority

## Scope

Concern Atom Carriers and non-Concern Content Role Atom Carriers.

## Claim

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

## Details
