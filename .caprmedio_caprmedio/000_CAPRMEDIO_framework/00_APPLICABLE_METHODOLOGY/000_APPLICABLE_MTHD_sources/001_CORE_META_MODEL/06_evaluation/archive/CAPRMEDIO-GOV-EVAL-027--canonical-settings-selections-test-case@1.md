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
      - CAPRMEDIO-GOV-REQU-396--artifact-naming-setting
      - CAPRMEDIO-GOV-REQU-397--artifact-creation-setting
      - CAPRMEDIO-SPEC-SKILLS-REQU-570--implementation-mode-setting
---

# Test Case — Validate canonical settings selections

The deterministic suite must prove defaults, every accepted value, invalid
value rejection, and selected runtime behavior for
`artifacts.subtype_in_names`, `artifacts.creation_strictness`, and
`workflows.implement.mode` in root `caprmedio_settings.toml`.

Bootstrap and adopter writers emit only the canonical filename and keys. A
legacy root `dset.toml` remains read compatibility only, dual roots fail, and
no writer extends the legacy surface.

This Test definition is immutable. Runs and evidence are separate.

## Primary claim

Deterministic tests prove that canonical settings keys select artifact naming, atom-creation strictness, and implementation preparation without legacy write paths.
