---
subjects:
  governs:
    continuant:
      - Git Index
version: 8
updated_at: 2026-09-15 03:15:32 +0400
relations:
  evaluation_for:
    - CA-R-805

---
# Reject runtime and temporary state from the Git index

## Claim checked

Repository-local runtime, temporary, and Git-internal state cannot enter a commit through the managed pre-commit boundary.

## Test case

In separate runs, force-stage one file below `.caprmedio_runtime` and one file below `.caprmedio_tmp`, then invoke `git-hook pre-commit`.

## Acceptance criteria

Each run returns one stable local-machine-path diagnostic before commit creation and leaves the staged Carrier, working tree, index, refs, Journal, governed source, runtime, and temporary state byte-identical.

## Failure disposition

Reject the delivery if the boundary succeeds, silently unstages or rewrites either file, mutates governed state, or reports the runtime file as an Atom.
