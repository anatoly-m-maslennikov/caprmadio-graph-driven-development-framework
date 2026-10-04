---
atom_id: CA-R-866
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: ["Atom", "Atom/Revision", "Atom/Summary", "Artifact/Carrier", "Atom Change Classification", "Atom/Revision/Updated At"]
version: 12
updated_at: "2026-10-04 17:35:27 +0000"
relations:
  relates_to: [CA-O-030, CA-E-304, CA-O-067, CA-R-1432, CA-R-1788, CA-R-1464, CA-R-1415, CA-R-1371]
---
# Summary

Update CAPRMEDIO Markdown Atoms

## Scope

Same-identity updates of exact selected Markdown Atom Carriers by the ATOM_UPDATE Tool.

## Claim

the ATOM_UPDATE Tool **must** provide same-identity updates of the frontmatter, content, **or** both for exact selected Markdown Atoms:

- preserve the Carrier path, filename, Atom identity, **and** Summary. do **not** assign an ID **to** an unassigned Draft merely **to** update its Carrier. a Summary change requires replacement under CA-R-1464, **not** a same-ID update.
- resolve the admitted change class against the exact current Revision **and** proposal under CA-R-1432, reusing the current identity assessment under CA-O-067 where applicable. `carrier_only` **and** equivalent `refinement` retain Version; `semantic_revision` advances **`=1`** Version **and** preserves the exact prior semantic Revision under CA-R-1415 **and** CA-R-1371. replacement-required **or** uncertain classification must stop this update rather than silently changing identity **or** assuming permission.
- refresh Updated At **to** the actual accepted edit instant under CA-R-1788 for **every** accepted edit, including formatting-only **and** lossless-serialization edits. an actual no-op creates no fictitious edit, Version, timestamp refresh **or** archive effect; retain its truthful result for the governing Run contract.
- reject duplicate, missing, ambiguous, invalid, **or** stale targets; preflight the complete operation.
- support **`=1`** exact target **or** a frozen bulk set of **`>=2`** targets with expected Revisions **or** digests. apply the complete validated set atomically **and** restore the mutable transaction frontier on apply **or** postcondition failure.
- permit reuse of generic metadata **or** Relation-patch mechanics while retaining responsibility for Atom authority validation, admitted change class, Revision, transaction, **and** effect semantics.
- default **to** mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

CA-O-030 defines the operational Action. CA-E-304 supplies its automated conformance cases **without** duplicating them **in** this capability Requirement.

## Details
