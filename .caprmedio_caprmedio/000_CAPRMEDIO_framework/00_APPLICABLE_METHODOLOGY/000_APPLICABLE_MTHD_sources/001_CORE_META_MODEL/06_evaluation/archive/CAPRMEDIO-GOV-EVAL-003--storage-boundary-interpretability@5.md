---
cce_version: cce_1
cce_form: evaluation
artifact_subtype: qa_case
subjects:
  declared:
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-018--runtime-boundary-interpretability
  check_of:
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
  child_of:
    - CA-R-1054
---
# Storage-boundary interpretability

## Claim checked

An operator can place an Atom, Journal record, resumable checkpoint, generated cache, and disposable workspace in the governed storage boundary and explain its retention behavior.

## Applicable conditions

The available boundaries are `.caprmedio`, `.caprmedio_runtime`, and the host temporary root. Governed Journals are located inside `.caprmedio` by scope and Content role.

## Acceptance criteria

At least 90% of classifications are correct and no classification treats runtime or scratch as canonical truth.

## Failure disposition

Record a Concern for every ambiguous boundary and stop storage-boundary readiness until the governing rule or its presentation is corrected.
