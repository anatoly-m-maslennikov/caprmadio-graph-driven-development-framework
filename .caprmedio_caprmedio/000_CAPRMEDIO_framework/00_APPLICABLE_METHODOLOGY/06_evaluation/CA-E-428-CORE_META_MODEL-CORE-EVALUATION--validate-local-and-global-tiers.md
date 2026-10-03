---
atom_id: CA-E-428
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Atom Tier Validation
  depends_on:
    continuant:
      - Atom/Global Tier
      - Atom/Local Tier
      - Atom/Scope
      - Scope Unit
      - Project
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-428-CORE_META_MODEL-CORE-EVALUATION--validate-local-and-global-tiers.md
---
# Validate Local and Global Tiers

the Evaluation **must** reject a Project Goal whose Global Tier is not **`-1`** **or** that has a Local Tier, a Project-scoped Atom whose Principle, Core, **or** Standard Global Tier is not respectively **`0`**, **`1`**, **or** **`2`**, a non-Project Scope Unit Atom whose Core **or** Standard Global Tier does not follow the recursive parent rule, a Principle outside the Project, a Core Claim that does not apply to the full Scope of its current Scope Unit, a Standard Claim that does not apply to a proper part of that Scope, **or** a non-Project Goal that is not a Standard Atom of its direct parent Scope Unit.
