---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
version: 5
updated_at: "2026-10-03 00:05:13 +0400"
relations: {"relates_to": ["CA-R-1576", "CA-R-1579", "CA-R-1590"]}
atom_id: "CA-R-1536"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Restrict Direct Plan Decomposition

## Scope

direct `DECOMPOSES_INTO` relations between Plan Atoms.

## Claim

`DECOMPOSES_INTO` **must** connect **only** distinct Plan Atoms; **any** Plan **may** decompose into other Plans regardless of their Labels, **without** requiring incoming decomposition.

## Details
