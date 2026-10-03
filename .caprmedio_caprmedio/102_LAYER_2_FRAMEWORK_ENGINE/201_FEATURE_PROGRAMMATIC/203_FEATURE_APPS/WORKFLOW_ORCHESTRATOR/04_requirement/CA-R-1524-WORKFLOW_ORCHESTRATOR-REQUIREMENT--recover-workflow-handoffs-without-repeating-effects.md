---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step Run"
    - "Action"
    - "Artifact/Revision"
    - "Journal"
    - "Journal/Record"
    - "Projection"
    - "Operator"
version: 2
updated_at: "2026-09-18 21:51:53 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1522", "CA-R-1520", "CA-R-1525", "CAPRMEDIO-META-REQU-158", "CA-R-1468", "CA-R-1470"]}
---
# Recover Workflow handoffs without repeating effects

WORKFLOW_ORCHESTRATOR **must** recover accepted work **and** admitted Run handoffs **after** interruption **without** losing work **or** blindly repeating effects.

- preserve an accepted request durably **before** acknowledging acceptance **to** its client.
- preserve the predecessor's terminal result **and** continuation intent durably **before** dispatching a successor. correlate that intent with the successor Run so repeated delivery **or** recovery cannot independently launch duplicate successors.
- retain execution facts **in** the canonical Project Journal under CAPRMEDIO-META-REQU-158. scheduling indexes, queues, **and** displayed state **must not** become a second historical authority; derived state is reconciled against its authoritative sources.
- recovery **must** distinguish work **not** started, work started, observed completion, **and** uncertain effect outcomes. an uncertain non-repeatable effect requires evidence reconciliation **or** Operator escalation, **not** an assumed exactly-once guarantee.
- retain the original request, Run associations, exact definition bindings under CA-R-1525, performed effects, **and** remaining retry allowance. changed definitions pause dispatch for recorded revalidation; current authority **and** target freshness remain required **before** further effects.
- a stopped service **or** lost client session **must not** imply successful completion. incomplete **or** conflicting recovery evidence blocks affected execution visibly.
