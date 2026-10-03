---
cce_version: cce_1
cce_form: obligation
subjects:
  - authority
  - relation-model
  - local-tier
version: 1
updated_at: 2026-08-23 14:31:42
autonomous_confidence_threshold: 98
---
# Remove cross-scope Tier-parent relations

WHEN CA-P-064 is Done, THE Assignee MUST make every active PROGRAMMATIC RMED Atom use Tier-parent relations only within its own Current Scope.

## Scope

`(ALL Atoms WHERE (Current Scope IN (PROGRAMMATIC, APPS, MCP, TOOLS, GRAPH_APP, AGENT_HOST_PLUGINS, CODEX_PLUGIN, TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, IMPLEMENTATION_INVENTORY, ADOPT_RECONCILE, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, ATOM_SEARCH, ATOM_READ, ATOM_CREATE, ATOM_UPDATE, ATOM_MOVE, ATOM_ARCHIVE, ATOM_PROMOTE, ATOM_UPGRADE, MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, CLOSE_ATOM, REPLACE_ATOM) AND Lifecycle State = active AND Content Role IN (REQUIREMENT, METHOD, EVALUATION, DELIVERY)))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-064 is not Done OR ANY active Atom in Task Scope has a Tier-parent relation whose source and target have different Current Scopes OR ANY removed Tier-parent relation is replaced by another cross-scope authority relation OR ANY required non-Tier structural or semantic relation is lost OR the exact Task Scope Resolution and relation-validation result are not recorded).

## Details

Apply the current distinction between same-scope Tier authority, structural ownership, and cross-unit semantic flow. Do not use `child_of` or another Tier-parent relation to connect different Scope Units.
