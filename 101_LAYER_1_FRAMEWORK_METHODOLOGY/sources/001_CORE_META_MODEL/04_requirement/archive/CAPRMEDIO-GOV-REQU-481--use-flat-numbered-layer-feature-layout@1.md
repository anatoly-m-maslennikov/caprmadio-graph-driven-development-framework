---
subject_scopes:
  - layout
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-287--assign-each-feature-to-one-layer
---
# Use a flat numbered Layer–Feature layout

The `.caprmedio/` root contains the installed-framework boundary, project
settings, generated control carriers, numbered Layer scopes, and
`04_requirement/`. The project-level Requirement directory owns project
Principles and project Core and Standard Requirements. Its Standards define
concrete Layer scopes and Contracts between Layers. Other project-level
Content-role directories are not created, and every non-project semantic
carrier has exactly one Layer or Feature owner.

Directories materializing accepted Layer and Feature scopes are flat siblings and use these uppercase fixed-width grammars:

```text
<L>00_LAYER_<L>_<LAYER_NAME>/
<L><FF>_FEATURE_<FEATURE_NAME>/
```

`L` is the one-digit Layer order and is repeated in the Layer label because Layer order is mandatory in the visible carrier address. `FF` is the two-digit Feature order within that Layer from `01` through `99`. A Feature directory's first digit encodes its accepted parent Layer. Layer and Feature names use `UPPER_SNAKE_CASE`.

Directory names and placement encode accepted semantic scope identities but cannot establish, merge, or redefine them. PROJECT owns Layer scope authority, each Layer owns its Feature scope authority, and PROJECT Contracts own cross-Layer scope correspondence.

Every Layer and Feature scope materializes only the lowercase Content-role directories it uses:

```text
01_concern/
02_analysis/
03_plan/
04_requirement/
05_method/
06_evaluation/
07_delivery/
08_implementation/
09_ops/
```

Each admitted Atom lives in the role-local root or lifecycle subdirectory registered for its Content role. The role-specific lifecycle Requirements govern use of `drafts/`, `solved/`, `done/`, and `archive/`; placement is authoritative and is not repeated as embedded lifecycle metadata.

The canonical Layer and Feature structure is:

```text
100_LAYER_1_META/
200_LAYER_2_GOV/
300_LAYER_3_SPEC/
301_FEATURE_METHODOLOGY/
302_FEATURE_TOOLS/
303_FEATURE_SKILLS/
304_FEATURE_PROFILES/
305_FEATURE_ADAPTERS/
306_FEATURE_EVALUATION/
307_FEATURE_DOCUMENTATION/
400_LAYER_4_IMPLEMENTATION/
401_FEATURE_METHODOLOGY/
402_FEATURE_TOOLS/
403_FEATURE_SKILLS/
404_FEATURE_PROFILES/
405_FEATURE_ADAPTERS/
406_FEATURE_EVALUATION/
407_FEATURE_DOCUMENTATION/
500_LAYER_5_DELIVERY/
600_LAYER_6_OPS/
```

The installed framework boundary `000_caprmedio_framework/` is outside the Layer and Feature number space and is governed separately. Native source code, executable tests, skill packages, configuration, CI, and other Implementation remain in their prescribed repository locations outside `.caprmedio/`.
