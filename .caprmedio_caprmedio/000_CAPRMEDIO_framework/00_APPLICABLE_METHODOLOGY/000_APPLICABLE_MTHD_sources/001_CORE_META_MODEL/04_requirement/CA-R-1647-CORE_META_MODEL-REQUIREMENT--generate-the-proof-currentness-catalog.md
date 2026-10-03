---
subjects:
  governs: "evaluation"
  depends_on: []
version: 18
updated_at: "2026-10-03 01:31:08 +0400"
relations:
  resolution_of:
    - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
atom_id: "CA-R-1647"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Generate the proof currentness Catalog

## Scope

proof-currentness Catalogs generated from governed proof dependency frontiers and their additional invalidation conditions.

## Claim

CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.

## Details
