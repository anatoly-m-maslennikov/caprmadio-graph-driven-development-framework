---
atom_id: CA-R-865
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_CREATE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 14
updated_at: "2026-10-04 18:00:17 +0000"
relations: {}
---
# Summary

Create CAPRMEDIO Markdown Atoms

## Scope

ATOM_CREATE admission and creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations.

## Claim

the ATOM_CREATE Tool **must** provide admission **and** creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations:

- accept a complete path **or** a directory **and** filename with frontmatter **and** content; enforce applicable placement, filename, metadata, **and** initial Revision authority.
- reject destination collisions **and** reused assigned Atom IDs, including IDs retained **only** **in** historical authority. identity admission follows CA-D-508; an unassigned Draft does **not** acquire an invented ID.
- support **`=1`** Carrier **or** a frozen bulk set of **`>=2`** Carriers. preflight the complete set **and** publish it all-or-nothing; a failed preflight **or** apply **must not** leave partial creation.
- permit generic Carrier-construction mechanics while retaining responsibility for Atom admission, identity, Revision, transaction, **and** effect semantics.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

## Details

CA-O-032 defines the operational Action; CA-E-303 supplies its automated conformance cases. exact Carrier syntax remains governed by Delivery authority rather than duplicated here.
