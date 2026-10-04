---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "object-construction"
  depends_on:
    - "programmatic software"
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject I/O during object construction

## Claim checked

one PROGRAMMATIC object is constructed **without** acquiring resources **or** applying
external effects.

## Test case

construct one object while its declared resource boundary is unavailable **and**
observe whether construction attempts filesystem, process, network,
persistence, **or** logging-export I/O.

## Acceptance criteria

pass **only** **when** construction completes **without** I/O **and** acquisition begins **only**
through a specifically named explicit method.

## Failure disposition

reject the object lifecycle **until** acquisition is removed from construction.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
