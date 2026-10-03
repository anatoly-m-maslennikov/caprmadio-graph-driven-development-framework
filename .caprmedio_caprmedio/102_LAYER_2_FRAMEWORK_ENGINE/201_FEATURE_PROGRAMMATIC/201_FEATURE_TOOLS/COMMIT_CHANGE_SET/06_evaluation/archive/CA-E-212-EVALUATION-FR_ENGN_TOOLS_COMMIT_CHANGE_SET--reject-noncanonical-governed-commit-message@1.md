---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-21 01:33:02
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
  check_of:
    - CA-D-010-DELIVERY-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--deliver-commit-change-set-script
---
# Reject a noncanonical governed commit message

## Claim checked

The `commit-msg` Evaluation accepts a governed commit message only when it is the exact deterministic Projection of the staged completed `governed_file_change` event and its referenced previous result.

## Test case

Stage one valid governed subject-plus-sidecars change set. Invoke `git-hook commit-msg`, first with the generated message and then with a changed source relation, action type, result, extra body line, or trailer.

## Acceptance criteria

The exact generated single-line message succeeds. Every changed or extended message returns one stable diagnostic without changing the message carrier, index, working tree, governed source, Journal, refs, or runtime state.

## Failure disposition

Reject the delivery if a noncanonical governed message passes, the canonical message fails, or Evaluation rewrites any repository carrier.
