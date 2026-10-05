---
atom_id: CA-O-112
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
  governs: "Tool discovery"
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
  relates_to: [CA-R-1804, CA-D-512]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-112-PROJECT_CONFIGURATION-ACTION--discover-tools.md
  source_atom_id: CA-O-112
  source_atom_revision: 1
  source_sha256: 6f0b9eaaa3d69011259f1c6f8c5f07da670988092eab2a1b5407c798d60764c2
  original_relations_sha256: 2546a899cd4c6c82eb55e6cb5fafe4bcc76d8fddae0ac1cd4f3107b0135324b1
---
# Summary

Find Tools by capability

## Operation

Tool discovery **means** the Programmatic Action implementing the following responsibility:

- search declared Tool bindings and observed entrypoints; keep implemented, MCP-exposed, source-only, missing, and unresolved bindings distinct.
- accept the declared inputs **and** return the declared results under CA-D-512-DISCOVER_TOOLS--encode-discover-tools-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
