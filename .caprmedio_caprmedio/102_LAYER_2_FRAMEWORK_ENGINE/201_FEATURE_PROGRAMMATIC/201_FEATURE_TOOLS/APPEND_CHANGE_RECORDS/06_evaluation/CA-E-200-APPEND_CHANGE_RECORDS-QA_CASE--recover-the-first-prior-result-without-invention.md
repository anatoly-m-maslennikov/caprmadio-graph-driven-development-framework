---
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on: []
version: 14
updated_at: "2026-09-12 04:15:38 +0400"
relations:
  evaluation_for:
    - CA-R-812
    - CAPRMEDIO-GOV-REQU-340
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Recover the first prior result without invention

## Claim checked

**when** an existing governed subject has no accepted prior result event, recovery creates a separate evidenced baseline **only** **when** the prior state is sufficiently supported.

## Test case

run the first schema-v2 change for one existing subject with matching Git **and** carrier evidence, **then** repeat with contradictory **and** insufficient evidence.

## Acceptance criteria

the supported case appends one `recovered` `governed_file_state` baseline **and** makes the change event reference it through `previous_result_event`; the contradictory **and** insufficient cases append nothing **and** return stable recovery diagnostics; no field is guessed.

## Failure disposition

reject recovery **if** it embeds the baseline **in** the change event, invents prior state, accepts contradictory evidence, **or** proceeds **without** the required previous-result reference.
