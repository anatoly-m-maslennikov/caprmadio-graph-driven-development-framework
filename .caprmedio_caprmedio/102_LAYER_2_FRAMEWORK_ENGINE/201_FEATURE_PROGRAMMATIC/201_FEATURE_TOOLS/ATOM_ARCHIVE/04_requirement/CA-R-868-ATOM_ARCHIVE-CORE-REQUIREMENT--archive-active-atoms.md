---
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on:
    - "Atom"
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 11
updated_at: "2026-09-17 02:57:30 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
---
# Archive active Atoms

the ATOM_ARCHIVE Tool **must** provide withdrawal of active Markdown Atom authority while preserving its exact historical evidence:

- preserve Carrier bytes, stable Atom ID, Version, prior Revision history, **and** resolvable historical dependents **without** retaining current authority. archival is **not** promotion **or** upgrade.
- use the applicable archive Carrier encoding **and** placement under CA-D-289 **and** CA-D-303. unchanged content **and** identity do **not** require retaining the active filename.
- reject Drafts, already archived Atoms, non-Atom Markdown, invalid destinations, **and** collisions **before** applying a complete validated selection.
- support **`=1`** exact target **or** a frozen bulk set of **`>=2`** targets with expected Revisions **or** digests. apply the complete set atomically; restore **every** selected source **and** destination on an apply **or** postcondition failure.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

the operational Action is CA-O-029. CA-E-306 supplies the automated conformance cases for this capability; the Tool Requirement does **not** duplicate their procedure.
