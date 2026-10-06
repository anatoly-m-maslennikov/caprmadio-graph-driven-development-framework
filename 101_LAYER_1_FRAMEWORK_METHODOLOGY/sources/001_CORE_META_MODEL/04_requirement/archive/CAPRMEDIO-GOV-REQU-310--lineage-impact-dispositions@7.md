---
subjects:
  declared:
    continuant:
      - relation-model
  prerequisite:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: cardinality
version: 7
updated_at: 2026-08-23 15:24:07
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  relates_to:
    - CAPRMEDIO-GOV-REQU-309--use-direct-typed-relation-change-set-commit-messages
---
# Classify lineage impact with four dispositions

WHEN an Atomic Artifact receives a new committed Revision, EVERY directly dependent child reached by the Impact Review MUST receive EXACTLY ONE disposition from (`compatible`, `update_required`, `replacement_required`, `uncertain`).
