---
subjects:
  governs: "Project-Owned Markdown Atom Carrier/Filename"
  depends_on:
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Atom/Scope"
version: 13
updated_at: "2026-10-02 18:57:51 +0400"
relations: {}
atom_id: "CA-D-283"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-283-CORE_META_MODEL-DELIVERY--serialize-project-owned-markdown-atom-filenames.md
---
# Summary

Serialize Project-Owned Markdown Atom Filenames

## Scope

Identified Project-owned Markdown Atom filenames other than Plan filenames governed by CA-D-469.

## Claim

**every** identified Project-owned Markdown Atom filename other than a Plan filename governed by CA-D-469 **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<LOCAL_TIER>][-<ATOM_TYPE>][-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. serialize the `ATOM_TYPE` segment **only** **when** the Atom carries a Type under CA-D-276; an omitted Type has no filename segment. **every** same-identity Atom Revision **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.

## Details
