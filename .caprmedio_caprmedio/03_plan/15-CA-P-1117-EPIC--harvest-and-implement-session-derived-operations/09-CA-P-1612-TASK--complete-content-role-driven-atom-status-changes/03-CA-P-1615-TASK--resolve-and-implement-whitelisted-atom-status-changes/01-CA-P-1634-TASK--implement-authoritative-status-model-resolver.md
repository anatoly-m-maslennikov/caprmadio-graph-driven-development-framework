---
atom_id: CA-P-1634
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Implement authoritative status model resolver"
  depends_on: [Atom, Content Role, Status, Carrier, Tool, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 02:36:46 +0000"
relations:
  is_decomposition_of: [CA-P-1615]
  blocks: [CA-P-1637]
---
# Summary

Implement authoritative status model resolver

## Objective

Within <=15 minutes, implement authoritative status model resolver.

## Details

New authoritative_status_models.py only; active current source Role/Type declarations are the sole domain authority. Most-specific Type overrides role fallback; retain exact casing and source pins, and reject missing/ambiguous/stale/forged models. Coordinate with P1635 test author; no existing lifecycle file changes.

Inputs: accepted CA-P-1633 source packet and current saved lifecycle inputs; current default role domains, R1825@3/E545@2 and D565@1. Host/image gates C449 and relocation gate C447 remain unchanged. The existing development worker can run focused development tests, not immutable-image proof.

## Definition of Done

The pure read-only resolver passes accepted current model and refusal golden cases, or returns a precise unfinished result. No runtime/image or complete integration claim.

