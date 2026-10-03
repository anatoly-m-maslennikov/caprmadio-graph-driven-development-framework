---
subject_scopes:
  - feature-boundary
version: 7
updated_at: "2026-08-23 11:37:28"
relations:
  method_for:
    - CA-R-856
---
# Install one verified Tool release

Inventory every eligible regular file below the canonical Tool source, excluding tests, caches, bytecode, and host metadata; bind its relative path, content digest, and executable mode into one release digest; stage the complete release; verify its manifest and every copied byte; then atomically select it through `.caprmedio_install/current.toml`.

Before apply, retain the current selection manifest and canonical Codex Hook fragment in memory. After selection, register the enabled Codex adapter; set repository-local Git configuration `caprmedio.codex-hooks = v1`; merge `PreToolUse` and `PostToolUse` groups with the valid full-value regular-expression matcher `.*`, plus `SessionStart` and `Stop` dispatcher groups, into the user-level Codex Hook carrier; register Git `pre-commit`, `commit-msg`, and `post-commit` Hooks; and install stable Tool launchers. Never use the invalid bare quantifier `*` as a regular-expression matcher. If a required user Hook carrier cannot be updated, restore the retained selection and fragment, restore the previous Git Hook registration and recognized project-local carrier, and report `host-hook-carrier-unavailable`. Each generic Codex command resolves the current Git root, requires that exact activation marker, exits without effect when the marker or executable `.caprmedio_install/bin/commit-trigger` is absent, and otherwise delegates to that launcher. Remove recognized managed groups from the former project-local Codex carrier without changing unrelated project groups. Reinstallation reuses an identical release or selects a new digest, rewrites the launcher behind its stable address, and preserves the generic Codex Hook definition byte-for-byte when its behavior contract is unchanged. Report Codex host activation as operator-reviewed external state rather than infer it from carrier presence. Remove only recognized obsolete CAPRMEDIO installation and Hook directories from `.caprmedio_runtime` after the new installation verifies.
