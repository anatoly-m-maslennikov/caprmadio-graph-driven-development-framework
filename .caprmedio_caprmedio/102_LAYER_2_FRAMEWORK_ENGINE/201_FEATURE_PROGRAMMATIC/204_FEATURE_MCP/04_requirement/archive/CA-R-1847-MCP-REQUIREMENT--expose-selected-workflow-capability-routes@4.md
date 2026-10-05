---
atom_id: CA-R-1847
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-05 02:00:00 +0400"
subjects:
  governs: "MCP/selected Workflow capability routes"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1720, CA-R-1525, CA-R-1728, CA-P-1484]
---
# Summary

Expose selected Workflow capability routes

## Scope

The Project-local MCP adapter surface for the original thirteen Operator-selected
P1117 capabilities plus the two explicitly admitted read-only P1520 query
Workflows, with their standalone/nested Action and Run observations.

## Claim

MCP **must** expose exactly the selected capability adapters below through the existing reloadable Project-local server, while delegating execution and every-Run recording to the shared `WORKFLOW_OPERATIONS/RUN_SUPPORT` service.

## Details

The public route names are `create_atom`, `update_atom`, `replace_atom`,
`change_atom_status`, `create_scope_unit`, `rename_scope_unit`,
`move_scope_unit`, `remove_scope_unit`, `run_implementation_workflow`,
`revert_changes`, `build_entities_graph`, `build_terms_graph`,
`build_applicable_methodology`, `find_and_fetch_artifacts`, and
`find_and_fetch_journal_events`. Their one selected-definition binding is the
derived fifteen-route Projection
`.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`. It carries
every route's full current source Workflow, ordered Steps, ordered Action
bindings, and only source-closed native Action calls with exact source path,
Version, and SHA-256 digest. It is an immutable derived projection, not another
Workflow graph or source authority.

The original thirteen entries retain CA-A-1142 v2 as their unchanged selected
source registry and retain its closed source policies. The two query entries
are admitted only by `query_source_admissions` in that same canonical manifest;
that field contains exactly these current acceptance-frontier pins and their
corresponding Workflow/Action/Step pins:

- `find_and_fetch_artifacts`: CA-P-1532@2 at
  `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/12-CA-P-1532-TASK--independently-accept-repaired-artifact-query-source.md`, SHA-256 `b1474e81cafa4f55d2b3bd92f930293c8ff65d5bf6abd2cefb21efd605f8d432`; CA-O-158@2 `2424aa7475d2e7f98006040dc0d5826702e641190c6535a834869c1fe5a7e536`, CA-O-159@2 `3fd33badbff039e58c1c0b31dfbf3608c37a58d779a1b3ebc14d7bb5ee27dc08`, and CA-O-160@2 `a743a84fd24db32123ac8162e7a2178e6d83b1b727cbe54477b6020914537384` at their accepted P1532 paths.
- `find_and_fetch_journal_events`: CA-P-1535@2 at
  `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md`, SHA-256 `6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc`; CA-O-161@2 `362b9d3848a796a14e7374cfa0bf0b561c4f2035b7b2bf87bd9b56fc97a6724d`, CA-O-162@2 `71301ecf9531c70adeba03d6cf7f39761a237a081cee43eb0f9f7ce40e12f9fe`, and CA-O-163@2 `8d0238a1614f5888f2aa486038d271cc58db1d3f0d7014dece0baa53004a489c` at their accepted P1535 paths.

The two acceptance pins are explicit admission evidence, not a second registry,
authority, manifest, parser, or executor. Missing, malformed, incomplete,
duplicate, digest-mismatched, or stale bindings or admissions reject the route
before shared support, worker start, Run creation, Action Run creation, effect,
or Journal event.

Every route delegates one normalized CA-D-527 v3 request to shared
`run_selected_operation(request)`: request/route identity, typed
input/parameters, target-frontier and effects digests, caller-chosen
idempotency/retry key, optional real parent lineage, explicit current sealed
Initiative authorization for mutations, and exactly one outer
`definition_manifest` (`manifest_ref`, `manifest_digest`). That outer object is
the sole canonical manifest binding. `source_freshness` carries only current
selected-source registry/binding evidence; `definition_manifest_ref`,
`definition_manifest_digest`, or any other manifest ref/digest supplied there
or elsewhere are unknown shadow fields and are rejected, including if their
digest differs. It returns only the shared `RunResult`: real Run/definition IDs,
outcome, safe result/effect/report/output refs, canonical Journal recording
state/event refs, source currentness, and diagnostics. `mode` defaults to
`preview`; preview creates no Run, Action Run, Event, mutation authority, or
Journal write. Only explicit `execute` may start work. A mutation-capable route
also requires its exact current Operator authorization. An admitted read-only
query may execute only with its exact current query-source admission, canonical
manifest, and explicit `execute` request; it gains no mutation authority. Its
actual Run/Action Run recording remains shared support's responsibility. No
`apply` mode exists.

Before shared support admits `find_and_fetch_journal_events`, the adapter must
capture and bind CA-O-163's sealed canonical Journal byte-prefix snapshot. The
actual Workflow/Action Run records are appended only after that capture and
cannot enter, enlarge, or replay the query result. Both query routes reuse the
one CA-R-1850 closed literal grammar and never accept SQL, code, arbitrary
expressions, secrets, or a second parser.

`get_selected_workflow_run` and `get_selected_action_run` read only one exact Run/Action Run and return its status, safe output/result/effect references, lineage, source currentness, and canonical event/receipt references. `recover_selected_run_recording` accepts only a pending shared-recording event reference and retries persistence with the same event identity and payload; it never replays an Action or Workflow. MCP must not implement a parallel request schema or execution path.

The adapters reuse the server's existing Project-root/stdin binding, discovery helpers, `workflow_orchestrator`, and hot-reload gateway. CA-D-521 v3's existing DBOS `enqueue_selected` variant remains the general selected-dispatch variant; MCP supplies the admitted request to that existing APP and does not create another executor. The adapters add no alternate root, shell, arbitrary path, generic mutation, implicit dispatch, Journal writer, or duplicate business behavior. The existing eight helper names and their contracts remain available. Route annotations truthfully describe preview/execute behavior and do not override client permission policy.

### Sources

- CA-A-1142 v2, unchanged original-thirteen registry; CA-P-1532 v2 and CA-P-1535 v2, the exact two query admission frontiers; CA-P-1117 v7 shared Run obligation.
- CA-D-527 v3; CA-D-521 v3; CA-D-548 v2; CA-R-1720 v17; CA-R-1525 v6; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v2; CA-R-1867 v1.
