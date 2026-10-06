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
      - CAPRMEDIO-GOV-REQU-401--control-runtime-and-scratch-boundaries
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-EVAL-017--hidden-layout-interpretability
---

# Evaluation Case — Interpret the three state boundaries

Give independent reviewers a repository tree including hidden entries and the
governing description. Pass when they consistently identify:

- `.caprmedio/` as committed project control truth;
- `.caprmedio_runtime/` as ignored but resumable project-local operational state;
- `/tmp` on POSIX, or the native Windows temporary root, as disposable process
  scratch; and
- same-directory atomic swap state as a bounded publication mechanism rather
  than durable runtime or governance.

Record ambiguity instead of resolving it by majority vote. This Evaluation
atom is immutable; later correction requires a successor Evaluation and an
append-only lifecycle event.

## Primary claim

A reviewer can distinguish committed DSET control truth, ignored resumable runtime state, and disposable process scratch from the repository tree and governing text.
