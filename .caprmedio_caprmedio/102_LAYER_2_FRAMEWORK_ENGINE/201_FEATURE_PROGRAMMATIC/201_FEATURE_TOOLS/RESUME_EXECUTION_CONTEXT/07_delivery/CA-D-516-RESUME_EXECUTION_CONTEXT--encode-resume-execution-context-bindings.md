---
atom_id: CA-D-516
content_role: Delivery
current_scope_unit: RESUME_EXECUTION_CONTEXT
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Tool/RESUME_EXECUTION_CONTEXT/Carrier"
  depends_on:
    - "Tool"
    - "Action"
    - "Workflow"
    - "Atom"
    - "Scope Unit"
    - "Implementation"
    - "Workflow Run"
    - "Journal"
relations:
  relates_to: [CA-O-116, CA-R-1808]
---
# Summary

Encode RESUME_EXECUTION_CONTEXT Tool binding

## Scope

the RESUME_EXECUTION_CONTEXT capability for Tool/RESUME_EXECUTION_CONTEXT/Carrier.

## Claim

the RESUME_EXECUTION_CONTEXT Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a supported Run ID; return original request, frozen selection and criteria bindings, pending check or fix work, saved handoffs, current-source observations, and recording blockers.

```toml
[tool_binding]
name = "RESUME_EXECUTION_CONTEXT"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RESUME_EXECUTION_CONTEXT/resume_execution_context.py"
action_ids = ["CA-O-116"]
mcp_name = "resume_execution_context"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
