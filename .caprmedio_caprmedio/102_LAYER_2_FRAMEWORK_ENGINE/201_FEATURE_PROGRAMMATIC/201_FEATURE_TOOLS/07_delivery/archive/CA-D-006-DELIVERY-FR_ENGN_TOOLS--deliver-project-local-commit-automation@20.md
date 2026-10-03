---
subject_scopes:
  - provenance
version: 20
updated_at: 2026-08-23 13:21:41
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CA-R-1064
    - CA-R-1065
---
# Deliver project-local commit automation

Deliver the project-path flow through four peer Tool units: `COMMIT_TRIGGER`, `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and `COMMIT_CHANGE_SET`. The flow admits ordinary project files, Atom files, and non-empty folders from the Git-admitted project frontier. One folder action remains one Journal event set and one commit. Their canonical source carriers and shared libraries live under root `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS`. `INSTALL_TOOLS` publishes them with every other Tool in one content-addressed, digest-verified, self-contained release under `.caprmedio_install`; installed Tools import code and read the relation registry only from that release. Mutable state, caches, logs, and retained operational history occupy separate directories under `.caprmedio_runtime`. One user-level Codex Hook carrier dispatches every Codex task by its working directory only when the resolved repository carries the installer-set local activation marker, then delegates to that repository's installed launcher without containing independent framework implementation. Installed Git Hook launchers live under `.caprmedio_install/hooks/git` and are registered through repository-local `core.hooksPath`; they delegate the `pre-commit`, `commit-msg`, and `post-commit` boundaries to Evaluation modes of `COMMIT_CHANGE_SET`, so they do not create additional Tool units. `COMMIT_CHANGE_SET` exposes the complete dry-run and apply flow and composes the other peer interfaces without becoming their structural owner. The standalone interfaces remain available for deterministic inspection, bounded execution, and retry.

The integrated delivery exposes a replaceable Hook-adapter interface with explicit install, status, enable, disable, and uninstall controls. Each enabled adapter must declare its substrate boundary, stable source-event identity semantics, canonical LLM application name, and deterministic host-session UUID resolver; emit the canonical `COMMIT_TRIGGER` without classifying or mutating; and suppress pipeline-owned Journal and runtime-state writes through action correlation. A validated session value supplied by the invoking Skill or operator takes precedence over host discovery. The Codex adapter resolves the Hook payload session UUID, uses `PostToolUse` for immediate per-operation processing, and uses `Stop` only to reconcile eligible uncommitted changes missed since that session's `SessionStart` baseline. Every other LLM application adapter must register an equivalent explicit host interface and fail closed rather than infer a UUID from unrelated process state.

Operators may invoke each Tool manually. One integrated read-only status surface must report the enabled adapter, resolved LLM application and session UUID when available, current repository lease, pending or blocked action, last completed action, Git Hook registration, and deterministic recovery instruction without requiring specialist Hook or Git knowledge or manual inspection of runtime files. Trigger, context, structured Journal record set, ordered receipt set, lease token and disposition, deterministic message Projection, Git-boundary Evaluation result, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Trigger and context envelopes may carry `llm_session` and `occurred_at` ephemerally, but the delivery persists those values only in Journal events; Atom and Projection carriers receive no copy, and `.caprmedio_runtime` recovery state retains only identifiers and receipts that resolve the canonical Journal record.

Installation and removal of an adapter must preserve any pre-existing repository Hook behavior and restore the prior local `core.hooksPath` state when the managed Git Hook registration is removed. When a repository already declares a different local `core.hooksPath`, installation must fail closed with a stable conflict diagnostic and leave the configured path, referenced Hook carriers, adapter registry, and managed installation Hook directory unchanged; it must not silently replace, merge, copy, or back up that configuration. No delivery component writes backup copies, and no disabled or uninstalled adapter emits a trigger.
