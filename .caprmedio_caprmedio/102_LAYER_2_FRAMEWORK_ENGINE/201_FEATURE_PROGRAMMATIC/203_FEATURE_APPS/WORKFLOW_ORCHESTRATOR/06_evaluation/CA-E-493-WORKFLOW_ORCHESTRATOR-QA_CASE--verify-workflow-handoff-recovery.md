---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Action"
    - "Artifact/Revision"
    - "Journal"
    - "Projection"
    - "Operator"
version: 2
updated_at: "2026-09-18 21:51:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for": ["CA-R-1524", "CA-M-302"], "relates_to": ["CA-E-352", "CA-E-489", "CA-E-491", "CA-E-494"]}
---
# Verify Workflow handoff recovery

the Evaluation **must** check WORKFLOW_ORCHESTRATOR recovery at the boundaries of an update-to-replacement handoff under CA-R-1524.

## Interruption cases

- interrupt **before** the handoff is durable: recovery **must not** assume an accepted successor dispatch.
- interrupt **after** durable handoff but **before** successor start: resume the same continuation intent **without** losing the accepted request.
- interrupt **after** successor start but **before** its acknowledgement: repeated dispatch delivery **must not** create another successor Run.
- lose the response **after** a non-repeatable effect: require reconciliation evidence **or** escalation rather than blind replay.
- change the target Revision **or** revoke permission **before** resumed execution: require paused dispatch under the applicable validation rules rather than use of stale approval **or** inputs.
- change a bound Workflow **or** Action definition during a wait **or** service restart: require paused dispatch under CA-R-1525, retained original bindings, **and** recorded revalidation **before** continuation; silently selecting the new Revision **or** continuing an unvalidated old binding fails.
- provide valid revalidation for remaining work: resume **only** with its exact admitted bindings, current authorization, **and** compatible effects **and** inputs; completed Step Runs retain their original bindings **and** are **not** replayed.
- change a definition while an Action is **in** flight: follow the admitted interruption policy, retain its actual binding **and** result, **and** block subsequent dispatch **until** revalidation; do **not** force termination **or** repeat its effect merely because the definition changed.
- rebuild the execution view **after** restart: canonical Journal facts **must** remain its historical authority; predecessor completion alone **must not** appear as completed replacement.

pass **only** with evidence of retained request identity, correct Run associations, no duplicate successor effects, preserved retry allowance, **and** truthful outcomes. reuse the general App restart boundary under CA-E-352; no real Project Atom replacement is required for this fixture.
