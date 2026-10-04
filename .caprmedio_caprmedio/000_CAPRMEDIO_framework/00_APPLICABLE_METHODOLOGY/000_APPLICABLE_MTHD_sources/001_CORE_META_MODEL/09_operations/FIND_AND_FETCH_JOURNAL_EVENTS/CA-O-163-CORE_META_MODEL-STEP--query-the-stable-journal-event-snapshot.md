---
atom_id: CA-O-163
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:30:00 +0400"
subjects:
  governs: "Find and Fetch Journal Events/Step: query"
  depends_on: [Workflow, Step, Action, Journal, Event, Workflow Run, Action Run]
relations:
  relates_to: [CA-O-161, CA-O-162, CA-R-1861, CA-R-1866, CA-R-1867]
---
# Summary

Query the stable Journal Event snapshot

## Operation

This Step is the query node of CA-O-161 and invokes exactly one Action, CA-O-162, Query Journal Events.

### Inputs and parameters

Before Action dispatch, bind the selected Project's canonical `.caprmedio_<project name>/_journal/` Event carriers into one opaque snapshot token that identifies the complete ordered source frontier. Bind the literal filter expression, requested result mode (`ids`, selected `fields`, or `full_events`), selected fields when applicable, and bounded page request. The token's frontier excludes this invocation's later Run/Event records and remains fixed even if append occurs while the query is read.

## Details

The Step accepts no filename identity, secret-bearing selection, arbitrary SQL/code, mutation parameter, or fallback Journal root. A failed or incomplete Action returns its actual diagnostic and does not fabricate a successful Workflow or Action Run.
