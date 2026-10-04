---
atom_id: CA-P-1465
content_role: Plan
type: Plan
label: Task
work_sequence_number: 32
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on: [Operations, Implementation, Plan]
version: 2
updated_at: "2026-10-04 17:35:37 +0000"
relations:
  is_decomposition_of: [CA-P-1132]
  blocks: [CA-P-1132, CA-P-1158, CA-P-1160]
---
# Summary

Remove duplicated Workflow Step bindings

## Objective

Repair only O010, O011 and O015 against R1570 v4 and P1457 F1. Workflow owns graph Step references/Relations/entry/conditions/outcomes; Steps exclusively own Action references/parameters/input bindings. Remove duplicated bindings while preserving every graph node, transition, outcome and guard. Preserve prior whole revisions under archive; keep Summaries/IDs fixed and increment semantic Versions. Own these three Workflows, their archives, this Plan and narrow C425. No Step or code edits. Estimate <=12 minutes. An independent reviewer must review the changed clauses before source acceptance.

Use current CA-P-1117 v3 and relevant active Principles. Own only stated files; you are not alone, preserve others' edits. No harvesting, FPF, code, Journal or Git writes. Record actual clock and result. A saved source is not runtime proof.

## Details

### Actual bounded repair binding

First clock 2026-10-04 17:25:45 UTC, unchanged; exact binding 2026-10-04 17:30:08 UTC. Read current P1117 v3, the full P1457 v1 F1 review, R1570 v4 and all three current owned Workflows completely. Goal13/all14 active Principles were qualified unchanged from their previously fully read bytes. R1570 assigns only the graph scheme to a Workflow; Step Atoms exclusively own Action references/parameters/input bindings. No full model redesign is authorized.

| Owned semantic revision | Exact current input/output | Exact original whole-revision archive |
| --- | --- | --- |
| CA-O-010 v8→v9 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources.md` | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources@8.md` |
| CA-O-011 v11→v12 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-011-CORE_META_MODEL-WORKFLOW--bind-source-reconciliation-to-applicable-methodology.md` | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-011-CORE_META_MODEL-WORKFLOW--bind-source-reconciliation-to-applicable-methodology@11.md` |
| CA-O-015 v7→v8 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-015-CORE_META_MODEL-WORKFLOW--maintain-project-structure.md` | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-015-CORE_META_MODEL-WORKFLOW--maintain-project-structure@7.md` |

Retain all three Summaries/identities and all other metadata except meaningful Version increments and actual edit time. The original full Carriers are preserved verbatim at the absent archive targets above. Remove only the duplicated binding columns/declarations from node tables and Action IDs/labels from transition source cells. Preserve all six nodes in each Workflow and every existing16/16/13 transition condition, destination, order, entry and full approval/currentness/confidence/revisit/recovery/failure/terminal guard. Generic authority/ownership notes and metadata references are not second per-Step binding assignments and are not a model-migration target.

Create narrow CORE_META_MODEL Problem C425 at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/01_concern/CA-C-425-CORE_META_MODEL-PROBLEM--remove-duplicated-workflow-step-bindings.md`, concerning these three sources and P1465, retaining P1457 F1/R1570 evidence and repair-pending-independent-review disposition. No Step, Action, other source, code, shared parent, Git or Journal edits. Steps remain peer reviewed; root must separately bind independent review of these three amended graph-only Workflows before source acceptance.

### Actual saved result and verification

O010 v9, O011 v12 and O015 v8 were saved 2026-10-04 17:31:25 UTC; each exact previous v8/v11/v7 Carrier is preserved verbatim at the archive path in the binding table. C425 v1 is saved Active at the bound Core Concern path and remains pending independent amended-source review. No Step or Action was changed.

Each Workflow node table now declares only its six Step references. The duplicated Action/parameter/input columns and per-transition Action IDs/labels were removed; O011's descriptive role column was removed with that duplicate binding table. Entry points, node identities/order, typed ON_RESULT meaning and all16/16/13 transition rows remain unchanged. Generic authority/ownership notes and nonbinding metadata references were not turned into new invocation declarations.

The one proportionate saved check passed 2026-10-04 17:33:11 UTC: all three saved Workflows and C425 have strict duplicate-key-safe YAML, registered sections, unchanged Summary/identity/current and target scope/other metadata, clean trailing whitespace and one EOF newline. The three whole predecessor snapshots are byte-identical to the complete original reads. The current18 node references resolve to existing same-Workflow Step Carriers read-only; this is endpoint closure, not new Step review. Every transition condition/destination/order and full confidence/authorization/currentness/retry/recovery/stop guard is exact; reversing only the removed binding columns/labels and Version/updated_at reproduces each whole prior Carrier. No Action ID is independently assigned in the repaired Workflow bodies.

| Bounded graph scenario | Saved result |
| --- | --- |
| Reconciliation or methodology compilation clean assessed frontier | Same selection→assessment→publication route and complete current checks/approval predicate; no new publication bypass. |
| Exact decision/correction/reselection, requested revision or partial recovery | Same decision/no-correction/revisit routes, renewed selection/assessment and expressly authorized bounded recovery; no retry reset or invented approval. |
| Structural create/rename/move/remove request | Same six-node select→prepare→assess-candidate→authorize→apply→assess-result graph; canonical Step input bindings remain in their unchanged sources. |
| Failure/stale/unauthorized/below-threshold/unevaluated result | Same exact16/16/13 stop/terminal predicates and actual-state reporting; completion cannot be inferred from removing duplicate declarations. |

This leaf's own bounded repair/proof is complete. Root must independently review O010 v9/O011 v12/O015 v8 before accepting source ownership conformance or resolving C425; Step review remains with peers. P1132/P1158/P1160 gates are retained and no dependent RMED, implementation or runtime readiness is claimed. No other source, Step/Action, parent, code, Project Structure/settings, Git or Journal was written.

Original first 2026-10-04 17:25:45 UTC; completion 2026-10-04 17:35:37 UTC; actual elapsed 592s within the <=12-minute estimate. Only the three Workflow outputs, their exact prior archives, narrow C425 and this Plan were written. The final saved receipt/physical Done check retains the exact Summary/identity and dependency gates.

### Definition of Done

The exact bound work and one proportionate saved-file/scenario check are complete. Findings and remaining independent review stay explicit; a completed review may report findings without claiming clean source acceptance. Place this Plan in done/ only when its own work is complete.
