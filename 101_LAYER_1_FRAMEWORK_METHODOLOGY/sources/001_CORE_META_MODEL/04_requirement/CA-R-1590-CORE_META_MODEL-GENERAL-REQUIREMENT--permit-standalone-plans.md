---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Claim"
    - "Atom/Carrier"
version: 4
updated_at: "2026-10-03 00:47:18 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1579"]}
atom_id: "CA-R-1590"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Permit standalone Plans

## Scope

Plan Atoms.

## Claim

a Plan Atom **may** exist **without** an incoming `DECOMPOSES_INTO` Relation; its Label **must not** require a containing Plan.

## Details
