---
version: 14
updated_at: "2026-10-02 20:03:51 +0400"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-R-1559","CA-R-1591","CA-R-1552","CA-R-1080"]}
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "Atom/Revision/Author"
    - "Operator"
    - "AI Agent"
    - "AI Agent/Confidence"
    - "Atom/Content Role: Plan/Type: Plan/Autonomous Confidence Threshold"
    - "Spec"
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Project"
atom_id: "CA-E-440"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-440-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--evaluate-governing-atom-change-approval.md
  source_atom_id: CA-E-440
  source_atom_revision: 14
  source_sha256: 04cf2c957d5cba0f777d0d9c4ecab39e816bed26bce872a9a5eae74224e10a4a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Evaluate governing Atom change approval

## Scope

Governing Atom changes.

## Claim

the governing-Atom change Evaluation **must** return `fail` **if** an Operator-authored Atom changes **without** Operator approval, an AI-authored Atom changes autonomously below the Plan confidence threshold, a permission **or** additional Operator constraint is bypassed, the Author is changed **before** resolving the approval requirement, **or** an omitted **or** unresolved Author is assumed **to** be an AI Agent. it **must** also return `fail` **if** an authorized RMED change is reported against the old unchanged baseline **or** its affected work **and** Evaluations are **not** resolved again. AI authorship **and** sufficient confidence **must not** override an explicit prohibition.

## Details
