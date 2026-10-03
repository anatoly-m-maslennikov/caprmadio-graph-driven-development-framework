---
atom_id: CA-O-079
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Reconcile Unfinished Work"
  depends_on:
    - "Action"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Revision"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Status"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
    - "Relation"
    - "Journal"
    - "Journal/Record"
    - "Carrier"
    - "Operator"
    - "Workflow Run"

version: 1
updated_at: "2026-09-23 16:51:13 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CAPRMEDIO-META-REQU-147", "CA-M-306", "CA-R-1574", "CA-R-1576", "CA-R-1577", "CA-R-1579", "CA-R-1580", "CA-R-1583", "CA-R-1599", "CA-R-1539", "CA-R-1464", "CA-D-461", "CA-D-470", "CA-D-481", "CA-R-1490", "CAPRMEDIO-META-REQU-158"]}
---
# Summary

Reconcile unfinished operative work

## Claim

Reconcile Unfinished Work **means** the Action that reconciles still-valid remaining work with its applicable Plan representation under CAPRMEDIO-META-REQU-147, **without** duplicating existing Plans **or** authorizing execution of that work.

### Inputs and preconditions

- the selected work, its source context, available completion evidence, **and** the reason it remains unfinished.
- current relevant Plan Revisions, their Claims, Definitions of Done, Status values, decomposition, blocking Relations, **and** evidence references.
- applicable Scope Unit ownership, Claim Target Scope Unit, authoring rules, **and** authorization for the proposed Plan changes.

### Behavior

1. distinguish the still-valid remaining work from completed results, canceled work, obsolete requests, **and** uncertain completion claims. use available evidence; missing evidence is **not** proof of completion **or** permission **to** replay an effect.
2. find whether the remaining work is already represented by a Plan. check the originating Plan first **when** available, **then** other relevant Plans by Claim **and** applicability rather than Label **or** folder name. reuse an applicable existing Plan; **if** several competing representations remain unresolved, report them rather than create another duplicate.
3. reconcile necessary progress, remaining-work details, blockers, **and** source references within the authorized change. retain the existing Claim boundary **and** identity; a Summary change requires replacement under CA-R-1464. reference completed Plan Atoms **and** canonical Journal events using existing preservation authority CA-D-461, CA-R-1490, **and** CAPRMEDIO-META-REQU-158; do **not** copy those Atoms **or** historical events into another authoritative record.
4. **if** no applicable Plan represents still-valid work, create a Plan **only** within existing creation authority **and** under CA-M-306, CA-R-1599, **and** CA-D-470. select admitted Status **and** placement under CA-R-1539 **and** CA-D-461. use an explicitly justified `IS_DECOMPOSITION_OF` Relation under CA-D-481 **when** the work contributes required work **to** another Plan; a standalone Plan remains permitted. do **not** introduce a Version Plan **or** Change Plan authoring model merely from its Label.
5. retain explicit blocking under CA-R-1580 independently of decomposition **and** navigation order. do **not** silently reopen Done, Canceled, **or** Archived work, change another Plan's Status, **or** infer readiness from moving a Carrier. unresolved authority, applicability, validity, **or** destination selection remains a reported blocker.
6. **before** applying an authorized change, confirm the selected Plan Revisions remain current. apply **only** the bounded reconciliation, check its resulting references **and** Carrier placement, **and** record actual change events under the existing Journal authority. an already reconciled item is a no-change result, **not** another Plan **or** duplicate historical event.

### Results and effects

- reconciled: the existing **or** newly created Plan IDs, the remaining-work disposition, actual authorized changes **or** no-change result, **and** references **to** existing completion evidence.
- blocked: the preserved source context, unresolved item, relevant Plan IDs, missing evidence **or** authority, **and** the decision required from the Operator **when** current authority cannot settle it.
- failed: the exact completed **and** incomplete effects, recoverable evidence, **and** required recovery; do **not** report partial reconciliation as completion.

this Action maintains the representation of unfinished work. it does **not** execute that work, restart a Workflow Run, replay completed effects, mark the work Done, **or** introduce another completed-work preservation policy. resulting Plan Atoms remain subject **to** their existing Definition of Done, Status, authorization, **and** execution rules.
