---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-REQU-395--verbose-project-settings
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-025--canonical-toml-artifacts-test-case
---

# Test Case — Validate verbose project settings

Tests must prove that new and bootstrapped repositories emit
`caprmedio_settings.toml` only; its defaults load without hidden fallback; each
registered value selects the documented behavior; invalid values fail with the
owning key; and the skill context exposes the selected strictness,
implementation mode, workspace default, and delegation budget profile.

The suite must also prove that a legacy root `dset.toml` remains readable,
that new writers never emit it, and that simultaneous legacy and canonical
files fail deterministically. Project manifests must no longer own Change
workspace or delegation budget selection, while continuing to own project
identity, topology, contracts, release, verification, and provenance facts.

Repository-wide reference checks must accept only deliberate immutable
historical references to the retired filename. Existing sealed atoms and
legacy Decision carriers must retain their recorded digests.

This emitted Test definition is immutable. Runs and evidence are separate.

## Primary claim

Deterministic tests prove the verbose settings filename, settings-manifest boundary, compatibility rules, selected behavior, bootstrap output, and immutable historical exceptions.
