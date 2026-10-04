---
atom_id: CA-R-1814
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 02:57:00 +0400"
subjects:
  governs: "Workflow Run/permissions"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Constrain isolated Agent fixes to granted authority

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** admit Agent-proposed changes **only** within the Operator-granted selection **and** permissions.

## Details

- initial automated fixes preserve Version; a Version-changing proposal pauses for a governed Revision history transition rather than overwriting previous authority.

- checks use read-only isolated Codex CLI sessions.
- fix Agents return proposed content; the orchestrator applies admitted content, rather than granting Agents unrestricted access **to** the Project.
- initial automated fixes retain the Atom ID **and** Summary. replacement, retirement, changed Summary, missing authority **or** confidence below the requested threshold require an interrupted Run with explicit blockers.
- completion requires the existing report admission **and** progress criteria; a worker exit code **alone** proves no semantic completion.
- credentials remain outside requests, prompts, reports **and** source authority.
