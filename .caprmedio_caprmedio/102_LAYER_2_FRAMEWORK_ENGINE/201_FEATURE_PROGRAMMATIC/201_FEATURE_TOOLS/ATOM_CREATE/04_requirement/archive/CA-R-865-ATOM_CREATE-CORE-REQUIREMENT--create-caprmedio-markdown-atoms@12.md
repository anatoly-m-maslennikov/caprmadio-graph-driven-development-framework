---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool/ATOM_CREATE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 12
updated_at: "2026-09-17 03:12:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Create CAPRMEDIO Markdown Atoms

the ATOM_CREATE Tool **must** provide admission **and** creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations:

- accept a complete path **or** a directory **and** filename with frontmatter **and** content; enforce applicable placement, filename, metadata, **and** initial Revision authority.
- reject destination collisions **and** reused assigned Atom IDs, including IDs retained **only** **in** historical authority. identity admission follows CA-R-732; an unassigned Draft does **not** acquire an invented ID.
- support **=1** Carrier **or** a frozen bulk set of **>=2** Carriers. preflight the complete set **and** publish it all-or-nothing; a failed preflight **or** apply **must not** leave partial creation.
- permit generic Carrier-construction mechanics while retaining responsibility for Atom admission, identity, Revision, transaction, **and** effect semantics.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

CA-O-032 defines the operational Action; CA-E-303 supplies its automated conformance cases. exact Carrier syntax remains governed by Delivery authority rather than duplicated here.
