---
atom_id: CA-P-1114
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 99
status: Active
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Atom"
    - "Evaluation"
    - "Implementation"
version: 1
updated_at: "2026-09-24 19:16:49 +0000"
relations:
  is_decomposition_of:
    - CA-P-1106
  blocks:
    - CA-P-1115
---
# Summary

Implement source-bound Atom checks

## Claim

the assigned AI Agent **must** implement current source-bound Property, section, Subject, Relation and projected-source checks with an independent coverage inventory.

## Definition of Done

the Plan is **not** Done **if** source-dependent checks lack exact authority bindings, unsupported obligations silently vanish, bad fixtures pass, good fixtures fail, or projected fidelity is inferred rather than checked.

## Details

- authority and validation adapters only; estimated 12 minutes, split further if necessary.
- use the source-bound input packet **in** `.caprmedio_tmp/implementation/validate-atoms-20260924`; current source Atoms remain authority. record evidence **without** editing unrelated work, weakening expected results, **or** promoting learned Methods inside this implementation Run.
