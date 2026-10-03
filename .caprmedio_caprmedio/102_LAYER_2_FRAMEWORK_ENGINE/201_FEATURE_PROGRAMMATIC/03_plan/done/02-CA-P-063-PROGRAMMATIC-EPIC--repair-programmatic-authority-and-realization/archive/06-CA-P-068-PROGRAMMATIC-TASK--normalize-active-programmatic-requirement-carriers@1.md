---
cce_version: cce_1
cce_form: obligation
subjects:
  - carrier-format
  - requirement-authority
  - artifact-identity
version: 1
updated_at: 2026-08-23 14:31:42
autonomous_confidence_threshold: 98
---
# Normalize active PROGRAMMATIC Requirement carriers

WHEN CA-P-067 is Done, THE Assignee MUST make every active Requirement Atom owned by PROGRAMMATIC or one of its descendant Scope Units conform to the current BSEED Atom, carrier, identity, Scope, Tier, Subject, and relation authority.

## Scope

`(ALL Atoms WHERE (Current Scope IN (PROGRAMMATIC, APPS, MCP, TOOLS, GRAPH_APP, AGENT_HOST_PLUGINS, CODEX_PLUGIN, TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, IMPLEMENTATION_INVENTORY, ADOPT_RECONCILE, COMMIT_TRIGGER, COMMIT_CONTEXT, APPEND_CHANGE_RECORDS, COMMIT_CHANGE_SET, INSTALL_TOOLS, START_BACKGROUND_SERVICES, ATOM_SEARCH, ATOM_READ, ATOM_CREATE, ATOM_UPDATE, ATOM_MOVE, ATOM_ARCHIVE, ATOM_PROMOTE, ATOM_UPGRADE, MIGRATE_ATOM_IDENTITY, REBIND_ATOM_RELATIONS, CLOSE_ATOM, REPLACE_ATOM) AND Lifecycle State = active AND Content Role = REQUIREMENT))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-067 is not Done OR ANY Atom in the final successor-inclusive Validation Set has a noncanonical carrier address OR duplicated derived frontmatter OR a missing or duplicated identity OR an invalid Current Scope, Type, or local Tier OR missing or invalid Subjects OR an unresolved or forbidden relation OR ANY changed Atom lacks required Revision and lifecycle history OR the frozen input Task Scope and final successor-inclusive Validation Set are not recorded).

## Details

Freeze the exact active Requirement set before mutation. Resolve legacy and duplicate identities explicitly, preserve every prior Revision required by lifecycle governance, and do not change accepted Requirement meaning except where Tasks CA-P-064 through CA-P-067 establish the required replacement or revision.
