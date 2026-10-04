---
atom_id: CA-D-538
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Carrier"
  depends_on: [Tool, Projection, Artifact]
relations:
  delivery_for: [CA-R-1835, CA-R-1836, CA-R-1837]
---
# Summary

Bind graph projection Tool carriers

## Scope

The declared existing Tool entrypoint and RMED packet for the two graph builders.

## Claim

The bounded packet **must** keep `GENERATE_ENTITY_GRAPH` as the single declared Tool carrier while exposing separate Entities and Terms graph namespaces.

## Details

```toml
[tool_binding]
name = "GENERATE_ENTITY_GRAPH"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py"
mcp_name = "generate_entity_graph"
graph_kinds = ["entities", "terms"]
```

This delivery binds no new source authority, executable grammar, database, schedule, or code change. Implementation remains gated on independent RMED review.
