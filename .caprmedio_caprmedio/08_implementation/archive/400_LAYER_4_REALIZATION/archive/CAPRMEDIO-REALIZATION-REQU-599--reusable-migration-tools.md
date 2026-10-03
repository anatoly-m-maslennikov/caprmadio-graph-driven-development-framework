---
subject_scopes:
  - migrations
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-REALIZATION-REQU-582--local-python-tools-profile
  - type: relates_to
    targets:
      - CAPRMEDIO-REALIZATION-REQU-583--portable-dry-run-and-diagnostics
      - CAPRMEDIO-REALIZATION-REQU-584--place-and-explain-settings-and-constants
      - CAPRMEDIO-REALIZATION-REQU-598--apply-local-python-tools-profile
      - CAPRMEDIO-GOV-METH-004--bounded-scripted-migrations
---

# Requirement — Keep reusable migration tools

## Primary claim

Reusable migration executables belong to the IMPL `tools` scope under
`15_layer_implementation/tools/migrations`. The active toolkit contains only
portable, repeatable migrations and shared safety mechanisms; completed
schema-specific rewrites remain inert historical sources.

Every active migration:

- discovers or accepts its repository root instead of embedding a machine path;
- performs a mutation-free deterministic preview by default;
- requires explicit `--apply` before changing files;
- refuses unknown structures, path escape, symlink escape, collisions, and
  changed preimages;
- reports a stable plan digest that can bind preview to application;
- validates staged results before replacement and restores touched bytes after
  failure;
- verifies postconditions and produces no operations after successful
  reapplication; and
- uses portable Python filesystem and subprocess behavior across macOS,
  Windows, WSL, and Linux.

Executable entry points remain thin. Shared planning, digest, path-safety,
transaction, rollback, and verification behavior lives in reusable modules.
Migration-specific classification and rewriting remain bounded recipes.

Temporary transaction state belongs to `.caprmedio_runtime`; optional redacted
append-only execution logs belong to `.caprmedio_logs`. Neither location becomes
project authority.

## Rationale

One-off scripts are valuable during a cutover but unsafe as an implied public
toolkit. Extracting their proven safety mechanisms into a small migration
runtime preserves the useful work without promoting retired identities,
schemas, or repository layouts.
