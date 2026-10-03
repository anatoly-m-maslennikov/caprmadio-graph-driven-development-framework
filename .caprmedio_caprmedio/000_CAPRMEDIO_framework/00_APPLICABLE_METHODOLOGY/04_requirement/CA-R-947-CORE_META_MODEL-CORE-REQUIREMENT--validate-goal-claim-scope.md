---
subjects:
  governs:
    continuant:
      - Atom/Claim/Scope
  depends_on:
    continuant:
      - "Atom/Content Role: Requirement/Type: Goal"
      - Atom/Scope
      - Atom/Claim/Scope/Scope Unit Set
      - Structural Parent Relation
      - Project
atom_id: CA-R-947
cce_version: cce_1
cce_form: obligation
version: 14
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-947-CORE_META_MODEL-CORE-REQUIREMENT--validate-goal-claim-scope.md
---
# Validate Goal Claim Scope

a Goal Atom Claim Scope Unit Set **must** **contain** **`=1`** Scope Unit that is a direct child of its Atom Scope Unit **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit.
