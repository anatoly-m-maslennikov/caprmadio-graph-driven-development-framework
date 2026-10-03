---
name: ca-project-settings
description: Check and regenerate the governed CAPRMEDIO Project Scope Unit Graph and Sources Projections from Project Configuration, admitted graph contributions, current graph structure, and Journal inputs. Use when the operator asks to build, update, refresh, synchronize, validate, or diagnose the current Scope Unit Graph or its exact sources.
---

# CA Project Scope Unit Graph

Use the registered Tools as the only writers of the two Project Scope Unit Graph Projections. Treat `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml` as the sole Carrier of current Operator-selected Project Configuration values. Treat applicable active RMED `project_scope_unit_graph` and `project_graph_state` contributions, current Project graph structure, and applicable Journal inputs as the only other admitted inputs.

## Workflow

1. Resolve the repository root containing `.caprmedio_framework/`, `.caprmedio_caprmedio/`, and `.caprmedio_runtime/`.
2. Treat check, inspect, validate, or currentness requests as read-only. Treat build, update, refresh, regenerate, or synchronize requests as authorization to update both Projections; semantic value changes still require an approved Configuration change.
3. Confirm that the current Project Configuration Revision Binding resolves through its completed governed-change receipt under `.caprmedio_caprmedio/work_journal/`. For a read-only request, report a missing or stale binding without mutation.
4. Run `python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py` from the repository root without `--apply`.
5. If it reports `changed=true` during an authorized update, repeat it with `--apply`. Never edit `.caprmedio_caprmedio/project_scope_unit_graph.projection.toml` or `.caprmedio_caprmedio/project_scope_unit_graph_sources.projection.toml` directly.
6. Repeat the read-only Tool command and require `changed=false`.
7. Report the exact Project Configuration Atom reference, Scope Unit Graph currentness, admitted-source count, changed outputs, and any rejected source.

## Maintain authority and generation

When an effective current Operator-selected value changes, update the Project Configuration Carrier through the applicable governed-change flow, record its exact current Revision Binding, then rebuild both Projections. When registered graph facts, defaults, or structural context change, update the applicable active RMED `project_scope_unit_graph` or `project_graph_state` contribution. When authority changes composition, TOML grammar, Map grammar, precedence, or validation mechanics, update the registered Tool implementation under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/`, release it through the separate Engine flow, and rebuild both Projections through this workflow. The installed Engine verifies execution compatibility; it never supplies governing authority.

Keep deterministic code in Tools. Treat the TOML Sources Projection as a versionless `map / implementation` Projection, not an Atom, authoring surface, or second Configuration carrier. Do not copy executable logic into this Skill, synthesize values without admitted authority, read a prior Projection as an input, or claim currentness after a failed or partial rebuild.
