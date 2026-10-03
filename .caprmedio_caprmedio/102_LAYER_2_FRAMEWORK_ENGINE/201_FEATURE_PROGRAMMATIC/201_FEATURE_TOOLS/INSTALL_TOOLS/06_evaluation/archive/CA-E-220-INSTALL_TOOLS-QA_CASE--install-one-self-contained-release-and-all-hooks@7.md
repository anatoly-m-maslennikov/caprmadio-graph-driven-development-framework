---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103

---
# Install one self-contained release and all Hooks

## Claim checked

One apply installs a verified self-contained Tool release, stable launchers, the enabled Codex adapter, all four Codex lifecycle boundaries, and all three Git Hook phases without installing executable framework code into the Codex user directory.

## Test case

Install the complete canonical Tool source into a clean repository, inspect status, invoke the common machine interface of representative installed Tools, and load every installed executable entrypoint with the canonical source absent from its import path.

## Acceptance criteria

Status verifies every installed digest, current release, launcher, adapter, canonical Codex Hook fragment, merged user carrier, removed recognized project-local carrier, local `caprmedio.codex-hooks = v1` activation, Git Hook, and `core.hooksPath`. The generic Codex Hook commands cover wildcard `PreToolUse`, wildcard `PostToolUse`, `SessionStart`, and `Stop`; resolve the repository at invocation time; require its activation marker; address its stable `commit-trigger` launcher; and contain no absolute project or release path. Status identifies host activation as requiring or depending on operator-controlled Codex review, representative Tool entrypoints return valid machine envelopes, every installed executable loads successfully, and `.caprmedio_install` contains no bytecode, cache, log, PID, or mutable runtime state.

## Failure disposition

Reject delivery if any Tool or dependency is missing, any Hook addresses another location, an installed Tool imports implementation outside its release, or mutable state enters the installation.
