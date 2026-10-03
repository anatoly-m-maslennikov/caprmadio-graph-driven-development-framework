---
subject_scopes:
  - artifact-catalog
version: 4
updated_at: 2026-08-22 01:56:15
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-100--preserve-external-and-relational-boundary-obligations
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role
---
# Derive default external Type names

When GOVERNANCE derives an external Type name from an internal Type, it uses `external_<internal_type_name>`. When the internal Type is the Content role's default, the derived name uses that registered default Type. A separately registered explicit external Type name is non-default and does not modify this derivation rule.
