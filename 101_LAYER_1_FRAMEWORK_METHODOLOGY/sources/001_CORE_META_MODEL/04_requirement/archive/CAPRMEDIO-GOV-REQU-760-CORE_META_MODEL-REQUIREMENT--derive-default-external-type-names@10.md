---
atom_id: CAPRMEDIO-GOV-REQU-760
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - artifact-catalog
version: 10
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-100-CORE_META_MODEL-REQUIREMENT--preserve-external-boundary-obligations
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role
---
# Derive default external Type names

**when** GOVERNANCE derives an external Type name from an internal Type, it uses `external_<internal_type_name>`. **when** the internal Type is the Content role's default, the derived name uses that registered default Type. A separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
