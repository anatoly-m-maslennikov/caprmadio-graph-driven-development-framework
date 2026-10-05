---
atom_id: "CA-D-544"
content_role: "Delivery"
type: "Delivery"
current_scope_unit: "PROMPTS"
claim_target_scope_unit: "PROMPTS"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
version: 1
updated_at: "2026-10-04 18:26:33 +0000"
subjects:
  governs: "Implementation Workflow prompt carriers"
  depends_on: ["Prompt", "Carrier", "Step", "Action"]
relations:
  relates_to: [CA-R-1843, CA-M-326]
---
# Summary

Deliver current Implementation Workflow prompt carriers

## Scope

the future reviewed prompt package at `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/`.

## Claim

the package **must** contain only `CA-O-091`, `CA-O-092`, `CA-O-093`, `CA-O-094`, `CA-O-095`, `CA-O-096`, and `CA-O-099` `.prompt.md` carriers, plus `README.md`, `source_bindings.json`, and `tests/`.

## Details

Each prompt header carries exact Step, Action, and context. This Delivery specifies future reviewed carriers and does not authorize changes to current prompt files.
