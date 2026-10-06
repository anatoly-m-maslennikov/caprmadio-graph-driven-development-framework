---
cce_version: cce_1
cce_form: evaluation
artifact_subtype: qa_case
subjects:
  - evaluation
version: 4
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-033--generated-only-provenance-test-case
  check_of:
    - CA-M-135
  child_of:
    - CA-R-1054
---
# Generated-only provenance boundary

## Claim checked

Every commit retains auditable provenance, while only commits containing a non-generated governed change contribute Implementation relations and coverage.

## Applicable conditions

1. Validate required provenance on substantive, generated-only, and mixed commits.
2. Include substantive and mixed commits in derived implementation relations and coverage.
3. Exclude generated-only commits from those relations and coverage.
4. Confirm generated-only commits remain visible in Git audit history.
5. Reject a generated carrier that cites itself as its semantic input.

## Acceptance criteria

All commits retain auditable provenance, while only commits with at least one non-generated governed change contribute implementation edges.

## Failure disposition

Reject the derived relation or coverage result and record a Concern naming the misclassified commit.
