---
atom_id: CA-E-227
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-803
  check_of:
    - CA-D-007
---
# Reconcile a missed session change at Stop

## Claim checked

The Codex adapter can recover one eligible uncommitted governed change missed by immediate Tool Hooks without adopting pre-existing or concurrently committed work.

## Test case

Capture one `SessionStart` baseline, change one active Atom without a matching `PostToolUse`, and invoke `Stop`; repeat with no baseline, with a carrier already committed after the baseline, and with ambiguous concurrent dirty ownership.

## Acceptance criteria

The first Stop invocation emits one stable trigger with the current Codex session provenance and passes it through the normal commit flow. The already committed carrier is ignored. Missing-baseline and ambiguous-ownership fixtures return stable diagnostics without Journal, index, commit, or governed-file mutation. A successful immediate or reconciled commit refreshes or retires the session baseline so a later Stop does not duplicate it.

## Failure disposition

Reject the adapter if it misses or duplicates the attributable change, adopts an existing dirty carrier, attributes another task's work to the current task, or bypasses the normal trigger and commit flow.
