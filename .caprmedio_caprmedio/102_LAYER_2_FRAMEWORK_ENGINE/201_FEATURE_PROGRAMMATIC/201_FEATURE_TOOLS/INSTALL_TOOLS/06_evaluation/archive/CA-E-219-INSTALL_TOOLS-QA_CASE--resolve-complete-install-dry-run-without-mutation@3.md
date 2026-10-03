---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103

---
# Resolve a complete install dry-run without mutation

## Claim checked

The installer resolves the complete canonical source, release identity, target layout, launchers, and Hook set before mutation.

## Test case

Prepare a Git repository containing the complete canonical Tool source and no prior installation, runtime, Codex carrier, or local Hooks path; invoke `INSTALL_TOOLS run` without apply.

## Acceptance criteria

One deterministic result reports the canonical source, install and runtime roots, release digest, file count, launchers, Hook set, and previous Hooks path. No file, directory, Git configuration entry, index entry, ref, Hook, or runtime state changes.

## Failure disposition

Reject delivery if the target set is incomplete or unstable, dry-run creates any carrier, or a required conflict remains undiscovered until apply.
