---
subjects:
  governs: "CAPRMEDIO Routing Tree"
  depends_on: []
version: 6
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for":["CA-R-1640"]}
atom_id: "CA-E-483"
content_role: "Evaluation"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/06_evaluation/CA-E-483-PROJECT_CONFIGURATION-GENERAL-EVALUATION_APPROACH--validate-the-routing-tree.md
  source_atom_id: CA-E-483
  source_atom_revision: 6
  source_sha256: aacc1f70871357084c8594e2b06d4ebcf85a26fc4e1ecfe87fcb5bc108ae8d6e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate the routing tree

## Scope

the CAPRMEDIO Routing Tree.

## Claim

the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-CORE-REQUIREMENT--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:

## Details

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
