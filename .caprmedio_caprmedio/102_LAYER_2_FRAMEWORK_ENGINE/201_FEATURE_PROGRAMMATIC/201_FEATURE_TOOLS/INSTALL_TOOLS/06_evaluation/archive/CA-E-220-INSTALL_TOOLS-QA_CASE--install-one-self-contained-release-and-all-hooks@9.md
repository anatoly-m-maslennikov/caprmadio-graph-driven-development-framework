---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 9
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
---
# Install one self-contained release and its Hooks

## Claim checked

One apply installs a verified self-contained Tool release, stable launchers, one asynchronous Codex PostToolUse intake carrier, all three Git Hook phases, and registered background services without installing executable framework code into the Codex user directory.

## Test case

Install the complete canonical Tool source into a clean repository, inspect status and Hook configuration, invoke representative installed Tools, and load every installed executable entrypoint with canonical source absent from its import path.

## Acceptance criteria

Status verifies every installed digest, selected release, launcher, adapter, service registration, canonical Codex Hook fragment, merged user carrier, local caprmedio.codex-hooks = v1 activation, Git Hooks, and core.hooksPath. Exactly one generic Codex PostToolUse command group has matcher .* and async: true, resolves the repository at invocation time, requires activation, and addresses the stable installed commit-trigger launcher. No automatic-commit PreToolUse, SessionStart, or Stop group exists. Every installed executable loads without canonical source, and .caprmedio_install contains no mutable state.

## Failure disposition

Reject delivery if any Tool, dependency, Hook, or service registration is missing or duplicated; if a Hook addresses another location; if automatic-commit synchronous lifecycle groups remain; if installed code imports outside its release; or if mutable state enters the installation.
