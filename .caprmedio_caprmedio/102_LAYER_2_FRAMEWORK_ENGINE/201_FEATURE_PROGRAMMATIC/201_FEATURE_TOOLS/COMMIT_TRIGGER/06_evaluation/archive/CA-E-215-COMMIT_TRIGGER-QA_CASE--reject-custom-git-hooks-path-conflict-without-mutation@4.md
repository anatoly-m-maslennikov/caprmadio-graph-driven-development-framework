---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-856

---
# Reject a custom Git Hooks path conflict without mutation

## Claim checked

Installing the managed Git Hooks fails safely when the repository already declares another local `core.hooksPath`.

## Test case

Prepare a repository with a custom local `core.hooksPath`, executable Hook carriers and recorded bytes and modes, but no managed CAPRMEDIO Git Hook registration; invoke `INSTALL_TOOLS run --apply`.

## Acceptance criteria

Installation returns one stable conflict diagnostic. The configured path, every referenced Hook byte and mode, adapter registry, Git configuration, index, refs, `.caprmedio_install`, and `.caprmedio_runtime` remain unchanged, and no backup carrier is created.

## Failure disposition

Reject the delivery if installation replaces, merges, copies, backs up, or partially registers over the custom Hook configuration, or if the failure is not deterministic.
