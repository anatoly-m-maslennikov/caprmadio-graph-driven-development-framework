---
subjects:
  governs: "Relational Atom Classification Validation"
  depends_on:
    - "Relational Atom/Qualified Type"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Atom/Content Role: Requirement/Type: Demand"
    - "Atom/Content Role: Plan/Type: Plan"
version: 14
updated_at: "2026-10-02 20:03:51 +0400"
relations: {"evaluation_for": ["CA-R-923", "CA-R-924", "CA-R-1576", "CA-R-1588"]}
atom_id: "CA-E-425"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-425-CORE_META_MODEL-QA_CASE--validate-relational-atom-classifications.md
  source_atom_id: CA-E-425
  source_atom_revision: 14
  source_sha256: 85d8366aa1962ce23d5564888bff061ea929068d2872670d3ba66e58150b97d4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Relational Atom Classifications

## Scope

Relational Atom classifications.

## Claim

the Relational Atom classification Evaluation **must** enforce the qualified Types admitted by CA-R-924 **without** treating Plan Labels as Types.

- accept permitted relational Requirement/Goal, Requirement/Demand, **and** Plan/Plan cases with explicit non-default Claim targets.
- accept a current-scope Plan with decomposition **or** blocking **without** classifying it as relational merely because those Relations exist.
- change the Plan Label from Task **to** Objective **or** Epic; retain the same target-based classification.
- reject an unregistered qualified Type, an invalid relational target, **or** a Label interpreted as Type authority.

report the exact Atom, qualified Type, **and** target condition.

## Details
