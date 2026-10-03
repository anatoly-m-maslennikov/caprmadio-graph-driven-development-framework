---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - tool-source-architecture
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-27 14:45:30 +0400
relations:
  evaluation_for:
    - CA-M-157
    - CA-M-158
    - CA-M-160
    - CA-M-162
    - CA-M-182
---
# Evaluate Tool source architecture and dispatch conformance

## Claim checked

Changed Tool source conforms to the shared PROGRAMMATIC function, object,
effect, source-boundary, and manager-defined execution-graph Methods.

## Applicable conditions

Apply to every new or materially changed Tool source tree.

## Check

Evaluate declared file and executable-unit limits, side-effect-free standalone
functions, specifically named effect-owner objects, one pure decision manager,
atomic non-deciding workers, an acyclic manager-defined execution graph,
mechanical scheduling or direct dispatch, canonical manager, worker, and asset
placement, and externalized large static mappings. Inject worker observations
and require every semantic and lifecycle decision to remain in the manager's
explicit result. Require handoffs and queued completions to follow only
manager-declared transitions.

## Acceptance

Pass only when every applicable boundary conforms independently and the
dispatcher or scheduler advances the declared graph without changing it.

## Failure and stop

Fail each violated constraint independently with the exact file, object,
dependency, transition, or effect boundary. Generated Runtime or Delivery
output cannot excuse a violation in hand-authored Tool source.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python FAQ: testing programs and components](https://docs.python.org/3/faq/library.html#how-do-i-test-a-python-program-or-component)
- [Python documentation: `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
