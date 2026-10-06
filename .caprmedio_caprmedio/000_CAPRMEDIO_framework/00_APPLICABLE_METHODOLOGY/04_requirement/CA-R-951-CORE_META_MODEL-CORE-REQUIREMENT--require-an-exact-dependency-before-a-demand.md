---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Admission"
  depends_on:
    - "Consumer/Goal"
    - "Producer/Result"
version: 17
updated_at: "2026-10-02 21:01:00 +0400"
relations:
  child_of:
    - CA-R-933
atom_id: "CA-R-951"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-951-CORE_META_MODEL-CORE-REQUIREMENT--require-an-exact-dependency-before-a-demand.md
  source_atom_id: CA-R-951
  source_atom_revision: 17
  source_sha256: 6162c2771fd120c086a7ef053f0ade2e1ba313158cf2e2345e88c9a3205cb5d7
  original_relations_sha256: 5463f7bebc49570104b47556da8a5785c8b62028d2d02be2df820f960444ce29
---
# Summary
Require an exact dependency before a Demand

## Scope

Consumer Scope Units with an accepted Goal.

## Claim

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.

## Details
