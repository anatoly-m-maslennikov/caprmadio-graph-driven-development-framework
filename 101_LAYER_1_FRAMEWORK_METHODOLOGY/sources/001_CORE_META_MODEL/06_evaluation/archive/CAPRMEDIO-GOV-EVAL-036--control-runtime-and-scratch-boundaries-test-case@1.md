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
      - CAPRMEDIO-GOV-REQU-401--control-runtime-and-scratch-boundaries
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-035--hidden-project-control-root-test-case
---

# Test Case — Verify control, runtime, and scratch boundaries

Run layout, settings, bootstrap, runtime, session, migration, distribution,
self-host, cross-platform, and full repository tests. Prove that:

1. current governed state resolves only below `.caprmedio/`;
2. resumable run, session, readiness, cache, and recovery state resolves below
   ignored `.caprmedio_runtime/` and never becomes project authority;
3. POSIX scratch workspaces use `/tmp` even when ambient `TMPDIR` points at the
   repository;
4. native Windows scratch workspaces use the native system temporary root;
5. normal and handled-failure paths delete their scratch workspaces;
6. self-hosting and bootstrap leave no `dset-*` scratch directory in the
   repository; and
7. same-directory atomic-publication staging is bounded to the transaction and
   cannot survive its return path.

The complete recursive verifier must pass after bootstrap and generated views
are refreshed. This Test atom is immutable; later correction requires a
successor Test and append-only lifecycle event.

## Primary claim

Deterministic tests prove distinct control, runtime, scratch, and atomic-publication boundaries without repository scratch leakage.
