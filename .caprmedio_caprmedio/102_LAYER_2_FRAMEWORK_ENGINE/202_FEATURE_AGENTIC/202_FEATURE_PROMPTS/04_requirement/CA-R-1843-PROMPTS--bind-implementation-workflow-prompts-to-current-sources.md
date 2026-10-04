---
atom_id: "CA-R-1843"
content_role: "Requirement"
type: "Requirement"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation Workflow prompt source currentness"
  depends_on: ["Prompt", "Workflow", "Step", "Action"]
relations:
  relates_to: [CA-O-016, CA-O-091, CA-O-092, CA-O-093, CA-O-094, CA-O-095, CA-O-096, CA-O-099]
---
# Summary

Bind implementation prompts to current Workflow sources

## Scope

the PROMPTS implementation of the current seven-Step CA-O-016 Implementation Workflow.

## Claim

the Implementation **must** dispatch a Step prompt only with current, fully read bindings for O016v11, O091v4/O092v3/O093v3/O094v4/O095v3/O096v3/O099v2 and O017v6/O018v6/O019v4/O020v5/O089v3/O024v11/O021v9.

## Details

`source_bindings.json` is derived review evidence, not authority. A changed, absent, mismatched, or partially read source blocks the affected prompt until independent PROMPTS RMED review refreshes its binding; changing a pin only to satisfy a check is forbidden.
