---
atom_id: CA-O-122
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Action"
    - "Atom/Revision"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Status"
    - "Relation"
    - "Operator"
    - "Workflow Run"
    - "Journal"
version: 1
updated_at: "2026-10-04 15:12:11 +0000"
relations:
  relates_to: [CA-R-1583, CA-R-1599, CA-R-1520, CA-R-1580, CA-O-079, CA-O-017, CA-O-077, CA-O-090]
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-122-CORE_META_MODEL-ACTION--assess-completed-work-handoff.md
  source_atom_id: CA-O-122
  source_atom_revision: 1
  source_sha256: e4099e0498f664d6f5179247a14fadb619c47ae70a7541dc4d1ba94a71f7c9e7
  original_relations_sha256: 7038b731397220a891683e692ecd42be19539b02fa491c4738bc20910feef073
---
# Summary

Assess completed-work handoff

## Operation

This optional read-only Action assesses a completed bounded Plan's actual result against the current inputs and prerequisites of affected next Plans within an explicitly declared complete candidate universe. It applies when a handoff-assessment request is admitted; it is not a mandatory trigger after every Task or a new completion policy.

### Inputs and preconditions

- the admitted assessment request, selected predecessor Plan identity and current Revision, bounded actual outputs, and references to existing completion, check and performed-effect evidence. Include non-implementation work; a supplied Done value or historical test/save report alone is not completion proof.
- applicable current authority and Project Principles, the predecessor's own work, decomposition and Definition of Done, and any unresolved completion obligations under CA-R-1583 and CA-R-1599.
- the declared complete universe of candidate next Plans, its scope and exclusions, each candidate's exact current Revision, Claim boundary, inputs, required checks, prerequisites, declared consumption bindings and explicit blocking Relations. Folder order, sibling location and mere mentions are not dependency evidence.
- the assessor's authorized read context and applicable permission limits. If separately authorized reconciliation has already occurred, provide its exact CA-O-079 outcome, before/current Revisions and recoverable effect evidence; do not assume or replay an effect.

### Assessment

1. Verify the applicable predecessor completion evidence under existing completion authority. Missing or uncertain evidence, unfinished own work or directly decomposed Plans, or a Definition of Done whose falsifying condition is not established false prevents a verified closure/readiness claim. Return the exact missing or failed obligation; do not close the Plan or weaken its conditions.
2. Identify actually affected candidates from the actual result, declared consumption and explicit governing bindings. Give every candidate an evidence-backed affected or unaffected disposition when supported. If the universe or a consumption/dependency binding is insufficient to justify exhaustive coverage, retain each unresolved classification and return blocked or uncertain coverage with the missing scope/evidence; never force an unsupported binary disposition, certify “all affected Plans” from a partial set or guess an edge.
3. For each affected Plan, compare every relevant exact input, Claim boundary, required check and prerequisite with the actual predecessor output and current authority. Assess output changes even when authority is unchanged. Disposition each affected binding as unchanged, rebinding-required, blocked or recovery-required, with its observed Revision and exact evidence. Preserve unrelated candidates and their unselected work unchanged.
4. Where representation changes are needed, return a bounded CA-O-079-ready reconciliation request and its missing permission or prerequisite. CA-O-079 remains the owner of authorized remaining-work edits, reuse or conditional creation, completed-prefix preservation, explicit blocking, current-Revision/placement checks and actual Journal events. This Action neither performs nor invokes those edits. If an actual separately authorized reconciliation outcome was supplied, assess and reference that outcome rather than duplicate it; partial or stale effects retain exact recoverable state and recovery-required or blocked disposition.
5. Before returning a current assessment, confirm the observed source, predecessor and candidate Revisions still match the compared evidence. A changed Revision or result invalidates the affected success claim: return its stale binding and required fresh assessment or recovery, not stale success or an automatic retry. The receipt is evidence for this exact binding only.
6. Return one checkable receipt containing predecessor/output/completion evidence references, applicable authority and observed Revisions, declared candidate universe and exclusions, every candidate's supported affected/unaffected disposition or exact unresolved classification, every affected binding's disposition and evidence, actual separately authorized reconciliation outcome or pending required change, unresolved blockers and requested next use. A complete unchanged assessment is a no-change result, not another Plan, historical event or repeated completed effect.
7. For a declared Workflow-to-Workflow handoff, reuse CA-R-1520's terminal result and distinct-Run boundary. Distinguish a requested continuation from authorized, started or completed continuation; the ending Run does not call, wait for or resume a successor, and required pending, blocked or failed continuation is not reported complete. The separate executor retains predecessor/successor association and rechecks authority/input freshness before any separately admitted successor start.

## Details

### Ownership and outcomes

The contribution is the bounded completed-Plan result-to-affected-next-Plan assessment and receipt, including non-implementation work. CA-R-1583/CA-R-1599 retain completion/DoD meaning; CA-R-1520 retains Workflow handoff policy; CA-O-079 retains reconciliation effects; CA-O-017 retains implementation preparation, CA-O-077 coordinated Property/address reconciliation, and CA-O-090 corrective-Method acceptance. Reuse their responsibilities without broadening or duplicating them.

An assessed receipt may retain unchanged, rebinding-required, blocked and recovery-required bindings together. Incomplete universe or closure evidence prevents exhaustive/current readiness assurance, even if some individual comparisons are supported. Missing edit permission keeps the request pending and mutation blocked; a newly required prerequisite remains a start blocker under existing CA-R-1580 until separately satisfied. Refer to existing evidence and recoverable originals, not a new history or Journal store. Repeated assessment of the same evidence/Revisions has the same dispositions and no repeated completed effect; no-change is not an instruction to append a duplicate event.

### Invocation and authority boundary

The Operator retains whether to invoke this capability and what effects to authorize. A selected Plan or Workflow may require this assessment within its explicitly approved sequence; that does not make the sequence universal. A passed assessment grants no permission to edit, execute, close, release or adopt.

No automatic Done, Status or placement change, successor invocation, Run restart, execution, replay, retry-allowance reset, compulsory follow-up, guessed routing/dependency/permission, new relation kind, universal concurrency rule or duplicate preserved-data policy follows. This read-only Action does not perform repair, create a Workflow/Step, choose continuation, or call CA-O-079. Current-snapshot evidence does not replace a later caller's own freshness, authorization, blocking and completion checks.
