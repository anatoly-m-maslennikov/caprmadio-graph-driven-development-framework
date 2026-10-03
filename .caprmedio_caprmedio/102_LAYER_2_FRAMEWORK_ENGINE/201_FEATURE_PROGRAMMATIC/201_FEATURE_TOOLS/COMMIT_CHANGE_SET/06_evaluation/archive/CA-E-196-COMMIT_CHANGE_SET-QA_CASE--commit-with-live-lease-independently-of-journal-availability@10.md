---
atom_id: CA-E-196
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 10
updated_at: 2026-09-04 03:10:59 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
---
# Commit with a live lease independently of Journal availability

## Claim checked

The Git Doer may commit a governed real-change action while its Journal record is absent, pending, or already appended, but it cannot commit without the live repository lease and exact sealed action boundary.

## Test case

Invoke `COMMIT_CHANGE_SET` for one current sealed real-change action with a live matching lease while its Journal state is respectively absent, pending, and appended. Repeat with a missing, stale, released, or different-action repository lease. Then append the Journal record and commit it in a later Journal-only batch.

## Acceptance criteria

Each valid Journal-state case creates the same exact real-change commit without requiring or staging a Journal carrier. Each invalid lease produces a stable diagnostic before staging or commit creation and does not release or alter another action's lease. The later Journal record binds the real-change commit identity and its Journal-only commit contains only selected Journal carriers.

## Failure disposition

Reject the Git Doer if Journal availability gates a valid real-change commit, if it commits without the live matching lease and exact sealed target set, if it mixes a Journal carrier into the real-change commit, or if delayed Journal append or batching loses or duplicates provenance.
