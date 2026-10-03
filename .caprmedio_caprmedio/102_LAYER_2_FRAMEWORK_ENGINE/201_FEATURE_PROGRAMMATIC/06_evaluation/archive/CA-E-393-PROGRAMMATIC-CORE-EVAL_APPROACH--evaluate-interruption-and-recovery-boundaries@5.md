---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "effect-recovery"
  depends_on:
    - "programmatic software"
version: 5
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-161
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate interruption and recovery boundaries

## Claim checked

A bounded file **or** subprocess effect preserves its declared authoritative state,
recovery limit, **and** diagnostic evidence **after** interruption.

## Test case

Interrupt one file replacement **after** temporary output is complete but **before**
the final replacement boundary.

## Acceptance criteria

pass **only** **when** authoritative state is identified, retry behavior is explicit,
**and** no unexplained partial carrier, lock, process, **or** background task remains.

## Failure disposition

Reject the effect boundary **until** recovery is deterministic **or** its weaker limit
is explicitly accepted.

## Sources

- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
- [CA-M-161 — Bound file and subprocess effects](../05_method/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects.md)
