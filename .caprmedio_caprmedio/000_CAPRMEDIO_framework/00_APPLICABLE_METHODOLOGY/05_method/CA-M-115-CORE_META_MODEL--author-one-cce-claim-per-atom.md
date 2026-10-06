---
subjects:
  governs: "Atom Claim Boundary Authoring"
  depends_on:
    - "Atom"
    - "Claim"
    - "Atom/Claim"
    - "CCE"
    - "Author"
    - "Scope Unit"
    - "Atom/Claim/Target Scope Unit"
    - "Relational Atom"
version: 23
updated_at: "2026-09-28 15:12:22 +0400"
relations: {}
atom_id: "CA-M-115"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-115-CORE_META_MODEL--author-one-cce-claim-per-atom.md
  source_atom_id: CA-M-115
  source_atom_revision: 23
  source_sha256: caf1459a6cce687b0e981e258783ed8efa417f289b6034623ddec7c6f6645dcc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Author one CCE Claim per Atom

## Scope

authoring the boundary of **`=1`** independently replaceable Atom contribution.

## Claim

**to** author an Atom, the Author **must** perform **all** of:

1. identify one statement whose complete effect **must** be accepted, replaced, **and** retired together.
2. split **every** independently replaceable component into another Atom.
3. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit. express applicability **in** the registered body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; for RMED, use Scope **and** write the Claim within that applicability; those restrictions alone do **not** make the Atom Relational.
4. write the complete Claim **in** the current CCE version.
5. remove **every** duplicate alternate authoritative statement.

## Details
