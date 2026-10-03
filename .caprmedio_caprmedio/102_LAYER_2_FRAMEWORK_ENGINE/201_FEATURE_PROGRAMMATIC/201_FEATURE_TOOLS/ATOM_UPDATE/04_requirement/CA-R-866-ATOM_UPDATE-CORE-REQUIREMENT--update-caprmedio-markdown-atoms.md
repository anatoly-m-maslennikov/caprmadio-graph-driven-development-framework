---
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on:
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-17 02:59:41 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
---
# Update CAPRMEDIO Markdown Atoms

the ATOM_UPDATE Tool **must** provide same-identity updates of the frontmatter, content, **or** both for exact selected Markdown Atoms:

- preserve the Carrier path, filename, Atom identity, **and** Summary. do **not** assign an ID **to** an unassigned Draft merely **to** update its Carrier. a Summary change requires replacement under CA-R-1464, **not** a same-ID update.
- advance **`=1`** Version per changed Atom, preserve its exact prior Revision, **and** follow the applicable Updated At rule. formatting-only **and** lossless-serialization changes retain Updated At under CA-R-1492.
- reject duplicate, missing, ambiguous, invalid, **or** stale targets; preflight the complete operation.
- support **`=1`** exact target **or** a frozen bulk set of **`>=2`** targets with expected Revisions **or** digests. apply the complete validated set atomically **and** restore the mutable transaction frontier on apply **or** postcondition failure.
- permit reuse of generic metadata **or** Relation-patch mechanics while retaining responsibility for Atom authority validation, Revision, transaction, **and** effect semantics.
- default **to** mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

CA-O-030 defines the operational Action. CA-E-304 supplies its automated conformance cases **without** duplicating them **in** this capability Requirement.
