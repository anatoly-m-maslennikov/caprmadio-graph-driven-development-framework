---
atom_id: CA-R-856
subject_scopes:
  - feature-boundary
version: 10
updated_at: 2026-08-23 15:33:04 +0400
---
# Install all FRAMEWORK_ENGINE Tools

`INSTALL_TOOLS` must be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS`, and realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/INSTALL_TOOLS/`. It must resolve every runnable Tool and shared implementation dependency from the canonical root `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS`, publish one digest-verified content-addressed release under `.caprmedio_install`, select that release through one machine-readable current manifest, and install every registered stable launcher and host Hook for the selected release. The Codex integration must merge one generic user-level dispatcher into the active Codex user Hook carrier while preserving unrelated Hook groups. The dispatcher must resolve the current repository at invocation time, require its installer-set local Git activation marker, and address its stable install-owned launcher rather than a repository-specific or content-addressed release path, so all Codex tasks can share one reviewed Hook identity without executing an uninstalled repository's lookalike carrier.

Installation must use dry-run unless apply is explicit, preserve pre-existing user-level Codex and default Git Hook behavior, reject an unrelated local `core.hooksPath` before mutation, migrate only recognized prior CAPRMEDIO project-local Hook carriers, and leave mutable execution state under `.caprmedio_runtime`. If a required host Hook carrier is unavailable, installation must fail with a stable diagnostic and restore the previously selected release and install-owned Hook fragment rather than leave a partially selected installation. No executable framework dependency may be installed into the Codex user directory. Installed Tools must remain runnable when the canonical source is not on their import path and must not create bytecode, logs, caches, PIDs, or mutable state below `.caprmedio_install`. Installation status must distinguish an installed Hook carrier from host activation and must state when the host requires one operator-controlled trust or review action that the installer cannot establish.
