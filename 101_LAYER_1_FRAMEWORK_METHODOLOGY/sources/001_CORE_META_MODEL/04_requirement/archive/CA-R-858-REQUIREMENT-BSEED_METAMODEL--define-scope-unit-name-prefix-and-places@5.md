---
subject_scopes:
  - scope-topology
tier: core
version: 5
updated_at: 2026-08-22 04:00:55
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-834
---
# Define Scope Unit name, filename scope name, and places

Every Scope Unit has exactly one registered full `name`, exactly one filename `scope_path_name`, exactly one authority place for its governed Artifacts, and exactly one physically distinct Delivery place for its realized output. The registered full name and filename scope name are atomic, case-sensitive uppercase `SNAKE_CASE` tokens. The full name is also the Unit's directory basename wherever the Unit is represented by a directory. A non-Project Unit's filename scope name may occur as `<CURRENT_SCOPE>` or `<TARGET_SCOPE>`. The Project root omits `<CURRENT_SCOPE>` but retains its filename scope name for use as `<TARGET_SCOPE>`. The Project identity prefix is a separate identity construct.
