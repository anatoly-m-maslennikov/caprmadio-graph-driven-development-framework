---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - tool-orchestration
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-182
---
# Advance one fixed direct worker handoff

## Claim checked

A fixed direct worker handoff advances only the transition already declared by
the manager.

## Test case

Given a manager-produced two-step execution graph whose second step depends on
the first, execute the first worker and its synchronous handoff.

## Acceptance criteria

The exact typed result reaches only the declared second worker, the manager is
not re-entered for a new decision, and neither worker can select or alter the
downstream transition.

## Failure disposition

Reject the handoff when a result reaches an undeclared worker, a worker changes
the transition, the manager is re-entered for an already declared decision, or
the handoff loops.

## Sources

- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
