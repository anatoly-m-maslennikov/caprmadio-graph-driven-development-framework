---
cce_version: cce_1
cce_form: obligation
subjects:
  - tool-authority
  - atom-operations
  - mcp
version: 1
updated_at: 2026-08-23 14:31:42
autonomous_confidence_threshold: 98
---
# Consolidate generic and Atom-specific Tool authority

WHEN CA-P-066 is Done, THE Assignee MUST establish one non-duplicative authority boundary between generic PROGRAMMATIC Tools, Atom-specific Tools, and MCP exposure.

## Scope

`(ALL Atoms WHERE (Current Scope IN (PROGRAMMATIC, MCP, TOOLS, TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, IMPLEMENTATION_INVENTORY, ADOPT_RECONCILE, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, ATOM_SEARCH, ATOM_READ, ATOM_CREATE, ATOM_UPDATE, ATOM_MOVE, ATOM_ARCHIVE, ATOM_PROMOTE, ATOM_UPGRADE, MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, CLOSE_ATOM, REPLACE_ATOM) AND Lifecycle State = active AND Content Role = REQUIREMENT))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-066 is not Done OR two active Tool Requirements independently own the same operation semantics OR MCP owns Tool behavior instead of exposing registered Tools OR generic artifact operations contradict CAPRMEDIO Markdown Atom operations OR archive, promote, and upgrade are conflated OR upgrade lacks an explicit target Tier OR singular and bulk operation contracts are incompatible OR the exact Task Scope Resolution and ownership matrix are not recorded).

## Details

Keep search and read mutation-free. Keep create, update, move, archive, promote, and upgrade as distinct Atom operation capabilities that accept singular or bulk target sets where valid. Promotion changes `draft` to `active`; upgrade requires an explicit higher target Tier and may also require a governed move to an upper Scope Unit.
