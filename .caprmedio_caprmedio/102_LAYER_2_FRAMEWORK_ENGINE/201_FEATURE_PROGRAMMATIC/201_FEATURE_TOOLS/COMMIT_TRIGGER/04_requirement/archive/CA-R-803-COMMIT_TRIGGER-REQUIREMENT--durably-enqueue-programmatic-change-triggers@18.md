---
subjects:
  declared:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 18
updated_at: 2026-08-25 01:49:10 +0400
---
# Durably enqueue programmatic change triggers

COMMIT_TRIGGER MUST accept an authorized MCP Atom mutation event or a registered project-change adapter event and atomically persist one immutable schema-versioned envelope below .caprmedio_runtime/state/commit_automation/inbox/ before acknowledging intake. The envelope MUST preserve repository identity, stable source-event identity, source application, session and turn identities when supplied, Tool-use identity when supplied, observation time, changed-target candidates, sealed Initiative and action identity when supplied by an authoritative producer, and expected subject revision or digest when one exists.

The Codex adapter MUST use one PostToolUse command Hook configured with async: true. Its handler may validate and normalize the host payload, resolve the activated repository, write through a temporary carrier and atomic rename, and return. It MUST NOT scan the repository, capture a before-event frontier, gather commit context, append a Journal, stage files, acquire the Git gate, run or spawn a pipeline worker, retry the pipeline, or wait for a Git commit. PreToolUse, SessionStart, and Stop MUST NOT be used for automatic-commit intake or missed-change reconciliation.

Any number of producers MAY enqueue concurrently and complete out of order. Repeated delivery of the same stable source-event identity MUST remain idempotent. A cancelled asynchronous Hook cannot revoke an envelope whose atomic rename completed. An event that cannot establish its activated repository or stable source identity MUST fail without acknowledgment. Missing or cancelled Hook delivery is recovered by the independently supervised repository reconciliation service, not by synchronous host lifecycle work.
