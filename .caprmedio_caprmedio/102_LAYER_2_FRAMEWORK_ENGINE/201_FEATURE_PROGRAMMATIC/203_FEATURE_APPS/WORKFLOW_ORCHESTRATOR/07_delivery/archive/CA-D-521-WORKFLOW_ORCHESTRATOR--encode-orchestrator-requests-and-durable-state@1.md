---
atom_id: CA-D-521
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 02:57:00 +0400"
subjects:
  governs: "Workflow Run/Carrier"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Encode orchestrator requests and durable state

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** use the following request **and** persistence Carriers.

## Details

- Implementation Folder: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR.
- authoritative requests carry workflow_id, run_id, selection of atom_id/path, criteria_paths, author, scope, confidence_threshold, allow_fixes **and** agent_timeout_seconds; optional journal_author carries the existing Journal's GitHub identity without replacing the Atom Author. extra fields are rejected.
- persistent local DBOS SQLite file: .caprmedio_install/workflow_orchestrator/dbos.sqlite. this operational checkpoint store is **not** ephemeral runtime state **or** a second Atom authority.
- request, dispatch intent, admitted output **and** staged edit evidence: .caprmedio_install/workflow_orchestrator/runs/<run_id>/. relative paths reject traversal, symlinks **and** secret Carriers.
- confirmed Workflow events use the existing shared Project Journal; full reports remain tmp/RMED Atoms Base Revise/<run_id>.md through the existing Tool.
- CLI supports enqueue, status, worker **and** start-worker. start-worker explicitly launches a detached local worker; MCP exposes workflow_orchestrator for enqueue **and** status **and** does **not** start workers implicitly.
- Agent output carries report_json, candidate_content **and** confidence; queued requests bind the selected sources, rules, Workflow definition, prompts **and** implementation fingerprint.
- defaults: confidence threshold 90 percent for this requested implementation, Agent timeout 600 seconds, source limit 8 MiB **and** selection limit 10000. request overrides remain within strict types **and** bounds.
- initial defaults allow_fixes=false; an explicit true value delegates fixes within the selected Atom, retaining Summary **and** identity.
