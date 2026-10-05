---
atom_id: CA-D-557
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 04:47:55 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source binding"
  depends_on: [Workflow, Step, Action, Tool, Implementation]
relations:
  delivery_for: [CA-R-1872]
---
# Summary

Bind Journal query source route to one Tool

## Scope

The one-route binding.

## Claim

The delivered Journal query Tool **must** bind CA-O-161, CA-O-163, and CA-O-162 as one route without defining a second Workflow, Action, or Journal.

## Details

```toml
[tool_binding]
name = "FIND_AND_FETCH_JOURNAL_EVENTS"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/find_and_fetch_journal_events.py"
action_ids = ["CA-O-162"]
workflow_ids = ["CA-O-161"]
mcp_name = "find_and_fetch_journal_events"
```

This discovery binding identifies the existing read-only Tool and its existing
MCP route. MCP and orchestrator registration remain separate delivery work;
the binding creates no Workflow, Action, Run, or Journal.
