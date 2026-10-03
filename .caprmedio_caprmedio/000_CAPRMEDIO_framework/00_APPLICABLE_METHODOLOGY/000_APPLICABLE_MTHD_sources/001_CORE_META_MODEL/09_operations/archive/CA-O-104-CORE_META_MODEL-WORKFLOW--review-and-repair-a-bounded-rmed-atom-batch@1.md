---
atom_id: CA-O-104
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-28 16:14:59 +0400"
subjects:
  governs: "RMED Atom Review Workflow"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Workflow/Relation Kind: On Result"
    - "Atom"
relations: {"relates_to":["CA-O-108","CA-O-109","CA-O-110"]}
---
# Summary

Review and repair a bounded RMED Atom batch

## Operation

RMED Atom Review Workflow **means** the graph that selects a bounded active RMED batch, evaluates its Atoms one by one, **and** repairs verified findings through the following Steps.

- entry: CA-O-108.
- nodes: CA-O-108, CA-O-109, CA-O-110.
- transitions use Workflow-scoped `ON_RESULT`; completed **and** blocked are terminal results, **not** Steps.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-108 | ready | CA-O-109 |
| CA-O-108 | empty | completed |
| CA-O-108 | blocked | blocked |
| CA-O-109 | clean | completed |
| CA-O-109 | issues | CA-O-110 |
| CA-O-109 | blocked | blocked |
| CA-O-110 | verified | completed |
| CA-O-110 | blocked | blocked |

an unknown result **or** failed invocation ends the Run as blocked with retained partial evidence. the caller owns routing; an Action does **not** invoke the next Step. completion covers **only** the manifest's selected batch, **not** its deferred queue. another batch requires a new admitted Run. changing selected sources **or** governing authority invalidates affected prior results; resumption verifies bindings **and** retains retry accounting rather than silently replaying completed effects.

## Details

the implementation uses short Action prompts plus **=1** reusable Evaluation prompt; no Workflow server **or** MCP integration is required.
