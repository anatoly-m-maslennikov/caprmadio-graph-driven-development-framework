---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-21 03:12:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
  check_of:
    - CA-D-010-DELIVERY-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--deliver-commit-change-set-script
---
# Observe a created commit without recursion

## Claim checked

The `post-commit` Evaluation observes the completed Git boundary and records reconstructible runtime evidence without starting another governed action.

## Test case

Create one valid governed commit and one ordinary non-governed commit while the installed Git Hooks are registered. Inspect the post-commit result and runtime observation log after each commit.

## Acceptance criteria

Each commit produces exactly one runtime observation naming its commit identity, parent, changed paths, governed-boundary classification, and validation result. A governed observation verifies the singular subject, related Journal sidecars, and deterministic message. No Atom, Journal, index entry, ref beyond the original commit, trigger handoff, or recursive commit is created.

## Failure disposition

Reject the delivery if completion is not observable, invalid governed content is reported as valid, governed source is mutated, or observation starts recursive Hook or auto-commit work.
