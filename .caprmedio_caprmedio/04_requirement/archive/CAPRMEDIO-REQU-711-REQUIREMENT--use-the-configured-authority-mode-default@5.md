---
atom_id: CAPRMEDIO-REQU-711
subject_scopes:
  - requirement-topology
version: 5
updated_at: "2026-09-09 23:04:14 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  depends_on:
    - CA-R-1430
  replacement_of:
    - CAPRMEDIO-REQU-624--use-casual-authority-for-other-project-scopes
  child_of:
    - CAPRMEDIO-REQU-029-CORE-REQUIREMENT--govern-each-scope-by-authority-mode
    - CAPRMEDIO-REQU-622-CORE-REQUIREMENT--keep-selected-settings-in-their-authoritative-settings-artifact
---
# Use the configured Authority Mode default

a caprmedio Scope Unit **without** an explicit Authority Mode override **must** use the default selected in Framework Instance Settings **without** independently maintaining that selected value in a Project Atom.
