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
      - CAPRMEDIO-GOV-REQU-399--slim-project-control-layout
---

# Test Case — Verify the slim project control layout

Run layout, settings, bootstrap, governance, carrier-transition, link,
classification, traceability, and full repository tests. Prove that:

1. current discovery selects only `dset/caprmedio_settings.toml` and schema 1.3;
2. fixed layer roots are direct children of `dset/`;
3. project-wide and Version artifacts resolve through `project/` and
   `versions/`;
4. initialization emits that layout and passes repository validation without a
   follow-up migration;
5. competing current/legacy configuration carriers fail closed; and
6. every immutable relocation remains byte- and Git-source-verifiable.

This Test atom is immutable. Later correction requires a successor Test and an
append-only lifecycle event.

## Primary claim

Deterministic tests prove schema 1.3 discovery, single-config ownership, direct layer roots, project and Version roots, initialization, relocation integrity, and rejection of competing legacy carriers.
