---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - extension-lifecycle
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1152
  derived_from:
    - CA-A-058
---
# Manage installed Extensions

## Applicable when

Use this Method when one Extension must be installed, uninstalled, updated, or downgraded by exact declared source and version.

## Procedure

1. Resolve the requested operation, Extension identity, exact source, exact package version, and current installed-state inventory.
2. Verify that the selected source and version identify one package and compute the target installed-state inventory.
3. Produce a complete transition plan with affected files, previous installed state, and rollback actions.
4. On explicit authorization, apply the unchanged plan atomically and restore the previous state if any operation fails.
5. Report the resulting Extension identity, source, version, file inventory, and verification status.

## Outcome

One exact Extension lifecycle operation produces an attributable resulting installed state or restores the prior state completely.

## Failure or stop

Stop or roll back on an unresolved source or version, identity mismatch, collision, incomplete plan, failed effect, or unverifiable resulting state.
