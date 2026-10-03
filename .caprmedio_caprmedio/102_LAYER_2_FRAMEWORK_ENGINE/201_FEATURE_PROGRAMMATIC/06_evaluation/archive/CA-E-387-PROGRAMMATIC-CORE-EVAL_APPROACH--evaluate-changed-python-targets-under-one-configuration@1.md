---
atom_id: CA-E-387
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - changed-python-evaluation
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-164
  derived_from:
    - CA-A-053
---
# Evaluate changed Python targets under one configuration

## Claim checked

Each changed Python target receives distinct syntax, Ruff, Mypy, and relevant
behavioral evidence under one declared interpreter and configuration.

## Test case

Evaluate one changed target for which Ruff passes, Mypy fails, and its focused
behavioral case passes.

## Acceptance criteria

Pass only when the three results remain separate and the aggregate changed-code
gate fails with the target, diagnostic, boundary, and replay command.

## Failure disposition

Reject masking one mechanism with another and return the failed evidence to its
owner.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [CA-M-164 — Ratchet typing and automation adoption](../05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md)
