---
atom_id: CA-P-944
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Methodology Finalization Frontier
    occurrent:
      - Methodology Finalization Frontier Freeze
  depends_on:
    continuant:
      - Methodology Source
      - Applicable Methodology
version: 1
updated_at: 2026-09-03 21:28:22 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Freeze Methodology Finalization Frontier

**when** this Epic starts, **then** the Assignee **must** freeze the exact current authority, Carrier, Tool, test, **and** Projection frontier required to finalize the CAPRMEDIO Methodology **before** work starts in another active Epic.

## Scope

`((all Active RMEDO Atoms in CORE_META_MODEL) union (all Active RMEDO Atoms in LOCAL_CONFIGURATION) union (all Active RMEDO Atoms in INSTALLED_EXTENSIONS) union (the current APPLICABLE_METHODOLOGY output) union (all current methodology compiler, retrieval, Entity-graph, Subject-graph, validation, and test Carriers) union (all current Project Settings that select those Carriers))`

## Definition of Done

the Task is **not done if** (**any** in-scope source Carrier lacks its exact identity, revision, lifecycle location, repository-relative path, **and** digest **or** **any** selected Tool, test, Projection, **or** Project Setting lacks the same receipt **or** Draft, Archived, Done, Canceled, generated, Bootstrap-history, **or** runtime material is treated as source authority **or** the frontier does not distinguish CORE_META_MODEL, INSTALLED_EXTENSIONS, LOCAL_CONFIGURATION, **and** APPLICABLE_METHODOLOGY **or** another active Epic changes the frozen frontier **before** this Epic closes **or** uncertainty below 99 percent is resolved **without** the Operator).

## Details

freeze live working-tree bytes. treat INSTALLED_EXTENSIONS as a visible Methodology Source even when it contributes **`=0`** Active Atoms. record concurrent changes without absorbing unrelated work.
