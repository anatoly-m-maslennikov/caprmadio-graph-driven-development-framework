---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
---
# Reject a commit without complete Journal receipts and a live lease

## Claim checked

The Git Doer cannot commit a governed subject change unless every related Journal record has been durably appended and proven by the complete matching receipt set and the caller still owns the live repository lease for that action.

## Test case

Invoke `COMMIT_CHANGE_SET` with one current sealed context and, in separate runs, a missing, incomplete, predicted, stale, digest-mismatched, action-mismatched, and extra unrelated Journal receipt set, and a missing, stale, released, or different-action repository lease.

## Acceptance criteria

Each invalid receipt or lease envelope produces a stable validation diagnostic before staging or committing. It creates no new Journal, index, Git, or runtime mutation and does not release or alter a lease owned by another action.

## Failure disposition

Reject the Git Doer if it reconstructs receipts or lease authority, commits without the complete exact set and live matching lease, accepts mismatched or unrelated event, carrier, or lease data, releases another action's lease, or partially mutates state.
