---
atom_id: CA-M-234
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-boundary-validation
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 01:50:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Validate untrusted structured data with Pydantic

Use Pydantic when untrusted structured data crosses an admitted Python
boundary. Validate once at the boundary and pass accepted typed values into
the deterministic core without making Pydantic the universal internal model.

## Applicable when

Apply to an admitted CLI payload, Hook event, configuration carrier, Journal
record, protocol message, or external adapter whose invalid structure could
hide a contract defect.

## Procedure

1. Define the bounded input model with field types and constraints before
   custom validators.
2. Use strict validation when coercion could hide a defect; admit lax conversion
   only for a declared interoperability need and make it observable.
3. Reject undeclared extra fields for closed machine contracts.
4. Return structured validation diagnostics and pass the accepted typed value
   to the deterministic core.
5. Add Pydantic as a runtime dependency only where validation and schema value
   justify its dependency cost.

## Outcome

Untrusted structured inputs become explicit typed values at one boundary while
the internal model remains independent of the validation library.

## Failure or stop

Stop admission when the boundary is not declared, coercion is silent, extra
fields escape a closed contract, or the dependency has no bounded benefit.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/concepts/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
