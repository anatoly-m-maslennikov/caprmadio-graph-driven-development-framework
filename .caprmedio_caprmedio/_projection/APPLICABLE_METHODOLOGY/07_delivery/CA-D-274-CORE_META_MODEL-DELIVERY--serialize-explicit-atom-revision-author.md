---
subjects:
  governs: "Atom/Revision/Author/Frontmatter"
  depends_on:
    - "Operator"
    - "Project/Operator Registry"
version: 17
updated_at: "2026-10-02 18:57:51 +0400"
relations: {}
atom_id: "CA-D-274"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-274-CORE_META_MODEL-DELIVERY--serialize-explicit-atom-revision-author.md
  source_atom_id: CA-D-274
  source_atom_revision: 17
  source_sha256: db4a0f0b1952dfd28ddabce2cfb3db1f3c53618fbc1d1b33ddfc5259a32d7d54
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Explicit Atom Revision Author

## Scope

Markdown Atom Carriers.

## Claim

a Markdown Atom Carrier **must** serialize **`=1`** resolved Author as the top-level frontmatter Property `author`; apply the applicable Author default during authoring rather than leaving the accepted Revision dependent on an omitted Author.

- encode `author` as **=1** nonempty YAML string equal **to** a name **in** the Project's Operator registry under CA-D-494, **not** a list **or** a null value.
- validate Author by exact registry membership. an unlisted name fails membership; unavailable **or** invalid registry context leaves the check incomplete. do **not** require an additional Actor identity lookup **or** copy the registered role into Atom frontmatter.

## Details
