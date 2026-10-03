---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
    - CA-R-1126
---
# Route by the sealed Journal date

## Claim checked

The Journal-appending Doer routes an event by the author and local date sealed in its context, even when the current clock has crossed a calendar boundary.

## Test case

In `Asia/Tbilisi`, seal one context at `2026-08-20 23:59:59 +04`, advance the controlled clock to `2026-08-21 00:00:01 +04`, and apply the unchanged sealed event.

## Acceptance criteria

The event is appended once to `<author>-2026-08-20-part-<N>.ndjson`; its stored `occurred_at` remains unchanged; and no carrier for `2026-08-21` is created for that event.

## Failure disposition

Reject the Doer if it recomputes author, date, timezone, or `occurred_at`, routes by the current clock or filesystem time, or appends the event more than once.
