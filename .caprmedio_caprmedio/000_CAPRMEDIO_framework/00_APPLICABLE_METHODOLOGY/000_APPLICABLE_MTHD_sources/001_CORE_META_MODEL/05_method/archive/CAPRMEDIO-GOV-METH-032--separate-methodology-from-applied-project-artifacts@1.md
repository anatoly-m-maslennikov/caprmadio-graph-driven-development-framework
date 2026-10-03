---
artifact_subtype: implementation_decision
subject_scopes:
  - methodology
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-REQU-409--recursive-root-directory-convention
      - CAPRMEDIO-GOV-REQU-404--framework-project-separation
---

# Decision — Separate methodology from applied project artifacts

The project-local DSET control plane uses three visibly distinct carriers:

```text
.caprmedio/000_caprmedio_methodology/   installed project-local DSET methodology
.caprmedio/100_project/            applied project-wide artifacts
.caprmedio/100_LAYER_1_META/         applied META artifacts
.caprmedio/200_LAYER_2_GOV/          applied GOV artifacts
.caprmedio/103_layer_tool/         applied TOOL artifacts
.caprmedio/104_layer_skill/        applied SKILL artifacts
.caprmedio/105_layer_ops/          applied OPS artifacts
.caprmedio/150_versions/           applied Version artifacts
```

The reusable DSET framework source remains a separate governed product surface
at the repository root:

```text
10_project/
11_layer_meta/
12_layer_gov/
13_layer_tool/
14_layer_skill/
15_layer_ops/
50_versions/
```

`000_caprmedio_methodology` contains governing rules, procedures, schemas,
templates, and workflow definitions. It never owns this project's Decisions,
Questions, Problems, QA atoms, evidence, or applied specifications and plans.

## Rationale

Methodology defines how the project works; applied artifacts record what this
project decides, plans, checks, and observes. Keeping those carriers in
separate numbered namespaces prevents framework rules from being mistaken for
project state while preserving deterministic local rule resolution for thin
skills.

## Primary claim

DSET stores the installed project-local methodology only under .caprmedio/000_caprmedio_methodology, stores applied project artifacts only under .caprmedio/100_project through .caprmedio/150_versions, and keeps the reusable framework source in the repository root's 10_project through 50_versions product structure.
