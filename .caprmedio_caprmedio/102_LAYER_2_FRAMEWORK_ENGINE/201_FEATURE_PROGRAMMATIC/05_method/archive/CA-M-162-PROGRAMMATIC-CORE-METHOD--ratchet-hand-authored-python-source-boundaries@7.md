---
atom_id: "CA-M-162"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    continuant:
      - "source-boundary"
  depends_on:
    continuant:
      - "programmatic software"
version: 7
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-110"
---
# Ratchet hand-authored Python source boundaries

Keep new or materially changed hand-authored PROGRAMMATIC Python source within
the accepted source-size ratchet and require cyclomatic-complexity lint for
each changed executable unit. Apply CA-M-157, CA-M-158, and CA-M-160 for
function allocation, object ownership, effect boundaries, and their naming
rules rather than restating those policies here. Review cohesion,
responsibility, dependency direction, and testability independently from size
and complexity scores.

## Applicable when

Apply to each new or materially changed hand-authored Python file in Tools, App
backend services, or MCP components. Generated Runtime and Delivery outputs
are outside this source rule.

## Procedure

1. Target at most 200 physical lines per file.
2. Target at most 25 logical lines per executable unit; use 26–40 only for one
   coherent job.
3. Run the Method-selected cyclomatic-complexity lint for every new or
   materially changed executable unit.
4. Reject a unit above the Method-selected complexity maximum as materialized
   in canonical configuration unless one specific bounded exception records
   the measured value, applicable maximum, reason, and condition for
   reconsideration.
5. For an executable unit above 40 logical lines, record the specific
   source-size exception and retain its single responsibility.
6. Externalize a static mapping larger than 20 entries or 25 source lines.
   Use TOML by default, JSON for schemas or machine interchange, and YAML only
   when its distinct features are required. Treat size and complexity scores
   as navigation constraints rather than proof of quality.

## Outcome

Changed source ratchets toward readable, bounded units and externalized static
data without declaring existing oversized or over-complex source an immediate
whole-repository failure. Source size and cyclomatic complexity cannot regress
silently in changed executable units.

## Failure or stop

Stop claiming conformance for a changed unit that exceeds its source-size or
cyclomatic-complexity boundary without a documented bounded exception or
retains a large static mapping inside executable Python source. Stop when no
accepted Method selects the complexity-lint profile and maximum, their
materialization is absent or inconsistent, or reducing a score would obscure
a separate responsibility or needed recovery boundary.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
