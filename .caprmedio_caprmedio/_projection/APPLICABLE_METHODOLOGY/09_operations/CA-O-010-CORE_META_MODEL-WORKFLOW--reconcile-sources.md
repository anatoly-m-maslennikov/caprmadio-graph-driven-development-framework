---
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
version: 9
updated_at: "2026-10-04 17:31:25 +0000"
relations: {}
atom_id: "CA-O-010"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Workflow"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources.md
  source_atom_id: CA-O-010
  source_atom_revision: 9
  source_sha256: 0f20146444637ca38de69f97931c4a45c663c9a6dd2d759c3599e9864acfc7da
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reconcile sources

## Operation

Source Reconciliation **means** the reusable Workflow whose nodes are the following Steps **and** whose control flow is defined by their result conditions. the Step references reuse those Action definitions; they do **not** copy them **or** make another Workflow the Action invoked by a Step.

the entry Step is CA-O-146. interpret Step bindings **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.

### Steps

| Step |
|---|
| CA-O-146 |
| CA-O-147 |
| CA-O-148 |
| CA-O-149 |
| CA-O-150 |
| CA-O-151 |

### Transitions

the transitions below use the Workflow-scoped ON_RESULT Relation under CA-R-1513 **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step | Result condition | Next Step **or** outcome |
|---|---|---|
| CA-O-146 | complete exact selection | CA-O-147 |
| CA-O-146 | incomplete, ambiguous, **or** failed selection | stop **and** escalate; no publication |
| CA-O-147 | required checks complete, no unresolved conflict, required approvals valid | CA-O-151 |
| CA-O-147 | unresolved conflict with an authorized correction-proposal route | CA-O-148 |
| CA-O-147 | incomplete checks, unavailable correction authority, **or** unsupported resolution | stop **and** escalate; no publication |
| CA-O-148 | exact supported proposal ready | CA-O-149 |
| CA-O-148 | unsupported proposal **or** unmet confidence/authority gate | stop **and** escalate; no source mutation **or** publication |
| CA-O-149 | valid exact approval **and** upstream corrections required | CA-O-150 |
| CA-O-149 | valid exact resolution decision **without** a needed source correction | CA-O-146, **then** reassess the decision against the selected frontier |
| CA-O-149 | requested revision **and** applicable authority permits another bounded proposal attempt | CA-O-148 |
| CA-O-149 | rejection, absent decision, invalid approval, **or** no accepted further attempt | stop **and** escalate; no source mutation **or** publication |
| CA-O-150 | authorized correction completed | CA-O-146, **then** reassess the new frontier |
| CA-O-150 | failed **or** partially completed correction | stop **and** escalate with actual effects; an expressly authorized bounded recovery re-enters at CA-O-146 |
| CA-O-151 | completed publication from the still-valid final frontier | complete |
| CA-O-151 | changed frontier | CA-O-146 **only** under the applicable accepted revisit conditions; **otherwise** stop **and** escalate |
| CA-O-151 | failed publication | stop **and** escalate under applicable recovery authority; do **not** report completion |

an AI Agent **must** resolve **and** satisfy its effective applicable Autonomous Confidence Threshold from governing sources **and** valid overrides, together with authorization gates, **before** continuing autonomously. this does **not** require a persisted Task Atom; unmet **or** unresolved gates require Operator clarification **or** escalation. **every** autonomous revisit, including re-evaluation **after** an approved source change, repeated correction proposals, **and** recovery retries, **must** remain within the applicable accepted retry budget **and** escalation conditions for the current Workflow Run. reselection **or** discovery of a new conflict does **not** reset that budget. an absent, exhausted, **or** unresolved revisit allowance requires stopping **and** escalation; required re-evaluation **must not** be skipped **to** publish. this Workflow does **not** authorize concurrent execution, arbitrary recursion, automatic source corrections, **or** publication with unresolved conflicts. execution evidence remains distinct from this reusable definition.

## Details
