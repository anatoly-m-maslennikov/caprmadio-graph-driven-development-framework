---
subjects:
  governs: "Background Service/Process"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-857
    - CA-M-104

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Start each enabled service once

## Claim checked

Apply starts each enabled installed service once and repeated apply recognizes its live process.

## Test case

Install one enabled long-running Python service, invoke dry-run, apply, apply again, and status.

## Acceptance criteria

Dry-run predicts one start without mutation. First apply starts one process and writes its PID and logs only under its runtime service directory. Second apply reports the same PID as already running and starts no process. Status reports one enabled and running service; `.caprmedio_runtime/tools` contains no Python cache; and disposable bytecode and cache Carriers exist only below `.caprmedio_tmp`.

## Failure disposition

Reject delivery if dry-run mutates, apply duplicates a live service, state is written outside `.caprmedio_runtime`, implementation is read outside `.caprmedio_runtime/tools`, or liveness is reported incorrectly.
