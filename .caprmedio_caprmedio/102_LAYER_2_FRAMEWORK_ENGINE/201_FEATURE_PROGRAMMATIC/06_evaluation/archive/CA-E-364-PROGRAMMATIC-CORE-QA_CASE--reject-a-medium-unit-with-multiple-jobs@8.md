---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "executable-unit-size"
  depends_on:
    - "programmatic software"
version: 8
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-162
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject a medium unit with multiple jobs

## Claim checked

one changed executable unit between 26 **and** 40 logical lines performs **=1** coherent job.

## Test case

evaluate one 30-line changed function whose accurate name **and** branches reveal
two independently reusable responsibilities.

## Acceptance criteria

pass **only** **when** the unit is rejected **until** the two responsibilities are split.

## Failure disposition

block the unit from claiming the 26-to-40-line allowance.

## Sources

- [CA-M-162 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries.md)
