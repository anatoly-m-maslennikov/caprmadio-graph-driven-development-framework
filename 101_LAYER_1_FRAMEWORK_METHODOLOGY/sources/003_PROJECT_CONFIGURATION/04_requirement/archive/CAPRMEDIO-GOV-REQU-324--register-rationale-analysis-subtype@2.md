---
subject_scopes:
  - artifact-catalog
project_settings:
  artifacts:
    enabled_subtypes:
      - analysis:rationale
version: 2
updated_at: 2026-08-18 20:19:17
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Register the Rationale Analysis subtype

GOV registers `rationale` as a direct subtype of the internal `analysis` Atom Type.

A Rationale Atom owns one primary explanatory conclusion that justifies one or more Requirement, Method, Evaluation, or Delivery Atoms. It may preserve material decision grounds, alternatives, trade-offs, implications, and reasons for selecting or rejecting an option.

A Rationale Atom cannot establish or modify normative specification. If an explanation changes an obligation, boundary, selected method, evaluation condition, delivery rule, or acceptance meaning, the applicable specification Atom must be created or replaced directly.

Rationale remains optional. Writers must not create an empty or ceremonial Rationale Atom merely to satisfy a template, and sub-subtypes are forbidden.
