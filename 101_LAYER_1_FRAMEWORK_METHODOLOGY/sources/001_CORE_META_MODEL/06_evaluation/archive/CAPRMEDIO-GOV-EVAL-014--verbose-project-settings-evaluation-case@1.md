---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: medium
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
      - CAPRMEDIO-GOV-EVAL-013--canonical-toml-artifacts-evaluation-case
---

# Evaluation Case — Judge settings discoverability

Without implementation knowledge, cold readers must find every active setting,
accepted value, default, effect, and practical example in
`caprmedio_settings.toml`. They must correctly predict where to change an operator
preference and where to inspect project identity, topology, contracts, release
targets, or verification commands.

At least 90% of representative questions must be answered correctly, with no
authority-source error, no assumption that omitted settings are unavailable,
and no treatment of legacy `dset.toml` compatibility as a writable second
source.

This emitted Evaluation definition is immutable. Execution and evidence are
separate.

## Primary claim

Cold readers can configure DSET from caprmedio_settings.toml and correctly distinguish selectable behavior from project truth and governing definitions.
