---
subjects:
  governs: "Atom/Scope"
  depends_on:
    - "Atom/Revision/Author"
    - "Scope Unit/Scope"
    - "Operator"
    - "Atom/Governed Subject"
    - "Atom/Claim"
version: 18
updated_at: "2026-10-02 21:09:50 +0400"
relations:
  child_of:
    - CA-R-1596
atom_id: "CA-R-1014"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1014-CORE_META_MODEL-CORE-REQUIREMENT--resolve-atom-scope-contextually.md
  source_atom_id: CA-R-1014
  source_atom_revision: 18
  source_sha256: 57013a4e165d493701cb180a4cc32df85c8aa79373b2ec503e3b4e5dd1c4352e
  original_relations_sha256: bb6e7449127f6a7b5fd2adfab279201f33fd1e44c746e3974b29f5c557c9b581
---
# Summary

Resolve Atom Scope Contextually

## Scope

Atom Scope.

## Claim

an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.

## Details
