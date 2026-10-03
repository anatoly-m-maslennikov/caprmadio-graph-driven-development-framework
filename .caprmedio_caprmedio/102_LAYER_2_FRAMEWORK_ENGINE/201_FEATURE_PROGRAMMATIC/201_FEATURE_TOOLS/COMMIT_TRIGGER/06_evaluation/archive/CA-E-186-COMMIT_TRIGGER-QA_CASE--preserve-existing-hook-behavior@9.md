---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 9
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-856

---
# Preserve existing Hook behavior

## Claim checked

Installing, controlling, and removing the project-local commit adapter preserves pre-existing repository Hook behavior.

## Test case

Prepare a repository with one existing executable default `.git/hooks/pre-commit` Hook that records a sentinel and no local `core.hooksPath`. Run the adapter's install, status, enable, disable, and uninstall operations, invoking the file-change boundary while enabled, while disabled, and after uninstall.

## Acceptance criteria

Installation leaves the existing Hook bytes and executable mode unchanged, registers `.caprmedio_install/hooks/git` as the local `core.hooksPath`, and its installed launcher invokes the existing Hook once before the managed Evaluation. The enabled adapter emits exactly one `COMMIT_TRIGGER`; the disabled and uninstalled adapter emits none. Status reports each state correctly. Uninstall removes only the managed registration and launchers, restores the prior absence of local `core.hooksPath`, leaves the existing Hook byte-for-byte intact, and creates no backup carrier.

## Failure disposition

Reject delivery if existing behavior is skipped, duplicated, reordered incompatibly, overwritten, or not restored byte-for-byte; if disabled or uninstalled operation emits a trigger; or if installation creates a repository backup copy.
