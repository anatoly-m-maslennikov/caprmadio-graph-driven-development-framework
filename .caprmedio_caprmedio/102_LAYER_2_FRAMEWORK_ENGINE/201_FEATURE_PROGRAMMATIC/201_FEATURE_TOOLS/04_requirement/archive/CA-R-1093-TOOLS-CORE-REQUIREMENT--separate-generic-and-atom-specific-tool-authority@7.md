---
subjects:
  governs: "tool-authority"
  depends_on:
    - "artifact-operations"
    - "mcp"
cce_version: cce_1
cce_form: obligation
version: 7
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate generic and Atom-specific Tool authority

Each public Tool operation **must** have exactly one semantic behavior owner. A generic Artifact Tool owns **only** artifact-form-agnostic carrier mechanics **and** contracts. It **must not** define CAPRMEDIO Markdown Atom identity, admission, authority, lifecycle-transition, **or** target-effect semantics. A CAPRMEDIO Markdown Atom Tool owns those semantics for its named Atom operation **and** **may** use a generic Artifact Tool **only** as an internal helper.

MCP owns discovery, projection, transport validation, request forwarding, **and** result transport. It **must** delegate **to** the canonical Tool **and** **must not** resolve an Atom target, reinterpret a Tool contract, decide a mutation, mutate a carrier, **or** recover an effect. A CAPRMEDIO Markdown Atom Doer's `--apply` entry point is callable **only** through an authorized project-local MCP delegation; direct execution **may** produce a mutation-free dry run but **must** reject `--apply`.

Finders, including `ATOM_SEARCH` **and** `ATOM_READ`, are strictly read-only. Doers default **to** dry run **and** require explicit `--apply`. Each Atom Doer accepts exactly one resolved target for an atomic action **or** a frozen set of two **or** more resolved targets for a bulk action; a bulk action preflights **every** target **and** either applies **all** targets **or** **none**.

`ATOM_ARCHIVE`, `ATOM_PROMOTE`, **and** `ATOM_UPGRADE` are distinct transitions. Archive preserves the assigned Atom ID **and** historical carrier. Promotion assigns an operator-supplied role-matching Atom ID **to** a draft **and** makes it active. Upgrade preserves an active Atom ID, requires an explicit enabled target Tier of `core` **or** `standard` that is higher than the source Tier, **and** **may** move the Atom **only** **to** an explicitly named ancestor Scope Unit.
