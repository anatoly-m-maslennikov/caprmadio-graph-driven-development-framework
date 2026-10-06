---
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: cardinality
version: 9
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1054
  relates_to:
    - CAPRMEDIO-GOV-REQU-309--use-direct-typed-relation-change-set-commit-messages
---
# Classify lineage impact with four dispositions

**when** an Atomic Artifact receives a new committed Revision, **every** directly dependent child reached by the Impact Review **must** receive **`=1`** disposition from (`compatible`, `update_required`, `replacement_required`, `uncertain`).
