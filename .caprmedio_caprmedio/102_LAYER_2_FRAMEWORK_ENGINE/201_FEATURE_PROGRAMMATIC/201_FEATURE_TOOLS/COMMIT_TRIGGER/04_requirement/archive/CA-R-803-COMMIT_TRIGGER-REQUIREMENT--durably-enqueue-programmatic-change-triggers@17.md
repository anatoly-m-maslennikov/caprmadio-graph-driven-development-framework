---
subjects:
  declared:
    continuant:
      - feature-boundary
cce_version: cce_1
cce_form: obligation
version: 17
updated_at: 2026-08-23 16:16:20 +0400
---
# Durably enqueue programmatic change triggers

`COMMIT_TRIGGER` MUST accept a sealed action from an authorized MCP Atom mutation or a registered project-change adapter and durably enqueue exactly one trigger before returning successful intake. The trigger MUST preserve the repository identity, stable action identity, sealed Initiative, source-event identity, observation time, changed-target candidates, and expected subject revision or digest when one exists.

Any number of authorized trigger producers MAY enqueue concurrently. Repeated delivery of the same stable action or source-event identity MUST remain idempotent. Trigger acceptance MUST NOT gather full context, append a Journal, stage files, acquire the Git gate, or wait for a Git commit. A trigger that cannot establish its project boundary, Initiative, action identity, or required mutation provenance MUST fail without acknowledgment.
