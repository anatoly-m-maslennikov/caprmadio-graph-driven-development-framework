---
atom_id: "CA-M-232"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    continuant:
      - "engine-settings-reader"
  depends_on:
    continuant:
      - "programmatic software"
version: 3
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
---
# Read Engine settings through one shared boundary

Use one centralized Settings Reader for every applicable Tool, App, and MCP
component. It reads only the canonical CAPRMEDIO project-settings Projection,
validates the complete input, and returns an immutable typed snapshot with
source and version provenance.

## Applicable when

Apply whenever PROGRAMMATIC behavior depends on CAPRMEDIO project settings.

## Procedure

1. Read `.caprmedio_caprmedio/caprmedio_project_settings.toml` through the
   shared Reader.
2. Validate the complete carrier at the boundary and return structured
   diagnostics for invalid input.
3. Pass the immutable snapshot explicitly to the consuming deterministic core
   or application service.
4. Do not add component-specific parsers, default chains, environment
   fallbacks, semantic overrides, or writes to the Reader.
5. Make the control panel use the same Reader and change settings through their
   governed source and dedicated Doer, never through the Projection.

## Outcome

Every component observes one validated settings snapshot without duplicating
parsing or inventing a second control panel.

## Failure or stop

Stop when the canonical Projection is missing or invalid, provenance is absent,
or a consumer would bypass or mutate the shared snapshot.

## Sources

- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
