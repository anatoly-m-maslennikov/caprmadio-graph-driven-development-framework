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
    - CA-M-087
    - CA-R-804
---
# Reject a trigger with no file change

## Claim checked

A trigger that resolves to neither a lifecycle change, Structural relocation, nor governed carrier update does not produce a commit change set.

## Test case

Supply a trigger whose candidate file has identical identity, path, filename, content, governed carrier state, and version in committed, working, and staged graphs.

## Acceptance criteria

Context gathering fails closed with a deterministic no-change diagnostic and does not return `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`.

## Failure disposition

Reject the classifier and report the incorrectly emitted change set.
