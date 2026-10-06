---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 20
updated_at: "2026-10-01 21:44:50 +0400"
relations:
  child_of:
    - CA-R-1051
atom_id: "CA-R-1676"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep RMED-to-RMED Relations within Active Authority

## Scope

direct relations authored by Active RMED Atoms that target RMED Atoms.

## Claim

**if** a direct relation is authored by an Active Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Active.

## Details
