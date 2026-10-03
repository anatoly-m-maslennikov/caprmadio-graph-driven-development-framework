---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-812
    - CAPRMEDIO-GOV-REQU-340--recover-work-journal-coverage-without-invention
---
# Recover the first prior result without invention

## Claim checked

When an existing governed subject has no accepted prior result event, recovery creates a separate evidenced baseline only when the prior state is sufficiently supported.

## Test case

Run the first schema-v2 change for one existing subject with matching Git and carrier evidence, then repeat with contradictory and insufficient evidence.

## Acceptance criteria

The supported case appends one `recovered` `governed_file_state` baseline and makes the change event reference it through `previous_result_event`; the contradictory and insufficient cases append nothing and return stable recovery diagnostics; no field is guessed.

## Failure disposition

Reject recovery if it embeds the baseline in the change event, invents prior state, accepts contradictory evidence, or proceeds without the required previous-result reference.
