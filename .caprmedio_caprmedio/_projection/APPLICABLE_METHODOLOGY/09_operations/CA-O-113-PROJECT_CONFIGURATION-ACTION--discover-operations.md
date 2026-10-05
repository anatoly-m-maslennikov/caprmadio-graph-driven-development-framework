---
atom_id: CA-O-113
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 14:55:01 +0000"
subjects:
  governs: "Workflow and Action discovery"
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
  relates_to: [CA-R-1805, CA-D-513]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-113-PROJECT_CONFIGURATION-ACTION--discover-operations.md
  source_atom_id: CA-O-113
  source_atom_revision: 1
  source_sha256: b2f0fb072a13859902671561908fe6282c03ea35d3ef654fe985c67c5fb9a3db
  original_relations_sha256: d1fe0ed7e6499ac210ea978a45aab657c305c01331ee5b3a1e853069bdc63669
---
# Summary

Find Workflows and Actions by outcome

## Operation

Workflow and Action discovery **means** the Programmatic Action implementing the following responsibility:

- search carried Operations Type, Summary, Operation, Scope Unit, and declared implementation bindings; report unknown execution kind explicitly.
- accept the declared inputs **and** return the declared results under CA-D-513-DISCOVER_OPERATIONS--encode-discover-operations-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
