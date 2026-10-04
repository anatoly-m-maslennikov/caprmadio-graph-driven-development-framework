---
atom_id: CA-R-1812
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:12:24 +0400"
subjects:
  governs: "Workflow Run/execution"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Execute authorized Base Revise Runs independently

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** execute an Operator-authorized RMED Atoms Base Revise Run independently of the requesting session.

## Details

- accept a stable Run ID, explicit Atom selection, current rule files, named Author, confidence threshold **and** permissions.
- execute gather, check **and** fix using the existing Action prompts **and** coordination Tool; preserve the initial checks **without** adding a recheck phase.
- return admission promptly. a separately started local worker executes queued Runs after the MCP client disconnects.
- report queued, running, completed, failed **or** interrupted execution honestly; provide saved status, results **and** recovery through existing observation capabilities.
- initial support is the existing RMED Atoms Base Revise Workflow. unknown Workflow definitions are explicit unsupported requests.
