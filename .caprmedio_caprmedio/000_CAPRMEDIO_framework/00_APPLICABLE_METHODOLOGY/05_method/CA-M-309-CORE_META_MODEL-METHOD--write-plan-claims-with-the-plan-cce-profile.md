---
subjects:
  governs: "CCE/Role Profile: Plan"
  depends_on:
    - "Atom/Content Role: Plan"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "CCE Operator"
version: 4
updated_at: "2026-10-01 21:41:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-123
    - CA-M-306
    - CA-R-1575
    - CA-R-1581
atom_id: "CA-M-309"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-309-CORE_META_MODEL-METHOD--write-plan-claims-with-the-plan-cce-profile.md
  source_atom_id: CA-M-309
  source_atom_revision: 4
  source_sha256: 0ccf013b3aa5e388853f9b0a8acd98e73180fd4d4e0028684a472f2566e46f61
  original_relations_sha256: 55738e4ef8b9a22c50eaa72508a8c36a2fd271300e142933cb6bdfa7928d3dae
---
# Summary

Write Plan Claims with the Plan CCE Profile

## Scope

Plan Claims written with the Plan CCE Role Profile.

## Claim

**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:

1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.
2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.
6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.

## Details

an action word **in** a Plan identifies intended work. it does **not** define a reusable Operations Action.
