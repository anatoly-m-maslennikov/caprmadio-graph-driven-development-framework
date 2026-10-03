---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 5
updated_at: 2026-08-20 23:55:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
  check_of:
    - CA-D-010-DELIVERY-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--deliver-commit-change-set-script
---
# Keep dry-run mutation-free

## Claim checked

`COMMIT_CHANGE_SET` dry-run returns the complete predicted commit result without changing Git or governed state.

## Test case

Snapshot governed files, runtime outputs, repository lease state, index entries, refs, and object reachability for one valid sealed `UPDATE` context, invoke the complete flow in dry-run mode, then repeat every snapshot.

## Acceptance criteria

The result names the exact identity, change set, typed upstream relations, structured sidecar record set, message Projection, predicted lease availability, and validations, while every captured state remains unchanged, no lease is acquired, and no new reachable commit exists.

## Failure disposition

Reject the Doer and report the first missing prediction or mutation.
