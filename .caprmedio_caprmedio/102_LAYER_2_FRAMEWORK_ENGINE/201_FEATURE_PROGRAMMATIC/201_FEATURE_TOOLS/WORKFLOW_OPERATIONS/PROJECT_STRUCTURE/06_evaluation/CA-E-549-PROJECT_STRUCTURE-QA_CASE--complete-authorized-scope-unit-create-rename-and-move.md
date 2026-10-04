---
atom_id: CA-E-549
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:03 +0400"
subjects:
  governs: "Tool/PROJECT_STRUCTURE golden successful cases"
  depends_on: [Tool, Scope Unit, Project Structure, Workflow, Action, Journal]
relations:
  relates_to: [CA-R-1662, CA-R-1829, CA-R-1830, CA-R-1831, CA-R-1832]
---
# Summary

Complete authorized Scope Unit Create, Rename, and Move

## Scope

Golden functional cases against a disposable project with declared TOML authority and independently observed implementation paths, entered only through CA-D-527's shared service interface.

## Claim

The Evaluation **must** prove an authorized Create, Rename, and Move produce the expected tree and repaired reference sets through the real workflow boundary without constructing a second route envelope.

## Details

- Submit one complete CA-D-527 request with PROJECT_STRUCTURE route-specific `parameters` and omitted `mode`; assert the default service `preview`, a sealed preview receipt/proposal, no Run or Event identity, and no TOML, reference, or Carrier effect. The payload declares a valid Ordered Create with unique sibling `local_order`, nonempty label, correct structural level, nonnegative navigation number, separate paths, and an explicit direct-parent Goal-coverage disposition.
- Submit the authorized explicit `execute` through that same interface, using D527's current/pinned bindings and preview authorization. Create the unit, Rename it, and Move it under a valid parent; assert the service result and Run evidence separately from a `structural_result.state = completed`.
- Assert authoritative TOML changes, distinct authority/delivery paths, cycle-free declarations, correct explicit or inherited effective authority mode, repaired incoming references/parent-owned attachments, reported Carrier observations, and exact result revisions. Assert no unrelated Carrier is deleted and inspect shared Journal evidence only through its existing contract.
