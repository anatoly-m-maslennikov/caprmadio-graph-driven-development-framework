---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-246
---
# Verify transition one generic Artifact lifecycle

## Claim checked

CA-M-246 applies exactly one registered generic Artifact lifecycle transition or fails closed without changing the carrier.

## Applicable when

Apply whenever a generic lifecycle state model, destination derivation, or lifecycle transaction mechanics change.

## Test case

Prepare one source Artifact at a registered lifecycle state with one canonical reference. Request one valid transition and then a transition not present in the state model.

## Acceptance criteria

The valid case creates the permitted destination if needed, moves the carrier, records required metadata and reference updates, and reaches the registered state. The undefined transition changes nothing.

## Failure disposition

Reject the realization and preserve the state model, source and destination states, metadata and reference diffs, transaction evidence, and undefined-transition finding.
