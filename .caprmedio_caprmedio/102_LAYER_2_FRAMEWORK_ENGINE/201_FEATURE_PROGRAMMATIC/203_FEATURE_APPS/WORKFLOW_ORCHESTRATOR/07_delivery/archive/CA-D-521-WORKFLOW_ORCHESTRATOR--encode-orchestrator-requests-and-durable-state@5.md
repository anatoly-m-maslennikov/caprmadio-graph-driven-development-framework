---
atom_id: CA-D-521
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-05 02:32:00 +0400"
subjects:
  governs: "Workflow Run/Carrier"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Encode orchestrator requests and durable state

## Scope

WORKFLOW_ORCHESTRATOR's existing local execution capability and the fifteen Operator-selected Workflow routes: the original thirteen of CA-P-1117 plus the two accepted read-only query routes of CA-P-1520.

## Claim

WORKFLOW_ORCHESTRATOR **must** use the following request **and** persistence Carriers.

## Details

- Implementation Folder: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR.
- the retained Base Revise `enqueue` variant carries workflow_id, run_id, selection of atom_id/path, criteria_paths, author, scope, confidence_threshold, allow_fixes, allow_replacements **and** agent_timeout_seconds; optional journal_author carries the existing Journal's GitHub identity without replacing the Atom Author. extra fields are rejected.
- persistent local DBOS SQLite file: .caprmedio_install/workflow_orchestrator/dbos.sqlite. this operational checkpoint store is **not** ephemeral runtime state **or** a second Atom authority.
- request, dispatch intent, admitted output **and** staged edit evidence: .caprmedio_install/workflow_orchestrator/runs/<run_id>/. relative paths reject traversal, symlinks **and** secret Carriers.
- confirmed Workflow, Step and Action events use the one existing Project Events Journal. The selected routes use CA-D-527/528/529's shared selected-Run contract and schema-v5 events; existing Base Revise v4 Journal support remains admitted. Full selected reports use `tmp/<Workflow Summary>/<run_id>.md` and safe result/effect references; Base Revise retains its existing report path.
- the additional strictly tagged `enqueue_selected` request carries `run_id` and `execution` containing CA-D-527's strict `execute` request. Its requested Workflow Run identity must match `run_id`. Its one canonical `definition_manifest` admits exactly fifteen routes: the original thirteen retain CA-A-1142@2 as their unchanged registry authority; `find_and_fetch_artifacts` and `find_and_fetch_journal_events` are admitted only through that same manifest's explicit `query_source_admissions`, pinned to accepted CA-P-1532@2 and CA-P-1535@2. CA-P-1543@2 is the external MCP source-review gate, not a query-source admission pin. This admission creates no second registry, executor, Agent contract or effect schema. Its definition/currentness, sealed Initiative and explicit current route-bound Operator authorization are validated before queue dispatch, then revalidated at dispatch. The two query routes have no mutation authority and retain the tagged request, shared selected-Run recording and canonical-manifest currentness checks. Before a Journal query records its own Run or Action start evidence, its adapter has captured CA-O-163's sealed canonical Journal byte-prefix; queued or worker-side recording cannot enter or enlarge that source frontier. Queued acknowledgment is not execution or Journal completion. This source-only contract amendment neither publishes a runtime route nor accepts query execution.
- the existing DBOS worker persists the exact frozen selected request, source bindings, dispatch intent, accepted result and report references under the same Run directory. Selected dispatch invokes the admitted Workflow graph and real Step/Action adapters through the shared Run library, not a second independent Workflow policy. An uncertain post-intent dispatch ends with retained recovery evidence, never automatic effect replay.
- CLI supports `enqueue`, `enqueue_selected`, `status`, `worker` and `start-worker`. `start-worker` explicitly launches a detached local worker; MCP exposes `workflow_orchestrator` for these admitted enqueue variants and status, and does not start workers implicitly. Status/result observation after client disconnect uses actual durable scheduler and result state and returns the selected Workflow identity, Run/report/Journal references and truthful pending/failure disposition. Existing Base Revise clients remain compatible.
- Agent output carries report_json, candidate_content **and** confidence; queued requests bind the selected sources, rules, Workflow definition, prompts **and** implementation fingerprint.
- the retained Base Revise request bounds are unchanged: Agent timeout 600 seconds, source limit 8 MiB and selection limit 10000. Confidence values follow current applicable settings/Operator overrides. The selected execution variant uses its reviewed route's applicable settings and strict bounds rather than inheriting Base Revise selection or permission fields implicitly.
- permission defaults: allow_fixes=false **and** allow_replacements=false. allow_replacements=true requires allow_fixes=true **and** delegates Summary-changing replacement of selected Atoms.
- `replacement.json` carries reserved predecessor/successor IDs, original **and** destination hashes, complete destination bytes, sealed lifecycle Events **and** confirmed receipts. replacement reports carry `replacement` with predecessor_atom_id, successor_atom_id, before, archived, successor **and** journal_receipts; the result is replaced_not_rechecked.
- same-identity edits retain Summary **and** identity. replacements use the successor's carried Properties **and** Summary for its filename; the predecessor's archive basename retains its assigned ID **and** Version.
