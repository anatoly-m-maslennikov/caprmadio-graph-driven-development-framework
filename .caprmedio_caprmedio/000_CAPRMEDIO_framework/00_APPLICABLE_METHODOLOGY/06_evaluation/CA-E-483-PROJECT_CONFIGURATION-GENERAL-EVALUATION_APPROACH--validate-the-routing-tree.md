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
