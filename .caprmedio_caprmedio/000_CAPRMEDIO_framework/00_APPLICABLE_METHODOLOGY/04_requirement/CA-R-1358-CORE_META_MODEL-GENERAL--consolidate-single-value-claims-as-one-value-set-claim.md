---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom/Scope"
    - "Atom/Claim"
    - "Claim Value Set"
    - "Property"
    - "IS_ALLOWED_VALUE_OF"
version: 13
updated_at: "2026-10-02 22:23:29 +0400"
relations:
  child_of:
    - CA-R-918
    - CA-R-1596
atom_id: "CA-R-1358"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1358-CORE_META_MODEL-GENERAL--consolidate-single-value-claims-as-one-value-set-claim.md
  source_atom_id: CA-R-1358
  source_atom_revision: 13
  source_sha256: b75db4adf78238bff327cee6eb85f75983a6b407e56f4f3298be6136a478e407
  original_relations_sha256: 76c3beb05ab71c7f3fb555e25cf340c6946d6ed275fb430f9bb136e49c7be086
---
# Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.

## Details
