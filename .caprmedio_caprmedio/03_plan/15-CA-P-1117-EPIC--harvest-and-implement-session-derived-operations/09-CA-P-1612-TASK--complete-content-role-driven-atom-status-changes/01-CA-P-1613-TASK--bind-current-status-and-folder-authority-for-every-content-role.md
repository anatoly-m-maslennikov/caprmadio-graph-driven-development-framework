---
atom_id: CA-P-1613
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Bind current status and folder authority for every Content Role"
  depends_on: [Atom, Content Role, Status, Carrier, Workflow, Action, Tool, Journal]
version: 1
updated_at: "2026-10-05 01:04:37 +0000"
relations:
  is_decomposition_of: [CA-P-1612]
  blocks: [CA-P-1614]
---
# Summary

Bind current status and folder authority for every Content Role

## Objective

Within <=15 minutes, bind the current authoritative status whitelists and Delivery folder mappings to the existing Change Atom Status Workflow and necessary Tool RMED. Correct only demonstrated source gaps; reuse existing definitions instead of creating duplicate status authority.

## Details

### Inputs

All applicable Content Role and specialized Type status definitions and Carrier folder rules in methodology; CA-O-127/129/128 and current status Tool RMED. Record exact source IDs/Versions/paths/hashes and whether any definition is missing.

### Output and ownership

One coherent O/RMED packet explaining how the implementation resolves current status/folder authority for any Atom, including Drafts and current identity rules. Defined same-status no-op, invalid/missing model, collision, history/reference diagnostics and shared recording boundaries remain explicit.

## Definition of Done

Exact source pins and destination ownership support independent CA-P-1614 review. Ask unresolved material choices below90%; do not silently invent whitelist values, folder policies, mandatory transition restrictions or a second authoritative registry.
