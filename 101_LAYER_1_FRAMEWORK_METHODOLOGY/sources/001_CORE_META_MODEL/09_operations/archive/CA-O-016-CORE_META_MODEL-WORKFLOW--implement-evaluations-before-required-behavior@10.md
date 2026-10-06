---
atom_id: CA-O-016
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Workflow"
  depends_on:
    - "Workflow"
    - "Step"
    - "Workflow/Relation Kind: On Result"
    - "Workflow Run"
    - "Step Run"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Control"
version: 10
updated_at: "2026-09-24 17:18:07 +0000"
relations:
  relates_to:
    - CA-R-1509
    - CA-R-1519
    - CA-R-1525
    - CA-R-1570
    - CA-O-091
    - CA-O-092
    - CA-O-093
    - CA-O-094
    - CA-O-095
    - CA-O-096
    - CA-O-099
    - CA-O-098
---
# Summary

Implement Evaluations before required behavior

## Claim

Implementation Workflow **means** the test-first implementation graph below; its referenced Step Atoms own Action/input/context bindings, **and** its Action Atoms own operational behavior.

- entry: CA-O-091.
- nodes: CA-O-091, CA-O-092, CA-O-093, CA-O-094, CA-O-095, CA-O-096, CA-O-099.
- transitions between Steps use Workflow-scoped `ON_RESULT`; `completed` **and** `blocked` are terminal results, **not** Steps.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-091 | evaluation_ready | CA-O-092 |
| CA-O-091 | requirement_ready | CA-O-093 |
| CA-O-091 | evaluation_runnable | CA-O-094 |
| CA-O-091 | complete | completed |
| CA-O-091 | blocked | blocked |
| CA-O-092 | prepared | CA-O-091 |
| CA-O-092 | blocked | blocked |
| CA-O-093 | implemented | CA-O-091 |
| CA-O-093 | blocked | blocked |
| CA-O-094 | passed | CA-O-091 |
| CA-O-094 | failed | CA-O-095 |
| CA-O-094 | blocked | blocked |
| CA-O-095 | expected_initial_failure | CA-O-091 |
| CA-O-095 | implementation_defect | CA-O-096 |
| CA-O-095 | test_implementation_defect | CA-O-096 |
| CA-O-095 | authority_change_required | blocked |
| CA-O-095 | environment_blocker | blocked |
| CA-O-095 | unresolved | blocked |
| CA-O-096 | retry_permitted | CA-O-099 |
| CA-O-096 | retry_blocked | blocked |
| CA-O-099 | repaired | CA-O-091 |
| CA-O-099 | authority_change_required | blocked |
| CA-O-099 | blocked | blocked |

an unknown result, failed invocation, unresolved confidence/permission gate, **or** non-progressing revisit ends the Run as `blocked` with actual partial results. **every** repair path crosses CA-O-096; revisiting preparation **or** changing a failure **must not** reset that retry state. preparation revisits retain completed work **and** require a changed residual work/evidence/baseline state; otherwise they are blocked rather than looping.

a terminal blocker preserves completed effects **and** pending P work. resumption requires fresh admission under the definition-binding rules; it is **not** success **or** permission **to** silently replay completed work.

Method creation **and** acceptance are outside this Workflow. return retained issue, test, diagnosis, **and** fix evidence for a separately invoked Method-learning Run under CA-O-102; neither that Run nor creation of an M Atom is an implementation-completion prerequisite.
