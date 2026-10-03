---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-805

---
# Reject installation and runtime state from the Git index

## Claim checked

Repository-local installation, runtime, and Git-internal state cannot enter a commit through the managed pre-commit boundary.

## Test case

In separate runs, force-stage one file below `.caprmedio_install` and one file below `.caprmedio_runtime`, then invoke `git-hook pre-commit`.

## Acceptance criteria

Each run returns one stable local-machine-path diagnostic before commit creation and leaves the staged carrier, working tree, index, refs, Journal, governed source, installation, and runtime byte-identical.

## Failure disposition

Reject the delivery if the boundary succeeds, silently unstages or rewrites either file, mutates governed state, or reports the runtime file as an Atom.
