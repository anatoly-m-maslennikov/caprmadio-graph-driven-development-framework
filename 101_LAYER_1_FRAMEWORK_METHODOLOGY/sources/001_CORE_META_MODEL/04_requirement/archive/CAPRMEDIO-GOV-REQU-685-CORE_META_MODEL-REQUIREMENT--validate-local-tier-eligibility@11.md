---
atom_id: CAPRMEDIO-GOV-REQU-685
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - applicability
version: 11
updated_at: "2026-09-09 21:56:59 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-680--enable-a-local-tier-subset-for-each-structural-level
---
# Validate local tier eligibility

the resolver **must** derive a tier-classified PRMEDO Atom's local tier from its `PRINCIPLE` marker, `CORE` marker, **or** unmarked `standard` default **and** reject the Atom **when** that tier is **not** enabled for the Structural level occupied by its current Scope Unit.
