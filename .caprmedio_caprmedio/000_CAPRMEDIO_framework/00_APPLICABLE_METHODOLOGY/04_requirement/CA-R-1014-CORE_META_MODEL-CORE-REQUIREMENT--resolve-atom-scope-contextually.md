---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Scope
  depends_on:
    continuant:
      - Scope Unit/Scope
      - Operator
      - Atom/Subjects/Subject/Entity
      - Atom/Claim/Scope
version: 11
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-919
    - CA-R-1013
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1014-CORE_META_MODEL-CORE-REQUIREMENT--resolve-atom-scope-contextually.md
---
# Resolve Atom Scope Contextually

an Atom Scope **must** include its current Scope Unit Scope **or** named Operator fallback, the Entity referenced by its **`=1`** GOVERNS Subject, **and** any explicit Scope constraints in its Claim.
