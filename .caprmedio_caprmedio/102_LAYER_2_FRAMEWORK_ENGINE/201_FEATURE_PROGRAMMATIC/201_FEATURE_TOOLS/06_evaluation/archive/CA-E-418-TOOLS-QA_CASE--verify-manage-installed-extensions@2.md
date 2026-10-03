---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - extension-lifecycle
    occurrent:
      - evaluation
version: 2
updated_at: 2026-09-02 00:40:00 +0400
relations:
  evaluation_for:
    - CA-M-252
---
# Verify manage installed Extensions

## Claim checked

CA-M-252 applies one exact Extension lifecycle transition atomically and reports its resulting installed state, or restores the prior state completely.

## Applicable when

Apply whenever exact Extension source or version resolution, installed-state planning, lifecycle effects, or rollback handling changes.

## Test case

Use one bounded Extension lifecycle trace: install an exact package into an empty inventory, update it to a second exact source and version, downgrade it to the first exact source and version, uninstall it, then attempt one transition containing a deliberately failing file effect.

## Acceptance criteria

Install, update, downgrade, and uninstall each produce exactly the planned identity, source, version, file inventory, and verification status. The failing transition restores the complete prior installed state and reports rollback evidence.

## Failure disposition

Reject the realization and preserve initial inventory, transition plan, source and version resolution, final inventories, failed effect, and rollback evidence.
