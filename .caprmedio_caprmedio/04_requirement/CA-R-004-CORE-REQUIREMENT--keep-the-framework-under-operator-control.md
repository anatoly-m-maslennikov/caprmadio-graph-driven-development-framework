---
atom_id: CA-R-004
content_role: Requirement
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Core
global_tier: 1
status: Active
author: Anatoly Maslennikov
version: 18
updated_at: "2026-09-30 21:46:00 +0000"
relations:
  child_of:
    - CA-P-033
subjects:
  governs: "CAPRMEDIO Framework Instance/control"
  depends_on:
    - "CAPRMEDIO Framework Instance"
    - "Operator"
    - "Project"
---
# Summary

Keep the framework under Operator control

## Scope

**every** governed part of the CAPRMEDIO Framework Instance **in** **every** governed state, including **after** admissible instance changes.

## Claim

the CAPRMEDIO Framework Instance **must** keep **every** governed part of itself under the Operator's control **and** keep the Operator able **to** change the Project through that instance.

## Details

control remains available throughout admissible Framework Instance changes.
