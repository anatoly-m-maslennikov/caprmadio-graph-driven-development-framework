---
atom_id: "CA-R-1845"
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
  governs: "Implementation prompt agentic context"
  depends_on: ["Prompt", "Step", "Action", "Agent"]
relations:
  relates_to: [CA-O-091, CA-O-092, CA-O-093, CA-O-094, CA-O-095, CA-O-096, CA-O-099]
---
# Summary

Preserve agentic context and bounded handoffs

## Scope

Integrated and Isolated prompt invocation for the seven current Implementation Workflow Steps.

## Claim

the Implementation **must** use the Step's supplied Integrated or Isolated context before actual Agentic dispatch; Isolated work uses an assigned subagent with a complete handoff, a fresh admission, and one bounded P subtask estimated below fifteen minutes.

## Details

Unavailable, ambiguous, unsupported, or incomplete context blocks dispatch. A prompt returns its result and retained evidence to its caller; it neither auto-starts a successor nor grants permissions, changes Workflow state, or silently falls back between contexts.
