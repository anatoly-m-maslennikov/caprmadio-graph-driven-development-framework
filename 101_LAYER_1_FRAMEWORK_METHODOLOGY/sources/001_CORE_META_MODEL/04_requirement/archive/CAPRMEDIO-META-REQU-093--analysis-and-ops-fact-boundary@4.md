---
cce_version: cce_1
cce_form: separation
subjects:
  declared:
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-224--analysis-and-observation-boundary
  child_of:
    - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
---
# Requirement — Separate Analysis from factual Ops records

Ops records what occurred, was measured, or was reported during enacted execution or operation, with its available provenance and context. Examples include logs, complaints, tickets, errors, execution outputs, measurements, delivery outcomes, and externally received operational reports.

An Ops record does not explain causes, justify a choice, synthesize implications, or prescribe a required outcome, method, evaluation mechanism, or delivery path.

Analysis interprets Concerns, Ops records, Requirements, Methods, Evaluation, Delivery, or Implementations. It MAY compare alternatives, investigate causes, synthesize findings, explain implications, and provide rationale for a Requirement, Method, Evaluation rule, or Delivery rule.

When one carrier mixes factual input with interpretation, the factual Ops record and interpretive Analysis are separate governed artifacts linked by explicit relations.

## Primary claim

Factual Ops records and interpretive Analysis are separate semantic contributions.
