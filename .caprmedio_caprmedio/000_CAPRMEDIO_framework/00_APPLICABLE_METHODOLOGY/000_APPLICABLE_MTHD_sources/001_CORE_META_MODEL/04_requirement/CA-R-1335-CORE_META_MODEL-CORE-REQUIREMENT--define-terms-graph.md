---
subjects:
  governs: "Projection/Type: Terms Graph"
  depends_on:
    - "Projection"
    - "Term"
    - "Relation Kind"
    - "Relation"
    - "CAPRMEDIO Graph"
version: 13
updated_at: "2026-10-02 22:05:04 +0400"
relations: {}
atom_id: "CA-R-1335"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Terms Graph

## Scope

Terms Graph projections **and** their represented graph facts.

## Claim

Terms Graph **means** the Type value under Projection whose instances are derived CAPRMEDIO Graphs with native Term nodes **and** edges representing Relations admitted for that graph kind by their governing authority. their represented facts retain their appropriate source authority under CA-R-1746.

## Details

admitted external graph **or** source references under CA-R-1472 do **not** become native Term nodes merely by being referenced. those references retain their own endpoint classes **and** graph-qualified Relation authority.
