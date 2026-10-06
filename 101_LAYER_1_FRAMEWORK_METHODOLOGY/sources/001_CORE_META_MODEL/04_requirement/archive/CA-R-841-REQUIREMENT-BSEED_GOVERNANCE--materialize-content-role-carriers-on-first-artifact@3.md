---
atom_id: CA-R-841
subjects:
  - carrier-placement
version: 3
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-835-REQUIREMENT-BSEED_SEMANTICS--scope-artifacts-through-scope-units
    - CAPRMEDIO-GOV-REQU-736--derive-atom-classification-from-carrier-address
---
# Materialize Content-role carriers on first Artifact

A Scope Unit may contain only the subset of registered Content-role folders needed by its current Artifacts. GOVERNANCE materializes a Content-role folder and any required role-local organizational subfolder only when creating the first Artifact whose canonical carrier address requires it. An absent folder represents an empty role in that Scope Unit; Content-role folders and their organizational subfolders are carrier layout, not Scope Units or project-graph nodes.
