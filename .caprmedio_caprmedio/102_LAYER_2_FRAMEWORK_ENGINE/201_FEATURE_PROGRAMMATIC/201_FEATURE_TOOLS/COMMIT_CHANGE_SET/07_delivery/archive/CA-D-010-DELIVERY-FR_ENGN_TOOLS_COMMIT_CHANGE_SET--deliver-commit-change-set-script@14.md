---
subject_scopes:
  - provenance
version: 14
updated_at: 2026-08-23 16:45:00 +0400
relations:
  delivery_for:
    - CA-R-805
    - CA-R-1121
    - CA-R-1124
    - CA-R-1064
---
# Deliver the commit-change-set script

Realize `COMMIT_CHANGE_SET` through the canonical source script `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_CHANGE_SET/commit_change_set.py` and its content-identical carrier in the selected `.caprmedio_install` release. It exposes the common Doer CLI in dry-run and authorized-MCP apply modes and composes only peer code from that release.

The script receives a durable outbox action, chooses it only while holding the repository-scoped lease and current fencing token, and revalidates the sealed Initiative, expected Git base, subject frontier, and complete target set immediately before staging, Git mutation, and result recording. An atomic real-change commit stages exactly one action target; a bulk commit stages all and only its frozen targets. Both use the Initiative-based message Projection and stage no Journal carrier. Journal append is a peer operation; a later Journal-only batch is a distinct gate item with only Journal carrier changes and the batch message form.

Dry run is mutation-free. Recovery reconciles any uncertain Git effect against the outbox and reachable Git history before retry. The installed script may expose read-only Git-hook validation and observation modes, but neither mode creates a trigger, writes a Journal record, stages a path, or creates a commit. It rejects staged installation, runtime, Git-internal, mixed real-change/Journal, stale, or unfenced action boundaries.
