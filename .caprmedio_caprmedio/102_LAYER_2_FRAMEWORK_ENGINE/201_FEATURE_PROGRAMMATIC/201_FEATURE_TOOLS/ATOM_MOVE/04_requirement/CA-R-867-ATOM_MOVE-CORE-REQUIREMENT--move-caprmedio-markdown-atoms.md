---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 13
updated_at: 2026-09-04 03:10:59 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Move CAPRMEDIO Markdown Atoms

the `ATOM_MOVE` Tool is the canonical Doer for moving CAPRMEDIO Markdown Atom carriers between content-role locations **in** the configured Project control root while preserving their bytes, filenames, **and** Atom IDs. it **must** support exact selectors **and** recursive source-subtree selection, preserve the selected subtree by default, flatten **only** **when** explicitly requested, reject collisions **and** invalid destinations, **and** preflight the complete operation. an atomic action moves **=1** Atom; a bulk action freezes two **or** more Atom targets with their expected revisions **or** digests **and** is all-or-nothing. it **may** use generic rename mechanics but owns Atom placement, identity-preservation, transaction, **and** effect semantics. it **must** default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

automated tests **must** prove singular **and** bulk moves, default subtree preservation, explicit flattening, byte **and** identity preservation, collision **and** destination rejection, mutation-free dry run, MCP-gated apply, **and** restoration of **every** source **and** destination **after** an apply failure.
