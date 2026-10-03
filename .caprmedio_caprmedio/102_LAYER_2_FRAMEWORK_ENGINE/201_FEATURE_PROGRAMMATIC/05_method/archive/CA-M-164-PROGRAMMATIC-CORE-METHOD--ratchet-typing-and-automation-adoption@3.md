---
atom_id: CA-M-164
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - engineering-ratchet
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 01:45:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Ratchet typing and automation adoption

Advance PROGRAMMATIC typing and automation through bounded passing targets:
prevent regression, require the admitted profile for changed or new targets,
and expand only deliberately.

## Applicable when

Apply when a Tool, App backend service, or MCP component adds or materially
changes source that falls within an admitted typing, formatting, linting, or
behavioral-check capability.

## Procedure

1. Resolve each selected typing, formatting, linting, or behavioral-check
   capability from its accepted Method owner.
2. Read its current tool, version, profile, and bounded target materialization
   from canonical configuration or Implementation; read carrier placement and
   encoding from Delivery.
3. Keep formatting, linting, typing, and behavioral evidence distinct.
4. Prevent changed or new targets from regressing below the current admitted
   boundary.
5. Expand or replace a selected capability only through a Method change;
   materialize that change separately and preserve actual runs as Ops evidence.

## Outcome

Automation and typing improve monotonically at an admitted surface without
turning an unselected tool, version, or strictness level into shared authority.

## Failure or stop

Stop a claimed ratchet when no accepted Method owns the selection, no passing
baseline or bounded materialization exists, or the configuration,
Implementation, Delivery, and Ops evidence disagree with that selection.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
