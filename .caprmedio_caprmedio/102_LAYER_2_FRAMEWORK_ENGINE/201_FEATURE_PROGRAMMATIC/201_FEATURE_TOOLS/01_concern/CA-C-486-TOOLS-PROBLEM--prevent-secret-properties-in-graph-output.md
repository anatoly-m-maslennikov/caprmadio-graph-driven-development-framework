---
atom_id: CA-C-486
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
  governs: "Prevent secret properties in graph output"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1760]
---
# Summary

Prevent secret properties in graph output

## Concern

W11 serializes unrestricted source frontmatter properties into the Entities Graph, including secret-shaped keys.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py:1196` retains unrestricted properties and line 1510 serializes them. CA-O-134's secret boundary governs.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Reject unsafe source properties before publication; output and error reports must not contain the secret value.

CA-P-1760 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
