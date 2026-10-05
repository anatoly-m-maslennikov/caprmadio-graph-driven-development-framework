---
atom_id: CA-C-471
content_role: Concern
type: Problem
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 15:39:55 +0000"
subjects:
  governs: "Release recovery result"
  depends_on: [Run, Journal, Workflow, Action, Implementation]
relations:
  concern_about: [CA-P-1716, CA-D-577, CA-E-583]
---
# Summary

Return existing canonical Release recovery receipts

## Concern

The Release recovery response reads `event_refs`, while the shared selected result supplies `event_receipts`. It consequently returns an empty canonical Journal reference list even when receipts exist. The separate recovery observer also omits the required canonical references and pending reason.

## Evidences

/root/runtime_prerequisites independently observed the mismatch between `WORKFLOW_ORCHESTRATOR/backend.py` and `workflow_run_support.py` and rejected the current response against CA-D-577. Its inspection confirmed that the recovery observer uses supported fields in the installed DBOS API. Eight bounded tests passed; one errored during temporary-directory cleanup after its test body, which is not an acceptance result for that case.

The first receipt-shape repair passes ten retained-fixture tests. Independent re-review accepts the receipt extraction but finds that the real shared `recording_pending` result has `pending_event_ids` and no `reason`. The remaining repair must derive its factual pending reason from that existing state; a null reason does not satisfy CA-D-577 for this case.

## Blast radius

Only the public recovery response and observation metadata under CA-P-1716. Existing canonical Run identity and execution remain unchanged. Actual queue, MCP and Docker proof remain separate unfinished gates.

## Decision

Derive canonical Event identifiers from the existing shared receipt shape and return the same truthful canonical metadata from both operations. Keep transport status separate from the original canonical Run. Test actual receipt layouts and retain fixture directories as directed; do not invent Journal events or infer recording from a queue handle.

## Result

The backend now derives exact unique Event IDs from shared `event_receipts` in both recovery submission and observation. For the real `recording_pending` result with nonempty sealed `pending_event_ids` and no explicit reason, it reports a factual pending-recording reason. /root/runtime_prerequisites independently accepts this bounded response repair; root reruns the declared retained-fixture transport suite with 10 passing tests. Source inspection confirms compatibility with the installed DBOS status fields. Actual queue/MCP/Docker execution remains unfinished under CA-P-1716 and is not inferred from this resolved code finding.
