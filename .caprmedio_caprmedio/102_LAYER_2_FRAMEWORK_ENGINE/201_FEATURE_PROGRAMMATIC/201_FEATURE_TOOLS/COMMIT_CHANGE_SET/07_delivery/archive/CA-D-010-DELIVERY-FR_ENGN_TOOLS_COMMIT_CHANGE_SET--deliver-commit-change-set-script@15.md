---
subject_scopes:
  - provenance
version: 15
updated_at: 2026-08-25 02:15:00 +0400
relations:
  delivery_for:
    - CA-R-805
    - CA-R-1121
    - CA-R-1124
    - CA-R-1064
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the canonical source script `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py` and its content-identical carrier in the selected `.caprmedio_install` release. It exposes the common Doer CLI in dry-run and authorized-MCP apply modes. It consumes only sealed peer results and MUST NOT import, invoke, schedule, or otherwise orchestrate `COMMIT_TRIGGER`, `COMMIT_CONTEXT`, or `APPEND_CHANGE_RECORDS`.

The script receives a durable outbox action, chooses it only while holding the repository-scoped lease and current fencing token, and revalidates the sealed Initiative, expected Git base, subject frontier, and complete target set immediately before staging, Git mutation, and result recording. An atomic real-change commit stages exactly one action target; a bulk commit stages all and only its frozen targets. Both use the Initiative-based message Projection and stage no Journal carrier. Journal append is a peer operation; a later Journal-only batch is a distinct gate item with only Journal carrier changes and the batch message form.

Dry run is mutation-free. Recovery reconciles any uncertain Git effect against the outbox and reachable Git history before retry. The installed script may expose read-only Git-hook validation and observation modes. Each synchronous `pre-commit` or `commit-msg` carrier performs only its required fail-closed Evaluation, and `post-commit` performs only its declared observation. Every carrier has an explicit measured latency threshold and timeout, stable exit semantics, and structured diagnostics. Broad repository scans, graph traversal, context gathering, Journal append, staging, commit creation, retry, lifecycle control, and background processing are prohibited inside these Hook processes; non-gating work is handed to changed-target or background execution.

No Git-hook mode creates a trigger, writes a Journal record, stages a path, or creates a commit. The modes reject staged installation, Runtime, Git-internal, mixed real-change/Journal, stale, or unfenced action boundaries. Codex automatic-commit intake remains a separate asynchronous carrier governed by `COMMIT_TRIGGER`.
