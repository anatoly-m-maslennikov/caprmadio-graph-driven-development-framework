---
subjects:
  governs: "project-containment graph"
  depends_on:
    - "Primary Entity"
    - "Artifact"
    - "Structural Entity"
version: 16
updated_at: "2026-10-02 20:52:00 +0400"
relations:
  child_of:
    - CA-R-834-CORE_META_MODEL-CORE-REQUIREMENT--partition-project-graph-nodes
atom_id: "CA-R-836"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-836-CORE_META_MODEL-GENERAL-REQUIREMENT--encode-project-graph-node-partitions.md
  source_atom_id: CA-R-836
  source_atom_revision: 16
  source_sha256: 4cf8a0db9a87b23f6315ded79a33e8a4c746e205f012ed37e70b02da4d05faae
  original_relations_sha256: 4ed3b58e7782f7823940ffd5344ce09aa90541e3c48e227e7f7b8c768af35893
---
# Summary

Encode project-graph node partitions

## Scope

governed project-containment graph nodes.

## Claim

the project-containment graph **must** derive **`=1`** partition for **every** governed Primary Entity node from its Artifact **or** Structural Entity classification **and** reject a node whose partition count is **`!=1`**.

## Details
