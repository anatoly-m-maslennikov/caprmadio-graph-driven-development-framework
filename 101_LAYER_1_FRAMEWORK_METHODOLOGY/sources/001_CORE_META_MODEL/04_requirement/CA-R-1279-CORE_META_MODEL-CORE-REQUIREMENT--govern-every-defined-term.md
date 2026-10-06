---
subjects:
  governs: "GOVERNS"
  depends_on:
    - "Definition Atom"
    - "Subject"
    - "Term"
    - "Subject Path"
    - "Atom/Claim"
version: 12
updated_at: "2026-10-02 21:45:33 +0400"
relations: {}
atom_id: "CA-R-1279"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

**every** Definition Atom **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by its Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim establishes that Term's meaning; the other Term components **in** the path are references **to** their own definitions, **not** additional definitions supplied by this Atom.

## Details
