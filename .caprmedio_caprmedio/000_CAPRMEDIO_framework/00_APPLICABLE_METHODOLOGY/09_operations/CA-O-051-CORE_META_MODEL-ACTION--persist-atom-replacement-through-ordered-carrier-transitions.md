---
subjects:
  governs: "Persist Atom Replacement"
  depends_on:
    - "Action"
    - "Atom"
    - "Artifact/Revision"
    - "Atom/Carrier"
    - "Journal"
    - "Artifact/Revision/Archive Carrier Basename"
version: 6
updated_at: "2026-09-28 06:30:40 +0400"
relations: {relates_to: [CA-R-1432, CA-R-807]}
atom_id: "CA-O-051"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-051-CORE_META_MODEL-ACTION--persist-atom-replacement-through-ordered-carrier-transitions.md
---
# Persist Atom replacement through ordered Carrier transitions

Persist Atom Replacement **means** the reusable Action that persists **`=1`** accepted Atom replacement through its successor activation **and** predecessor archival under CA-R-1432 **and** CA-R-807. its boundary is this replacement transition; it does **not** select **or** authorize the replacement. the execution **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. preserve the predecessor's body, Summary, identity, Version, **and** every frontmatter value except its lifecycle `status` **and** `updated_at`; serialize `status: Archived` **and** refresh `updated_at` to the actual archive time. change its basename **only** by adding the canonical `@<version>` Archive suffix under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.
