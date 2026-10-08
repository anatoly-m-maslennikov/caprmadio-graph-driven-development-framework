---
atom_id: CA-P-1612
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
subjects:
  governs: "Complete Content Role driven Atom status changes"
  depends_on: [Atom, Content Role, Status, Carrier, Workflow, Action, Tool, Journal]
version: 3
updated_at: "2026-10-08 04:07:03 +0400"
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1519, CA-P-1123, CA-P-1124, CA-P-1655]
---
# Summary

Complete Content Role driven Atom status changes

## Objective

Deliver Change Atom Status as one of the six FIRST CUT Workflows, for any Atom using the current applicable Content Role/Type status whitelist and defined Carrier folders. This remains an active bounded obligation, not a completion claim.

## Details

### Inputs

Existing CA-O-127 → CA-O-129 → CA-O-128; current status and Carrier-folder authority; selected change_atom_status route, lifecycle_intents.py, atom_operations.py and shared selected execution. Preserve currentness, identity, permissions, secrets, status-model and shared Workflow/Action Journal checks. The generic path already exists; supplied fixtures do not themselves prove all-role authority resolution.

### Output and ownership

Reuse the existing Workflow and Action. Resolve the current authoritative model, preserve lifecycle/identity rules and shared Run evidence, and provide independent proof for all declared Content Roles. No duplicate Workflow, Tool, manual status registry, unrelated harvest or structural-entity expansion. Scope Unit mutations, Revert, graph builders, standalone advanced Artifact/Journal queries, and automatic Release Version/prior-image retirement remain deferred from the FIRST CUT without deleting or relabeling their existing work.

## Definition of Done

CA-P-1613 → CA-P-1614 → CA-P-1615 → CA-P-1616, with explicit BLOCKS edges. Source/tests/registration alone do not close actual execution proof: retain passing all-role behavior, no-op/failure handling, and shared Journal lineage/terminal evidence, while keeping permission and runtime blockers truthful. This Plan neither requires nor claims a full-release or N+1 promotion gate.

