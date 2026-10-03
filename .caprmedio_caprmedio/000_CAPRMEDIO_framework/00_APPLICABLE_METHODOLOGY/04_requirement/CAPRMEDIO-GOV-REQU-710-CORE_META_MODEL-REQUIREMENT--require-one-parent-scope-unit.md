---
atom_id: CAPRMEDIO-GOV-REQU-710
subjects:
  governs:
    continuant:
      - scope-topology
  depends_on:
    continuant:
      - authority
cce_version: cce_1
cce_form: cardinality
version: 9
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-710-CORE_META_MODEL-REQUIREMENT--require-one-parent-scope-unit.md
---
# Require one parent Scope Unit

**every** Scope Unit except a Scope Unit root **must** have **`=1`** direct parent Scope Unit.
