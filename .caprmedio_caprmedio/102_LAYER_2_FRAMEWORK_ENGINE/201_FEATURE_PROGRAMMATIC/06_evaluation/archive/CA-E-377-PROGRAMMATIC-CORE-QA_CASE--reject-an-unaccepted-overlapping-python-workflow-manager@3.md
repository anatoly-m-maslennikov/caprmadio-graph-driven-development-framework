---
atom_id: CA-E-377
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-workflow-exception"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject an unaccepted overlapping Python workflow manager

## Claim checked

One Python workflow does not mix uv with another overlapping environment or
dependency manager unless an accepted Method owns a bounded exception.

## Test case

Evaluate one governed path that runs both uv and Poetry without an accepted
exception.

## Acceptance criteria

Pass only when the path is rejected before environment mutation.

## Failure disposition

Block the alternative manager until a required capability, bounded carriers,
commands, cost, recovery procedure, and Operator acceptance are governed.

## Sources

- [CA-M-221 — Use uv as the default Python workflow frontend](../05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md)
