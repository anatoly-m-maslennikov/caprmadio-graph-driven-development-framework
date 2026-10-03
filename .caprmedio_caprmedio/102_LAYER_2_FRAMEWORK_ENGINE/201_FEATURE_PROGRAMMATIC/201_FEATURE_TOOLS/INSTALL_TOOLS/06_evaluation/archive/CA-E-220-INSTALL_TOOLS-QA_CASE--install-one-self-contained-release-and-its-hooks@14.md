---
subjects:
  governs: "Tool Installation"
  depends_on: []
version: 14
updated_at: 2026-09-15 03:15:32 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Install one self-contained release and its Hooks

## Claim checked

One apply installs a verified self-contained Tool release, stable launchers, one asynchronous Codex PostToolUse intake carrier, all three Git Hook phases, and registered background services without installing executable framework code into the Codex user directory.

## Test case

Install the complete canonical Tool source into a clean repository, inspect status and Hook configuration, invoke representative installed Tools, and load every installed executable entrypoint with canonical source absent from its import path.

## Acceptance criteria

Status verifies every installed digest, selected release, launcher, adapter, service registration, canonical Codex Hook fragment, merged user Carrier, local `caprmedio.codex-hooks = v1` activation, Git Hooks, and `core.hooksPath`. The generic Codex dispatcher resolves the repository at invocation time, requires activation, and addresses the stable runtime Tool launcher. Every installed executable loads without canonical source; persistent operational Carriers exist only below `.caprmedio_runtime/`; disposable staging, bytecode, cache, Evaluation, and atomic-write intermediate Carriers exist only below `.caprmedio_tmp/`; and `.caprmedio_install/` does not exist after successful migration.

## Failure disposition

Reject delivery if any Tool, dependency, Hook, or service registration is missing or duplicated; if a Hook addresses another location; if installed code imports outside its release; if disposable state enters runtime; if persistent operational state enters temporary state; or if the legacy installation root remains after successful migration.
