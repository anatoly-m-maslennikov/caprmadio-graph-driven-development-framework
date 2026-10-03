---
cce_version: cce_1
cce_form: obligation
subjects:
  - method
  - evaluation
  - delivery
  - provenance
  - tool-authority
version: 1
updated_at: 2026-08-23 16:50:00 +0400
autonomous_confidence_threshold: 98
---
# Replace stale PROGRAMMATIC Methods, Evaluations, and Deliveries

WHEN CA-P-068 is Done, THE Assignee MUST replace or revise every active Method, Evaluation, and Delivery Atom owned by PROGRAMMATIC or a registered descendant Scope Unit whose Claim, carrier relation, Evaluation target, or Delivery topology is stale against the current Requirement frontier.

## Scope

`(ALL Atoms WHERE (Current Scope IN (PROGRAMMATIC, APPS, MCP, TOOLS, GRAPH_APP, AGENT_HOST_PLUGINS, CODEX_PLUGIN, TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, IMPLEMENTATION_INVENTORY, ADOPT_RECONCILE, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, ATOM_SEARCH, ATOM_READ, ATOM_CREATE, ATOM_UPDATE, ATOM_MOVE, ATOM_ARCHIVE, ATOM_PROMOTE, ATOM_UPGRADE, MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, CLOSE_ATOM, REPLACE_ATOM) AND Lifecycle State = active AND Content Role IN (METHOD, EVALUATION, DELIVERY)))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-068 is not Done OR ANY frozen active MED carrier refers to a replaced Requirement identity OR ANY active MED Claim retains the superseded sidecar-coupled real-change commit topology or superseded direct Atom-Doer apply behavior OR CA-M-143 retains the unsupported same-scope equal-Core `child_of` relation OR ANY changed carrier lacks its exact predecessor revision and updated successor OR the frozen scope, successor rebinding result, Evaluation coverage map, deferred coverage handoff, and final Validation Set are not recorded).

## Details

Preserve accepted Method, Evaluation, and Delivery meaning when it remains current. Rebind direct Requirement references only to the exact CA-P-068 successors. Treat Git and Journal provenance as independent evidence systems: a real-change commit contains only its sealed target change, and a Journal-only batch is a separate gate item. Align Atom Doers with CA-R-1093: direct execution is dry-run only and `--apply` requires authorized project-local MCP delegation with a sealed Initiative action. Do not modify native Implementation or the separate CA-P-061/CA-P-070 through CA-P-075 workstream.
