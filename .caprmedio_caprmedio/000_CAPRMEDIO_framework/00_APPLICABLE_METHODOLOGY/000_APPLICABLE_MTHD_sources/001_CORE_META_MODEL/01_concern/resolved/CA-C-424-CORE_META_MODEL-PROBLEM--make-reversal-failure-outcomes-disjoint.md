---
atom_id: CA-C-424
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 17:44:00 +0000"
subjects:
  governs: "Approved Change Reversal/Outcomes"
  depends_on: [Workflow, Step, Action, Plan]
relations:
  concern_about: [CA-O-131, CA-P-1450]
---
# Summary

Make reversal failure outcomes disjoint

## Concern

O131's failed and partial_failure predicates overlap for an uncertain first effect with zero confirmed effects.

## Evidences

Independent P1450 F1 read actual outcome rows: execution failure before any approved effect is confirmed matches failed, while uncertain completion matches partial_failure. O130 preserves the effect account but cannot make the Action's selected outcome deterministic.

## Blast radius

### Disposition

Done P1461 corrected O131v2's two outcome predicates. Independent P1463 passed known-zero, uncertain-zero and confirmed-partial cases and verified every other clause remained unchanged. This source overlap is resolved; no reversal execution is inferred.

P1461 makes known-zero-effect failure distinct from any uncertain/confirmed partial effect. Preserve current permission, history, references and Journal guards; re-review only changed outcome clauses. No runtime reversal was performed.
