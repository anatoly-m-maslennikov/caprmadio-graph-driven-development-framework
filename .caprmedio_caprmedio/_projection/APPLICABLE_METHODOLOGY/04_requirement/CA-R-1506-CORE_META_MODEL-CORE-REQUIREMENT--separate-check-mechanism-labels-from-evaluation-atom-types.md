---
subjects:
  governs: "Atom/Content Role: Evaluation/Type"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Type"
version: 4
updated_at: "2026-10-02 23:35:16 +0400"
relations: {}
atom_id: "CA-R-1506"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1506-CORE_META_MODEL-CORE-REQUIREMENT--separate-check-mechanism-labels-from-evaluation-atom-types.md
  source_atom_id: CA-R-1506
  source_atom_revision: 4
  source_sha256: 8e30fc8aefaeb60d95efcfd811a82abccfae5b1a6afd2ca235480b735b22591d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate check mechanism labels from Evaluation Atom Types

## Scope

mechanism labels and admitted Type values for Evaluation Atoms.

## Claim

the mechanism labels `Test` **and** `Evaluation` **must** describe implementation mechanisms, **not** Type values under `Atom/Content Role: Evaluation/Type`. the governing Evaluation Atom **and** its realization **must not** acquire the same classification merely because their names overlap.

## Details

this distinction does **not** define another Content Role **or** close the admitted Evaluation Type domain. its separately governed Type values remain subject **to** the applicable Type authority.
