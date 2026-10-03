---
subject_scopes:
  - external-boundary
version: 1
updated_at: 2026-08-17 23:57:12
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - F4F-REQUIREMENT-255-preserve-project-independence-from-upstream-seeds
    - F4F-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
---

# Isolate cohosted F4F from project-default operations

A cohosted F4F seed must live under the repository-root `.f4f/` boundary and remain outside default CAPRMEDIO discovery, validation, migration, and Projection generation unless an operation explicitly selects F4F as its target.
