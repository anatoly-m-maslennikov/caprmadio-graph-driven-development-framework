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
version: 4
updated_at: "2026-09-17 05:03:20 +0000"
relations: {relates_to: [CA-R-1432, CA-R-807]}
atom_id: "CA-O-051"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
---
# Persist Atom replacement through ordered Carrier transitions

Persist Atom Replacement **means** the reusable Action that persists **`=1`** accepted Atom replacement through its successor activation **and** predecessor archival under CA-R-1432 **and** CA-R-807. its boundary is this replacement transition; it does **not** select **or** authorize the replacement. the execution **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. preserve the predecessor's content, identity, frontmatter, **and** Version exactly; change its basename **only** by adding the canonical `@<version>` Archive suffix under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.
