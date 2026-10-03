---
subjects:
  declared:
    continuant:
      - tool-authority
  prerequisite:
    continuant:
      - artifact-operations
      - mcp
cce_version: cce_1
cce_form: obligation
version: 2
updated_at: 2026-08-23 16:16:20 +0400
---
# Separate generic and Atom-specific Tool authority

Each public Tool operation MUST have exactly one semantic behavior owner. A generic Artifact Tool owns only artifact-form-agnostic carrier mechanics and contracts. It MUST NOT define CAPRMEDIO Markdown Atom identity, admission, authority, lifecycle-transition, or target-effect semantics. A CAPRMEDIO Markdown Atom Tool owns those semantics for its named Atom operation and MAY use a generic Artifact Tool only as an internal helper.

MCP owns discovery, projection, transport validation, request forwarding, and result transport. It MUST delegate to the canonical Tool and MUST NOT resolve an Atom target, reinterpret a Tool contract, decide a mutation, mutate a carrier, or recover an effect. A CAPRMEDIO Markdown Atom Doer's `--apply` entry point is callable only through an authorized project-local MCP delegation; direct execution MAY produce a mutation-free dry run but MUST reject `--apply`.

Finders, including `ATOM_SEARCH` and `ATOM_READ`, are strictly read-only. Doers default to dry run and require explicit `--apply`. Each Atom Doer accepts exactly one resolved target for an atomic action or a frozen set of two or more resolved targets for a bulk action; a bulk action preflights every target and either applies all targets or none.

`ATOM_ARCHIVE`, `ATOM_PROMOTE`, and `ATOM_UPGRADE` are distinct transitions. Archive preserves the assigned Atom ID and historical carrier. Promotion assigns an operator-supplied role-matching Atom ID to a draft and makes it active. Upgrade preserves an active Atom ID, requires an explicit enabled target Tier of `core` or `standard` that is higher than the source Tier, and MAY move the Atom only to an explicitly named ancestor Scope Unit.
