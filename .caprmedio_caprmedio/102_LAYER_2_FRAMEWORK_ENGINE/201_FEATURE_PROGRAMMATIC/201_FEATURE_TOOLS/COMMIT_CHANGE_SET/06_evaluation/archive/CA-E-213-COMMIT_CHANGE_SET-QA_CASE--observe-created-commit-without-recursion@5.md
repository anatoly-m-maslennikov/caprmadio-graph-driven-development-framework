---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-812

---
# Observe created commit without recursion

## Claim checked

Completion observation records reconstructible runtime evidence for real-change and Journal-only commits without creating another action or commit.

## Test case

Create one valid real-change commit and one later Journal-only batch while installed observation hooks are registered. Inspect the observation log and outbox/reconciliation state after each commit.

## Acceptance criteria

Each commit produces one idempotent runtime observation naming its commit identity, parent, changed paths, commit class, and validation result. The real-change observation validates its sealed target and Initiative message; the Journal-only observation validates its selected Journal carrier set and batch form. No Atom, Journal record, index entry, ref beyond the original commit, trigger, or recursive commit is created.

## Failure disposition

Reject the delivery if completion is not observable, invalid content is reported valid, observation mutates governed source, or observation starts recursive work.
