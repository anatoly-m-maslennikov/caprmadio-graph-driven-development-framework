---
subjects:
  governs: "Confidence Threshold/resolution validation"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Confidence Threshold"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "Hub Atom"
    - "Framework Instance Settings"
    - "Property"
    - "Concern"
    - "Carrier"
version: 10
updated_at: "2026-10-01 21:31:46 +0400"
relations: {"evaluation_for":["CA-R-1587","CA-R-1044","CA-R-1045","CA-R-1427","CA-R-1428","CA-M-271","CA-R-1591","CA-D-472","CA-D-485","CA-R-1713"]}
atom_id: "CA-E-443"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-443-CORE_META_MODEL-QA_CASE--validate-confidence-threshold-precedence-and-inheritance.md
  source_atom_id: CA-E-443
  source_atom_revision: 10
  source_sha256: 46d0dd92027080aced49be321e800f842bb2f5e4a3d42262910b82399e3ef970
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate confidence-threshold precedence **and** inheritance

## Scope

the confidence-threshold Evaluation.

## Claim

the confidence-threshold Evaluation **must** preserve CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence precedence **and** CA-R-1591-CORE_META_MODEL-GENERAL-REQUIREMENT--apply-autonomous-confidence-thresholds-to-plan-execution authorization gates.

- supply distinct valid values through Operator input, a Plan, nested Hubs, **and** Framework Instance Settings; omit sources successively **and** confirm nearest explicit source selection.
- scope direct input **to** one execution; retain the unrelated execution's setting.
- omit the inner Hub's optional confidence override while retaining its mandatory file **and** a retry override: inherit confidence **without** copying it. reject a missing mandatory file.
- supply a Hub file with explicit values: require the same Atom identity as its folder **and** its DoD; reject a separate Objective, `epic_overrides`, **or** a nearby unrelated file as an inherited source.
- use a current Plan Revision **without** taking values from its Archived copies; reject an ambiguous Bundle **or** invalid reached source **without** silent fallback.
- preserve an explicit override equal **to** the inherited value **after** the upstream source changes; an omitted override follows that change.
- accept permitted integer values including **`=0`**, **`=87`**, **`=99`**, **and** **`=100`**; reject out-of-range, non-integer, missing effective, **or** ambiguous values.
- confidence below the effective value requests Operator disposition; equal **or** greater confidence grants no additional authority.

report the selected source, context, expected value, **and** failed condition **without** mutating source values.

## Details
