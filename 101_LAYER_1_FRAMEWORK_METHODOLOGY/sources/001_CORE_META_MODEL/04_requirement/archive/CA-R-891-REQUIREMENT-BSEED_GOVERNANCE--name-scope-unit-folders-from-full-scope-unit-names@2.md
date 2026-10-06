---
subject_scopes:
  - carrier-placement
tier: core
version: 2
updated_at: 2026-08-22 02:36:07
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CA-R-858
    - CA-D-003
---
# Name Scope Unit folders from full Scope Unit names

Whenever a Scope Unit is represented by a directory beneath a declared authority or Delivery root, the directory basename must equal the Unit's registered full name unchanged. Structural kind, level, coordinate, `local_order`, presentation order, and filename `scope_path` short name must not be encoded in that basename.

Formally, for every such Scope Unit \(u\):

\[
\operatorname{folder\_basename}(u)=\operatorname{name}(u)
\]
