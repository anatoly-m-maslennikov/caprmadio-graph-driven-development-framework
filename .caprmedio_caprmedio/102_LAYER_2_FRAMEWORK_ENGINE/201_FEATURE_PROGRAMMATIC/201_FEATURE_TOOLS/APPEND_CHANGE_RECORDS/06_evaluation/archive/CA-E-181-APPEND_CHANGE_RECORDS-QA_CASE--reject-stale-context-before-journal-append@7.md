---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
    - CA-R-812
---
# Reject stale context before Journal append

## Claim checked

The Journal-appending Doer fails closed when the repository state no longer matches the sealed context.

## Test case

Gather one valid `UPDATE` context, advance its Git base or alter one sealed frontier digest, then invoke `APPEND_CHANGE_RECORDS` apply with the stale envelope.

## Acceptance criteria

The Doer releases any provisional unconsumed lease, returns a deterministic stale-context diagnostic before the first Journal append, and creates no Journal record, runtime blockage, index, ref, object-reachability, or governed-file change.

## Failure disposition

Reject the Doer if it appends, silently refreshes, or partially applies the stale context.
