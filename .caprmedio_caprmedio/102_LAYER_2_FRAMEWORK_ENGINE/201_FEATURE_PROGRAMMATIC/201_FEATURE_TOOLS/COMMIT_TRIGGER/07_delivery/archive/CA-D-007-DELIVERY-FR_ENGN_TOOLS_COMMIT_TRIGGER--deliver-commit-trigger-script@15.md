---
subject_scopes:
  - feature-boundary
version: 15
updated_at: 2026-08-23 16:40:00 +0400
relations:
  delivery_for:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CA-R-1124
    - CA-R-1064
---
# Deliver the commit-trigger script

Realize `COMMIT_TRIGGER` through the canonical source script `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/COMMIT_TRIGGER/commit_trigger.py` and its content-identical carrier in the selected `.caprmedio_install` release. `INSTALL_TOOLS`, not `COMMIT_TRIGGER`, owns Tool and Hook installation. `COMMIT_TRIGGER` exposes the common Hook CLI contract, implements registered Hook adapters without embedding substrate-specific meaning into the canonical trigger, and hands an accepted trigger unchanged to the `COMMIT_CHANGE_SET` end-to-end interface.

The user-level Codex host carrier is one generic dispatcher shared by Codex tasks. Its `PreToolUse` and `PostToolUse` groups use the valid full-value regular-expression matcher `.*`, not the invalid bare quantifier `*`, so every Codex tool name can reach the callbacks. It resolves the Git root from the Hook working directory, requires the exact repository-local `caprmedio.codex-hooks = v1` activation written by `INSTALL_TOOLS`, exits without effect when the marker or installation is absent, and otherwise invokes the stable install-owned `commit-trigger` launcher, which resolves only the release selected by `.caprmedio_install/current.toml`. Its command identity contains neither a repository-specific absolute path nor a release digest. The before-event callback may write one reconstructible runtime frontier snapshot keyed by the Codex session and tool-use identities; its matching after-event callback consumes and removes that snapshot, emits the canonical trigger without semantic classification, passes the unchanged trigger to `COMMIT_CHANGE_SET`, and records only reconstructible runtime completion or failure diagnostics.

The session-start callback writes one reconstructible session frontier below `.caprmedio_runtime`. The frontier contains Git-tracked paths and untracked paths admitted by current Git ignore rules. It excludes every top-level dot-directory except `.caprmedio`; `.caprmedio_runtime` and `.caprmedio_install` are therefore never logger subjects. The stop callback compares the baseline with the current frontier, ignores carriers whose working bytes already equal Git `HEAD`, and passes each unambiguously attributable missed change through the same trigger and downstream flow. Multiple changed entries under one unambiguous non-root folder in the same callback produce one folder trigger, not one trigger per entry. A successful immediate commit refreshes the session frontier. A stop callback with no baseline or ambiguous concurrent ownership reports a stable non-mutating diagnostic instead of adopting existing dirty work. These host-transport effects do not alter the trigger, establish governed meaning, or give `COMMIT_TRIGGER` ownership of context gathering, Journal append, commit, or installation semantics.

Adapter installation and removal must preserve pre-existing repository Hook behavior. Installation must refuse a different pre-existing local `core.hooksPath` with a stable diagnostic and zero configuration or Hook-carrier mutation. When no conflicting path exists, it registers the managed installation Hook directory and chains any executable default `.git/hooks` carrier before the managed Evaluation.
