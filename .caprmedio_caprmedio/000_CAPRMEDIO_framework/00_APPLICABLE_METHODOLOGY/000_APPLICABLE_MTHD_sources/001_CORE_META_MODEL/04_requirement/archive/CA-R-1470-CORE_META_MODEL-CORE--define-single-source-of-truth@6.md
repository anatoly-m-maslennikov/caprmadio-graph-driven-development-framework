---
subjects:
  governs: "Single Source of Truth"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Project Structure"
    - "Structural Entity"
    - "Journal"
    - "Projection"
version: 6
updated_at: "2026-10-02 23:17:53 +0400"
relations: {}
atom_id: "CA-R-1470"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Single Source of Truth

## Scope

the authority of independently maintained facts.

## Claim

Single Source of Truth **means** **`=1`** canonical authoritative source for **every** independently maintained fact **in** the same applicable context. another representation of that fact references **or** derives from its source **without** becoming an independently maintained authority.

source authority is assigned per fact under the governing model: Atoms carry governing Claims **and** their declared source Relations; Project Structure owns declared Scope Unit facts; Structural Entity Carriers supply materialization observations; Journals preserve recorded historical facts. other admitted sources retain their declared authority. this does **not** require **all** facts **to** reside **in** **`=1`** Atom, file, **or** Artifact. a derived result **may** use multiple authoritative input facts **without** creating another authoritative source for those facts.

## Details
