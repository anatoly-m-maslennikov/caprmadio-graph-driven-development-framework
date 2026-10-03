---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - commit-automation
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-25 01:49:10 +0400
relations:
  evaluation_for:
    - CA-M-182
---
# Reject an undeclared downstream transition

## Claim checked

A worker or Scheduler cannot invent downstream work outside the accepted graph.

## Test case

Return a valid worker result together with a requested step identity absent from the persisted manager-defined transitions.

## Acceptance criteria

The completion facts remain inspectable, the requested transition is rejected, autonomous execution stops safely, and no queue, Journal, Git, or governed-content mutation follows.

## Failure disposition

Reject the architecture if undeclared work is queued, dispatched, or silently ignored without a blocked diagnostic.
