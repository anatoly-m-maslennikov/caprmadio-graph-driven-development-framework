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
    - CA-R-812
    - CA-R-805
---
# Derive the Git message from the structured Journal event

## Claim checked

The canonical Git commit message is a deterministic Projection of the structured file-change event rather than a second stored action payload.

## Test case

Apply one valid context whose structured event contains two typed upstream relation groups and an `UPDATE` action, independently render the expected canonical message from that event, and compare it with the Git commit subject while inspecting the NDJSON object.

## Acceptance criteria

The Git commit subject is byte-identical to the independently rendered Projection, preserves canonical relation and action ordering, contains no added prefix, suffix, quoting, normalization, or line wrapping, and the NDJSON object contains no `action_message` field.

## Failure disposition

Reject the flow at the first rendering mismatch or duplicated message field and report the structured input and divergent output.
