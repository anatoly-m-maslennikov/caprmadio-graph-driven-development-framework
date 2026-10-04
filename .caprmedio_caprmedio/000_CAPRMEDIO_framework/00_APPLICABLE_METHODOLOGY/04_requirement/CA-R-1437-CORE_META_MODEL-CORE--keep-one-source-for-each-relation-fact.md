---
subjects:
  governs: "Relation/authority"
  depends_on:
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Single Source of Truth"
    - "Atom/Claim"
    - "Structural Entity"
    - "Journal"
version: 6
updated_at: "2026-10-02 22:59:46 +0400"
relations: {}
atom_id: "CA-R-1437"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1437-CORE_META_MODEL-CORE--keep-one-source-for-each-relation-fact.md
---
# Summary

Keep one source for each relation fact

## Scope

authoritative source declarations for Relation facts.

## Claim

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.

## Details
