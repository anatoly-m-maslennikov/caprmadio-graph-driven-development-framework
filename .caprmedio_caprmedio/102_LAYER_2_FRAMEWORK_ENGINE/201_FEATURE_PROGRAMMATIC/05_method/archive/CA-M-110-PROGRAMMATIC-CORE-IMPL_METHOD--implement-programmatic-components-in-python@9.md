---
atom_id: CA-M-110
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - programmatic-components
  depends_on:
    continuant:
      - programmatic software
version: 9
updated_at: 2026-09-01 01:33:45 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Implement PROGRAMMATIC components in Python

Use Python for applicable PROGRAMMATIC Tools, App backend services, and MCP
components. This Method owns the Python technology selection for that bounded
scope. Configuration and Implementation materialize the selected runtime,
dependencies, and exceptions; Delivery governs their carrier placement and
encoding; Ops governs workflow execution and operational evidence. This Method
does not govern Skills or make Python a discipline-independent CAPRMEDIO
meaning.

## Applicable when

Apply when a Tool, App backend service, or MCP component is added or materially
changed, or when its Python realization, runtime dependency, or non-Python
exception is proposed.

## Procedure

1. Apply the Python selection established by this Method and read its current
   materialization before realizing a component.
2. Use the standard library when it provides the required behavior with
   comparable clarity and reliability.
3. Add or change a runtime, library, workflow tool, or non-Python exception
   only through an accepted Method that selects it for a bounded scope.
4. Materialize each accepted selection in canonical configuration and
   Implementation without making either carrier a second authority.
5. Place and encode each materialization through its Delivery, and preserve
   actual execution results as Ops evidence.

## Outcome

Every applicable component follows one Method-owned technology selection.
Configuration and Implementation reproduce it, Delivery locates its carriers,
and Ops records its execution without taking over selection authority.

## Failure or stop

Stop admission or release when no accepted Method owns a required selection,
its materialization disagrees with that Method, or the Delivery or Ops boundary
is absent. Do not infer a platform-support claim from local execution.

## Sources

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
