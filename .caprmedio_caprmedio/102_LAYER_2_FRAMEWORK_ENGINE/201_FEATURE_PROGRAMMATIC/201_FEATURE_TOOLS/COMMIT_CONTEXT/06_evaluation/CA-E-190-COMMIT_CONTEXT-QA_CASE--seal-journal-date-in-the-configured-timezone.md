---
subjects:
  governs: "Work Journal/Event/Occurred At"
  depends_on: []
version: 11
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Seal Journal date in the configured timezone

## Claim checked

the context Finder seals one local calendar date from `occurred_at` **in** the configured Artifact timestamp timezone **and** predicts Journal partitions from that sealed date.

## Test case

Configure `Asia/Tbilisi` **and** gather a context for an event at `2026-08-20 00:30:00 +04`, while the corresponding UTC date is still `2026-08-19`.

## Acceptance criteria

the sealed local date is `2026-08-20`, the predicted carrier is `<author>-2026-08-20-part-1.ndjson`, **and** the read-only Finder creates no Journal **or** other repository mutation.

## Failure disposition

Reject the Finder **if** it seals `2026-08-19`, uses filesystem time **or** an unconfigured timezone, omits the local date, **or** mutates a carrier.
