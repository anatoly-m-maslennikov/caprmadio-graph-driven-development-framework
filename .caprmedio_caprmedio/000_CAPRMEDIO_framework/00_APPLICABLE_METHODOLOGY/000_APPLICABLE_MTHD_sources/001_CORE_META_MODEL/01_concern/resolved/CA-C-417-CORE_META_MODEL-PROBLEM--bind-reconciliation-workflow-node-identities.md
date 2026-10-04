---
atom_id: CA-C-417
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 2
updated_at: "2026-10-04 18:15:44 +0000"
subjects:
  governs: "Source Reconciliation/Step bindings"
  depends_on: [Workflow, Step, Action]
relations:
  concern_about: [CA-O-010, CA-O-011, CA-P-1442]
---
# Summary

Bind reconciliation Workflow node identities

## Concern

The selected generic reconciliation and Applicable Methodology workflows describe local nodes without current Step Atom identity bindings.

## Evidences

Independent P1442 directly read O010v7/O011v10, R1509v6/R1513v4 and current Step carriers. No exact reconciliation Step definitions were located; local names select/assess/propose/decide/correct/publish refer directly to shared Actions O004-O009. Existing approval, currentness, correction/reselection and retry semantics remain reusable.

## Blast radius

### Resolution

P1448/P1449 saved exact Step identities O146–151 and O152–157. Independent P1457/P1458/P1459/P1460 reviewed their bindings; P1469 accepted graph-only ownership. P1474–P1477 accepted all affected context deltas. Current O010v9/O011v12 and all twelve v2 Steps preserve source correction, Operator disposition, reselection and publication guards. This source identity defect is resolved; compiler implementation gaps remain assigned to PROGRAMMATIC.

### Original impact

P1448 binds generic O010 Steps O146-O151; P1449 binds O011's specific invocations O152-O157. Shared Actions remain one truth; separate invocation parameters and Workflow ownership are not duplicated Action definitions. Preserve graph behavior and use independent <=4-source slices before source-stage acceptance. Compiler Extension/approval defects are separate implementation work, not a reason to weaken these sources.
