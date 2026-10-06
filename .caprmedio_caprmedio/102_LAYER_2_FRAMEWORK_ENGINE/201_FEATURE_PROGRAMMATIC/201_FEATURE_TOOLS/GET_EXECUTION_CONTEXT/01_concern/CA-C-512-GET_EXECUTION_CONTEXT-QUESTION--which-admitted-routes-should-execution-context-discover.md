---
atom_id: CA-C-512
content_role: Concern
type: Question
current_scope_unit: GET_EXECUTION_CONTEXT
local_tier: Standard
global_tier: 14
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 18:28:00 +0000"
subjects:
  governs: "Tool/GET_EXECUTION_CONTEXT"
  depends_on: [Tool, Workflow, Action, Source Carrier, Projection, Operator]
relations:
  concern_about: [CA-P-1807, CA-R-1804, CA-R-1805, CA-R-1806, CA-D-514]
---
# Summary

Which admitted routes should execution context discover

## Concern

live Create and Update context requests fail despite their current admitted MCP bindings; only Release Version is synthesized into the discovery catalog. a shared Action request expands the whole RMED scope and exceeds its context budget.

## Evidences

the live MCP reproduces generic context errors for create_atom and update_atom. the read-only source helper raises Unknown or ambiguous capability for create_atom; Release Version returns current revision-9 bindings. O128 v4 is read correctly but its broad same-scope expansion returns incomplete context.

## Blast radius

discovery and context retrieval for the existing sixteen selected capabilities. this does not authorize new routes, Action effects, or a release result.

## Decision

apply existing R1804, R1805 and R1806: expose every currently validated and registered selected route in discovery, return its route-specific input schema, and keep admitted Action context bounded to its exact source and actual bindings. disclose all bindings for a shared Action rather than selecting one route or granting dispatch authority. preserve explicit gaps and fail-closed stale-source behavior.

## Result

the bounded implementation and independent regression review are pending under P1807. installed N and historical evidence remain unchanged.
