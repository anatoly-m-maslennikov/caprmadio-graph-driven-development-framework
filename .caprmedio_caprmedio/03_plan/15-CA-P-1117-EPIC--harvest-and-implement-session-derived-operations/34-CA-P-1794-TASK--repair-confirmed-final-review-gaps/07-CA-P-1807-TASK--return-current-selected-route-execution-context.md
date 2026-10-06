---
atom_id: CA-P-1807
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 18:28:00 +0000"
subjects:
  governs: "Selected route execution context"
  depends_on: [Tool, Workflow, Action, Projection, Source Carrier]
relations:
  is_decomposition_of: [CA-P-1794]
  relates_to: [CA-C-512, CA-R-1804, CA-R-1805, CA-R-1806, CA-D-514, CA-P-1800]
---
# Summary

Return current selected route execution context

## Objective

repair the discovery implementation so current admitted selected routes and their exact Operations definitions return truthful bounded context under existing authority.

## Details

- use the validated canonical manifest and actual exposed names; a source definition alone does not establish an executable binding.
- keep route-specific request schemas and disclose all matching bindings for a shared Action without choosing or executing one.
- preserve currentness, ambiguity, context-budget and explicit-gap behavior; do not add a new route, request protocol or permission grant.
- root owns source integration, actual MCP reload and rediscovery before freezing N13.

## Definition of Done

focused service/MCP regressions and independent review accept the bounded implementation; live route-name, Workflow-ID and shared Action-ID context requests return their current exact source bindings and truthful schemas without effects.
