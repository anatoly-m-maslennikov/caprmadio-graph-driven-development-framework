---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 8
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
---
# Append all related Journal records before the commit

## Claim checked

The Journal Doer completes every related append under one repository-scoped apply lease and returns the complete durable receipt set before the Git Doer begins commit creation.

## Test case

Start two valid apply flows for the same repository. Instrument the first flow, whose related records span multiple Journal carriers, from lease acquisition through every Journal fsync and receipt return to Git verification and lease release. Attempt to advance the second flow throughout the first flow.

## Acceptance criteria

The first flow holds one live lease from before its first Journal append through Git verification, fsyncs every related append, and gives the Git Doer exactly the complete valid receipt set. The second flow waits without appending or mutating state while that lease is held; only after release may it acquire the lease and revalidate its sealed context.

## Failure disposition

Reject the flow if Git mutation starts first, any related append is not durable, the Git Doer uses a predicted, incomplete, or different receipt set, the lease is absent or released before verification, or the second flow appends or mutates state while the first lease is held.
