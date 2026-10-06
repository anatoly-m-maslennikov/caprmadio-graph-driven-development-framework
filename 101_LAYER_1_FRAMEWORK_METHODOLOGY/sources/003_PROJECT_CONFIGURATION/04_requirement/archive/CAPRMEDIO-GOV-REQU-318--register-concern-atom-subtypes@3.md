---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    enabled_subtypes:
      - concern:question
      - concern:problem
      - concern:risk
      - concern:opportunity
version: 3
updated_at: 2026-08-19 04:33:37
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register Concern Atom subtypes

GOV registers these direct subtypes of the internal Concern Atom Type:

- `question` records an unresolved matter whose answer may change governed
  understanding or action;
- `problem` asserts a present undesirable condition requiring disposition;
- `risk` records a possible future undesirable condition with a trigger or
  uncertainty boundary; and
- `opportunity` records an optional improvement whose expected value does not
  establish a present defect or obligation.

Defect, gap, debt, and other more specific labels remain descriptions until GOV admits them as direct subtypes; sub-subtypes are forbidden.

## Rationale

The four subtypes distinguish missing knowledge, present harm, possible future
harm, and optional value without creating separate top-level Types or deriving
artifact identity from workflow state.
