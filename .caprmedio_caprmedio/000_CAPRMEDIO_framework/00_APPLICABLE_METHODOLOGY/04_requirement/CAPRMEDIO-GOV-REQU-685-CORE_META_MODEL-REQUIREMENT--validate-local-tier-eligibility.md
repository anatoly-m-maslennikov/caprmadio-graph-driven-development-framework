---
atom_id: CAPRMEDIO-GOV-REQU-685
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - applicability
version: 10
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-680--enable-a-local-tier-subset-for-each-structural-level
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-685-CORE_META_MODEL-REQUIREMENT--validate-local-tier-eligibility.md
---
# Validate local tier eligibility

GOVERNANCE **must** derive a tier-classified PRMEDO Atom's local tier from its `PRINCIPLE` marker, `CORE` marker, **or** unmarked `standard` default **and** reject the Atom **when** that tier is **not** enabled for the Structural level occupied by its current Scope Unit.
