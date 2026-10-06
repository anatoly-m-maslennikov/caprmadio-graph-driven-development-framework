---
subjects:
  governs: "Atom/Revision/Updated At"
  depends_on:
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Entity"
    - "Atom/Revision/Status"
    - "Artifact/Carrier Placement"
version: 1
updated_at: "2026-10-03 03:47:16 +0400"
claim_target_scope_unit: "CORE_META_MODEL"
relations:
  child_of:
    - CA-R-1416
atom_id: "CA-R-1788"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1788-CORE_META_MODEL--refresh-updated-at-whenever-an-atom-changes.md
  source_atom_id: CA-R-1788
  source_atom_revision: 1
  source_sha256: 253278979269bbc4ce755a729f601409798ce309eaa035f03ee7a18d708373b6
  original_relations_sha256: 4847fb4582248044a24be63c7b8943ad429a2717d1a91a92e578a6a7656a08d0
---
# Summary

Refresh Updated At whenever an Atom changes

## Scope

accepted Markdown Atom Carrier edits.

## Claim

**every** accepted edit **to** an Atom Carrier **must** refresh that Atom Revision's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, Status, **or** archive-placement edit.

## Details

this requirement covers formatting, lossless representation, Entity-name, Status, **and** archive-placement edits. timestamp encoding follows `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`.
