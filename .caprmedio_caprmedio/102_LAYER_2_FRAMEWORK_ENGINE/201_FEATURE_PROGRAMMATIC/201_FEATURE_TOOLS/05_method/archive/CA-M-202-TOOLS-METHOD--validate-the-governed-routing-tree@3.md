---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1123
  derived_from:
    - CA-A-058
---
# Validate the governed routing tree

## Applicable when

Use this Method before a governed router selects or traverses a route in the current routing tree.

## Procedure

1. Load the current routing-tree authority and its declared node, edge, root, leaf, priority, and fallback constraints.
2. Resolve every referenced target against the current active graph without following derived inverse relations as authored edges.
3. Check root uniqueness, reachability, permitted edge types, cycle rules, selector exclusivity, fallback completeness, and terminal-route validity.
4. Emit one stable issue per violated constraint with source carrier and exact route location.
5. Permit routing only when the selected tree frontier has no blocking issue.

## Outcome

Routing receives a deterministic valid verdict or an attributable set of structural violations before any route is used.

## Failure or stop

Treat unreadable authority, unresolved targets, ambiguous roots, and stale frontiers as blocking validation failures.
