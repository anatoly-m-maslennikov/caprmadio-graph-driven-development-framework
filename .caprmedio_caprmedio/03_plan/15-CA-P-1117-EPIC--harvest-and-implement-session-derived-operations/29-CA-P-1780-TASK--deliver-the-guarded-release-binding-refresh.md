---
atom_id: CA-P-1780
content_role: Plan
type: Plan
label: Task
work_sequence_number: 29
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 10:19:18 +0000"
subjects:
  governs: "Guarded Release binding refresh delivery"
  depends_on: [Manifest, Delivery, Evaluation, Journal, Operator, MCP]
relations:
  is_decomposition_of: [CA-P-1117]
  relates_to: [CA-C-496, CA-R-1882, CA-M-339, CA-E-582, CA-D-576]
  blocks: [CA-P-1717, CA-P-1721]
---
# Summary

Deliver the guarded Release binding refresh

## Objective

deliver and use the Operator-approved, source-first guarded refresh of the existing sixteen-route Release binding, without weakening ordinary admission or changing installed runtime N.

## Details

- root owns the RMED amendments, integration, exact Operator authorization and actual journaled publication. independently bounded worker lanes own refresh-base validation, trusted publication/recovery, regression proof and read-only review; each implementation or verification slice has an estimated duration <=15 minutes.
- R1882/M339/E582/D576 v3 govern the narrow same-route, same-identity pin refresh. preserve the initial fifteen-to-sixteen operation and historical sealed-intent normalization.
- normal discovery/dispatch/loading remain strict. the new private refresh validator is non-dispatching; it cannot admit route, query, registry, source-identity or occurrence changes.
- actual refresh follows an exact byte-preserving plan and trusted operation-specific Operator context, sealed pending intent, canonical carrier lock, atomic replacement, strict readback and canonical Journal finalization. if recording is uncertain, inspect the saved result before recovery; never replay the write.
- only after accepted refresh, resume the remaining Epic gates using a fresh source-bound Release Run through MCP. N5–N8 remain immutable historical evidence.

## Definition of Done

the amended source contract and implementation have independent acceptance; focused initial and refresh regression suites pass; the actual canonical binding is refreshed and strictly reopened; its Journal record is verified with no pending publication; installed N remains unchanged. this Task does not claim the complete Release gate or Epic closure.

## Pre-execution review

the Operator explicitly approved this guarded capability and its use after RMED. C496 identifies the confirmed missing refresh path; resetting or hand-editing the canonical binding is not an alternative. use the existing source-owned D572 derivation and lifecycle support rather than another registry or Journal.
