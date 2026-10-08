---
atom_id: CA-C-487
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Bind graph Run evidence to actual recording"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1760]
---
# Summary

Bind graph Run evidence to actual recording

## Concern

Graph construction accepts caller-provided confirmed receipt strings; selected execution must not use them as proof of actual same-invocation recording.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py:1464,1651` accepts caller receipt strings, and the selected executor records Action execution later. CA-O-133 and CA-R-1728 require actual Run recording.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Use genuine Action start recording before effects and terminal recording afterward; preserve unrecorded facts as pending without effect replay.

CA-P-1760 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
