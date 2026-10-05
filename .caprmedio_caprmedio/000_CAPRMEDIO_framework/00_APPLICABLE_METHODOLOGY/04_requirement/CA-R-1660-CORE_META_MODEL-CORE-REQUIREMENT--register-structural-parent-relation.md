---
subjects:
  governs: "Structural Parent Relation"
  depends_on:
    - "Scope Unit"
    - "Project Structure"
    - "Structural Entity"
version: 17
updated_at: "2026-10-03 01:43:51 +0400"
relations: {}
atom_id: "CA-R-1660"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1660-CORE_META_MODEL-CORE-REQUIREMENT--register-structural-parent-relation.md
  source_atom_id: CA-R-1660
  source_atom_revision: 17
  source_sha256: 5f00f0344054fb15433df0c28b1bd593fc263b3d1783a3e9cf783b480ad05bc1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register structural parent relation

## Scope

the Structural Parent Relation directed from a child to its immediate parent.

## Claim

the Structural Parent Relation **must** be the kind-independent Structural ownership relation directed from a child **to** its immediate parent. Project Structure owns Scope Unit parent declarations; structural graph views derive the corresponding `structural_parent` edge **without** maintaining a second source. a Carrier's physical containment **must not** silently replace a declared logical parent.

## Details
