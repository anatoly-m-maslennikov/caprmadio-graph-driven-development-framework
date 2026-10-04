---
atom_id: "CA-D-545"
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
  governs: "Implementation prompt input packet"
  depends_on: ["Prompt", "Carrier", "Method", "Evaluation"]
relations:
  relates_to: [CA-R-1844, CA-M-329]
---
# Summary

Deliver the implementation prompt input packet

## Scope

the invocation packet passed to one current Implementation Workflow prompt.

## Claim

the packet **must** carry current Workflow/Step/Action pins, P/DoD and owned paths, R/D targets, the verified active-M file, E checks, authority, permissions, confidence, retry accounting, assigned context, retained evidence, and Step-specific input.

## Details

Preparation may begin from a bounded request plus admitted authority, but it must produce or verify the M file before delegated work. A missing field produces the Step's blocked result.
