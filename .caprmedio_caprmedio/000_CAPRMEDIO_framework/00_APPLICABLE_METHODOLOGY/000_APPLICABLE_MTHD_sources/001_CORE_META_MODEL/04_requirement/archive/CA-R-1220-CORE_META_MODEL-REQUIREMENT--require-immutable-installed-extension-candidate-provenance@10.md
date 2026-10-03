---
subjects:
  governs: "Applicable Methodology/Sources/Installed Extensions/Catalog Entry"
  depends_on:
    - "Extension"
    - "Artifact/Revision"
version: 10
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
atom_id: "CA-R-1220"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 11
---
# Require Immutable Installed Extension Candidate Provenance

**every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.
