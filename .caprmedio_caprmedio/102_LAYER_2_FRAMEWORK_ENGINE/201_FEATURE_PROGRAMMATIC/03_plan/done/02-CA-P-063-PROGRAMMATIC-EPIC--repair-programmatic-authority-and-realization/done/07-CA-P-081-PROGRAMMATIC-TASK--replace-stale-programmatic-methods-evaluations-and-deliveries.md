---
cce_version: cce_1
cce_form: obligation
subjects:
  - method
  - evaluation
  - delivery
  - provenance
  - tool-authority
version: 2
updated_at: 2026-08-23 17:00:00 +0400
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

## Task Scope Resolution

CA-P-068 is Done. The frozen input set at `2026-08-23 16:29:00 +0400` was 230 active PROGRAMMATIC MED Atoms: 22 Methods, 169 Evaluations, and 39 Deliveries. The set covers PROGRAMMATIC and its registered descendant Scope Units named in this Task's Scope.

This carrier is the identity-corrected record of user-ordered Task 7. `CA-P-069` was already allocated to the BSEED-superlayer task; this Task does not claim completion of that BSEED work.

## Execution Result

The reconciliation rebound 101 direct references to the exact CA-P-068 Requirement successors: 7 from `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520` to `CA-R-1124`, 2 from `...REQU-522` to `CA-R-1126`, 29 from `...REQU-534` to `CA-R-1136`, and 63 from `...REQU-535` to `CA-R-1137`. Each revision preserves its exact immediate predecessor in its local archive.

27 current MED carriers were revised for the independent Git/Journal provenance topology or the CA-R-1093 Atom-Doer/MCP authority boundary. Two Evaluation carrier summaries were renamed to remove the obsolete sidecar-coupled topology. `CA-M-143` was revised to remove its unsupported same-scope equal-Core `child_of: CA-M-142` relation without adding a replacement semantic claim.

## Evaluation Coverage Map and Deferred Handoff

Direct current-Evaluation coverage is 29 of 102 current Requirements: `CA-R-803`, `CA-R-804`, `CA-R-805`, `CA-R-812`, `CA-R-856`, `CA-R-857`, `CA-R-1041`, `CA-R-1042`, `CA-R-1048`, `CA-R-1049`, `CA-R-1059` through `CA-R-1070`, `CA-R-1076`, `CA-R-1077`, `CA-R-1093`, `CA-R-1121`, `CA-R-1126`, `CA-R-1136`, and `CA-R-1137`.

The remaining 73 explicit acceptance-boundary gaps are handed off unchanged to CA-P-061 and CA-P-070 through CA-P-075: `CA-R-802`; `CA-R-863` through `CA-R-870`; `CA-R-1071` through `CA-R-1075`; `CA-R-1094` through `CA-R-1120`; `CA-R-1122` through `CA-R-1125`; `CA-R-1127` through `CA-R-1135`; and `CA-R-1138` through `CA-R-1156`. This Task does not invent Evaluation Atoms outside that separate workstream.

## Validation Result

`validate_ca_p081.py` passed against the final active set: 230 active MED carriers, 63 CA-P-068 mappings, zero stale predecessor references, 101 preserved predecessor archive carriers for those mappings, 27 lifecycle-preserved semantic revisions, zero unresolved active relation targets, and no forbidden sidecar-coupled/direct-apply claims. The check also confirms the 29/73 Evaluation coverage map above.
