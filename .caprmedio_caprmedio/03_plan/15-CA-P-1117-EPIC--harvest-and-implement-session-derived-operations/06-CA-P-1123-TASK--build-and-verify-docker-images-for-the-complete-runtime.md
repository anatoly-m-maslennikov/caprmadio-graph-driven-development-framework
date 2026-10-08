---
atom_id: CA-P-1123
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 6
updated_at: "2026-10-08 00:11:25 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1655
    - CA-P-1173
    - CA-P-1124
    - CA-P-1147
---
# Summary

Build and verify Docker images for the complete runtime

## Objective

Build and functionally verify a Docker image for the FIRST CUT only: Create Atom, Update Atom, Replace Atom, Change Atom Status, the Implementation Workflow, and Build Applicable Methodology. Verify their required existing orchestrator and stdio MCP paths, shared Workflow/Action Journal evidence, and the actual loopback HTTP MCP path governed by CA-P-1757.

Exercise image-based mutation, no-op and required failure paths on a controlled mock Project. Preserve explicit permissions, secret isolation, currentness, identity, status-model and Journal-evidence checks. A successful image build or host-only test is insufficient; runtime Project-data mounts are allowed, but undeclared host implementation mounts and baked secrets are not.

## Details

### Docker and MCP boundary

The actual Docker HTTP MCP proof binds authenticated initialize/list/call, health, and lifecycle behavior on an explicit loopback port using an ephemeral test token. Invalid credentials, Host and Origin must fail before tools; stdio compatibility must remain usable. Retain image identity, Run/Action IDs and bounded result evidence.

This Plan preserves the existing global RMED formal Release gates without executing or weakening them. FIRST CUT acceptance is not a full-release or N+1 promotion claim and does not invoke the all-sixteen inventory or automatic Release Version/prior-image retirement. Scope Unit mutations, Revert, graph builders, and standalone advanced Artifact/Journal query delivery remain deferred. Their existing code, history and status are retained without falsely marking them done or deleting them.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its child files partition the current image/runtime checks and HTTP Docker proof. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

### Definition of Done

This Plan is not Done unless the six named Workflow paths have passing current-image functional evidence; required stdio MCP/orchestrator compatibility and shared Workflow/Action Journal lineage and terminal results are retained; and CA-P-1757 supplies actual authenticated loopback Docker HTTP MCP evidence. Failures, no-ops, invalid credentials/Host/Origin, permissions, secrets, currentness, identity and status-model checks must be proved as applicable. Deferred capabilities and unchanged formal Release gates are not FIRST CUT completion criteria.
