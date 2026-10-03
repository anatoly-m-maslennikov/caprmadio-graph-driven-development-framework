---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "source-name"
  depends_on:
    - "programmatic software"
version: 6
updated_at: 2026-09-01 23:50:00 +0400
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject an ambiguous changed source name

## Claim checked

One new or materially changed source unit has a specific,
intention-revealing name that states one responsibility.

## Test case

Evaluate one changed class named `Manager` without a qualifying project term or
owned responsibility.

## Acceptance criteria

Pass only when the class is rejected until its name identifies the exact
responsibility it owns.

## Failure disposition

Block the changed unit from claiming naming conformance.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
