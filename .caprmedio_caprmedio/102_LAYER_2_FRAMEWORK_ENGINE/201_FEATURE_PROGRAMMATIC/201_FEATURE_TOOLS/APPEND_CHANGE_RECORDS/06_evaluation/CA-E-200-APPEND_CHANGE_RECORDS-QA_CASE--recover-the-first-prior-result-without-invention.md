---
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on: []
version: 15
updated_at: "2026-10-08 02:28:30 +0000"
relations:
  evaluation_for:
    - CA-R-812
    - CA-R-1644
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Recover the first prior result without invention

## Claim checked

**when** an existing governed subject has no accepted prior result event, recovery creates a separate evidenced baseline **only** **when** the prior state is sufficiently supported.

## Test case

prepare the first schema-version-3 non-ADD file change for an existing subject with no prior recorded result. prove a separate recovered baseline from matching present Carrier readback **without** Git, **then** with genuine Git corroboration. repeat with contradictory **and** insufficient evidence, an ID-less Draft Carrier, a no-op, **and** unconfirmed append receipts.

## Acceptance criteria

the supported case appends **=1** `recovered` `governed_project_state` baseline **before** effects **and** makes the `completed` `governed_project_change` event reference its confirmed prior through `previous_result_event`. the contradictory **and** insufficient cases do **not** mutate the subject; no historical field is guessed. a no-op creates **none** of a baseline **or** change event. unconfirmed baseline recording blocks effects; unconfirmed post-effect recording retains the real effects as partial **and** permits recording retry **only**. accepted legacy schema-version-2 records remain readable, **not** current write examples.

## Failure disposition

reject recovery **if** it embeds the baseline **in** the change event, invents prior state, accepts contradictory evidence, **or** proceeds **without** the required previous-result reference.
