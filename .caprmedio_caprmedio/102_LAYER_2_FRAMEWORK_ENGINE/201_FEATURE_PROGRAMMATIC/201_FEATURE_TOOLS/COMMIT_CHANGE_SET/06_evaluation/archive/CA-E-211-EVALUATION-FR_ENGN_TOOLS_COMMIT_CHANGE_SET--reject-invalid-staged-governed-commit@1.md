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
# Reject an invalid staged governed commit

## Claim checked

The `pre-commit` Evaluation accepts a governed Git boundary only when the index contains exactly one governed subject change and every related Journal sidecar record for that action.

## Test case

Stage, in separate runs, an unresolved index, a whitespace-invalid change, a governed Atom without a Journal sidecar, a Journal sidecar without a governed Atom, two governed Atoms, and one valid subject-plus-sidecars change set; invoke `git-hook pre-commit` for each state.

## Acceptance criteria

Each invalid state returns one stable diagnostic before commit creation. The valid state succeeds without changing the index, working tree, governed source, Journal, refs, or runtime state.

## Failure disposition

Reject the delivery if an invalid governed boundary passes, a valid boundary fails, or Evaluation mutates repository state.
