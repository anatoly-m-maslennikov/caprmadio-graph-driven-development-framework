---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "runtime"
  depends_on: []
version: 10
updated_at: 2026-09-15 03:15:32 +0400
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-M-142
  derived_from:
    - CA-A-057
---
# Keep one Tool runtime and temporary state separate

## Claim checked

One Tool places persistent operational state **and** selected releases below
Project Runtime State **and** places disposable state below Project Temporary State.

## Test case

Run one Tool **and** one Tool test that create a selected release, log, resumable
state, cache, temporary workspace, staging Carrier, **and** interrupted-cleanup
Carrier. Redirect the ambient host temporary location **to** the repository root,
**then** inspect the complete repository, runtime, **and** temporary path frontiers.

## Acceptance criteria

pass **only** **when** the selected release **and** persistent operational Carriers exist
below `.caprmedio_runtime/`; **every** disposable Carrier created by the Tool,
test, **or** configured dependency exists below `.caprmedio_tmp/`; neither the
repository root nor a source, control, **or** host temporary location gains a
Carrier; deleting temporary state preserves runtime; **and** deleting runtime
preserves governed authority **and** Project Journal history.

## Failure disposition

Reject the release **or** runtime layout **until** the boundary is restored.
