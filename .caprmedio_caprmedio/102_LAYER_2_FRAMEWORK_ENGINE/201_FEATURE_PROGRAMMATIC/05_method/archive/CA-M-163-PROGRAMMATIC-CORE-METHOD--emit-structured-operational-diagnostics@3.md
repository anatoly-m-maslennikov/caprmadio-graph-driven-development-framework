---
atom_id: CA-M-163
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - operational-diagnostic
  depends_on:
    continuant:
      - programmatic software
      - Logging Policy
version: 3
updated_at: 2026-09-01 01:45:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Emit structured operational diagnostics

Emit structured operational diagnostics for PROGRAMMATIC work under the active
Logging Policy in `CAPRMEDIO-GOV-REQU-315`, including its ERROR, WARNING, INFO,
and DEBUG meanings. This Method applies that authority to PROGRAMMATIC
diagnosis; it does not own the level vocabulary, level meanings, or Journal
meaning.

## Applicable when

Apply when a Tool, App backend service, or MCP component reports normal
operation, degraded operation, failure, recovery, or diagnostic detail.

## Procedure

1. Select ERROR, WARNING, INFO, or DEBUG according to the active Logging Policy;
   do not introduce a fifth shared severity.
2. Emit records through one project-owned logging abstraction and schema.
   Include timestamp, level, component, operation, outcome, and the canonical
   action or event identity when one exists.
3. Include actionable, contextual, sanitized fields and keep DEBUG bounded to
   diagnosable need.
4. Materialize sink and runtime settings in configuration or Implementation,
   govern carrier placement and encoding through Delivery, and preserve actual
   execution and diagnostic evidence through Ops.
5. Declare retention, loss, and back-pressure behavior at those bounded
   materialization and operational boundaries.
6. Make logging failure observable without silently breaking primary work.

## Outcome

Operators can diagnose component behavior without exposing secrets, confusing
operational diagnostics with governed Journal history, or relying on an
undeclared sink behavior.

## Failure or stop

Stop emission or release of the affected diagnostic path when required context
cannot be sanitized, a logging failure is hidden, or the component would use
the Journal as a substitute logging sink.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
