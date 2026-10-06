---
subject_scope: layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-475--repeat-ordered-role-folders-in-every-scope
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-111--nine-content-roles-with-plan
      - CAPRMEDIO-META-REQU-116--use-nouns-for-content-role-names
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
      - CAPRMEDIO-REQUIREMENT-META-109
      - CAPRMEDIO-GOV-REQU-313--govern-catalog-map-and-hub-projections
---

# Requirement — Repeat CAPRMEDIO role folders in every scope

The `.caprmedio/` root is the implicit project scope. Every project scope and
configured descendant `scope_path` uses the same ordered Content-role folders:

```text
01_concern/
02_analysis/
03_PLAN/
04_REQUIREMENT/
05_METHOD/
06_EVALUATION/
07_DELIVERY/
08_IMPLEMENTATION/
09_ops/
```

The folder labels use the canonical noun role names. Their numbers express the
CAPRMEDIO navigation order only; they do not establish authority, priority,
dependency, lifecycle state, or permission to skip an applicable role.

Every CAPRMEDIO Atom, Journal, or Projection carrier is placed in the folder
matching its derived Content role. Native project carriers such as source code,
executable tests, configuration, packages, documentation, and CI workflows
remain in their prescribed project locations outside `.caprmedio/` and are not
copied into the Implementation role folder.

For Atoms, active carriers live directly in the role folder, mutable
pre-admission candidates live under `drafts/`, and inactive admitted carriers
live unchanged under `archive/`. Journals and Projections retain their own
change rules.

Role folders are materialized only when needed. An absent folder is an empty
canonical role slot. Installed external methodology and runtime state remain
outside the governed project-role surface under their separately governed
boundaries.

## Primary claim

Every CAPRMEDIO structural scope repeats the ordered `01_concern` through
`09_ops` role surface while native Implementation remains in project-owned
locations outside `.caprmedio/`.

## Rationale

The recursive folder surface makes the nine-role order visible without
confusing the Implementation governance slot with the actual project
realization.
