---
atom_id: CA-O-174
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run complete tests"
  depends_on: [Workflow, Step, Action, Test, Applicable Methodology, Journal]
version: 2
updated_at: 2026-10-06 00:00:00 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the closed candidate unit gate

## Step

This Step invokes CA-O-168 once with phase `closed_unit_gate`, binding CA-O-173's complete compiled candidate Projection, frozen N/N+1/source bindings and the declared closed unit gate.

## Details

Focused, cached, host-only or historical results are not a substitute for this closed gate, and this closed gate is not substituted for CA-O-182 host Candidate E2E or CA-O-184 Full Gate aggregation. It completes before staging and cannot select N+1. A failed, blocked, unsafe, unavailable or unjournalable result stops before staging, image work, promotion or retirement and preserves actual evidence without retry.
