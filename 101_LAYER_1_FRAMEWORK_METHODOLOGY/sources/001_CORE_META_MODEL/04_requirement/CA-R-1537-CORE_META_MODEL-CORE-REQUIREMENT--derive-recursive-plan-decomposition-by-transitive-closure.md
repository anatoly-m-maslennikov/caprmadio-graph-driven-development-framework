---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Recursive Decomposition"
  depends_on:
    - "Atom/Content Role: Plan/Direct Work Decomposition"
version: 5
updated_at: "2026-10-03 00:05:13 +0400"
relations: {"relates_to": ["CA-R-1536", "CA-R-1579"]}
atom_id: "CA-R-1537"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Derive Recursive Plan Decomposition by Transitive Closure

## Scope

recursive Plan work decomposition derived from direct `DECOMPOSES_INTO` Relations.

## Claim

recursive Plan work decomposition **means** the transitive closure of direct `DECOMPOSES_INTO` Relations; it **must not** be authored as a second direct relation set.

## Details
