---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-803
---
# Suppress the recursive Journal trigger

## Claim checked

No related Journal append produced for one file-change trigger generates another trigger.

## Test case

Run one registered subject-file change whose related records span multiple Journal carriers through the complete apply flow while observing every Hook boundary, including every internal Journal carrier write.

## Acceptance criteria

Exactly one `COMMIT_TRIGGER` exists for the subject change, every correlated Journal append is suppressed, the complete related record set is appended, and exactly one Git commit results.

## Failure disposition

Reject the Hook if it emits a trigger for any internal Journal append, suppresses the original subject change, or depends only on timing to avoid recursion.
