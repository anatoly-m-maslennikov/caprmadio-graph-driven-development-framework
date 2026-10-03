---
atom_id: CA-P-910
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Scope Unit, Job, and Demand Authority
    occurrent:
      - Scope Relation Authority Update
  depends_on:
    occurrent:
      - CA-P-909
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Update Scope Unit, Job, and Demand Authority

**when** CA-P-909 is Done, **then** the Assignee **must** make Scope Unit creation and cross-scope Requirement authority use explicit references and the accepted Job and Demand boundaries.

## Scope

`((every CA-P-905 frontier entry assigned to SCOPE_UNIT_JOB_AND_DEMAND) union (every replacement or new authority Atom created from such an entry))`

## Definition of Done

the Task is **not done if** (Current Scope or Claim Scope makes its referenced Scope Unit bearer-dependent on the Atom **or** Current Scope does not reference the owning Scope Unit when one exists **or** an empty Current Scope does not resolve to its identified Operator **or** Claim Scope does not reference the Scope Unit or Scope Expression to which the Claim applies **or** any Atom Type other than `Atom/Content Role: Requirement/Type: Job` may establish a Scope Unit **or** admitting a Job that establishes a Scope Unit is not atomic with establishing that Scope Unit **or** an established Scope Unit has no accepted Job **or** the direct parent does not own the establishing Job for its child Scope Unit **or** the same Scope Unit governance pattern cannot apply recursively at every Structural level **or** two Scope Units in one Project may share one Scope Unit Name **or** Job or Demand is not classified as a Relational Atom **or** `Atom/Content Role: Requirement/Type: Demand` does not remain distinct from Job **or** a Demand fully defines its Producer Scope Unit instead of constraining only the Producer result on which its Consumer depends **or** a Demand is owned by any Scope Unit other than its Consumer **or** a Demand targets an ancestor, a direct child, a deeper descendant, or a later ordered sibling **or** a Demand is admitted without a Job-authorized dependency on its Producer result **or** Demand introduces another graph relation instead of deriving its direction from its Consumer Current Scope and Producer Claim Scope references **or** a Scope Unit instance such as CORE_META_MODEL or LOCAL_CONFIGURATION is encoded with SUBTYPE_OF instead of INSTANCE_OF **or** the Project-root Operator exception or direct-parent ownership rule is lost **or** any replaced conflicting authority remains active).

## Details

require Current Scope to resolve before admission. permit a Job Claim Scope to identify the direct-child Scope Unit established by that accepted Job. subsequent Job Atoms may add Jobs without recreating the Scope Unit. preserve Demand as the distinct Consumer-to-Producer cross-scope Requirement Type. permit a Demand only about the result on which the Consumer's accepted Job depends; keep parent-to-direct-child scope establishment in Job authority and keep ancestry, deeper-descendant, and backward ordered-sibling directions forbidden in the Demand graph.
