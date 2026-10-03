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
    - CA-R-1126
---
# Roll the Journal part after one hundred events

## Claim checked

Each author-date Journal segment contains at most 100 accepted events.

## Test case

Prepare `<author>-2026-08-20-part-1.ndjson` with 99 valid events, append two new events for the same author and date, and inspect both receipts and carriers.

## Acceptance criteria

The first append becomes line 100 of `part-1`; the second append becomes line 1 of `part-2`; neither segment contains more than 100 events; and no part number is skipped.

## Failure disposition

Reject the Journal Tool if it overfills `part-1`, opens `part-2` early, skips a part number, or rewrites an admitted record.
