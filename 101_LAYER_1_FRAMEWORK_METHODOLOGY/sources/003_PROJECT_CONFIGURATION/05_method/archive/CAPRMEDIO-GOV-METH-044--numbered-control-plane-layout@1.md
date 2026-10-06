---
artifact_subtype: implementation_decision
subject_scopes:
  - layout
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-GOV-METH-032--separate-methodology-from-applied-project-artifacts
      - CAPRMEDIO-GOV-METH-036--number-methodology-without-path-registry
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-201--canonical-layer-definitions
      - CAPRMEDIO-META-REQU-086--bounded-recursive-self-hosting
---

# Implementation Decision — Use the complete numbered control-plane layout

The installed project-local methodology lives only under:

```text
.caprmedio/000_caprmedio_methodology/
├── 00_project/
├── 01_meta/
├── 02_gov/
├── 03_tool/
├── 04_skill/
├── 05_implementation/
└── 06_ops/
```

Applied project authority lives only under:

```text
.caprmedio/
├── 100_project/
├── 100_LAYER_1_META/
├── 200_LAYER_2_GOV/
├── 103_layer_tool/
├── 104_layer_skill/
├── 400_LAYER_4_IMPLEMENTATION/
├── 600_LAYER_6_OPS/
└── 150_versions/
```

The reusable framework product source remains distinct at the repository root:

```text
10_project/
11_layer_meta/
12_layer_gov/
13_layer_tool/
14_layer_skill/
15_layer_implementation/
16_layer_ops/
50_versions/
```

Every committed descendant of `000_caprmedio_methodology` uses a stable,
zero-padded numeric prefix unique among its siblings. Materialization derives
these names deterministically and does not persist a source-to-installed path
registry.

## Primary claim

Installed methodology, applied project authority, and reusable framework source
use the complete numbered layouts above and remain distinct owners.

## Rationale

One complete layout replaces two partial artifacts whose layer lists no longer
matched the accepted META→GOV→TOOL→SKILL→IMPL→OPS flow.
