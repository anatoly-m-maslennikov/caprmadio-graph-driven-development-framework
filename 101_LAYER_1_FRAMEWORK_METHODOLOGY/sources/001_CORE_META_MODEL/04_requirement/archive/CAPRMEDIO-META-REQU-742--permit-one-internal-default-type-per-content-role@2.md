---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-21 20:51:16
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
---
# Permit one internal default Type per Content role

A Content role may register at most one default Type. Every default Type has
internal Governance origin, and the default does not prevent that role from
admitting other internal or external Types.
