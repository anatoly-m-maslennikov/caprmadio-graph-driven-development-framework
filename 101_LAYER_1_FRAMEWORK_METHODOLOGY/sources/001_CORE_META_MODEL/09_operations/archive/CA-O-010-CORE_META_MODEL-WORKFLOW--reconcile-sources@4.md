---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Source Reconciliation"
  depends_on:
    - "Workflow/Relation Kind: On Result"
    - "Step Run"
    - "Workflow Run"
    - "Action"
    - "Step"
    - "Workflow"
    - "Select Reconciliation Sources"
    - "Assess Source Conflicts"
    - "Propose Source Corrections"
    - "Obtain Source Correction Decision"
    - "Apply Approved Source Corrections"
    - "Publish Reconciled Projection"
    - "Operator"
    - "AI Agent"
    - "Autonomous Confidence Threshold"
    - "Projection/Type: Reconciled Projection"
version: 4
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile sources

Source Reconciliation **means** the reusable Workflow whose nodes are the following Steps **and** whose control flow is defined by their result conditions. the Step references reuse those Action definitions; they do **not** copy them **or** make another Workflow the Action invoked by a Step.

the entry Step is select. interpret Step bindings **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.

## Steps

| Step | Action reference | Parameters **and** inputs |
|---|---|---|
| select | CA-O-004 | the requested source selection **and** applicable source authority |
| assess | CA-O-005 | the exact frontier returned by select **and** applicable checks |
| propose | CA-O-006 | the assessed frontier, identified conflicts, **and** authorized correction boundaries |
| decide | CA-O-007 | the exact proposal, conflicts, frontier, **and** required approval context |
| correct | CA-O-008 | the exact approved correction **and** its current source frontier |
| publish | CA-O-009 | the final assessed frontier, valid decisions, **and** selected Projection Delivery authority |

## Transitions

the transitions below use the Workflow-scoped ON_RESULT Relation under CA-R-1513 **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step **and** Action reference | Result condition | Next Step **or** outcome |
|---|---|---|
| select — CA-O-004, Select Reconciliation Sources | complete exact selection | assess |
| select — CA-O-004 | incomplete, ambiguous, **or** failed selection | stop **and** escalate; no publication |
| assess — CA-O-005, Assess Source Conflicts | required checks complete, no unresolved conflict, required approvals valid | publish |
| assess — CA-O-005 | unresolved conflict with an authorized correction-proposal route | propose |
| assess — CA-O-005 | incomplete checks, unavailable correction authority, **or** unsupported resolution | stop **and** escalate; no publication |
| propose — CA-O-006, Propose Source Corrections | exact supported proposal ready | decide |
| propose — CA-O-006 | unsupported proposal **or** unmet confidence/authority gate | stop **and** escalate; no source mutation **or** publication |
| decide — CA-O-007, Obtain Source Correction Decision | valid exact approval **and** upstream corrections required | correct |
| decide — CA-O-007 | valid exact resolution decision **without** a needed source correction | select, **then** reassess the decision against the selected frontier |
| decide — CA-O-007 | requested revision **and** applicable authority permits another bounded proposal attempt | propose |
| decide — CA-O-007 | rejection, absent decision, invalid approval, **or** no accepted further attempt | stop **and** escalate; no source mutation **or** publication |
| correct — CA-O-008, Apply Approved Source Corrections | authorized correction completed | select, **then** reassess the new frontier |
| correct — CA-O-008 | failed **or** partially completed correction | stop **and** escalate with actual effects; an expressly authorized bounded recovery re-enters at select |
| publish — CA-O-009, Publish Reconciled Projection | completed publication from the still-valid final frontier | complete |
| publish — CA-O-009 | changed frontier | select **only** under the applicable accepted revisit conditions; **otherwise** stop **and** escalate |
| publish — CA-O-009 | failed publication | stop **and** escalate under applicable recovery authority; do **not** report completion |

an AI Agent **must** resolve **and** satisfy its effective applicable Autonomous Confidence Threshold from governing sources **and** valid overrides, together with authorization gates, **before** continuing autonomously. this does **not** require a persisted Task Atom; unmet **or** unresolved gates require Operator clarification **or** escalation. **every** autonomous revisit, including re-evaluation **after** an approved source change, repeated correction proposals, **and** recovery retries, **must** remain within the applicable accepted retry budget **and** escalation conditions for the current Workflow Run. reselection **or** discovery of a new conflict does **not** reset that budget. an absent, exhausted, **or** unresolved revisit allowance requires stopping **and** escalation; required re-evaluation **must not** be skipped **to** publish. this Workflow does **not** authorize concurrent execution, arbitrary recursion, automatic source corrections, **or** publication with unresolved conflicts. execution evidence remains distinct from this reusable definition.
