---
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
version: 9
updated_at: 2026-08-29 04:33:13 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-094--mechanism-neutral-evaluation-atoms
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CA-R-1054
  replacement_of:
    - CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes
---
# Register Type Values for Evaluation Atoms

GOVERNANCE registers QA Case with Carrier token `qa_case` **and** Evaluation Control with Carrier token `evaluation_control` as internal values of `Atom/Content Role: Evaluation/Type`.
