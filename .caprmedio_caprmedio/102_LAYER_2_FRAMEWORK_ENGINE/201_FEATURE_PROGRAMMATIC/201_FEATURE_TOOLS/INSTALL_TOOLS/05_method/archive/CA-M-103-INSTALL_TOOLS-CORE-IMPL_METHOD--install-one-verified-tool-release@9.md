---
subjects:
  declared:
    continuant:
      - feature-boundary
version: 9
updated_at: 2026-08-25 01:49:10 +0400
relations:
  method_for:
    - CA-R-856
---
# Install one verified Tool release

Inventory every eligible regular file below the canonical Tool source, excluding tests, caches, bytecode, and host metadata; bind its relative path, content digest, and executable mode into one release digest; stage the complete release; verify its manifest and every copied byte; then atomically select it through .caprmedio_install/current.toml.

Before apply, retain the current selection manifest and canonical Codex Hook fragment in memory. After selection, register the enabled Codex adapter; set repository-local Git configuration caprmedio.codex-hooks = v1; merge exactly one asynchronous PostToolUse command group with matcher .* and async: true into the user-level Codex Hook carrier; register the independent Git pre-commit, commit-msg, and post-commit Evaluation Hooks; install stable Tool launchers; and register enabled background services. Do not install automatic-commit PreToolUse, SessionStart, or Stop groups.

Each generic Codex command resolves the current Git root, requires the exact activation marker, exits without effect when the marker or executable installed commit-trigger launcher is absent, and otherwise delegates to that launcher. The command performs only durable event intake. Remove recognized managed groups from former CAPRMEDIO Hook carriers without changing unrelated groups. Reinstallation reuses an identical release or selects a new digest and preserves an unchanged generic Hook definition byte-for-byte.

If a required Hook carrier, launcher, Git Hook, service registration, or release verification fails, restore the retained selection, Hook fragment, Git Hook registration, activation marker, and service registry selection; report one stable diagnostic; and leave no partially selected installation. Report Codex host activation as operator-reviewed external state rather than infer it from carrier presence.
