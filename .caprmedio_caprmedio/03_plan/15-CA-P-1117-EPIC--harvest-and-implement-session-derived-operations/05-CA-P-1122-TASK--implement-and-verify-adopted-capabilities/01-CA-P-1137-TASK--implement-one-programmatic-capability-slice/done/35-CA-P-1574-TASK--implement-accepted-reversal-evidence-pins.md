---
atom_id: CA-P-1574
content_role: Plan
type: Plan
label: Task
work_sequence_number: 35
current_scope_unit: caprmedio
claim_target_scope_unit: REVERT_CHANGES
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Accepted native reversal evidence pin resolution"
  depends_on: [Operator, Action, Journal, Carrier, Evaluation]
version: 2
updated_at: "2026-10-04 23:52:49 +0000"
relations:
  is_decomposition_of: [CA-P-1568]
  blocks: [CA-P-1568, CA-P-1567, CA-P-1519]
---
# Summary

Implement accepted reversal evidence pins

## Objective

Within <=15 minutes after P1571 source ACCEPT, complete the existing safe native provider's exact evidence-currentness bindings.

## Details

- Dispatch remains blocked until P1571 accepts exact current D536 source bytes. Read accepted D536/R1833/E553/E554 and P1568's safe fail-closed result first.
- Own native_revert_provider.py, a narrow evidence reader if necessary, and directly affected native-provider/selected-provider focused tests only. Preserve the safe permission/path/budget/JSON/Event checks already implemented. No source, shared executor/backend, fixture, MCP, Plan, Journal or commit writes.
- Consume exactly the accepted current pin schema for governing-definition identity/revision, actual recorded Operator decision and executor permission, selected-change/history/before-after and affected references. Reobserve actual source/evidence at admission, pre-execution and before every effect. No fabricated authority, arbitrary resolver, duplicate Journal or inverse inference.
- Functional tests use real disposable current records and canonical Event evidence where declared. Prove current exact native reversal succeeds and post-admission revocation/change blocks before Action start or remaining effects. Coordinate the accepted fixture interface with P1567; use deterministic existing structural recovery for W10 if needed, not forecasted timestamp-dependent hashes.
- Inherit 90%; use apply_patch and preserve concurrent edits. No FPF, harvesting, paid Agent, permission bypass or live Project mutation. Root saves and records separate native/transport/image proof.

## Saved result

All accepted evidence pins now reobserve actual source/evidence at admission, pre-start and each effect. Exact recorded decision includes full ordered effects; same IDs with changed parameters are denied. Current combined Revert suites passed 24/24 and exact registered selected Revert case passed. Independent P1581 ACCEPT. Provider hash fcf61f100eb8fd194d3c066f23c82c5825249a3cbf9d5e0f849d5bbe975ace45. Two unrelated W09 startup tests are blocked by concurrently stale prompt bindings; no all-image claim.

## Definition of Done

Accepted evidence pins are implemented with passing bounded current/changed/revoked functional proof; native happy-path/image closure are never inferred from synthetic references.
