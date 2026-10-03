---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-R-812
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
