---
atom_id: CA-O-117
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
  governs: "Execution notifications"
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
  relates_to: [CA-R-1809, CA-D-517]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-117-PROJECT_CONFIGURATION-ACTION--watch-execution.md
  source_atom_id: CA-O-117
  source_atom_revision: 1
  source_sha256: 191ac3dafa96c103f8901dd8b2e4f7ffc4a435fcd6b27d071e28c7f21a28aac3
  original_relations_sha256: 63883dea412b083bcba96aa4c656c03f32da1f6070efd71c1e59b51c125e9fa4
---
# Summary

Wait for execution updates

## Operation

Execution notifications **means** the Programmatic Action implementing the following responsibility:

- compare snapshots of existing saved evidence; replay confirmed Journal updates after the cursor, await changes asynchronously, and distinguish unconfirmed event recording.
- accept the declared inputs **and** return the declared results under CA-D-517-WATCH_EXECUTION--encode-watch-execution-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
