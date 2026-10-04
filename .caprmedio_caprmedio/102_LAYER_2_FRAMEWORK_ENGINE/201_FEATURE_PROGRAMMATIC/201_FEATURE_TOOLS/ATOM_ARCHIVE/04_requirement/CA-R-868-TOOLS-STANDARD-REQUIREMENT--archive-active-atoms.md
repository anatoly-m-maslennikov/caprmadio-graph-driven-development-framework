---
atom_id: CA-R-868
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on: ["Atom", "Atom/Revision", "Artifact/Carrier", "Atom/Revision/Status", "Atom/Revision/Updated At"]
version: 12
updated_at: "2026-10-04 17:35:27 +0000"
relations:
  relates_to: [CA-O-029, CA-E-306, CA-R-1521, CA-R-1788, CA-D-289, CA-D-303]
---
# Summary

Archive active Atoms

## Scope

The ATOM_ARCHIVE shortcut withdrawing exact selected active Markdown Atom authority under the Atom's applicable qualified status model and transition rules.

## Claim

the ATOM_ARCHIVE Tool **must** provide withdrawal of active Markdown Atom authority while preserving its historical evidence:

- preserve governed meaning, complete body, Summary, stable Atom ID, Version, prior Revision history, resolvable historical dependents **and** all other properties except the admitted lifecycle Status **and** actual Updated At changes. resolve the archive transition from the actual Atom Content Role/Type's applicable status model under CA-R-1521; set its admitted archival Status **and** refresh actual Updated At under CA-R-1788. exclude the withdrawn Revision from current authority; archival is **not** promotion, upgrade **or** a semantic Revision.
- use the applicable archive Carrier encoding **and** placement under CA-D-289 **and** CA-D-303. unchanged meaning **and** identity do **not** require retaining the active filename; the whole Carrier transition remains atomic.
- reject Drafts, already archived Atoms, non-Atom Markdown, missing **or** unsupported status/transition models, invalid destinations, **and** collisions **before** applying a complete validated selection. do **not** invent a universal lifecycle for other Entity **or** Artifact kinds.
- support **`=1`** exact target **or** a frozen bulk set of **`>=2`** targets with expected Revisions **or** digests. apply the complete set atomically; restore **every** selected source **and** destination on an apply **or** postcondition failure.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

the operational Action is CA-O-029. CA-E-306 supplies the automated conformance cases for this capability; the Tool Requirement does **not** duplicate their procedure.

## Details
