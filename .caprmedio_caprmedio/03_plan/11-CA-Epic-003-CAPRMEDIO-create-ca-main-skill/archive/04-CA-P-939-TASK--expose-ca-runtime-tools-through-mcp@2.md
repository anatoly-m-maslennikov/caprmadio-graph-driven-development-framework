---
atom_id: CA-P-939
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - CA MCP Surface
      - Project-local Provider-neutral MCP Service
    occurrent:
      - CA MCP Exposure
version: 2
updated_at: 2026-09-02 00:43:03 +0400
autonomous_confidence_threshold: 99
relations:
  depends_on:
    - CA-P-938
---
# Expose CA Runtime Tools Through MCP

**when** CA-P-938 is Done, **then** the Assignee **must** expose the admitted CA runtime Tools through one provider-neutral MCP discovery, schema, dispatch, and result-transport surface.

## Scope

`((CA Deterministic Routing Runtime Tool Set) union (CA Asynchronous Lifecycle Runtime Tool Set) union (canonical MCP source, endpoint projection, transport validation, tests, installation metadata, and model-readable results))`

## Definition of Done

the Task is **not done if** (MCP omits an admitted CA Tool, exposes an inactive or invalid Tool, changes Tool identity or meaning, duplicates routing or lifecycle mechanics, performs an effect outside the Tool gate, or reports durable submission as completed worker execution **or** discovery, input schemas, structured outputs, explicit failure states, cancellation, status inspection, and receipt retrieval are incomplete **or** the Project-local Provider-neutral MCP Service is not admitted as **`=1`** current Implementation result with its exact identity, native target, revision **or** digest, governing Requirement frontier, and current-realization evidence **or** headless MCP conformance and end-to-end Tool delegation tests fail).

## Details

keep MCP limited to provider-neutral discovery, transport validation, delegation, and result transport. preserve the distinction among accepted, queued, running, stopped, failed, completed, and reconciled states. admit the one current service realization before any Consumer Job or Demand refers to it as a produced Implementation result.
