---
atom_id: CA-E-225
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-21 03:12:00
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
  check_of:
    - CA-D-011
---
# Reject drift in an existing release

## Claim checked

An existing content-addressed release cannot be reused or repaired in place after any installed byte or executable mode drifts.

## Test case

Install one release, change one installed registry byte, record the current manifest and managed Hook bytes, and apply the unchanged canonical source again.

## Acceptance criteria

Installation returns one stable release-collision diagnostic before selecting or repairing the release. The changed installed byte remains observable, while the current manifest, launchers, Hooks, Git configuration, canonical source, runtime, index, and refs remain unchanged.

## Failure disposition

Reject delivery if reinstall silently trusts, overwrites, or partially repairs the drifted release; repoints any managed carrier; or changes unrelated state.
