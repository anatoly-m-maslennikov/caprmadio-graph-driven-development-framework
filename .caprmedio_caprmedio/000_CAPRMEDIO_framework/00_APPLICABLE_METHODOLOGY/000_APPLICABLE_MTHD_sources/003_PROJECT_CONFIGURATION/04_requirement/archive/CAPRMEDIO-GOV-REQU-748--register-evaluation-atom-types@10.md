---
atom_id: CAPRMEDIO-GOV-REQU-748
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Evaluation/Type"
project_graph_state:
  artifacts:
    enabled_types:
      - evaluation:qa_case
      - evaluation:evaluation_control
version: 10
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-094-CORE_META_MODEL-REQUIREMENT--requirement-keep-evaluation-atoms-mechanism-neutral-and-chains-distinct
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
  replacement_of:
    - CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes
---
# Register Type Values for Evaluation Atoms

GOVERNANCE registers QA Case with Carrier token `qa_case` **and** Evaluation Control with Carrier token `evaluation_control` as internal values of `Atom/Content Role: Evaluation/Type`.
