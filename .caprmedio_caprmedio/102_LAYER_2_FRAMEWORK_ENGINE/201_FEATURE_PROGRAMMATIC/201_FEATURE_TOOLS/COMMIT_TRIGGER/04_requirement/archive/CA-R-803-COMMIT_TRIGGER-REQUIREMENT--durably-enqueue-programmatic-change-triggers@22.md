---
subjects:
  governs: "feature-boundary"
  depends_on: []
cce_version: cce_1
cce_form: obligation
version: 22
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Durably enqueue programmatic change triggers

COMMIT_TRIGGER **must** accept an authorized MCP Atom mutation event **or** a registered project-change adapter event **and** atomically persist one immutable schema-versioned envelope below .caprmedio_runtime/state/commit_automation/inbox/ **before** acknowledging intake. The envelope **must** preserve repository identity, stable source-event identity, source application, session **and** turn identities **when** supplied, Tool-use identity **when** supplied, observation time, changed-target candidates, sealed Initiative **and** action identity **when** supplied by an authoritative producer, **and** expected subject revision **or** digest **when** one exists.

the Codex adapter **must** use one PostToolUse command Hook configured with async: true. Its handler **may** validate **and** normalize the host payload, resolve the activated repository, write through a temporary carrier **and** atomic rename, **and** return. It **must not** scan the repository, capture a before-event frontier, gather commit context, append a Journal, stage files, acquire the Git gate, run **or** spawn a pipeline worker, retry the pipeline, **or** wait for a Git commit. PreToolUse, SessionStart, **and** Stop **must not** be used for automatic-commit intake **or** missed-change reconciliation.

Any number of producers **may** enqueue concurrently **and** complete out of order. Repeated delivery of the same stable source-event identity **must** remain idempotent. A cancelled asynchronous Hook cannot revoke an envelope whose atomic rename completed. An event that cannot establish its activated repository **or** stable source identity **must** fail **without** acknowledgment. Missing **or** cancelled Hook delivery is recovered by the independently supervised repository reconciliation service, **not** by synchronous host lifecycle work.
