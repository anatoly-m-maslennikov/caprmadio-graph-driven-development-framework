---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "runtime"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-143
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Isolate one Tool runtime folder

## Claim checked

Each Tool that persists runtime files uses its dedicated owned runtime directory.

## Test case

Run two Tools that persist runtime files concurrently.

## Acceptance criteria

Each Tool writes only below its own runtime directory or declared run-specific descendant, and neither relies on the other's files.

## Failure disposition

Stop the affected Tool execution and report the unowned shared-state boundary.
