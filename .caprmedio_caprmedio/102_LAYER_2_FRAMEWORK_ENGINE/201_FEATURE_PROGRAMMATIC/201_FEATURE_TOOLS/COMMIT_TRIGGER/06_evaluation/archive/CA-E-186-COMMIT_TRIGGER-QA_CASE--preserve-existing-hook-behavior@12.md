---
subjects:
  governs: "Git Hook"
version: 12
updated_at: "2026-09-15 21:31:49 +0000"
relations:
  evaluation_for:
    - CA-R-856
    - CA-D-010

---
# Preserve existing Hook behavior

## Claim checked

installation, control, **and** removal of a selected project-local Git Hook adapter **must** preserve pre-existing repository Hook behavior. Git Hooks **must not** produce COMMIT_TRIGGER events under CA-D-010.

## Test case

prepare a repository with an executable pre-commit Hook that records a sentinel **and** no local hook-path override. explicitly select Git Hook integration, run installation, status, enable, disable, **and** uninstall, **and** invoke the Hook boundary **in** **every** state. **in** a separate fixture, select installation **without** Hook integration.

## Acceptance criteria

**all** of the following **must** hold:

- selected installation preserves the existing Hook's bytes **and** executable mode; the managed launcher invokes it **=1** time **before** the managed Evaluation.
- an enabled Git Hook performs **only** its registered Evaluation **or** observation. enabled, disabled, **and** uninstalled Git Hooks produce **=0** COMMIT_TRIGGER events.
- status reports the actual selected integration state.
- uninstall removes **only** managed registration **and** launchers, restores the previous hook-path selection, **and** leaves the existing Hook unchanged **without** creating a backup Carrier.
- installation **without** selected Hook integration leaves existing Hook Carriers **and** registration unchanged **and** does **not** require host Hook availability.

## Failure disposition

reject delivery **if** prior Hook behavior is lost, duplicated, reordered incompatibly, **or** overwritten; **if** a Git Hook produces a trigger; **or** **if** installation changes unselected Hook integration.
