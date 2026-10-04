---
atom_id: CA-C-423
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
  governs: "Atom lifecycle/Assessment scope"
  depends_on: [Workflow, Step, Action, Plan]
relations:
  concern_about: [CA-O-127, CA-O-128, CA-O-129, CA-O-145, CA-P-1452]
---
# Summary

Bound lifecycle assessment to one target

## Concern

Bulk Update is admitted without a complete per-target O067 assessment frontier.

## Evidences

P1452 directly read O128v1/O145v1/O129v1 and O067v6: single assessment describes only its supplied proposal/identified Revision. A second target with different meaning or Summary change cannot be classified by the first result.

## Blast radius

### Disposition

Done P1462 restricts lifecycle invocation to one target while preserving complete Carrier sets and multiple replacement successors. Independent P1464 passed all four v2 sources with exact case/delta evidence. The bulk-assessment defect is resolved; runtime remains unimplemented.

P1462 restricts each lifecycle invocation to one target/predecessor, preserving full Carrier and approved successor sets. Multiple independent requests use separate runs. Independent narrow review follows; no unassessed bulk effects.
