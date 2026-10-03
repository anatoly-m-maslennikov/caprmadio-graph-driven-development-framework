---
atom_id: CA-E-223
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-857
    - CA-M-104
  check_of:
    - CA-D-012
---
# Start each enabled service once

## Claim checked

Apply starts each enabled installed service once and repeated apply recognizes its live process.

## Test case

Install one enabled long-running Python service, invoke dry-run, apply, apply again, and status.

## Acceptance criteria

Dry-run predicts one start without mutation. First apply starts one process and writes its PID and logs only under its runtime service directory. Second apply reports the same PID as already running and starts no process. Status reports one enabled and running service, and the installation contains no Python cache.

## Failure disposition

Reject delivery if dry-run mutates, apply duplicates a live service, state is written outside `.caprmedio_runtime`, implementation is read outside `.caprmedio_install`, or liveness is reported incorrectly.
